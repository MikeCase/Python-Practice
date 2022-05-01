# Practicing working with strings
import random
import string

name = "Johnny Pneumonic"
email = "johnny@pneumonic.org"
website = "www.example.com"
ip_address = "192.168.1.67"
txt_string = "This is a sentence."
phone_num = "555-555-5555"

# Seperating names into first middle and last
def mk_first_last(name):
    split_name = name.split(" ")
    last_name = split_name[-1]
    first_name = split_name[0]
    middle_initial = (split_name[1] if len(split_name) > 2 else None)

    print(f"First Name:\t{first_name}\nMiddle Initial:\t{(middle_initial if middle_initial != None else '')}\nLast Name:\t{last_name}\n")


#split email address into user and host
def sp_email(email):
    user, host = email.split("@")
    print(f"User:\t{user}\nHost:\t{host}\n")


# Generate random password
def mk_passwd(cmplx):
    pwd_complexity = cmplx
    gen_pwd = ''

    # Given the complexity integer of this function
    # perform an action based on the complexity integer.
    if pwd_complexity == 1:
        for i in range(4):
            gen_pwd += random.choice(string.ascii_lowercase)
            
    if pwd_complexity == 2:
        for i in range(10):
            gen_pwd += random.choice(string.ascii_letters)

    if pwd_complexity == 3:
        for i in range(20):
            all_chars = string.ascii_letters+string.digits+string.punctuation
            gen_pwd += random.choice(all_chars)

    if pwd_complexity == 99:
        for i in range(32):
            all_chars = string.ascii_letters+string.digits+string.punctuation
            gen_pwd += random.choice(all_chars)
    
    # Return the generated password 
    # so's I can use it in the organize_chars() function. 
    return gen_pwd


#given a random string of characters, separate into classes(upper, lower, digit, punctuation)
def organize_chars(random_txt):
    upper_case = ''
    lower_case = ''
    punctuations = ''
    digits = '' # Initialize lists for characters.
    print('\nCatagorization of characters in given string:')
    print(f'Given string: {random_txt}')
    # Loop through characters in string
    # If character is found in string.caracter_class
    # Add to appropriate list. 
    for c in random_txt:
        if c in string.ascii_lowercase:
            lower_case += c
            lower_case = ''.join(sorted(lower_case))
        if c in string.ascii_uppercase:
            upper_case += c
            upper_case = ''.join(sorted(upper_case))
        if c in string.digits:
            digits += c
            digits = ''.join(sorted(digits))
        if c in string.punctuation:
            punctuations += c
            punctuations = ''.join(sorted(punctuations))


    # I should return this but I'm just printing
    print(f"Lower Case:\t{lower_case}\nUpper Case:\t{upper_case}\nDigits:\t\t{digits}\nPunctuation:\t{punctuations}\n")

def count_duplicates_string(s):
    """
    Count the duplicate characters in a string. 

    @param: s = String you want to count the duplicates in
    
    count_duplicates_string(character_string) -> [char, int]
    """

    print("Duplicate characters in a given string: ");
    print(f'Given string: {s}')

    # Found on the interwebs.. 
    # Going to try to understand and break it down. 

    # Go through the length of the string
    for i in range(0, len(s)):
        # Set count to equal 1 instead of starting from 0
        count = 1;
        # Go through the entire range of the characters again
        # increment i + 1, so j=i+1
        for j in range(i+1, len(s)):
            # Check to see if the current character is equal to the next character
            # Also 
            if(s[i] == s[j] and s[i] != ' '):
                count = count + 1;
                s = s[:j] + '0' + s[j+1:];
        
        if(count > 1 and s[i] != '0'):
            print(s[i]," - ",count);

        

def parse_name_and_email(f):
    # Format of parse.txt:
    # <SURNAME>/<FIRSTNAME>/<LOCATION>/<TIMEFRAME>/<EMAILADDRESS>
    # Simple right?..

    with open(f) as nl:
        names = nl.readlines()

    for name in names:
        surname, firstname, _location, _timeframe, email = name.split("/")
        
pwd = mk_passwd(99)

mk_first_last(name)
sp_email(email)

mk_passwd(1)
mk_passwd(2)
mk_passwd(3)

parse_name_and_email('./parse.txt')

count_duplicates_string(pwd)
organize_chars(pwd)