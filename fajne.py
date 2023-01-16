a = int(input())
b = int(input())
suma = a+b
print(suma)
k = int(input())
dzielnik = suma // k
print(dzielnik)
if dzielnik % 2:
  print("Jest liczba nie parzystą")
elif dzielnik % 3:
  print("Jest liczbą parzystą")