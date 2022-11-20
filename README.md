# CS330-PROJECT-FINISHED
This has been tested on Windows.
For the first part I have an unlocking(232361) and locking(232364) code that will lock or unlock the security device,
and the second part, is just using a fixed code with the last digit being random. Is very straight forward only follow the steps of the program.
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
*Example: pyinstaller --onefile Solution.py
6-Your executable will be created at the location that you specified. Go the location of the repository, you’ll notice that few 
additional files were created at that location.To find the executable file, open the dist folder. You’ll then see the executable file. Just double click 
on the file and should open.
 
