# asks three questions, website name, action, device
website_name = input("What website you need your new password for? ")
action = input("What action do you do on this website? ")
device = input("What device do you perform this action on? ")

# creates the password string
password_string = "" # sets empty quote to password_string
for letter in website_name:
    if not letter in "aeiouAEIOU": # removes vowels
        password_string += letter # adds value to variable (website_name) to password_string
        password_string = password_string.upper() # function onto variable
        password_string = password_string[0:2] # setting new variable as first two letters
        
# abbreviate password_string into a two letter phrase
site_abbreviation = password_string # setting variable to password_string
letters_in_site_name = len(website_name) # counting letters in website_name and outputs a number

# creates the verb for the password
verb = "" # empty string
for letter in action: # for loop
    if not letter in "aeiouAEIOU": # removes vowels
        verb += letter 
        verb = verb.lower() # lowercasing letters
        verb = verb.replace(" ","") # removes space from verb

# creates the subject for the password
subject = ""
for letter in device:
    subject = device.upper()

# adds two special characters to the password based on the first letter of the website name
specials = ""
letter = website_name[0]
if letter.lower() in "abcd":
    specials = "!@"
if letter.lower() in "efgh":
    specials = "#$"
if letter.lower() in "ijkl":
    specials = "%^"
if letter.lower() in "mnop":
    specials = "&*"
if letter.lower() in "qrstuvwxyz":
    specials = "()"


# f string, evaluate variable within the string
# puts multiple variable inside a string, calls them all before printing
print(f'{website_name} is where I {action} on my {device}') # prints website_name, action, device and forms it into a sentence

print(f'Your password is {site_abbreviation +str(letters_in_site_name) + verb + subject + specials}') # prints password
