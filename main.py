import tkinter
import random
import string

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                     'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
uppercase_letters = []

# Converting letters to Uppercase & storing in a new Array
for letter in lowercase_letters:
    uppercase_letters.append(letter.upper())

# Variables are randomly set & change each time
random_uppercase_letter = uppercase_letters[random.randint(0, 25)]
random_lowercase_letter = lowercase_letters[random.randint(0, 25)]
random_number = random.randint(0, 9)
random_punctuation = string.punctuation[random.randint(0, len(string.punctuation) - 1)]

# All random characters are concatenated
concatenated_characters = (random_uppercase_letter * random.randint(1, 4)) + \
                          (random_lowercase_letter * random.randint(1, 4)) + \
                          (str(random_number) * random.randint(1, 4)) + \
                          (random_punctuation * random.randint(1, 4))
# Characters are converted into an array
list_of_characters = list(concatenated_characters)
# Array is randomly shuffled
random.shuffle(list_of_characters)
# Array is joined together to make new password
final_password = ''.join(list_of_characters)

# Tkinter Window is initialised
window = tkinter.Tk()
window.title("Secure Password Generator")
window.geometry("450x350")

# get_password_text = tkinter.Label(text="Get New Password")
# get_password_text.pack()
#
# password_entry = tkinter.Entry(text="enter password")
# password_entry.pack()
#
# submit_btn = tkinter.Button(text="Refresh", width=10, height=1)
# submit_btn.pack()

# Text is rendered to screen
text = tkinter.Label(text="\n\nYour New Secure Password is\n", justify='center', font=(1,24))
text.pack()
# Secure Password is rendered under text
new_password = tkinter.Label(text=final_password + " \n\n Enjpy!!!", font=(1,24))
new_password.pack()

# Loop ended
window.mainloop()

