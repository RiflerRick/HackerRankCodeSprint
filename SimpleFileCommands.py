#!/bin/python3

import sys
# each new file will be in a new list inside files dictionary, key to the dictionary is the filename and value is the number of revisions of the file present
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
            flag=0
            for i in files[fileName]:
                if i=='Removed':
                    files[fileName][count]=count
                    flag=1
                    break
                count+=1
            if flag!=1:
                files[fileName].append(count)
            if count==0:
                output = ('+ '+fileName)
            else:
                output = ('+ '+fileName+'('+str(count)+')')
        else:
            files[fileName]=[0]
            output = ('+ '+fileName)


    elif action=='delete':
        fileName=command[commandLength+1:]
        if fileName[-1:]==')':
            # it means we are required to delete an revision of the file
            revision=int(fileName[-3:][1:2])
            fileNameSansRevision=fileName[:-3]
            files[fileNameSansRevision][revision]='Removed'
                
            output = ('- '+str(fileName))

        else:
            files[fileName][0]='Removed'

            output = ('- '+str(fileName))
    


    elif action=='rename':
        command=command.split()
        targetFileName=command[1]
        renamedFileName=command[2]
        if targetFileName[-1:]==')':
            # trying to remove a revision of the file
            revision=int(targetFileName[-3:][1:2])
            fileNameSansRevision=targetFileName[:-3]
            files[fileNameSansRevision][revision]='Removed'
        else:
            files[targetFileName][0]='Removed'

        # deletion over, now creation renaming

        if renamedFileName in files:
            # here we need to search for the least value in the list of files
            count=0
            flag=0
            for i in files[renamedFileName]:
                if i=='Removed':
                    files[fileName][count]=count
                    flag=1
                    break
                count+=1
            if flag!=1:
                files[renamedFileName].append(count)
            renamedFileOutput=renamedFileName+'('+str(count)+')'
        else:
            files[renamedFileName]=[0]
            renamedFileOutput=renamedFileName
        output = ('r '+str(targetFileName)+' -> '+str(renamedFileOutput))

    # print(files)
    return output

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    print(answer(command))
