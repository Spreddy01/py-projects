import smtplib

from email.mime.text import MIMEText  

from email.mime.multipart import MIMEMultipart

#here comes your mail id 
sender_email = "your_email@gmail.com"
#here comes your password 
password = "your_password"

#here comes the reciever info 
sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
subject = "Hello from python email automation"
body = "This is an automated email sent using Python."

#google smtp
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()
