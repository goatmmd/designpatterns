"""
    the observer method is a Behavioral design Pattern which allows you to define or create a subscription mechanism to
    send the notification to the multiple objects about any new event that happens to the object that they are observing.
    The subject is basically observed by multiple objects. The subject needs to be monitored and whenever there is a change in the subject,
    the observers are being notified about the change. This pattern defines one to Many dependencies between objects so that one object changes state,
    all of its dependents are notified and updated automatically.
"""

from abc import abstractmethod, ABC


class Notification_Base(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Notification_Base):
    @staticmethod
    def send(message=''):
        return f"Send Email : {message}"


class SMSNotification(Notification_Base):
    @staticmethod
    def send(message=''):
        return f"Send Sms : {message}"
