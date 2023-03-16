import os
import shutil

def organize_files(directory_path):
    # Create a set of all the unique file extensions in the directory
    extensions_set = set(os.path.splitext(file)[1].lower() for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file)))

    # Initialize an empty dictionary to store mappings between file extensions and folder names
    extension_to_folder = {}

    # Iterate through the extensions set and prompt the user to enter folder names
    for extension in extensions_set:
        if extension not in extension_to_folder.keys():
            folder_name = input(f"Enter folder name for {extension} files: \n 請為{extension}類型檔案命名: \n ")
            extension_to_folder[extension] = folder_name
        folder_path = os.path.join(directory_path, extension_to_folder[extension])
        os.makedirs(folder_path, exist_ok=True)

        # Get a list of all files with the current extension
        files_to_move = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file)) and os.path.splitext(file)[1].lower() == extension]

        # Move each file to the corresponding folder
        for file in files_to_move:
            shutil.move(os.path.join(directory_path, file), os.path.join(folder_path, file))

    # Write the extension_to_folder dictionary to a text file
    with open('file_extensions.txt', 'w') as f:
        for extension, folder in extension_to_folder.items():
            f.write(f"{extension}: {folder}\n")


def main():
    # Prompt the user to enter the directory path
    directory_path = input("Enter the directory path to organize: \n輸入要管理的檔案路徑\n ")

    # Call the organize_files function to organize the files in the directory
    organize_files(directory_path)

    # Print a message to indicate that the files have been organized
    print("Files have been organized successfully. 檔案成功被整理")


if __name__ == "__main__":
    main()
