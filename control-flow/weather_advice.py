# weather advice program

# Print the clothing recommendation based on the weather condition provided by the use.

# predfined weather (sunny/rainy/cold)
print ("weather condition is: sunny, rainy or cold")

# define a VAR and prompot the user to to tell about weather case today.
weather = input ("What's the weather like today? (sunny/rainy/cold): ")

# use conditional statement 
if weather == "sunny":
           print (" Wear a t-shirt and sunglasses.")
elif weather == "rainy":
           print ("Dont forget your umbrella and a raincoat.")
elif weather == "cold":
           print ("Make sure to wear a warm coat and a scarf.")
else:
           print ("Sorry, I don't have recommendations for this weather.")
