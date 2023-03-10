# multiple line string 
 
y  = """ hello world this is my first program in 
pyhton
helo world this is second program in python 

"""
print(y)




# string indexing
z = "the quick brown fox jumps and over a lazy dog"
print(z[2])
# left to right me 0,to 123

print(len(z))


print(z[-1])
# right to left me -1,-2,-3 negative indexing





# strings In or Not function
print("the" in z)





#string slicing 
x = "pakistan is a great city"
print(x[1:-4])
print(x[0:])
print(x[-10:-2])
print(type(x))






#strings concatinate
z = "pakistan"
c = "karachi"
v = z +' '+c
print(v)
print( z+" "+c)



# one line add multiple strings
print("hello"+" world")



#multiply strings
print(c* 10)



# string format function
car = "mehran"
model = 2004
price = 500000

v = ("i want to car {} and {} price {}")
print(v.format(car,model,price))


v = ("i want to car {1} and {2} price {0}")
print(v.format(car,model,price))





# escape sequance character
h = "The quick brown \\n fox \"jumps\" and over \ python file6.py \\t a lazy dog"
print(h)



#string methods
print(h.upper())
print(h.lower())
print(h.title())
