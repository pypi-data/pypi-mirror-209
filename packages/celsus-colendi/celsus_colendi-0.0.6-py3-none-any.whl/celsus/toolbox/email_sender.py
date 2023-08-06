from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib
import ssl
        
def email_sender(filepath_list, file_list, body, subject, sender, password, contacts):
    """
    It creates connection to mail and sending mail.

    Parameters
    ----------
    filepath_list : list
        list of the file path
    file_list : list
        list of the file name
    body : str
        body of the mail
    subject : str
        subject of the mail
    sender : str
        sender mail
    password : str
        sender password
    contacts : str
        contacts mail, # contacts should be separated with ", "
    """
    # mail paramaters
    text = ''
    # body of the mail
    subject = subject
    body = body
    # Create a multipart message and set headers
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = ", ".join(contacts)
    message["Subject"] = subject
    # message["Bcc"] = receiver_email
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    for index in range(len(filepath_list)):
        # Open PDF file in binary mode
        with open(filepath_list[index], "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition", f"attachment; filename= {file_list[index]}",)
    # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        if server.noop()[0] == 250:
            server.login(sender, password)
            server.sendmail(password, contacts, text)
            print("Report send by email succecfully")
        else:
            print("There is a STMP connection error.")
