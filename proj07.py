##############################################################################
#   Computer Project 07
#   
#   Country Regime and Allies Program
#       prompt for a file
#       output options 1-3 and prompt for desired option
#       call corresponding function for option loop
#       loop options and prompt until q or Q
##############################################################################

import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''
    
def open_file():
    ''' 
    Attempts to open file until valid file is input
    no parameters taken;
    Returns: file pointer to be read
    '''
    
    file = input("Enter a file: ") 
    
    while True:             #loop continues until file is opened
        try:
            fp = open(file, "r")
            return fp
        except FileNotFoundError:
            print("File not found. Please try again.")
            file = input("Enter a file: ")

def read_file(fp):
    ''' 
    Reads file and creates two lists full of the country names and regime info
    fp: file information for extraction and manipulation
    Returns: country_names - list of countries ; list_of_regimes_lists - 
    list of lists with regime number history for each country
    '''
        
    country_names = []
    list_of_regimes_lists = []          #first two lists will be returned
    political_regime = []       #used to make list of lists with ints
    
    reader = csv.reader(fp)
    next(reader,None)       #skip the first line
    for line in reader:
        country = str(line[1])      #define location of each value
        regime = int(line[4])
        
        if country not in country_names:
            if len(country_names) != 0:     #loop to compile list
                list_of_regimes_lists.append(political_regime)
            country_names.append(country)
            political_regime = [regime]
            
        else:
            political_regime.append(regime) #to account for final country's regimes
            continue
    
    list_of_regimes_lists.append(political_regime)
    
    return country_names, list_of_regimes_lists
    
def history_of_country(country,country_names,list_of_regime_lists):
    ''' 
    Determines what regime is most prevelant in country history
    country: input from user
    country_names: compiled in read_file()
    list_of_regime_lists: compiled in read_file()
    Returns: most prevalent regime for a given country
    '''
    
    index = country_names.index(country)    #index based on country input
    
    small_list = list_of_regime_lists[index]    #compile smaller list for each
                                                #country's prevelant regime
    count_0 = small_list.count(0)
    count_1 = small_list.count(1)
    count_2 = small_list.count(2)
    count_3 = small_list.count(3)
    
    most_count = max(count_0, count_1, count_2, count_3)
                                                #^determines which value appears most
    if count_0 == most_count:
        return REGIME[0]
    if count_1 == most_count:       #returns the regime that appears most
        return REGIME[1]
    if count_2 == most_count:
        return REGIME[2]
    if count_3 == most_count:
        return REGIME[3]

def historical_allies(regime,country_names,list_of_regime_lists):
    '''
    Compiles a list of allies for a given country
    regime: user input
    country_names: compiled in read_file()
    list_of_regime_lists: compiled in read_file()
    Returns: sorted list of allies
    '''
        
    allies = []     #allies will be returned
    
    for country in country_names:
        if regime == history_of_country(country,country_names,list_of_regime_lists):
            allies.append(country)  #if the regime is what appears most then 
                                    # it becomes a value in allies
    allies.sort()
    
    return allies

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    """
    Determines the country with most coups
    top: user input
    country_names: compiled in read_file()
    list_of_regime_lists: compiled in read_file()
    Returns: amount of coups based on desired top value
    """
    
    coup_detat = [] # list of most coups will be returned
    
    
    for i in range(len(list_of_regime_lists)):  
        regime_list = list_of_regime_lists[i]
        country = country_names[i]  #define the location of regimes and country
        count = 0
        
        for i in range(1, len(regime_list)):
            if regime_list[i-1] != regime_list[i]: # for all values not equal 
                count += 1                          #to previous values
                                                    #add to count for that country
        tup = (country, count)      #return values in correct format 
        coup_detat.append(tup)
        
    
    coup_detat.sort(key=itemgetter(1), reverse = True)  #sort from highest to 
                                                #lowest based on count
    
    
    return coup_detat[:int(top)] #return for values through user input
    
def main():

    fp = open_file()        #access file for manipulation
    country_names, list_of_regimes_list = read_file(fp) 
            #retreve these varaibles
    print(MENU)
    
    while True: #endless loop only breaks if q or Q is entered vv
        
        option = input("Input an option (Q to quit): ")
        
        if option == "q" or option == "Q":
            print("The end.")
            break
    
        if option == "1":
            
            country = input("Enter a country: ")    # retrieve country from input
            while country not in country_names:
                print("Invalid country. Please try again.") #account for invalid
                country = input("Enter a country: ")
            else:
                regime = history_of_country(country,country_names,list_of_regimes_list)
                
                #call function and format return values correctly
                if regime == "Electoral democracy" or regime == "Electoral autocracy":
                    print("\nHistorically {} has mostly been an {}".format(country,regime))
                if regime == "Liberal democracy" or regime == "Closed autocracy":
                    print("\nHistorically {} has mostly been a {}".format(country,regime))
                 
                print(MENU)
                
                
        if option == "2":
            
            regime = input("Enter a regime: ")
            while regime not in REGIME:
                print("Invalid regime. Please try again.") #account for invalid
                regime = input("Enter a regime: ")
            else:
                allies = historical_allies(regime,country_names,list_of_regimes_list)
                
                #call function and format return values correctly
                historic_allies = "\nHistorically these countries are allies of type:"
                print(historic_allies, regime)
                print(", ".join(allies))
                
                print(MENU)
    
    
        if option == "3":
            
            top = input("Enter how many to display: ")
            while top.isdigit() == False or (type(top) == int and int(top) < 0):
                print("Invalid number. Please try again.") #account for invalid
                top = input("Enter how many to display: ")
            else:
                list_of_countries = top_coup_detat_count(top, country_names,list_of_regimes_list)
                
                #call function and format return values correctly
                print("\n{0: >25} {1: >8}".format("Country", "Changes"))
                for data in list_of_countries:
                    print("{0: >25} {1: >8}".format(data[0],data[1]))
                
                print(MENU)
    
  

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main() 