# type following to terminal to install: pip install pyspellchecker
from spellchecker import SpellChecker
# Checks the spelling
spell = SpellChecker()


def validate(input_data, max_input):
    if not input_data:
        print("input size wrong")
        return False

    if len(input_data) > max_input:
        print("input size wrong")
        return False

    return True


def parse_message(input_data, option):
    trimmed_array = []
    temp_array = []
    temp_string_split = []

    if option == 1:
        if len(input_data.split(" ")) != len(input_data.split(",")):     # Check if number of words is same when parsed
            return False
        else:
            data_array = input_data.split(",")
            corrected_input = ""
            choice_option = ""
            for x in data_array:
                if spell.correction(x.strip()) != x.strip():
                    print("Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nDo you "
                          "wish to change it:\n1) Yes\n2) No" % (x.strip(), spell.correction(x.strip())))
                    choice_option = input()
                    while int(choice_option) != 1 and int(choice_option) != 2:
                        print(
                            "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nDo you "
                            "wish to change it:\n1) Yes\n2) No" % (x.strip(), spell.correction(x.strip())))
                        choice_option = input()
                    print(choice_option)
                    if int(choice_option) == 1:
                        print(
                            "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nplease input corrected word: " % (
                                x.strip(), spell.correction(x.strip())))
                        corrected_input = input()
                        while spell.correction(corrected_input.strip()) != corrected_input:
                            print(
                                "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nplease input corrected word: " % (
                                corrected_input, spell.correction(corrected_input.strip())))
                            corrected_input = input()
                        trimmed_array.append(corrected_input.strip())
                    else:
                        trimmed_array.append(x.strip())
                else:
                    trimmed_array.append(x.strip())
            return trimmed_array
    if option == 2:
        data_array = input_data.split(",")
        corrected_input = ""
        choice_option = ""
        temp_trimmed_array = []
        for y in data_array:
            split_by_space = y.split(" ")
            for x in split_by_space:
                if spell.correction(x.strip()) != x.strip():
                    print("Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nDo you "
                          "wish to change it:\n1) Yes\n2) No" % (x.strip(), spell.correction(x.strip())))
                    choice_option = input()
                    while int(choice_option) != 1 and int(choice_option) != 2:
                        print("Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nDo you "
                              "wish to change it:\n1) Yes\n2) No" % (x.strip(), spell.correction(x.strip())))
                        choice_option = input()
                    print(choice_option)
                    if int(choice_option) == 1:
                        print(
                            "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nplease input corrected word: " % (
                                x.strip(), spell.correction(x.strip())))
                        corrected_input = input()
                        while spell.correction(corrected_input.strip()) != corrected_input:
                            print(
                                "Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\nplease input corrected word: " % (
                                corrected_input, spell.correction(corrected_input.strip())))
                            corrected_input = input()
                        temp_trimmed_array.append(corrected_input.strip())
                    else:
                        temp_trimmed_array.append(y.strip())
                else:
                    temp_trimmed_array.append(y.strip())
            trimmed_array.append(temp_trimmed_array)
            return trimmed_array
    if option == 3:
        temp_array = input_data.split(",")      # First parse it by comma
        temp_value = 0
        for element in temp_array:
            temp_trimmer = []
            temp_string_split = (element.strip()).split(" ")     # Second parse it by space
            print(temp_string_split)
            if len(temp_string_split) == 4:     # Make sure it has 4 elements
                count = 1
                for value in temp_string_split:     # Check for first two words autocorrect and than 3rd and 4th integer
                    if count == 1 or count == 2:
                        temp_trimmer.append(spell.correction(value.strip()))
                    if count == 3:
                        if value.isdigit():     # Is it integer?
                            if int(value) < 2 or int(value) > 15:
                                return False
                            temp_trimmer.append(value)
                            temp_value = int(value)
                        else:
                            return False
                    if count == 4:
                        if value.isdigit():     # Is it integer?
                            if temp_value > int(value) or int(value) > 15:
                                return False
                            temp_trimmer.append(value)
                        else:
                            return False
                    count += 1
            else:
                return False
            trimmed_array.append(temp_trimmer)
        return trimmed_array




def read_input():
    input_data = input()
    return input_data


def display_message(output_message):
    print(output_message)


def main():
    user_input = ""     # Will get modified overtime can be list or just string
    output_file_name = "rules.txt"
    quit_prompt = False
    MAX_WORDS = 6
    MAX_PHRASES = 4
    MAX_PATTERNS = 2
    PROMPT_FOR_WORDS = "Please input up to 6 words separated by comma',' (word_1, word_2...):"
    PROMPT_FOR_PHRASES = "Please input up to 4 phrases separated by comma',' (phrase_1, phrase_2...):"
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
            f = open(output_file_name, "w")
            for word in user_input:
                f.write(word + "\n")
            print(user_input)    # Eventually output that to file

    quit_prompt = False     # reset prompter
    while not quit_prompt:
        display_message(PROMPT_FOR_PHRASES)
        user_input = read_input()
        user_input = parse_message(user_input, PROMPT_PHRASE_OPTION)
        quit_prompt = validate(user_input, MAX_PHRASES)
        # Print error message if input is incorrect
        if not quit_prompt:
            display_message(ERROR_MSG)
        else:
            for word in user_input:
                f.write(word + "\n")
            print(user_input)    # Eventually output that to file

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
            for word in user_input:
                for x in word:
                    f.write(x)
                f.write("\n")
            print(user_input)  # Eventually output that to file

    f.close()


main()