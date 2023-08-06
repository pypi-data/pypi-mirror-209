import requests
import common.config as config
cfg = config.Config()

def send_email(sender: str, to: list[str], subject: str, body_text: str):
    return requests.post(
        cfg.mailgun_api_url,
        auth=("api", cfg.mailgun_api_key),
        data={"from": sender,
              "to": to,
              "subject": subject,
              "text": body_text})

def send_email_closure(subject: str, body_text: str):
    def innerFunction():
        send_email(subject=subject, body_text=body_text)
    return innerFunction 