def fibionaci_generator(n):
  a=0
  b=1
  for i in range(n):
      yield a
      a,b=b,a+b
 
 
 
for index, number in enumerate(fibionaci_generator(10), start=1):
    print(f"Fibonacci number {index}: {number}")