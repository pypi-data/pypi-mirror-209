import os, platform, shutil, math
from sys import executable as python_executable, argv as python_argv, exit as python_exit
from pathlib import Path
from subprocess import call
from n4s import strgs

## WINDOWS BACKSLASHES
backslash = "\\"

## COPY FILES
def copy_file(Source: Path, Destination: Path='', overwrite: bool=False, debug: bool=False):
    '''
    Source: path to file(s)
    Destination: path to place copied file(s)
    overwrite: (boolean), enable to overwrite existing files
    debug: (boolean)
    '''

    ## CHECK IF DESTINATION IS A DIRECTORY OR FILE PATH
    if read_format(Destination, False) == '':
        is_dir = True
    else:
        is_dir = False

    ## COPY A LIST OF FILES
    if type(Source) == list:

        ## PASS EACH ITEM IN LIST TO FUNCTION
        if overwrite: ## OVERWRITE ENABLED
            for x in range(len(Source)):
                copy_file(Source[x], Destination, True)

                ## DEBUG: PRINT COMPLETION MESSAGE
                if debug:
                    print("\nn4s.fs.copy_file():\n"
                            f"Source => {Source[x]}\nDestination => {Destination}\n")
        else: ## OVERWRITE DISABLED
            for x in range(len(Source)):
                copy_file(Source[x], Destination, False)

                ## DEBUG: PRINT COMPLETION MESSAGE
                if debug:
                    print("\nn4s.fs.copy_file():\n"
                            f"Source => {Source[x]}\nDestination => {Destination}\n")
    
    ## COPY A SINGLE FILE
    elif type(Source) == str:

        ## VALIDATE SOURCE
        if path_exists(Source):

            ## GET SOURCE FILENAME
            if system('is-mac'):
                src_filename = str(Source).split('.')[0].split('/')[-1]
            else:
                src_filename = str(Source).split('.')[0].split('\\')[-1]

            ## IF NO DEST., USE SOURCE DIR AND ITERATE WITH INT
            if Destination == '':

                ## ITERATE COPIES WITH NUMERICAL VALUES
                for i in range(1, 100):
                    if path_exists(f"{Source.replace(src_filename, f'{src_filename}({i})')}"):
                        Destination = f"{Source.replace(src_filename, f'{src_filename}({i+1})')}"
                    else:
                        Destination = f"{Source.replace(src_filename, f'{src_filename}({i})')}"
                        break
            
            ## IF DEST. EXISTS, ITERATE WITH INT
            if path_exists(Destination):

                ## GET DESTINATION FILENAME
                if system('is-mac'):
                    dest_filename = str(Destination).split('.')[0].split('/')[-1]
                else:
                    dest_filename = str(Destination).split('.')[0].split('\\')[-1]
                file_format = read_format(Source, True)

                ## IF DESTINATION IS A DIRECTORY
                if is_dir:

                    ## OVERWRITE DISABLED
                    if not overwrite:

                        ## ITERATE COPIES WITH NUMERICAL VALUES
                        for i in range(1, 100):
                            if system('is-mac'):
                                if path_exists(f"{Destination.replace(dest_filename, f'{dest_filename}/{src_filename}({i}){file_format}')}"):
                                    Destination = f"{Destination.replace(f'{dest_filename}({i})', f'{dest_filename}/{src_filename}({i+1}){file_format}')}"
                                else:
                                    if path_exists(f"{Destination.replace(dest_filename, f'{dest_filename}/{src_filename}{file_format}')}"):
                                        Destination = f"{Destination.replace(dest_filename, f'{dest_filename}/{src_filename}({i}){file_format}')}"
                                    break
                            else:
                                if path_exists(f"{Destination.replace(dest_filename, f'{dest_filename}{backslash}{src_filename}({i}){file_format}')}"):
                                    Destination = f"{Destination.replace(f'{dest_filename}({i})', f'{dest_filename}{backslash}{src_filename}({i+1}){file_format}')}"
                                else:
                                    if path_exists(f"{Destination.replace(dest_filename, f'{dest_filename}{backslash}{src_filename}{file_format}')}"):
                                        Destination = f"{Destination.replace(dest_filename, f'{dest_filename}{backslash}{src_filename}({i}){file_format}')}"
                                    break

                ## IF DESTINATION IS A FILE PATH
                else:

                    ## OVERWRITE DISABLED
                    if not overwrite:

                        ## ITERATE COPIES WITH NUMERICAL VALUES
                        for i in range(1, 100):
                            if path_exists(f"{Destination.replace(dest_filename, f'{dest_filename}({i})')}"):
                                Destination = f"{Destination.replace(f'{dest_filename}({i})', f'{dest_filename}({i+1})')}"
                            else:
                                Destination = f"{Destination.replace(dest_filename, f'{dest_filename}({i})')}"
                                break
            
            ## COPY FILE
            shutil.copy(Source, Destination)

            ## DEBUG: PRINT COMPLETION MESSAGE
            if debug:
                return print("\nn4s.fs.copy_file():\n"
                            f"Source => {Source}\nDestination => {Destination}\n") 
        else:
            if debug:
                return print("\nn4s.fs.copy_file():\n"
                            f"Does Not Exist => {Source}\n")
            return

## SEND MAIL
def mail(Send_To: str='', Subject: str='', Body: str='', Attachment: Path=''):

    ## SUPPORT FOR MACOS
    if system('is-mac'):

        ## IMPORT LIBRARIES
        from appscript import app as app_script, k
        from mactypes import Alias

        ## CALL MAIL APP
        mail = app_script('Mail')

        ## COMPOSE MESSAGE W/ SUBJECT AND BODY
        msg = mail.make(
            new=k.outgoing_message,
            with_properties={
                k.subject: f'{str(Subject)}',
                k.content: f'{str(Body)}\n\n'})

        ## ADD ATTACHMENT, IF ANY
        if not Attachment == '':
            attachment = Path(Attachment)
            p = Alias(str(attachment)) # convert string/path obj to POSIX/mactypes path
            msg.content.paragraphs[-1].after.make(new=k.attachment,
                with_properties={k.file_name: p})

        ## ADD RECIPIENT
        msg.make(new=k.to_recipient, 
            with_properties={k.name: Send_To})

        ## ACTIVATE MAIL APP
        msg.activate()
    else:
        return print('n4s.fs.mail() - ONLY supports macOS at this moment!')

## CHECK IF PATH EXISTS
def path_exists(Path: Path, Make: bool=False, debug: bool=False):
    '''
    Path: Path to directories/files (str or list)
    Make: Create directory/file if it does not exist (boolean)
    debug: (boolean)
    '''
    ## CATCH ERROR
    try:
        
        ## IF ALL PATHS ALREADY EXIST
        all_paths_exists = True
        ## IF PATH IS A LIST OF PATHS
        if type(Path) == list:
            for x in range(len(Path)):
                ## IF PATHS ARE FILES && EXIST
                if os.path.isfile(Path[x]):
                    ## DEBUG: FILES EXIST
                    if debug:
                        print("\nn4s.fs.path_exists():\n"
                                    f"File Exists - {Path[x]}\n") 
                    ## AT COMPLETION
                    if x+1 == len(Path):
                        if debug and all_paths_exists:
                            print("All Paths Exist")
                        return True
                ## IF PATHS ARE NOT FILES.....
                else:
                    ## IF PATHS ARE DIRS && EXIST
                    if os.path.isdir(Path[x]):
                        ## DEBUG: DIRS EXIST
                        if debug:
                            print("\nn4s.fs.path_exists():\n"
                                        f"Directory Exists - {Path[x]}\n") 
                        if x+1 == len(Path):
                            if debug and all_paths_exists:
                                print("All Paths Exist")
                            return True
                    ## IF PATH DOES NOT EXIST....
                    else:
                        ## ALL PATHS WERE NOT FOUND
                        all_paths_exists = False
                        ## IF MAKE IS ENABLED AND PATH IS NOT A FILENAME
                        if Make and not "." in Path[x]:
                            ## CREATE THE DIRECTORY
                            os.makedirs(Path[x])
                            ## DEBUG: DIR CREATED
                            if debug:
                                print("\nn4s.fs.path_exists():\n"
                                        f"Created Dir - {Path[x]}\n")
                            if x+1 == len(Path):
                                return True
                        ## IF MAKE IS ENABLED AND PATH IS A HIDDEN DIRECTORY
                        elif Make and str(Path[x]).split('/')[-1][0] == '.' and not len(str(Path[x]).split('/')[-1].split('.')) == 3:
                            ## MAC ONLY
                            if system('is-mac'):
                                ## CREATE DIRECTORY
                                os.makedirs(Path[x])
                                ## DEBUG: FILE CREATED
                                if debug:
                                    print("\nn4s.fs.path_exists():\n"
                                            f"Created Directory - {Path[x]}\n")
                            else:
                                print("\nn4s.fs.path_exists():\n"
                                    f"Invalid Input - {Path[x]}\n"
                                    "Cannot have '.' in pathname!\n") 
                        ## IF MAKE IS ENABLED AND PATH IS A FILENAME
                        elif Make:
                            ## CREATE THE FILE
                            open(Path[x], 'x')
                            ## DEBUG: FILE CREATED
                            if debug:
                                print("\nn4s.fs.path_exists():\n"
                                        f"Created File - {Path[x]}\n")
                            if x+1 == len(Path):
                                return True
                        ## IF MAKE IS DISABLED
                        else:
                            if debug:
                                print("\nn4s.fs.path_exists():\n"
                                        f"Does Not Exist - {Path[x]}\n")
                            return False
        ## IF PATH IS A SINGLE STRING
        else:
            ## IF PATH IS A FILE && EXISTS
            if os.path.isfile(Path):
                ## DEBUG: FILE EXISTS
                if debug:
                    print("\nn4s.fs.path_exists():\n"
                                f"File Exists - {Path}\n") 
                return True
            ## IF PATH IS NOT A FILE......
            else:
                ## IF PATH IS A DIR && EXISTS
                if os.path.isdir(Path):
                    ## DEBUG: DIR EXISTS
                    if debug:
                        print("\nn4s.fs.path_exists():\n"
                                    f"Directory Exists - {Path}\n") 
                    return True
                ## IF PATH DOES NOT EXIST....
                else:
                    ## ALL PATHS WERE NOT FOUND
                    all_paths_exists = False
                    ## IF MAKE IS ENABLED AND PATH IS NOT A FILENAME
                    if Make and not "." in Path:
                        ## CREATE THE DIRECTORY
                        os.makedirs(Path)
                        ## DEBUG: DIR CREATED
                        if debug:
                            print("\nn4s.fs.path_exists():\n"
                                    f"Created - {Path}\n")
                        return True
                    ## IF MAKE IS ENABLED AND PATH IS A HIDDEN DIRECTORY
                    elif Make and str(Path).split('/')[-1][0] == '.' and not len(str(Path).split('/')[-1].split('.')) == 3:
                        ## MAC ONLY
                        if system('is-mac'):
                            ## CREATE DIRECTORY
                            os.makedirs(Path)
                            ## DEBUG: FILE CREATED
                            if debug:
                                print("\nn4s.fs.path_exists():\n"
                                        f"Created Directory - {Path}\n")
                        else:
                            return print("\nn4s.fs.path_exists():\n"
                                f"Invalid Input - {Path}\n"
                                "Cannot have '.' in pathname!\n") 
                    ## IF MAKE IS ENABLED AND PATH IS A FILENAME
                    elif Make:
                        ## CREATE THE FILE
                        open(Path, 'x')
                        ## DEBUG: FILE CREATED
                        if debug:
                            print("\nn4s.fs.path_exists():\n"
                                    f"Created File - {Path}\n")
                        return True
                    ## IF MAKE IS DISABLED
                    else:
                        if debug:
                            print("\nn4s.fs.path_exists():\n"
                                    f"Does Not Exist - {Path}\n") 
                        return False
    ## PATH != LIST OR STR
    except Exception:
        return print("\nn4s.fs.path_exists():\n"
                                f"Invalid Input - {Path}\n"
                                "Make sure path is type(list) or type(string), "
                                "and that parent directories are created before nesting files\n") 

## READ THE CONTENTS OF A DIRECTORY
def read_dir(Source: Path, Output: str='content', Ignore: list=[], Filter: list=[], Print: bool=False, Hidden: bool=False, debug: bool=False):
    '''
    Source: (str) path to a directory
    
    Output: 'content', 'files', 'dirs', 'content_count', 'file_count', 'dir_count'

    Ignore: (list) of files and dirs to ignore

    Filter: (list) or (str) of filetypes to target in your search ('docs', 'images')

    Print: (bool) print file/dir names to terminal

    Hidden: (bool) include hidden files

    debug: (bool) print results to terminal
    '''

    ## INITIALIZE FILE LIST
    file_list = []

    ## INITIALIZE DIR LIST
    dir_list = []

    ## INITIALIZE TOTAL LIST
    if not system('is-mac') or Hidden:
        total_list = os.listdir(Source)
    else:
        import Foundation
        url = Foundation.NSURL.fileURLWithPath_(Source)
        fm = Foundation.NSFileManager.defaultManager()
        urls = fm.contentsOfDirectoryAtURL_includingPropertiesForKeys_options_error_(
            url, [], Foundation.NSDirectoryEnumerationSkipsHiddenFiles, None)[0]
        total_list = [u.path() for u in urls]
        for x in range(len(total_list)):
            total_list[x] = total_list[x].split('/')[-1]

    ## FILTER TOTAL LIST - VIA LIST
    if type(Ignore) == list:
        if len(Ignore) > 0:
            for x in range(len(Ignore)):
                
                ## ADD FILE EXTENSION IF NOT PASSED IN
                if not str(Ignore[x]).endswith(read_format(Ignore[x], True)):
                    for y in range(len(total_list)):
                        if Ignore[x] == str(total_list[y]).split('.')[0]:
                            Ignore[x] = total_list[y]
                
                ## REMOVE FROM TOTAL
                if Ignore[x] in total_list:
                    total_list.remove(Ignore[x])

    ## FILTER TOTAL LIST - VIA STRING
    if type(Ignore) == str:
        if not Ignore == '':

            ## ADD FILE EXTENSION IF NOT PASSED IN
            if not str(Ignore).endswith(read_format(Ignore, True)):
                for x in range(len(total_list)):
                    if Ignore == str(total_list[x]).split('.')[0]:
                        Ignore = total_list[x]
            
            ## REMOVE FROM TOTAL
            if Ignore in total_list:
                total_list.remove(Ignore)

    ## INITIALIZE SKIPPED FILES LIST
    skipped_list = []

    ## READ LIST OF FILES
    try:
        for x in range(len(total_list)):
            try:
                if not total_list[x] == '':
                    if os.path.isfile(f"{Source}/{total_list[x]}"):
                        file_list.append(total_list[x])
                    elif os.path.isdir(f"{Source}/{total_list[x]}"):
                        dir_list.append(total_list[x])
            except Exception:
                skipped_list.append(total_list[x])
    except Exception as e:
        if debug:
            print("\nn4s.fs.list_files():\n"
                    f"Invalid Input - {Source}\n"
                    f"Make sure path is a valid (str) of a directory\n")
            return print(e)
        return

    if type(Filter) == str and not Filter == '':
        if Filter.lower() == 'documents' or Filter.lower() == 'docs' or Filter.lower() == 'text' or Filter.lower() == 'txt':
            Filter = ['doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'htm', 'odt', 'pdf', 'rtf', 'txt', 'wps', 'xml', 'xps',
            'csv', 'dbf', 'dif', 'ods', 'prn', 'slk', 'xla', 'xlam', 'xls', 'xlsb', 'xlsm', 'xlsx', 'xltm', 'xltx', 'xlw',
            'pptx', 'ppt', 'ppsx', 'pps']
        elif Filter.lower() == 'images' or Filter.lower() == 'pictures' or Filter.lower() == 'pics' or Filter.lower() == 'photos':
            Filter = ['bmp', 'dng', 'eps', 'gif', 'jpg', 'jpeg', 'nef', 'png', 'raw']
        for x in range(len(total_list)):
            try:
                if read_format(str(total_list[x]).lower()) not in Filter:
                    if total_list[x] in file_list:
                        file_list.remove(total_list[x])
                        skipped_list.append(total_list[x])
                    # total_list.remove(total_list[x])
            except IndexError as e:
                print(e)

    ## PRINT TO TERMINAL
    if Print:
        if Output == 'files' or Output == 'file_count':
            print()
            for x in range(len(file_list)):
                print(file_list[x])
        elif Output == 'directories' or Output == 'dirs' or Output == 'dir_count':
            print()
            for x in range(len(dir_list)):
                print(dir_list[x])
        else:
            print('\nDirectories:\n')
            for x in range(len(dir_list)):
                print(dir_list[x])
            print('\nFiles:\n')
            for x in range(len(file_list)):
                print(file_list[x])

    ## PRINT DEBUG TO TERMINAL
    if debug:
        if len(skipped_list) > 0:
            print(f"\nSkipped:\n{skipped_list}")
            print(f"Skip Count: {len(skipped_list)}")
        print(f"\nFound: {len(file_list)} files")
        print(f"Found: {len(dir_list)} directories")
        print(f"Total: {len(total_list)}")

    ## RETURN
    if Output == 'content':
        return total_list
    if Output == 'files':
        return file_list
    if Output == 'directories' or Output == 'dirs':
        return dir_list
    if Output == 'content_count':
        return len(total_list)
    if Output == 'file_count':
        return len(file_list)
    if Output == 'directory_count' or Output == 'dir_count':
        return len(dir_list)

## READS FILE SIZES
def read_filesize(File: Path, Print: bool=False, Bytes: bool=False, debug: bool=False):
    
    file_size = os.path.getsize(File)

    ## CAST FILE SIZE AS INT
    file_size = int(file_size)
    
    ## CONVERT FILE SIZE
    if file_size == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(file_size, 1024)))
    p = math.pow(1024, i)
    s = round(file_size / p, 2)

    # RETURN FILE SIZE IN BYTES
    if Bytes:
        if Print:
            print(file_size)
        return file_size
    
    ## RETURN FILE SIZE (FORMATTED)
    if Print:
        print("%s %s" % (s, size_name[i]))
    return "%s %s" % (s, size_name[i])

## READS FILE EXTENSIONS
def read_format(Input: str, Include_Period: bool=False, Print: bool=False, Uppercase: bool=False, Read_Filename: bool=False):

    ## INCLUDE PERIOD IN FORMAT
    if Include_Period:
        file_format = f".{Input.split('.')[-1]}"
    
    ## RETURN FORMAT WITHOUT PERIOD
    else:
        file_format = Input.split('.')[-1]

    ## CLEAR SPECIAL CHARACTERS
    if '?' in file_format:
        file_format = file_format.split('?')[0]
    if '/' in file_format:
        file_format = file_format.split('/')[0]
    
    ## IF UPPERCASE == ENABLED
    if Uppercase:
        file_format = file_format.upper()

    ## IF READ_FILENAME == ENABLED
    if Read_Filename:

        ## GET FILENAME
        file_name = strgs.filter_text(Input.split('/')[-1], [file_format])

        ## PRINT FORMAT TO TERMINAL
        if Print:
            print(file_name)

        ## RETURN FORMAT
        return file_name

    ## PRINT FORMAT TO TERMINAL
    if Print:
        print(file_format)

    ## RETURN FORMAT
    return file_format

## READS THE NAME OF THE FILE/DIR AT THE END OF A PATH
def read_pathname(Source: Path, Include_Format: bool=False, Print: bool=False):
    '''
    Source: Input path
    Include_Format: Include file extension if applicable
    Print: Print to terminal
    '''
    print_arg = Print
    if Source[-1] == '/' or Source[-1] == backslash:
        Source = Source[:-1]
    return read_format(Input=Source, Include_Period=True, Print=print_arg, Uppercase=Include_Format, Read_Filename=True)

## REMOVE DIRECTORIES
def remove_dir(Directory: Path, debug: bool=False):
    '''
    Directory: Path to directories
    debug: (boolean)
    '''
    if type(Directory) == list:
        Dirs = Directory
        for x in range(len(Dirs)):
            if os.path.isdir(Dirs[x]):
                shutil.rmtree(Dirs[x])
                if debug:
                    print("\nn4s.fs.remove_dir():\n"
                            f"Removed - {Dirs[x]}\n") 
            else:
                if debug:
                    print("\nn4s.fs.remove_dir():\n"
                            f"Does Not Exist - {Dirs[x]}\n")
    elif type(Directory) == str:
        if os.path.isdir(Directory):
            shutil.rmtree(Directory)
            if debug:
                return print("\nn4s.fs.remove_dir():\n"
                            f"Removed - {Directory}\n") 
        else:
            if debug:
                return print("\nn4s.fs.remove_dir():\n"
                            f"Does Not Exist - {Directory}\n")

## REMOVE FILES
def remove_file(File: Path, debug: bool=False):
    '''
    File: Path to files
    debug: (boolean)
    '''
    if type(File) == list:
        Files = File
        for x in range(len(Files)):
            if os.path.isfile(Files[x]):
                os.remove(Files[x])
                if debug:
                    print("\nn4s.fs.remove_file():\n"
                            f"Removed - {Files[x]}\n") 
            else:
                if debug:
                    print("\nn4s.fs.remove_file():\n"
                            f"Does Not Exist - {Files[x]}\n")
    elif type(File) == str:
        if os.path.isfile(File):
            os.remove(File)
            if debug:
                return print("\nn4s.fs.remove_file():\n"
                            f"Removed - {File}\n") 
        else:
            if debug:
                return print("\nn4s.fs.remove_file():\n"
                            f"Does Not Exist - {File}\n")

## RENAME FILE / DIR
def rename(Name: Path, Rename: str='', debug: bool=False):
    '''
    Name: Path to input file
    Rename: str of the new file/dir name (do not use a full file path!)
    debug: (boolean)
    '''
    ## VALIDATE INPUT PATH
    if not path_exists(Name):
        if debug:
            return print("\nn4s.fs.rename():\n"
                            f"Does Not Exist - {Name}\n")
        return

    ## LIST OF ROOT DIRS
    root_dirs = [
        str(root('user')),
        str(root('desktop')),
        str(root('docs')),
        str(root('dl')),
        str(root('applications')),
        str(root('userlib')),
        str(root('syslib')),
        '/Users/afshari/test',
        '/Users/afshari/Desktop/index'
    ] 
    
    ## PREVENT RENAMING ROOT DIRS
    for i in range(len(root_dirs)):
        if Name == root_dirs[i] or Name == f"{root_dirs[i]}/":
            if debug:
                return print("\nn4s.fs.rename():\n"
                            f"Cannot rename a user directory - {Name}\n")
            return

    ## CAPTURE INPUT PATH
    Pathname = Name

    ## CHECKS FOR TRAILING '/' DASH
    if system('is-mac'):
        if str(Name[-1]) == '/':
            Name = str(Name.split('/')[-2])
        else:
            Name = str(Name.split('/')[-1])
    else:
        if str(Name[-1]) == '\\':
            Name = str(Name.split('\\')[-2])
        else:
            Name = str(Name.split('\\')[-1])

    ## UPDATE INPUT PATH
    Pathname = strgs.filter_text(Pathname, [Name])
    
    ## VALIDATE RENAME ARG
    if Rename == '':
        if debug:
            return print("\nn4s.fs.rename():\n"
                        f"Rename arg can't be blank!\n")
        return

    ## CHECKS IF RENAME ALREADY EXISTS
    if path_exists(f"{Pathname}{Rename}"):
        if debug:
            return print("\nn4s.fs.rename():\n"
                            f"Rename already exists => {Rename}\n"
                            f"{Pathname}{Rename}\n")
        return

    ## ASSIGN FULL PATH NAMES
    Name = f"{Pathname}{Name}"
    Rename = f"{Pathname}{Rename}"

    ## CHECK FOR EXCPLICIT FILE EXTENSION
    if system('is-mac'):
        if not '.' in str(Rename).split('/')[-1]:
            inherited_format = read_format(Name, True)
            Rename = f"{Rename}{inherited_format}"
    else:
        if not '.' in str(Rename).split('\\')[-1]:
            inherited_format = read_format(Name, True)
            Rename = f"{Rename}{inherited_format}"

    ## RUN RENAME
    os.rename(Name, Rename)

    ## DEBUG: PRINT RESULTS
    if debug:
        print("\nn4s.fs.rename():\n"
                            f"Name => {Name}\n"
                            f"Rename => {Rename}\n")

## AMEND ALL FILENAMES WITHIN A DIRECTORY
def amend_filenames(Directory: Path, Action='add', Rename: str='', Nested: bool=False, Output: str='', debug: bool=False):
    '''
    Add / Remove text from all filenames within a directory

    Directory: Path to input dir
    Action: 'add' OR 'remove'
    Rename: str to add or remove
    Nested: Iterate through one level of sub-directories
    debug: Enable debugging console
    '''

    ## COUNT CHANGES
    amend_count = 0
    total_files = 0

    ## DEBUG HEADER
    if debug:
        print("\nn4s.fs.amend_filenames():")
    
    ## ADD TEXT TO FILE NAMES
    if Action == 'add':

        ## ITERATE THROUGH NESTED DIRECTORIES
        if Nested:

            ## COUNT OF NUMBER OF NESTED DIRECTORIES
            dirs_count = read_dir(Directory, 'dir_count')

            ## LIST OF DIRECTORIES NESTED WITHIN INPUT DIR
            dirs_list = read_dir(Directory, 'dirs')

            ## ASSIGN FULL PATHNAME TO DIRS LIST
            for x in range(dirs_count):

                ## MACOS
                if system('is-mac'):
                    dirs_list[x] = f"{Directory}/{dirs_list[x]}"
                
                ## WINDOWS
                else:
                    dirs_list[x] = f"{Directory}{backslash}{dirs_list[x]}"

            ## ITERATE THROUGH DIRECTORIES WITHIN INPUT DIR
            for i in range(dirs_count):

                ## LIST OF FILES WITHIN DIRECTORY
                file_list = sorted(read_dir(dirs_list[i], 'files'))

                ## COUNT OF FILES WITHIN DIRECTORY
                file_count = read_dir(dirs_list[i], 'file_count')

                ## RENAME FILES
                for file in range(file_count):

                    ## MACOS
                    if system('is-mac'):

                        ## ORIGINAL FILENAME
                        og_filename = f"{dirs_list[i]}/{file_list[file]}"

                        ## AMENDED FILENAME
                        new_filename = f"{read_format(file_list[file], True, Read_Filename=True)}{Rename}"

                        ## RENAME FILE
                        rename(og_filename, new_filename)

                        ## OUTPUT OR DEBUG
                        if Output == 'amend_count' or debug:

                            ## IF FILENAME WAS CHANGED
                            if not og_filename == f"{dirs_list[i]}/{new_filename}":
                            
                                ## PRINT DEBUG MESSAGE
                                if debug:
                                    print(f"\nOriginal: {og_filename}\n"
                                        f"Amended: {dirs_list[i]}/{new_filename}")

                                ## ADD TO AMEND COUNT
                                amend_count += 1

                            ## IF FILENAME WAS NOT CHANGED
                            else:
                                print(f"No Change: {dirs_list[i]}/{file_list[file]}")

                            ## PRESENT TOTAL CHANGES
                            if file == file_count - 1:
                                total_files = total_files + file_count

                    ## WINDOWS
                    else:

                        ## ORIGINAL FILENAME
                        og_filename = f"{dirs_list[i]}{backslash}{file_list[file]}"

                        ## AMENDED FILENAME
                        new_filename = f"{read_format(file_list[file], True, Read_Filename=True)}{Rename}"

                        ## RENAME FILE
                        rename(og_filename, new_filename)
                        
                        ## OUTPUT OR DEBUG
                        if Output == 'amend_count' or debug:

                            ## IF FILENAME WAS CHANGED
                            if not og_filename == f"{dirs_list[i]}{backslash}{new_filename}":
                            
                                ## PRINT DEBUG MESSAGE
                                if debug:
                                    print(f"\nOriginal: {og_filename}\n"
                                        f"Amended: {dirs_list[i]}{backslash}{new_filename}")

                                ## ADD TO AMEND COUNT
                                amend_count += 1

                            ## IF FILENAME WAS NOT CHANGED
                            else:
                                print(f"No Change: {dirs_list[i]}{backslash}{file_list[file]}")

                            ## PRESENT TOTAL CHANGES
                            if file == file_count - 1:
                                total_files = total_files + file_count
        
                ## END OF DIR LOOP
                if i == dirs_count - 1:

                    ## PRINT TOTALS
                    if debug:
                        print(f"\nTotal Files: {total_files} | Amended: {amend_count}")

                    ## RETURN AMEND COUNT
                    if Output == 'amend_count':
                        return amend_count

        ## SINGLE DIRECTORY, ITERATE THROUGH FILES ONLY
        else:
        
            ## LIST OF FILES WITHIN DIRECTORY
            file_list = sorted(read_dir(Directory, 'files'))

            ## COUNT OF FILES WITHIN DIRECTORY
            file_count = read_dir(Directory, 'file_count')

            ## RENAME FILES
            for file in range(file_count):
                
                ## MACOS
                if system('is-mac'):

                    ## ORIGINAL FILENAME
                    og_filename = f"{Directory}/{file_list[file]}"

                    ## AMENDED FILENAME
                    new_filename = f"{read_format(file_list[file], True, Read_Filename=True)}{Rename}"

                    ## RENAME FILE
                    rename(og_filename, new_filename)
                    
                    ## OUTPUT OR DEBUG
                    if Output == 'amend_count' or debug:

                        ## IF FILENAME WAS CHANGED
                        if not og_filename == f"{Directory}/{new_filename}":
                            
                            ## PRINT DEBUG MESSAGE
                            if debug:
                                print(f"\nOriginal: {og_filename}\n"
                                    f"Amended: {Directory}/{new_filename}")

                            ## ADD TO AMEND COUNT
                            amend_count += 1

                        ## IF FILENAME WAS NOT CHANGED
                        else:
                            print(f"No Change: {Directory}/{file_list[file]}")

                        ## PRESENT TOTAL CHANGES
                        if file == file_count - 1:
                            if debug:
                                print(f"\nTotal Files: {file_count} | Amended: {amend_count}")
                            if Output == 'amend_count':
                                return amend_count
                
                ## WINDOWS
                else:

                    ## ORIGINAL FILENAME
                    og_filename = f"{Directory}{backslash}{file_list[file]}"

                    ## AMENDED FILENAME
                    new_filename = f"{read_format(file_list[file], Include_Period=True, Read_Filename=True)}{Rename}{read_format(file_list[file], Include_Period=True)}"

                    ## RENAME FILE
                    rename(og_filename, new_filename)
                    
                    ## OUTPUT OR DEBUG
                    if Output == 'amend_count' or debug:

                        ## IF FILENAME WAS CHANGED
                        if not og_filename == f"{Directory}{backslash}{new_filename}":
                            
                            ## PRINT DEBUG MESSAGE
                            if debug:
                                print(f"\nOriginal: {og_filename}\n"
                                    f"Amended: {Directory}{backslash}{new_filename}")

                            ## ADD TO AMEND COUNT
                            amend_count += 1

                        ## IF FILENAME WAS NOT CHANGED
                        else:
                            print(f"No Change: {Directory}{backslash}{file_list[file]}")

                        ## PRESENT TOTAL CHANGES
                        if file == file_count - 1:
                            if debug:
                                print(f"\nTotal Files: {file_count} | Amended: {amend_count}")
                            if Output == 'amend_count':
                                return amend_count

    ## REMOVE TEXT FROM FILE NAMES
    if Action == 'remove':

        ## ITERATE THROUGH NESTED DIRECTORIES
        if Nested:

            ## COUNT OF NUMBER OF NESTED DIRECTORIES
            dirs_count = read_dir(Directory, 'dir_count')

            ## LIST OF DIRECTORIES NESTED WITHIN INPUT DIR
            dirs_list = read_dir(Directory, 'dirs')

            ## ASSIGN FULL PATHNAME TO DIRS LIST
            for x in range(dirs_count):
                
                ## MACOS
                if system('is-mac'):
                    dirs_list[x] = f"{Directory}/{dirs_list[x]}"
                
                ## WINDOWS
                else:
                    dirs_list[x] = f"{Directory}{backslash}{dirs_list[x]}"

            ## ITERATE THROUGH DIRECTORIES WITHIN INPUT DIR
            for i in range(dirs_count):

                ## LIST OF FILES WITHIN DIRECTORY
                file_list = sorted(read_dir(dirs_list[i], 'files'))

                ## COUNT OF FILES WITHIN DIRECTORY
                file_count = read_dir(dirs_list[i], 'file_count')

                ## RENAME FILES
                for file in range(file_count):
                    
                    ## MACOS
                    if system('is-mac'):

                        ## ORIGINAL FILENAME
                        og_filename = f"{dirs_list[i]}/{file_list[file]}"

                        ## AMENDED FILENAME
                        new_filename = strgs.filter_text(file_list[file], [Rename])

                        ## RENAME FILE
                        rename(og_filename, new_filename)
                        
                        ## DEBUG
                        if Output == 'amend_count' or debug:

                            ## IF FILENAME WAS CHANGED
                            if not og_filename == f"{dirs_list[i]}/{new_filename}":

                                ## PRINT DEBUG MESSAGE
                                if debug:
                                    print(f"\nOriginal: {og_filename}\n"
                                        f"Amended: {dirs_list[i]}/{new_filename}\n")

                                ## ADD TO AMEND COUNT
                                amend_count += 1

                            ## IF FILENAME WAS NOT CHANGED
                            else:
                                print(f"No Change: {dirs_list[i]}/{new_filename}")

                            ## PRESENT TOTAL CHANGES
                            if file == file_count - 1:
                                total_files = total_files + file_count

                    ## WINDOWS
                    else:
                        rename(f"{dirs_list[i]}{backslash}{file_list[file]}", strgs.filter_text(file_list[file], [Rename]))
                        if debug:
                            print("\nn4s.fs.amend_filenames():\n"
                                f"Original: {dirs_list[i]}{backslash}{file_list[file]}\n"
                                f"Amended: {read_format(file_list[file], True, Read_Filename=True)}{Rename}\n")
                
                ## END OF DIR LOOP
                if i == dirs_count - 1:

                    ## PRINT TOTALS
                    if debug:
                        print(f"\nTotal Files: {total_files} | Amended: {amend_count}")

                    ## RETURN AMEND COUNT
                    if Output == 'amend_count':
                        return amend_count

        ## SINGLE DIRECTORY, ITERATE THROUGH FILES ONLY
        else:

            ## LIST OF FILES WITHIN DIRECTORY
            file_list = sorted(read_dir(Directory, 'files'))

            ## COUNT OF FILES WITHIN DIRECTORY
            file_count = read_dir(Directory, 'file_count')

            ## AMEND FILENAMES
            for file in range(file_count):
                
                ## MACOS
                if system('is-mac'):

                    ## ORIGINAL FILENAME
                    og_filename = f"{Directory}/{file_list[file]}"

                    ## AMENDED FILENAME
                    new_filename = strgs.filter_text(file_list[file], [Rename])

                    ## RENAME FILE
                    rename(og_filename, new_filename)

                    ## DEBUG
                    if Output == 'amend_count' or debug:

                        ## IF FILENAME WAS CHANGED
                        if not og_filename == f"{Directory}/{new_filename}":

                            ## PRINT DEBUG MESSAGE
                            if debug:
                                print(f"\nOriginal: {og_filename}\n"
                                    f"Amended: {Directory}/{new_filename}")
                            
                            ## ADD TO AMEND COUNT
                            amend_count += 1

                        ## IF FILENAME WAS NOT CHANGED
                        else:
                            print(f"No Change: {Directory}/{file_list[file]}")

                        ## PRESENT TOTAL CHANGES
                        if file == file_count - 1:
                            if debug:
                                print(f"\nTotal Files: {file_count} | Amended: {amend_count}")
                            if Output == 'amend_count':
                                return amend_count
                
                ## WINDOWS
                else:
                    
                    ## ORIGINAL FILENAME
                    og_filename = f"{Directory}{backslash}{file_list[file]}"

                    ## AMENDED FILENAME
                    new_filename = strgs.filter_text(file_list[file], [Rename])

                    ## RENAME FILE
                    rename(og_filename, new_filename)

                    ## DEBUG
                    if Output == 'amend_count' or debug:

                        ## IF FILENAME WAS CHANGED
                        if not og_filename == f"{Directory}{backslash}{new_filename}":

                            ## PRINT DEBUG MESSAGE
                            if debug:
                                print(f"\nOriginal: {og_filename}\n"
                                    f"Amended: {Directory}{backslash}{new_filename}")
                            
                            ## ADD TO AMEND COUNT
                            amend_count += 1

                        ## IF FILENAME WAS NOT CHANGED
                        else:
                            print(f"No Change: {Directory}{backslash}{file_list[file]}")

                        ## PRESENT TOTAL CHANGES
                        if file == file_count - 1:
                            if debug:
                                print(f"\nTotal Files: {file_count} | Amended: {amend_count}")
                            if Output == 'amend_count':
                                return amend_count

## FIND DIRECTORIES (ROOT == USER)
def root(Directory: str='user', debug: bool=False):
    if Directory == 'applications' or Directory == 'apps':
        if platform.system() == 'Darwin':
            if debug:
                print("/Applications")
            return "/Applications"
        if platform.system() == 'Windows':
            if debug:
                print("C:\Program Files")
            return "C:\Program Files"
    if Directory == 'desktop' or Directory == 'desk':
        if platform.system() == 'Darwin':
            if debug:
                print(f"{Path.home()}/Desktop")
            return f"{Path.home()}/Desktop"
        if platform.system() == 'Windows':
            if debug:
                print(f"{Path.home()}\Desktop")
            return f"{Path.home()}\Desktop"
    if Directory == 'documents' or Directory == 'docs':
        if platform.system() == 'Darwin':
            if debug:
                print(f"{Path.home()}/Documents")
            return f"{Path.home()}/Documents"
        if platform.system() == 'Windows':
            if debug:
                print(f"{Path.home()}\Documents")
            return f"{Path.home()}\Documents"
    if Directory == 'downloads' or Directory == 'dl':
        if platform.system() == 'Darwin':
            if debug:
                print(f"{Path.home()}/Downloads")
            return f"{Path.home()}/Downloads"
        if platform.system() == 'Windows':
            if debug:
                print(f"{Path.home()}\Downloads")
            return f"{Path.home()}\Downloads"
    if Directory == 'user':
        if debug:
            print(Path.home())
        return Path.home()
    if Directory == 'userlib':
        if platform.system() == 'Darwin':
            if debug:
                print(f"{Path.home()}/Library")
            return f"{Path.home()}/Library"
        if platform.system() == 'Windows':
            if debug:
                print(f"{Path.home()}\AppData")
            return f"{Path.home()}\AppData"
    if Directory == 'syslib':
        if platform.system() == 'Darwin':
            if debug:
                print("/Library")
            return "/Library"
        if platform.system() == 'Windows':
            if debug:
                print("C:\Windows\System32")
            return "C:\Windows\System32"

## SYSTEM COMMANDS
def system(Action: str='info', Print: bool=False):
    '''
    Action: ['app-', 'is-'], ['info', 'os', 'python']

    app-: commands for applications
    is-: system validation checks
    os: Returns Operating Sytem
    info: ['OS', 'Version', 'Processor']
    python: Python Version
    '''

    ## CONVERT INPUT TO LOWERCASE
    Action = Action.lower()

    ## RUN SYSTEM CHECK
    if 'is-' in Action:

        ## PARAMETERS
        os_ver = platform.platform().split('-')[0].lower()
        os_arch = platform.machine().lower()
        check = False

        ## IF NO FOLLOW UP COMMAND ENTERED
        if Action == 'is-':
            return print("\nn4s.fs.system('is-'):\n"
                        f"['is-mac', 'is-windows', 'is-arm']\n") 

        ## IF MACOS
        if Action == 'is-mac' and os_ver == 'macos':
            check = True

        ## IF WINDOWS
        if Action == 'is-windows' and os_ver == 'windows':
            check = True

        ## IF ARM PROCESSOR
        if Action == 'is-arm' and 'arm' in os_arch:
            check = True

        ## DETECT HIDDEN FILES
        if 'is-hidden' in Action:
            is_hidden = Action.split('-')[-1]
            import stat
            input(is_hidden)
            return bool(os.stat(is_hidden).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

        ## PRINT TO TERMINAL
        if Print:
            print(check)

        ## RETURN
        return check

    ## APPLICATIONS
    if 'app-' in Action:

        ## VERIFY COMPATIBILITY
        if not system('is-mac'):
            return print("\nn4s.fs.system('app-'):\n"
                        f"ONLY supports macOS at this moment!\n") 

        ## IF NO FOLLOW-UP COMMAND ENTERED
        if Action == 'app-':
            return print("\nn4s.fs.system('app-'):\n"
                        f"Enter an app's name or use 'app-list' to return a list of installed apps\n") 

        ## LIST OF ALL APPS
        app_list = []

        ## LIST OF SYSTEM/APPS
        sys_app_list = []

        ## LIST OF UTILITIES/APPS
        util_app_list = []

        ## LIST OF USER INSTALLED APPS
        user_app_list = []

        ## FILTER OUT THESE PHRASES
        filter_list = ['.app', 
                        '.DS_Store', 
                        '.localized', 
                        '.Karabiner-VirtualHIDDevice-Manager',
                        'Utilities']
        
        ## READ SYSTEM APPS
        for x in range(len(os.listdir('/System/Applications'))):
            app_list.append(strgs.filter_text(os.listdir('/System/Applications')[x], filter_list))
            sys_app_list.append(strgs.filter_text(os.listdir('/System/Applications')[x], filter_list))

        ## READ UTILITIES APPS
        for x in range(len(os.listdir('/System/Applications/Utilities'))):
            app_list.append(strgs.filter_text(os.listdir('/System/Applications/Utilities')[x], filter_list))
            util_app_list.append(strgs.filter_text(os.listdir('/System/Applications/Utilities')[x], filter_list))

        ## READ USER APPS
        for x in range(len(os.listdir('/Applications'))):
            app_list.append(strgs.filter_text(os.listdir('/Applications')[x], filter_list))
            user_app_list.append(strgs.filter_text(os.listdir('/Applications')[x], filter_list))
        
        ## SORT LISTS
        app_list.sort()
        sys_app_list.sort()
        util_app_list.sort()
        user_app_list.sort()

        ## FILTER OUT EMPTY SPACES
        app_list = list(filter(None, app_list))

        ## GET APP NAME FROM ACTION INPUT
        app_name = Action.split('-')[-1]

        ## LIST OF INSTALLED APPS
        if Action == 'app-list':
            if Print:
                print()
                for x in range(len(app_list)):
                    print(f"{app_list[x]}")
            return app_list

        ## APP...
        for x in range(len(app_list)):
            
            ## IF APP IS FOUND
            app_found = False

            ## LAUNCHER
            if Action == f"app-{str(app_list[x]).lower()}":

                ## PRINT: LAUNCHING APP...
                if Print:
                    print(f"Launching: {app_list[x]}...")
                
                ## LAUNCH SYSTEM APP
                if str(app_list[x]).lower() in str(sys_app_list).lower():
                    call(["/usr/bin/open", f"/System/Applications/{app_list[x]}.app"])
                    app_found = True
                    return

                ## LAUNCH UTILITIES APP
                if str(app_list[x]).lower() in str(util_app_list).lower():
                    call(["/usr/bin/open", f"/System/Applications/Utilities/{app_list[x]}.app"])
                    app_found = True
                    return

                ## LAUNCH USER INSTALLED APP
                if str(app_list[x]).lower() in str(user_app_list).lower():
                    call(["/usr/bin/open", f"/Applications/{app_list[x]}.app"])
                    app_found = True
                    return

            ## CHECK INSTALL
            if Action == f"app-{str(app_list[x]).lower()}-installed":

                ## LAUNCH SYSTEM APP
                if str(app_list[x]).lower() in str(sys_app_list).lower():
                    app_found = True

                ## LAUNCH UTILITIES APP
                if str(app_list[x]).lower() in str(util_app_list).lower():
                    app_found = True

                ## LAUNCH USER INSTALLED APP
                if str(app_list[x]).lower() in str(user_app_list).lower():
                    app_found = True
                
                ## PRINT: APP_FOUND VALUE
                if Print:
                    print(app_found)

                return app_found

        ## RETURN APP_FOUND VALUE
        if 'installed' in Action:

            ## PRINT: APP_FOUND VALUE
            if Print:
                print(app_found)

            ## RETURN
            return app_found

        ## RETURN APP NOT FOUND
        return print(f"App Not Found => " + strgs.clean_text(app_name, 'title'))

    ## SYSTEM INFO
    else:

        ## RETURNS OPERATING SYSTEM
        if Action == 'os':
            if Print:
                print(platform.platform().split('-')[0])
            return platform.platform().split('-')[0]

        ## RETURNS ['OS', 'OS-VERSION', 'PROCESSOR']
        if Action == 'info':

            ## GET INFO
            version = platform.platform()

            ## GET OS
            version_os = version.split('-')[0]

            ## GET OS VERSION
            version_num = version.split('-')[1].replace(f"{version_os}-", '')

            ## IF MACOS...
            if 'MACOS' in version.upper():

                ## GET PROCESSOR
                if 'ARM' in version.upper():
                    version_arch = 'arm64'
                else:
                    version_arch = 'Intel'

            ## IF WINDOWS...
            if 'WINDOWS' in version.upper():

                ## GET PROCESSOR
                version_arch = platform.machine()

            ## RETURN
            if Print:
                print([version_os, version_num, version_arch])
            return [version_os, version_num, version_arch]

        ## PYTHON COMMANDS
        if 'python' in Action:

            ## RETURNS PYTHON VERSION
            if Action == 'python':
                if Print:
                    print(platform.python_version())
                return platform.python_version()

            ## RESTART PYTHON APP
            if Action == 'python-restart':
                python = python_executable
                os.execl(python, python, * python_argv)

            ## EXIT PYTHON APP
            if Action == 'python-exit':
                python_exit()

        return print("\nn4s.fs.system():\n"
                    f"['app-', 'is-'], ['info', 'os', 'python']\n") 



## TESTS