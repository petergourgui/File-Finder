File Finder

This Python-based File Finder allows users to explore directories, filter files based on various criteria, and perform actions on interesting files.
The tool supports operations in both the terminal shell and the management of file structures in a user-friendly manner.

Key Features:

Directory Exploration: Navigate through directories and consider files for further actions based on user-defined criteria.
File Filtering: Filter files based on their names, extensions, content, and sizes.
Actions on Files: Perform various actions, such as displaying the first line of text files, duplicating files, and updating the last accessed time of files.

How to Run:

Simply run the file_searching.py file in order to start the program.
Input format: R <directory_path> or D <directory_path>
    R: Recursive - includes files in subdirectories
    D: Direct - includes only files in the specified directory

After specifying a valid path, you'll have options to filter files based on:

A: Show all files.
N <file_name>: Show files with the specified name.
E <file_extension>: Show files with the specified extension.
T <text>: Show files containing the specified text.
< <size>: Show files smaller than the specified size.
> <size>: Show files larger than the specified size.


Perform Actions
For the files identified as "interesting," you can perform the following actions:

F: Display the first line of text files.
D: Duplicate selected files (adds ".dup" suffix).
T: Update the last accessed time of selected files.