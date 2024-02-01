import turtle as t
import math

t.up()
t.ht()
t.speed(1000)
t.bgcolor("black")
t.color("white")
t.pensize(4)

number_of_turns = 0

board_list = []
for i in range(5):
    row = [" "] * 5
    board_list.append(row)

buttons = []

#coords = [
#    [(-350, 100 ), (-175, 100 ), (0, 100 ), (165, 100 ), (330, 100 )],
#    [(-350, -8  ), (-175, -8  ), (0, -8  ), (165, -8  ), (330, -8  )],
#    [(-350, -116), (-175, -116), (0, -116), (165, -116), (330, -116)],
#    [(-350, -224), (-175, -224), (0, -224), (165, -224), (330, -224)],
#    [(-350, -332), (-175, -332), (0, -332), (165, -332), (330, -332)]
#]

coords = [[(-350 + j * 175, 100 - i * 108) for j in range(5)] for i in range(5)]

def draw_board():
    t.seth(270)
    for i in range(6):
        t.up()
        t.goto(-430+170*i,200)
        t.down()
        t.fd(540)
        t.up()
    
    
    t.seth(0)
    for i in range(6):
        t.up()
        t.goto(-450,-340+108*i)
        t.down()
        t.fd(890)
        t.up()
    
def click_event(x,y):
    global number_of_turns, board_list
    ans = get_clicked_button_id(x,y)
    if(ans == -1): return
    
    
    bool1 = add_element_in_col(ans)
    if(bool1):
        number_of_turns += 1
        add_element(x,y, ans)

        check = check_win()
        if(check != " "):
            winner = ""
            if(check == "Y"): winner = "Yellow"
            else: winner = "Red"
            t.color("#00FF0F")
            t.up()
            t.goto(0,0)
            t.write(f"{winner} wins!", align="center", font=("Arial", 100, "bold"))
            t.goto(0,-50)
            t.write("Restart te program", align="center", font=("Arial", 40, "bold"))
            t.onscreenclick(None)
    

def add_element(mouse_x, mouse_y, col):
    global coords, number_of_turns, board_list

    for i in range(5):
        if(board_list[i][col] == "R"):
            t.color("red")
            x,y = coords[i][col]
            t.up()
            t.goto(x,y)
            t.begin_fill()
            t.circle(44)
            t.end_fill()
            t.up()
        elif(board_list[i][col] == "Y"):
            t.color("yellow")
            x,y = coords[i][col]
            t.up()
            t.goto(x,y)
            t.begin_fill()
            t.circle(44)
            t.end_fill()
            t.up()
        

def check_win():
    global board_list
    targets = ["R", "Y"]
    
    # Check rows
    for row in board_list:
        for target in targets:
            if row.count(target) >= 4:
                return target
    
    # Check columns
    for j in range(len(board_list[0])):
        column_elements = [board_list[i][j] for i in range(len(board_list))]
        for target in targets:
            if column_elements.count(target) >= 4:
                return target
    
    return " "
        

def add_element_in_col(col):
    global board_list, number_of_turns

    if all (row[col] != " " for row in board_list):
        return False

    for i in range(len(board_list)-1,-1,-1):
        if(board_list[i][col] == " "):
            if(number_of_turns % 2 == 0):
               board_list[i][col] = "R" #R => Red
               return True
            else:
                board_list[i][col] = "Y" #Y => Yellow
                return True
    return True

def get_clicked_button_id(mouse_x, mouse_y):
    global buttons
    for i in range(len(buttons)):
        circle_x, circle_y, radius = buttons[i]
        
        distance = math.sqrt((mouse_x - circle_x)*(mouse_x - circle_x)
                             + (mouse_y - circle_y)*(mouse_y - circle_y))

        if(distance <= radius):
            return i

    return -1

def init_game():
    global buttons
    t.color("#838383")

    for i in range(5):
        buttons.append( (-350+168*i,320, 50) )
        t.goto(-350+168*i,270)
        t.down()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.up()
    
    
    t.color("white")

t.onscreenclick(click_event)
draw_board()
init_game()
