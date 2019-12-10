"""
    Program Description: This program is designed to read read the rules file created by the make__codebook.py file
    and find the patterns described in the rules.txt file.  This information is then shown on a graph for the user.

    Author: Bekzod Tolipov, Duc Ngo, Enrique Casillas, Lawrence C, Joel A
    Date: 11/13/2019
"""

# used to plot graph_list, based off the information gathered using both txt files.
import matplotlib.pyplot as plt
import numpy as np

#defines rules.txt file
rules_file = "rules.txt"
# initializes word_cound and line_count at 0
word_count = 0
line_count = 0
# declares word_list and graph_list
word_list = []
graph_list = []

# counts the amount of lines in rules.txt
for line in open(rules_file).readlines():
    line_count += 1

# array that keeps track of each time an instance of the rule is recorded
count_final = []
# adds a spot with the value 0 for each line of rules.txt
count_final += ([0] * line_count)

voice_file = "voice.txt"

# reads voice_file and removes any delimiters present, and adds to inFile
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
        # removes any capital letters and adds each word to the word_list list
        for word in lines:
            word = word.lower()
            word_list.append(word)
# opens and rads rules_file
my_file = open(rules_file).readlines()

# initializes the variable x as 0
x = 0

# the following lines take the rules file and prepare it to be read.  This means removing any extra spaces,
# and lowercasing all letters
with open(rules_file) as fp:

    for cnt, line in enumerate(fp):

        old_line = line.split(" ")
        old_line[-1] = old_line[-1].strip()
        while "" in old_line:
            old_line.remove("")
        new_line = []
        for word in old_line:
            new_line.append(word.lower())
        graph_list.append(new_line)
        # if the length of the line is 1, the program searches for the word listed on the line in the
        # word_list list
        if len(new_line) is 1:
            y = 0
            while y < len(word_list):
                if new_line[0] in word_list[y]:
                    count_final[cnt] += 1
                y += 1
            cnt += 1

        # If the length of the line is 2, the program searches for a word in word_list that is immediately
        # followed by another word
        elif len(new_line) is 2:
            a = new_line[0]
            b = new_line[1]
            z = 0
            k = (len(word_list)) - 1

            while z < len(word_list):
                if (z <= k) and a in word_list[z] and b in word_list[z + 1]:
                    count_final[cnt] += 1
                z += 1
            cnt += 1
        # If the length of the line is 3, the program searches for a word in word_list followed by the next two words
        # listed on the line.
        elif len(new_line) is 3:
            a = new_line[0]
            b = new_line[1]
            c = new_line[2]
            z = 0
            k = (len(word_list)) - 2

            while z < len(word_list):
                if (z <= k) and a in word_list[z] and b in word_list[z+1] and c in word_list[z+2]:
                    count_final[cnt] += 1
                z += 1
            cnt += 1
        # If the length of the line is 4, the program searches for the first word followed by a range of words in
        # between the second word.  This range is determined by the lower bound and upper bound from the rules.txt
        elif len(new_line) is 4:

            a = new_line[0]
            b = new_line[1]
            c = (int(new_line[2])) + 1
            d = (int(new_line[3])) + 1
            q = 0

            while q < len(word_list):

                if a in word_list[q]:
                    for i in range(c, d):
                        if ((q + i) < len(word_list)) and b in word_list[q + i]:
                            count_final[cnt] += 1

                q += 1
            cnt += 1

# Uses rules.txt and graph_list to create graph for user, displaying results of program
index = np.arange(len(graph_list))
plt.rcParams['toolbar'] = 'None'
plt.barh(index, count_final, align='center', alpha=0.5)
plt.yticks(index, graph_list, fontsize=10)
plt.xlabel('Count', fontsize=10)
plt.ylabel('Rule', fontsize=10)
plt.title('Results')
plt.tight_layout()
fig = plt.gcf()
fig.canvas.set_window_title('Word Count')
plt.show()


print(count_final)
print(word_list)
print(my_file)
print(new_line)
print(cnt)
print(len(new_line))
print(graph_list)

