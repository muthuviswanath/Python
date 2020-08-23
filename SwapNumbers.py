# Get the values of a and b from the user
a = int(input("Enter the value for the first number: "))
b = int(input("Enter the value for the second number: "))

#printing the values of a and b
print("Values of a and b before swapping")
print("---------------------------------")
print(f"Value of a : {a}")
print(f"Value of b : {b}")

#swapping the values
a,b = b,a

#printing the values of a and b
print("Values of a and b before swapping")
print("---------------------------------")
print(f"Value of a : {a}")
print(f"Value of b : {b}")
