#Bibliotheques d'interface
import tkinter
from tkinter import ttk
from tkinter import *
import time
import os

dirname = os.path.dirname(__file__)

window = tkinter.Tk()#Creation d'une fenetre graphique tkinter
window.wm_title("RestoBot App for administrator") #Nom de la fenetre
window.minsize(1280,720) #Dimension minimum
window.maxsize(1500,1000) #Dimension maximum (les deux sont egales, la fenetre n'est pas redimensionnable)

frame = ttk.Frame(window) #La frame est une facon plus pratique de gerer le placement des objets, c'est un "groupement"
frame.pack(fill="both",expand='yes')
robotList = dict()
orderList = dict()
mapList = dict()
interface = dict() #Dictionnaire qui va contenir l'interface non modulaire une fois connecte

OrdersData = [["frite","prep",9],["steak","Delivered",42]]
RobotsData = [["Heron","livraison"],["robotino","prise commande"],["turtlebot_2i","libre"]]

#Affichage du logo de l'entreprise en haut de l'ecran
logo = tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/logo.png')).subsample(2, 2)
interface[0] = ttk.Label(window, image = logo)
interface[0].pack() #Pack est basique mais permet de centrer les objets sans se poser de question

def purge(plist): #La fonction purge permet de vider tout les elements de la frame pour afficher un autre menu
    for i in range(len(plist)):
        plist[i].destroy()

def go_back(): #La fonction go back detruit le bouton pour retourner en arriere et affiche le main
    main()

def entry_point():
    purge(interface)
   
    interface[0] = ttk.Label(frame, image = logo)
    interface[0].pack()
    interface[1] = ttk.Button(frame, text = 'Connexion', command = lambda : go_main())
    interface[1].pack()
    
    interface[2] = ttk.Label(frame, text = '"RestoBot, We go above and beyond the universe for you" - Gerard')
    interface[2].pack(side = 'bottom')
    
def go_main():
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
    interface[3].place(relx=.65, rely=.9)

    interface[4] = fmap
    interface[4].pack(side='top',fill="both")
    MyMap(fmap)   


def update():
    #client.update()
    time.sleep(.2) #Temps de chargement pour que l'update se face


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
    orderList[3*len(OrdersData)].place(relx=.13,rely=.9)
    
def MyRobots(frobot):
    purge(robotList)
    blankspace = "    "
    
    for k in range(len(RobotsData)):
        robotList[k] = ttk.Label(frobot, text = RobotsData[k][0] + blankspace)
        robotList[k+len(RobotsData)] = ttk.Label(frobot, text = RobotsData[k][1]+"  ")
        robotList[k+2*len(RobotsData)] = ttk.Button(frobot, text = "Stat")
        
        robotList[k].grid(row=k,column=0)
        robotList[k+len(RobotsData)].grid(row=k,column=1)
        robotList[k+2*len(RobotsData)].grid(row=k,column=2)
    
    robotList[3*len(RobotsData)] = ttk.Button(frobot, text = "Refresh", command = lambda: MyRobots(frobot))
    robotList[3*len(RobotsData)].place(relx=.13,rely=.9)

def MyMap(fmap):
    map1 = tkinter.PhotoImage(file=os.path.join(dirname, 'app_data/map.png')).subsample(3, 3)
    mapList[0] = ttk.Label(fmap, image = map1)
    mapList[0].pack(fill = "both", expand = "yes")


    mapList[1] = ttk.Button(fmap, text = "Refresh", command = lambda: MyMap(fmap))
    mapList[1].place(relx=.8,rely=.8)
def clear_this(RobotsData,j):
    
    OrdersData = OrdersData[:j] + OrdersData[j+1:]    


entry_point() #Appelle du point d'entree de la fenetre au demarrage

window.mainloop() #Bouclage infini sur la fenetre principale

#client.stop() #On s'assure bien que le client quitte le serveur si il coup brusquement
