# Ask the user for their name
username = input ("Hello user, what is your name?")

# Ask the user for their favourite integer
fav_num = int(input("What is your favourite integer?"))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2 
squared = fav_num * fav_num

# Greet the user
print("Hello {}, your favourite number is {}".format(username, fav_num))

# Output the results of doubling, halving 
# and squaring their favourite number
print("The double {} is {}". format(fav_num, double))
print("Half of {} is {}". format(fav_num, half))
print("{} squared is {}". format(fav_num, squared))