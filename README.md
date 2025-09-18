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

To configure the watcher, create a `config.json` file. This file must be in the same directory as the script or the final executable.

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

There are two ways to run the application:

### 1. As a Python Script

Simply run the script from your terminal:
```bash
python domain-watcher.py
```

### 2. As a Standalone Executable

1.  Build the executable (see [Building the Executable](#-building-the-executable)).
2.  Place the generated `domain-watcher.exe` (from the `dist` folder) in any directory.
3.  Place your `config.json` file in the **same directory** as the `.exe` file.
4.  Double-click `domain-watcher.exe` to run it.

The script will perform an initial check immediately upon starting and then continue to run in a loop. All activities will be displayed on the console and saved in the `watcher.log` file in the same directory.

---

## 📝 Logging

All events, including domain checks, email notifications, and errors, are logged with timestamps. If `watcher.log` does not exist, it will be created with a "Log file created" message. Logs are:
1.  Printed to the console in real-time.
2.  Saved to a `watcher.log` file in the application's directory.

This allows you to have a persistent record of the watcher's activity.

---

## 💻 Building the Executable

To create a standalone Windows executable (`.exe`) that is portable and configurable, `pyinstaller` is used.

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the build command:**
    ```bash
    python -m PyInstaller --onefile domain-watcher.py
    ```
3.  **Find the executable:**
    The generated `domain-watcher.exe` file will be located in the `dist` directory. This executable can be moved to any location, as long as a `config.json` file is present in the same directory.
