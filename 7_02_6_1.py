from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return ('Базовый класс Model')

class ModelForm(Model):
    def __init__(self, log, pas):
        self._log = log
        self._pas = pas
        self._id = hash(log) + hash(pas)

    def get_pk(self):
        return self._id