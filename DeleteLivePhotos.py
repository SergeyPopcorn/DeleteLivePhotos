from tkinter.filedialog import askdirectory

import os
path = askdirectory()
def PrintList(theList):
    listName = "The List Entries are: "
    print(listName)
    print(theList)
    print('\n')

def ListContains(heicList,movList):
    duplicates = []
    for heic in heicList:
        for mov in movList:
            if heic == mov:
              duplicates.append(heic)
    return duplicates

def Reappend(duplicateList, extension):
    appendedList =[]
    for entry in duplicateList:
        entry = entry + extension
        appendedList.append(entry)
    return appendedList
    
dir_list = os.listdir(path)

heicList = []
movList = []
elseList = []

extension = '.MOV'

for file in dir_list:

    strInput = file
    strCut = strInput.split('.')
    if strCut[1] == 'HEIC':
        heicList.append(strCut[0])
    elif strCut[1] == 'MOV':
        movList.append(strCut[0])
    else:
        elseList.append(strCut[0])

duplicates = ListContains(heicList,movList)

finalList = Reappend(duplicates, extension)

for entry in finalList:
    toPrint = path+'\\'+entry
    print(toPrint)
    os.remove(toPrint)
    print("Deleted\n")
    
print('Operation Complete')




