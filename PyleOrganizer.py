import re, os, datetime as dt, time
"""
Name: Isaac (IzzySWE)
Date: 12/02/2024

Project: File Organizer
"""


# File Organizer
# default configurations
# Modify the file directory within the double quotes "file-directory"
filePath = "/Users/xyz.isx/Downloads"

# Modify (filter out) to either "date" or "filename"
searchByFilter = "filename"

# Modify String by file name including dotfile type eg: "HelloWorld.docx"
# Modify String by Date (FORMAT: YYYY/MM/DD)
searchByFile = "project_Proposals.txt"
searchByDate = "2024/12/04"


# if its by date, we'll need to split it to use the datetime properly
dateSplit = searchByDate.split("/")
# cast it into int and index the string converted to list
year = int(dateSplit[0])
month = int(dateSplit[1])
day = int(dateSplit[2])


# called it the default file path function as this will be the main functionality
def defaultFilePath():
    # displays in print function the current working directory using the cwd os function
    print("Current working directory: "+os.getcwd())
    # check which operating system user is using to avoid any potential directory errors
    if os.name == 'nt':
        # so if its "nt" (windows), replace "/" with "\\"
        replacedPath = filePath.replace("/", "\\")
        # then open the path
        fileinput = os.chdir(filePath)
        # check again which OS it's using to avoid directory errors
    elif os.name == 'posix':
        # if its "posix" (any unix based system), change to the directory as is
        fileinput = os.chdir(filePath)
    # showing the changed directory using the cwd os function
    print("Changed directory: "+os.getcwd())
    # called the function below (automatedSearch)
    automatedSearch()


# this could have gone above, however i made it seperate for readability reasonings
# created a function called automatedSearch as this will detect if the string is either Date or filename
def automatedSearch():
    # if the filter default is "date"
    if searchByFilter == "date":
        # grab the sectioned datasplit that we both casted and indexed and put it on datetime to get the date
        getDate = dt.datetime(year, month, day)
        # call the searchByDate with the getDate date object as the argument to find any files with the exact date
        SearchByDate(getDate)
    # HOWEVER, if the filter is "filename"
    if searchByFilter == "filename":
        # call the searchByFileName and provide the "default variable" (string variable) to find the file name
        # within the current directory
        SearchByFileName(searchByFile)


# created the searchByDate function with the retrieved data parameter to indicate that we've "retrieved data"
def SearchByDate(retrievedDate):
    # display to the user that the program is searching
    print(f"Searching Files during {retrievedDate.date()}")
    # pause the program for at least 4 second to make it seem like it working hard in finding it
    time.sleep(1)
    # loop through the list of dirs, so in a verbose way, for every file inside the list of directory...
    for file in os.listdir():
        # check if the file is infact a "file" and not a folder
        if os.path.isfile(file):
            # if so, output the file name
            print(file)
            # and call the categorize file function with file as the argument to then catergorize the file into
            # which folder is appropriate
            CategorizeFiles(file)


# Created a function called Search by File Name with the file name as the parameter
# since we want to find the file using filename instead
def SearchByFileName(fileName):
    # display the user that the program is searching
    print(f"Searching Files with File Name: {fileName}")
    # again, we will pause the program for at least 4 second to make the user convinced its a hard worker
    time.sleep(1)
    # loop through the list of the current directories, as mentioned, another way to think of it is as
    # for every file that is in the list of the directory
    for file in os.listdir():
        # check if it is infact a file
        if os.path.isfile(file):
            time.sleep(2)
            # if it is the case, print out the file name
            print(file)
            # call the categorize file function with the loop's file variable as the argument to
            # then figure out where each file should go to
            CategorizeFiles(file)


# created a function called categorizeFile as appropriate name with the parameter "fileType"
# so whatever file is picked, the function can choose accordingly
def CategorizeFiles(fileType):
    # created 2 list of folders, each folder will accept the following
    Documents = [".doc", ".docx", ".txt", ".pdf"]
    Spreadsheets = [".xls", ".xlsx", ".numbers", ".mov"]
    Code = [".java", ".py", ".cs", ".go", ".sql", ".cpp", ".lua"]
    Temporary = [".dmg", ".zip", ".tar.br2", ".rar"]
    Images = [".jpeg", ".jpg", ".png", ".svg", ".webp"]

    # Use regex to verify it is an eligible file type and extract it from its given argument
    fileReg = re.search(r"\.[a-zA-Z0-9]+$", fileType)
    # if fileReg matches with the regex given
    if fileReg:
        # our dotExtension (new variable) will be assigned to the matching regex
        # (0 representing the entire file extension)
        dotExtension = fileReg.group(0)
    else:
        # else give it blank since no appropriate files were found
        dotExtension = ""

    # if the dotExtension meets with any of the dot extensions that is inside the document list
    if dotExtension in Documents:
        # call the function with 2 arguments, One will the dot extension Type
        # and other will be the folder name that will be created
        moveToFolder(fileType, "Documents")
    # OR if the dotExtension meets any of the dot extension that is inside the Spreadsheets list
    elif dotExtension in Spreadsheets:
        # call the function with the same first argument however use "Spreadsheets" as the second argument
        # as that will be what the folder name will be
        moveToFolder(fileType, "Spreadsheets")
    elif dotExtension in Code:
        moveToFolder(fileType, "Code")
    elif dotExtension in Temporary:
        moveToFolder(fileType, "Temporary")
    elif dotExtension in Images:
        moveToFolder(fileType, "Images")
    else:
        # and if dot Extension is assigned to blank
        # (meaning if it doesn't meet any of the list under document or spreadsheet)
        # just output that it doesn't match
        print(f"File not found, file doesn't match category: {fileType}")


# created a function called movetoFolder where it will begin the process of copying its content
# create a folder and new file, delete the old file. 2 arguments one represented the file type it is
# and other represents the foldername it will create the folder with the given name
def moveToFolder(fileType, createFolder):
    # create a source variable, using the default path and with the added file the program found that matches
    source = filePath + "/" + fileType
    # the destination folder variable that now holds the default path with what the new folder will be named
    destFolder = filePath + "/" + createFolder
    # lastly the destinated path the new folder will be created with the one we made above and its file type
    destPath = destFolder + "/" + fileType

    # checking if it exists, if it does
    if os.path.exists(destFolder):
        # let the user know hey, you already have a file, but we'll add it in the existing file
        print("folder already exist, inserting into existing folder...")
        # wait for 4 seconds
        time.sleep(4)
        # open source file and read binary or just read
        file = open(source, 'rb')
        # save the read content
        content = file.read()
        # close the file
        file.close()

        # we will open the destinated path file
        file = open(destPath, 'wb')
        # write the read content from the source file
        file.write(content)
        # close the file
        file.close()
        # and remove the original file so it simulates a "moved file"
        os.remove(source)
    else:
        # if it doesn't exist, create the directory using the destination folder variable i created earlier
        os.makedirs(destFolder)
        # open the source folder variable, it is going to read it and read it in binary,
        # incase folders like documents or pdf come in play. its a little bit outside of our scope,
        # but i felt it would be abit embarrassing if i am not using libraries except for pyip
        file = open(source, 'rb')
        # anyways, we will read the content (or binary if it isn't a readable file)
        content = file.read()
        # then close the file
        file.close()

        # now we will open up the destination Path variable and it is going to write (or write in binary)
        # incase the file type is not readable
        file = open(destPath, 'wb')
        # now whatever program read, it will regurgitate what ti read unto the destination file
        file.write(content)
        # then close the file
        file.close()

        # the original file is still there that we found so it make it seem like we've "moved it"
        # we removed it using the remove os function and removed the source file aka the original file
        os.remove(source)
        print(f"Moved {fileType} to {createFolder}")
        print("done.")


try:
    defaultFilePath()
except:
    print("An exception occurred")
print("finished.")
