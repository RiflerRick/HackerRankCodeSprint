#!/bin/python3

import sys
# each new file will be in a new list inside files dictionary, key to the dictionary is the filename and value is the number of revisions of the file present
output=[]
files={}
commandLength=3
cmd={'crt':'create','del':'delete','rnm':'rename'}

def answer(command):
    action=cmd[command[:commandLength]]
    if action=='create':
        fileName=command[commandLength+1:]
        if fileName in files:
            numFiles=files[fileName]

            output.append('+ '+fileName+'('+str(files[fileName]-1)+')')
        else:
            files[fileName]=[0]
            output.append('+ '+fileName)
    elif action=='delete':
        fileName=command[commandLength+1:]
        files[fileName]-=1
        if files[fileName]!=0:
            output.append('- '+fileName+'('+str(files[fileName]-1)+')')
        else:
            output.append('- '+fileName)
    elif action=='rename':
        

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
