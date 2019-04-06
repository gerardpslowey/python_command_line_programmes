myshell - User Manual Page
============================

-> Hello and welcome to the user manual for myshell.
-> myshell is a custom built linux shell implemented through the python language, specifically Python 3. 
-> myshell offers to you, the beginner linux user the most common commands as executed by linux users everyday. 
-> The shell accepts multiple different commands as explained later in this manual. 
-> The myshell file is designed to be run in any linux environment on the command line (the terminal)
-> Happy Reading!

-----------------------
▶ Section A. Operation
-----------------------

1. Initial Setup and Running the shell
---------------------------------------

++++++++++++++++++++++++++
Getting your system ready
++++++++++++++++++++++++++

First lets take a look at getting myshell up and running:
- You will need a linux operating system to run the myshell file.

- MacOs is based of linux so it will run the file natively.
- Microsoft Windows does not natively support the linux operating system so it has to be downloaded externally.
- There are many different distributions of linux, I recommend using Ubunut, it is user friendly and free.
	○ It is available to download at: https://www.ubuntu.com/download/desktop
	○ Guide to installing: https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/

- When you have your linux operating system running save the myshell file to the 'home' directory.
	○ this saves confusion at this step.

- In your linux application folder you should find a programme called 'Terminal'.
	○ Click on the icon to launch the terminal.

- Next type the following command verbatim or copy and paste it into the terminal (excluded the hashes):

		############################
		#	 python3 myshell.py    #
		############################

- This command executes the custom shell so we can use it and experiment with it.

- If you are successful in starting the shell, you should be greated with a welcome message such as:
	○ "Hello 'your name', type 'help' to display a list of commands."

	○ We will also see another line below the welcome message displayed in green:
		○ This shows us the path to the directory we are currently in (from where the shell was executed).
		○ Its will look something like this:
			/home/username/folder_name/folder_name
		○ This will be further described in the sections below.

- If you do not see the messages above, you have gone wrong somewhere in the process, check through the steps again.

+++++++++++++++++++++++++++++++++
Submitting Commands to the shell
+++++++++++++++++++++++++++++++++

- The shell gives us space to type our commands after the directory path highlighted in green text.
- When we have typed the command we want to execute we then hit the 'enter' key to submit.
- The shell then executes the command and returns the result.
- Congratulations you are one step closer to becoming a linux master!

-----------------------
-----------------------
▶ Section B. Commands:
-----------------------
-----------------------

Next, lets focus on what myshell can be used for:

-------------------------------
1. Changing the file directory
-------------------------------
- Directories is the term used in linux to refer to storage folders for files.
- Usually the type of file is stored in the directory related to the name, this is not a strict rule however.

The Linux Directory Structure, explained.
- Coming from Windows the Linux file system can seem a bit strange.
- The C:\ drive are now gone and these are replaced by a '/' and funny sounding directory names.

/ : The Root Directory
- Every other directory in your linux system is located under the '/' directory, known as the root directory.
- The root directory is similar to the C:\ drive in windows in a simplified view.

- Some default directories we will focus on including a templete directory path:
	○ home				/home
	○ Documents			/home/user_name/Documents
	○ Downloads			/home/user_name/Downloads
	○ Music				/home/user_name/Music
	○ Pictures			/home/user_name/Pictures
	○ Videos			/home/user_name/Videos

- As mentioned above the shell displays the directory we are currently located, in green.

- This helps us keep track of what directory we are in.

- If we the user want to switch between the directories from our shell, we type the following command:

		############################
		#		cd 'directory' 	   #
		############################

- This command chages the current directory to the directory specified in between the quotes.

************************************
Subdirectories and Superdirectories
************************************

There are two options for browsing directories in linux.

- To return to the parent folder of the current folder.
	e.g to go from 		/home/user/Documents/New   to   /home/user/Documents
	(Documents contains the 'New' folder)

- Enter the following command:

		##########################
		#			cd .. 		 #
		##########################

- Otherwise to navigate to a folder within the directory you are in:
	e.g to go from 		/home/user/Documents   to   /home/user/Documents/New
	(The 'New' folder is contained within 'Documents')

- Enter the following command:

		#########################
		#    cd 'folder_name'  	#
		#########################

- Where 'folder_name' is the name of the folder we want to access.

- If we want to access a pre-definded path to a directory we enter the above command replacing 'folder_name' with the required path.

~~~~~~~~~~~
Side Note:

		##########################
		#	        cd .		 #
		##########################

'.' refers to the current directory in linux.

If we type 'cd .' in our shell, it will have no real noticable effect as we will remain in the current directory.


-----------------------------
2. Clearing the shell screen
-----------------------------
We use the clear function if we want want to clear the shell of text from previously executed commands.

To clear the screen we type in our shell:

		###########################
		#			clr			  #
		###########################

WARNING: You will loose all previous commands you have entered.


---------------------------------------
3. Listing the contents of a directory
---------------------------------------
If we want to see what files are contained in a directory we enter:

		##########################
		#	  dir 'directory'	 #
		##########################

To simply view what the current directory stores enter 'dir' followed by no directory.

However if we are in the 'Documents' Directory and we want to view the files in the 'Downloads' directory for example, 
	- We enter the path of the Downloads folder, usually it will look something like this.
		/home/user/Downloads


-----------------------------------
4. Listing all environment strings
-----------------------------------
To print all environment variables we enter:

		#######################
		#		environ		  #
		#######################

- We do not need to be in any specific directory to see environment variables.
- As a beginner linux user, most of the environment vriables will make no sense to you.
- However, if we look closely we can see what actually is being displayed.
	USERNAME - displays the name of the user currently logged in.
	PWD - displays the current directory tht the user is working from.
	HOME - displays the home folder for your specific system.
	SHELL - this stores the loaction of where the myshell file was originally executed from.

Its unlikely a beginner linux user will ever use the environment variables, they are however useful for reference.


-----------------------------------------
5. Displaying a custom comment on screen
-----------------------------------------
If you want to have a little fun with the shell and want to disply a comment on screen you can use the echo command.

		#######################
		#  echo 'comment'     #
		#######################

The comment entered can be any length and contain any characters you want.


------------------------------
6. Opening the command manual
------------------------------
If you want reminding of what a particular function does enter:

		#####################
		#		help    	#
		#####################

This displays a selection of avaialble commands and a short explanation.

---------------------
7. Pausing the shell
---------------------
If you want to pause shell operation the pause command can be used:

		#####################
		#      pause		#
		#####################

It's handy when you want to go  a cup of tea but you arn't finished with the shell.
Any keyboard input will just be ignored by the shell when it is paused.
To resume the shell we just hit the enter key.


---------------------
8. Quiting the shell
---------------------
When you are finished using the shell you can enter the following command to kill the shell:

		######################
		#       quit  	  	 #
		######################

However, if you are lazy like me and don't like typing you can simply enter q and it will perform the same action.
This suspends the shell and returns to the normal linux command line.


----------------------------------------
9. Running a file from the command line
----------------------------------------


------------------------------------------------
10. Executing a set of commands from a batchfile
------------------------------------------------
A batchfile is just a file containing a set of commands you want to execute.
The commands you can put into the file must be some of the files in the above document.

Building the batchfile:
	Each line of the batchfile must contain one and only one command.

	E.g.
	echo Hello
	dir
	cd

You can then save the file with any desired name such as batch or commands.txt
The .txt extension is not required, but can be included if you want.


--------------------
11. I/O redirection
--------------------

