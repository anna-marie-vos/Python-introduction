# Creating a webblocker
* windows / mac has host-files
* This is where you go to add redirects
* on windows the hosts file lives here: C:/windows/System32/drivers/etc
* on linux & mac the hosts file lives here: /etc/hosts
* when you declare varName = r"lots of \n " the r tells python that this is row string, and it ignores the \n as a newline
* It will add lines that block certain websites at a sertain time and remove it after the time is up.
* for windows pythonw.exe so change the extension of your python file to .pyw and not .py
* in linux: in the terminal type: `sudo crontab -e` and then select 2 (nano)
* then in the terminal type: `@reboot python3 /home/Workspace/Python-introduction/Tut7/web_blocker.py`
* then press ctrl+y and that should do it. 
