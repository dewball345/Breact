from breact.baseclasses import *
from browser.html import *
from browser import document, bind, timer


QUIZ_CONTENT = [
    {"question": "What is 2+2", 'options': [1,3,4,2], 'answer': 4},
    {"question": "What is 2+1", 'options': [1,34,3,2], 'answer': 3},
    {"question": "What is 33+1", 'options': [1,34,4,2], 'answer': 34},
]

class Quiz(StatefulSegment):
    def __init__(self):
        self.oi = GenerateContainers()
        self.state = {"question": 0, "correct":0, "wrong":0}
    def update(self, one_state_change=False):
        if self.state["question"] >= len(QUIZ_CONTENT):
            print("Reached!")
            app = group(DIV(Class="m-3"), [
                H1(f"Correct: {self.state['correct']}"),
                H1(f"Wrong: {self.state['wrong']}"),
                reset := BUTTON("reset", Class="btn btn-danger")    
            ])

            @bind(reset, "click")
            def toZero(e):
                # del self.state['prev']
                self.setState({"question":0, "correct":0, "wrong":0})
            
            return app

        elementOn = QUIZ_CONTENT[self.state["question"]]
        options = elementOn['options']
        question = elementOn['question']
        ans = elementOn['answer']

        def correctWrong():
            if "prev" in self.state:
                if self.state["prev"] == True:
                    return H3("Your answer is correct", Class="text-success")
                return H3("Your answer was wrong", Class="text-danger")
            return DIV()

        app = group(DIV(Class="container", style={
            "minWidth": "60vw"    
        }), [
            H1(question + ":"),
            correctWrong(),
            group(DIV(Class="container"), [
                group(DIV(Class="row"), [
                    option1 := BUTTON(options[0], Class="col-sm btn btn-danger m-2"),
                    option2 := BUTTON(options[1], Class="col-sm btn btn-info m-2"),
                ]),
                group(DIV(Class="row"), [
                    option3 := BUTTON(options[2], Class="col-sm btn btn-warning m-2"),
                    option4 := BUTTON(options[3], Class="col-sm btn btn-success m-2"),
                ])
            ])
        ])

        def submission(option):
            if options[option] == ans:
                correct = True
            else:
                correct = False
            self.setState({"prev": correct})
            def next():
                del self.state['prev']
                self.setState({
                    "question": self.state["question"] + 1, 
                    "correct": self.state["correct"] + 1 if correct else self.state["correct"],
                    "wrong": self.state["wrong"] + 1 if not correct else self.state["wrong"]
                }) 
            timer.set_timeout(next, 500)

        @bind(option1, "click")
        def nextOption1(e):
            submission(0)

        @bind(option2, "click")
        def nextOption2(e):
            submission(1)

        @bind(option3, "click")
        def nextOption3(e):
            submission(2)

        @bind(option4, "click")
        def nextOption4(e):
            submission(3)

        return app

class Main(Base):
    def render(self):
        return group(
            DIV(Class="container d-flex flex-column justify-content-center align-items-center", style={
                "height": "100vh"
            }), 
            [
                Quiz().render()
            ]
        )

# document <= Main().render()