###############################################################################
#   Computer Project 08
#   
#   Covid Obesity Data Organizer
#       prompt for a file
#       output region specific data
#       output data for each country
#       output maximum and minimum statistics for countries
###############################################################################

import csv
from operator import itemgetter

def open_file():
   """
   Attempts to open file until valid file is input
   no parameters taken;
   Returns: file pointer to be read
   """ 
    
   file = input('Input a file: ')       
   while True:        
       try:
           fp = open(file, encoding='utf-8')
           return fp                    #loop continues until file is opened
       
       except FileNotFoundError:   
           print("Error: file does not exist. Please try again.")
           file = input('Input a file: ')

def max_in_region(D,region):
    """
    Determines what country has the highest diabeties per capita
    D: master dictionary of list of lists
    region: key label
    Returns: tuple (string, float)
    """
    
    a_region = D[region]
    max_v = -1000           # arbitrary low number
    max_c = ''
    
    for a_list in a_region:
        capita = a_list[-1] # initialize values
        country = a_list[0]
        
        if capita > max_v:      # loops and replaces values if they are higher
            max_v = capita
            max_c = country
            
        a_tup = (max_c, max_v)  # returns value and country in a tuple
        
    return a_tup

def min_in_region(D,region):
    """
    Determines what country has the lowest diabeties per capita
    D: master dictionary of list of lists
    region: key label
    Returns: tuple (string, float)
    """
    
    a_region = D[region]
    min_v = 1000            # arbitrary high number
    min_c = ''
    
    for a_list in a_region:
        capita = a_list[-1] # initialize values
        country = a_list[0]
        
        if capita < min_v and capita > 0:   # cannot equal zero
            min_v = capita    # loops and replaces values if they are higher
            min_c = country
            
        a_tup = (min_c, min_v)  # returns value and country in a tuple
        
    return a_tup

def read_file(fp):
    """
    Reads file and creates a master dictionary of list of lists
    fp: file information
    Returns: master dictionary of list of lists
    """
    
    dict_of_lists = {}  # initialize variables

    reader = csv.reader(fp)
    next(reader,None)
    for line in reader:         
        region = str(line[1])   #d efines location of region  
        
        if region not in dict_of_lists:
            dict_of_lists[region] = []  # creates new list if region is not yet
                                                        # within master list
        try:
            country = str(line[2])
        except ValueError:              # open these values as certain type
            continue                    # else skip line
        try:
            diabetes = float(line[9])
        except ValueError:
            continue
        
        population = str(line[5])   #  define position and get rid of comma
        population = population.replace(",", "")
        
        try:
            population = float(population)
        except ValueError:
            continue
        
        country_format = [country, diabetes, population]    # organize values
                                                            # as such
        dict_of_lists[region].append(country_format)
    
    for key, value in dict_of_lists.items():
        value.sort()    # iterate through dictionary to organize
    
    
    return dict_of_lists


def add_per_capita(D):
    """
    Adds diabeties per capita onto the values list
    D: master dictionary of list of lists
    Returns: new master dictionary of list of lists
    """
    
    for key, value in D.items(): # iterate through dictionary 
        for a_list in value:
            diabetes = a_list[1]    # define position
            population = a_list[2]
            
            try:
                capita = diabetes / population  # account for zero division error
                a_list.append(capita)
            except ZeroDivisionError:
                a_list.append(0.0)
                
    return D

def display_region(D,region):
    """
    Calls functions and uses them to organize file statistics
    D: master dictionary of list of lists
    region: key label
    Returns: nothing
    """
    
    a_region = D[region]
    region_info = []    # define variables
    countries = []
    
    for value in a_region:  # iterate through each country information
        if value[0] == region:
            region_info = value
        else:                       # account for region data apart from entire set
            countries.append(value)
    
    countries.sort(key=itemgetter(3), reverse = True)   # sort based on diabetes
                                                            # per capita
    max_v = max_in_region(D,region)
    min_v = min_in_region(D,region) # define max and min values from function
    
    
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(region, region_info[1], 
                                                         region_info[2], region_info[3]))
    
    # print out values according to previous steps
    print()
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))
    
    for country in countries:
        print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(country[0], country[1], 
                                                             country[2], country[3]))
    # iterate through list and print each of the countries in the region
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(max_v[0],max_v[1]))    #print max and min
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(min_v[0],min_v[1]))
    
def main():
    
    initial_D = read_file(open_file()) # call read and open file functions 
    D = add_per_capita(initial_D)   # get diabetes per capita on list
    
    for region, values in D.items():    # iterate through master_list
        print("Type1 Diabetes Data (in thousands)")   
        display_region(D,region)    # call the data print function
        print("-"*72)
    print('\n Thanks for using this program!\nHave a good day!')

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()