#!/usr/bin/env python3

# importing the modules we use in myshell
import os, sys, subprocess

# A colours class consisting of escape sequences to make the terminal stand out more
class colours:      
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class myshell:

    def __init__(self):
        # Requirement 1(ix)
        # the shell environment contains the full path for the shell executable
        os.environ['SHELL'] = str(os.getcwd()) + "/myshell"

    # Requirement 1(i)
    # A function that changes the current default directory to <directory>
    def cd(self, directory):
        try:
            # change the current directory to the <directory> supplied
            os.chdir(directory)
            
            # also update the PWD environment variable
            os.environ['PWD'] = os.getcwd()

        # if the directory given does not exist an appropriate error is reported
        except FileNotFoundError:
            directoryWarning = colours.FAIL + "cd: '" + directory + "': No such directory exists" + colours.END
            print(directoryWarning)

    # Requirement 1(ii)
    # A function to clear the terminal of text
    def clr(self):
        # prints an escape command to clear the terminal
        print("\033c", end ="")

    # Requirement 1(iii)
    # A function to list the contents of a specified directory
    def dir(self, directory):
        try:
        # try getting the number of items in a directory
            itemCount = len([name for name in os.listdir(directory)])

            # if the directory contains items, print them out one by one
            if itemCount > 0:
                for item in os.listdir(directory):
                    print(item)
            else:
                # otherwise print a blank line to represent an empty directory
                print("")

        # else display an appropriate error message if the directory does not exist
        except FileNotFoundError:
            accessWarning = colours.WARNING + "dir: cannot access '" + directory + "': No such file or directory"
            print(accessWarning)

    # Requirement 1(iv)
    # A function to list all of the environment strings.
    def environ(self):
        environment = os.environ
        # print each environmental string, one per line
        for item in environment:
            # print format is name = value
            print(item + " = " + environment[item])

    # Requirement 1(v)   
    # A function to display user input on the terminal followed by a new line
    def echo(self, input):
        # if input is supplied to echo
        if len(input) > 0:
            # print the input out, followed by a newline
            print(input + "\n")
        else:
            # display an error message, indicating no input was provided
            print(colours.FAIL + "'echo': cannot display message: no input provided" + colours.END)

    # Requirement 1(vi)
    # A function that displays the user manual using the more command
    def help(self):
        # use a system call to display the readme file
        os.system("more readme")

    # Requirement 1(vii)
    # A function that pauses the shell
    def pause(self):
        # use the input() function to pause the shell
        try:
            waiting = input("Shell Operation Paused - Press Enter to resume")
            # if the enter button is pressed, resume execution
            if not waiting:
                raise ValueError("Execution Resumed")
        except ValueError as e:
            print(e)

    # Requirement 1(viii)
    # A function that exits the shell
    def quit(self):
        # print a goodbye message
        print("Goodbye For Now, Exiting")
        # raises a system exit
        exit()

##########################################################################################
# Main command checker function

    # Checks user input for commands and symbols and directs what action to take next
    def run(self, command):
        try:
        # check for i/o redirection commands
            if len(command) > 2 and (command[-2] == ">" or command[-2] == ">>"):
                instructions = command[:-1]
                file = command[-1]
                self.redirect(instructions, file)
            
        # check for background execution commands
            elif command[-1] == "&":
                try:
                    p = subprocess.Popen(command[:-1])
                    p.wait()
                except:
                    print("Command Error, execution failed")

        # otherwise just check for normal execution commands with error handling 
            elif command[0] == "cd":
                if len(command) == 2:
                    self.cd(command[1])
                elif len(command) > 2:
                    # inform the user they have used the cd command wrong
                    print(colours.WARNING + "error: 'cd' only accepts one directory parameter" + colours.END)
                else:
                    # if the <directory> argument is not present, the current directory is returned
                    self.cd(".")

            elif command[0] == "clr":
                if len(command) > 1:
                    # appropriate error handling if a parameter is supplied with the clr command
                    print(colours.WARNING + "error: 'clr' does not take a parameter" + colours.END)
                else:
                    self.clr()
            
            elif command[0] == "dir":
                if len(command) == 2:
                    self.dir(command[1])
                elif len(command) == 1:
                    self.dir(".")
                else:
                    print(colours.WARNING + "error: 'dir': only accepts one directory parameter" + colours.END)
            
            elif command[0] == "environ":
                if len(command) > 1:
                    print(colours.WARNING + "error: 'environ' does not take a parameter" + colours.END)
                else:
                    self.environ()
            
            elif command[0] == "echo":
                # multiple spaces/tabs are reduced to a single space.
                self.echo(" ".join(command[1:]))
            
            elif command[0] == "help":
                if len(command) > 1:
                    print(colours.WARNING + "error: 'help' does not take a parameter" + colours.END)
                else:
                    self.help()
            
            elif command[0] == "pause":
                if len(command) > 1:
                    print(colours.WARNING + "error: 'pause' does not take a parameter" + colours.END)
                else:
                    self.pause()
            
            elif command[0] == "quit" or command[0] == "q":
                self.quit()
            
            # All other command line input is interpreted as program invocation
            # Gets done by shell forking and executing the programs as its own child processes
            else:
                self.childProcess(command[:])
        
        except EOFError as e:
            print(colours.WARNING + "Error while trying to execute" + command + colours.END)
        
########################################################################################
# Multiprocessing Functions

    # Creates a subprocess to execute the given programme
    def childProcess(self, args):
        try:
            # e.g. python3 test.py
            subprocess.run([args[0], args[1]]) 
        except:
            print(colours.WARNING + "Process Creation Error" + colours.END)

########################################################################################
# IO Redirection Functions

    # a main redirect function that calls other smaller redirect functions (dir, environ, echo & help)
    def redirect(self, command, file):
        try:
            # here we first match our commands
            if command[0] == "dir":
                # if a directory is supplied
                if len(command) > 2:
                    directory = command[1]
                    symbol = command[-1]
                    self.dir_redirect(directory, symbol, file)
                else:
                    # otherwise just use the current directory
                    directory = "."
                    symbol = command[-1]
                    self.dir_redirect(directory, symbol, file)

            elif command[0] == "environ":
                # if a parameter is supplied in error, display a message
                if len(command) > 2:
                    print(colours.WARNING + "error: 'environ' command does not take parameters" + colours.END)
                else:
                    # execute as normal
                    symbol = command[-1]
                    self.environ_redirect(symbol, file)

            elif command[0] == "echo":
                # if no echo message is supplied
                if len(command) == 2:
                    print(colours.WARNING + "error: 'echo' no text entered to redirect" + colours.END)
                else:
                    # continue as normal
                    text = command[1:-1]
                    symbol = command[-1]
                    self.echo_redirect(" ".join(text), symbol, file)

            elif command[0] == "help":
                # if a parameter is supplied with the help command
                if len(command) > 2:
                    print(colours.WARNING + "error: 'help' command does not take parameters" + colours.END)
                else:
                    # otherwise continue as normal
                    symbol = command[-1]
                    line = self.help_redirect(symbol, file)

            else:
                # inform the user the command they want to use is not applicable to i/o redirection
                print(colours.WARNING + "Error: I/O redirection unavailable for '" + " ".join(command[:-1]) + "'" + colours.END)
        
        except:
            # handle exceptions by displaying an execution error
            print(colours.WARNING + "Execution error for " + command + colours.END)

    def echo_redirect(self, args, symbol, file):
        data = args.rstrip()
        # we strip of any unneccessary whitespace from the inputted arguments

        # if we use the overwrite symbol(>)
        if ">" == symbol:
            # we overwrite data in the file with new data given on the command line
            self.overwrite(file, data)
                
        # else if we use the append symbol (>>)
        else:
            # we append the new data to the data already pre-existent in the file.
            self.append(file, data)

    def help_redirect(self, symbol, file):
        try:
            # first open the readme file in read mode
            f = open("readme", "r")
            # read the contents of readme into the variable data
            data = f.read()

            # if we use the overwrite symbol(>)
            if ">" == symbol:
                # overwrite the data in the file with our new data
                self.overwrite(file, data)

            # else if we use the append symbol (>>)
            else:
                # we append the new data to the data already pre-existent in the file.
                self.append(file, data)
            
            # finally close the readme file as we are finished with it
            f.close()

        except FileNotFoundError:
            accessWarning = colours.WARNING + "readme cannot be accessed: file missing"
            print(accessWarning)

    def environ_redirect(self, symbol, file):
        # make referencing the environment variables easier
        environment = os.environ
        variables = ""
        for item in environment:
            # add each item to the variables variable
            variables += ((item + " = " + environment[item]) + "\n")
        
        # overwrite
        if ">" == symbol:
            # overwrite the file contents
            self.overwrite(file, variables)

        # else append
        else:
            # we append the new data to the data already pre-existent in the file.
            self.append(file, variables)

    def dir_redirect(self, directory, symbol, file):
        # if no arguments have been supplied
        if not directory:
            # take the directory as the directory where we are currently located
            directory = "."

        try:
            data = ""
            for line in os.listdir(directory):
                data += line + "\n"
            
            # overwrite the data
            if ">" == symbol:
                self.overwrite(file, data)

            # else append
            else:
                self.append(file, data)

        except FileNotFoundError:
            accessWarning = colours.WARNING + "dir: cannot access '" + directory + "': No such file or directory"
            print(accessWarning)

########################################################################################
# Data Manipulation Functions

    # An overwriting command
    def overwrite(self, file, data):
        with open(file, 'w+') as f:
            f.write(data + "\n")
            f.write("---------------------------------\n")

    # An append command
    def append(self, file, data):
        with open(file, 'a+') as f:
            f.write(data + "\n")
            f.write("---------------------------------\n")

    # Enables the shell to take its command line input from a file.
    # e.g myshell batchfile
    # the batchfiles commands are executed
    def read(self, file):
        try:
            for line in open(file, "r"):
                print(" ")
                print(line.rstrip())
                print("-" * len(line))
                self.run(line.split())
        except:
            # if the file supplied cannot be accessed display a failure message to the user
            accessWarning = colours.WARNING + "Cannot access '" + file + "': No such file exists" + colours.END
            print(accessWarning)

########################################################################################
# Main function
def main(argv):
    
    # get the user name
    user = str(os.environ['USER'])

    # if the shell is invoked with a batchfile
    if len(argv) == 2:
        # the file name is the arg at position 1
        file = argv[1]

        # invoke the read method to execute batchfile commands
        myshell().read(file)

        # when the end of file is reached the shell exits and displays this message
        print("Exiting My Shell. Goodbye now")
    
    else:
        # display a welcome message the user when they open the shell first
        print("Hello " + user + ", type 'help' to display the manual.")
        
        # an infinite loop to allow the user to enter commands until they call quit()
        while True:
            
            # a command to display the current working directory to the user
            entry = input(colours.GREEN + colours.BOLD + os.environ['PWD'] + colours.END + "$ ")
            
            # if there is a command is entered
            if len(entry) != 0:
                # invoke the run method
                myshell().run(entry.split())

if __name__ == '__main__':
    main(sys.argv)
