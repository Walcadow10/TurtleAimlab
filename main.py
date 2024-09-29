from turtle import Screen, Turtle

from random import randint

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')

def change_position():
    target.hideturtle()
    x = randint(-screen_width, screen_width)
    y = randint(-screen_height, screen_height)
    target.goto(x, y)
    target.showturtle()

score = 0

def update_score():
    global score

    score += 1
    score_keeper.clear()
    score_keeper.write(score, align='center', font=SMALL_FONT)

def update_time():
    time_keeper.undo()
    time_keeper.write(seconds, align='center', font=LARGE_FONT)

def target_clicked(x, y):
    if seconds > 0:
        update_score()
        change_position()

def action():
    global seconds

    seconds -= 1

    if seconds <= 0:
        target.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Süreniz Doldu", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        screen.ontimer(action, 1000)  # 1 second = 1,000 milliseconds

screen = Screen()
screen.bgcolor("White")
screen.setup(width=1.0, height=1.0)
screen.cv._rootwindow.state('zoomed')

screen.title("Aim Geliştirme Uygulaması")
# screen.addshape("ezgif.com-resize.gif")

target = Turtle()
target.penup()
screen_width = screen.window_width() // 2  # Yarı genişlik
screen_height = screen.window_height() // 2  # Yarı yükseklik
x = randint(-screen_width, screen_width)
y = randint(-screen_height, screen_height)
# target.shape("ezgif.com-resize.gif")
target.shape('circle')

score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()

seconds = int(screen.numinput("Zamanlayıcı", "Süreyi Giriniz", minval=0, maxval=59))

time_keeper = score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Kalan Zaman", align='center', font=SMALL_FONT)
time_keeper.sety(300)
time_keeper.write(seconds, align='center', font=LARGE_FONT)

target.onclick(target_clicked)

action()

screen.mainloop()
