##What Is This?
As stated above, this is a small script that aims to keep you up to date and informed with all of the generally useless information about today, via email, or sms if you use your carier's sms2txt service. It goes out into the internet and downloads, scrapes, or otherwise obtains information about all kinds of things like those crazy national holidays, historical events, and [The Word Of The Day](https://www.merriam-webster.com/word-of-the-day)
##How do I use it?
Simple. You'll need to download and install python, for whatever system you're running, then run this script from the terminal like:
python nationaldays.py
or, on unix systems:
python3.x nationaldays.py
###dependencies
Upon running this python script, you may have received an error regarding modules that were not found. Nationaldays uses some things you'll need to install with pip first. They are:
* [ics](https://pypi.org/project/ics/)
pip install ics
* and [requests](https://pypi.org/project/requests/)
pip install requests
* 
###Running At A Certain Time Of Day
You can run this program in one of two ways:
* Let the built-in timer send you trigger the email at 7:00 every morning, which would require you to keep a terminal open constantly. Also not recommended because the sleep function is not accurate and you'll receive the email a few seconds later each day.
* remove the timer, and run this script automatically with a linux cron job or Windows task scheduler.
##caveats
###Gmail error message when the script sendds mail
In order to get around this, you will need to [Go To The Google Accounts Page](https://accounts.google.com) and sign in with the account you're sending from. You should see a section in your main account overview that tells you to "Review Recent Account Activity" or "Take Security Checkup" or something of that sort. Essentially, you'll want to look around until yu find the setting called "Less Secure App Access."
It is not recommended that you disable this for your main account, as it is a security risk to do so. I would create an alternate Gmail just for this, and any future, less secure scripts you would like to use.
###Can't keep a terminal Open all the time
If you can't or don't want to keep a terminal open all the time, here are your options.
* as stated above, you can remove the time function and run this script automatically via your OS's scheduler
* if you don't know how to do that, you can run the program like so:
pythonw nationaldays.py
or on unix systems:
pythonw3.x nationaldays.py
This will invoke pythonw, a gui version of python. But, as this script has no gui, it will not require your terminal be open. You can then close it, and after that you just have to make sure your computer doesn't shut down. 
This is really more of a program for a server and not a pc, but you can run it on either.
###Additional Questions
[Contact Me](mailto:quantomrush34@icloud.com)