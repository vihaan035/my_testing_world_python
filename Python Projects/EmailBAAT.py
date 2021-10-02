import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'vihaangupta035@gmail.com'
email_password = 'onlysecret@123'
email_send = 'rajeshgpec@gmail.com'

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = 'vihaangupta035@gmail.com'
msg['To'] = 'rajeshgpec@gmail.com'
msg['Subject'] = "This email was sent using Vihaan's email bot"

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='filename'
attachment=open('maths_test.txt','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
