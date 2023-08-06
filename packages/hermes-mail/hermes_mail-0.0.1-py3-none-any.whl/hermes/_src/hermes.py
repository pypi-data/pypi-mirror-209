import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

# Set up logging with metadata
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Client:
    def __init__(self, password: str):
        self.logger = logging.getLogger(__name__)
        self.password = password
        if not self.password:
            self.logger.error("No email password provided. Set EMAIL_PASSWORD environment variable.")

    def send_email(self, sender_email: str, receiver_email: List[str], subject: str, body: str):
        """Send an email via Gmail.

        Args:
            sender_email: The sender's email address.
            receiver_email: A list of receiver's email addresses.
            subject: The subject line of the email.
            body: The body text of the email.

        Returns:
            None.
        """
        # Create email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_email)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(sender_email, self.password)
                server.sendmail(sender_email, receiver_email, text)
                self.logger.info("\033[32mEmail sent successfully to {}\033[0m".format(", ".join(receiver_email)))
        except Exception as e:
            self.logger.error("\033[31mFailed to send email. Error: {}\033[0m".format(str(e)))
