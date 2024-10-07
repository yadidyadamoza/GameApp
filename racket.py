from turtle import Turtle

#נשתמש ב OOP שבעזרתו ניצור מחלקה של המחבט
#אנו מבצעים ירושה מספריית Turtel כדי להתשמש בתכונות שלו

class Racket(Turtle):
    # הבנאי יקבל מהמשתמש את קורדינטות וככה יבנה את המחבט
    def __init__(self, position):
        # כדי שנוכל לגשת לכל הפונקציות בספריית Turtel
        super().__init__()
        # יצירת המחבט של השחקן
        self.shape("square")
        # מגדיר את המימדים של האוביקט
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

     # פונקציה שתזיז את המחבט למעלה
    def move_up(self):
        # אנו זזים על ציר ה Y
        up = self.ycor() + 25
        # אנו לא משנים את המיקום של ציר ה X
        self.goto(self.xcor(), up)

     # פונקציה שתזיז את המחבט למטה
    def move_down(self):
        # אנו זזים על ציר ה Y
        down = self.ycor() - 25
         # אנו לא משנים את המיקום של ציר ה X
        self.goto(self.xcor(), down)