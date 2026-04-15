n1 = int(input("Ingrese el primer número"))
n2 = int(input("Ingrese el segundo número"))
n3 = int(input("Ingrese el tercer número"))
if n1+n2==n3:
    print("La suma del primero mas segundo numero es igual al tercero")
if n3+n2==n1:
    print("La suma del tercer mas el segundo es igual al primero") 
if n1+n3==n2:
    print("La suma del primero mas el tercero es igual al segundo")
else:
    print("La suma de dos numeros no es igual al tercero")   