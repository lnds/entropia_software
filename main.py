def main(n: int) -> int:
  if n <= 0: return n

  def sum_step(step):
    p = (n-1) // step
    return step * p * (p+1) // 2
 
  return sum_step(3) + sum_step(5) - sum_step(3*5)

if __name__ == "__main__":
  try:
    n = int(input("ingrese n: "), 0)
    print('el resultado es',  main(n))
  except ValueError:
    print("debe ingresar un número")
