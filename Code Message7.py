#coding: utf-8

#import os

with open('Message7.txt' , 'r', encoding='utf8') as file:
    message7= file.read()

def decaler(caractere, cle):
    numero_carac = ord (caractere) + cle       
    return chr(numero_carac)


def caractere_plus_frequent(texte):
    dictionnaire = frequence(texte)
    valeurmax = 0
    indicemax = ''
    for indice in dictionnaire:
        if valeurmax < dictionnaire[indice]:
            valeurmax = dictionnaire[indice]
            indicemax = indice
    return(indicemax)


def dechiffre_vigenere(message, cle):
    liste = list(message)
    new_liste = []
    index_cle = 0
    for i in liste:
            new_liste.append(decaler(i,-cle[index_cle]))
            new_message = ''.join(new_liste)
            index_cle += 1
            if index_cle >= len(cle):
                  index_cle = 0
    return new_message


def frequence(texte):
    liste = list(texte)
    dictionnaire = {}
    for i in liste:
        dictionnaire[i] = liste.count(i)
    return dictionnaire


def deviner_cle_cesar(message):
    caractere = caractere_plus_frequent(message)
    cle_probable = ord(caractere) - ord(' ') 
    return(cle_probable)
    
def deviner_cle_vigenere(message, longueur):
    """
    prend en arguments le message chiffré (une chaine de caractère) et une longueur possible de clé (un entier) et retourne la clé la plus probable en utilisant une analyse de fréquence (liste d'entier).
    """
    cle=[]
    for i in range(longueur):
        # analyse de fréquence (sur quoi les caractères en position longueur*k+i)
        # prendre un caractère sur longueur en position longueur*k+i :
        message_i = message[i : len(message) : longueur]
        cle.append(deviner_cle_cesar(message_i))

    return cle


def pgcd(a,b):
    if b == 0:
        return a
    while a%b !=0:
        a, b = b, a%b
    return b

def pgcd_list(l):
    if len(l) == 0:
        return 0
    else :
        return pgcd(l[0], pgcd_list(l[1:]))

def repetition(message, k = 3, n = 10):
    # cherche les n premières répétitions de taille k dans message
    compteur = 0
    ecarts = []
    for i in range (1,len(message)-k+1):
        for j in range(i+1,len(message)-k+1):
            if compteur !=n:
                if (message[i:i+k] == message[j:j+k]):
                    print("{}ième répétition : {}\t écart : {}".format(compteur, message[i:i+k], j-i))
                    compteur = compteur +1
                    ecarts.append(j-i)
    return pgcd_list(ecarts)


print(dechiffre_vigenere(message7, deviner_cle_vigenere(message7, repetition(message7, k = 3, n = 10))))
