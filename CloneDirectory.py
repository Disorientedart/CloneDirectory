import os


# Add the Args information to the project to increase usability
_Source_File = ""
_Destination_File = ""


def get_contents_directory(path):
    for root, dirs, files in os.walk(path):
        return dirs


def get_folder_contents(path):
    for root, dirs, files in os.walk(path):
        return files


def get_files_existence(path):
    for root, dirs, files in os.walk(path):
        return len(dirs) >= 0


def make_copy_file(path):
    if not os.path.exists(path):
        os.mkdir(path)


def suffix_current_directory(path, folder):
    return path + "\\" + folder


def copy_files_to_new_location(path, folder_contents):
    for content in folder_contents:
        full_path = suffix_current_directory(path, content)
        if not os.path.exists(full_path):
            new_file = open(full_path, "w+")
            new_file.close()


def copy_the_working_path(folder, destination):
    print folder
    full_contents = get_folder_contents(folder)
    copy_files_to_new_location(destination, full_contents)
    print "complete"


def create_duplicates(operation_path, copy_path):
    current_contents = get_contents_directory(operation_path)
    for folder in current_contents:
        current_file = suffix_current_directory(operation_path, folder)
        current_copy_path = suffix_current_directory(copy_path, folder)
        make_copy_file(current_copy_path)
        copy_the_working_path(current_file, current_copy_path)
        if get_files_existence(current_file):
            create_duplicates(current_file, current_copy_path)


create_duplicates(_Source_File, _Destination_File)


