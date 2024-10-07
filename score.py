# ניצור מחלקה שתחשב את הנקודות שכל משתמש השיג
from turtle import Turtle

# נבצע ירושה מספריית Turtel
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # ניצור 2 משתנים שיסכמו את הנקודות של 2 הצדדים
        self.left_score = 0
        self.right_score = 0
        # קריאה ללפונקציה שמעדכנת
        self.update_score()



      # מעדכן את הניקוד של המשתמש
    def update_score(self):
        # נשתמש בפונקציה של ניקוי מסך ככה הניקוד יתעדכן ולא ישאר על המסך
        self.clear()
        # נירשום היכן אנו רוצים שהניקוד השמאלי יופיע על המסך
        self.goto(-100, 190)
        # נירשום את ההצגה של הניקוד השמאלי
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))

        # ניצור את הניקוד הימני ואת המיקום שלו
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))



     # ניצור 2 פונקציות שיעלו את הנקודות של המשתמשים במידה ואחד מהם נפל לפני התנאים
    def left_point(self):
        self.left_score += 1
        # כאשר יש לנו נקודה נשתמש בפונקציה שמעדכנת לנו את הניקוד
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()