# def my_generator():
#   for i in range(5):
#     yield i

# # Create a generator object
# my_gen = my_generator()

# # Iterate over the generator object
# for i in my_gen:
#   print(i)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1
my_countdown = countdown(5) 
# Iterate over the generator object using next() and str() functions.
print(next(my_countdown))  # Output: 5  
print(str(next(my_countdown)))  # Output: "4"
print(list(countdown(3)))  # Output: [2, 1, 0]  

for x in countdown(7):
    if x == 0:
      break
    else:
      print(x)  # Output: 6 5 4 3 2 1      
