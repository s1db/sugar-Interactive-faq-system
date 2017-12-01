# -*- coding: utf-8 -*-
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'chat.freenode.net' #irc server
PORT = 6665 #port
NICK = 'faqsbot'
USERNAME = 'faqsbot'
REALNAME = 'Sidhant Bhavnani'

print('soc created |', s)
remote_ip = socket.gethostbyname(HOST)
print('ip of irc server is:', remote_ip)


s.connect((HOST, PORT))

print('connected to: ', HOST, PORT)

nick_cr = ('NICK ' + NICK + '\r\n').encode()
s.send(nick_cr)
usernam_cr= ('USER test test test :sidhant bhavnani \r\n').encode()
s.send(usernam_cr)
s.send('JOIN #sugar-newbies \r\n'.encode()) #chanel

while 1:
    data = s.recv(4096).decode('utf-8')
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        print('PONG sent \n')
    print(str(data))
    if data.find('faqsbot') != -1:
        print(data.split()[2])
        s.send((str('PRIVMSG ' + data.split()[2]) + ' Hi! \r\n').encode())

s.close()
