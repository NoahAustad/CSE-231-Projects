##############################################################################
#   Computer Project 03
#
#   MSU Tuition Calculator Program
#       prompt for grade level
#       prompt for college
#       prompt for amount of credits
#       calculate tuition based on credits, year, and college acceptance
#       output results
#       prompt user to continue 
##############################################################################

print("2021 MSU Undergraduate Tuition Calculator.\n")

special_fees = 0
taxes = 0

# prompt for grade level and store in variable
grade_level = input("Enter Level as freshman, "
                    "sophomore, junior, senior: ").lower() 

# account for invalid inputs
if grade_level != "freshman" and grade_level != "sophomore" and \
    grade_level != "junior" and grade_level != "senior":
    print("Invalid input. Try again.")
    grade_level = input("Enter Level as freshman,"
                        " sophomore, junior, senior: ").lower() 
    
# account for valid inputs    
while grade_level == "freshman" or grade_level == "sophomore" or \
    grade_level == "junior" or grade_level == "senior":
    
    # condition of junior and senior inputs
    if grade_level == "junior" or grade_level == "senior":
        college_upper = input("Enter college as business, "
                              "engineering, health, sciences, or none: ") 
        
        # condition for james madison prompt
        if college_upper != "business" and college_upper != "engineering":
            james_college = input("Are you in the James "
                                  "Madison College (yes/no): ").lower()
            if james_college == "yes":
                taxes += 7.50
                
        credit = (input("Credits: "))
        
        # account for non number inputs, zeros, and floats
        while not credit.isdigit() or credit <= "0" or credit == float:
            print("Invalid input. Try again.")
            credit = (input("Credits: "))
        else:
            credit = int(credit)   
        
        # taxes based on credit
        if credit >= 6:
            taxes += 29
        else:
            taxes += 24
           
        # include credit rates condition based on college
        if college_upper == "business" or college_upper == "engineering":
        
        
            if credit >= 1 and credit <= 11:
                upper_rate = (573 * credit) 
            elif credit >= 12 and credit <= 18:
                upper_rate = 8595
            elif credit > 18:
                upper_rate = (573 * (credit - 18)) + 8595
            
            # fees based on college
            if college_upper == "business" and credit > 4:
                special_fees = 226
            elif college_upper == "engineering" and credit > 4:
                special_fees = 670
        
        
            if college_upper == "business" and credit <= 4:
                special_fees = 113
            elif college_upper == "engineering" and credit <= 4:
                special_fees = 402
                
        # standard credit rate condition       
        else: 
            
            if credit >= 1 and credit <= 11:
                upper_rate = (555 * credit) 
            elif credit >= 12 and credit <= 18:
                upper_rate = 8325
            elif credit > 18:
                upper_rate = (555 * (credit - 18)) + 8325
            
        
        
        print("Tuition is ${:,.2f}.".format(upper_rate + taxes + special_fees))

        # continue loop
        prompt = input("Do you want to do another calculation (yes/no): ")
        if prompt == "no":
            break
        else:
            grade_level = input("Enter Level as freshman,"
                                " sophomore, junior, senior: ").lower()



    # condition of freshman and sophomore inputs
    elif grade_level == "freshman" or grade_level == "sophomore":
        college_eng = input("Are you admitted to the "
                            "College of Engineering (yes/no): ").lower()
        if college_eng != "yes":
            college_eng == "no"
            james_college = input("Are you in the James "
                                  "Madison College (yes/no): ").lower()
        credit = (input("Credits: "))
    
        # account for non number inputs, zeros, and floats
        while not credit.isdigit() or credit <= "0" or credit == float:
            print("Invalid input. Try again.")
            credit = (input("Credits: "))
        
        else:
            credit = int(credit)
    
        # tax rates based on credit 
        if credit >= 6:
            taxes = 29
        else:
            taxes = 24
            
        # condition of rate based on freshman year and credit
        if grade_level == "freshman":
            if credit >= 1 and credit <= 11:
                rate = (482 * credit) 
            elif credit >= 12 and credit <= 18:
                rate = 7230
            elif credit > 18:
                rate = (482 * (credit - 18)) + 7230
        
        # condition of rate based on sophomore year and credit
        elif grade_level == "sophomore":
            if credit >= 1 and credit <= 11:
                rate = (494 * credit) 
            elif credit >= 12 and credit <= 18:
                rate = 7410
            elif credit > 18:
                rate = (494 * (credit - 18)) + 7410
    
        # special fees based on college 
        if college_eng == "yes":
            if credit > 4:
                special_fees = 670
            elif credit <= 4:
                special_fees = 402
        else:
            special_fees = 0 
        
        
        print("Tuition is ${:,.2f}.".format(rate + taxes + special_fees))
       
        # continue loop
        prompt = input("Do you want to do another calculation (yes/no): ")
        if prompt == "no":
            break
       
        grade_level = input("Enter Level as freshman,"
                            " sophomore, junior, senior: ").lower()