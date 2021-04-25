from breact_code.baseclasses import *
from browser.html import *
from browser import document, bind


class ListItemWidget(Base):
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def render(self):
        return group(DIV(Class="card shadow-sm", style={
            "margin":"20px"
        }), [
            group(DIV(Class="card-header"), [
                H3(f"Title: {self.title}", style={
                    "font-weight":"bolder"
                }),
            ]),

            H5(f"Description: {self.description}", Class="card-body")
        ])

class List(StatefulSegment):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"items": []}
    def update(self, one_state_change=False):
        def func(item):
            return ListItemWidget(item["title"], item["description"]).render()
        return group(DIV(Class="bg-primary", style={
            "height":"400px",
            "overflowY":"scroll",
            "margin-bottom": "50px",
            # "background-color": "#AABBFF",
            "border-radius": "5px"
        }), [
            func(item) for item in self.state["items"]
        ])

class TxtManager(StatefulSegment):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"title":"", "description":""}
    def update(self, one_state_change=False):
        return DIV()

class TodoMain(Base):
    def __init__(self):
        super().__init__()
        print("initted")
    def onCreated():
        print("Component Created!")
    def render(self):
        txt = TxtManager()
        todo = List()
        app = group(DIV(Class="container d-flex flex-column justify-content-center"), 
            group(DIV(Class="container-sm m-3"), [
                DIV(style={
                    "margin":"10px"
                }),
                txt.render(),
                H1("Todo List With Breact"),
                DIV(style={
                    "margin":"10px"
                }),
                todo.render(),

                group(DIV(Class="row"), [
                    group(DIV(Class="col-sm form-group"), [
                        LABEL("Enter Title", to="inputt", Class="form-label"),
                        title := INPUT(id="inputt", type="text", Class="form-control"),
                    ]),
                    description := group(DIV(Class="col-sm form-group"), [
                        LABEL("Enter Description", to="inputts", Class="form-label"),
                        TEXTAREA(id="inputts", type="text", Class="form-control")
                    ]),
                ]),

                btn := BUTTON("Submit please", Class="btn btn-primary m-2"),
                DIV(style={
                    "margin":"40px"
                })
            ])
        )

        @bind(title, "keyup")
        def updateTitle(e):
            txt.setState({"title": e.target.value})
        
        @bind(description, "keyup")
        def updateDesc(e):
            txt.setState({"description": e.target.value})

        @bind(btn, "click")
        def submit(e):
            submission = {
                "title":txt.state["title"], 
                "description":txt.state["description"]
            }
            todo.state["items"].append(submission)
            todo.setState({"items": todo.state["items"]})
        return app

# document["root"] <= Main().render()