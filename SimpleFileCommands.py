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
            # here we need to search for the least value in the list of files
            count=0
            for i in files[fileName]:
                if files[fileName]=='Removed':
                    files[fileName][count]=count
                    flag=1
                    break
                count+=1
            if flag!=1:
                files[fileName].append(count)
            output.append('+ '+fileName+'('+str(count)+')')
        else:
            files[fileName]=[0]
            output.append('+ '+fileName)
    elif action=='delete':
        fileName=command[commandLength+1:]
        if fileName[-1:]==')':
            # it means we are required to delete an revision of the file
            revision=int(fileName[-3:][1:2])
            fileNameSansRevision=fileName[:-3].strip()
            for i in files[fileNameSansRevision]:
                if i==revision:
                    i='Removed'
                    break
            output.append('- '+str(fileName))
        else:
            for i in files[fileName]:
                files[fileName][0]='Removed'
            output.append('- '+str(fileName))

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
