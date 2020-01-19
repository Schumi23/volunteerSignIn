The point of this program is to provide a simple sign in for SOPO Bike Co-op, a bicycle collective in Atlanta Georgia. 
We wanted something simple that runs on a Raspberry Pi, that simply requires someone to type in their name, and stores people entering when. 
The ability to add another field relatively simply (for example "Volunteer", "manager", etc.) is potentially desired.

Dependancies: 
This software requires python3, tkinter, and datetime. All should be included in python by default.
Note: It is coded to run in python3 - if you want to use python2 you will have to change tkinter to Tkinter

You need to create a file called data.csv containing "name, purpose, time" (if you want the columns to have a header. 
You can make this by opening a basic text document (notepad, textedit, etc.) typing the above in it, and saving it as a .csv file (or as data.csv with filetype set to "all files")