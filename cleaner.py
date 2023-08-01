
import os, shutil

location = input("\nThe path of the drive to clean (default is the current directory): ")

if location == "":
        location = "."
        
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
                        desktopPath = os.path.join(os.environ["USERPROFILE"], "Desktop")
                        os.mkdir(f"{desktopPath}/TRASH")
                except Exception:
                        pass
        else:
                try:
                        desktopPath = os.path.expanduser("~/Desktop")
                        os.mkdir(f"{desktopPath}/TRASH")
                except Exception:
                        pass
        

        for dir, sub, _ in os.walk(location):
                if toCheck(dir):
                        directories.append(dir)
                        for  item in sub:
                                directories.append(os.path.join(dir, item))
        

        for item in directories:
                contents = getContents(item)
                for file in contents[0]:
                        try:
                                if os.stat(os.path.join(item, file)).st_size == 0:
                                        print(f"moved {os.path.basename(os.path.join(item, file))} from {item}.")
                                        shutil
                        except Exception as error:
                                print(f"Failed to access file at {os.path.join(item,file)}")
                                ignore.append(os.path.join(item, file))
                                
                for folder in contents[1]:
                        try:
                                if not os.listdir(os.path.join(item, folder)):
                                        print(f"{os.path.basename(os.path.join(item, folder))} from {item}")
                        except Exception as error:
                                print(f"Failed to access folder at {os.path.join(item, folder)}")
                                ignore.append(os.path.join(item, folder))

        if len(ignore) != 0:
                print("\n\nFailed to access:\n\n")
                print(ignore)
# def visualize_directory_tree(directory_tree):
#     for directories, subdirectories, files in directory_tree:
#         # for dir in directories:
#         if directories
#                 print(directories + "|")
#                 for sub in subdirectories:
#                       print(f"\t\t-{sub}")
#                 for file in files:
#                       print(f"\t\t\t-{file}")        

# visualize_directory_tree(os.walk(location))

                
                      

# def reverse(the_paths):
#     for item in the_paths:
#         os.system(f"cacls {item} /e /p {os.getlogin()}:F")


# if os.name == "nt":
#     try:
#         os.mkdir(f"/users/{os.getlogin()}/Onedrive/Desktop/TRASH")
#     except Exception:
#         pass
#     my_file = open(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH/log.txt", "w")
#     if my_file:
#         for path, directories, files in os.walk(location):
#             for item in directories:
#                 try:
#                     if item == "AppData" or item[0] == "." or item == "TRASH":
#                         os.system(
#                             f"cacls {os.path.join(path, item)} /e /p {os.getlogin()}:N"
