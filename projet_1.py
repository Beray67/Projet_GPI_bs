#! /usr/bin/env python3

import sys
import RNA.utils as utils

if len(sys.argv) !=2:
    print('Incorrect number of arguent')
    print('Usage:')
    print('> projetc_1.py file.pdb')
    exit()

pdb_name = sys.argv[1]

RNA = utils.parsePDB(pdb_name)
utils.generate_dot_bracket(RNA)

with open(pdb_name,'r') as file:
    line = file.readline()
    print(line)  
    while line[0:6].strip() != 'TER':
        if line[0:6].strip() == 'ATOM':
            x = float(line[30:38].strip())
            print(x)
        line = file.readline()