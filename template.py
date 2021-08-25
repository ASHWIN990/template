#!/usr/bin/env python3

# Importing required libraries
import argparse
import os
import shutil
import sys
import stat

# Color codes
black_col = "\u001b[30;1m"
red_col = "\u001b[31;1m"
green_col = "\u001b[32;1m"
yellow_col = "\u001b[33;1m"
blue_col = "\u001b[34;1m"
magenta_col = "\u001b[35;1m"
cyan_col = "\u001b[36;1m"
white_col = "\u001b[37;1m"
reset_col = "\u001b[0m"


def CHECK_AVAILABLE_TEMPLATES():
    TEMPLATE_DIR = "/usr/share/template_maker"

    if not os.path.isdir(TEMPLATE_DIR):
        print(
            f"{red_col}Error{yellow_col} : (Exiting) {reset_col}Template directory not found{reset_col}")
        sys.exit(1)

    FILES = {}
    AVAILABLE_TEMPLATE = {}
    AVAILABLE_FILETYPES = []

    for file in os.listdir(TEMPLATE_DIR):
        full_dir_path = (f"{TEMPLATE_DIR}/{file}")
        tmp_filen = file.split("-")
        AVAILABLE_FILETYPES.append(tmp_filen[0].lower())
        AVAILABLE_TEMPLATE.update({tmp_filen[0].lower(): tmp_filen[1]})
        FILES.update({tmp_filen[0].lower(): full_dir_path})

    return AVAILABLE_FILETYPES, AVAILABLE_TEMPLATE, FILES


def LIST_AVAILABLE_TEMPLATES(AVAILABLE_TEMPLATE):
    print("Available Templates are:- \n")
    print("{:<10} {:<10}".format(f"{green_col}Language{reset_col}",
          f"{magenta_col}  File Name{reset_col}"))
    print("--------------------")
    for i in AVAILABLE_TEMPLATE:
        print("{:<10} {:<10}".format(i, AVAILABLE_TEMPLATE[i]))


def MAKE_FILE(AVAILABLE_TEMPLATE, FILES, ARG_FILETYPE, IS_FILENAME_GIVEN, FILENAME_BY_USER, IS_EXECUTABLE_GIVEN):
    PWD = os.getcwd()

    SRC_FILE = FILES.get(ARG_FILETYPE)
    FILE_NAME = AVAILABLE_TEMPLATE.get(ARG_FILETYPE)

    if IS_FILENAME_GIVEN:
        FILE_NAME = FILENAME_BY_USER

    DES_FILE = (f"{PWD}/{FILE_NAME}")

    if os.path.isfile(DES_FILE):
        _opt = input(
            f"{yellow_col}WARNING{reset_col} : '{FILE_NAME}' exist, Press (Y/y) to overwrite : ")
        if _opt.lower() != "y":
            sys.exit(0)

    try:
        shutil.copyfile(SRC_FILE, DES_FILE)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        sys.exit(1)

    if IS_EXECUTABLE_GIVEN:
        PERMS = os.stat(DES_FILE)
        os.chmod(DES_FILE, PERMS.st_mode | stat.S_IEXEC)


def main():
    parser = argparse.ArgumentParser(
        description=f"Template maker, Written by : {blue_col}ASHWINI SAHU{reset_col}")

    parser.add_argument("-f", metavar="FILE TYPE", required=False,
                        help="Provide the Template type",     type=str)
    parser.add_argument("-n", metavar="FILE NAME", required=False,
                        help="Provide the desired File name", type=str)
    parser.add_argument("-x", action="store_true",
                        required=False, help="Make the new file executable")
    parser.add_argument("-l", action="store_true",
                        required=False, help="List the available Templates")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    AVAILABLE_FILETYPES, AVAILABLE_TEMPLATE, FILES = CHECK_AVAILABLE_TEMPLATES()

    # SOME FLAGS TO CHECK
    IS_FILENAME_GIVEN = False
    FILENAME_BY_USER = ""
    IS_EXECUTABLE_GIVEN = False

    if args.l:
        LIST_AVAILABLE_TEMPLATES(AVAILABLE_TEMPLATE)
        sys.exit(0)

    if args.f:
        ARG_FILETYPE = (args.f).lower()
        if ARG_FILETYPE not in AVAILABLE_FILETYPES:
            print(
                f"{red_col}Error{yellow_col} : (Exiting) {reset_col}Unknown File Type{reset_col}\n")
            parser.print_help()
            sys.exit(1)

    if args.n:
        IS_FILENAME_GIVEN = True
        FILENAME_BY_USER = args.n

    if args.x:
        IS_EXECUTABLE_GIVEN = True

    MAKE_FILE(AVAILABLE_TEMPLATE, FILES, ARG_FILETYPE,
              IS_FILENAME_GIVEN, FILENAME_BY_USER, IS_EXECUTABLE_GIVEN)


if __name__ == "__main__":
    main()
    print(f"{green_col}SUCCESS{reset_col}")
