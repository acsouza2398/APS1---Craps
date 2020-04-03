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

#round begin
while c > 0:
   print("Fase Come Out")

   answer = input("Você quer apostar? ")
   if answer == "não":
      quit()

   amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Pass Line Bet \n Field \n Any Craps \n Twelve "))
   while amount > 4:
      print("Não há tantos tipos de aposta. Favor escolher de novo (Máximo de 4). ")
      amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Pass Line Bet \n Field \n Any Craps \n Twelve "))
   
   i = 0
   typeb = [0]*amount
   bet = [0]*amount
   alltypes = ["Pass Line Bet (1)", "Field (2)", "Any Craps (3)", "Twelve(4)"]
   while i < amount:
      typeb[i] = int(input("Qual aposta você quer fazer (aposta n° {0})? \n Opções: \n {1} \n {2} \n {3} \n {4} ".format(i+1,alltypes[0],alltypes[1],alltypes[2],alltypes[3])))
      if typeb[i] == 1:
         rtype = "Pass Line Bet"
         bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
         alltypes[0] = ""
      elif typeb[i] == 2:
         rtype = "Field"
         bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
         alltypes[1] = ""
      elif typeb[i] == 3:
         rtype = "Any Craps"
         bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
         alltypes[2] = ""
      elif typeb[i] == 4:
         rtype = "Twelve"
         bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
         alltypes[3] = ""
      else:
         print("Favor digitar um tipo de aposta válido (número do lado do nome da aposta).")
         i=i-1
      i=i+1
   
   #roll dice
   d1 = random.randint(1,6)
   d2 = random.randint(1,6)
   d = d1 + d2
else:
   print("Você perdeu todas as fichas. Q azar!")
   
