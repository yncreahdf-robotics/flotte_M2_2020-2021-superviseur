#Bibliotheques d'interface
import tkinter
from tkinter import ttk
from tkinter import *
import time
import os
import random as rd

dirname = os.path.dirname(__file__)

window = tkinter.Tk()#Creation d'une fenetre graphique tkinter
window.wm_title("RestoBot App for administrator") #Nom de la fenetre
window.minsize(1537,832) #Dimension minimum
window.maxsize(1537,832) #Dimension maximum (les deux sont egales, la fenetre n'est pas redimensionnable)

frame = ttk.Frame(window) #La frame est une facon plus pratique de gerer le placement des objets, c'est un "groupement"
frame.pack(fill="both",expand='yes')
robotList = dict()
orderList = dict()
mapList = dict()
interface = dict() #Dictionnaire qui va contenir l'interface non modulaire une fois connecte


OrdersData = [["frite","prep",9],["steak","Delivered",42]]
RobotsData = [["Heron","service","occupe"],["Robotino","service","batterie"],["turtlebot_2i","service","libre"],["Nyrio","preparateur","libre"],["Nyrio","preparateur","occupe"],["accueil","accueil","libre"]]

#Affichage du logo de l'entreprise en haut de l'ecran
logo = tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/logo.png'))

def purge(plist): #La fonction purge permet de vider tout les elements de la frame pour afficher un autre menu
    for i in range(len(plist)):
        if(not isinstance(plist[i],int)):
            plist[i].destroy()

def entry_point():
    purge(interface)
   
    interface[0] = ttk.Label(frame, image = logo)
    interface[0].pack()
    interface[1] = ttk.Button(frame, text = 'Connexion', command = lambda : main())
    interface[1].pack()
    
    interface[2] = ttk.Label(frame, text = '"RestoBot, We go above and beyond the universe for you" - Gerard')
    interface[2].pack(side = 'bottom')
    
def main():
    purge(interface)
    
    UserData = "RestoBot"#client.GetUserData()
        
    #Affichage du message de bienvenue
    welcomsg = "Bienvenue dans l'interface de controle du " + UserData + "!"
    interface[0] = ttk.Label(frame, text = welcomsg)
    interface[0].pack()

    #Bouton avec sa frame pour le menu des commandes
    forder= LabelFrame(frame, text="Liste des comandes", padx=20, pady=20)
    frobot= LabelFrame(frame, text="Liste de robot", padx=20, pady=20)
    fmap= LabelFrame(frame, text="Map", padx=20, pady=20)
    
    interface[1] = frobot
    interface[1].pack(side='left',fill="both")
    MyRobots(frobot)
    
    interface[2] = forder
    interface[2].pack(side='right',fill="both")
    MyOrders(forder)

    interface[3] = ttk.Button(frame, text = "Disconnect", command = lambda : entry_point())
    interface[3].place(relx=.65, rely=.95)

    interface[4] = fmap
    interface[4].pack(side='top',fill="both")
    MyMap(fmap)   


def MyOrders(forder):
    purge(orderList)
    blankspace = "           "
    
    for k in range(len(OrdersData)):
        orderList[k] = ttk.Label(forder, text = OrdersData[k][0] + blankspace)
        orderList[k+len(OrdersData)] = ttk.Label(forder, text = OrdersData[k][1]+"  ")
        if OrdersData[k][1] != "Delivered": #Si l'objet n'est pas encore livre, on ne peut pas le sortir de l'historique
            orderList[k+2*len(OrdersData)] = ttk.Button(forder, text = "Please wait")
        else:
            orderList[k+2*len(OrdersData)] = ttk.Button(forder, text = "Forget this", command = lambda a=k: clear_this(OrdersData,a))
        
        orderList[k].grid(row=k,column=0)
        orderList[k+len(OrdersData)].grid(row=k,column=1)
        orderList[k+2*len(OrdersData)].grid(row=k,column=2)
    
    orderList[3*len(OrdersData)] = ttk.Button(forder, text = "Refresh", command = lambda: MyOrders(forder))
    orderList[3*len(OrdersData)].place(relx=.7,rely=.98)
    
def MyRobots(frobot):
    purge(robotList)
    blankspace = "    "
    
    for k in range(len(RobotsData)):
        robotList[k] = ttk.Label(frobot, text = RobotsData[k][0] + blankspace)
        imRob=tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/'+RobotsData[k][1]+'.png')).subsample(3, 3)
        robotList[k+len(RobotsData)] = ttk.Label(frobot, image=imRob)
        robotList[k+len(RobotsData)].image = imRob
        robotList[k+2*len(RobotsData)] = ttk.Label(frobot, text = RobotsData[k][2]+"  ")
        robotList[k+3*len(RobotsData)] = ttk.Button(frobot, text = "Stat", command = lambda k=k: StatRobot(frobot,k))
        
        robotList[k].grid(row=k,column=0)
        robotList[k+len(RobotsData)].grid(row=k,column=1)
        robotList[k+2*len(RobotsData)].grid(row=k,column=2)
        robotList[k+3*len(RobotsData)].grid(row=k,column=3)

    b=len(robotList)
    robotList[b] = ttk.Button(frobot, text = "Refresh", command = lambda: MyRobots(frobot))
    robotList[b].place(relx=.01,rely=.98)

def StatRobot(frobot,k):
    purge(robotList)

    robotList[0] = ttk.Label(frobot, text = RobotsData[k][0])
    robotList[0].pack()

    imRob=tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/'+RobotsData[k][0]+'.png')).subsample(2, 2)
    robotList[1] = ttk.Label(frobot, image=imRob)
    robotList[1].image = imRob
    robotList[1].pack()

    robotList[2] = ttk.Label(frobot, text = "Type :   "+RobotsData[k][1])
    robotList[2].pack()

    robotList[3] = ttk.Label(frobot, text = "Etat :   "+RobotsData[k][2])
    robotList[3].pack()
    
    robotList[4] = ttk.Button(frobot, text = "Retour", command = lambda: MyRobots(frobot))
    robotList[4].place(relx=.01,rely=.98)

    
def MyMap(fmap):
    purge(mapList)
    
    map1 = tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/map.png')).zoom(2, 2)
    map1= map1.subsample(3,3)
    wi=map1.width()
    hi=map1.height()
    mapList[0] = Canvas(fmap,width=wi, height=hi)
    mapList[0].create_image(0, 0, anchor=NW, image=map1)
    mapList[0].image = map1
    mapList[0].pack(fill = "both", expand = "yes")

    color={'batterie':'red','libre':'green','occupe':'blue',}

    for i in range(len(RobotsData)):
        c=color.get(RobotsData[i][2],'black')
        x,y=rd.randint(0,wi),rd.randint(0,hi)
        mapList[2*i+1] = mapList[0].create_oval(x, y, x+10, y+10, outline=c, fill=c)
        mapList[2*i+2] = mapList[0].create_text(x-1-2*len(RobotsData[i][0]), y+8, anchor="nw",text=RobotsData[i][0])

    f=len(mapList)    
    mapList[f] = ttk.Button(fmap, text = "Refresh", command = lambda: MyMap(fmap))
    mapList[f].place(relx=.9,rely=.95)

def clear_this(data,j):   
      orderList[j].destroy()
      orderList[j+len(data)].destroy()
      orderList[j+2*len(data)].destroy()

def move(event):
    "Move the sprite image"
    if event.keysym == 'q':
        mapList[0].move(mapList[1], -10, 0)
        mapList[0].move(mapList[2], -10, 0)
    elif event.keysym == 'd':
        mapList[0].move(mapList[1], 10, 0)
        mapList[0].move(mapList[2], 10, 0)
    elif event.keysym == 'z':
        mapList[0].move(mapList[1], 0, -10)
        mapList[0].move(mapList[2], 0, -10)
    elif event.keysym == 's':
        mapList[0].move(mapList[1], 0, 10)
        mapList[0].move(mapList[2], 0, 10)
    elif event.keysym == 'Left':
        mapList[0].move(mapList[3], -10, 0)
        mapList[0].move(mapList[4], -10, 0)
    elif event.keysym == 'Right':
        mapList[0].move(mapList[3], 10, 0)
        mapList[0].move(mapList[4], 10, 0)
    elif event.keysym == 'Up':
        mapList[0].move(mapList[3], 0, -10)
        mapList[0].move(mapList[4], 0, -10)
    elif event.keysym == 'Down':
        mapList[0].move(mapList[3], 0, 10)
        mapList[0].move(mapList[4], 0, 10)

entry_point() #Appelle du point d'entree de la fenetre au demarrage

window.bind("<Key>", move)
window.mainloop() #Bouclage infini sur la fenetre principale

#client.stop() #On s'assure bien que le client quitte le serveur si il coup brusquement
