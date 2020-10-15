#Bibliotheques d'interface
import tkinter
from tkinter import ttk
from tkinter import *
import time

window = tkinter.Tk()#Creation d'une fenetre graphique tkinter
window.wm_title("RestoBot App for customers") #Nom de la fenetre
window.minsize(500,750) #Dimension minimum
window.maxsize(500,750) #Dimension maximum (les deux sont egales, la fenetre n'est pas redimensionnable)

#Affichage du logo de l'entreprise en haut de l'ecran
#logo = tkinter.PhotoImage(file='C:/Users/theot/Pictures/Hazbin_hotel.jpg')
#Logo = ttk.Label(window, image = logo)
#Logo.pack() #Pack est basique mais permet de centrer les objets sans se poser de question

frame = ttk.Frame(window) #La frame est une facon plus pratique de gerer le placement des objets, c'est un "groupement"
frame.place(relx=.1,rely=.3) #place de la frame relatif a la taille de la fenetre

objects = dict() #Dictionnaire qui va contenir les differents objets de la frame
interface = dict() #Dictionnaire qui va contenir l'interface non modulaire une fois connecte

OrdersData = [["frite","prep",9],["steak","Delivered",42]]
ShopData = ["RestoBot"]

def purge(): #La fonction purge permet de vider tout les elements de la frame pour afficher un autre menu
    for i in range(len(objects)):
        objects[i].destroy()

def go_back(): #La fonction go back detruit le bouton pour retourner en arriere et affiche le main
    main()

def entry_point():
    purge()
    for i in range(len(interface)):
        interface[i].destroy()
        
    for i in range(5):
        interface[i] = ttk.Label(window, text = ' ')
        interface[i].pack()
    interface[5] = ttk.Button(window, text = 'Log in', command = lambda : go_main())
    interface[5].pack()
    
    interface[6] = ttk.Label(window, text = '"RestoBot, We go above and beyond the universe for you" - Gerard')
    interface[6].pack(side = 'bottom')
    
def go_main():
    purge()
    for i in range(len(interface)):
        interface[i].destroy()
    
    #time.sleep(2) #Sleep le temps que la mise a jour des donnees se fassent
    
    UserData = "test toto"#client.GetUserData()
        
    #Affichage du message de bienvenue
    welcomsg = "Welcome to our service dear " + UserData + "!"
    interface[0] = ttk.Label(window, text = welcomsg)
    interface[0].pack()

    #Bouton avec sa frame pour le menu des commandes
    interface[1] = ttk.Label(window, text = ' ')
    interface[1].pack() 
    interface[2] = ttk.Button(window, text = "My Orders", command = lambda: Myorders())
    interface[2].pack()
    
    interface[3] = ttk.Button(window, text = "Disconnect", command = lambda : entry_point())
    interface[3].place(relx=.7, rely=.9)
    
    main()

def update():
    #client.update()
    time.sleep(.2) #Temps de chargement pour que l'update se face
    main()

def main(): #Le maine est le menu d'entree, il permer d'afficher tout les autres
    purge()
    interface[6].destroy()
    interface[6] = ttk.Label(window, text = ShopData[0]+"!" )
    interface[6].pack()

def Myorders():
    purge()
    blankspace = "                    "
    separator = " . . . . . . . . . ."
    
    for k in range(len(OrdersData)):
        objects[k] = ttk.Label(frame, text = OrdersData[k][0] + separator)
        objects[k+len(OrdersData)] = ttk.Label(frame, text = OrdersData[k][1] + blankspace)
        if OrdersData[k][1] != "Delivered": #Si l'objet n'est pas encore livre, on ne peut pas le sortir de l'historique
            objects[k+2*len(OrdersData)] = ttk.Button(frame, text = "Please wait")
        else:
            objects[k+2*len(OrdersData)] = ttk.Button(frame, text = "Forget this", command = lambda a=k: clear_this(OrdersData,a))
        
        objects[k].grid(row=k,column=0)
        objects[k+len(OrdersData)].grid(row=k,column=1)
        objects[k+2*len(OrdersData)].grid(row=k,column=2)
    
    objects[3*len(OrdersData)] = ttk.Button(window, text = "Back", command = lambda: go_back())
    objects[3*len(OrdersData)].place(relx=.13,rely=.9)   
    
        
def clear_this(OrdersData,j):
    
    OrdersData = OrdersData[:j] + OrdersData[j+1:]    


entry_point() #Appelle du point d'entree de la fenetre au demarrage

window.mainloop() #Bouclage infini sur la fenetre principale

#client.stop() #On s'assure bien que le client quitte le serveur si il coup brusquement
