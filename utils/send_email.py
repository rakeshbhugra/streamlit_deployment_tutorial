from utils.email_helper import EmailHelper

def send_email(to, subject, body):
    email_helper = EmailHelper()

    to = "rakeshkbhugra@gmail.com"
    email_helper.send_email(to, subject, body)

    return "Email sent successfully!"

    
if __name__ == "__main__":
    subject = "Test Email from Streamlit App" 
    body = "This is a test email sent from the Streamlit app."
    send_email(subject, body)