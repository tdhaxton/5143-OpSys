## Shell Project - Implementation of a Basic Shell

#### Due: TBD

**Parts Due Dates**: TBD

### Group Members:
- Tim Haxton
- Harika Vemulapalli
- Cooper Wolf

## Overview

In this project, we will implement a basic "shell". A shell is a command-line interface we often interact with, and provides an powerful interface with your system. Below is an overview of the actions our shell will perform:

1. Print a prompt(`$: `) to the user.
2. Read a command line from stdin.
3. Tokenize (lexically analyze) the command a create an array of command parts (tokens).
4. Parse the token array to identify the command and its arguments.
5. Execute the command:
    - If necessary, create a child process via `fork()`.
    - The child process receives an additional input (arguments) and executes the appropriate command.

## Requirements

- **Language**: Python
- **Threads (Optional)**:
    - Use threads to execute commands.
    - If no background execution (`&`), wait for the thread to complete before returning control to the shell.
- **Command Features**:
    - Each command returns a string.
    - Commands can accept input from other commands.

Our shell will support the following command types:

### 1. **Exit Command**

- **Command**: `exit`
- **Description**: Terminates the shell.
- **Concepts**: Exiting the shell with system calls like exit().

### 2. **Command without Arguments**

- **Example**: `ls`
- **Description**: Executes a command without arguments and waits for it to complete.
- **Concepts**: Synchronous execution, process forking.

### 3. **Command with Arguments**

- **Example**: `ls -l`
- **Description**: Parses command-line arguments and executes the command.
- **Concepts**: Command-line paramaters.

### 4. **Background Execution (`&`)**

- **Example** `ls &`
- **Description**: Executes a command without blocking, allowing the shell to accept further input immediately.
- **Concepts**: Background execution, signals, asynchronous execution.

### 5. **Output Redirection**

- **Example**: `ls > output.txt`
- **Description**: Redirects the command output to a specified file.
- **Concepts**: File operations, output redirection.

### 6. **Input Redirection**

- **Example**: `sort < inputfile.txt`
- **Description**: Takes input from a file instead of the user’s input.
- **Concepts**: File operations, input redirection.

### 7. **Piping Commands**

- **Example**: `ls -l | more`
- **Description**: Passes the output of one command as input to another command.
- **Concepts**: Pipes, synchronous operations.

## Instructions:
Clone the repository.
install requests if not already done
    - pip install requests
Run the `shell.py` file and use the following commands...

## Commands:
| Command               | Description                                         | Author   |
|-----------------------|-----------------------------------------------------|----------|
| `ls`                  | List files and directories                          | Cooper   |
| `pwd`                 | Print working directory                             | Cooper   |
| `ls -a`               | List all files, including hidden ones.              | Cooper   |
| `ls -l`               | Long listing format.                                | Cooper   |
| `ls -h`               | Human-readable file sizes.                          | Cooper   |
| `mkdir`               | Create a directory.                                 | Cooper   |
| `cd directory`        | Change to a named directory.                        | Cooper   |
| `cd`                  | Change to the home directory if no argument given.  | Cooper   |
| `cp file1 file2`      | Copy file1 to file2.                                |          |
| `mv file1 file2`      | Move or rename file1 to file2.                      |          |
| `rm -r`               | Recursively delete a directory.                     |          |
| `cat file`            | Display contents of a file.                         |          |
| `head -n`             | Display the first n lines of a file.                |          |
| `tail -n`             | Display the last n lines of a file.                 |          |
| `grep 'pattern' file` | Search for a pattern in a file.                     |          |
| `wc -l`               | Count lines in a file.                              |          |
| `wc -w`               | Count words in a file.                              |          |
| `chmod xxx`           | Change file permissions.                            |          |
| `history`             | Show previously used commands.                      | Cooper   |
| `!x`                  | Re-run command number *x* from history.             | Cooper   |
| `exit`                | Exits the shell.                                    | Cooper   |
| `up & down arrows`    | Navigate previous command                           | Cooper   |
| `left & right arrows` | Move cursor                                         | Cooper   |
| `more`                |                                                     |          |
| `less`                |                                                     |          |
| `[program] > file`    |                                                     |          |
| `[program] < file`    |                                                     |          |
| `hfind`               |                                                     |          |
| `piping`              |                                                     |          |

### Help

- Every command will print help information if the user passes `--help` as an argument.

## Non-Working Components:
cp
mv
rm
cat
head
tail
grep
wc
chmod
more
less
"<"
">"
hfind
commands with piping


## References:
- [geeksforgeeks](https://www.geeksforgeeks.org/python/executing-shell-commands-with-python/)
- [ChatGPT](https://chatgpt.com/)
- [Python Docs](https://docs.python.org/3/library/os.html)