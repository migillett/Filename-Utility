#!/usr/bin/env python3

import os

search_folder = '/Volumes/Genesis'

invalid_chars = '"'


def main(folder):

    counter = 0

    os.chdir(folder)
    print('Changed directory to:', folder)

    print('Beginning search...')
    for root, dirs, files in os.walk('.', topdown=False):
        for file in files:
            if invalid_chars in file:
                print('Invalid Character detected in filename:', os.path.join(root, file))
                counter += 1

    print('Search complete. Total errors:', counter)


if __name__ == '__main__':
    main(search_folder)
