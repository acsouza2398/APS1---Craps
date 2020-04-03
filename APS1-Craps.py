#Field bet
def field(d, c, bet):
     if d == 5 or d == 6 or d == 7 or d == 8:
         print("Você perdeu tudo!")
         c = 0
         quit()
     elif d == 3 or d == 4 or d == 9 or d == 10 or d == 11:
        print("Você ganhou {0}!".format(bet))
        c = c + bet
     elif d == 2:
        print("Você ganhou {0}!".format(bet*2))
        c = c + bet*2
     elif d == 12:
        print("Você ganhou {0}!".format(bet*3))
        c = c + bet*3
     return c

#Any Craps bet
def craps(d, c, bet):
   if d == 2 or d == 3 or d == 12:
      print("Você ganhou {0}!".format(bet*7))
      c = c + bet*7
   else:
      print("Você perdeu a aposta!")
      c = c - bet
   return c

#Twelve bet
def twelve(d, c, bet):
   if d == 12:
      print("Você ganhou {0}!".format(bet*30))
      c = c + bet*30
   else:
      print("Você perdeu a aposta!")
      c = c - bet

#Pass Line bet
def plb(d, c, bet):
   if d == 7 or d == 11:
      print("Você ganhou {0}!".format(bet))
      c = c + bet
      return c
   elif d == 2 or d == 3 or d == 12:
      print("Você perdeu a aposta!")
      c = c - bet
      return c
   else:
      return "p"

import random

#start with 30 chips
c = 30

#roll dice
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d = d1 + d2

bet = 10

c = field(d,c,bet)

print (c)