required_weight = 50
required_height = 170

weight = int(input("enter your weight: "))
height = int(input("enter your height: "))

print (weight == required_weight or height == required_height) 
print(weight == required_weight and height == required_height)
print(weight >= required_weight or height >= required_height)
print(weight <= required_weight and height <= required_height)
