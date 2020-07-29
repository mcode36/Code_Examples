'''
without pygame installed, if you run the command "import pygame", python will
show errors:
    ModuleNotFoundError: No module named 'pygame'

Below are the instructions to install pygame (with virtualenv)
1. Open DOS command window
2. change directory to project folder

# step 3 is required only when virtualenv is not installed
3. run "pip install virtualenv"

4. run "virtualenv venv"
5. run "venv\scripts\activate.bat"
6. run "pip install pygame"

To start python IDLE with venv activated:
1. change directory to project folder
2. venv\scripts\activate.bat
3. python -m idlelib.idle your_program.py

'''


import pygame