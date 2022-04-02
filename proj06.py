##############################################################################
#   Computer Project 06
#
#   Billboard Music Ranking System
#       prompt for a file name
#       output file in current ranking order
#       display options and prompt for listed option
#       utilize input to output the correct organization structure
#       loop display and prompt
##############################################################################

import csv
from operator import itemgetter

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"


def get_option():
    
    """
    Prompts for value and determines whether value is valid or invalid.
    no parameters taken;
    Returns: valid prompt value
    """
    
    print(OPTIONS) # display the options that the user can choose
    
    prompt = input("Enter one of the listed options: ").lower()
    
    valid_prompt = ["a","b","c","d","q"]
    
    while True: # loops through until it can return valid prompt
        
        if prompt == valid_prompt[0]:   # returns in each instant
            return prompt
        if prompt == valid_prompt[1]:
            return prompt
        if prompt == valid_prompt[2]:
            return prompt
        if prompt == valid_prompt[3]:
            return prompt
        if prompt == valid_prompt[4]:
            return prompt

        else:
            print("Invalid option!\nTry again")  # resets and loops
            prompt = input("Enter one of the listed options: ").lower()

def open_file():
    
    """
    Prompts for a file and attempts to open file.
    no parameters taken;
    Returns: file pointer designated for reading
    """

    file = input('Enter a file name: ')
    
    while True:        # loops until a file can be opened
        try:
            fp = open(file, "r")
            return fp
        
        except FileNotFoundError:   # if file cannot be opened prompt again
        
            print("\nInvalid file name; please try again.\n")
            file = input('Enter a file name: ')
           
def read_file(fp):
    
    """
    Read the file and assign index values to be interated through within list.
    fp: file pointer; acquired through open_file() function to open file
    Returns: new list with song information embedded each index value
    """
        
    master_list = []        # new list to append values
       
    
    reader = csv.reader(fp)
    next(reader,None)
    for line in reader:
        song = str(line[0]) # identify each of the the variables within the 
        artist = str(line[1])                                       #structure
        rank = line[2]
        last_week = line[3]
        peak = line[4]
        weeks = line[5]
        
            # account for situations when value cannot be opened as int
        try:
            rank = int(line[2])
        except ValueError:
            rank = -1
        try:
             last_week = int(line[3])
        except ValueError:
             last_week = -1
        try:
             peak = int(line[4])
        except ValueError:
             peak = -1
        try:
            weeks = int(line[5])
        except ValueError:
            weeks = -1
        
        
        list_format = [song, artist, rank, last_week, peak, weeks]
        # append this^ format to the new list
        master_list.append(list_format)
 
        
    return master_list
        
def print_data(song_list):
    
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    
    """
    Sorts through master_list and returns a list of the christmas songs
    master_list: list of lists created by file and manipluated for data
    Returns: list of christmas songs
    """
        
    christmas_list = [] # new list to be compiled from master list information
    
    christmas_words = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                       'wonderful time', 'santa', 'reindeer']
      
    for line in master_list:
        song = line[0]  # if index value of list exists in song, then append it
        if christmas_words[0] in song.lower():
            christmas_list.append(line)
        if christmas_words[1] in song.lower():
            christmas_list.append(line)
        if christmas_words[2] in song.lower():
           christmas_list.append(line)
        if christmas_words[3] in song.lower():
            christmas_list.append(line)
        if christmas_words[4] in song.lower():
            christmas_list.append(line)
        if christmas_words[5] in song.lower():
           christmas_list.append(line)
        if christmas_words[6] in song.lower():
            christmas_list.append(line)
        if christmas_words[7] in song.lower():
            christmas_list.append(line)
            
    christmas_list.sort()       # sort alphabetically
    return christmas_list
            
def sort_by_peak(master_list):
    
    """
    Creates new list based on where song places in the category: peak rank
    master_list: list of lists created by file and manipluated for data
    Returns: list sorted by peak rank
    """
    
    peak_list = [] # new list to be organized, but based on master list
    
    for line in master_list:
        peak_rank = line[4]     # identify peak rank, account for -1
        if peak_rank == -1:
            continue

        peak_list.append(line)  # append that line to peak list
        
    peak_list.sort(key=itemgetter(4)) # sort based on the value at index 4
        
    return peak_list

def sort_by_weeks_on_list(master_list):
    
    """
    Creates new list based on where song places in the category: weeks on list
    master_list: list of lists created by file and manipluated for data
    Returns: list sorted by how many weeks the song has spent on list
    """
    
    weeks_on_list = []
    
    for line in master_list:
        weeks_on = line[5] # identify where weeks on list value arises
        if weeks_on == -1:
            continue

        weeks_on_list.append(line) # append the line to the new list


    weeks_on_list.sort(key=itemgetter(5), reverse = True) # reverse the order
        
    return weeks_on_list
        
def song_score(song):
    
    """
    Calculates a score based on criteria like peak rank, weeks on chart, etc.
    song: song within list; along with the corresponding data
    Returns: the score that each song earned
    """
        
    A,B,C,D = 1.5, -5, 5, 3
    
    for line in song:
        
        curr_rank = song[2]   # find what position / index value rank is derived
        
        if curr_rank >= 0: # reverse and compensate for high listed values 
            curr_rank = 100 - curr_rank 
        else:
            curr_rank = -100
        
        
        peak_rank = song[4] # how to derive peak rank via index
        
        if peak_rank >= 0:
            peak_rank = 100 - peak_rank
        else:
            peak_rank = -100
        

        rank_delta = song[2] - song[3] # change in rank is done with subtraction

        weeks_on_chart = song[5] # weeks on chart is song at index position 5
    
    # score formula
    score = A * peak_rank + B * rank_delta + C * weeks_on_chart + D * curr_rank
            
    return score

def sort_by_score(master_list):
    
    """
    Create a new list ranked based on the song score recieved from song_score()
    master_list: list of lists created by file and manipluated for data
    Returns: new master list ranked by song score
    """
    
    master_list_sort = [] 
    
    new_master = []
    
    for line in master_list: 
        score = song_score(line)  # finding the basis of ranking (score)
        master_list_sort.append(line + [score]) # new list with score appended
    
    # sort first based on score, then on song name
    master_list_sort.sort(key=itemgetter(-1,0), reverse = True)
    
    # append all the values except for the score to a new list and return it
    for line in master_list_sort:
        new_master.append(line[:-1])

    return new_master
    
def main():
    
    """
    Opens relevant functions and displays data; continues to loop through
    no parameters taken;
    Displays the corresponding list of values sorted accordingly
    """
    print("\nBillboard Top 100\n")
    
    fp = open_file()        # open and read file 
    master_list = read_file(fp)
    
    print_data(master_list) # print untouched rankings
    
    option = get_option() # give option to view functions
    
    christmas_songs = 0
    all_songs = 0
    
    while not option == "Q" or option == "q":
        
        
        if option == "a":
            new_list = get_christmas_songs(master_list) 
            print_data(new_list) # prints list of christmas songs with function
            
            for number in new_list:  # keep track of these values within lists
                christmas_songs += 1
            for number in master_list:
                all_songs += 1
                
            # formula for percentage calculation
            percent = ((christmas_songs * 100) // all_songs)
            
            # check whether list is empty, or whether to display the percentage
            if len(new_list) == 0:
                print('None of the top 100 songs are Christmas songs.')
            else:
                print('\n{:d}% of the top 100 songs are Christmas songs.'.format(percent))
                
            # loop and reprompt 
            print(OPTIONS)
            option = input("Enter one of the listed options: ").lower()
            
            
        
        # each of the remaining options excluding "q" require calling the 
        # required functions to sort via input method
        
        if option == "b":
            new_list = sort_by_peak(master_list) 
            print_data(new_list)
            print(OPTIONS)
            option = input("Enter one of the listed options: ").lower()
            
        
        if option == "c":
            new_list = sort_by_weeks_on_list(master_list)
            print_data(new_list)
            print(OPTIONS)
            option = input("Enter one of the listed options: ").lower()
            
        
        if option == "d":
            new_list = sort_by_score(master_list)
            print_data(new_list)
            print(OPTIONS)
            option = input("Enter one of the listed options: ").lower()
            
        
    
        if option == "Q" or option == "q":
            print("\nThanks for using this program!\nHave a good day!\n")
            break
        
    
    
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           