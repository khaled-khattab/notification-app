from abc import ABC, abstractmethod


class NotificationMethod(ABC):
    @abstractmethod
    def send(self):
        pass

