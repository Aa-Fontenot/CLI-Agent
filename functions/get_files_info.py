

def get_file_info(working_directory, directory="."):
    absolute_workingdir_path = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(absolute_workingdir_path, directory))
    commonpath = os.path.commonpath([absolute_workingdir_path, target_directory]) == absolute_workingdir_path
    if commonpath == False:
        f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if 
