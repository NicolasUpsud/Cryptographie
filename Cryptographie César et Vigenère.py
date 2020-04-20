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

def afficher(x):
    if x != None:
        print(x)
message_secret1 = 'mhvxlvmxohvfhvdu'
message_secret2 = 'dwwdtxhdodxeh'
message_secret3 = "Mðspjp{h{pvuz'(']v|z'ñ{lz'hyyp}ðz'ç'kðjopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'Jðzhy'u.h'kðzvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"

for i in range(25):
    afficher(dechiffrement_cesar(message_secret1,i))
for i in range(25):
    afficher(dechiffrement_cesar(message_secret2,i))
for i in range(25):
    afficher(dechiffrement_cesar(message_secret3,i))                                      
                         
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
#%%                               Question 7
message_secret = '#Pk#gnljlui&gi&Ymmhrîui&hwz#yt#w\x7fvxîpi&gi&floijxhqkqx&ssr|erslgeízlu{h0&f”kvx&xr&floijxhqkqx&sex#w{ewzlx{wmuq0&peov${qi&pîsh$rhxzui&gy&piyvemh$ioeou$vhyz/$yxm|drz#wg#tuvmzlst#hgqw&firxm3fm2#îzui&uisspgfík#tgu$jhw&oizwvkv$jljlìvkqxkv0&fstwvglvkpitw$æ#yt#w\x7fvxîpi&gi&floijxhqkqx&pstrerslgeízlu{h$irqsh$rh$ikmlivk#hk#Gïvex#,wx+oo${wmrlwk#gksitgetw$irqsh$irqvrwgqx/1$Ihxzh$sìxnrhk#vïvmywi&dmtvm&ã$r*etdp\x7fvi&gi&ivïtykqgkv0&fi&tyo#iyw${q$gyetwemh$jìgovml#w{u$rhw&floijxhqkqxy#quqsgotndfïwmwxiy1$Ihtkqhgqx&oi&floijxh$jh$\\lkkqìxh$g#ízì$vhviì$vdv&oi&peprv&sv{vwohr&Ivohhxlgn#Ogvmynm&tyo#e&syhomï#wg#qïwlugi&hr&4<<62&Lp&q“uijxh$voyy#hksyov$ihxzh$ïsswxi&dyixrk#wïfyxlxï1\x0e\x10Lp&hwz#rupqï#eoqwo#e{#|o{i&vmîfpk#it#vïiíxhrih$gx$jltrrqgwi&gy&{zoh$ylìioi&Epglwk#hk#Zojitëvk/$wxm&oi&gíiumz#,oqxïjvï#ä&xr&floijxhqkqx&sp{v$irqvoi~h-&getv$yrr&wvglxï#hkv$ikmlivkv$vdv{#it#5;;:4#St#xxry|h$kq$ldmz#hïmä&xrk#qïwlugi&gi&floijxhqkqx&drgosmxi&getv${q$iryxw$zueowí&gi&Jmuyet#Fgwxovxg#Fkopgvs&sexx$kq$78791'

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
print("La longeur de la clé est {}.".format(repetition(message_secret)))

#%%                               Question dechiffrer le message secret
print(dechiffre_vigenere(message_secret, deviner_cle_vigenere(message_secret, repetition(message_secret, k = 3, n = 10))))
