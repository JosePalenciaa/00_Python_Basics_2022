print()
print("~~~ Coffee Order Demo ~~~")

keep_going = ""
while keep_going =="":

    print()
    want_coffee = input("Would you like coffee? ").lower()
    if want_coffee != "yes":
        print()
        print("WRONG!, you always want coffee.")
        continue

    else:
        print()
        print("Good Choice!")
        break

print()
print("End of program")
print()