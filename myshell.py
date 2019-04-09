#!/usr/bin/env python3

# Student Name: Gerard Slowey
# Student Number: 17349433

# importing our neccessary modules
import os, sys, subprocess
from cmd import Cmd

# from itertools import izip

# A colours class consisting of escape commands to make the terminal stand out more
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

        # initiate custom shell variables
        self.originDirectory = os.getcwd()
        os.environ['SHELL'] = str(self.originDirectory) + "/myshell"
        os.environ['PWD'] = str(os.getcwd()) 

    # 1(i)
    # A function that changes the current default director to <directory>
    # Directory initiated to default value of empty string
    def cd(self, directory = ""):
        
        # If the <directory> argument is not present, the current directory is returned
        if directory == "" or directory == ".":
            return
        
        # Changes the current directory to <directory> and updates the PWD environment variable.
        try:
            os.chdir(directory)
            
            # this command also changes the PWD environment variable
            newDir = os.getcwd()
            os.environ['PWD'] = newDir

        # if the directory given does not exist an appropriate error is reported.
        except:
            directoryWarning = colours.FAIL + "cd: " + directory + ": No such directory exists" + colours.END
            print(directoryWarning)

    # 1(ii)
    def clr(self):
        # Clears the screen
        print("\033c", end ="")


    
    # 1(iii)
    # A function to list the contents of a specified directory.
    def dir(self, directory):
        try:
            itemCount = len([name for name in os.listdir(directory)])

            # if the directory contains items, print them out one by one
            
            if itemCount > 0:
                for item in os.listdir(directory):
                    print(item)
            else:
                # otherwise print a blank line to represent an empty directory
                print("")

        # else display an appropriate error message
        except:
            accessWarning = colours.WARNING + "dir: cannot access '" + directory + "': No such file or directory"
            print(accessWarning)

    def redirection_dir(self, args, symbol, filename):
        if not args:
            args = "."
            content = "-----------------\n"
        for line in os.listdir(args):
         content += line + "\n"
        content += "-----------------"
        if ">" == symbol:
         with open(filename, 'w+') as f:
             f.write(content)
        else:
         with open(filename, 'a+') as f:
             f.write("\n" + content)



    # 1(iv)
    # A function to list all of the environment strings.
    def environ(self):
        environment = os.environ
        for item in environment:
            print(item + " = " + environment[item])

    def redirection_environ(self, symbol, filename):
        environ = os.environ
        content = ""
        for k,v in environ.items():
            content += k + "=" + v + "\n"
        if ">" == symbol:
            with open(filename, 'w+') as f:
                f.write(content)
        else:
            with open(filename, 'a+') as f:
                f.write("\n" + content)
    


    # 1(v)   
    # A function to display user input on the terminal followed by a new line
    def echo(self, input):
        if len(input) > 0:
            print(input + "\n")
        else:
            print("error: 'cd' no input provided")


    def redirection_echo(self, args, symbol, filename):
        content = args.rstrip()
        if ">" == symbol:
            with open(filename, 'w+') as f:
                f.write(content)
        else:
            with open(filename, 'a+') as f:
                f.write("\n" + content)



    # 1(vi)
    # A function that displays the user manual using the more command
    def help(self):
        os.system("more readme")

    def redirection_help(self, symbol, filename):
        f = open("readme", "r")
        if f.mode == "r":
            content = f.read()
        if ">" == symbol:
            with open(filename, 'w+') as f:
                f.write(content)
        else:
            with open(filename, 'a+') as f:
                f.write("\n" + content)



    # 1(vi)
    # A function that pauses the shell
    def pause(self):
        try:
            waiting = input("Shell Operation Paused - Press Enter to resume")
            if not waiting:
                raise ValueError("Execution Resumed")
        except ValueError as e:
            print(e)


    # 1(vii)
    # A function that exits the shell
    def quit(self):
        print("Goodbye For Now")
        exit()

    # Creates a new subprocess with specified environment variables
    def childProcess(self, args):
        try:
            pid = os.fork()
            if pid > 0:
                wpid = os.waitpid(pid, 0)
            else:
                subprocess.call([args[0], args[1]]) 
        except:
            print(colours.WARNING + "Process Creation Error" + colours.END)



    def redirection(self, command, filename):
    #main overwrite that will deal with dir, environ, echo & help
        try:
         if "dir" == command[0]:
            #redirection(command, sign, filename)
            redirection_dir("".join(command[1:-1]),command[-1],filename)
         elif "environ" == command[0]:
            #redirection(sign, filename)
            redirection_environ(command[-1], filename)
         elif "echo" == command[0]:
            #redirection(command, sign, filename)
            redirection_echo(" ".join(command[1:-1]),command[-1],filename)
         elif "help" == command[0]:
            #redirection(sign, filename)
            line = redirection_help(command[-1], filename)
         else:
            print("Output redirectionion unavailable for *" + " ".join(command[:-1]) + "*")
        except:
            print("Error while trying to execute" + command)


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
            print(colours.WARNING + "Cannot access '" + file + "': No such file exists" + colours.END)
        

    # Checks user input for commands, otherwsie
    def run(self, command):
        try:
            if len(command) > 2 and (">" == command[-2] or ">>" == command[-2]):
                redirection(command[:-1], command[-1])
            
            elif "&" == command[-1]:
                try:
                    subprocess.Popen(command[:-1])
                    return
                except:
                    print("Command Error, execution failed")

            elif command[0] == "cd":
                if len(command) > 2:
                    print("error: 'cd' only accepts one directory parameter")
                else:
                    self.cd(command[1])
            
            elif command[0] == "clr":
                if len(command) > 1:
                    # appropriate error handling if a paramter is supplied with the clr command
                    print("error: 'clr' does not take a parameter")
                else:
                    self.clr()
            
            elif command[0] == "dir":
                if len(command) > 1:
                    self.dir(command[1])
                else:
                    self.dir(".")
            
            elif command[0] == "environ":
                self.environ()
            
            elif command[0] == "echo":
                # multiple spaces/tabs are reduced to a `ngle space.
                self.echo(" ".join(command[1:]))
            
            elif command[0] == "help":
                self.help()
            
            elif command[0] == "pause":
                self.pause()
            
            elif command[0] == "quit" or command[0] == "q":
                self.quit()
            
            else:
                # All other command line input is interpreted as program invocation
                # Gets done by shell forking and executing the programs as its own child processes.
                self.childProcess(command[:])
        
        except EOFError as e:
            print("Error while trying to execute" + command)
        
# Main function
def main(argv):
    
    # get the user name
    user = str(os.environ['USER'])

    # this function gets executed when executing from a supplied batch file
    if len(argv) == 2:
        filename = argv[1]

        # invoke the read method to execute batchfile commands
        myshell().read(filename)

        # when the end of file is reached the shell exits and displays this message
        print("Exiting My Shell. Goodbye now")
    
    else:
        # display a welcome message the user when they open the shell first
        print("Hello " + user + ", type 'help' to display a list of commands.")
        while True:
            entry = input(colours.GREEN + colours.BOLD + os.environ['PWD'] + colours.END + "$ ")
            if len(entry) != 0:
                # invoke the run method
                myshell().run(entry.split())


if __name__ == '__main__':
    main(sys.argv)
