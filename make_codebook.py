'''
    Program Description: This program is designed to create code book for word_counter where it produced rules.txt file
    which contains all necessary data for program to analyze speech file which will be created by raspberry pi.

    Author: Bekzod Tolipov, Duc Ngo, Enrique Casillas, Lawrence C, Joel A
    Date: 11/13/2019
'''

# type following to terminal to install: pip install pyspellchecker
# its used to check typo's when program prompts the user for data
from spellchecker import SpellChecker

# Checks the spelling
spell = SpellChecker()


# Validates the input from user if it does NOT
# exceed its limits for words, phrases, and patterns
# allowed (6 words, 4 phrases, 2 patterns with lower bound 2 and upper bound 15)
def validate(input_data, max_input):
    if not input_data:
        print("ERROR: Input size wrong")
        return False

    if len(input_data) > max_input:
        print("ERROR: Input size wrong")
        return False

    return True


# This function receives data input as an array of strings and option which will interprated as if word, phrase or
# pattern is given
def parse_message(input_data, option):
    trimmed_array = []
    temp_array = []
    temp_string_split = []
    caution_msg = "\n--CAUTION: Current word may not return results as expected\n"
    prompt_msg = "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nDo you " \
                 "wish to change it:\n1) Yes\n2) No"
    prompt_choice_wrong_msg = "Given input: (%s) \nPossible spelling: (%s)\nDo you " \
                              "wish to change it:\n1) Yes\n2) No"
    prompt_fixed_word_msg = "Given input: (%s) \nPossible spelling: (%s)\nplease input corrected word: "
    second_chance_msg = "Do you want to change it:\n1) Yes\n2) No"

    if option == 1:     # IF OPTION IS FOR WORD
        if len(input_data.split(" ")) != len(input_data.split(",")):  # Check if number of words is same when parsed
            return False
        else:
            data_array = input_data.split(",")      # Split the given input_data by comma, data_array will hold return
                                                    # string array of words
            corrected_input = ""
            choice_option = ""      # its used to store user's choice for their desired choice
            for x in data_array:    # traverse array of words
                # first IF means it does not match
                if spell.correction(x.strip()) != x.strip():    # Check if spelling is matching after auto correct check
                    display_message(prompt_msg % (x.strip(), spell.correction(x.strip())))    # Prompt if want to change
                    choice_option = read_input()
                    while int(choice_option) != 1 and int(choice_option) != 2:  # If choice not 1 or not 2 ask again
                        display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                        choice_option = read_input()
                    if int(choice_option) == 1:     # User wants to change the word
                        display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                        corrected_input = read_input()
                        # Check the word after user corrects it
                        while spell.correction(corrected_input.strip()) != corrected_input:
                            display_message(prompt_fixed_word_msg % (corrected_input,
                                                                     spell.correction(corrected_input.strip())))
                            corrected_input = read_input()
                        # add the newly modified word into trimmed_array
                        trimmed_array.append(corrected_input.strip())
                    else:   # If user does NOT want to change the word
                        display_message(caution_msg)  # Print caution msg
                        still_dont_want = True  # Raise still dont want
                        display_message(second_chance_msg)    # Ask second time if they still dont want to change it
                        choice_option = read_input()
                        while int(choice_option) != 1 and int(choice_option) != 2:
                            display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                            choice_option = read_input()
                        if int(choice_option) == 1:     # User chose to change the word
                            still_dont_want = False
                            display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                            corrected_input = read_input()
                            while spell.correction(corrected_input.strip()) != corrected_input:
                                display_message(prompt_fixed_word_msg % (
                                    corrected_input, spell.correction(corrected_input.strip())))
                                corrected_input = read_input()
                            # add the newly modified word into trimmed_array
                            trimmed_array.append(corrected_input.strip())
                        if still_dont_want:     # This will be executed only if user does NOT want to change word
                            trimmed_array.append(x.strip())
                else:
                    # add the newly modified word into trimmed_array
                    trimmed_array.append(x.strip())
            # return trimmed_array back
            return trimmed_array
    # Phrases limits only allowed to consist minimum 2 words and maximum 3 words for each phrase
    if option == 2:     # IF OPTION IS FOR PHRASE
        data_array = input_data.split(",")  # Split the given input_data by comma, data_array will hold return
                                            # string array of phrases
        corrected_input = ""
        choice_option = ""
        temp_string = ""
        # Since data_array holds array of phrases we need to check each word in a phrase
        for y in data_array:    # Phrase in phrases
            split_by_space = y.split(" ")  # Split the given phrase "y" and split it by space
            print(len(split_by_space))
            if len(split_by_space) == 1:
                return False
            if 2 < len(split_by_space) > 4:
                return False
            for x in split_by_space:    # Each word in a phrase
                if spell.correction(x.strip()) != x.strip():
                    display_message(prompt_msg % (x.strip(), spell.correction(x.strip())))
                    choice_option = read_input()
                    while int(choice_option) != 1 and int(choice_option) != 2:
                        display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                        choice_option = read_input()
                    if int(choice_option) == 1:
                        display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                        corrected_input = read_input()
                        while spell.correction(corrected_input.strip()) != corrected_input:
                            display_message(prompt_fixed_word_msg % (corrected_input,
                                                                     spell.correction(corrected_input.strip())))
                            corrected_input = read_input()
                        # Create new phrase with fixed word
                        temp_string += (str(corrected_input.strip())) + " "
                    else:
                        display_message(caution_msg)
                        still_no_change = True
                        display_message(second_chance_msg)
                        choice_option = read_input()
                        while int(choice_option) != 1 and int(choice_option) != 2:
                            display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                            choice_option = read_input()
                        if int(choice_option) == 1:
                            still_no_change = False
                            display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                            corrected_input = read_input()
                            while spell.correction(corrected_input.strip()) != corrected_input:
                                display_message(prompt_fixed_word_msg %
                                      (corrected_input, spell.correction(corrected_input.strip())))
                                corrected_input = read_input()
                            temp_string += (str(corrected_input.strip())) + " "
                        else:  # No need for still_no_change anymore can remove it
                            if still_no_change:
                                temp_string += (str(x.strip())) + " "
                else:   # If spelling is correct just copy it
                    temp_string += (str(x.strip())) + " "
            # Each fixed phrase appends into trimmed_array
            trimmed_array.append(temp_string.strip())
            temp_string = ""    # Reset temp_string
        return trimmed_array
    if option == 3:     # IF OPTION IS FOR PATTERN
        temp_array = input_data.split(",")  # First parse it by comma
        temp_value = 0
        temp_string = ""
        for element in temp_array:
            temp_trimmer = []
            temp_string_split = (element.strip()).split(" ")  # Second parse it by space
            if len(temp_string_split) == 4:  # Make sure it has 4 elements
                count = 1
                for x in temp_string_split:  # Check for first two words autocorrect and than 3rd and 4th integer
                    if count == 1 or count == 2:    # First and second element of the pattern
                        ##################### Check words below ###############################
                        if spell.correction(x.strip()) != x.strip():
                            display_message(prompt_msg % (x.strip(), spell.correction(x.strip())))
                            choice_option = read_input()
                            while int(choice_option) != 1 and int(choice_option) != 2:
                                display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                                choice_option = read_input()
                            if int(choice_option) == 1:
                                display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                                corrected_input = read_input()
                                while spell.correction(corrected_input.strip()) != corrected_input:
                                    display_message(prompt_fixed_word_msg %
                                          (corrected_input, spell.correction(corrected_input.strip())))
                                    corrected_input = read_input()
                                temp_string += (str(corrected_input.strip())) + " "
                            else:
                                display_message(caution_msg)
                                still_no_change = True
                                display_message(second_chance_msg)
                                choice_option = read_input()
                                while int(choice_option) != 1 and int(choice_option) != 2:
                                    display_message(prompt_choice_wrong_msg % (x.strip(), spell.correction(x.strip())))
                                    choice_option = read_input()
                                if int(choice_option) == 1:
                                    still_no_change = False
                                    display_message(prompt_fixed_word_msg % (x.strip(), spell.correction(x.strip())))
                                    corrected_input = read_input()
                                    while spell.correction(corrected_input.strip()) != corrected_input:
                                        display_message(prompt_fixed_word_msg %
                                                        (corrected_input, spell.correction(corrected_input.strip())))
                                        corrected_input = read_input()
                                    temp_string += (str(corrected_input.strip())) + " "
                                else:
                                    if still_no_change:
                                        temp_string = (str(x.strip()))
                        else:   # If spelling is correct
                            temp_string = (str(x.strip()))
                        temp_trimmer.append(temp_string.strip())
                    ##################### Check the lower bound and upper bound ###############################
                    if count == 3:  # Lower bound element of the pattern
                        if x.isdigit():  # Is it integer?
                            if int(x) < 2 or int(x) >= 15:  # Allowed min:2 and max:14
                                return False
                            temp_trimmer.append(x)
                            temp_value = int(x)
                        else:
                            return False
                    if count == 4:  # Upper bound element of the pattern
                        if x.isdigit():  # Is it integer?
                            if temp_value > int(x) or int(x) > 15:  # Allowed min:lower_bound and max:15
                                return False
                            temp_trimmer.append(x)
                        else:
                            return False
                    count += 1
            else:       # If pattern contains more than or less than 4 elements
                return False
            trimmed_array.append(temp_trimmer)
        return trimmed_array


# Reads the input from user
def read_input():
    input_data = input()
    return input_data


# Displays the message
def display_message(output_message):
    print(output_message)


def main():
    user_input = ""  # Will get modified overtime can be list or just string
    output_file_name = "rules.txt"
    quit_prompt = False
    MAX_WORDS = 6
    MAX_PHRASES = 4
    MAX_PATTERNS = 2
    PROMPT_FOR_WORDS = "Please input up to 6 words separated by comma',' (word_1, word_2...):"
    PROMPT_FOR_PHRASES = "Please input up to 4 phrases separated by comma',' " \
                         "min:2 words and max:3 words (phrase_1, phrase_2...):"
    PROMPT_FOR_PATTERN = "Please input up to 2 pattern followed by upper-bound=u, lower-bound=l " \
                         "separated by comma',' (word_1 word_2 l u, word_1 word_2 l u...):"
    ERROR_MSG = "ERROR: Given input was wrong please follow the following example:"
    PROMPT_WORD_OPTION = 1
    PROMPT_PHRASE_OPTION = 2
    PROMPT_PATTER_OPTION = 3

    while not quit_prompt:
        display_message(PROMPT_FOR_WORDS)
        user_input = read_input()
        user_input = parse_message(user_input, PROMPT_WORD_OPTION)
        quit_prompt = validate(user_input, MAX_WORDS)
        # Print error message if input is incorrect
        if not quit_prompt:
            display_message(ERROR_MSG)
        else:
            # Output result to a file
            f = open(output_file_name, "w")
            for word in user_input:
                f.write(word + "\n")
            print(user_input)   # Print it to terminal too

    quit_prompt = False  # reset prompter
    while not quit_prompt:
        display_message(PROMPT_FOR_PHRASES)
        user_input = read_input()
        user_input = parse_message(user_input, PROMPT_PHRASE_OPTION)
        quit_prompt = validate(user_input, MAX_PHRASES)
        # Print error message if input is incorrect
        if not quit_prompt:
            display_message(ERROR_MSG)
        else:
            # Output result to a file
            for word in user_input:
                for elem in word:
                    f.write(elem)
                f.write("\n")
            print(user_input)  # Print it to terminal too

    quit_prompt = False  # reset prompter
    while not quit_prompt:
        display_message(PROMPT_FOR_PATTERN)
        user_input = read_input()
        user_input = parse_message(user_input, PROMPT_PATTER_OPTION)
        quit_prompt = validate(user_input, MAX_PATTERNS)
        # Print error message if input is incorrect
        if not quit_prompt:
            display_message(ERROR_MSG)
        else:
            # Output result to a file
            for word in user_input:
                for x in word:
                    f.write(x + " ")
                f.write("\n")
            print(user_input)  # Print it to terminal too
    # Close the file
    f.close()


main()
