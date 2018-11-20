from ftplib import FTP_TLS
import re
import random
import rpyc
import logging

global inuser
inuser = raw_input('Type username: ')
global inpass
inpass = raw_input('Type user pass: ')

def GetSrvAdd():
    srvadd = raw_input("Type IPv4 address of ftps server: ")
    if not re.match(
            "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
            srvadd):
        print("Incorrect address")
        attempt = GetSrvAdd()
        return attempt
    else:
        return srvadd

def GiveSrv(srvlist, count,):
    srv = random.choice(srvlist)
#    logging.debug(count)
    if count < 6:
        try:
            ftps = FTP_TLS(str(srv))
            ftps.login(inuser, inpass)
            ftps.quit()
            return srv
        except:
            count += 1
            return GiveSrv(srvlist, count)
    else:
        ftperror = "There no available FTPS servers"
        return ftperror

srv1 = GetSrvAdd()
srv2 = GetSrvAdd()
global srvlist
srvlist = [srv1, srv2]
count = 0

logging.basicConfig(level=logging.DEBUG)

class MyService(rpyc.Service):
    def exposed_get_answer(self): # this is an exposed method
        return GiveSrv(srvlist,0)
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
