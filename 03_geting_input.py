# Asl the user for their name
username = input ("Hajimemashite, what is your name?")

# Ask the user for their favourite integer
fav_num = int(input("What is your favourite integer?"))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2 
squared = fav_num * fav_num

# Greet the user
print("Konnichiwa {}, your favourite number is {}".format(username, fav_num))

# Output the results of doubling, halving 
# and squaring their favourite number
print("Double {} is {}". format(fav_num, double))
print("Half {} is {}". format(fav_num, half))
print("Squared {} is {}". format(fav_num, squared))