The point of this program is to provide a simple sign in for SOPO Bike Co-op, a bicycle collective in Atlanta Georgia. 
We wanted something simple that runs on a Raspberry Pi, that simply requires someone to type in their name, and stores people entering when. 
The ability to add another field relatively simply (for example "Volunteer", "manager", etc.) is potentially desired.

Dependancies: 
This software requires python3, tkinter, datetime, and pandas. All but pandas should be included in python by default.

You need to create a file called data.csv containing "0, name, purpose, time" (if you want the columns to have a header. 
You can make this by opening a basic text document (notepad, textedit, etc.) typing the above in it, and saving it as a .csv file (or as data.csv with filetype set to "all files")