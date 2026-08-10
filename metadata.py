from flask import Flask, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    full_message = f"""
    New Contact Form Submission

    From: {name}
    Email: {email}

    Message:
    {message}
    """

    msg = MIMEText(full_message)
    msg["Subject"] = "New Contact Form Message"
    msg["From"] = email
    msg["To"] = "contactme@kayeeloisaa.info"   # Your email

    # SMTP Example (Gmail)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("YOUR_EMAIL@gmail.com", "YOUR_APP_PASSWORD")
        server.sendmail(email, "contactme@kayeeloisaa.info", msg.as_string())

    return "Message sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)
