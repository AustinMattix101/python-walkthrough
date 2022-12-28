import keyword

print("________________________ Python ________________________")

print(keyword.kwlist)

print("______________________________________________________________________________________")

print("Hello, World!")

a, b, c = 1, 2, 3
print(c, b, a)

a, b, _ = 5, 6, 7
print(a, b, c)

a = b = c = 1
a = 4
print(a)
print(type(a))

pi = 3.14
print(type(pi))

x = None
print(type(x))

y = True
print(type(y))

_first = 'Austin'
print(type(_first))
_middle = 'Connor'
_last = 'Mattix'

_full = _first + ' ' + _middle + ' ' + _last
print(_first, _last)
print(_full)
x = y = [6, 7, 8]
x[1] = 10
print(y)

x = y = [1, 2, [5, 6, 7], 3, 4]
print(x[2])
print(x[2][1])

	# Area
radius = 2
pi = 3.14
area = radius * radius * pi
print(area)

	# Function
def Getfullname():
	print("Austin Mattix")
Getfullname()

def my_function(fname):
  print(fname + " Mattix")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Austin Connor", "Mattix")

	# Error < Call 1 argument or 3 argument
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Amy")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

	# Default Parameter Value
def my_function(country = "Cambodia"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("U.S.A")

def multi_5(x):
  return 5 * x

print(multi_5(3))
print(multi_5(5))
print(multi_5(9))

def myfunction():
  pass

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print(fruits)
  
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def square(arg):
  return arg * arg

x = 2
y = 3
print(square(y), square(x))

name = input("What's your name?")
print("Hi!, " + name)

# Operater
o = 100 + 200
print(o)

print(5-2)
print(5*2)
print(5/2)
print(5//2) # No remainder as float
print(5%2) # only remainder
print(5**2) # power 2
print(10+7/7) # result 11
print((10+7)/17) # result 1

print(int)
def sec_converter():
  str_sec = input("Please enter the number of seconds you wish to convert!")
  input_sec = int(str_sec)

  hours = input_sec // 3600
  secs_remain = input_sec % 3600
  minutes = secs_remain // 60
  secs_final_remain = secs_remain % 60

  return print(hours, "hour(s), ", minutes, "min(s), " , secs_final_remain, "sec(s). ")
sec_converter()

print(len("Hello")) #len function count number of letter of Hello

def sub(a, b):
  return a - b

x = 2
y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))

# Type Coversion functions
int() # 3.99 convert to 3 not 4
float()
str()

big = max("Hello world")
print(big)

tiny = min("Hello world")
print(tiny)