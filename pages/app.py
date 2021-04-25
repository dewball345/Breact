from browser import document, html, window, timer, bind
from breact.baseclasses import *


'''
HTML4 tags : A, ABBR, ACRONYM, ADDRESS, APPLET, AREA, B, 
BASE, BASEFONT, BDO, BIG, BLOCKQUOTE, BODY, BR, BUTTON, 
CAPTION, CENTER, CITE, CODE, COL, COLGROUP, DD, DEL, DFN,
 DIR, DIV, DL, DT, EM, FIELDSET, FONT, FORM, FRAME, FRAMESET, 
 H1, H2, H3, H4, H5, H6, HEAD, HR, HTML, I, IFRAME, IMG, INPUT, 
 INS, ISINDEX, KBD, LABEL, LEGEND, LI, LINK, MAP, MENU, META, 
 NOFRAMES, NOSCRIPT, OBJECT, OL, OPTGROUP, OPTION, P, PARAM, 
 PRE, Q, S, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, STRONG, 
 STYLE, SUB, SUP, SVG, TABLE, TBODY, TD, TEXTAREA, TFOOT, TH, 
 THEAD, TITLE, TR, TT, U, UL, VAR
HTML5 tags : ARTICLE, ASIDE, AUDIO, BDI, CANVAS, COMMAND, DATA, 
DATALIST, EMBED, FIGCAPTION, FIGURE, FOOTER, HEADER, KEYGEN, MAIN, 
MARK, MATH, METER, NAV, OUTPUT, PROGRESS, RB, RP, RT, RTC, RUBY, 
SECTION, SOURCE, SUMMARY, TEMPLATE, TIME, TRACK, VIDEO, WBR
HTML5.1 tags : DETAILS, DIALOG, MENUITEM, PICTURE, SUMMARY
In the following link you can find the index of HTML tags with references (DRAFT).
'''




#tickers
class Ticker(StatefulSegment):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"tick": 0, "tock": 0}
    def update(self, one_state_change=False):
        stfulComp = group(html.DIV(), [
            html.H2(self.state["tick"]),
            html.H2(self.state["tock"])
        ])
        def increment():
            self.setState({
                "tick":self.state["tick"]+1, 
                "tock":self.state["tock"]-1
            })
        
        if not one_state_change:
            print("set time out")
            timer.set_timeout(increment, 1000)
        return stfulComp


class TickerWithDescription(Base):
    def render(self):
        app = html.DIV()
        tk = Ticker()
        # app <= tk.render()

        btn = html.BUTTON("click me to reset")
        @bind(btn, "click")
        def reset(e):
            tk.setState({"tick":0, "tock":0}, True)
        # app <= btn

        app = group(app, [
            tk.render(), btn
        ])
        return app


#text field 
class AffectedByTextField(StatefulSegment):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"text": "d"}
    def update(self, one_state_change=False):
        return html.H1(self.state["text"].replace("<", "&lt;"))

class TextField(Base):
    def __init__(self, title):
        self.title = title
    def render(self):
        app = html.DIV()

        aft = AffectedByTextField()
        input = html.INPUT(type="text")
        
        
        @bind(input, "keyup")
        def update(e):
            aft.setState({"text": e.target.value})

        app = group(app, [
            html.H1(self.title),
            aft.render(),
            input
        ])
        # app <= aft.render()
        # app <= input
        return app


#thing that makes me happy because it uses group a lot!
class WithGroups(Base):
    def render(self):
        app = group(html.DIV(), [
            html.H1("HI THERE!"),
            html.H2("GOOD TO SEE YOU!"),
            html.P("Some things about me:"),
            html.UL(
                [
                    html.LI("I am"),
                    html.LI("Does this work")
                ]
            ),
            html.H2("here is a nice little ticker"),
            TickerWithDescription().render(),
            TextField("here is a prop being passed").render()
        ])
        return app

# app = html.DIV(id="hithere")


# # app <= html.H1("hi there", id="what")
# thing = group(app, [WithGroups().render()])
# # thing = app
# document["root"] <= thing
# thid = document["hithere"]
# thid.innerHTML = "hedy"
# print(document.getElementById("hithere").innerHTML)
# document["what"] <= html.H1("buy")