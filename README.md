# File Organizing Program User Guide

## Purpose
This program helps users organize their files according to file types, making it easy to find and access files when needed.

## Use Case
Are you tired of searching through a messy file system to find the documents you need? Do you have trouble remembering where you saved that important file? Our file organizing program can help! With our program, you can quickly and easily organize your files by type, making it simple to find and access your documents when you need them.

Here are some examples of how the file organizing program might work in practice:

Example 1: Organizing a directory with documents and images
Suppose the user has a directory called "My Files" that contains the following files:

-report.docx
-presentation.pptx
-budget.xlsx
-photo1.jpg
-photo2.jpeg

When the user runs the file organizing program and inputs the "My Files" directory, the program will automatically sort these files into separate folders based on their file type. The result will be two folders named "Documents" and "Images", with the following files inside:

Documents
- report.docx
- presentation.pptx
- budget.xlsx

Images
- photo1.jpg
- photo2.jpeg

### How it handle duplicated files?
In the original version of the script, if there are files with the same name in different subfolders, then the script will overwrite the files with the same name in the target folder without warning. This can lead to data loss or other issues.

## Installation
The program is text-based and does not require installation. Simply download the Python script and the `file_extensions.txt` file and run the Python script in a Python environment.

## User Interface
The program runs in the command prompt or terminal. The user inputs the directory they want to organize and the program sorts the files into folders based on their file type. The `file_extensions.txt` file contains a list of file extensions and their corresponding folder names, which the program uses to determine where to move each file.

## Usage

### Python Method
To use the program, follow these steps:
- Open the command prompt or terminal
- Navigate to the directory where the Python script and `file_extensions.txt` file are located
- Type `organizefilesbyextention.py` 
- Enter the directory you want to organize when prompted

![image](https://user-images.githubusercontent.com/37545716/225633155-a7a08993-a7d5-42b8-979e-ac25084b12d1.png)

- The program will sort the files into folders based on their file type, using the `file_extensions.txt` file to determine where to move each file.

To handle duplicated files more safely, you can modify the script to add a version number to the filename. The version number indicates that the file is a newer version of an existing file with the same name. This ensures that each file in the target folder has a unique name and avoids overwriting existing files.

## What is the `file_extensions.txt` for?
The `file_extensions.txt` file is a text file that contains a list of file extensions and their corresponding folder names, separated by a colon (":") character. Each line of the file should contain a single file extension followed by its corresponding folder name, like this:

![image](https://user-images.githubusercontent.com/37545716/225633019-5d745e05-3a46-4a93-9c55-e68e9dd64833.png)
