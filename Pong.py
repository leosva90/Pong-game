import turtle
 
wn = turtle.Screen() #definiendo wn y pantalla como objeto
wn.title("Pong classic")#nombre
wn.bgcolor("black")#color de fondo de pantalla
wn.setup(width=800, height=600)#tamaño de pantalla
wn.tracer(0)
 
# Paddle A
 
paddle_a = turtle.Turtle()#definiendo paddle_a y Turtle-objeto
paddle_a.speed(0)#no es la velocidad del juego sino de la animacion
paddle_a.shape("square")#forma
paddle_a.color("white")#color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#tamaño
paddle_a.penup()
paddle_a.goto(-350, 0)#posición inicial
 
#Score A
score_a = 0
score_b = 0

 
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
 
# Ball
ball = turtle.Turtle()#definiendo la pelota
ball.speed(0)#velocidad de animación
ball.shape("square")#forma
ball.color("white")#color
ball.penup()
ball.goto(0, 0)#posición
ball.dx = 2#cada vez que nuestra pelota se mueva se va a mover 2 px
ball.dy = -2 

#Tabla de Score
pen = turtle.Turtle() 
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)#ubicación del score
pen.write('Jugador A:0 Jugador B:0', align='center', font=('Courier',24,'normal'))

# Function A
def paddle_a_up(): #definiendo la función
    y = paddle_a.ycor()#paddle_a = objeto
    y += 20 #cuantos px subir
    paddle_a.sety(y)
    
def paddle_a_down(): #definiendo la función
    y = paddle_a.ycor()#paddle_a = objeto
    y -= 20
    paddle_a.sety(y)

# Function B
def paddle_b_up(): #definiendo la función
    y = paddle_b.ycor()#paddle_b = objeto
    y += 20 #cuantos px subir
    paddle_b.sety(y)
    
def paddle_b_down(): #definiendo la función
    y = paddle_b.ycor()#paddle_a = objeto
    y -= 20
    paddle_b.sety(y)
 
 
# Keyboard binding
wn.listen() #escucha cada vez que aprete un boton en el teclado
wn.onkeypress(paddle_a_up, "w")  # llama a la  functio paddle_a_up()
wn.onkeypress(paddle_a_down, "s")  # llama a la  functio paddle_a_down()

wn.onkeypress(paddle_b_up, "Up")  # llama a la  functio paddle_b_up()
wn.onkeypress(paddle_b_down, "Down")  # llama a la  functio paddle_b_down()


# Game loop
while True:
    wn.update()
    
    #movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
 
    #bordes para la pelota parte superior e inferior de la pantalla
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    
        
    #bordes para la pelota parte derecha e iquierda de la pantalla
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1  
        pen.clear() 
        pen.write("Jugador A:{} Jugador B:{}".format(score_a, score_b), align='center', font=('Courier',24,'normal')) 
        
    if ball.xcor() < -390:
         ball.goto(0,0)
         ball.dx *= -1
         score_b +=1   
         pen.clear()
         pen.write("Jugador A: {} Jugador B: {}".format(score_a, score_b), align='center', font=('Courier',24,'normal'))        
         
    #cuando la pelota choca con la pelota
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50): 
         ball.setx(340)
         ball.dx *=-1
         
     
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50): 
         ball.setx(-340)
         ball.dx *=-1     