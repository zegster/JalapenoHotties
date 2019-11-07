# type following to terminal to install: pip install pyspellchecker
from spellchecker import SpellChecker
# Checks the spelling
spell = SpellChecker()


def validate(input_data, max_input):
    if not input_data:
        print("ERROR: Input size wrong")
        return False

    if len(input_data) > max_input:
        print("ERROR: Input size wrong")
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
        temp_string = ""
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
                        print("Is the given word spelled correctly?\nGiven input: (%s) \nPossible spelling: (%s)\n"
                              "please input corrected word: " % (x.strip(), spell.correction(x.strip())))
                        corrected_input = input()
                        while spell.correction(corrected_input.strip()) != corrected_input:
                            print("Possible spelling: (%s)\nplease input corrected word: " %
                                  (corrected_input, spell.correction(corrected_input.strip())))
                            corrected_input = input()
                        temp_string += (str(corrected_input.strip())) + " "
                    else:
                        temp_string += (str(x.strip())) + " "
                else:
                    temp_string += (str(x.strip())) + " "
            trimmed_array.append(temp_string.strip())
            temp_string = ""
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
                for elem in word:
                    f.write(elem)
                f.write("\n")
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
                    f.write(x + " ")
                f.write("\n")
            print(user_input)  # Eventually output that to file

    f.close()

    rules_file = "rules.txt"
    word_count = 0
    line_count = 0
    word_list = []

    for line in open(rules_file).readlines():
        line_count += 1

    count_final = []

    count_final += ([0] * line_count)

    voice_file = "voice.txt"
    is_file_exist = False
    while not is_file_exist:
        try:
            with open(voice_file) as inFile:
                for lines in inFile:
                    lines = lines.replace(",", "")
                    lines = lines.replace(".", "")
                    lines = lines.replace(";", "")
                    lines = lines.replace(":", "")
                    lines = lines.replace("\\", "")
                    lines = lines.replace("\"", "")
                    lines = lines.replace("\t", "")
                    lines = lines.replace("\n", "")
                    lines = lines.split(" ")

                    for word in lines:
                        word = word.lower()
                        word_list.append(word)
            is_file_exist = True
        except FileNotFoundError:
            print("ERROR: File not found")

    my_file = open(rules_file).readlines()

    x = 0

    with open(rules_file) as fp:
        for cnt, line in enumerate(fp):

            new_line = line.split(" ")
            new_line[-1] = new_line[-1].strip()

            if len(new_line) is 1:
                y = 0
                while y < len(word_list):
                    if new_line[0] in word_list[y]:
                        count_final[cnt] += 1
                    y += 1
                cnt += 1

            elif len(new_line) is 3:
                a = new_line[0]
                b = new_line[1]
                c = new_line[2]
                z = 0

                while z < len(word_list):
                    if a in word_list[z] and b in word_list[z + 1] and c in word_list[z + 2]:
                        count_final[cnt] += 1
                    z += 1
                cnt += 1

            elif len(new_line) is 4:

                a = new_line[0]
                b = (int(new_line[1])) + 1
                c = (int(new_line[2])) + 1
                d = new_line[3]
                q = 0

                while q < len(word_list):

                    if a in word_list[q]:
                        for i in range(b, c):
                            if d in word_list[q + i]:
                                count_final[cnt] += 1

                    q += 1
                cnt += 1

    print(count_final)
    print(word_list)
    print(my_file)
    print(new_line)
    print(cnt)
    print(len(new_line))


main()