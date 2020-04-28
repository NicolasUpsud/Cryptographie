#coding: utf-8

#import os

with open('Message1.txt' , 'r', encoding='utf8') as file:
    message = file.read()


def dechiffre_scytale(message, cle):
    message_clair = []
    for i in range(cle):
        for j in range(i,len(message),cle):
            message_clair.append(message[j])
    return "".join(message_clair)

for i in range (1,1560):
        if "Joël" in dechiffre_scytale(message,i):
            print( dechiffre_scytale(message,i))

                