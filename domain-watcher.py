import time
import whois
import smtplib
import datetime
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class DomainWatcher:
    def __init__(self, config):
        self.domain = config["domain"]
        self.smtp_host = config["smtp_host"]
        self.smtp_port = config["smtp_port"]
        self.smtp_user = config["smtp_user"]
        self.smtp_pass = config["smtp_pass"]
        self.from_email = config["from_email"]
        self.to_email = config["to_email"]
        self.check_interval_hours = config.get("check_interval_hours", 2)
        self.notify_interval_hours = config.get("notify_interval_hours", 24)
        self.notify_days = config.get("notify_days", 3)
        self.domain_available = False
        self.last_notification_time = None
        self.notifications_sent = 0

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(self.from_email, self.to_email, msg.as_string())
            print(f"[{datetime.datetime.now()}] Mail gönderildi!")
        except Exception as e:
            print(f"[{datetime.datetime.now()}] Mail gönderilemedi: {e}")

    def check_domain(self):
        try:
            w = whois.whois(self.domain)
            if w.domain_name is None:
                print(f"[{datetime.datetime.now()}] {self.domain} ALINABİLİR (Available)")
                self.domain_available = True
            else:
                print(f"[{datetime.datetime.now()}] {self.domain} HENÜZ DOLMAMIŞ (Not Available) (Expire: {w.expiration_date})")
                self.domain_available = False
        except Exception as e:
            print(f"[{datetime.datetime.now()}] {self.domain} ALINABİLİR olabilir (Available) (Hata: {e})")
            self.domain_available = True

    def maybe_notify(self):
        if not self.domain_available:
            return

        now = datetime.datetime.now()
        if self.notifications_sent >= (self.notify_days * 24 // self.notify_interval_hours):
            return  # Bildirim hakkı doldu

        if (
            self.last_notification_time is None
            or (now - self.last_notification_time).total_seconds() >= self.notify_interval_hours * 3600
        ):
            subject = f"{self.domain} Domain Uyarısı"
            body = f"{self.domain} şu anda ALINABİLİR görünüyor!\n\nBu {self.notifications_sent + 1}. bildirimdir."
            self.send_email(subject, body)
            self.last_notification_time = now
            self.notifications_sent += 1

    def run(self):
        while True:
            print(f"[{datetime.datetime.now()}] Domain kontrol ediliyor...")
            self.check_domain()
            self.maybe_notify()
            time.sleep(self.check_interval_hours * 3600)


if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    watcher = DomainWatcher(config)
    watcher.run()
