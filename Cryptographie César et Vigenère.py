# coding: utf-8

#import os
#
#with open('Message 1.txt', 'r') as file:
    # on fait des choses avec le fichier
#    message = file.read() # chaÃ®ne de caractÃ¨re avec le contenu du fichier
    # bla
# Ã  partir d'ici, le fichier est fermÃ©
 
    
        
    
                           #chiffrement de césar#
#%%                              Question 1
chaine = "azaqkomisdb vuifos unoiqbuv vfnnnnc vuifos ifbvi"
def compter_occurences( caractere , chaine):
    compteur = 0 
    for i  in chaine:
        if i == caractere:
            compteur = compteur+1
    return compteur

print(compter_occurences( "i" , chaine))



#%%                               Question 2 
def compter_mots(chaine):
    compteur = 0
    for i in chaine:
        if i == " ":
            compteur = compteur+1
    return compteur

print(compter_mots(chaine))

#%%                               Question 3 
def compter_occurences_mot(mot, chaine):
    compteur= 0
    for i in chaine.split(' '):
        if i== mot:
            compteur+=1
    return compteur

print(compter_occurences_mot("vuifos", chaine))

#%%                               Question 4 
def substituer():
    chaine = "azaqkomisdb vuifos unoiqbuv vfnnnnc vuifos ifbvi"
    liste = list(chaine) 
    liste[0] = '&'
    chaine = ''.join(liste) 
    return chaine
print(substituer())

#%%                               Question 5
def substituer_mot():
    chaine = "azaqkomisdb vuifos unoiqbuv vfnnnnc vuifos ifbvi" 
    liste = chaine.split(' ')
    index = -1
    for i in liste:
        index = index + 1 
        print(index)
        if i == 'vuifos':
            liste[index]="changer"
    chaine = ' '.join(liste)
    return chaine
print(substituer_mot())

#%%                               Question 7
def decaler(caractere, cle):
    numero_carac = ord (caractere) + cle       
    return chr(numero_carac)
print(decaler("a", 3))


#%%                               Question 8
def chiffrement_cesar(message, cle):
    liste = list(message)
    new_liste = [] 
    for i in liste:
        new_liste.append(decaler(i,cle))
        new_message = ''.join(new_liste)
    return new_message
print(chiffrement_cesar("un message avec des espaces", 3))

def dechiffrement_cesar(message,cle):
    liste = list(message)
    new_liste = [] 
    for i in liste:
        new_liste.append(decaler(i,-cle))
        new_message = ''.join(new_liste)
    if compter_occurences("e", new_message)>5:
        return new_message

print(dechiffrement_cesar("xq#phvvdjh#dyhf#ghv#hvsdfhvhh", 3))
#%%                               Question 9
message_secret1 = 'mhvxlvmxohvfhvdu'
message_secret2 = 'dwwdtxhdodxeh'
message_secret3 = "Mðspjp{h{pvuz'(']v|z'ñ{lz'hyyp}ðz'ç'kðjopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'Jðzhy'u.h'kðzvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"

for i in range(25):
    print(dechiffrement_cesar(message_secret1,i))
    

for i in range(25):
    print(dechiffrement_cesar(message_secret2,i))
    

for i in range(25):
    print(dechiffrement_cesar(message_secret3,i))                                         
                         
#%%                       #chiffre de Vigenère#
#%%                               Question 1
def vigenere(message, cle):
    liste = list(message)
    new_liste = []
    index_cle = 0
    for i in liste:
            new_liste.append(decaler(i,cle[index_cle]))
            new_message = ''.join(new_liste)
            index_cle += 1
            if index_cle >= len(cle):
                  index_cle = 0
    return new_message
        
print(vigenere("ceci est le message",[3,4,1]))

#%%                               Question 2
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
        
print(dechiffre_vigenere("fidl$fvx!oi!pitvehh",[3,4,1]))
#%%                               Question 3
def frequence(texte):
    liste = list(texte)
    dictionnaire = {}
    for i in liste:
        dictionnaire[i] = liste.count(i)
    return dictionnaire
print(frequence('bienvenue'))
#%%                               Question 4
def caractere_plus_frequent(texte):
    dictionnaire = frequence(texte)
    valeurmax = 0
    indicemax = ''
    for indice in dictionnaire:
        if valeurmax < dictionnaire[indice]:
            valeurmax = dictionnaire[indice]
            indicemax = indice
    return(indicemax)

print(caractere_plus_frequent('anticonstitutionnellement'))
#%%                               Question 5
def deviner_cle_cesar(message):
    caractere = caractere_plus_frequent(message)
    cle_probable = ord(caractere) - ord(' ') 
    return(cle_probable)
print(deviner_cle_cesar("Mðspjp{h{pvuz'(']v|z'ñ{lz'hyyp}ðz'ç'kðjopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'Jðzhy'u.h'kðzvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"))
#%%                               Question 6
def deviner_cle_vigenere(message, longueur):
    for
