def main(n: int) -> int:
  if n <= 0: return n
  sum = 0
  for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum


if __name__ == "__main__":
  try:
    n = int(input("ingrese n: "), 0)
    print('el resultado es',  main(n))
  except ValueError:
    print("debe ingresar un número")
