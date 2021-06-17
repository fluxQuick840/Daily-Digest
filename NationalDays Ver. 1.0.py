#NationalDays.py, a script to send you the nationally celebrated holidays of the current day... at seven in the morning every day
import ics
import requests
import smtplib, ssl
from email.message import EmailMessage
import datetime 
from time import sleep


#defining the function used to acquire today's national holidays from https://www.checkiday.com
def national_days():
    url = "https://www.checkiday.com/ical.php"
#instantiating an ics.calendar class and telling it where to read the calendar from
    c = ics.Calendar(requests.get(url, allow_redirects=True).text) 
    e = list(c.timeline) #a list of events
    holidays = """ """
#This calendar lists all events for a good week or so, so we'll need to loop through the list and find the ones that started today
    for i in range(0, len(e)):
        f = list(c.timeline)[i]
        readable = "Event '{}' started {}".format(f.name, f.begin.humanize()) #returns a more easily interpretable string of event details
        if "hours" in readable: #if an event string contains hours, as in started 7 hours ago, 
            if (readable[-12].isdigit()): #filtering out hours strings that start x hours from now
                readable = readable.split("'") #splitting every part of the string except for the event name away
                holidays += f"{readable[1]}, \n" #appending the name to our holidays string from earlier
    return holidays

#now defining an email function
def send(holidays):
    date = datetime.datetime.now() #for the email subject
    port = 465 #for logging into the smtp server
    smtp_server = "smtp.gmail.com"
    message = EmailMessage() #instantiating an emailMessage class
    message.set_content(holidays) #the body of the message
    sender = "email@gmail.com"
    to = "email@vzwpix.com" #note: you can use email to sms here but certain cellular companies limit your message to 160 chars
    password = "password" #to log into the gmail server
    message["From"] = sender #from header
    message["To"] = to #to header
    message["Subject"] = f"Holidays celebrated on {date.strftime('%B %d')} are:" #subject header
#start a connection to the server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, to, message.as_string()) #converting our emailMessage object to a string

def main():
#get the current time and store it in a variable labeled now
    now = datetime.datetime.now()
#convert this to seconds
    sec_list = [3600, 60, 1]
    now_secs = sum([a*b for a,b in zip(sec_list, [now.hour, now.minute, now.second])])
    send_secs = 25200 #the number of seconds between midnight and seven A.M.
#subtract now from send 
    wait_secs = send_secs - now_secs
    if wait_secs < 0:
        wait_secs += 86400
    print(f"Waiting {wait_secs} seconds until 7:00 A.M.")
    sleep(wait_secs)
    while True:
        nationalDays = national_days()
        send(nationalDays)
        sleep(86400) #wait 24 hours


main()