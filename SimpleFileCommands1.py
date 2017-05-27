#!/bin/python3

"""
The easy way to implement this program would be to use a simple list to store all the filenames.
"""

import sys

output=[]
files=[]
commandLength=3
cmd={'crt':'create','del':'delete','rnm':'rename'}

def searchFile(fileName):
    # searches for the fileName

def answer(command):
    action=cmd[command[:commandLength]]    
    if action=='create':
        fileName=command.split()[1]
        

    elif action=='delete':
        # TODO
    elif action=='rename':
        # TODO

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
