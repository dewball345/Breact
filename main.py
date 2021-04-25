from breact_code.baseclasses import *
from browser.html import *
from browser import document, bind, timer, window
from breact_code.router import *
from pages.quiz import *
from pages.todolist import *
from pages.app import *
from pages.routerTest import *

def homePage():
    return group(DIV(Class="container d-flex flex-column justify-content-center align-items-center", style={
        "height":"100vh"
    }), [
        H1("Breact: A python library for single page webapps", Class="text-center"),
        P('''
            This app was coded in python in Breact. Look in the inspector, and you will see
            <br>
            <code>&lt;script src="text/python" &gt; </code>
        ''', Class="text-center"),
        
        # P('''
        #     Breact is similar to react, 
        #     with components and state. The main difference, however, is that
        #     Breact doesn't have a virtual dom; instead, each stateful element
        #     (element that uses setState) is assigned a unique id and is retrieved
        #     and changed when necessary. Breact is very lightweight- the main base
        #     class file is at around 40 lines of code; but that's just because some parts of react;
        #     lifecycle methods, or stateful functional components, haven't been implemented yet.
        # ''', Class="text-center"),
        H3("Sample Apps:"),
        Link("/todo").render(BUTTON("Simple Todolist", Class="btn btn-primary m-2")),
        Link('/quiz').render(BUTTON("Small Quiz", Class="btn btn-primary m-2")),
        Link('/playground').render(BUTTON("A Little Playground", Class="btn btn-primary m-2")),
        Link('/router-playground').render(BUTTON("Router Playground", Class="btn btn-primary m-2"))
    ])

document <= Router({
    "/": homePage,
    "/quiz": Main().render,
    "/todo": TodoMain().render,
    "/playground": WithGroups().render,
    "/router-playground": RouterTestPage
}, lambda: H1("An error occurred")).render()