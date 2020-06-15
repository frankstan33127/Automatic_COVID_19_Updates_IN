# Automatic_COVID_19_Updates_IN

An automatic COVID-19 update tool which can be used to get information about COVID-19(for India). The program is made to provide the user with the number of COVID-19 cases(inactive, active and death cases) of India. This uses some basic web scraping from a website. Although, the original script is made to get updates of COVID-19 in India, it can be modified to get updates for your desired country by modifying the source code. The program is update live and therefore you must re-open to see the updates. 

Compatability:

This was made in a Linux OS and the files except for the python script will only run in linux. For windows users you should be able to click the python script and it should work. 

NOTE:
To make the desktop entry file work, make sure to open it in a text editor and change the language as .desktop and also go to properties of the file and make it executable (can also be done with chmod command). And make the python script executable too, if you want it to run on click.
The modules requests, beautifulsoup4, python3, tkinter, etc are require to run this. Also the icon won't work by default. To make it work, open the desktop entry in a text editor and edit the path of the Icon path attribute to the png/svg(toxic and toxic2 both work.
Icon=/home/$USER/CoronaUpdates/toxic.png, here change the '$USER' to the name of your username.

Installation :

Installation should be as simple as cloning this repo or downloading it. Once done, open the folder Automatic_COVID_19_Updates_IN and either run the CoronaUpdates.sh or CoronaUpdates[IN] which is a desktop entry to open the program. You can even open the python script from the terminal.

WARNING : Some websites may not allow web scraping and could even be illegal. Please check the website's policies/get their permission before attempting to scape information from their website. I am not to be held responsible if you get in trouble. 

This is python was script made using basic python modules such as requests, beautifulsoup, tkinter, etc. This was made in python3 and runs in python3. 

Credits : Icon : Icon made by Freepik from www.flaticon.com
          Awesome web scraping tutorial which helped me a lot : https://www.youtube.com/watch?v=MX33Yoa-EvE
          And thank you for the so many stack-overflow legends!
