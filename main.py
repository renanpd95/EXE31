import math,os

cat1 = int(input("Insira cateto 1: "))
cat2 = int(input("Insira o cate 2 : "))

os.system("clear")
#Potenciação dos dois números
pot1 = math.pow(cat1,2)
pot2 = math.pow(cat2,2)
#Soma das duas potencias
som = pot1 + pot2
#Raiz do resultado
raiz = math.sqrt(som)


print(f"A hipotenusa do Triangulo é: {raiz:.2f} ")


  