import smtplib

gmail_user = 'gabimarkcovid19@gmail.com'
gmail_password = 'jojhnezmidlzggpq'

sent_from = gmail_user
to = ['anteprojic@gmail.com']
subject = 'Test'
body = 'Test vjezba 8 zadatak 2 Robert Nincevic'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
