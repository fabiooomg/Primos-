#Este algoritmo devuelve un Boolean dependiendo si el input ingresado es un numero Primo o No.
def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
n = int(input())
print(es_primo(n))

  