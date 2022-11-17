import smtplib

my_email = "booogiemonster@gmail.com"
password = 'wjbbkqpifdfqxqnj'


def send_email(bday_list, subject='Happy Birthday!'):
    email = f"Subject: {subject}\n\n" \
            f"{bday_list[2]}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=bday_list[1], msg=email)
