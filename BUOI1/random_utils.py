import random 
def generate_numbers(n, start, end):
   return [random.randint(start, end) for _ in range(n)]
