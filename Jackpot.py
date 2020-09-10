#Basic jackpot game-Basit jackpot oyunu
import  random

emojis1=['👍','🤩','😎']
emojis2=['👍','🤩','😎']
emojis3=['👍','🤩','😎']

#Sonucu döndürme fonksiyonu
def roll(e1,e2,e3):

 print('----------------')
 print('|'+' '+e1+' '+'|'+' '+e2+' '+'|'+' '+e3+' '+'|')
 print('----------------')

e1=emojis1[random.randint(0,2)]
e2=emojis2[random.randint(0,2)]
e3=emojis3[random.randint(0,2)]

if e1 == e2 == e3:
    print("Bugün şanslı günündesin!200 lirayı kaptın valla!")
else:
    print("Kaybettin be morukkk!")

roll(e1,e2,e3)

