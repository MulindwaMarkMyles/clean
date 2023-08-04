
import os, threading, sys, time

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
        
        except Exception:
                return [],[]

def toCheck(dir):
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
                                                os.system(r'del /f/q %s\"%s" ' % (item ,file))
                                        else:
                                                os.system(r'rm -f %s/"%s" ' % (item, file))
                        except Exception:
                                neverChecked.append(os.path.join(item, f"{file}"))
                        
                for folder in contents[1]:
                        try:
                                if not os.listdir(os.path.join(item, f"{folder}")):
                                        if os.name == 'nt':
                                                os.system(r'rmdir /q/s %s\"%s"' % (item, folder))
                                        else:
                                                os.system(r'rm -fd %s/"%s"' % (item, folder))
                        except Exception:
                                neverChecked.append(os.path.join(item, f"{folder}"))
        
        stopEvent.set()
        loader.join()
        
        if neverChecked:
                print("\nFailed to access:\n")
                print(neverChecked)
        
        print(f"\n \nAll empty files and folders have been removed from {location}")
        
        