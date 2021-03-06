#!/usr/bin/env python3

# Written by Michael Gillett, 2020
# This program is designed to go through a directory and search for files with filenames with invalid characters
# Written as a utility to figure out why our server kept throwing errors when backing up over samba

import os

invalid_chars = ['"', '\\']
# more common invalid chars:
# invalid_chars = [ '"', '?', '!', ';', ':', '%', '*', '#']


def main():
    errors = 0
    corrected = 0
    file_count = 0
    folder = str(input('Folder to analyze:'))

    while True:
        rename = str(input('Do you want this program to rename files for you? (Y/N):'))
        if rename.upper() == 'Y':
            rename = True
            break
        elif rename.upper() == 'N':
            rename = False
            break
        else:
            input('Please select Y or N. Press enter to continue.')

    os.chdir(folder)
    print('Changed directory to:', folder)

    print('Beginning search...\n')
    for root, dirs, files in os.walk('.', topdown=False):
        for file in files:
            for char in invalid_chars:
                if char in file:
                    old_name = os.path.join(root, file)
                    print('Invalid Character detected in filename:', old_name)

                    errors += 1

                    # only runs if rename == True
                    if rename:
                        # deletes invalid char
                        new_name = os.path.join(root, file.replace(char, ''))

                        # gets rid of double spaces (separate from above)
                        # just in case invalid chars don't have spaces around them
                        new_name = new_name.replace('  ', ' ')

                        try:
                            os.rename(old_name, new_name)
                        except FileExistsError:
                            print('File already exists. Skipping.')
                            continue
                        except FileNotFoundError:
                            print('Warning: file not found. Could have been renamed in a previous loop.',
                                  'Please run program again.')
                            continue

                        print('New filename:', new_name)
                        corrected += 1
        file_count += 1

    print('''
    Search complete.
    Total files checked: {0}
    Total errors: {1}
    Total corrected: {2}
    '''.format(file_count, errors, corrected))


if __name__ == '__main__':          
    main()
