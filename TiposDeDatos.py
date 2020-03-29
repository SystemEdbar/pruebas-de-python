def PRODUCTOSUMA():
    primernumero =(input("INTRODUCE EL PRIMER NUMERO"))
    segundonumero =(input("INTRODUCE EL SEGUNDO NUMERO"))
    resultado=0
    for i in range(0,int(segundonumero)):
        resultado=resultado+primernumero
    print(resultado)

def PRODUCTOF():
    num1=1
    num2=1
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)

def VALORMAYOR():
    num1=0
    num2=0
    i = ord('d')
    while not i == 102:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        if num2 >= num1:
            num1=num2
        print("hola")
    else:
        num2=num1

    print("el numero mayor es"+str(num2))

def FIBONACCI():
    contador=0
    a=0
    b=1
    c=0
    N= int(input("INGRESE LA CANTIDAD QUE DESEA VER"))

    while contador < N:
        a=b
        b=c
        c=a+b
        print(c)
        contador=contador+1

def SUMARPARES():
    nu1 = 0
    cont = 0
    total = 0
    while cont < 30:
        nu1 = float(input("Ingrese un numero: "))
        cont = cont + 1
        if nu1 % 2 == 0:
            total = total + nu1
        else:
            total = total
    print("La suma de los pares es: " + str(total))
    print("")

def FACTORIALES(x, n):
        if (n > 0):
            x = factorial(x, n - 1)
            x = x * n
        else:
            x = 1
        return x

    print("**** Encontrar el factorial de un Numero ****")
    print("")
    n = int(input("Ingrese un numero: "))
    x = 1
    x = factorial(x, n)
    print("El factorial de ", n, "es: " + str(x))
    print("")

def VALORPRIMO(num):
        cont = 0;
        for i in range(1, num):
                if (num % i == 0):
                        cont += 1
                        if cont > 1:
                                return False
        return True

suma = 0
for i in range(30):
        i=int(input("Ingrese un numero: "))
        if VALORPRIMO(i):
                print("es primo")
                suma=suma+i
        else:
                print("no es primo")
                suma=suma

print("La suma de los primos es:", str(suma))

PRODUCTOSUMA()
PRODUCTOF()
VALORMAYOR()
FIBONACCI()
SUMARPARES()
FACTORIALES()
VALORPRIMO(30)

