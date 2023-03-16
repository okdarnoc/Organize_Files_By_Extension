# File Organizing Program User Guide

## Purpose
This program helps users organize their files according to file types, making it easy to find and access files when needed.

## Use Case
Are you tired of searching through a messy file system to find the documents you need? Do you have trouble remembering where you saved that important file? Our file organizing program can help! With our program, you can quickly and easily organize your files by type, making it simple to find and access your documents when you need them.

Here are some examples of how the file organizing program might work in practice:

Example 1: Organizing a directory with documents and images
Suppose the user has a directory called "My Files" that contains the following files:

report.docx
presentation.pptx
budget.xlsx
photo1.jpg
photo2.jpeg
When the user runs the file organizing program and inputs the "My Files" directory, the program will automatically sort these files into separate folders based on their file type. The result will be two folders named "Documents" and "Images", with the following files inside:

Documents
- report.docx
- presentation.pptx
- budget.xlsx

Images
- photo1.jpg
- photo2.jpeg


## Installation
The program is text-based and does not require installation. Simply download the Python script and the `file_extensions.txt` file and run the Python script in a Python environment.

## User Interface
The program runs in the command prompt or terminal. The user inputs the directory they want to organize and the program sorts the files into folders based on their file type. The `file_extensions.txt` file contains a list of file extensions and their corresponding folder names, which the program uses to determine where to move each file.

## Usage
To use the program, follow these steps:
- Open the command prompt or terminal
- Navigate to the directory where the Python script and `file_extensions.txt` file are located
- Type 'organizefilesbyextention.py' 
- Enter the directory you want to organize when prompted
- The program will sort the files into folders based on their file type, using the `file_extensions.txt` file to determine where to move each file.

## `file_extensions.txt` File Format
The `file_extensions.txt` file is a text file that contains a list of file extensions and their corresponding folder names, separated by a colon (":") character. Each line of the file should contain a single file extension followed by its corresponding folder name, like this:
