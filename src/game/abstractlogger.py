from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    @abstractmethod
    def sendMessage(self, entity, message):
        pass
