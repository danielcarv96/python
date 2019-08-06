def prog():
	
	n= int(input("cuantos numeros deseas buscar "))
	fibonacci= [0,1]
	for i in range(100):
			fibonacci.append(fibonacci[i]+fibonacci[i+1])
	for j in range(n):
		num= int(input("Escriba el numero de la  serie fibonachi que desea ver "))
		npi= "n"
		for i in range(100):
			if(i==99 and npi=="n"):
					print("No se encuentra")
			elif(num == fibonacci[i]):
				print (f"El indice del numero {num} es {i}")
				npi="y"

prog()