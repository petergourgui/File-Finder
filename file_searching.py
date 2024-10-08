from pathlib import Path
import os
import shutil

def first_path() -> (str, Path):
    "Returns a valid letter and Path according to the user's first valid input."
    path = Path()
    letter = ""

    while True:
        letter_and_path = input()
        input_letter = letter_and_path[0:2]
        input_path = Path(letter_and_path[2:])

        if (input_letter == "R " or input_letter == "D ") and input_path.exists() and len(letter_and_path) > 2:
            letter = input_letter
            path = input_path
            return letter, path
        else:
            print("ERROR")
    

def consider_paths(letter: str, path: Path) -> list[Path]:
    '''Prints the path to every file that is under consideration according to the letter and Path
       in lexicographical order and returns a list of the paths to each file.'''
    list_of_files = sorted(list(path.iterdir()))
    final_list = []
    
    if letter == "D ":
        for each_file in list_of_files:
            try:
                if each_file.is_file():
                    print(each_file)
                    final_list.append(each_file)
            except:
                continue

    elif letter == "R ":
        directories_list = []
        for each_file in list_of_files:
            try:
                if each_file.is_file():
                    print(each_file)
                    final_list.append(each_file)
                else:
                    directories_list.append(each_file)
            except:
                continue

        for directory in directories_list:
            try:
                final_list.extend(consider_paths(letter, directory))
            except:
                continue
    
    return final_list


def search_files(considered_files: list[Path]) -> list[Path]:
    '''Reads a line of input that describes the search characteristics
       that will be used to decide whether files are interesting and should
       have action taken on them. Returns a list of Paths of interesting files.'''
    
    while True:
        search_input = input()

        # All files will be considered interesting
        if search_input == "A":
            for each_file in considered_files:
                print(each_file)
            return considered_files
        
        # Files that match the input name will be considered interesting
        elif search_input[:2] == "N " and len(search_input) > 2:
            interesting_files = []
            user_file_name = search_input[2:]
            for each_file in considered_files:
                current_file = str(each_file)
                index = current_file.rfind(user_file_name)
                if index >= 0:
                    sliced_path = current_file[index:]
                    if sliced_path == user_file_name:
                        interesting_files.append(each_file)
                        print(each_file)
            return interesting_files
        
        # Files that end with the input extension will be considered interesting
        elif search_input[:2] == "E " and len(search_input) > 2:
            interesting_files = []
            user_extension = search_input[2:]
            if user_extension.find(".") < 0:
                user_extension = "." + user_extension
            for each_file in considered_files:
                current_file = str(each_file)
                index = current_file.rfind(user_extension)
                if index >= 0:
                    current_extension = current_file[index:]
                    if current_extension == user_extension:
                        interesting_files.append(each_file)
                        print(each_file)
            return interesting_files
        
        # Files that contain input text will be considered interesting
        elif search_input[:2] == "T " and len(search_input) > 2:
            text = search_input[2:]
            interesting_files = []
            for each_file in considered_files:
                current_file = None
                try:
                    current_file = open(each_file, 'r')
                    for line in current_file:
                        if line.endswith('\n'):
                            line = line[:-1]
                        if line.find(text) >= 0:
                            interesting_files.append(each_file)
                            print(each_file)
                            current_file.close()
                            break
                except:
                    continue
                finally:
                    if current_file != None:
                        current_file.close()

            return interesting_files

        # Files less than input size will be considered interesting
        elif search_input[:2] == "< " and len(search_input) > 2:
            interesting_files = []
            try:
                file_size = int(search_input[2:])
            except ValueError:
                print("ERROR")
                continue
            for each_file in considered_files:
                if each_file.stat().st_size < file_size:
                    print(each_file)
                    interesting_files.append(each_file)
            
            return interesting_files

        # Files greater than input size will be considered interesting
        elif search_input[:2] == "> " and len(search_input) > 2:
            interesting_files = []
            try:
                file_size = int(search_input[2:])
            except ValueError:
                print("ERROR")
                continue
            for each_file in considered_files:
                if each_file.stat().st_size > file_size:
                    print(each_file)
                    interesting_files.append(each_file)

            return interesting_files

        else:
            print("ERROR")
        

def take_action(interesting_files: list[Path]) -> None:
    "Performs an action on each interesting file depending on user's first valid input"
    if len(interesting_files) == 0:
        return
    
    while True:
        action_input = input()

        if action_input == "F":
            for each_file in interesting_files:
                try:
                    current_file = open(each_file, 'r')
                    first_line = current_file.readline()
                    if first_line.endswith('\n'):
                        first_line = first_line[:-1]
                    print(first_line)
                except:
                    print("NOT TEXT")
            return
        
        elif action_input == "D":
            for each_file in interesting_files:
                directory, file_name = os.path.split(each_file)
                new_file = file_name + ".dup"
                dup_file = os.path.join(directory, new_file)
                shutil.copy(each_file, dup_file)
            return


        elif action_input == "T":
            for each_file in interesting_files:
                os.utime(each_file)
            return

        else:
            print("ERROR")


if __name__ == '__main__':
    letter, path = first_path()
    list_of_considered = consider_paths(letter, path)
    if len(list_of_considered) != 0:
        interesting_files = search_files(list_of_considered)
        take_action(interesting_files)
