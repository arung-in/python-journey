python --version

#Activate Environment
python -m venv myenv
myenv\Scripts\Activate

#After activation, you should see something like:
(myenv) D:\Github\python-journey> 

#if activation failed then follow this
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#to see the installed packages use this 
python -m pip list

#To run the Day1.py file just put in cmd
python Day1.py