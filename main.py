import tkinter
from tkinter import *

from turtle import Turtle, Screen
import time
import random

import turtle
import pandas

from racket import Racket
from ball import Ball
from score import Score


window = tkinter.Tk()
window.title("GameApp")
window.minsize(width=1250, height=800)
window.config( bg="#BCCEF8")

snake_canvas = Canvas(width=195, height=192, highlightthickness=0)
snake_pic = PhotoImage(file="Snake Game pic.png")
snake_canvas.create_image(97, 96, image=snake_pic)
snake_canvas.place(x=65, y=180)


usa_canvas = Canvas(width=196, height=189)
usa_pic = PhotoImage(file="USA_Game.png")
usa_canvas.create_image(98, 94, image=usa_pic)
usa_canvas.place(x=500, y=180)


pong_canvas = Canvas(width=232, height=191, highlightthickness=0)
pong_pic = PhotoImage(file="PONGs-game-elements.png")
# נשים את חצי מהאורך והגובה של התמונה
pong_canvas.create_image(116, 96, image=pong_pic)
pong_canvas.place(x=930, y=180)



def snake_game():


    delay = 0.1

    score = 0
    high_score = 0

    screen = Screen()
    screen.title("Snake Game")
    screen.bgcolor("medium spring green")
    screen.setup(width=600, height=600)
    screen.tracer(0)  # מעדכן את הצעדים של הצב לפני 0 שניות

    # האוכל של הנחש שגורם לו לגדול
    food = Turtle()
    food.speed(0)
    food.color("red")
    food.shape("square")
    food.penup()
    food.goto(0, 100)

    # יצירת ראש הנחש בעזרת אוביקט מסוג Turtel
    head = Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    # מכניסים קורדינאטות - ראש הנחש יתחיל מהאמצע
    head.goto(0, 0)
    # ראש יהיה ללא כיון התחלה
    head.direction = "stop"

    # ניצור רשימה שכל פעם שהנחש אוכל ניצור אובייקט חדש שיהיה הזנב שלו שמתארך
    snake_tail = []

    # ניצור אוביקט מסוג turtel שיהיה העט שירשום את מספר הנקודות
    pen = Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

    # פונקציות תזוזה
    # בעזרתן אנו משתמשים בקורדנינטות של הראש וככה מזיזים את הראש על המסך לפי התנאים של פונקצית Move
    # בתנאים אנחנו מונעים מהנחש להיכנס לתוך עצמו בפעולה של למעלה/למטה/ימינה/שמאלה
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def do_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    # פונקציה להתקדם קדימה/אחורה, ניצור תנאי שאומר במידה ולחצנו למעלה/למטה נוסיף לקורדינטה של Y צעדים(20) ונעשה עדכון כדי שניראה על המסך
    # פונקציה להתקדם שמאלה/ימינה, ניצור תנאי שאומר במידה ולחצנו שמאלה/ימינה נוסיף לקורדינטה של X צעדים(20) ונעשה עדכון כדי שניראה על המסך
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # שימוש במקלדת לקריאה לפונקציות
    # מאזין למה שהמשתמש מזין במקלדת
    # על ידי לחיצה על הכפתורים שלנו במקלדת אנו קוראים לפונקציה
    screen.listen()
    screen.onkey(key="w", fun=go_up)
    screen.onkey(key="s", fun=do_down)
    screen.onkey(key="a", fun=go_left)
    screen.onkey(key="d", fun=go_right)

    # ניצור לולאה שתרוץ תמיד ותציג עדכונים למסך
    while True:
        screen.update()
        # פסילה - יצירת גבול המשחק
        # במידה וראש הנחש עובר את הקורדינטות הללו נעשה השעייה של שנייה במסך כדי לאתחל את הראש במרכז המסך
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            # ראש הנחש לא יזוז
            head.direction = "stop"

            # נסתיר את הזנב שהראש השיג לפני שנפסל
            for remove in snake_tail:
                remove.goto(1000, 1000)
            # ננקה את הרשימה של הזנב שהראש השיג
            snake_tail.clear()
            # נאתחל את מהירות הנחש
            delay = 0.1
            # כאשר הנחש פוגע בגבול אנו נירצה לאפס את הניקוד שלנו למשחק הבא
            score = 0
            # כדי שלא נירשום את הניקוד אחד על השני נמחוק את מה שהיה לפני ואז נירשום את הניקוד החדש כאר הנחש אוכל
            pen.clear()
            # נדפיס למסך את הערכים של הניקוד שהשגנו במהלך המשחק
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # בדיקה של הקורדינאטות של האוכל וראש הנחש
        if head.distance(food) < 20:
            # 20 מציין את מרחק התנוע של הראש בכל שנייה
            # הטווח הוא בין -290 ולבין 290 כי אנחנו לא רוצים שההופעה של האוכל יהיה מחוץ לגבול ולא על הגבול
            # אחרי שהראש אכל את האוכל נזיז את האוכל למקום רנדומלי במסך
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            # נוסיף קטע לאורך הזנב ניצור אוביקט של TURTLE
            new_tail = Turtle()
            new_tail.speed(0)
            new_tail.shape("square")
            new_tail.color("black")
            new_tail.penup()
            # נעשה הוספה של הזנב החדש לזנב הישן
            snake_tail.append(new_tail)

            # כשאר הנחש אוכל נירצה שמהירות הנחש תעלה כדי להקשות על השחקן
            delay -= 0.001

            # כאשר הנחש אוכל הניקוד עולה
            score += 10
            if score > high_score:
                high_score = score
            # כדי שלא נירשום את הניקוד אחד על השני נמחוק את מה שהיה לפני ואז נירשום את הניקוד החדש כאר הנחש אוכל
            pen.clear()
            # נדפיס למסך את הערכים של הניקוד שהשגנו במהלך המשחק
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # הלולאה עובדת כאשר יש לנו יותר מחלק אחד ברשימה של החלקים לזנב החדש
        # ניצור לולאה שתחבר את החלקים של הזנב החדש מסוף הרשימה להתחלה
        for index in range(len(snake_tail) - 1, 0, -1):
            # נירצה שהחלקים של הזנב יזוז כמו החלק שלפניהם לפי קורדינאטות
            x = snake_tail[index - 1].xcor()
            y = snake_tail[index - 1].ycor()
            snake_tail[index].goto(x, y)
        # נעשה תנאי ונבדוק האם הרשימה של החלקים של הזנב החדש ריקה
        # במידה ויש רק חלק יחיד
        if len(snake_tail) > 0:
            x = head.xcor()
            y = head.ycor()
            snake_tail[0].goto(x, y)

        # קריאה לפונקצית move שתרוץ תמיד
        move()

        # פסילה - במידה וראש הנחשב נוגע בזנב
        for touch in snake_tail:
            if touch.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                # נשלח את הזנב לקורדינטה אחרת שהיא לא בגבול המסך
                for remove in snake_tail:
                    remove.goto(1000, 1000)
                # ננקה את המערך של הזנב שהראש השיג עד שנפסך
                snake_tail.clear()
                head.direction = "stop"
                # נאתחל את מהירות הנחש
                delay = 0.1
                # כאשר הנחש פוגע בגבול אנו נירצה לאפס את הניקוד שלנו למשחק הבא
                score = 0
                # כדי שלא נירשום את הניקוד אחד על השני נמחוק את מה שהיה לפני ואז נירשום את הניקוד החדש כאר הנחש אוכל
                pen.clear()
                # נדפיס למסך את הערכים של הניקוד שהשגנו במהלך המשחק
                pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        # נשלח את משתנה דיילי - ניעזר בתכונות של Time
        time.sleep(delay)
    # מריץ את התוכנית בלי הגבלה
    screen.mainloop()


def usa_game():
    screen = turtle.Screen()
    screen.title("USA GAME")
    # ניצור משתנה שיכיל את התמונה שלנו
    image = "blank_states_img.gif"
    # זה אומר שהתמונה תהיה על כל המסך
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")

    # נירצה לבדוק את שם המדינה שהמשתמש הכניס לפי העמודה של states ניצור אוביקט שיבדוק את המדינות
    # ניצור רשימה של המדינות לפי עמודה של State
    list_all_states = data.state.to_list()

    # ניצור רשימה ריקה של התשובות שלנו
    guess_stats = []
    # יש לנו 50 מדינות כל עוד שלא סיימנו לענות נכון על כל השמות התוכנית תמשיך לרוץ
    while len(guess_stats) < 50:
        # ניצור חלון בתוך המסך שהמשתמש יכניס את התשובה שלנו
        # אורך הרשימה הריקה שהמשתמש הכניס תשובה נכונה יעדכן את המשתמש בכמה תשובות הוא צדק
        # נשתמש בפונקצית title() כדי שימיר את האות הראשונה בתשובה של המשתמש לאות גדולה במידה והוא רשם אות קטנה
        answer = screen.textinput(title=f"{len(guess_stats)}/50 States",
                                  prompt="What do you think the answer is?").title()

        # במידה והמשתמש ירצה לצאת מהמשחק הוא יזין את המחרוזת Exit
        if answer == "Exit":
            break
        # תנאי שבודק האם תשובת המשתמש נמצאת בבסיס הנתונים שלנו
        if answer in list_all_states:
            # כל פעם שהמשתמש מכניס תשובה נכונה נכניס אותה לרשימה הריקה שלנו
            guess_stats.append(answer)
            # ניצור אוביקט
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            # לפי העמודה של State בדיקה של התשובה
            data_states = data[data.state == answer]
            # במידה והתשובה נכונה שם המדינה יופיע בקורדינטות של X ו Y לפי מה שהגדרנו בקובץ ה csv
            # הסיבה שאנחנו שמים int זה כי אנחנו רוצים את הקורדינטות בתור מספרים ולא בתור מחרוזות
            t.goto(int(data_states.x), int(data_states.y))
            t.write(answer)


def pong_game():
    # יצירת אוביקט מסוג מסך
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.setup(width=800, height=600)
    # לא מראה את העידכונים של האנימציה על המסך
    screen.tracer(0)

    # ניצור אובייקטים שקוראים לפונקצית המחבטים על ידי קריאה לפונציות שנמצאות במחלקת מחבט
    right_racket = Racket((350, 0))
    left_racket = Racket((-350, 0))
    # ניצור אובייקט מסוג כדור
    ball = Ball()
    # ניצור אוביקט מסוג ניקוד
    score = Score()

    # אנחנו מאזמינים למה שהמשתמש מכניס
    screen.listen()
    # אנו נכניס את האוביקטים שיצרנו מסוג Racket ובעזרתם אנו ניקרא לפונקציות שנמצאות במחלקה Reacket
    screen.onkey(key="w", fun=left_racket.move_up)
    screen.onkey(key="s", fun=left_racket.move_down)
    screen.onkey(key="o", fun=right_racket.move_up)
    screen.onkey(key="l", fun=right_racket.move_down)

    # ניצור לולאה שתעבוד כאשר השחקן פותח את החלון והיא תעדכן בצורה מהירה את מיקום המחבט
    # אחרי שמחבט נוצר והגיע למיקום שלו אנחנו ניראה אותו על המסך
    on_the_game = True
    while on_the_game:
        # ניגרום לדיילי כדי שניראה את התזוזה של הכדור בצורה איטית יותר
        time.sleep(0.05)
        screen.update()
        # נעשה קריאה לפונקצית move שנמצאת במחלקה של Ball
        ball.move()
        # נבצע בדיקה האם הכדור פגע בקיר
        # במידה והכדור עובר את הקורדינטות בציר ה Y של הקירות למטה ולמעלה זה אומר שהכדור צריך לקפוץ
        if ball.ycor() > 280 or ball.ycor() < -280:
            # קריאה לפונקציה במחלקת הכדור
            ball.bounce_y()

        # בדיקה האם הכדור פגע במחבט הימני או השמאלי
        # האורך של ציר ה X הוא 800 אם הקורדינטה של הכדור בציר ה X גדולה מ 320 וגם המרחק בין הכדור ולבין המחבט הימני קטן מ 50
        if ball.distance(right_racket) < 50 and ball.xcor() > 320 or ball.distance(
                left_racket) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # ציר האיקס - בדיקה האם הכדור עבר את הגבול מצד ימין
        if ball.xcor() > 380:
            ball.reset_position()
            # אם המשתמש הימני נפסל נביא למשתמש השמאלי ניקוד - ניצור פונקציה שתביא לשחקן נקודה 1
            score.left_point()
        # ציר האיקס - בדיקה האם הכדור עבר את הגבול מצד שמאל
        if ball.xcor() < -380:
            ball.reset_position()
            # אם המשתמש השמאלי נפסל נביא למשתמש הימני ניקוד - ניצור פונקציה שתביא לשחקן נקודה 1
            score.right_point()

    screen.exitonclick()


title = tkinter.Label(text="Classic games", bg="#BCCEF8", font=("Arial", 30))
title.place(x=500, y=0)

title2 = tkinter.Label(text="ברוכים הבאים למשחקים הקלאסים שכולנו זוכרים ואוהבים, כדי לשחק בבקשה להעביר את המקלדת לאנגלית", bg="#BCCEF8", font=("Arial", 22))
title2.place(x=50, y=50)

icon_game = tkinter.Label(text="🎮", bg="#BCCEF8", font=("Arial", 30))
icon_game.place(x=450, y=0)

icon_game2 = tkinter.Label(text="💾", bg="#BCCEF8", font=("Arial", 30))
icon_game2.place(x=762, y=0)
snake_text = tkinter.Label(text="משחק הסנייק הקלאסי", bg="#FAF7F0", font=("Arial", 12))
snake_text.place(x=90, y=380)
snake_text_2 = tkinter.Label(text="השחקן צריך לאסוף את התפוחים האדומים", bg="#FAF7F0", font=("Arial", 12))
snake_text_2.place(x=35, y=400)
snake_text_3 = tkinter.Label(text="W=למעלה,S=למטה,D=ימינה,A=שמאלה",bg="#FAF7F0", font=("Arial", 12))
snake_text_3.place(x=35, y=420)


usa_text = tkinter.Label(text ="משחק הקלאסי לגלות את אמריקה", bg="#FAF7F0", font=("Arial", 12))
usa_text.place(x=500, y=380)
usa_text_2 = tkinter.Label(text= "המטרה לירשום את שמות המדינות ברחבי יבשת אמריקה" ,bg="#FAF7F0", font=("Arial", 12))
usa_text_2.place(x=440, y=405)


pong_text = tkinter.Label(text="משחק הקלאסי משנות ה 70", bg="#FAF7F0", font=("Arial", 11))
pong_text.place(x=960, y=370)
pong_text2 = tkinter.Label(text="המטרה להכניס את הכדור לצד היריב", bg="#FAF7F0", font=("Arial", 10))
pong_text2.place(x=960, y=390)
pong_text3 = tkinter.Label(text=" למעלה = O למטה = L --שחקן ימני", bg="#FAF7F0", font=("Arial", 10))
pong_text3.place(x=950, y=430)
pong_text4 = tkinter.Label(text=" למעלה = W למטה = S --שחקן שמאלי", bg="#FAF7F0", font=("Arial", 10))
pong_text4.place(x=950, y=410)




button_snake = Button(text="Play Snake Game", font=("Arial", 8))
button_snake.config(width=16, height=2, command=snake_game)
button_snake.place(x=100, y=450)

button_usa = Button(text="Play USA Game", font=("Arial", 8))
button_usa.config(width=16, height=2, command=usa_game)
button_usa.place(x=550, y=450)


button_pong = Button(text="Play pong Game", font=("Arial", 8))
button_pong.config(width=16, height=2, command=pong_game)
button_pong.place(x=1000, y=460)

window.mainloop()