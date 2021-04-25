from browser import document, html, window
import random
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def render(self):
        pass

class GenerateContainers:
    def __init__(self):
        self.outerId = "id" + str(random.randint(1, 999999999))
        self.innerId = "id" + str(random.randint(1, 999999999))
        self.container = html.DIV(id=self.outerId)
        self.content = html.DIV(id=self.innerId)

class StatefulSegment(Base):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {}
    def render(self):
        self.oi.content <= self.update()
        self.oi.container <= self.oi.content
        return self.oi.container
    def update(self):
        pass
    def setState(self, attrs, one_state_change=False):
        for attr in attrs.keys():
            self.state[attr] = attrs[attr]
        del document[self.oi.innerId]
        self.oi.content = html.DIV(id=self.oi.innerId)
        self.oi.content <= self.update(one_state_change)
        document[self.oi.outerId] <= self.oi.content


def group(parent, children):
    for child in children:
        parent <= child
    return parent