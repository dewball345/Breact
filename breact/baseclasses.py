from browser import document, html, window
import random


class Base:
    '''
    The Base(as mentioned in the class name) class, the one which all stateless and stateful components come from

    ...

    Attributes
    ----------
    You can pass props through the constructor. This is optional; no props need to be passed for this to work

    Methods
    -------
    render() -> an HTML element
        Initial rendering of content
    '''

    #Initial render of content(the collective content in this class will only be rendered once)
    def render(self):
        pass

class GenerateContainers:
    '''
    Class is used to generate containers that are identified and dom-diffed during setState()

    ...

    Attributes
    ----------
    self.outerId : str
        The id of the first identifier in setState. 

    self.innerId : str
        The id of the second identifier in setState. 

    self.container: html.DIV
        This is the first identifier in setState. Breact uses a simple 
        getElementById to access this container. The content container
        resides in here

    self.content: html.DIV
        This is the second identifier in setState, and holds the main 
        content. This container is dom-diffed in the StatefulSegment
        class or deleted and reupdated in the OLD_StatefulSegment class

    Methods
    -------
    None
    '''

    def __init__(self):
        self.outerId = "id" + str(random.randint(1, 999999999))
        self.innerId = "id" + str(random.randint(1, 999999999))
        self.container = html.DIV(id=self.outerId)
        self.content = html.DIV(id=self.innerId)

class StatefulDomDiffing(Base):
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
        self.state.update(attrs) 
        # Old code
#         for attr in attrs.keys():
#             self.state[attr] = attrs[attr]
        del document[self.oi.innerId]
        self.oi.content = html.DIV(id=self.oi.innerId)
        self.oi.content <= self.update(one_state_change)
        document[self.oi.outerId] <= self.oi.content
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
        self.state.update(attrs) 
        # Old code
#         for attr in attrs.keys():
#             self.state[attr] = attrs[attr]
        del document[self.oi.innerId]
        self.oi.content = html.DIV(id=self.oi.innerId)
        self.oi.content <= self.update(one_state_change)
        document[self.oi.outerId] <= self.oi.content


def group(parent, children):
    for child in children:
        parent <= child
    return parent
