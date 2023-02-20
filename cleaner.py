import os

location = input("\nThe path of the drive to clean: ")
location = location.replace("/", "\\") if location.__contains__("/") else location

for path, directories, files in os.walk(location):
    for item in directories:
        if item == "AppData":
            print("AppData")
            next
        else:
            try:
                if not bool(os.listdir(os.path.join(path, item))):
                    # os.system(f"rm {os.path.join(path,item)}")
                    print(item)
            except Exception as error:
                print(f"Error working on {os.path.join(path,item)} due to {error}. ")
    for item in files:
        try:
            if os.stat(os.path.join(path, item)).st_size == 0 and not item[0] == ".":
                # os.system(f"rm {os.path.join(path,item)}")
                print(os.path.join(path, item))
        except Exception as error:
            print(f"Error working on {os.path.join(path,item)} due to {error}. ")
