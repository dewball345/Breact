# Tutorial

Let's learn the basics of breact by building a simple todolist app. 

# Installation

Make sure to view README.md for this

# Setup

Before we get started, create these empty files in this directory structure

```
todo_list
|-- index.html
|-- main.py
`-- /widgets
    |-- __init__.py
    |-- listitem.py
    `-- list.py
```

# Instructions:

## HTML

In your index.html file, put this boilerplate:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython.min.js">
        </script>
        <script type="text/javascript"
            src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython_stdlib.js">
        </script>
    </head>

    <body onload="brython()">
        <script type="text/python" src="./main.py"></script>
        <div id="root"></div>
    </body>
</html>
```

Lets focus on some important parts:

### In the head:

We'll use bootstrap for styling. This is optional. If you do not want to use bootstrap, simply ignore the parts where I add styling(the Class=) sections
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
```
This code is used for brython. We need this to code in python
```
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython.min.js">
</script>
```
This is if you want to import anything.
```
<script type="text/javascript"
    src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython_stdlib.js">
</script>
```

### In the body:

This part runs the brython code. This takes the python and compiles it into javascript
```
<body onload="brython()">
```
The link to our script
```
    <script type="text/python" src="./main.py"></script>
```
Like react, breact injects html into a div with an id "root"
```
    <div id="root"></div>
</body>
```

## Python
Unlike react(and a bit like flutter), breact components fall under two categories: Stateless(under the ```Base``` superclass), and Stateful Segments(under the ```StatefulSegment``` class)
Stateful Segments are sections of code that can be rerendered with set-state and are changed. 

Stateless components:
- do not inherit setState
- main code is placed in render() function
- cannot change state
- Can be used to call setState in Stateful components, but only the Stateful Segments are changed

Stateful segments:
- do inherit setSetstate
- main code is placed in update() function, which is called whenever setState() is called
- The update function rerenders stateful segments
- you CAN call setState() within a stateful segment's update() function, but be aware that it can cause an infinite loop as setState() would be called repeatedly. 
- If you want setState to only be called once in an update() function, set the ```one_state_change``` parameter in setState() as true.

### ListItem widget(Does not change, so stateless.)

In ```/widgets/listitem.py```:

```
from breact.baseclasses import *
from browser.html import *
#from browser import document, bind


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
```

Let's go over the important parts:

With your apps, please don't use ```import *```. 
```
#imports base classes that we need
from breact.baseclasses import *
#imports brython html components(be careful when using these, especially the headers and p tags, as they can be vunerable to xss attacks. Sanitize your content.)
from browser.html import *

#from browser import document, bind
```

Here we define our stateless component(sorry for mixing the terms Widget and Component so much)... Once I get my ```CONTRUBUTING.md``` up and running, 
please feel free to add edits.

```
class ListItemWidget(Base):
```

Here we call the constructor init function, where we can pass props.

```
    def __init__(self, title, description):
        self.title = title
        self.description = description     
```

Here we call the render function...

```
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
```

Wanna know what ```group()`` does?

Brython has a specialized operator ```<=```. It allows you to append children to an HTML element. However, you can only do this one at a time, which is inefficient.

The group function does the following

```
def group(parent, children):
  for child in children:
    parent <= child
   return parent
```

#### Edit: 5/9/2021 

Brython supports passing in a list of nested children. Therefore, you do not need the group() function. Instead, please pass the list of children as the first argument.

With this in mind, here's how you translate that python code into JSX

```
function render(){
  return <div className="card shadow-sm" style={{fontWeight: "bolder"}}>
    <div className="card-header">
      <h3>Title: {this.title} </h3>
    </div>
    <h5> {this.description} </h5>
  </div>
}
```

### List Widget(List of items, and this changes when you add another item. For this reason, it is a StatefulSegment)
in ```/widgets/list.py```:

```
from breact.baseclasses import *
from browser.html import *
from widgets.listitem import ListItemWidget

# from browser import document, bind

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
```

Important parts:

Here we define the component as a Stateful one.
```
class List(StatefulSegment):
```

Here we initialize our function with a constructor. We define our state variable, much like we do in react, but what about ```self.oi```?
```
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"items": []}
```

#### How Breact Changes State

Breact's main difference in react is that there is no virtual dom; instead, stateful components are marked with a unique id, and are referenced and changed during setState(). 
Each stateful component is wrapped with two containers- an outer one(for identifying the stateful component), and an inner one(for identifying the content within the component
to replace).

Once Breact identifies the containers that are needed to change state, it then uses a dom-diffing algorithm to identify which exact parts have changed. This is to prevent unnecessarily erasing and rewriting big Stateful components. 

Prior to 5/8/2021, Breact used to just delete and rerender the entire stateful component. If ```StatefulSegment``` does not work for you, or for some reason you want to use the old method, use the ```OLD_StatefulSegment``` class instead. 

the ```GenerateContainers``` class generates the unique containers with unique ids, and they are stored in the ```self.oi``` instance variable.


Remember, in a stateful component, the main code is written in an update() function. This is the code that will be rerendered during changes. 
You do not want to put forms and stuff here, as they will be reloaded, and so will the content in them(though the data entered should be intact). 
This will make for an irritating process, so as a workaround, define them in a Stateless component and manage their state in a stateful container,
that handles state but doesn't render anything. If you want to see the code for that, visit the ```pages/todolist.py```, and view the ```TxtManager```
class. This will also be mentioned later on in this tutorial btw, so view them after reading this

Anyway, here is the update function. Anonymous functions are pretty limited in python, so create a nested function instead, like so.

```
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
```

### The main file(connecting the two widgets above together)

in main.py

```
from breact.baseclasses import *
from widgets import ListItemWidget, List
from browser.html import *
from browser import document, bind

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
```

Important parts

Necessary import statements needed

```
from breact.baseclasses import *
from widgets import ListItemWidget, List
from browser.html import *
from browser import document, bind
```

Here we are creating a TxtManager class. This stores the text information that is being typed without reloading the textbox component and removing what is typed already
```
class TxtManager(StatefulSegment):
```
Here we have our constructor. This class will store the title and description that is being typed.
```
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"title":"", "description":""}
```
Because this just manages the state of the text boxes, nothing needs to be rendered
```
    def update(self, one_state_change=False):
        return DIV()
```

This class has the list of todo items, and a form which you can use to enter a new item. The ordinary components in here will not change, so this is a Stateless class
```
class TodoMain(Base):
```

This is our render function, and it is a bit big. 
```
    def render(self):
        #initialize the text manager class that handles input state
        txt = TxtManager()
        #the list of items
        todo = List()
        #we are storing the content that we want to render in a variable
        app = group(DIV(Class="container d-flex flex-column justify-content-center"), 
            group(DIV(Class="container-sm m-3"), [
                DIV(style={
                    "margin":"10px"
                }),
                #when you call the render function it returns the html elements.
                txt.render(),
                H1("Todo List With Breact"),
                DIV(style={
                    "margin":"10px"
                }),
                #rendering the list of items
                todo.render(),
                
                #this is our form
                group(DIV(Class="row"), [
                    group(DIV(Class="col-sm form-group"), [
                        LABEL("Enter Title", to="inputt", Class="form-label"),
                        #This beautiful syntax is part of python. the :=(beaver) operator returns an object and stores it to a variable, which we can modify
                        title := INPUT(id="inputt", type="text", Class="form-control"),
                    ]),
                    description := group(DIV(Class="col-sm form-group"), [
                        LABEL("Enter Description", to="inputts", Class="form-label"),
                        TEXTAREA(id="inputts", type="text", Class="form-control")
                    ]),
                ]),
                #button that submits
                btn := BUTTON("Submit please", Class="btn btn-primary m-2"),
                DIV(style={
                    "margin":"40px"
                })
            ])
        )
```
This may look complete by now, but keep in mind that these component's don't do anything yet. Let's change that
```
        #this changes the state of the text manager to store the text input
        @bind(title, "keyup")
        def updateTitle(e):
            txt.setState({"title": e.target.value})
        
        @bind(description, "keyup")
        def updateDesc(e):
            txt.setState({"description": e.target.value})
            
        #this appends the newest item to the list of items when the button is clicked
        @bind(btn, "click")
        def submit(e):
            submission = {
                "title":txt.state["title"], 
                "description":txt.state["description"]
            }
            todo.state["items"].append(submission)
            todo.setState({"items": todo.state["items"]})
        return app
```

You might wonder why i call setState() externally? It's a bit different that react, right? Basically, stateful segments get replaced when their state is changed
which is why you don't keep textboxes in them; when they are replaced, the textbox's value is reset, meaning that you have to type all over again.

Here you add the page to the ```main.html``` file, so that the user can see and interact with it.

```
document["root"] <= Main().render()
```

...And we're done! If everything worked, you should see

![image](https://user-images.githubusercontent.com/30184788/116163119-03024c00-a6ac-11eb-9f88-cd8be059329b.png)

If you have any problems, please put them in the issues tab in this repo








