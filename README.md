# Domain Watcher

A lightweight Python tool to monitor domain availability using WHOIS queries.  
Sends email alerts when a domain becomes available. Fully configurable via a simple `config.json` file.

---

## ✨ Features
- Monitor any domain’s availability via WHOIS.
- Automatic email alerts when a domain becomes available.
- Customizable check frequency, notification interval, and duration.
- SMTP configuration for your own mail server.
- All events are logged to both the console and a `watcher.log` file.

---

## 📦 Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## ⚙️ Configuration

Create a `config.json` file and fill in your details. 

**Important:** This file contains sensitive credentials. It is already listed in `.gitignore` to prevent accidental commits. **Do not remove it from `.gitignore` or share it publicly.**

```json
{
  "domain": "example.com",
  "smtp_host": "smtp.example.com",
  "smtp_port": 587,
  "smtp_user": "your-email@example.com",
  "smtp_pass": "your-password",
  "from_email": "your-email@example.com",
  "to_email": "recipient@example.com",
  "check_interval_hours": 2,
  "notify_interval_hours": 24,
  "notify_days": 3
}
```

---

## 🚀 How to Run

Simply run the script from your terminal:
```bash
python domain-watcher.py
```
The script will perform an initial check immediately upon starting and then continue to run in a loop. All activities will be displayed on the console and saved in the `watcher.log` file.

---

## 📝 Logging

All events, including domain checks, email notifications, and errors, are logged with timestamps. Logs are:
1.  Printed to the console in real-time.
2.  Saved to a `watcher.log` file in the project directory.

This allows you to have a persistent record of the watcher's activity.
