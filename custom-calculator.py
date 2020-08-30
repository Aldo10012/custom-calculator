import math

# Intro 
print("The year is 2183 and the USA is at war with Russia!")
print()
print("After returning from a top-secret mission, a small group of spies has located the location of Russia’s secret base. The Commander-In-Chief has ordered an orbital strike directly on that base. However, resources have dwindled due to the war and you don’t have the equipment to build a powerful missile.")
print()
print("The government has hired you, an engineer for the Department of Defence(DD), to create an alternative weapon to use during the orbital strike.")
print()
print("You, and your ingenious brain, propose an idea: instead of building a missile, you just apply basic physics. Force is equal to mass times acceleration, so why not just drop a really heavy object from space! Luckily, the DD happens to have a massive inventory of osmium, the densest chemical element.")
print()
print("YOUR OBJECTIVE:")
print("You will design a cylindrical rod of osmium, determine its dimensions, and decide what altitude to drop it from. From that data, we can determine how much force the osmium will produce. Once you have completed that, the Space Force will take several of your osmium rods into orbit and launch an orbital strike")
print("")
print("If all goes well, this could end the war.")
print()
print()
print("---------------------------------------------------------------------")
print()

# enter values for calculations:
radius_m = float(input("Enter radius of osmium tube in meters: "))
length_m = float(input("Enter length of osmium tube in meters: "))
hight_km = float(input("Enter hight in kilometers: (For point of reference, the ISS is 408 km high) "))

# formulas used for final calculation, math for formulas done on paper
surface_area_m = math.pi * (radius_m ** 2)
volume_m = surface_area_m * length_m
# mass = volume * density. Density of osmium is 22.59 grams per cm^3, or 225700 grams per m^3
mass_g = volume_m * 225900      
mass_lb = mass_g/0.0022   

# acceloration of gravity is 9.8 m/s^2, or 0.0098 km/s^2
# a(t) = -0.00981                    equation for misile asseloration
# v(t) = -0.00981t                   equation for misile velocity
# p(t) = -0.0049t^2 + hight          equation for misile position
# t = math.sqrt(hight/0.0049).       equation for how long it take's for tube to hit ground 
# acceloration = (9.8 * t)*100       calculate deceloration at moment of impace (assuming it tales 1/100th of a second to come to a complete stop)

# formulas to calculate the force of impact
time_sec = math.sqrt(hight_km/0.0049)    
acceloration = (9.8 * time_sec)*100
force_newtons = mass_g * acceloration
force_megaton = force_newtons / 9806650000


print()
print("---------------------------------------------------------------------")
print()
print("Information regarding your osmium misile:")

print("radius: ", radius_m, "meters")
print("length: ", length_m, "meters")
print("hight: ", hight_km, "km")
#print("volume: ", volume_m, 'cm^3')
print("volume: ", (round(volume_m * 100)/100), "cubic meters")
#print("mass in grams: ", mass_g, "grams")
print("mass in grams: ", (round(mass_g * 100)/100), "grams")
#print("mass in lbs: ", mass_lb, "lb's")
print("mass in lbs: ", (round(mass_lb * 100)/100), "pounds")

print()
print("---------------------------------------------------------------------")
print()
print()
print("It will take about", (round(time_sec * 100)/100), "seconds for the osmium misile to hit the target")
print()
print("The Osmium misile will hit the target with a force of about", (round(force_megaton * 100)/100), "megatones of force")

print()
print("---------------------------------------------------------------------")
print()
print()
print("Congradulations!")
print("Your designs worked and the srike has gone according to plan. Russia has declared its surrender and our soldiers can finaly return home. You did your country a great service.")
