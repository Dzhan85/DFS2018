from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler
import os
import sys
import time, threading
import argparse

#os.system("apt-get install -y rsync")

parser = argparse.ArgumentParser()
#parser.add_argument('--secsrv', default="127.0.0.1")
parser.add_argument('--homedir', default="/ftpsrv/share/")
parser.add_argument('--user', default="user")
parser.add_argument('--passwd', default="12345")
args = parser.parse_args()

if not os.path.exists(args.homedir):
    os.makedirs(args.homedir)

# os.system("apt update")
# os.system("apt install -y rsync")

global ftphomedir
ftphomedir = args.homedir

global ftpsecsrv
ftpsecsrv = raw_input("Enter second server: ") #args.secsrv

global ftpuser
ftpuser = args.user

global ftppasswd
ftppasswd = args.passwd


def replication():
    threading.Timer(10, replication).start()
    os.system("rsync -czvrupotq '-e ssh' " + ftphomedir + " root@" + ftpsecsrv + ":" + ftphomedir)
    # print "replicated"


# replication()

class MyHandler(TLS_FTPHandler):
    #    def get_freesize()
    #        free_size = str(stinfo.f_bsize*stinfo.f_bavail/1024/1024)+" MB"
    #        return free_size

    stinfo = os.statvfs('/ftpsrv/share')
    banner = "Total free space is: " + str(
        stinfo.f_bsize * stinfo.f_bavail / 1024 / 1024) + " MB"  # "pyftpdlib %s ready." % __ver__

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)
        # os.system("rsync -czvrupotq '-e ssh' sdi@172.23.1.13:/home/sdi/ /home/sdi/")

    def on_disconnect(self):
        # do something when client disconnects
        os.system("rsync -czvrupotq '-e ssh' " + ftphomedir + " root@" + ftpsecsrv + ":" + ftphomedir)
        print "%s:%s disconnected"
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        os.remove(file)

    def on_delete(self, path):
        # os.system("path = sed 's:/[^/]*$::' path")
        path = path[:path.rfind('/')] + "/"
        os.system("rsync -czvrupotq --delete '-e ssh' " + path + " root@" + ftpsecsrv + ":" + path)
        # print "deleted %path %ftpsecsrv"
        pass

    def ftp_DELE(self, path):
        """Delete the specified file.
        On success return the file path, else None.
        """
        try:
            self.run_as_current_user(self.fs.remove, path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            self.respond('550 %s.' % why)
        else:
            self.respond("250 File removed.")
            self.on_delete(path)
            return path

    def ftp_RMD(self, path):
        """Remove the specified directory.
        On success return the directory path, else None.
        """
        if self.fs.realpath(path) == self.fs.realpath(self.fs.root):
            msg = "Can't remove root directory."
            self.respond("550 %s" % msg)
            return
        try:
            self.run_as_current_user(self.fs.rmdir, path)
        except (OSError, FilesystemError) as err:
            why = _strerror(err)
            self.respond('550 %s.' % why)
        else:
            self.on_delete(path)
            self.respond("250 Directory removed.")
 
def main():
    replication()
    authorizer = DummyAuthorizer()
    authorizer.add_user(ftpuser, ftppasswd, homedir=ftphomedir, perm='elradfmwMT')
    #authorizer.add_anonymous('.')
    handler = MyHandler
    handler.certfile = 'server.pem'
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    handler.tls_control_required = True
    handler.tls_data_required = True
    server = FTPServer(('', 21), handler)
    server.serve_forever()

if __name__ == '__main__':
    main()

