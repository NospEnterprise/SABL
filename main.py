from tkinter import*
import sqlite3
from row_module import *
root = Tk()
root.resizable(width=False, height=False)

conn=sqlite3.connect('serveur.db')
c=conn.cursor()

def init():
    global f1
    for c in root.winfo_children():
            c.destroy()
    f1=Frame(root,borderwidth=2,relief=GROOVE)
    f1.pack(side=LEFT,padx=10,pady=10)

def user():
    global f1
    init()
    def get_var():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        print(prenom,nom)
        add_user(nom,prenom)
        user()
    entry_nom = StringVar()
    label = Message( f1, text="nom").grid(column=1, row=1)
    label2 = Message( f1, text="prenom", width= 100).grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=1)
    entry_prenom = StringVar()
    passEntry = Entry(f1, textvariable=entry_prenom).grid(column=2, row=2)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil).grid(column=2, row=3)
    interact_box("utilisateur")
    
def responsable():
    global f1
    init()
    def get_var():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        print(prenom,nom)
        add_responsable(nom,prenom)
        responsable()
    entry_nom = StringVar()
    entry_prenom = StringVar()
    label2 = Message( f1, text="nom").grid(column=1, row=1)
    label3 = Message( f1, text="prenom", width= 100).grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_prenom,).grid(column=2, row=2)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil).grid(column=2, row=3)
    interact_box("responsable")

def salle():
    global f1
    init()
    def get_var():
        numero = entry_numero.get()
        etage = entry_etage.get()
        batiment = entry_batiment.get()
        print(numero, etage, batiment)
        add_salle(numero, etage, batiment)
        salle()
    entry_numero = StringVar()
    entry_etage = StringVar()
    entry_batiment = StringVar()
    label2 = Message( f1, text="numero", width= 100).grid(column=1, row=1)
    label3 = Message( f1, text="etage", width= 100).grid(column=1, row=2)
    label4 = Message( f1, text="batiment", width= 100).grid(column=1, row=3)
    passEntry = Entry(f1, textvariable=entry_numero,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_etage,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_batiment,).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil).grid(column=2, row=4)
    interact_box("salle")
def batiment():
    global f1
    init()
    def get_var():
        nomb = nom_batiment.get()
        
        print(nomb)
        add_batiment(nomb)
        batiment()
    nom_batiment = StringVar()
    label = Message( f1, text='nom batiment', width= 100).grid(column=1, row=1)
    passEntry = Entry(f1, textvariable=nom_batiment,).grid(column=2, row=1)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=2)
    submit = Button(f1, text='retour', command=accueil).grid(column=2, row=2)
    interact_box("batiment")
def serrure():
    global f1
    init()
    def get_var():
        ids = idsalle.get()
        
        print(ids)
        add_serrure(ids)
        serrure()
    idsalle = IntVar()
    label = Message( f1, text="id salle", width= 100).grid(column=1, row=1)
    passEntry = Entry(f1, textvariable=idsalle,).grid(column=2, row=1)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil).grid(column=2, row=3)
    interact_box("serrure")

def accueil():
    global f1
    init()
    submit = Button(f1, text='responsable', command=responsable, width= 10).grid(column=1, row=1)
    submit2 = Button(f1, text='serrure', command=serrure,width= 10).grid(column=1, row=2)
    submit3 = Button(f1, text='batiment', command=batiment, width= 10).grid(column=1, row=3)
    submit4 = Button(f1, text='salle', command=salle, width= 10).grid(column=1, row=4)
    submit5 = Button(f1, text='utilisateur', command=user, width= 10).grid(column=1, row=5)
    text2 = Text(root, height=20, width=50, state='normal')
    scroll = Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)

    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#f7b90f',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                   '<1>',
                   lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nSimpleAdministrator\n', 'big')
    quote = """
    Un logiciel de gestion est un logique de pratique
    qui effectue de la gestion de données, c'est-à-dire
    de la manipulation de grande quantité
    d'informations (collecte, classement, exploration,
    recherche) pour les besoins d'une application
    informatique.

    """
    text2.insert(END, quote, 'color')
    text2.insert(END, 'Connecté à "serveur.db" [69 77 76 78 66]\n', 'follow')
    text2.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)
    text2.configure(state = 'disabled')
    
    


def add_salle(numero, etage, batiment):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO salle ('numero', 'etage', 'batiment') VALUES ("+"'"+numero+"'"+","+"'"+etage+"'"+","+"'"+batiment+"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_batiment(idb):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO batiment ('nom') VALUES ("+"'"+ nomb +"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_serrure(ids):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO serrure ('idsalle') VALUES ("+"'"+ str(ids)+"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_responsable(nom,prenom):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO responsable ('nom', 'prenom') VALUES ("+"'" + nom+"'"+","+ "'"+prenom+"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_user(nom,prenom):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO utilisateur ('nom', 'prenom') VALUES ("+"'"+ nom+"'"+","+ "'"+prenom+"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()
def interact_box(table):
    global c
    
    f2=Frame(root)
    f2.pack(side=TOP,padx=10,pady=10)
    
    text2 = Text(f2, height=10, width=50, state='normal')
    scroll = Scrollbar(f2, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)

    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#f7b90f',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                   '<1>',
                   lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nSimpleAdministrator\n', 'big')
    quote = """
    NONE

    """
    text2.insert(END, quote, 'color')
    text2.insert(END, 'Connecté à "serveur.db" [69 77 76 78 66]\n', 'follow')
    text2.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)
    text2.configure(state = 'disabled')
    
    f3=Frame(root,borderwidth=2,relief=GROOVE)
    f3.pack(side=BOTTOM,padx=10,pady=10)
    row(table, f3, c)
    



accueil()
