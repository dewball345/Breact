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
        self.outerId = "id" + str(random.randint(1, 9999999999))
        self.innerId = "id" + str(random.randint(1, 9999999999))
        self.container = html.DIV(id=self.outerId)
        self.content = html.DIV(id=self.innerId)

class StatefulSegment(Base):
    '''
    Class is used for stateful components. Content in here is meant to be changed. 

    ...

    Attributes
    ----------
    You can pass props through the constructor, though this is optional

    Methods
    -------
    render() -> HTML Element
        Initial render of StatefulSegment

    update() -> HTML Element
        New content that will be placed when state changes.

    setState() -> None
        Changes states and updates DOM by first identifying container that needs to be changed and dom-diffing
    '''
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
        # for attr in attrs.keys():
        #     self.state[attr] = attrs[attr]

        if(len(attrs.keys()) > 0):
            self.state.update(attrs)

        #REMOVED COPY DETECTION, CODE DOESN'T WORK
        # print("HERE")
        # if(len(attrs.keys()) > 0 and not disable_copy):
        #     print(attrs.keys())
        #     state_copy = str(self.state)
        #     self.state.update(attrs)
        #     if str(self.state) == state_copy:
        #         print("SAME", self.state, state_copy)
        #         return;

        # print("reach") 
        def find_diffs(o, n, op):
            oldChildren = o
            newChildren = n
            for i in range(min(len(oldChildren), len(newChildren))):
                if(str(oldChildren[i]) == str(newChildren[i])):
                    if(len(oldChildren[i].children) == 0 and len(newChildren[i].children) == 0):
                        if(oldChildren[i].innerHTML != newChildren[i].innerHTML):
                            oldChildren[i].innerHTML = newChildren[i].innerHTML
                    else:
                        find_diffs(oldChildren[i].children, newChildren[i].children, oldChildren[i])
                elif(str(oldChildren[i]) != str(newChildren[i])):
                    # print(str(oldChildren[i]), "not_equal_to", str(newChildren[i]))
                    oldChildren[i].parentNode.replaceChild(newChildren[i], oldChildren[i])

            if len(newChildren) > len(oldChildren):
                for i in newChildren[len(oldChildren):]:
                    # print("APPEND")
                    # print(str(i))
                    op <= i
            elif len(oldChildren) > len(newChildren):
                for i in oldChildren[len(newChildren):]:
                    # print("REVOKE")
                    # print(str(i))
                    i.remove()
        # print("SETSTATE")
        old = document[self.oi.innerId].children
        update = self.update(one_state_change)
        uChildren = [update]
        find_diffs(old, uChildren, document[self.oi.innerId])

class OLD_StatefulSegment(Base):
    '''
    Former class for stateful components. Content in here is meant to be changed. 
    The difference between this and the new one is that there is no dom-diffing here. Content is simply removed and replaced.
    For Big stateful components, this can be a burden. If the new class doesn't work for you, please use this one.
    Also, feel free to submit an issue or pr.

    ...

    Attributes
    ----------
    You can pass props through the constructor, though this is optional

    Methods
    -------
    render() -> HTML Element
        Initial render of StatefulSegment

    update() -> HTML Element
        New content that will be placed when state changes.

    setState() -> None
        Changes states and updates DOM by first identifying container that needs to be changed and removing/replacing them
    '''

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
        if(len(attrs.keys()) > 0):
            self.state.update(attrs) 
        # Old code
#         for attr in attrs.keys():
#             self.state[attr] = attrs[attr]
        del document[self.oi.innerId]
        self.oi.content = html.DIV(id=self.oi.innerId)
        self.oi.content <= self.update(one_state_change)
        document[self.oi.outerId] <= self.oi.content


def group(parent, children):
    '''
    Because brython supports a list of children as input, this function is essentially useless.
    However, I will still keep it in case you have already used this method

    ...

    Parameters
    ----------
    Parent : HTML element
        This is the element that will have the children in it
    
    Children: List[HTML element]
        This is the children that will be added

    Returns
    -------
    HTML Element
        Combined element with parent and children
    '''

    for child in children:
        parent <= child
    return parent
