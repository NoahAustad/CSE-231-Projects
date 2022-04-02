#############################################################################
#   Computer Project 05
#
#   Wave Data and Best Surfing Conditions Calculator
#       prompt for year
#       access corresponding data file
#           loop through file for desired values 
#       calculate the minimum, average, and maximum wave height
#       calculate the best surfing time
#       output results
##############################################################################

def open_file():
    
    """
    Open the corresponding .txt file based on user input.
    no parameters taken; year is assigned within function
    Returns: file pointer, to allow reading of data
    """
    
    year = input("Input a year: ")
    
    
    while True:         # will loop until data file is returned
        try:
            data_list = ("wave_data_" + year + ".txt") # concatenation of input
         
            fp = open(data_list, "r")
    
            return fp
        
        except FileNotFoundError:   
        
            print("File does not exist. Please try again.")
            year = input("Input a year: ")
           
            # loop ends when valid data file is input

def get_month_str(mm):
    
    """
    Replace numeral representation of month with three character abbreviation.
    mm: The value to be converted (str)
    Returns: The three character abreviation of corresponding month
    """

    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
               'Sep', 'Oct', 'Nov', 'Dec']
    
    # replaces number with corresponding item from list ^
    
    if mm == "01":              
        return month_list[0]
    if mm == "02":
        return month_list[1]
    if mm == "03":
        return month_list[2]
    if mm == "04":
        return month_list[3]
    if mm == "05":
        return month_list[4]   
    if mm == "06":
        return month_list[5]
    if mm == "07":
        return month_list[6]
    if mm == "08":
        return month_list[7]
    if mm == "09":
        return month_list[8]
    if mm == "10":
        return month_list[9]
    if mm == "11":
        return month_list[10]
    if mm == "12":
        return month_list[11]
    
    
def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    
    """
    Determines best surfing conditions based on relevant variables.
    mm: representation of month (str)
    dd: representation of day (str)
    hr: representation of hour (int)
    wvht: representation of wave height (float)
    dpd: representation of dominant wave period (float)
    best_(x): comparison values while sorting data (str,str,int,float,float)
    Returns: either of the 5 parameters based on prior standards and conditions
    """
    
    # condtions that determine which set of values get returned
    if hr <= 6 or hr >= 19:
        return best_mm,best_dd,best_hr,best_wvht,best_dpd
    
    if wvht > best_wvht:
        return mm,dd,hr,wvht,dpd
    
    if wvht < best_wvht:
        return best_mm,best_dd,best_hr,best_wvht,best_dpd
    
    if wvht == best_wvht:   # tiebreaker is decided by dpd
        if dpd > best_dpd:
            return mm,dd,hr,wvht,dpd
        else:
            return best_mm,best_dd,best_hr,best_wvht,best_dpd
        
        
def main(): 
    
    """
    Calls relevant functions to output desired wave height data and surf times.
    no parameters taken; used as main driver of program
    Returns: max, min, and best values
    """
    
    print("Wave Data")
    
    fp  = open_file() # access valid data file
    header1 = fp.readline() # skip over the two lines of labeling and units
    header2 = fp.readline()
    
    # initialize variables
    total = 0
    count = 0
    min_wave = 10**6
    max_wave = 0
    mm = ""
    dd = 0
    hr = 0
    wvht = 0
    dpd = 0
    best_mm = ""
    best_dd = 0
    best_hr = 0
    best_wvht = 0
    best_dpd = 0
    
    
    # sort through lines to extract data
    for line in fp:
        mm = str(line[5:7])
        dd = str(line[8:10])
        hr = int(line[11:13])
        wvht = float(line[30:36])
        dpd = float(line[37:42])
        
        
        if wvht == 99.00 or dpd == 99.00:  # continue past spurious values
            continue
        
        # calculations for max and min wave height
        if wvht > max_wave:     
            max_wave = wvht
            
        if wvht < min_wave:
            min_wave = wvht
        
        # calculations for average wave height
        total += wvht
        count += 1
        average = total / count
        
        # calling best_surf to access the best wave data
        best_mm,best_dd,best_hr,best_wvht,best_dpd = best_surf(
            mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd)

    
    # output the wave calculations  
    print("\nWave Height in meters.")   
    print("average: {:.2f}".format(average), "m")
    print("max    : {:.2f}".format(max_wave), "m")
    print("min    :", min_wave, "m")
    
    
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR",
                                                   "WVHT","DPD"))
    
    new_mm = get_month_str(best_mm) # replace numbers with characters
    
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(
        new_mm,best_dd,best_hr,best_wvht,best_dpd))
   
    # display best surfing conditions
    
if __name__ == "__main__": 
    main()
    