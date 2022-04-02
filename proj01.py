###########################################################################
#   Computer Project 01
#
#  Unit Conversion Program
#    prompt for a float in rods
#    input a number
#    convert number into various units
#    round conversions to three decimal points
#    output various conversions
###########################################################################


rods_float = float(input ( "Input rods: " ) ) 
print( "You input", rods_float ,"rods." )

# convert rods into various units using conversion rates in relation to rods
meters_float = rods_float * 5.0292
feet_float =  rods_float * 16.5
miles_float = rods_float * 0.00312528
furlongs_float = rods_float * 0.025
walktime_float = rods_float * 0.0604851

# output corresponding values with their labels, rounded to 3 decimal points
print( "\nConversions",)
print( "Meters:", round(meters_float, 3))
print( "Feet:", round(feet_float, 3 ))
print( "Miles:", round(miles_float, 3))
print( "Furlongs:", round(furlongs_float, 3))
print( "Minutes to walk", rods_float ,"rods:", round(walktime_float, 3))
