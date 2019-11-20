# Program Description: This program is designed to take input file name from user
# and read the file extract words, remove special symbols, than count the words by using
# dictionary method. At the end output the result to a default file and also show the
# result in a bar chart.
# Date: 10/11/2019
# Authors: Bekzod Tolipov, Nelson Su, Khalfani Wadlington

import re
import matplotlib.pyplot as pl
from pathlib import Path
from collections import Counter


def trim_word(word):
    new_word = ""
    for letter in word:
        # A to z (0 to 9) dash - or hyphen'
        if re.match("[a-zA-Z0-9-']", letter):
            new_word += letter
    return new_word


word_list = {}
new_word_list = {}
top_20 = {}


def main():
    print("Please input filename: ")
    file_name = input()
    quit_loop = True
    while quit_loop:
        if not Path(file_name).is_file():
            print("ERROR: INPUT FILE DOES NOT EXIST: Please input filename: ")
            file_name = input()
        else:
            quit_loop = False

    with open(file_name, "r") as open_file_object:
        for line in open_file_object:
            arr_words = line.split(" ")
            for pos in range(0, len(arr_words)):
                trimmed = trim_word(arr_words[pos])
                print(trimmed)
                if trimmed in word_list:
                    word_list[trimmed] += 1
                else:
                    word_list[trimmed] = 1

    output_file = "results.txt"
    out = open(output_file, "w")

    for key in sorted(word_list.keys()):
        out.write(key + " " + "%d" % (word_list[key]) + "\n")

    # Sort by most frequent
    new_word_list = sorted(word_list.items(), reverse=True, key=lambda x: x[1])

    k = Counter(new_word_list)
    top_20 = k.most_common(20)

    pl.bar(range(len(top_20)), [val[0][1] for val in top_20], align='center')
    pl.xticks(range(len(top_20)), [val[0][0] for val in top_20])
    pl.xticks(rotation=70)
    pl.show()

    # close files
    out.close()


main()


