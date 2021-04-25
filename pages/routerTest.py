


from breact.baseclasses import *
from browser.html import *
from browser import document, bind, timer, window
from breact.router import *

print(window.location.hash)


class Page(Base):
    def __init__(self, title):
        self.title = title
    def render(self):
        return group(DIV(), [
            H1(self.title),
            Link('/router-playground/').render(BUTTON('/')),
            Link('/router-playground/page1').render(BUTTON('/page1')),
            Link('/router-playground/page2').render(BUTTON('/page2'))
        ])


# class Link(Base):
#     def __init__(self, link):
#         self.link = link
#     def render(self):
#         button = BUTTON(self.link)
#         @bind(button, "click")
#         def link(e):
#             window.location.hash = "#" + self.link
#         return button

# class Page(Base):
#     def __init__(self, title):
#         self.title = title
#     def render(self):
#         return group(DIV(), [
#             H1(self.title),
#             Link('/').render(),
#             Link('/page1').render(),
#             Link('/page2').render()
#         ])

# class Router(StatefulSegment):
#     def __init__(self, routes):
#         self.oi = GenerateContainers()
#         # self.state = {"home": "/"}
#         self.routes = routes

#     def findComponentByPath(self, path):
#         if path in self.routes:
#             return self.routes[path]
#         else:
#             return None
#     def updateHash(self, e):
#         # print("loaded", dir(e))
#         self.setState({})
#     def render(self):
#         self.oi.content <= self.update()
#         self.oi.container <= self.oi.content
#         window.onload = self.updateHash
#         window.onhashchange = self.updateHash
#         return self.oi.container
#     def update(self, one_state_change=False):
#         path = window.location.hash[1:].lower()
#         if path == "":
#             window.location.hash = "#/"
#             path = "/"
#         component = self.findComponentByPath(path)
#         if component == None:
#             component = Page("error").render

#         return component()

# # def appendRouter(d):
# #     print("in append") 
# #     print("D", d)
# #     document <= "hi" #RouterTest().render()
# # # print(window.onload)
# # # window.onhashchange(appendRouter)
# # def thing():
# #     print("here")
# #     window.onload(appendRouter)
# # timer.set_timeout(thing, 1000)


def RouterTestPage():
    return Router({
        "/router-playground": Page("Home Page").render,
        "/router-playground/page1": Page("Page 1").render,
        "/router-playground/page2": Page("Page 2").render
    }, lambda: H1("An error occurred")).render()