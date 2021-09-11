
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from stor import total
import schedule
import time

def main():
    username = "outlookmailid"
    password = "********"
    mail_from = "outlookmailid.com"
    mail_to = "outlookmailid"
    mail_cc = "outlookmailid"
    mail_subject = "Store Report"
    mail_body = """Dear Sir/Madam, 
    Please find the attachment"""
    mail_attachment = r"path"
    mail_attachment_name = "filename"
    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Cc'] = mail_cc
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    with open(mail_attachment, "rb") as attachment:
        mimefile = MIMEBase('application', 'octet-stream')
        mimefile.set_payload((attachment).read())
        encoders.encode_base64(mimefile)
        mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
        mimemsg.attach(mimefile)
        connection = smtplib.SMTP(host='smtp.office365.com', port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()



schedule.every().day.at("time").do(main)
main()
while 1:
    schedule.run_pending()
    time.sleep(1)