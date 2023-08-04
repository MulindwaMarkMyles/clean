
import os, time

location = input("\nThe path of the drive to clean: ")

for i in range(10):
        if location == "":
                print("\nYou didn't enter any path.")
                location = input("\nThe path of the drive to clean: ")
        else:
                break
        
location = os.path.normpath(location)

def getContents(location):
        try:
                items = os.listdir(location)
                
                files = [item for item in items if os.path.isfile(os.path.join(location, item))]
                folders = [item for item in items if os.path.isdir(os.path.join(location, item))]
                return files, folders
        
        except Exception as error:
                print(f"Error: {error}")
                return [],[]

def toCheck(dir):
        for item in notToCheck:
                if dir.__contains__(item):
                        return False
        return True

if __name__ ==  "__main__":
        directories = []
        notToCheck = ['AppData', '.', 'Windows','adb', 'Intel', 'mingw64', 'PerfLogs', 'Program Files', 'ProgramData', 'Recovery']
        ignore = []
        
        if os.name == "nt":
                try:
                        trash = f"C:/Users/mulin/AppData/Local/Temp/TRASH"
                        
                        if not os.access(trash, os.F_OK):
                                os.mkdir(f"C:/Users/mulin/AppData/Local/Temp/TRASH")
                                
                except Exception as error:
                        print(error)

        else:
                try:
                        desktopPath = os.path.expanduser("~/Desktop")
                        os.mkdir(f"{desktopPath}/TRASH")
                        trash = f"{desktopPath}/TRASH"
                except Exception:
                        pass
        

        for dir, sub, _ in os.walk(location):
                if toCheck(dir):
                        directories.append(dir)
                        for  item in sub:
                                directories.append(os.path.join(dir, item))
        
        copy = directories

        for item in directories:
                contents = getContents(item)
                for file in contents[0]:
                        try:
                                if os.stat(os.path.join(item, f"{file}")).st_size == 0:
                                        print(os.system(r'del /f/q %s\"%s" ' % (item ,file)))
                        except Exception:
                                ignore.append(os.path.join(item, file))
                        
                for folder in contents[1]:
                        try:
                                if not os.listdir(os.path.join(item, f"{folder}")):
                                        print(os.system(r'rmdir /q/s %s\"%s"' % (item, folder)))
                        except Exception:
                                ignore.append(os.path.join(item, folder))

        if ignore:
                print("\nFailed to access:\n")
                print(ignore)
        
                                
        choice = input("All empty files and folders have been removed, should i remove the TRASH folder from your pc (Y/N): ").lower()
        
        if choice == "y":
                os.system("del /q/f/s %TEMP%\*")
        else:
                print("Check it out at {trash}")