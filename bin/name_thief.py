import sys


output = []
with open('names.txt') as f:
        content = f.readlines()
        for line in content:
            bits = line.split(' ');
            if (len(bits) == 2):
                    output.append(line)

with open("post_names.txt", 'w') as fout:
        for s in output:
                    fout.write(s)
