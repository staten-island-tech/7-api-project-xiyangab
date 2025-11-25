This article assumes you are on windows 10 and using Python 3.10 from the Microsoft Store

Begin in the terminal typing the following.
```
python3 -m venv app  
```
This should have created a folder called "app" with a virtual environment. VSCode will ask you if you want to activate the environment. If you are unable to activate the environment then type the following depneding on your terminal environment.

If Powershell, first change directory in the terminal to use the app folder (or whatver your project is called)
```
cd app
```
then activate
```
Scripts\Activate.ps1
```
If command prompt (CMD), first change directory in the terminal to use the app folder (or whatver your project is called)
```
cd app
```
then activate
```
Scripts/activate.bat
```
Be sure to copy and create a .gitignore file for your directory to not commit unnecessary files

We can also look at the bottom right of VSCode and change the interpreter path.

# Installing Requests 

```
pip install requests
```

Pip allows us to install outside packages for our apps. 
Ensure that after installing and importing in your .py file that there are no underlines indicating the package is not found. If it is not found you are not active in the virtual env. 

# Running the file
You will now likely need to use 
``` cmd 
python app.py
```

in order to run the file. Keep in mind the location of the file relative to your terminal

following might be needed.
```
cd ../
```