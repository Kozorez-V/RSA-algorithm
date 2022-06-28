import os.path
from sys import getdefaultencoding
getdefaultencoding()

def openFile():
    path = './message.txt'
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print('Your file is empty or does not exist')
        exit()
    file = open(path, 'r')
    return file

def readMessage(file):
    message = file.read()
    return message