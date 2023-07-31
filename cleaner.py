
import os, time, sys ,shutil

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
        notToCheck = ['Appdata', '.git']
        for item in notToCheck:
                if dir.__contains__(item):
                        return False
        return True


if __name__ ==  "__main__":
        directories = []

        for dir, sub, _ in os.walk(location):
                if toCheck(dir):
                        directories.append(dir)
                        for  item in sub:
                                directories.append(os.path.join(dir, item))

        for item in directories:
                contents = getContents(item)
                print(contents)
                for file in contents[0]:
                        if os.stat(os.path.join(item, file)).st_size == 0:
                                print(os.path.basename(os.path.join(item, file)))
                for folder in contents[1]:
                        if not os.listdir(os.path.join(item, folder)):
                                print(os.path.basename(os.path.join(item, folder)))


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
#                         )
#                         the_paths.append(os.path.join(path, item))
#                     else:
#                         if not os.listdir(os.path.join(path, item)):
#                             os.system(
#                                 f"move {os.path.join(path,item)} /Users/{os.getlogin()}/Onedrive/Desktop/TRASH"
#                             )
#                             my_file.write(f"successfully moved {item} from {path}\n\n")

#                 except Exception as error:
#                     my_file.write(
#                         f"Error working on {os.path.join(path,item)} due to {error}. \n\n"
#                     )

#             for item in files:
#                 try:
#                     if (
#                         os.stat(os.path.join(path, item)).st_size == 0
#                         and not item[0] == "."
#                     ):
#                         os.system(
#                             f"move {os.path.join(path,item)} /Users/{os.getlogin()}/Onedrive/Desktop/TRASH"
#                         )
#                         my_file.write(f"successfully moved {item} from {path}\n\n")

#                 except Exception as error:
#                     my_file.write(
#                         f"Error working on {os.path.join(path,item)} due to {error}. \n\n"
#                     )

#         # when done then restore permissions
#         reverse(the_paths)
#         #finally
#         output = "Finished cleaning the file system, if you wish to check what has been deleted... \ncheck the TRASH folder on the desktop, and if u wish to proceed press y and n if not."
#         for i in output:
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             time.sleep(0.025)
#         output = input("Your answer(y/n): ").lower()
#         if output.__contains__("y"):
#             print("The trash will be deleted..")
#             for item in list(os.listdir(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH")):
#                 if os.path.isdir(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH/{item}"):
#                     os.rmdir(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH/{item}") 
#                 else:
#                     os.remove(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH/{item}")
#             os.rmdir(f"/Users/{os.getlogin()}/Onedrive/Desktop/TRASH")
#         else:
#             print("No deletions made..")
#     else:
#         print("Failed to open..")

# else:
#     pass
