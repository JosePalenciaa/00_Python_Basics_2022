print()
print("~~~ Coffee Order Demo ~~~")

keep_going = ""
while keep_going =="":

    want_coffee = input("Would you like coffee? ")
    if want_coffee != "yes":
        print("WRONG!, you always want coffee.")
        continue

    else:
        print("Good Choice!")
        break

print()
print("End of program")
print()