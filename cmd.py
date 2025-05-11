import os

while True:
    command = input("Enter command: ")

    if command == "View":
        files = os.listdir()
        for file in files:
            print(file)

    elif command == "Create file":
        file_name = input("Enter a name fot the new file: ")
        file = open(file_name, "w")
        file.close()
        print("Файл создан!")

    elif command == "Create folder":
        directory = input("Enter the name of the new folder: ")
        os.mkdir(directory)

    elif command == "Delete file":
        file_name = input("Enter file name")
        if os.path.exists(file_name):
            os.remove(file_name)
            print("file deleted!")
        else:
            print("error")

    elif command == "Delete folder":
        directory = input("Enter a folder name: ")
        os.rmdir(directory)

    elif command == "help":
        print("All command:")
        print("Create file")
        print("Create folder")
        print("Delete file")
        print("Delete folder")
        print("help")

