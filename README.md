# CS330-PROJECT-FINISHED
Javier Alejandro Nova Estrella
This has been tested on Windows using Python.
For the first part I have an unlocking(232361) and locking(232364) code that will lock or unlock the security device, this works by input from the
keyboard a six-digits code for unlock/lock and to exit out the program, when you input the code is gonna tell you the operation, and digits only
from 0-9. And the second part, is just using a fixed code with the last digit being random. Is very straight forward only follow the steps of the program.
I have to different files for each program.
To run this project, you must create an executable first. These are the steps for creating and run the executable:
1- To start, you may want to add Python to Windows path.An easy way to add Python to the path is by downloading 
a recent version of Python, and then checking the box to ‘Add Python to PATH’ at the beginning of the installation.
2- After you install python or if you already have python then, open the Windows Command Prompt, and then 
type the following command to install the PyInstaller package: pip install pyinstaller.
3- git clone the repository in your desired location.
4-Now you’ll be able to create the executable of the Python script using PyInstaller.Simply go to the Command Prompt, and then type:
cd followed by the location where your Python script is stored. For example: cd C:\Users\Javier Nova\Desktop\CS330-PROJECT-FINISHED then press enter.
(after you typed the location where the Python script is stored on your computer).
5-Then, refer to the following template to create the executable:
pyinstaller --onefile pythonScriptName.py 
*pyinstaller --onefile Solution.py(without *)
6-Your executable will be created at the location that you specified. Go the location of the repository, you’ll notice that few 
additional files were created at that location.To find the executable file, open the dist folder. You’ll then see the executable file. Just double click 
on the file and should open.
7-Repeat step 5/6 to create an executable for the second archive named Solution2
*pyinstaller --onefile Solution2.py(without *)
#If you want to create the executable follow the steps from above, but after install any version of Python(step 1) you can just run the program 
from CMD on windows, just typing from your derised location
"python nameofthefile.py" example: python Solution2.py 

