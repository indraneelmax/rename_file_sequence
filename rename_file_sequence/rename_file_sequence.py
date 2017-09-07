#!/usr/bin/python
import os
import argparse
import re
from itertools import groupby


__input_dir = ""
__mock = False
__pad = 2
__verbose = False

def filter_files(file_list):
    """
    Apply our regex to split file name into tokens to identify sequence
    :param file_list: list of files
    :return: list of files names split into tokens
    """
    items = []
    regex = r"([a-z]*)(\d{0,})(.*)\.(.+)"

    for file_name in file_list:
        for item in re.findall(regex, file_name):
            items.append(item)
    return items


def rename_file(file_data, seq_numb, pad):
    """
    Renames the files detected as part of a sequence in a seq incremental order

    :param file_data: list of tuples containing file name split by regex
    :param seq_numb: list of detected integers in file name for a detected sequence
    :param pad: padding to be used for detected sequence

    """
    if __pad > pad:
        # Always keep min_pad for renamed sequence
        pad = __pad

    sort_seq_numb = sorted(seq_numb, key=lambda z: int(z))
    for index, value in enumerate(sort_seq_numb):
        seq = str(index+1).zfill(pad)
        old_name = "{}{}.{}".format(file_data[index][0], sort_seq_numb[index], file_data[index][-1])
        new_name = "{}{}.{}".format(file_data[0][0], seq, file_data[0][-1])

        if not __mock:
            # This should ideally always succeed for file names with a valid format
            try:
                os.rename(os.path.join(__input_dir, old_name), os.path.join(__input_dir, new_name))
                if __verbose:
                    print "Renamed {}  -->  {}".format(old_name, new_name)
            except OSError:
                print "{}{}{}.{} file is not valid format, will not rename".format(*file_data[index])
        else:
            if os.path.exists(os.path.join(__input_dir, old_name)):
                print "Will rename {}  -->  {}".format(old_name, new_name)
            else:
                print "{}{}{}.{} file is not valid format, will not rename".format(*file_data[index])


def group_and_rename_files(item_list):
    """
    Groups the file data with respect to 1st and last value
    i.e groups them by name and extension

    item_list = [('garvit', '14', '', 'jpg')
                  ('garvit', '1', '', 'jpg')
                  ('neel', '06', '', 'jpg')
                  ('neel', '02', '', 'jpg')]

    :param item_list: list of file name split into items as per regex

    """

    # Sort list by 1st(i.e. name) and last(i.e ext) value
    # Group by using 1st and last value as key
    for key, group in groupby(sorted(item_list, key=lambda z: (z[0], z[-1])), lambda x: (x[0], x[-1])):
        pad = 1
        file_data = []
        seq_numb = []
        for data in group:
            if pad < len(data[1]):
                pad = len(data[1]) # Find min padding
            seq_numb.append(data[1])
            file_data.append(data)
        rename_file(file_data,seq_numb, pad)


def find_files(input_dir):
    """
    Find files in the input_dir

    :param input_dir: path to the input dir
    :return: list of files in dir
    """
    file_list = []
    for dir_path, dir_names, file_name in os.walk(input_dir):
        file_list.extend(file_name)
        # break, don't look at sub-dir
        break
    return file_list


def get_args(args):
    """
    Process and return script arguments
    :param args: input arguments list
    :return:
        (argparse.Namespace): arguments
    """
    parser = argparse.ArgumentParser(description='''Given a directory identifies a sequence of files
        based on file name and extension, and renames them sequentially keeping the same order!
        Sample usage: rename_file_sequence.py /path/to/directory
        ''')
    parser.add_argument("input_dir", nargs='?', default=os.getcwd(),
                        help="Path to input directory containing files")
    parser.add_argument("--pad", nargs='?', type=int, default=2,
                        help="minimum padding for digits in renamed sequence, default is 2")
    parser.add_argument("--mock", action='store_true', default=False,
                        help="mock mode, do not rename")
    parser.add_argument("--verbose", action='store_true', default=False,
                        help="verbose mode")
    args = parser.parse_args(args)
    if not os.path.isdir(args.input_dir):
        raise IOError("{} is not a directory".format(args.input_dir))
    return args


def run(args):
    """
    Main starting point

    :param input_dir: Directory to look for files (top level only)
    :param pad: minimum padding for digits in renamed sequence, default is 2
    :param mock: mock mode, do not rename files
    :param verbose: verbose mode
    :return:
    """
    args = get_args(args)
    global __input_dir, __mock, __verbose, __pad
    __input_dir = args.input_dir
    __mock = args.mock
    __verbose = args.verbose
    __pad = args.pad
    print "Looking at Input directory: {}".format(args.input_dir)
    all_files = find_files(args.input_dir)
    file_items = filter_files(all_files)
    group_and_rename_files(file_items)