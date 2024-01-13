
import os, threading, sys, time

print("\n\nThis program can 'remove-empty' files, 'organise-files' and 'check-updates' on files.\n\n")

action = input("What would you like to do?")


def getContents(location):
        try:
                items = os.listdir(location)
                
                files = [item for item in items if os.path.isfile(os.path.join(location, item))]
                folders = [item for item in items if os.path.isdir(os.path.join(location, item))]
                return files, folders
        
        except Exception:
                return [],[]

def toCheck(dir):
        if dir == ".":
                return True
        for item in notToCheck:
                if dir.__contains__(item):
                        return False
        return True

def load(stopEvent):
        while not stopEvent.is_set():
                for item in ('|','/','-','\\'):
                        sys.stdout.write(item + '\r')
                        time.sleep(0.1)
                        sys.stdout.flush()

if __name__ ==  "__main__":

        directories = []
        notToCheck = ['AppData', '.', 'Windows','adb', 'Intel', 'mingw64', 'PerfLogs', 'Program Files', 'ProgramData', 'Recovery']
        neverChecked = []

        match action:
                case "remove-empty":

                        location = input("\nThe path of the drive to clean: ")

                        for i in range(10):
                                if location == "":
                                        print("\nYou didn't enter any path.")
                                        location = input("\nThe path of the drive to clean: ")
                                else:
                                        break
                                
                        location = os.path.normpath(location)
                        
                        stopEvent = threading.Event()
                        loader = threading.Thread(target=load, args=(stopEvent,))
                        loader.start()
                        
                        for dir, sub, _ in os.walk(location):
                                if toCheck(dir):
                                        directories.append(dir)
                                        for  item in sub:
                                                directories.append(os.path.join(dir, item))

                        for item in directories:
                                contents = getContents(item)
                                for file in contents[0]:
                                        try:
                                                if os.stat(os.path.join(item, f"{file}")).st_size == 0:
                                                        if os.name == 'nt':
                                                                os.system(r'del /f/q %s"%s" ' % (item ,file))
                                                        else:
                                                                os.system(r'rm -f %s/"%s" ' % (item, file))
                                        except Exception:
                                                neverChecked.append(os.path.join(item, f"{file}"))
                                        
                                for folder in contents[1]:
                                        try:
                                                if not os.listdir(os.path.join(item, f"{folder}")):
                                                        if os.name == 'nt':
                                                                os.system(r'rmdir /q/s %s"%s"' % (item, folder))
                                                        else:
                                                                os.system(r'rm -fd %s/"%s"' % (item, folder))
                                        except Exception:
                                                neverChecked.append(os.path.join(item, f"{folder}"))
                        
                        stopEvent.set()
                        loader.join()
                        
                        if neverChecked:
                                print("\n\nFailed to access:\n")
                                print(neverChecked)
                        
                        print(f"\n\nAll empty files and folders have been removed from {location}")
                

                case "organise-files":

                        location = input("\nThe path for the folder to organize: ")

                        for i in range(10):
                                if location == "":
                                        print("\nYou didn't enter any path.")
                                        location = input("\nThe path for the folder to organize: ")
                                else:
                                        break
                                
                        location = os.path.normpath(location)

                        mappings = {
                                "Applications":["exe","msix","msixbundle"],
                                "Music":["wav","mp3","m4a","aac","wma","aiff","flac","ape","midi"],
                                "Videos":["mp4","avi","mkv","mov","wmv","flv","webm","3gp","mpeg","ogv"],
                                "Scripts": ["bat","ps1","wsf","sh","py","js","pl","rb"]
                        }

                        neverMoved = []

                        contents = getContents(location)
                        
                        def makeFolder(folder)
                                try:
                                        os.mkdir(os.path.join(location,folder))
                                except Exception:
                                        pass

                        for file in contents[0]:
                                for folder in mappings:
                                        if file[file.find("."):] in mappings[folder]:
                                                makeFolder(folder)
                                                try:
                                                        if os.name == 'nt':
                                                                os.system(r'move %s "%s" ' % (os.path.join(location,file) ,os.path.join(location,folder)))
                                                        else:
                                                                os.system(r'mv %s "%s" ' % (os.path.join(location,file) ,os.path.join(location,folder)))
                                                except Exception:
                                                        neverMoved.append(os.path.join(location, f"{file}"))
                                                