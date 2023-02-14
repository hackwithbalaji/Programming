#List - muttable
print("List - Muttable")
x = [1,2,3]
print(id(x))
x.append(4)
print(id(x))
print()

#SET - muttable
print("SET - Muttable")
x = {1,2,3}
print(id(x))
x.add(4)
print(id(x))
print()

# When we try to concat in a immutable object, python will create a new object. We can verify it with the id.
#String - Immuttable
print("String - Immuttable")
x = "HELLO"
print(id(x))
x = x + "!"
print(id(x))
print()

#Tuple - Immuttable
print("Tuple - Immuttable")
x = (1,2,3)
print(id(x))
x = x + (4,)
print(id(x))
print()



