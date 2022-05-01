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

def split_name_w_middle_initial(name_w_initial):
    pass



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


def parse_name_and_email(f):
    # names = []
    with open(f) as nl:
        names = nl.readlines()

    for name in names:
        surname, firstname, _island, _timeframe, email = name.split("/")
        
    

mk_first_last(name)
sp_email(email)
organize_chars(mk_passwd(99))

mk_passwd(1)
mk_passwd(2)
mk_passwd(3)

parse_name_and_email('./parse.txt')