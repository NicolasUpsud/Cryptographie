#coding: utf-8

#import os

with open('Message4.txt' , 'r', encoding='utf8') as file:
    message4 = file.read()

    
def frequence0(texte):
    liste = list(texte)
    liste0 = liste[0:len(liste):2]
    dictionnaire = {}
    for i in liste0:
        dictionnaire[i] = liste0.count(i)
    return dictionnaire


def caractere_plus_frequent0(texte):
    dictionnaire = frequence0(texte)
    valeurmax = 0
    indicemax = ''
    for indice in dictionnaire:
        if valeurmax < dictionnaire[indice]:
            valeurmax = dictionnaire[indice]
            indicemax = indice
    return(indicemax)

def deviner_cle_cesar0(message):
    caractere = caractere_plus_frequent0(message)
    cle_probable = ord(caractere) - ord(' ') 
    return(cle_probable)    
    
    
    
def frequence1(texte):
    liste = list(texte)
    del liste[0:len(liste):2]
    liste1 = liste
    dictionnaire = {}
    for i in liste1:
        dictionnaire[i] = liste1.count(i)
    return dictionnaire

def caractere_plus_frequent1(texte):
    dictionnaire = frequence1(texte)
    valeurmax = 0
    indicemax = ''
    for indice in dictionnaire:
        if valeurmax < dictionnaire[indice]:
            valeurmax = dictionnaire[indice]
            indicemax = indice
    return(indicemax)                              

def deviner_cle_cesar1(message):
    caractere = caractere_plus_frequent1(message)
    cle_probable = ord(caractere) - ord(' ') 
    return(cle_probable)       



   
def decaler(caractere, cle):
    numero_carac = ord (caractere) +cle       
    return chr(numero_carac)  
         
def compter_occurences(caractere , chaine):
    compteur = 0 
    for i  in chaine:
        if i == caractere:
            compteur = compteur+1
    return compteur
   


def dechiffrement_cesar(message,cle):
    liste = list(message)
    new_liste = [] 
    index_cle = 0
    for i in liste:
        new_liste.append(decaler(i,-cle[index_cle]))
        new_message = ''.join(new_liste) 
        index_cle +=1
        if index_cle >= len(cle):
                  index_cle = 0
    return new_message

print(dechiffrement_cesar(message4 , [deviner_cle_cesar0(message4),deviner_cle_cesar1(message4)]))