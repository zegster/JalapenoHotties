rules_file = "rules.txt"

line_count = 0
word_list = []
word_count = 0

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

