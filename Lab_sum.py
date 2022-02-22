import math
while True:
	while True:
		try:
			r=float(input("Введiть точнiсть"))
		except ValueError:
			print("Введiть саме число")
			continue
		break
	while True:
		try:
			x=float(input("Введiть значення змiнної x"))
		except ValueError:
			print("Введiть саме число")
			continue
		break
	Sum=0
	n=1
	while True:
		S=x/((4**n)*math.factorial(n))
		if (S>= r):
			Sum+=S
			print("Sum= " , Sum)
			print(n)
			n+=1
		else: break
	print("Сума членiв= " , Sum)
	print("")
	Q=input("Продовжити? Оберiть так або нi")
	if (Q=="так") : continue
	else: break