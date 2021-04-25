from breact.baseclasses import *
from browser.html import *
from browser import document, bind, timer, window

class Link(Base):
    def __init__(self, link):
        self.link = link
    def render(self, child):
        # button = child
        @bind(child, "click")
        def link(e):
            window.location.hash = "#" + self.link
        return child

class Redirect(Base):
    def __init__(self, link):
        self.link = link
    def render(self):
        window.location.hash = self.link

#TODO: add prefix to router to prevent redundancy
#TODO: global routes?
class Router(StatefulSegment):
    def __init__(self, routes, err_component):
        self.oi = GenerateContainers()
        # self.state = {"home": "/"}
        self.routes = routes
        self.err_component = err_component

    def findComponentByPath(self, path):
        if path in self.routes:
            return self.routes[path]
        else:
            return None
    def updateHash(self, e):
        # print("loaded", dir(e))
        self.setState({})
    def render(self):
        self.oi.content <= self.update()
        self.oi.container <= self.oi.content
        window.onload = self.updateHash
        window.onhashchange = self.updateHash
        return self.oi.container
    def update(self, one_state_change=False):
        path = window.location.hash[1:].lower()
        if path == "":
            window.location.hash = "#/"
            path = "/"
        component = self.findComponentByPath(path)
        if component == None:
            component = self.err_component

        return component()