import math
W = int(input("Enter number from 1 to 4"))
while True: 
 if (W==1):
    while True:
     try:
      A=float(input("Введiть значення змiнної A: "))
     except ValueError:
      print("ii")
      continue
     else : break
    if (A<=3):
       Y=A**2-A
       print("Y= ", Y)
    elif(A==1):
       Y=math.cos(math.sqrt(A))
       print("Y= ", Y)
    else:
       Y=3*(A**3)-A**2+A
       print("Y= ", Y)
 elif (W==2):
   while True:
    try:
     B=float(input("Введiть значення змiнної B: "))
    except ValueError:
      print("ii")
      continue
    else : break
   if(B>0):
      Y=math.cos(B**3)
      print("Y= " , Y)
   else:
      Y=(B**2)/(1.5)
      print("Y= ", Y)
 elif(W==3):
   F="first"
   C=input("Введiть слово ")
   if(F<C):
    print(F,C)
   else:
    print(C,F)
 elif(W==4):
   S=input("Натиснiть клавiшу")
   print(ord(S))
 Q=(input("Продовжити? Напишть yes або no : "))
 if(Q=="yes"): 
  continue
 elif(Q=="no"): 
  break