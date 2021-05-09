from browser import document, html, window
import random

class Base:
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
        state_copy = self.state.copy()
        self.state.update(attrs)
        if self.state == state_copy:
            return;
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
                    print(str(oldChildren[i]), "not_equal_to", str(newChildren[i]))
                    oldChildren[i].parentNode.replaceChild(newChildren[i], oldChildren[i])

            if len(newChildren) > len(oldChildren):
                for i in newChildren[len(oldChildren):]:
                    print(str(i))
                    op <= i
            elif len(oldChildren) > len(newChildren):
                for i in oldChildren[len(newChildren):]:
                    i.remove()
        print("SETSTATE")
        old = document[self.oi.innerId].children
        update = self.update(one_state_change)
        uChildren = [update]
        find_diffs(old, uChildren, document[self.oi.innerId])

class OLD_StatefulSegment(Base):
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
