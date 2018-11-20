import rpyc
from ftplib import FTP_TLS
import logging
import sys

namesrv = raw_input("Type address of Name Server: ")

def GetFtpsSrv(namesrv):
    try:
        getans = rpyc.connect(namesrv, 18861)
        ftpssrv1 = getans.root.get_answer()
        return ftpssrv1
    except:
        print ("Name server adreess incorrect")
        namesrv = raw_input("Type address of Name Server: ")
        return GetFtpsSrv(namesrv)

ftpssrv = GetFtpsSrv(namesrv)
usrname = raw_input("Type an username: ")
passwrd = raw_input("Type password: ")
logging.basicConfig(level=logging.DEBUG)

try:
    ftps = FTP_TLS(str(ftpssrv))
    ftps.login(str(usrname), str(passwrd))
    ftps.prot_p()
    print ("Connected")
except:
    print ("Sorry, password or username incorrect")
    sys.exit()

while True:
    usrcmd = raw_input("Type command: ")
    if usrcmd == 'frspace':
        print (ftps.getwelcome())
    elif usrcmd == 'fllist':
        print(ftps.retrlines('LIST'))
    elif usrcmd == 'makedir':
        path = raw_input("Type path: ")
        ftps.mkd(path)
        print ("directory "+path+" created!")
    elif usrcmd == 'ftpsquit':
        print ("Bye!")
        sys.exit()
    elif usrcmd == "chngdir":
        path = raw_input("Type path: ")
        print(ftps.cwd(path))
    elif usrcmd == "readfile":
        path = raw_input("Type filename: ")
        outpath = raw_input("Type local path: ")
        fulloutpath = outpath+"\\"+path
        print(ftps.retrbinary('RETR '+path, open(fulloutpath, 'wb').write))
    elif usrcmd == "writefile":
        path = raw_input("Type local path of file without filename: ")
        filename = raw_input("Type filename: ")
        fullpath = path+"\\"+filename
        print(ftps.storbinary('STOR ' + filename, open(fullpath, 'rb'), 1024)) #
    elif usrcmd == "filedel":
        path = raw_input("Type filename: ")
        print(ftps.delete(path))
    elif usrcmd == "filesize":
        path = raw_input("Type filename: ")
        ftps.sendcmd('TYPE I')
        print(str(ftps.size(path))+" Bytes")
        ftps.sendcmd('TYPE A')
    elif usrcmd == "remdir":
        path = raw_input("Type directory name: ")
        print(ftps.rmd(path))
    elif usrcmd == "gethelp":
        print('gethelt - list of commands')
        print("frspace - to know available space")
        print('fllist - to list folder contains')
        print('makedir - to make new directory')
        print('chngdir - swich directory')
        print('readfile - to read/download file')
        print('writefile - to write/upload file')
        print('filedel - to delete file')
        print('filesize - to know size of file')
        print('remdir - to remoove folder')
        print('ftpsquit - to close client')

    else:
        print ("Unknown command, type gethelp to get list of commands")