def my_function(): #creatnig a function
    print("Hello from a Function")

my_function()
my_function()
my_function()

#repitatice work
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return value
def get_greeting():
   return "Hello From my side."
message = get_greeting()
print(message)

#Pass Statement
def my_function():
   pass