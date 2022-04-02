######################################################################
#   Computer Project 02
#
#   Forza Rental Feature Program
#       prompt the user to continue
#       prompt for a classification code
#       prompt for other relevant information
#       use classification code to calculate rates
#       use difference in odometer output to calculate mileage 
#       calculate values using classification code rates and mileage
#       output rental summary
#       prompt the user to continue
#
#######################################################################

import math

# introduce inputs with banner
BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"

print(BANNER)

# prompt for one of two characters
PROMPT = input("\nWould you like to continue (A/B)? ")

if PROMPT == "B":
    print("Thank you for your loyalty.")
    
while PROMPT == "A":
    
    # input for character code which can determine payment rates
    player_code = input("\nCustomer code (BD, D, W): ")
    
    # account for invalid characters
    while player_code != "BD" and player_code != "D" and player_code != "W":
        print("\n\t*** Invalid customer code. Try again. ***")
        player_code = input("\nCustomer code (BD, D, W): ")
        
    # prompt for the remaining values relevant to the calculation    
    days = int(input("\nNumber of days: "))
    initial_odom = int(input("Odometer reading at the start: "))
    end_odom = int(input("Odometer reading at the end:   "))
    
    # total miles standard equation
    total_miles = float((end_odom - initial_odom) / 10)
        
    # total miles if initial odometer reading is greater than final reading
    if initial_odom > end_odom:
        total_miles = float(((end_odom + 1000000) - initial_odom) / 10)
    
    
    # define the equations and cost of various classification codes:
    # condition of player code determines mathematical expressions
    
    if player_code == "BD": # budget rate
      amount_due = (0.25 * total_miles) + (40 * days)
        
    elif player_code == "D": # daily rate
        if total_miles <= 100:
            amount_due = (60 * days)
        elif total_miles > 100:
            amount_due = (0.25 * (total_miles - (100 * days)) + (60 * days))
  
    # condition of total_miles determines amount due
    # weekly rate requires weeks to be rounded and accounted for in equations
    elif player_code == "W": # weekly rate
        weeks = days / 7
        weeks_round = math.ceil(weeks)  
        if total_miles <= 900:       
            amount_due = weeks_round * 190
        elif total_miles > 900 and total_miles <= 1500 * weeks_round:
            amount_due = (weeks_round * 190) + (weeks_round * 100)
        elif total_miles > 1500 * weeks_round:
            amount_due = ( (weeks_round * 190) + (weeks_round * 200) + 
                          ((total_miles - (1500 * weeks_round)) * 0.25) )
    

    # print results and prompt continuation with two characters                  
    print("\nCustomer summary:")
    print("\tclassification code:", player_code)
    print("\trental period (days):", days)
    print("\todometer reading at start:", initial_odom)
    print("\todometer reading at end:  ", end_odom)  
    print("\tnumber of miles driven: ", total_miles  )
    print("\tamount due: $", float(amount_due)  )  
    
    PROMPT = input("\nWould you like to continue (A/B)? ")  
    
    if PROMPT == "B":
        print("Thank you for your loyalty.")