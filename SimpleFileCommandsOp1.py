#!/bin/python3

import sys
# each new file will be in a new list inside files dictionary, key to the dictionary is the filename and value is the number of revisions of the file present
files={}
removedFiles={}
commandLength=3
cmd={'crt':'create','del':'delete','rnm':'rename'}

def answer(command):
    action=cmd[command[:commandLength]]
    if action=='create':
        fileName=command[commandLength+1:]
        if fileName in files:
            
            # first priority goes to files that are removed, if there are such files then those will be filled first

            if fileName in removedFiles:
                revision=removedFiles[fileName].pop()
                if removedFiles[fileName]==[]:
                    del removedFiles[fileName]
                if revision==0:
                    output = ('+ '+fileName)
                else:
                    output = ('+ '+fileName+'('+str(revision)+')')
            
            else:
                revision=files[fileName]
                output = ('+ '+fileName+'('+str(revision+1)+')')
                files[fileName]+=1

        else:
            files[fileName]=0
            output = ('+ '+fileName)


    elif action=='delete':
        fileName=command[commandLength+1:]
        if fileName[-1:]==')':
            # it means we are required to delete an revision of the file
            revision=int(fileName[-3:][1:2])
            fileNameSansRevision=fileName[:-3]
            if fileNameSansRevision not in removedFiles:
                removedFiles[fileNameSansRevision]=[]
            removedFiles[fileNameSansRevision].append(revision)

            removedFiles[fileNameSansRevision].sort(reverse=True) # this step takes nlogn time and hence can be expensive
                
            output = ('- '+str(fileName))

        else:
            if fileName not in removedFiles:
                removedFiles[fileName]=[]
            removedFiles[fileName].append(0)

            output = ('- '+str(fileName))
    


    elif action=='rename':
        command=command.split()
        targetFileName=command[1]
        renamedFileName=command[2]
        if targetFileName[-1:]==')':
            # trying to remove a revision of the file
            revision=int(targetFileName[-3:][1:2])
            fileNameSansRevision=targetFileName[:-3]
            if fileNameSansRevision not in removedFiles:
                removedFiles[fileNameSansRevision]=[]
            removedFiles[fileNameSansRevision].append(revision)

            removedFiles[fileNameSansRevision].sort(reverse=True)

        else:
            if targetFileName not in removedFiles:
                removedFiles[targetFileName]=[]
            removedFiles[targetFileName].append(0)

        # deletion over, now creation renaming

        if renamedFileName in files:
            # here we need to search for the least value in the list of files

            if renamedFileName in removedFiles:
                revision=removedFiles[renamedFileName].pop()
                if removedFiles[renamedFileName]==[]:
                    del removedFiles[renamedFileName]
                if revision==0:
                    renamedFileOutput=renamedFileName
                else:
                    renamedFileOutput=renamedFileName+'('+str(revision)+')'
            
            else:
                revision=files[renamedFileName]
                renamedFileOutput = (renamedFileName+'('+str(revision+1)+')')
                files[renamedFileName]+=1

        else:
            files[renamedFileName]=0
            renamedFileOutput = (renamedFileName)

        output = ('r '+str(targetFileName)+' -> '+str(renamedFileOutput))

    print('files----> '+str(files))
    print('removedFiles-------> '+str(removedFiles))

    return output

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    print(answer(command))
