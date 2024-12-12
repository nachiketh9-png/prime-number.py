def is_prime(num):
  if num<= 1:
    return False

def is_prime(num):
    for i in range(2, int(num **0.5)+1):
        if num % i== 0:
          return False
    return True
number = int(input("Enter a number"))
if is_prime(number):
  print(number, "the number is prime number.")
else:
  print(number, "the number is not prime number.")
