from spellchecker import SpellChecker
# Checks the spelling
spell = SpellChecker()


def validate(input_data, max_input):
    if not input_data:
        return False

    if len(input_data) > max_input:
        return False

    return True


def parse_message(input_data, option):
    trimmed_array = []
    temp_array = []
    temp_string_split = []

    if option == 1:
        if len(input_data.split(" ")) != len(input_data.split(",")):     # Check if number of words is same when parsed
            return False
    if option == 3:
        temp_array = input_data.split(",")      # First parse it by comma
        for element in temp_array:
            temp_trimmer = []
            temp_string_split = (element.strip()).split(" ")     # Second parse it by space
            print(temp_string_split)
            if len(temp_string_split) == 4:     # Make sure it has 4 elements
                count = 1
                for value in temp_string_split:     # Check for first two words autocorrect and than 3rd and 4th integer
                    if count == 1 or count == 2:
                        temp_trimmer.append(spell.correction(value.strip()))
                    if count == 3 or count == 4:
                        if value.isdigit():     # Is it integer?
                            temp_trimmer.append(value)
                        else:
                            return False
                    count += 1
            else:
                return False
            trimmed_array.append(temp_trimmer)
        return trimmed_array

    data_array = input_data.split(",")
    for x in data_array:
        trimmed_array.append(spell.correction(x.strip()))
    return trimmed_array


def read_input():
    input_data = input()
    return input_data


def display_message(output_message):
    print(output_message)


def main():
    user_input = ""     # Will get modified overtime can be list or just string
    quit_prompt = False
    MAX_WORDS = 6
    MAX_PHRASES = 4
    MAX_PATTERNS = 2
    PROMPT_FOR_WORDS = "Please input up to 6 words separated by comma',' (word_1, word_2...):"
    PROMPT_FOR_PHRASES = "Please input up to 4 phrases separated by comma',' (phrase_1, phrase_2...):"
    PROMPT_FOR_PATTERN = "Please input up to 2 pattern followed by upper-bound=u, lower-bound=l " \
                         "separated by comma',' (word_1 word_2 u l, word_1 word_2 u l...):"
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
            print(user_input)  # Eventually output that to file


main()