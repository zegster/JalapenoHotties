import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter
import numpy as np


rules_file = "rules.txt"
word_count = 0
line_count = 0
word_list = []
graph_list = []

for line in open(rules_file).readlines():
    line_count += 1

count_final = []

count_final += ([0] * line_count)

voice_file = "voice.txt"

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

my_file = open(rules_file).readlines()

x = 0

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

        if len(new_line) is 1:
            y = 0
            while y < len(word_list):
                if new_line[0] in word_list[y]:
                    count_final[cnt] += 1
                y += 1
            cnt += 1

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

# this is for plotting purpose
index = np.arange(len(graph_list))
plt.rcParams['toolbar'] = 'None'
plt.barh(index, count_final, align='center', alpha=0.5)
plt.yticks(index, graph_list, fontsize=10)
plt.xlabel('Rule', fontsize=10)
plt.ylabel('Count', fontsize=10)
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

