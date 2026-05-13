#! /usr/bin/env python3

lines = []
with open('8D28.pdb', 'r') as file:
    while line != '':
        line = file.readline()
        lines.append(line)

for line in lines:
    if line[:4] == 'TITLE':
        print(line)


