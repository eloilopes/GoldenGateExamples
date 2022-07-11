 ##############################################################################################
 #                                                                                            #
 #        I'M NOT THE AUTHOR OF THIS SCRIPT ALL THE CREDITS TO Cody Brinkman                 #
 #                                                                                            #
 ##############################################################################################
 
 
 #LINK --> https://blogs.oracle.com/cloud-infrastructure/post/step-by-step-instructions-to-send-email-with-oci-email-delivery 
 #python script for sending SMTP configuration with Oracle Cloud Infrastructure Email Delivery
 
 
import smtplib 
import email.utils
from email.message import EmailMessage
import ssl

# Replace sender@example.com with your "From" address.
# This address must be verified.
# this is the approved sender email
def sendEmail(message,error_message):
    SENDER = '<my email>'
    SENDERNAME = 'Elói Lopes'
    
    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = '<email>'
    
    # Replace the USERNAME_SMTP value with your Email Delivery SMTP username.
    USERNAME_SMTP = 'ocid1.user.oc1..aaaaaaaaa4qa4sjad3.....'
    
    # Put the PASSWORD value from your Email Delivery SMTP password into the following file.
    PASSWORD_SMTP_FILE = 'ociemail.config'
    
    # If you're using Email Delivery in a different region, replace the HOST value with an appropriate SMTP endpoint.
    # Use port 25 or 587 to connect to the SMTP endpoint.
    HOST = "smtp.email.eu-frankfurt-1.oci.oraclecloud.com"
    PORT = 587
 
    # The subject line of the email.
    SUBJECT = message
    
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = (message + "\r\n" +
                error_message
                )
    
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>"""+message + """</h1>
    <p>Error: """ + error_message+"""</p>
    </body>
    </html>"""

    # get the password from a named config file ociemail.config
    with open(PASSWORD_SMTP_FILE) as f:
        password_smtp = f.readline().strip()

    # create message container
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT

    # make the message multi-part alternative, making the content the first part
    msg.add_alternative(BODY_TEXT, subtype='text')
    # this adds the additional part to the message
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.add_alternative(BODY_HTML, subtype='html')

    # Try to send the message.
    try: 
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        # most python runtimes default to a set of trusted public CAs that will include the CA used by OCI Email Delivery.
        # However, on platforms lacking that default (or with an outdated set of CAs), customers may need to provide a capath that includes our public CA.
        server.starttls(context=ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None))
        # smtplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, password_smtp)
        # our requirement is that SENDER is the same as From address set previously
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Email successfully sent!")
