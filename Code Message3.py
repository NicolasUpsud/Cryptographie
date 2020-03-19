#coding: utf-8

#import os

with open('Message3.txt' , 'r', encoding='utf8') as file:
    message3 = file.read()

    
def frequence(texte):
    liste = list(texte)
    dictionnaire = {}
    for i in liste:
        dictionnaire[i] = liste.count(i)
    return dictionnaire

                              
def caractere_plus_frequent(texte):
    dictionnaire = frequence(texte)
    valeurmax = 0
    indicemax = ''
    for indice in dictionnaire:
        if valeurmax < dictionnaire[indice]:
            valeurmax = dictionnaire[indice]
            indicemax = indice
    return(indicemax)


def deviner_cle_cesar(message):
    caractere = caractere_plus_frequent(message)
    cle_probable = ord(caractere) - ord(' ') 
    return(cle_probable)       
    
def compter_occurences(caractere , chaine):
    compteur = 0 
    for i  in chaine:
        if i == caractere:
            compteur = compteur+1
    return compteur
   
def decaler(caractere, cle):
    numero_carac = ord (caractere) +cle       
    return chr(numero_carac)

def dechiffrement_cesar(message,cle):
    liste = list(message)
    new_liste = [] 
    for i in liste:
        new_liste.append(decaler(i,-cle))
        new_message = ''.join(new_liste)    
    return new_message

print(dechiffrement_cesar(message3 , deviner_cle_cesar(message3)))
