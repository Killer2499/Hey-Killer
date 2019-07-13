from ftplib import FTP
import os

ftp = FTP('')
ftp.connect('192.168.3.62',2121)

ftp.login('killer','##auto_generated##')
ftp.getwelcome()
files=ftp.dir()
#ftp.retrlines('LIST')
print (files)
ftp.cwd("43AE-1A09")
print(ftp.pwd())

files_inside=ftp.dir()
print(files_inside)

#ftp.cwd("Android")

files_inside=ftp.dir()
#print(files_inside)

print(ftp.pwd())

#ftp.cwd("data")
files_inside=ftp.dir()
#print (files_inside)
filedata = open('PRO-SuperSU-v2.67.zip', 'wb')
ftp.retrbinary('RETR PRO-SuperSU-v2.67.zip', filedata.write)  

direc= 'C:/Users/Sanath/Desktop';
os.chdir(direc)
filedata.close()


