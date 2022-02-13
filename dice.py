from tkinter import*
from PIL import ImageTk, Image
from random import*

root = Tk()
root.title('DICE ROLL SIMULATOR')
#root.attributes('-fullscreen', True)
root.geometry("1500x1500")
canvas = Canvas(root,bg='black')
canvas.pack(fill="both", expand=True)
bg = ImageTk.PhotoImage(file="C:\\Users\\HP\\Pictures\\Saved Pictures\\88f3ea76-9a91-4e55-bb2d-65e35814f6a8.jpg")
canvas_bg = canvas.create_image(420,150,image= bg, anchor = "nw")
canvas_text = canvas.create_text(300, 100, text='', fill = "#30D5C8", font =("GEORGIA", 30,"bold"), anchor=NW)

test_string = "WELCOME TO DICE ROLL SIMULATOR!"
#Time delay between chars, in milliseconds
delta = 70 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta
    
def resizer(e):
    global bg1,resized_bg,new_bg
    #open our image
    bg1=Image.open("C:\\Users\\HP\\Pictures\\Saved Pictures\\88f3ea76-9a91-4e55-bb2d-65e35814f6a8.jpg")
    #resize the image
    resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS)
    #define our image again
    new_bg=ImageTk.PhotoImage(resized_bg)

root.bind('<Configure>',resizer)
def createnewWindow():
    newWindow=Toplevel(root,bg="purple")
    newWindow.geometry("700x200")
    my_label= Label(newWindow, text="1.Click on 'START' button.\n2.Add your name in the input box.\n3.Press enter key.\n4.Click on 'ROLL DICE' button.\n5.If the sum on both the dices comes out to be even, 'YOU WIN'.\n6.Otherwise, 'YOU LOOSE', play again! ",fg="black",bg="purple",font=("Georgia",15))
    my_label.grid(row=0,column=0)
    
    
my_button1 = Button (root,text="Instructions",borderwidth=00,padx=5,pady=0,font=("Calibri",20,"underline"),bg="black", fg="lightgreen",command=createnewWindow)
my_button1_window=canvas.create_window(5,5,anchor="nw",window=my_button1)


def createWindow1():
    newWindow1=Toplevel(root,bg="black")
    newWindow1.geometry("1500x800")
    my_label1=Label(newWindow1, text="You win if you roll an even number",font=("Calibri",20),bg="black", fg="cyan")
    my_label1.pack(pady=50)
    
    # get the dice value
    def get_number(x):
        if x=='\u2680':
            return(1)
        elif x=='\u2681':
            return(2)
        elif x=='\u2682':
            return(3)
        elif x=='\u2683':
            return(4)
        elif x=='\u2684':
            return(5)
        else :
            return(6)
    
    #create a dice list
    dice_list = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
             
    #roll the dice
    def roll_dice():
        d1 = choice(dice_list)
        d2 = choice(dice_list)

        v1 = get_number(d1)
        v2 = get_number(d2)

        #update labels
        dice_label1.config(text=d1)
        dice_label2.config(text=d2)

        #update value labels
        value_label1.config(text=f"Dice 1 = {v1}")
        value_label2.config(text=f"Dice 2 = {v2}")

        #update total label
        total = v1 + v2

        #checking if the player won
        if total%2==0:
            total_label.config(text =f"{total}\nYOU WON!!", fg="blue")
            dice_label1.config(fg = "blue")
            dice_label2.config(fg="blue")
        else:
            total_label.config(text =f"{total}\nYOU LOOSE!,TRY AGAIN", fg="red")
            dice_label1.config(fg="red")
            dice_label2.config(fg="red")
    
    #create buttons
    roll_button = Button(newWindow1, text = "Roll dice", command=roll_dice, font=("calibri",20), padx=5, pady=3,bg = "green",fg="white", activebackground="lightblue")
    roll_button.pack(side=TOP,pady= 20)
    exit_button = Button(newWindow1, text = "Exit", command=quit, font=("calibri",20), padx=10, pady=2,bg = "red",fg="white", activebackground="lightblue")
    exit_button.pack(side=BOTTOM,pady = 20)
    my_label1=Label(newWindow1,text="",bg="black")
    my_label1.pack(pady=20,padx=50)
    
    #create a dice frame
    dice_frame=Frame(newWindow1, bg="black",highlightbackground="green",highlightthickness=3)
    dice_frame.pack(pady=2)
    
#create a total frame
    total_frame=Frame(newWindow1, bg="black",highlightbackground="green",highlightthickness=3)
    total_frame.pack(pady=5)

#create button frame
    button_frame=Frame(newWindow1,bg="black")
    button_frame.pack(pady=10) 
    
#create dice labels
    dice_label1 =Label(dice_frame, text  = "", font=("Helvetica", 100), bg="black", fg = "lightblue")
    dice_label1.grid(row=0,column=0, padx = 100, pady = 25)
    value_label1 = Label(dice_frame, text = "", bg="black", fg="lightblue", font=("calibri", 15))
    value_label1.grid(row=1,column=0, padx = 5,pady=8)
    
    dice_label2 =Label(dice_frame, text  = "", font=("Helvetica", 100), bg="black", fg = "lightblue")
    dice_label2.grid(row=0,column=1, padx = 100, pady=8)
    value_label2 =Label(dice_frame, text = "", bg="black", fg="lightblue",font=("calibri", 15))
    value_label2.grid(row=1,column=1, padx = 5, pady=8)

# print total on screen
    total_label =Label(total_frame, text = "SUM OF DICE", font=("calibri", 24), bg = "black", fg="lightblue")
    total_label.pack(padx=72, pady=20)
     
start_btn=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Pictures\\Saved Pictures\\a0c871cf-3fd6-4571-9ee7-fd65054facd8.jpg"))

img_label =Label(image=start_btn,bg="black")

my_button = Button(root,image=start_btn,borderwidth=00,bg="black",command=createWindow1)
my_button_window=canvas.create_window(850,600,anchor="se",window=my_button)

root.mainloop()
