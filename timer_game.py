# template for "Stopwatch: The Game"
import simplegui
# define global variables

interval = 100
time = 0
time_final ="0:00.0"
x, y = 0, 0
timer_stop = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time_final
    ones = t % 10
    x = (t - ones) / 10 
    tens = x % 60
    thousands = x / 60
    if tens < 10:
        tens = str(0)+str(tens)
        time_final = str(thousands)+':'+tens+'.'+str(ones)
    else:
        time_final = str(thousands)+':'+str(tens)+'.'+str(ones)
    return time_final
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    format(time)
    
def Start():
    global timer_stop
    timer.start()
    timer_stop = False
    
def Stop():
    global time, x, y, timer_stop
    timer.stop()
    if (timer_stop == False):
        y += 1
        if (time % 10) == 0:
            x +=1
    timer_stop = True

def Restart():
    global time, timer_stop, x, y
    timer.stop()
    time = 0
    x = 0
    y = 0 
    timer_stop = False

# define draw handler
def draw_handler(canvas):
    global time, x, y
    format(time)
    attmpt = (str(x)+'/'+str(y))
    canvas.draw_text(time_final, (140, 150), 24, 'Red')
    canvas.draw_text(attmpt, (250, 40), 24, 'Red')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', Start, 60)
button2 = frame.add_button('Stop', Stop, 60)
button3 = frame.add_button('Restart', Restart, 60)

# start frame
frame.start()

# Please remember to review the grading rubric
