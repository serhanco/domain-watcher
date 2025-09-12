# Domain Watcher

A lightweight Python tool to monitor domain availability using WHOIS queries.  
Sends email alerts when a domain becomes available. Fully configurable via Python code or a simple `config.json` file.

---

## ✨ Features
- Monitor any domain’s availability via WHOIS.
- Automatic email alerts when a domain becomes available.
- Customizable check frequency, notification interval, and duration.
- SMTP configuration for your own mail server.
- Configurable through code or `config.json`.

---

## 📦 Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install python-whois

⚙️ Configuration

You can configure the watcher in two ways:

## 1. Inside Python Code

Edit the parameters directly in domain_watcher.py:

watcher = DomainWatcher(
    domain="serhan.co",
    smtp_host="mail.kurumsaleposta.com",
    smtp_port=587,
    smtp_user="your-email@example.com",
    smtp_pass="your-password",
    from_email="your-email@example.com",
    to_email="recipient@example.com",
    check_interval_hours=2,
    notify_interval_hours=24,
    notify_days=3
)

## 2. Using config.json

Create a config.json file:

{
  "domain": "serhan.co",
  "smtp_host": "mail.kurumsaleposta.com",
  "smtp_port": 587,
  "smtp_user": "your-email@example.com",
  "smtp_pass": "your-password",
  "from_email": "your-email@example.com",
  "to_email": "recipient@example.com",
  "check_interval_hours": 2,
  "notify_interval_hours": 24,
  "notify_days": 3
}


## Run:

python domain_watcher.py

## 📧 How it works

The script checks the WHOIS record of your chosen domain.

If the domain is free, an email notification is sent.

Notifications repeat according to your chosen interval and number of days.

## 🚀 Example

Check every 2 hours.

If domain is available, send notification every 24 hours.

Continue for 3 days.
