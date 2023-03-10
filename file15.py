                             #list
                    # LIST ARE MUTABLE CHANGEABLE


# name = ['name',"ebad","anas","owais"]
# print(type(name))
# print(name[2])
# print(name[-2])
# print(name[1:3])


# append function
# name.append("ahad")
# print(name)

# insert function
# name.insert(2,"owais")
# print(name)


# pop function
# name.pop(1)
# print(name)


# update function
# name[0] = "nasir"
# print(name)

# remove function  
# name.remove("name")
# print(name)

# del function
# del name[2]
# print(name)
            # list constructor

# names = list((33,34,36,78))
# print(names)

 

# testing_list = ["hello",79,3.4,True,name]
# print(testing_list)

names = list((33,34,36,78))
# for i in names:
#     print(i)


nam = len(names)
na = 0
while na < nam:
    # print(names[na])
    na += 1



 # max numers in any list
# names = list((33,34,36,200))
# max = names[0]
# for m in names:
#     if  m > max:
#         max = m

# print()     




# even numbers program
# even = []
# name = [1,2,4,6,8,100,101,102,104,105]
 
# for m in name:
#     if m %2 ==0:
#         even.append(m)

# print(even)




name = [1,2,4,6,8,9,11,100,101,102,104,105]
even = [m for m in name if m % 2 == 0]
print(even)




