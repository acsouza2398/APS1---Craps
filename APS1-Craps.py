#BET FUNCTIONS

#Field bet
def field(d, c, bet):
     if d == 5 or d == 6 or d == 7 or d == 8:
         print("Você perdeu tudo com o Field Bet!")
         c = 0
         return c
     elif d == 3 or d == 4 or d == 9 or d == 10 or d == 11:
         print("Você ganhou {0} com o Field Bet!".format(bet))
         c = c + bet
         return c
     elif d == 2:
         print("Você ganhou {0} com o Field Bet!".format(bet*2))
         c = c + bet*2
         return c
     elif d == 12:
         print("Você ganhou {0} com o Field Bet!".format(bet*3))
         c = c + bet*3
         return c

#Any Craps bet
def craps(d, c, bet):
   if d == 2 or d == 3 or d == 12:
      print("Você ganhou {0} com o Any Craps Bet!".format(bet*7))
      c = c + bet*7
      return c
   else:
      print("Você perdeu a aposta com o Any Craps Bet!")
      c = c - bet
      return c

#Twelve bet
def twelve(d, c, bet):
   if d == 12:
      print("Você ganhou {0} com o Twelve Bet!".format(bet*30))
      c = c + bet*30
      return c
   else:
      print("Você perdeu a aposta com o Twelve Bet!")
      c = c - bet
      return c

#Pass Line bet
def plb(d, c, bet):
   if d == 7 or d == 11:
      print("Você ganhou {0} com o Pass Line Bet!".format(bet))
      c = c + bet
      return c
   elif d == 2 or d == 3 or d == 12:
      print("Você perdeu a aposta com o Pass Line Bet!")
      c = c - bet
      return c
   else:
      return c
   

###################################################################
#GAME STARTS HERE

import random

#start with 30 chips
c = 30

#round begin - Come Out phase
while c > 0:
   print("Fase Come Out")
   print("Você tem {0} fichas.".format(c))
   phase = "c"

   #continue game?
   answer = input("Você quer apostar? (sim/não) ")
   if answer == "não":
      print("Obrigada por Jogar! Você terminou com {0} fichas.".format(c))
      quit()

   #define amount of bets
   amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Pass Line Bet \n Field \n Any Craps \n Twelve "))
   while amount > 4:
      print("Não há tantos tipos de aposta. Favor escolher de novo (Máximo de 4). ")
      amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Pass Line Bet \n Field \n Any Craps \n Twelve "))
   
   #define type of bet and how many chips per bet
   i = 0
   b = 0
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
      b=b+bet[i]
      i=i+1
   
   #failsafe for chip amount < bet total
   if b > c:
      print("Você apostou mais do que tem. Favor apostar de novo")
      r=1
   else:
      r=0
   
   while r == 1:
      i = 0
      b = 0
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
         b=b+bet[i]
         i=i+1
      if b > c:
         print("Você apostou mais do que tem. Favor apostar de novo")
         d=1
      else:
         d=0

   #roll dice
   d1 = random.randint(1,6)
   d2 = random.randint(1,6)
   d = d1 + d2
   print("O valor dos dados deu {0}!".format(d))
   
   #playing out the bets
   i=0
   while i < amount:
      if typeb[i] == 2:
         c = field(d,c,bet[i])
      elif typeb[i] == 3:
         c = craps(d,c,bet[i])  
      elif typeb[i] == 4:
         c = twelve(d,c,bet[i])
      elif typeb[i] == 1:
         c1 = plb(d,c,bet[i])
         if c1 == c:
            phase = "p"
            tempbet = bet[i]
         else:
            c=c1
      i=i+1
   
   #exit if no chips left
   if c <= 0:
      break


  ###################################################################
   #phase shift
   if phase == "p":
      print("Mudança de fase para Point")
      point=d
      betpld = tempbet

   #start Point phase
   while phase == "p":
      print("Fase Point")
      print("Você tem {0} fichas.".format(c))
      
      #Define amount of bets
      amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Field \n Any Craps \n Twelve "))
      while amount > 3:
         print("Não há tantos tipos de aposta. Favor escolher de novo (Máximo de 3). ")
         amount = int(input("Quantos tipos de aposta quer fazer? \n Opções: \n Field \n Any Craps \n Twelve "))

      #Define type of bet and how many chips per bet
      if amount > 0:
         i = 0
         b = 0
         typeb = [0]*amount
         bet = [0]*amount
         alltypes = ["Field (1)", "Any Craps (2)", "Twelve(3)"]
         while i < amount:
            typeb[i] = int(input("Qual aposta você quer fazer (aposta n° {0})? \n Opções: \n {1} \n {2} \n {3} ".format(i+1,alltypes[0],alltypes[1],alltypes[2])))
            if typeb[i] == 1:
               rtype = "Field"
               bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
               alltypes[0] = ""
            elif typeb[i] == 2:
               rtype = "Any Craps"
               bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
               alltypes[1] = ""
            elif typeb[i] == 3:
               rtype = "Twelve"
               bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
               alltypes[2] = ""
            else:
               print("Favor digitar um tipo de aposta válido (número do lado do nome da aposta).")
               i=i-1
            b=b+bet[i]
            i=i+1
   
         #failsafe for chip amount > bet total
         if b > c:
            print("Você apostou mais do que tem. Favor apostar de novo")
            r=1
         else:
            r=0
      
         while r == 1:
            i = 0
            b = 0
            typeb = [0]*amount
            bet = [0]*amount
            alltypes = ["Field (1)", "Any Craps (2)", "Twelve(3)"]
            while i < amount:
               typeb[i] = int(input("Qual aposta você quer fazer (aposta n° {0})? \n Opções: \n {1} \n {2} \n {3} ".format(i+1,alltypes[0],alltypes[1],alltypes[2])))
               if typeb[i] == 1:
                  rtype = "Field"
                  bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
                  alltypes[0] = ""
               elif typeb[i] == 2:
                  rtype = "Any Craps"
                  bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
                  alltypes[1] = ""
               elif typeb[i] == 3:
                  rtype = "Twelve"
                  bet[i] = int(input("Quanto você quer apostar em {0}? ".format(rtype)))
                  alltypes[2] = ""
               else:
                  print("Favor digitar um tipo de aposta válido (número do lado do nome da aposta).")
                  i=i-1
               b=b+bet[i]
               i=i+1
            if b > c:
               print("Você apostou mais do que tem. Favor apostar de novo")
               d=1
            else:
               d=0

      #roll dice
      d1 = random.randint(1,6)
      d2 = random.randint(1,6)
      d = d1 + d2
      print("O valor dos dados deu {0}!".format(d))
   
      #playing out the bets
      i=0
      while i < amount:
         if typeb[i] == 1:
            c=field(d,c,bet[i])
         elif typeb[i] == 2:
            c=craps(d,c,bet[i])  
         elif typeb[i] == 3:
            c=twelve(d,c,bet[i])
         i=i+1

      
      #checking pass line bet
      if d == point:
         print("Você ganhou {0} com o Pass Line Bet!".format(betpld))
         c = c + betpld
         print("Fim da fase Point")
         phase = "c"
         break
      elif d == 7:
         print("Você perdeu tudo com o Pass Line Bet!")
         c = 0
         break
      
      #exit if no chips left
      if c <= 0:
         break
  
print("Você perdeu todas as fichas. Q azar!")