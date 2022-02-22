while True:
	Z=[]
	while True:
		try:
			n=int(input("Введiть кiлькiсть чисел масиву: "))
		except ValueError:
			print("Введiть саме число")
			continue
		break
	for i in range(n):
			z=int(input("Введiть елементи масиву що є цiлими числами"))
			Z.append(z)
	print("Ваш масив: ", Z)
	s_Z=sorted(Z)
	print("Вiдсортований масив: ", s_Z)
	r=(max(s_Z)+min(s_Z))/2
	s_Z.append(r)
	s_Z.sort()
	print("Вхiдний масив", Z)
	print("Середнє арифметичне максимального мiнiмального елементiв вхiдного масиву: ", r)
	print("Змінений масив: ", s_Z)
	
	