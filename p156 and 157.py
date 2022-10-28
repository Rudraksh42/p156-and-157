
#https://www.loom.com/share/19e0a58755f249d98e5c19b5874d0eda


#Basic Format
from tkinter import *
from PIL import ImageTk,Image 
import random


root = Tk()
root.title("Pokemon Card Battle")
root.geometry("700x700")
root.configure(bg = "coral2")

#Image

img = ImageTk.PhotoImage(Image.open("button.jpg"))

img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("6.jpg"))
img7 = ImageTk.PhotoImage(Image.open("7.jpg"))
img8 = ImageTk.PhotoImage(Image.open("8.jpg"))
img9 = ImageTk.PhotoImage(Image.open("9.jpg"))
img10 = ImageTk.PhotoImage(Image.open("10.jpg"))
img11 = ImageTk.PhotoImage(Image.open("11.jpg"))
img12 = ImageTk.PhotoImage(Image.open("12.jpg"))
img13 = ImageTk.PhotoImage(Image.open("13.jpg"))
pokemon_list= [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13]
power_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]

#Player 1
player1 = Label(root , text = "Player 1" , bg = "deep sky blue" , font = 15)
player1.place(relx = 0.1 , rely = 0.2 , anchor=CENTER)
player1_score = Label(root ,text= "" , bg = "turquoise" , fg = "grey1", font = 15)
player1_score.place(relx = 0.1 , rely = 0.3 , anchor=CENTER)

#Player 2
player2 = Label(root , text = "Player 2" , bg = "deep sky blue", font = 15 )
player2.place(relx = 0.9 , rely = 0.2 , anchor=CENTER)
player2_score = Label(root ,text= "" , bg = "turquoise" , fg = "grey1", font = 15)
player2_score.place(relx = 0.9 , rely = 0.3 , anchor=CENTER)

#Center Image
pokemon= Label(root , image = img1)
pokemon.place(relx = 0.5 , rely = 0.4 , anchor=CENTER)




#functions
score1 = 0 
def player1_random():
    global score1
    ran1 = random.randint(0,12)
    print(ran1)
    random_pokemon = pokemon_list[ran1]
    pokemon["image"] = random_pokemon
    power_point = power_list[ran1]
    print( power_point )
    score1 = score1 +  power_point
    player1_score["text"] = str(score1)
    
    
score2 = 0 
def player2_random():
    global score2
    ran2 = random.randint(0,12)
    print(ran2)
    random_pokemon1 = pokemon_list[ran2]
    pokemon["image"] = random_pokemon1  
    power_point2 = power_list[ran2]
    print(power_point2)
    score2 = score2 + power_point2
    player2_score["text"] = str(score2)
    

    
  
    

#Buttons   
btn1 = Button(root, image=img , bg= "coral2" , command = player1_random)
btn1.place(relx = 0.1 , rely = 0.5 , anchor = CENTER)

    
btn2 = Button(root, image=img , bg= "coral2" ,command = player2_random )
btn2.place(relx = 0.9 , rely = 0.5 , anchor = CENTER )


root.mainloop()