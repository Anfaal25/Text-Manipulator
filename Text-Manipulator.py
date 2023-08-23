# String Manipulator
# Terminal based program that changes/ manipulates the string inputted by the user according to the choice made by the user from the list of options presented to said user.

def print_menu():
    print('Menu')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix Capitalization')
    print('s - Shorten spaces')
    print('q - Quit')
    print('')

def get_num_of_non_WS_characters(user_input_string):
    num_of_non_ws_characters = sum(1 for char in user_input_string if not char.isspace())
    print('Number of non-Whitespace characters:', num_of_non_ws_characters)

def get_num_of_words(user_input_string):
    user_input_string_lst = user_input_string.split()
    num_of_words = len(user_input_string_lst)
    print('Number of words:', num_of_words)

def fix_capitalization(user_input_string):
    user_input_string_lst = user_input_string.split('. ')
    user_input_string_lst = [sentence.capitalize() for sentence in user_input_string_lst]
    num_of_letters_capitalized = len(user_input_string_lst)
    print('Number of letters capitalized:', num_of_letters_capitalized)
    print('Edited text:', '. '.join(user_input_string_lst))
    return '. '.join(user_input_string_lst)  # Return the edited text


def shorten_space(user_input_string):
    Edited_input = ' '.join(user_input_string.split())
    print('Edited text:', Edited_input)
    return Edited_input  # Return the edited text


def execute_menu(user_input_string):
    while True:
        print_menu()
        user_choice = input('Choose an option:')
        if user_choice == 'c':
            get_num_of_non_WS_characters(user_input_string)
        elif user_choice == 'w':
            get_num_of_words(user_input_string)
        elif user_choice == 'f':
            user_input_string = fix_capitalization(user_input_string)
        elif user_choice == 's':
            user_input_string = shorten_space(user_input_string)
        elif user_choice == 'q':
            break

## Main Program 
print('Enter a sample text:')    
user_input_string = input()
print('You entered:', user_input_string)
execute_menu(user_input_string)
