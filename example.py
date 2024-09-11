from abc import ABC, abstractmethod

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class EmailNotifier(NotifierInterface):
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")

class SMSNotifier(NotifierInterface):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier: NotifierInterface):
        self.notifier = notifier

    def send_notification(self, message: str) -> None:
        self.notifier.send(message)

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

email_service = NotificationService(email_notifier)
sms_service = NotificationService(sms_notifier)

email_service.send_notification("Hello, this is an email notification!")
sms_service.send_notification("Hello, this is an SMS notification!")
