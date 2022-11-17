import smtplib
import datetime as dt
import random

my_email = "booogiemonster@gmail.com"
password = 'wjbbkqpifdfqxqnj'
FRIDAY = 4

with open('./quotes.txt', 'r')as file:
    quotes = file.read().split('\n')

day = dt.datetime.now().weekday()
if day == FRIDAY:
    subject = "Have a Great Day!"
    message = quotes[random.randint(0, len(quotes)-1)]
    email = f"Subject: {subject}\n\n" \
            f"{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='andrewdhadlock@gmail.com', msg=email)


