# This program implements a basic shell with the following commands:
# 1. exit
	# - terminates the shell
# 2. commands without arguments: 
	# - executes a command without arguments and waits for 
	# it to complete
# 2a. ls -a, -h, and -l
	# - list all files, including hidden ones, long listing 
	# format, human-readable file sizes
# 2b. mkdir
	# - create a directory
# 2c. cd (directory)
	# - change to a named directory or the home directory if
	# no argument is provided
# 2d. pwd
	# - print the current directory
# 2e. cp (file1, file2)
	# - copy file1 to file2
# 2f. mv (file1, file2)
	# - move or rename file1 to file2
# 2g. rm -r
	# - recursively delete a directory
# 2h. cat (file)
	# - display contents of a file
# 2i. head -n
	# - display the first n lines of a file
# 2j. tail -n
	# - display the last n lines of a file
# 2k. grep ('pattern', file)
	# - search for a pattern in a file
# 2l. wc -l, -w
	# - count the lines or words in a file
# 2m. chmod (xxx)
	# - change file permissions
# 3. command with arguments
	# - parses command-line arguments and executes the command
# 4. background execution
	# - executes a command without blocking, allowing the shell to
	# accept further input immediately
# 5. output redirection
	# - redirects the output to a specified file
# 6. input redirection
	# - takes input from a file instead of the user's input
# 7. piping commands
	# - passes the output of one command as input to another
	# command

import sys

def exit():
    '''
    Exit the shell.

    Exits the shell with a status of N. If N is omitted, the exit status 
    is that of the last command executed
    '''

def ls(argc, argv[]):
    '''
    Usage: ls [OPTION]... [FILE]...
    List information about FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all                 do not ignore entries starting with .
      -h, --human-readable      with -l, print sizes linke 1K 234M 2G etc.
      -l                        use a long listing format
          --help        display this help and exit

    Exit status:
      0  if OK,
      1  if minor problems (e.g., cannot access subdirectory),
      2  if serious trouble (e.g., cannot access command-line argument).
    '''

def mkdir():
    '''
    Usage: mkdir [OPTION]... DIRECTORY...
    Create the DIRECTORY(ies), if they do not already exist.

    Mandatory arguments to long options are mandatory for short options too.
          --help        display this help and exit
    '''

def cd(dir):
    '''
    Change the shell working directory.

    Change the current directory to DIR. The default DIR is the value of the
    HOME shell variable. If DIR is "-", it is converted to $OLDPWD.

    The variable CDPATH defines the search path for the directory containing
    DIR. Alternative directory names in CDPATH are separated by a colon (:).
    A null directory name is the same as the current directory. If DIR begins
    with a slash (/), then CDPATH is not used.

    If the directory is not found, and the shell option 'cdable_vars' is set,
    the word is assumed to be a variable name. If that variable has a value,
    its value is used for DIR.

    Exit Status:
    Returns 0 if the directory is changed; non-zero otherwise.
    '''

def pwd():
    '''
    Print the name of the current working directory.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read
    '''

def cp(file1, file2):
    '''
    Copy SOURCE to DEST.

          --help        display this help and exit
    '''
def mv(file1, file2):
    '''
    Rename SOURCE to DEST

          --help        display this help and exit
    '''

def rm():
    '''
    Usage: rm [OPTION]... [FILE]...
    Remove (unlink) the FILE(s).

      -r, -R, --recursive   remove directories and their contents recursively
              --help    display this help and exit

    By default, rm does not remove directories. Use the --recursive (-r or -R)
    option to remove each listed directory, too, along with all of its contents.

    To remove a file whose name starts with a '-', for example '-foo',
    use one of these commands:
        rm -- -foo
        rm ./-foo
    '''

def cat(file):
    '''
    Usage: cat [FILE]...

    Example:
        cat f - g   Output f's contents, t hen standard input, then g's contents.
        cat         Copy standard input to standard output.
    '''

def head():
    '''
    Usage: head [OPTION]... [FILE]...
    Print the first 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.

    With no FILE, or when FILE is -, read standard input.

    Mandatory arguments to long options are mandatory for short options too.
        -n, --lines=[-]NUM      print the first NUM lines instead of the first 10;
                                with the leading '-', print all but the last
                                NUM lines of each file

    NUM may have a multiplier suffix:
    b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
    GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y, R, Q.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.
    '''

def tail():
    '''
    Usage: tail [OPTION]... [FILE]...
    Print the last 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.
    
    Mandatory arguments to long options are mandatory for short options too.
        -n, --lines=[+]NUM      output the last NUM lines, instead of the last 10;
                                or use -n +NUM to skip NUM-1 lines at the start
    NUM may have a multiplier suffix:
    b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
    GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y, R, Q.
    Binary prefixes can be used, too: KiB=K, MiB=M, and so on.
    '''

def grep():
    '''
    Usage: grep PATTERNS [FILE]...
    Search for PATTERNS in each FILE.
    Example: grep 'hello world' menu.h main.c
    PATTERNS can contain multiple patterns separated by newlines.

    When FILE is '-', read standard input. With no FILE, read '.' if
    recursive, '-' otherwise.
    Exit status is 0 if any line is selected, 1 otherwise;
    if any error occurs, the exit status is 2.
    '''

def wc():
    '''
    Usage: wc [OPTION]... [FILE]...
      or:  wc [OPTION]... --files0-from=F
    Print newline, word, and byte counts for each FILE, and a total line if
    more than one FILE is specified. A word is a non-zero-length sequence of
    printable characters delimited by a white space.

    With no FILE, or when FILE is -, read standard input.

    The options below may be used to select which counts are printed, always in
    the following order: newline, word, character, byte, maximum line length.
        -l, --lines             print the newline counts
            --files0-from=F     read input from the files specified by
                                NUL-terminated names in file F;
                                If F is - then read names from standard input
        -w, --words             print the word counts
            --total=WHEN        when to print a line with total counts;
                                When can be: auto, always, only, never
            --help      display this help and exit
    '''

def chmod():
    '''
    Usage: chmod OCTAL-MODE FILE...
    Change the mode of each FILE to MODE.
    '''

import os
import socket   
username = os.getlogin()
computer_name = socket.gethostname()
cwd = os.getcwd()
print(username, "@", computer_name, ":",  cwd, "$", sys.argv[0])
argc = len(sys.argv)
input()