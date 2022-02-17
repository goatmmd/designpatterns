from abc import ABC, abstractmethod


class Message:
    """
    When you have alot of options to switch of your options
    in the runtime which pattern will be help ?
    That's a meaning of STATE
    this is our simple code to an automation employee in
    """
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_user):
        if to_user.__class__ not in self.current.allowed:

            print(f'{self.current.__class__} Not Allowed send message to {to_user.__class__} ')
        else:
            self.flow.append(to_user)
            print(f'{self.subject} - Send from {self.sender.__class__} to {to_user.__class__}')


class AbstractUser(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass


class HeadManager(AbstractUser):
    allowed = []


class InternalManager(AbstractUser):
    allowed = [HeadManager]


class Supervisor(AbstractUser):
    allowed = [InternalManager]


class Operator(AbstractUser):
    allowed = [Supervisor]


class Client(AbstractUser):
    allowed = [Operator]


if __name__ == "__main__":
    head_manager = HeadManager()
    internal_manager = InternalManager()
    supervisor = Supervisor()
    operator = Operator()

    client = Client()

    message = Message('Issue #12', "Issue Description", client)
    message.send(head_manager)
    message.send(operator)
