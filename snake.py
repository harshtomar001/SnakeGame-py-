from PIL import Image,ImageTk
import tkinter as tk
import random
SIZE=30
SNAKE_COLOR='#e8206d'
BALL_COLOR="green"
GAME_WIDTH=700
GAME_HEIGHT=650
SPEED=100




score=0


a=0
def start_game(a=False):
    if a==0:
        window.destroy()
    
    def exit():
        root.destroy()
    class Food:
        def __init__(self,canvas,size=SIZE):
            self.canvas=canvas
            self.size=size
            self.coordinates=[]
            self.squares=[]
            x=random.randint(0,int((GAME_WIDTH/self.size)-2))*self.size
            y=random.randint(0,int((GAME_HEIGHT/self.size)-2))*self.size
            self.coordinates.append([x,y])
            a=self.canvas.create_oval(x,y,x+self.size,y+self.size,fill=BALL_COLOR)
            self.squares.append(a)
        



    class  Snake:
        def __init__(self,canvas,size=SIZE):
            self.canvas=canvas
            self.size=size
            self.coordinates=[]
            self.list=[[90,60],[90,60-self.size],[90,60-2*(self.size)]]
            self.squares=[]
            for x,y in  self.list:
                self.coordinates.append([x,y])
                a=self.canvas.create_rectangle(x,y,x+self.size,y+self.size,fill=SNAKE_COLOR,outline='#7d0735')
                self.squares.append(a)
            print(self.squares)
            print(self.coordinates)

    
    root = tk.Tk()
    img = Image.open("cross11.jpg")
    resized = img.resize((40, 25))
    img3 = ImageTk.PhotoImage(resized)

    root.config(bg='#65f7d3')
    root.focus()
    label=tk.Label(root,bd='6',relief='ridge' ,text=f"Loading", bg='pink', width='20',fg='blue', font=('courier new', 40,'bold'))
    label.pack(padx='5', pady='5',expand=True)
    tk.Button(root,text='exit',image=img3,command=exit,bd='6',relief='raised',fg='red').place(relx=1.0, rely=0.0, anchor='ne')
   

    def ready():
        global a
        label.config(text=f"Loading.")
        a+=1
        root.after(500, ready1)

    def ready1():
        global a
        a += 1
        label.config(text=f"Loading..")
        root.after(500,ready2)
    def ready2():
        global a
        a += 1
        label.config(text=f"Loading...")
        if a>5:
            root.after(500,final_call)
        else:
            root.after(500, ready)
    def restart():
        global score
        score=0
        root.destroy()
        start_game(a=True)

    


    def  final_call():

        label.config(text=f"Score:{score}",font=('aerial',20,'bold'))
        
        canvas = tk.Canvas(root,width=GAME_WIDTH,height=GAME_HEIGHT, bd=5, relief="ridge",bg='#b0949f')
        canvas.pack()
        canvas.focus_force()# when we use -fullscreen many os block the focus  so we use the  focus_force

        direction="Down"
        canvas1=Food(canvas)
        canvas2=Snake(canvas)

        def game_over(obj):
            x,y=obj.coordinates[0]
            if x<0 or y<0 or x>GAME_WIDTH or y>GAME_HEIGHT:


                
                return True
            else:
                for i  in obj.coordinates[1:]:
                    if x==i[0] and y ==i[1]:

                        
                        return True
            return False

            root.after(1,lambda:game_over(obj))

        def change_dir(arg):
            nonlocal direction
            #print("hello")
            if arg=='Left':
                if direction!="Right":
                    direction="Left"
            elif arg=="Right":
                if direction!="Left":
                    direction="Right"
            elif arg=="Down":
                if direction!="Up":
                    direction="Down"
            elif arg=="Up":
                if direction!="Down":
                    direction="Up"

        root.bind_all("<Left>", lambda event: change_dir('Left'))
        root.bind_all("<Right>", lambda event: change_dir('Right'))
        root.bind_all("<Up>", lambda event: change_dir('Up'))
        root.bind_all("<Down>", lambda event: change_dir('Down'))

        
        def move(obj,food):
            global score
            nonlocal direction
            a=obj.coordinates
            #print(a)
            x,y=canvas2.coordinates[0]
            if direction=='Down':
                y+=SIZE
            elif direction=='Up':
                y-=SIZE
            elif direction=='Right':
                x+=SIZE
            elif direction=='Left':
                x-=SIZE
            square=canvas.create_rectangle(x,y,x+SIZE,y+SIZE,fill=SNAKE_COLOR,outline='#7d0735')
            obj.coordinates.insert(0,(x,y))
            obj.squares.insert(0,square)

            if x==food.coordinates[0][0] and y==food.coordinates[0][1]:


                del food.coordinates[-1]
                canvas.delete(food.squares[-1])
                del food.squares[-1]
                food=Food(canvas)
                score+=10
                label.config(text=f"Score:{score}")
            else:
                del obj.coordinates[-1]

                canvas.delete(obj.squares[-1])# obj.squares give rectangle id  to  delete 

                del obj.squares[-1]# also delete from the  squares list if not given then last one is already delete but her it will not update hence only one will delete
            if game_over(obj):
                canvas.delete('all')
                canvas.create_text(GAME_WIDTH//2,(GAME_HEIGHT//2)-40,text="Game over!", font=('Helvetica', 25,' bold'),fill='red',anchor='center')

                restart_btn = tk.Button(
                    root,
                    text="Restart",
                    width=15,
                    height=2,
                    font=('Arial', 14, 'bold'),
                    bg='lightgreen',
                    command=restart
                )

                canvas.create_window(
                    GAME_WIDTH // 2,
                    GAME_HEIGHT // 2 + 30,
                    window=restart_btn,
                    anchor='center'
                )
            else:
                root.after(SPEED,lambda:move(obj,food))# for speed of snake   and recall the function
        move(canvas2,canvas1)
        game_over(canvas2)



    root.after(500,ready1)
    root.attributes("-fullscreen",1)
    #root.update()
    root.mainloop()




def close_game():
    window.destroy()

window=tk.Tk()
img1=tk.PhotoImage(file="snake_game.png").subsample(6,6)
img2=tk.PhotoImage(file="cross.png").subsample(6,7)

window.title("Snake Game")
window.config(bg='light green')
window.attributes('-fullscreen',True)
button=tk.Button(window,text="Start Game" ,image=img1,command=start_game,compound='top',borderwidth='5'
             ,bg='green',fg='blue')
button.pack(padx='10',pady='10',expand=True)
button1=tk.Button(window,text="Close" ,image=img2,compound='top',command=close_game,
             fg='red')
button1.pack(padx='10',pady='10',expand=True)
window.mainloop()
