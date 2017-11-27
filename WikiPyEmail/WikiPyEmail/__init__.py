import pypandoc
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

def send_email(url, email_addresses):
    pypandoc.convert('content/' + url + '.md', 'pdf', outputfile="wiki/web/PDF/" + url + ".pdf",
                 extra_args=['-V', 'geometry:margin=1.5cm'])
    username = 'updatewpy@gmail.com'
    password = 'pass1pass1234'
    to = 'arnzent1@mymail.nku.edu'

    to = email_addresses
    if "," in to:
        ' ,'.join("'{0}'".format(x) for x in to)

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = "[" + to + "]"
    message['Subject'] = url.capitalize()
    body = "Email sent from wikiPy."

    body_send = MIMEText(body, 'plain')
    message.attach(body_send)
    filename = "wiki/web/PDF/" + url + ".pdf"

    element = MIMEBase('application', "octet-stream")
    element.set_payload(open(filename, "rb").read())
    encoders.encode_base64(element)
    element.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
    message.attach(element)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, to, message.as_string())
    server.close()
    return True
