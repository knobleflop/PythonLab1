import math
# question 1
r = 5
a = math.pi * r**2
r = 3
v = (4 / 3) * math.pi * r**3
a_side = 3
b_side = 4
c_side_sq = a_side**2 + b_side**2
pyt = math.sqrt(c_side_sq)
print(a, v, pyt)
# question 2
first_name = "Joseph"
last_name = "Long"
full_name = first_name + ' ' + last_name
name_length = len(full_name)
print(name_length, full_name, full_name.upper(), full_name.lower())
# question 3
age = 38
height = 5.5
weight = 140
height_in = height * 12
print(type(age), type(height), type(weight))
bmi = (weight / height_in**2) * 703
print(bmi)



