def triangle_sides(a,b,c):
   if (a + b) > c and (b + c) > a and (a + c) > b:
    print("ეს სამკუთხედი არსებოსბს")
   else:
    print(" ეს სამკუთხედი არ არსებობს ")
triangle_sides(2,3,4)    




y="სანდრო გიო ნიკა ელენე მათე"
x= y.split(" ")
print(x)



def split_string(names_string):
  names = names_string.split()
  print(names)
names = "dato nene megi"
split_string(names)