======================
myshell - User Manual 
======================

-> Hello and welcome to the user manual for myshell.
-> myshell is a custom built Linux shell implemented through the python language, specifically Python 3. 
-> myshell offers to you, the beginner Linux user the most common commands as executed by Linux users every day. 
-> The shell accepts multiple different commands as explained later in this manual. 
-> The myshell file is designed to be run in any Linux environment on the command line (the terminal)

*************************
Manual Layout explained:
*************************

    - Whenever you see text displayed between hash tags (#):
        This indicates some executable code snippet.

    - Text between asterisks (*):
        This indicates an important point that you should read carefully to fully understand what's going on.

-> Happy Reading!

-----------------------
▶ Section A. Operation
-----------------------

1. Initial Setup and Running the shell
---------------------------------------

**************************
Getting your system ready
**************************

First let's look at getting myshell up and running:
- You will need the Linux operating system to run the myshell file.
- MacOS is based of Linux, so it will run the file natively.
- Microsoft Windows does not natively support the Linux operating system so it has to be downloaded externally.
- There are many different distributions of Linux, I recommend using Ubuntu however as it is user friendly and free.
    ○ It is available to download at: 
        https://www.ubuntu.com/download/desktop
    ○ Guide to installing: 
        https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/

- When you have your Linux operating system running save the myshell file to the 'home' directory.
    ○ this saves confusion at this step.

- In your Linux application folder you should find a programme called 'Terminal'.
    ○ Click on the icon to launch the terminal.

- Next enter the following command verbatim or copy and paste it into the terminal:

    ############################
        python3 myshell.py    
    ############################

- This command executes the custom shell, so we can use it and experiment with it.

- If you are successful in starting the shell, you should be greeted with a welcome message such as:
    ○ "Hello 'your name', type 'help' to display the manual."

    ○ We will also see another line below the welcome message displayed in green:
        ○ This shows us the path to the directory we are currently in (from where the shell was executed).
        ○ It will look something like this:
            /home/username/folder_name/folder_name
        ○ If you don't fully understand this don't worry, it will be further described in the sections below.

- If you do not see the messages above, you have gone wrong somewhere in the process, check through the steps again.

*********************************
Submitting Commands to the shell
*********************************
    - The shell gives us space to type our commands after the directory path highlighted in green text.
    - When we have typed the command we want to execute, we then hit the 'enter' key to submit.
    - The shell then executes the command and returns the result.
    - Congratulations you are one step closer to becoming a Linux master!


-----------------------
▶ Section B. Commands:
-----------------------
Next, let's focus on what myshell can be used for:

-------------------------------
1. Changing the file directory
-------------------------------
Directories is the term used in Linux to refer to storage folders for files.
- Usually the type of file is stored in the directory related to the name, this is not a strict rule however.
- Folder and directory will be used interchangeably here.

The Linux Directory Structure, explained.
- Coming from Windows the Linux file system can seem a bit strange.
- The C:\ drive is now gone, and these are replaced by a '/'.

/ : The Root Directory
- Every other directory in your Linux system is located under the '/' directory, known as the root directory.
- The root directory is similar to the C:\ drive in windows in a simplified view.

- Some default directories we will focus on, including a template directory path:
    ○ home              /home
    ○ Documents         /home/user_name/Documents
    ○ Downloads         /home/user_name/Downloads
    ○ Music             /home/user_name/Music
    ○ Pictures          /home/user_name/Pictures
    ○ Videos            /home/user_name/Videos

- As mentioned above the shell displays the directory we are currently located, in green.
- If we the user want to switch between the directories from our shell, we type the following command:

    ########################
        cd 'directory'     
    ########################

- This command changes the current directory to the directory specified in between the quotes.

*************************************
Subdirectories and Super directories
*************************************

There are two options for browsing directories in Linux:
A) To return to the parent folder of the current folder.
    e.g. to go from      /home/user/Documents/New   to   /home/user/Documents
    (Documents contains the 'New' folder)

- Enter the following command:

    ##################
        cd ..      
    ##################

- This is a shortcut command which is very handy to remember.


B) To navigate to a folder within the directory you are in:
    e.g. to go from      /home/user/Documents   to   /home/user/Documents/New
    (The 'New' folder is contained within 'Documents')

- Enter the following command:

    #########################
        cd 'folder_name'    
    #########################

- Where 'folder_name' is the name of the folder we want to access.
- If we want to access a pre-defined path to a directory we enter the above command replacing 'folder_name' with the required path.

***********
Side Note:
***********

    ############
        cd .        
    ############

'.' refers to the current directory in Linux.

- If we type 'cd .' in our shell, it will have no real noticeable effect as we will remain in the current directory.


-----------------------------
2. Clearing the shell screen
-----------------------------
We use the clear function if we want to clear the shell of text from previously executed commands.

- To clear the screen, we type in our shell:

    ###############
        clr           
    ###############

WARNING: You will lose all previous commands you have entered.


---------------------------------------
3. Listing the contents of a directory
---------------------------------------
If we want to see what files are contained in a directory, we enter:

    ######################
        dir 'directory'  
    #######################

*********************
- To view what the current directory stores, enter 'dir', but leave the directory blank.
*********************

Example:
- If we are in the 'Documents' Directory and we want to view the files in the 'Downloads' directory 
    - We enter the path of the Downloads folder, usually it will look something like this.
        
    ####################################
        dir /home/user_name/Downloads
    ####################################

- The dir command can be used with I/O redirection, as explained below.

-----------------------------------
4. Listing all environment strings
-----------------------------------
To print all environment variables, we enter:

    ###############
        environ       
    ###############

- We do not need to be in any specific directory to see environment variables.
- As a beginner Linux user, most of the environment variables will make no sense to you.
- However, if we look closely we can see what actually is being displayed.
    USERNAME - displays the name of the user currently logged in.
    PWD - displays the current directory the the user is working from.
    HOME - displays the home folder for your specific system.
    SHELL - this stores the location from where the myshell file was originally executed from.

- It's unlikely a beginner Linux user will ever use the environment variables, they are however useful for reference.
- The environ command can be used with I/O redirection, as explained below.

-----------------------------------------
5. Displaying a custom comment on screen
-----------------------------------------
If you want to have a little fun with the shell and want to display a comment on screen you can use the echo command.

    #####################
        echo 'comment'
    #####################

- The echo command can be used with I/O redirection, as explained below.

------------------------------
6. Opening the command manual
------------------------------
If you want reminding of what a particular function does, enter:

    ##############
        help
    ##############

- This command displays this manual within the shell without having to exit the command line environment.
- The help command can be used with I/O redirection, as explained below.

---------------------
7. Pausing the shell
---------------------
If you want to pause shell operation, you can enter the pause command:

    #############
        pause
    #############

- It's handy when you want to go make a cup of coffee, but you aren't finished with the shell.
- Any keyboard input will just be ignored by the shell when it is paused.
- To resume the shell, we just hit the enter key.


---------------------
8. Quitting the shell
---------------------
When you are finished using the shell you can enter the following command to kill the shell:

    ###########
        quit
    ###########

- However, if you are lazy like me and don't like typing you can simply enter the letter q and it will perform the same action.
- This suspends the shell and returns to the Linux command line.


----------------------------------------
9. Running a file from the command line
----------------------------------------
If you want to run your own file from the myshell screen you can do so by entering the following command in myshell:

    ################################
        python3 'python_file'.py
    ################################

- Here you replace 'python_file' with the name of your python file.
- This will allow you to run your own python file as part of the myshell environment.

**********************
Background execution:
**********************
A special feature of myshell is the ability to run a programme in the background:

- If you want to run a file, but you want it to execute in the background, just simply place an ampersand '&' symbol at the end of your command.
- myshell will recognise that you want to run the programme in the background and will just return the result of your programme output when it finishes.

- Up until this point we were executing commands in the foreground.
- Usually when you launch a programme in foreground execution it takes over the terminal, stopping you from doing other work in the meantime.

- Background execution can be useful for running programmes that take a long time to complete.
- Basically, the programme is pushed to the background and may continue to run as long as the terminal window is open.


------------------------------------------------
10. Executing a set of commands from a batchfile
------------------------------------------------
- A batchfile is just a file containing a set of commands you want to execute.
- The commands you can put into the file must be some of the files in the above document.

Building the batchfile:
    - You can use a text editor to build your batchfile.
    - Each line of the batchfile must contain one and only one command.

    E.g.
        echo Hello
        dir
        cd

- You can then save the file with any desired name such as 'batch' or 'commands.txt'
- The .txt extension is not required, but can be included if you want.

**************************
To execute the batchfile:
**************************
- You must quit myshell and return to the Linux command line.
Reminder: to do this simply enter 'q'

- Then simply type as before:

    #######################################
       python3 myshell.py batchfile_name  
    #######################################

- This is known as invoking the shell with a command line argument.

- myshell will recognise that you have supplied a batchfile to execute from.
- When the commands have been executed, the result will be displayed on screen and myshell will exit.

--------------------
11. I/O redirection
--------------------
I/O redirection gives the user a shortcut to storing programme execution output to files.

    E.g. 
    To get the contents of a direction we enter the previously seen command: 

    ##########
        dir   
    ##########

However, if we want to store this command result to a file for later reference we extend our command to make use of I/O redirection:

    #######################
       dir > store_file   
    #######################
- Notice here, we use the '>' symbol to indicate to the system that we want to store the output to the file 'store_file'.
- If we open this file in a text editor we will see the directory contents listed one item per line.

*****************************************
There are two options in I/O redirection:
*****************************************

    A. Overwrite (>)
    ###############################
        echo hello > outputfile   
    ###############################
- This command will store the text hello to the outputfile
- The overwrite symbol (>) allows the user to replace the data in the output file with new data produced by the executed command.

    B. Append (>>)
    ########################################
        python3 echo hello >> outputfile   
    ########################################
- The append symbol used (>>) allows the user to append data produced from the executed command to any data already present in the outputfile while not overwriting it.
    
I/O redirection can be used with the following commands:
- dir
- environ
- echo
- help

**********************************
Don't worry if you have forgotten to create the outputfile that will be written to, myshell will do this automatically for you.
**********************************


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Overall, do not be afraid to adventure with the shell's functionality.
If something goes wrong the error message will give you a good insight to what you have done wrong and how you can fix it.
If you are still confused however, read the section of this manual related to the error you are having.

Finally, thanks for your time and hope you enjoyed myshell :)
