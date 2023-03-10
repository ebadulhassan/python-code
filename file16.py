# v = ("the ","quick ","brown ","fox ","jumps ","over ", "a", "lazy","dog")
# print(v)
# print(type(v))as 


# g =tuple(('helooworld'))
# print(type(g))
# print(g)



v = (("the ","quick ","brown ","fox ","jumps ","over ", "a", "lazy","dog"))
print(v[1])



# Tuple by using constructor
days = tuple (("mon","tues","wed","thurs","fri","sat","sun"))
print(days)





months = tuple (("sat" , "sun" , "mon" , "tues" , "wed" , "thurs" , "fri"))
months_list = list(months)
print(type(months_list))

months_list[1]= "sunday"
print(months_list)
month =tuple(months_list)
print(month)
print(type(month))
