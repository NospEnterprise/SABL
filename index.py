from tkinter import *
from tkinter.messagebox import *
import sqlite3

root=Tk()
root.configure(background='#D8D8DA', borderwidth=5, relief=RIDGE)
root.resizable(width=False, height=False)

conn=sqlite3.connect('serveur.db')
c=conn.cursor()

#initialisation pour l'ouverture d'un nouveau menu
def init():
    global f1
    for c in root.winfo_children():
            c.destroy()
    f1=Frame(root,borderwidth=2,relief=GROOVE)
    f1.pack(side=LEFT,padx=10,pady=10)

#les fonctions de suppressions requiert des entrées pour s'assurer de supprimer le(s) bon(s) element(s)
def horaire_del():
    global f1
    init()
    
    def get_var():
        idh = entry_id.get()
        heure_d = entry_depart.get()
        heure_f = entry_fin.get()
        jour = entry_jour.get()
        salle = entry_salle.get()
        print("Suppression de :", idh, heure_d, heure_f, jour, salle)
        del_horaire(idh, heure_d, heure_f, jour, salle)
        horaire_del()
    
    entry_id = StringVar()
    entry_depart = StringVar()
    entry_fin = StringVar()
    entry_jour = StringVar()
    entry_salle = StringVar()
    label = Label( f1, text="id").grid(column=1, row=1)
    label2 = Label( f1, text="heure de\ndépart").grid(column=1, row=2)
    label3 = Label( f1, text="heure de\nfin").grid(column=1, row=3)
    label4 = Label( f1, text="jour").grid(column=1, row=4)
    label5 = Label( f1, text="salle").grid(column=1, row=5)
    passEntry = Entry(f1, textvariable=entry_id,).grid(column=2, row=1, padx=5)
    passEntry = Entry(f1, textvariable=entry_depart).grid(column=2, row=2, padx=5)
    passEntry = Entry(f1, textvariable=entry_fin).grid(column=2, row=3, padx=5)
    passEntry = Entry(f1, textvariable=entry_jour).grid(column=2, row=4, padx=5)
    passEntry = Entry(f1, textvariable=entry_salle).grid(column=2, row=5, padx=5)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=6)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=6)
    interact_box("horaire", "Ici vous pouvez supprimer les permissions d'accès accordées  aux utilisateurs et voir celles deja   presentes")

def user_del():
    global f1
    init()
    
    def get_var():
        idu = entry_id.get()
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        print("Suppression de l'utilisateur :",idu,nom,prenom)
        del_user(idu,nom,prenom)
        user_del()
    
    entry_nom = StringVar()
    entry_prenom = StringVar()
    entry_id = StringVar()
    label = Label( f1, text="id").grid(column=1, row=1)
    label = Label( f1, text="nom").grid(column=1, row=2)
    label2 = Label( f1, text="prenom").grid(column=1, row=3)
    passEntry = Entry(f1, textvariable=entry_id,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_prenom).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=4)
    interact_box("utilisateur", "Ici vous pouvez supprimer les utilisateurs et voir ceux deja présent")
    
def responsable_del():
    global f1
    init()
    
    def get_var():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        idr = entry_id.get()
        print(prenom,nom, idr)
        del_responsable(nom,prenom, idr)
        responsable_del()
    
    entry_nom = StringVar()
    entry_prenom = StringVar()
    entry_id = StringVar()
    label = Label( f1, text="id (commençant par '*' pour un responsable)").grid( column=1, row=3)
    label2 = Label( f1, text="nom").grid(column=1, row=1)
    label3 = Label( f1, text="prenom").grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_prenom,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_id,).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=4)
    interact_box("responsable", "Ici vous pouvez supprimer les responsables et voir ceux deja présents")

def salle_del():
    global f1
    init()
    
    def get_var():
        numero = entry_numero.get()
        etage = entry_etage.get()
        batiment = entry_batiment.get()
        print(numero, etage, batiment)
        del_salle(numero, etage, batiment)
        salle_del()
    
    entry_numero = StringVar()
    entry_etage = StringVar()
    entry_batiment = StringVar()
    label2 = Label( f1, text="numero").grid(column=1, row=1)
    label3 = Label( f1, text="etage").grid(column=1, row=2)
    label4 = Label( f1, text="batiment").grid(column=1, row=3)
    passEntry = Entry(f1, textvariable=entry_numero,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_etage,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_batiment,).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=4)
    interact_box("salle", "Ici vous pouvez supprimer les salles et voir      celles deja présentes")
    
def batiment_del():
    global f1
    init()
    
    def get_var():
        idb = id_batiment.get()
        
        print(idb)
        del_batiment(idb)
        batiment_del()
    
    id_batiment = StringVar()
    label = Label( f1, text='id du batiment').grid(column=1, row=1)
    passEntry = Entry(f1, textvariable=id_batiment,).grid(column=2, row=1)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=2)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=2)
    interact_box("batiment", "Ici vous pouvez supprimer les batiments et voir   ceux deja présents")
    
def serrure_del():
    global f1
    init()
    
    def get_var():
        ids = idsalle.get()
        idsu = idserrure.get()
        
        print(ids, idsu)
        del_serrure(ids, idsu)
        serrure_del()
    idsalle = StringVar()
    idserrure = StringVar()
    label = Label( f1, text="id salle").grid(column=1, row=1)
    label = Label( f1, text="id serrure").grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=idsalle,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=idserrure,).grid(column=2, row=2)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil_del).grid(column=2, row=3)
    interact_box("serrure", "Ici vous pouvez supprimer les serrures et voir    celles deja présentes")

def accueil_del():
    global f1
    init()
    root.title("Interface Administrateur - Suppression d'élément")
    f4=Frame(root,borderwidth=2,relief=GROOVE)
    f4.pack(side=BOTTOM,padx=10,pady=10)
    submit = Button(f1, text='responsable', command=responsable_del, width= 10).grid(column=1, row=1)
    submit2 = Button(f1, text='serrure', command=serrure_del,width= 10).grid(column=1, row=2)
    submit3 = Button(f1, text='batiment', command=batiment_del, width= 10).grid(column=1, row=3)
    submit4 = Button(f1, text='salle', command=salle_del, width= 10).grid(column=1, row=4)
    submit5 = Button(f1, text='utilisateur', command=user_del, width= 10).grid(column=1, row=5)
    submit6 = Button(f1, text='accès', command=horaire_del, width= 10).grid(column=1, row=6)
    button = Button(f4, text='Retour', command=main_menu, width = 10).pack(side=LEFT)
    button = Button(f4, text='Quitter', command=close, width = 10).pack(side=RIGHT)
    text2 = Text(root, height=20, width=50, state='normal')

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
    text2.pack(side=LEFT, padx=10, pady=5)
    text2.configure(state = 'disabled')

# des messages de verifications sont affichés pour s'assurer que l'utilisateur souhaite bien
#supprimer la ligne entrée, les suppressions liées à celle demandées sont également signalées et la suppression est confirmée

def del_horaire(idh, heure_d, heure_f, jour, salle):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    for ligne in c.execute("SELECT * FROM utilisateur WHERE id="+idh+";"):
        nom = ligne[1]
        prenom = ligne[2]
    if askokcancel('Etes vous sûr ?', 'Voulez-vous retirer le droit à '+nom+', '+prenom+", d'entrer dans la salle numéro "+salle+" le "+jour+" de "+heure_d+"h à "+heure_f+"h ? ")==True:
        c.execute("DELETE FROM horaire WHERE id='"+idh+"' AND heure_d='"+heure_d+"' AND heure_f='"+heure_f+"' AND jour='"+jour+"' AND salle='"+salle+"';")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

#La suppression d'une salle supprime touts ses serrures et autorisations pour celle-ci.

def del_salle(numero, etage, batiment):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    for row in c.execute("SELECT id FROM salle WHERE numero='"+numero+"' AND etage='"+etage+"' AND batiment='"+batiment+"' ;"):
        ids = str(row[0])
    if askokcancel('Etes vous sûr ?', "Voulez-vous supprimer la salle numéro "+numero+", de l'etage "+etage+" dans le batiment "+batiment+" de la base de donnée ? Cela entrainera la suppression de toutes les serrures et permissions attachées à celle-ci.")==True:
        c.execute("DELETE FROM serrure WHERE idsalle='"+ids+"';")
        c.execute("DELETE FROM salle WHERE numero='"+numero+"' AND etage='"+etage+"' AND batiment='"+batiment+"' ;")
        c.execute("DELETE FROM horaire WHERE salle='"+ids+"' ;")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

#La suppression d'un batiment supprime les salles de celui-ci, les serrures et autorisations de ces salles

def del_batiment(idb):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    for row in c.execute("SELECT nomb FROM batiment WHERE id='"+idb+"' ;"):
        nomb = str(row[0])
    if askokcancel('Etes vous sûr ?', "Voulez-vous supprimer le batiment numéro "+idb+", nommé : "+nomb+" de la base de donnée ? Cela entrainera la suppression de toutes les salles, serrures et permissions attachées à celui-ci.")==True:
        ids=[]
        for row in c.execute("SELECT id FROM salle WHERE batiment='"+idb+"' ;"):
            ids.append(str(row[0]))
        for i in range(len(ids)):
            c.execute("DELETE FROM serrure WHERE idsalle='"+ids[i]+"';")
            c.execute("DELETE FROM horaire WHERE salle='"+ids[i]+"';")
        c.execute("DELETE FROM salle WHERE batiment='"+idb+"' ;")
        c.execute("DELETE FROM batiment WHERE id='"+idb+"' ;")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

def del_serrure(ids, idsu):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    if askokcancel('Etes vous sûr ?', "Voulez-vous supprimer la serrure numéro "+idsu+" ouvrant la salle numéro "+ids+" de la base de donnée ? ")==True:
        c.execute("DELETE FROM serrure WHERE idsalle='"+ids+"' AND id='"+idsu+"' ;")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

def del_responsable(nom,prenom, idr):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    if askokcancel('Etes vous sûr ?', "Voulez-vous supprimer le responsable "+nom+', '+prenom+", ayant pour identifiant "+idr+" de la base de donnée ? ")==True:
        c.execute("DELETE FROM responsable WHERE id='"+idr+"' AND nom='"+nom+"' AND prenom='"+prenom+"';")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

#la suppression d'un utilisateur supprime egalement tous ses accès

def del_user(idu,nom,prenom):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    if askokcancel('Etes vous sûr ?', "Voulez-vous supprimer l'utilisateur "+nom+', '+prenom+", de la base de donnée ? Cela entrainera la suppression de toutes ses permissions.")==True:
        c.execute("DELETE FROM horaire WHERE id='"+idu+"';")
        c.execute("DELETE FROM utilisateur WHERE id='"+idu+"' AND nom='"+nom+"' AND prenom='"+prenom+"';")
        showinfo('Succès', 'La requète a bien été effectuée.')
    conn.commit()
    conn.close()

#Les ajouts d'éléments necessitent les informations essentielles uniquement(id n'est pas demande si pas besoin par exemple)

def horaire_add():
    global f1
    init()
    
    def get_var():
        idh = entry_id.get()
        heure_d = entry_depart.get()
        heure_f = entry_fin.get()
        jour = entry_jour.get()
        salle = entry_salle.get()
        print(idh, heure_d, heure_f, jour, salle)
        add_horaire(idh, heure_d, heure_f, jour, salle)
        horaire_add()
    entry_id = StringVar()
    entry_depart = StringVar()
    entry_fin = StringVar()
    entry_jour = StringVar()
    entry_salle = StringVar()
    label = Label( f1, text="id").grid(column=1, row=1)
    label2 = Label( f1, text="heure de\ndépart").grid(column=1, row=2)
    label3 = Label( f1, text="heure de\nfin").grid(column=1, row=3)
    label4 = Label( f1, text="jour").grid(column=1, row=4)
    label5 = Label( f1, text="salle").grid(column=1, row=5)
    passEntry = Entry(f1, textvariable=entry_id,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_depart).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_fin).grid(column=2, row=3)
    passEntry = Entry(f1, textvariable=entry_jour).grid(column=2, row=4)
    passEntry = Entry(f1, textvariable=entry_salle).grid(column=2, row=5)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=6)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=6)
    interact_box("horaire", "Ici vous pouvez rajouter des permissions d'accès  aux utilisateurs et voir celles deja présentes")
    
def user_add():
    global f1
    init()
    
    def get_var():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        print(prenom,nom)
        add_user(nom,prenom)
        user_add()
    entry_nom = StringVar()
    label = Label( f1, text="nom").grid(column=1, row=1)
    label2 = Label( f1, text="prenom").grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=1)
    entry_prenom = StringVar()
    passEntry = Entry(f1, textvariable=entry_prenom).grid(column=2, row=2)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=3)
    interact_box("utilisateur", "Ici vous pouvez ajouter les utilisateurs et voir  ceux deja présent")
    
def responsable_add():
    global f1
    init()
    
    def get_var():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        idr = entry_id.get()
        print(prenom,nom, idr)
        add_responsable(nom,prenom, idr)
        responsable_add()
    entry_nom = StringVar()
    entry_prenom = StringVar()
    entry_id = StringVar()
    label = Label( f1, text="id (commençant par '*' pour un responsable)").grid( column=1, row=3)
    label2 = Label( f1, text="nom").grid(column=1, row=1)
    label3 = Label( f1, text="prenom").grid(column=1, row=2)
    passEntry = Entry(f1, textvariable=entry_nom,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_prenom,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_id,).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=4)
    interact_box("responsable", "Vous pouvez ajouter ici des reponsable ou voir ci dessous la liste des responsables deja présent.")

def salle_add():
    global f1
    init()
    
    def get_var():
        numero = entry_numero.get()
        etage = entry_etage.get()
        batiment = entry_batiment.get()
        print(numero, etage, batiment)
        add_salle(numero, etage, batiment)
        salle_add()
    entry_numero = StringVar()
    entry_etage = StringVar()
    entry_batiment = StringVar()
    label2 = Label( f1, text="numero").grid(column=1, row=1)
    label3 = Label( f1, text="etage").grid(column=1, row=2)
    label4 = Label( f1, text="batiment").grid(column=1, row=3)
    passEntry = Entry(f1, textvariable=entry_numero,).grid(column=2, row=1)
    passEntry = Entry(f1, textvariable=entry_etage,).grid(column=2, row=2)
    passEntry = Entry(f1, textvariable=entry_batiment,).grid(column=2, row=3)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=4)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=4)
    interact_box("salle", "Ici vous pouvez ajouter les salles et voir celles deja présentes")
    
def batiment_add():
    global f1
    init()
    
    def get_var():
        nomb = nom_batiment.get()
        
        print(nomb)
        add_batiment(nomb)
        batiment_add()
    nom_batiment = StringVar()
    label = Label( f1, text='nom batiment').grid(column=1, row=1)
    passEntry = Entry(f1, textvariable=nom_batiment,).grid(column=2, row=1)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=2)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=2)
    interact_box("batiment", "Ici vous pouvez ajouter les batiments et voir ceux deja présents")
def serrure_add():
    global f1
    init()
    
    def get_var():
        ids = idsalle.get()
        
        print(ids)
        add_serrure(ids)
        serrure_add()
    idsalle = StringVar()
    label = Label( f1, text="id salle").grid(column=1, row=1)
    passEntry = Entry(f1, textvariable=idsalle,).grid(column=2, row=1)
    submit = Button(f1, text='valider', command=get_var).grid(column=1, row=3)
    submit = Button(f1, text='retour', command=accueil_add).grid(column=2, row=3)
    interact_box("serrure", "Ici vous pouvez ajouter les serrures et voir      celles deja présentes")

def accueil_add():
    global f1
    init()
    root.title("Interface Administrateur - Ajout d'élément")
    f4=Frame(root,borderwidth=2,relief=GROOVE)
    f4.pack(side=BOTTOM,padx=10,pady=10)
    submit = Button(f1, text='responsable', command=responsable_add, width= 10).grid(column=1, row=1)
    submit2 = Button(f1, text='serrure', command=serrure_add,width= 10).grid(column=1, row=2)
    submit3 = Button(f1, text='batiment', command=batiment_add, width= 10).grid(column=1, row=3)
    submit4 = Button(f1, text='salle', command=salle_add, width= 10).grid(column=1, row=4)
    submit5 = Button(f1, text='utilisateur', command=user_add, width= 10).grid(column=1, row=5)
    submit6 = Button(f1, text='accès', command=horaire_add, width= 10).grid(column=1, row=6)
    button = Button(f4, text='Retour', command=main_menu, width = 10).pack(side=LEFT)
    button = Button(f4, text='Quitter', command=close, width = 10).pack(side=RIGHT)
    text2 = Text(root, height=20, width=50, state='normal')

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
    text2.pack(side=LEFT, padx=10, pady=5)
    text2.configure(state = 'disabled')
    
    
def add_horaire(idh, heure_d, heure_f, jour, salle):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO horaire ('id', 'heure_d', 'heure_f', 'jour', 'salle') VALUES ("+"'"+idh+"'"+","+"'"+heure_d+"'"+","+"'"+heure_f+"','"+jour+"','"+salle+"');"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_salle(numero, etage, batiment):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO salle ('numero', 'etage', 'batiment') VALUES ("+"'"+numero+"'"+","+"'"+etage+"'"+","+"'"+batiment+"'"+");"
    print(x)
    c.execute(x)
    conn.commit()
    conn.close()

def add_batiment(nomb):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO batiment ('nomb') VALUES ("+"'"+ nomb +"'"+");"
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

def add_responsable(nom,prenom, idr):
    conn=sqlite3.connect('serveur.db')
    c=conn.cursor()
    x = "INSERT INTO responsable ('nom', 'prenom', 'id') VALUES ("+"'" + nom+"'"+","+ "'"+prenom+"','"+idr+"');"
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

def accueil_mod():
    global f1
    init()
    root.title("Interface Administrateur - Modification d'élément")
    f4=Frame(root,borderwidth=2,relief=GROOVE)
    f4.pack(side=BOTTOM,padx=10,pady=10)
    submit = Button(f1, text='responsable', command=responsable_mod, width= 10).grid(column=1, row=1)
    submit2 = Button(f1, text='serrure', command=serrure_mod,width= 10).grid(column=1, row=2)
    submit3 = Button(f1, text='batiment', command=batiment_mod, width= 10).grid(column=1, row=3)
    submit4 = Button(f1, text='salle', command=salle_mod, width= 10).grid(column=1, row=4)
    submit5 = Button(f1, text='utilisateur', command=user_mod, width= 10).grid(column=1, row=5)
    submit6 = Button(f1, text='accès', command=horaire_mod, width= 10).grid(column=1, row=6)
    button = Button(f4, text='Retour', command=main_menu, width = 10).pack(side=LEFT)
    button = Button(f4, text='Quitter', command=close, width = 10).pack(side=RIGHT)
    text2 = Text(root, height=20, width=50, state='normal')

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
    text2.pack(side=LEFT, padx=10, pady=5)
    text2.configure(state = 'disabled')

#L'utilisation de Listbox permet de scroller dans les listes.

def responsable_mod():
    #Les fonctions yscroll et yview permettent de lier les differentes Listbox pour avoir un scroll general de toutes les listes et conserver l'alignement des listes
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)

    def yview(*args):
        pass
    
    global f1
    init()
    f1.destroy()
    scrollbar = Scrollbar(root, orient='vertical')
    liste_id=Listbox(root, activestyle='dotbox', height = 10, yscrollcommand=yscroll)
    liste_nom=Listbox(root, activestyle='dotbox', height = 10, yscrollcommand=yscroll)
    liste_prenom=Listbox(root, activestyle='dotbox', height = 10, yscrollcommand=yscroll)
    liste = [liste_id, liste_nom, liste_prenom]
    for row in c.execute("SELECT id, nom, prenom FROM responsable"):
        liste_id.insert(END, row[0])
        liste_nom.insert(END, row[1])
        liste_prenom.insert(END, row[2])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='nom :', background='#D8D8DA').grid(column=2, row=0)
    texte=Label(root, text='prenom :', background='#D8D8DA').grid(column=3, row=0)
    liste_prenom.grid(column=3, row=2)
    liste_nom.grid(column=2, row=2)
    liste_id.grid(column=1, row=2)
    scrollbar.grid(column= 4, row = 2, sticky="ns")
    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_nom.get(index))
            ligne.append(liste_prenom.get(index))
            mod_responsable(ligne[0], ligne[1], ligne[2])
        
        identifiant=liste_id.curselection()
        nom=liste_nom.curselection()
        prenom=liste_prenom.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
            go()
        elif nom!=null:
            index=nom
            go()
        elif prenom!=null:
            index=prenom
            go()
            
        
    
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton=Button(root, text='Retour', command=accueil_mod).grid(column=2, row=3)
    
def mod_responsable(identifiant, nom, prenom):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE responsable SET id='"+entry_id.get()+"', nom='"+entry_nom.get()+"', prenom='"+entry_prenom.get()+"' WHERE id='"+identifiant+"' AND nom='"+nom+"' AND prenom='"+prenom+"' ;")
        print("UPDATE responsable SET id='"+entry_id.get()+"', nom='"+entry_nom.get()+"', prenom='"+entry_prenom.get()+"' WHERE id='"+identifiant+"' AND nom='"+nom+"' AND prenom='"+prenom+"' ;")
        conn.commit()
        conn.close()
        mod_responsable(entry_id.get(), entry_nom.get(), entry_prenom.get())
    
    texte=Label(f1, text='id :').grid(column=0, row=0)
    texte=Label(f1, text='nom :').grid(column=1, row=0)
    texte=Label(f1, text='prenom :').grid(column=2, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_nom=StringVar()
    entry_nom.set(nom)
    entry_prenom=StringVar()
    entry_prenom.set(prenom)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_nom=Entry(f1, textvariable=entry_nom).grid(column=1, row=1)
    entree_prenom=Entry(f1, textvariable=entry_prenom).grid(column=2, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=responsable_mod).grid(column=1, row=2)

def serrure_mod():
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)

    def yview(*args):
        pass
    
    global f1
    init()
    f1.destroy()
    scrollbar = Scrollbar(root, orient='vertical')
    scrollbar.grid(column = 3, row = 2, sticky="ns")
    liste_id=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_idsalle=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste = [liste_id, liste_idsalle]
    for row in c.execute("SELECT id, idsalle FROM serrure"):
        liste_id.insert(END, row[0])
        liste_idsalle.insert(END, row[1])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='idsalle :', background='#D8D8DA').grid(column=2, row=0)
    liste_id.configure(height=10)
    liste_id.grid(column=1, row=2)
    liste_idsalle.configure(height=10)
    liste_idsalle.grid(column=2, row=2)
    scrollbar.config(command=yview)


    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_idsalle.get(index))
            mod_serrure(ligne[0], ligne[1])
        
        identifiant=liste_id.curselection()
        idsalle=liste_idsalle.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
            go()
        elif idsalle!=null:
            index=idsalle
            go()
    
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton=Button(root, text='Retour', command=accueil_mod).grid(column=2, row=3)

def mod_serrure(identifiant, idsalle):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE serrure SET id='"+str(entry_id.get())+"', idsalle='"+str(entry_idsalle.get())+"' WHERE id='"+str(identifiant)+"' AND idsalle='"+str(idsalle)+"' ;")
        print("UPDATE serrure SET id='"+str(entry_id.get())+"', idsalle='"+str(entry_idsalle.get())+"' WHERE id='"+str(identifiant)+"' AND idsalle='"+str(idsalle)+"' ;")
        conn.commit()
        conn.close()
        mod_serrure(entry_id.get(), entry_idsalle.get())
    
    texte=Label(f1, text='id :').grid(column=0, row=0)
    texte=Label(f1, text='id_salle :').grid(column=1, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_idsalle=StringVar()
    entry_idsalle.set(idsalle)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_idsalle=Entry(f1, textvariable=entry_idsalle).grid(column=1, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=serrure_mod).grid(column=1, row=2)

def user_mod():
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)

    def yview(*args):
        pass
    
    global f1
    init()
    f1.destroy()
    scrollbar = Scrollbar(root, orient='vertical')
    scrollbar.grid(column = 4, row = 2, sticky="ns")
    liste_id=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_nom=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_prenom=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste = [liste_id, liste_nom, liste_prenom]
    for row in c.execute("SELECT id, nom, prenom FROM utilisateur"):
        liste_id.insert(END, row[0])
        liste_nom.insert(END, row[1])
        liste_prenom.insert(END, row[2])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='nom :', background='#D8D8DA').grid(column=2, row=0)
    texte=Label(root, text='prenom :', background='#D8D8DA').grid(column=3, row=0)
    liste_id.configure(height=10)
    liste_id.grid(column=1, row=2)
    liste_nom.configure(height=10)
    liste_nom.grid(column=2, row=2)
    liste_prenom.configure(height=10)
    liste_prenom.grid(column=3, row=2)
    
    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_nom.get(index))
            ligne.append(liste_prenom.get(index))
            mod_user(ligne[0], ligne[1], ligne[2])
        
        identifiant=liste_id.curselection()
        nom=liste_nom.curselection()
        prenom=liste_prenom.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
        elif nom!=null:
            index=nom
        elif prenom!=null:
            index=prenom
        go()
    
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton = Button(root, text='Retour', command=accueil_mod).grid(column = 2, row=3)

#modifier un utilisateur modifie ses autorisations pour conserver les liens

def mod_user(identifiant, nom, prenom):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE utilisateur SET id='"+str(entry_id.get())+"', nom='"+entry_nom.get()+"', prenom='"+entry_prenom.get()+"' WHERE id='"+str(identifiant)+"' AND nom='"+nom+"' AND prenom='"+prenom+"' ;")
        print("UPDATE utilisateur SET id='"+str(entry_id.get())+"', nom='"+entry_nom.get()+"', prenom='"+entry_prenom.get()+"' WHERE id='"+str(identifiant)+"' AND nom='"+nom+"' AND prenom='"+prenom+"' ;")
        c.execute("UPDATE horaire SET id='"+str(entry_id.get())+"' WHERE id='"+str(identifiant)+"' ;")
        print("UPDATE horaire SET id='"+str(entry_id.get())+"' WHERE id='"+str(identifiant)+"' ;")
        conn.commit()
        conn.close()
        mod_user(entry_id.get(), entry_nom.get(), entry_prenom.get())
    
    texte=Label(f1, text='id :').grid(column=0, row=0)
    texte=Label(f1, text='nom :').grid(column=1, row=0)
    texte=Label(f1, text='prenom :').grid(column=2, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_nom=StringVar()
    entry_nom.set(nom)
    entry_prenom=StringVar()
    entry_prenom.set(prenom)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_nom=Entry(f1, textvariable=entry_nom).grid(column=1, row=1)
    entree_prenom=Entry(f1, textvariable=entry_prenom).grid(column=2, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=user_mod).grid(column=1, row=2)

def salle_mod():
    
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)

    def yview(*args):
        pass
    
    global f1
    init()
    f1.destroy()
    scrollbar = Scrollbar(root, orient='vertical')
    scrollbar.grid(column = 6, row = 2, sticky="ns")
    liste_id=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_numero=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_etage=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_batiment=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste = [liste_id, liste_numero, liste_etage, liste_batiment]
    for row in c.execute("SELECT id, numero, etage, batiment FROM salle"):
        liste_id.insert(END, row[0])
        liste_numero.insert(END, row[1])
        liste_etage.insert(END, row[2])
        liste_batiment.insert(END, row[3])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='numero :', background='#D8D8DA').grid(column=2, row=0)
    texte=Label(root, text='etage :', background='#D8D8DA').grid(column=3, row=0)
    texte=Label(root, text='batiment :', background='#D8D8DA').grid(column=4, row=0)
    liste_id.configure(height=10)
    liste_id.grid(column=1, row=2)
    liste_numero.configure(height=10)
    liste_numero.grid(column=2, row=2)
    liste_etage.configure(height=10)
    liste_etage.grid(column=3, row=2)
    liste_batiment.configure(height=10)
    liste_batiment.grid(column=4, row=2)
        
    
    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_numero.get(index))
            ligne.append(liste_etage.get(index))
            ligne.append(liste_batiment.get(index))
            mod_salle(ligne[0], ligne[1], ligne[2],ligne[3])
        
        identifiant=liste_id.curselection()
        numero=liste_numero.curselection()
        etage=liste_etage.curselection()
        batiment=liste_batiment.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
        elif numero!=null:
            index=numero
        elif etage!=null:
            index=etage
        elif batiment!=null:
            index=batiment
        
        go()
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton = Button(root, text='Retour', command=accueil_mod).grid(column = 2, row=3)

#modifier une salle modifie les serrures et autorisations liées à celle-ci pour conserver les liens existants

def mod_salle(identifiant, numero, etage, batiment):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE salle SET id='"+str(entry_id.get())+"', numero='"+str(entry_numero.get())+"', etage='"+str(entry_etage.get())+"', batiment='"+str(entry_batiment.get())+"' WHERE id='"+str(identifiant)+"' AND numero='"+str(numero)+"' AND etage='"+str(etage)+"' AND batiment='"+str(batiment)+"' ;")
        print("UPDATE salle SET id='"+str(entry_id.get())+"', numero='"+str(entry_numero.get())+"', etage='"+str(entry_etage.get())+"', batiment='"+str(entry_batiment.get())+"' WHERE id='"+str(identifiant)+"' AND numero='"+str(numero)+"' AND etage='"+str(etage)+"' AND batiment='"+str(batiment)+"' ;")
        c.execute("UPDATE serrure SET idsalle='"+str(entry_id.get())+"' WHERE idsalle='"+str(identifiant)+"' ;")
        print("UPDATE serrure SET idsalle='"+str(entry_id.get())+"' WHERE idsalle='"+str(identifiant)+"' ;")
        c.execute("UPDATE horaire SET salle='"+str(entry_id.get())+"' WHERE salle='"+str(identifiant)+"' ;")
        print("UPDATE horaire SET salle='"+str(entry_id.get())+"' WHERE salle='"+str(identifiant)+"' ;")
        conn.commit()
        conn.close()
        mod_salle(entry_id.get(), entry_numero.get(), entry_etage.get(), entry_batiment.get())
    
    texte=Label(f1, text='id :', background='#D8D8DA').grid(column=0, row=0)
    texte=Label(f1, text='numero :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(f1, text='etage :', background='#D8D8DA').grid(column=2, row=0)
    texte=Label(f1, text='batiment :', background='#D8D8DA').grid(column=3, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_numero=StringVar()
    entry_numero.set(numero)
    entry_etage=StringVar()
    entry_etage.set(etage)
    entry_batiment=StringVar()
    entry_batiment.set(batiment)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_numero=Entry(f1, textvariable=entry_numero).grid(column=1, row=1)
    entree_etage=Entry(f1, textvariable=entry_etage).grid(column=2, row=1)
    entree_batiment=Entry(f1, textvariable=entry_batiment).grid(column=3, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=salle_mod).grid(column=1, row=2)

def horaire_mod():
    global f1
    init()
    f1.destroy()
    
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)
    
    def yview(*args):
        pass
    
    scrollbar = Scrollbar(root, orient='vertical')
    scrollbar.grid(column=6, row=2, sticky='ns')
    
    liste_id=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_heure_d=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_heure_f=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_jour=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_salle=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste=[liste_id, liste_heure_d, liste_heure_f, liste_jour, liste_salle]
    for row in c.execute("SELECT id, heure_d, heure_f,jour,salle FROM horaire"):
        liste_id.insert(END, row[0])
        liste_heure_d.insert(END, row[1])
        liste_heure_f.insert(END, row[2])
        liste_jour.insert(END, row[3])
        liste_salle.insert(END, row[4])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='heure debut :', background='#D8D8DA').grid(column=2, row=0)
    texte=Label(root, text='heure fin :', background='#D8D8DA').grid(column=3, row=0)
    texte=Label(root, text='jour :', background='#D8D8DA').grid(column=4, row=0)
    texte=Label(root, text='salle :', background='#D8D8DA').grid(column=5, row=0)
    liste_id.configure(height=10)
    liste_id.grid(column=1, row=2)
    liste_heure_d.configure(height=10)
    liste_heure_d.grid(column=2, row=2)
    liste_heure_f.configure(height=10)
    liste_heure_f.grid(column=3, row=2)
    liste_jour.configure(height=10)
    liste_jour.grid(column=4, row=2)
    liste_salle.configure(height=10)
    liste_salle.grid(column=5, row=2)
    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_heure_d.get(index))
            ligne.append(liste_heure_f.get(index))
            ligne.append(liste_jour.get(index))
            ligne.append(liste_salle.get(index))
            mod_horaire(ligne[0], ligne[1], ligne[2],ligne[3], ligne[4])
        
        identifiant=liste_id.curselection()
        heure_d=liste_heure_d.curselection()
        heure_f=liste_heure_f.curselection()
        jour=liste_jour.curselection()
        salle=liste_salle.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
        elif heure_d!=null:
            index=heure_d
        elif heure_f!=null:
            index=heure_f
        elif jour!=null:
            index=jour
        elif salle != null:
            index=salle
        go()
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton = Button(root, text='Retour', command=accueil_mod).grid(column = 2, row=3)
    
def mod_horaire(identifiant, heure_d, heure_f, jour, salle):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE horaire SET id='"+str(entry_id.get())+"', heure_d='"+str(entry_heure_d.get())+"', heure_f='"+str(entry_heure_f.get())+"', jour='"+str(entry_jour.get())+"', salle='"+str(entry_salle.get())+"' WHERE id='"+str(identifiant)+"' AND heure_d='"+str(heure_d)+"' AND heure_f='"+str(heure_f)+"' AND jour='"+str(jour)+"' AND salle='"+str(salle)+"';")
        print("UPDATE horaire SET id='"+str(entry_id.get())+"', heure_d='"+str(entry_heure_d.get())+"', heure_f='"+str(entry_heure_f.get())+"', jour='"+str(entry_jour.get())+"', salle='"+str(entry_salle.get())+"' WHERE id='"+str(identifiant)+"' AND heure_d='"+str(heure_d)+"' AND heure_f='"+str(heure_f)+"' AND jour='"+str(jour)+"' AND salle='"+str(salle)+"';")
        conn.commit()
        conn.close()
        mod_horaire(entry_id.get(), entry_heure_d.get(), entry_heure_f.get(), entry_jour.get(), entry_salle.get())
    
    texte=Label(f1, text='id :').grid(column=0, row=0)
    texte=Label(f1, text='heure_d :').grid(column=1, row=0)
    texte=Label(f1, text='heure_f :').grid(column=2, row=0)
    texte=Label(f1, text='jour :').grid(column=3, row=0)
    texte=Label(f1, text='salle :').grid(column=4, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_heure_d=StringVar()
    entry_heure_d.set(heure_d)
    entry_heure_f=StringVar()
    entry_heure_f.set(heure_f)
    entry_jour=StringVar()
    entry_jour.set(jour)
    entry_salle=StringVar()
    entry_salle.set(salle)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_heure_d=Entry(f1, textvariable=entry_heure_d).grid(column=1, row=1)
    entree_heure_f=Entry(f1, textvariable=entry_heure_f).grid(column=2, row=1)
    entree_jour=Entry(f1, textvariable=entry_jour).grid(column=3, row=1)
    entree_salle=Entry(f1, textvariable=entry_salle).grid(column=4, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=horaire_mod).grid(column=1, row=2)

def batiment_mod():
    global f1
    
    init()
    f1.destroy()
    
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)
    
    def yview(*args):
        pass
    
    scrollbar = Scrollbar(root, orient='vertical')
    scrollbar.grid(column=3, row=2, sticky='ns')
    
    
    liste_id=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste_nomb=Listbox(root, activestyle='dotbox', yscrollcommand=yscroll)
    liste=[liste_id, liste_nomb]
    for row in c.execute("SELECT id, nomb FROM batiment"):
        liste_id.insert(END, row[0])
        liste_nomb.insert(END, row[1])
    texte=Label(root, text='id :', background='#D8D8DA').grid(column=1, row=0)
    texte=Label(root, text='nom batiment :', background='#D8D8DA').grid(column=2, row=0)
    liste_id.configure(height=10)
    liste_nomb.configure(height=10)
    liste_nomb.grid(column=2, row=2)
    liste_id.grid(column=1, row=2)
    
    def valid():
        
        def go():
            ligne.append(liste_id.get(index))
            ligne.append(liste_nomb.get(index))
            mod_batiment(ligne[0], ligne[1])
        
        identifiant=liste_id.curselection()
        nomb=liste_nomb.curselection()
        null=()
        ligne=[]
        if identifiant!=null:
            index=identifiant
        elif nomb!=null:
            index=nomb
        go()
    
    bouton=Button(root, text='Modifier', command=valid).grid(column=1, row=3)
    bouton = Button(root,text='Retour', command=accueil_mod).grid(column = 2, row=3)

#modifier un batiment modifie les salles qui se trouve dans celui-ci pour conserver le lien existant

def mod_batiment(identifiant, nom):
    global f1
    init()
    
    def mod():
        conn=sqlite3.connect('serveur.db')
        c=conn.cursor()
        c.execute("UPDATE batiment SET id='"+entry_id.get()+"', nomb='"+entry_nom.get()+"' WHERE id='"+str(identifiant)+"' AND nomb='"+nom+"' ;")
        print("UPDATE batiment SET id='"+entry_id.get()+"', nom='"+entry_nom.get()+"' WHERE id='"+str(identifiant)+"' AND nom='"+nom+"' ;")
        c.execute("UPDATE salle SET batiment='"+entry_id.get()+"' WHERE batiment='"+str(identifiant)+"' ;")
        print("UPDATE salle SET batiment='"+entry_id.get()+"' WHERE batiment='"+str(identifiant)+"' ;")
        conn.commit()
        conn.close()
        mod_batiment(entry_id.get(), entry_nom.get())
    
    texte=Label(f1, text='id :').grid(column=0, row=0)
    texte=Label(f1, text='nom :').grid(column=1, row=0)
    entry_id=StringVar()
    entry_id.set(identifiant)
    entry_nom=StringVar()
    entry_nom.set(nom)
    entree_id=Entry(f1, textvariable=entry_id).grid(column=0, row=1)
    entree_nom=Entry(f1, textvariable=entry_nom).grid(column=1, row=1)
    bouton=Button(f1, text='Valider', command=mod).grid(column=0, row=2)
    bouton=Button(f1, text='Retour', command=batiment_mod).grid(column=1, row=2)

#La fonction row permet d'afficher les tables dans les menus ajouter et supprimer pour pouvoir voir les elements dans celles-ci
#Comme pour les menus modifier, les listbox permettent de pouvoir scroller

def row(tab, window, c):
    compteur=0
    liste=[]
    
    def yscroll(*args):
        for li in liste:
            for lis in liste:
                if lis.yview() != li.yview():
                    lis.yview_moveto(args[0])
                scrollbar.set(*args)
    
    def yview(*args):
        pass
    
    for row in c.execute("SELECT * FROM "+tab+";"):
        colonne=len(row)
        
    for i in range(colonne):
        liste_i=Listbox(window, highlightcolor='white', highlightbackground='white', selectbackground='white', selectforeground='black', activestyle='none', height=10, yscrollcommand=yscroll)
        liste_i.grid(column=i, row=2)
        for element in c.execute("SELECT * FROM "+tab+""):
            liste_i.insert(END, element[i])
        liste.append(liste_i)
        maxi=i
        
    scrollbar = Scrollbar(window, orient='vertical')
    scrollbar.grid(column=maxi+1, row=2, sticky='ns')
    
    column=0
    for row in c.execute("PRAGMA table_info("+tab+");"):
        titre_i=Label(window, text=row[1])
        titre_i.grid(column=column, row=0)
        column+=1

#cette fonction permet d'afficher les elements "estetiques" dans les menus

def interact_box(table, test):
    
    f2=Frame(root, bg='#130797')
    f2.pack(side=TOP,padx=10,pady=10)
    
    text2 = Text(f2, height=9, width=50, state='normal')

    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#f7b90f',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                   '<1>',
                   lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nSimpleAdministrator\n', 'big')
    
    text2.insert(END, 'Connecté à "serveur.db" [69 77 76 78 66]\n', 'follow','\n')
    text2.insert(END, test)
    text2.pack(side=LEFT, padx=10, pady=5)
    text2.configure(state = 'disabled')
    
    f3=Frame(root,borderwidth=2,relief=GROOVE)
    f3.pack(side=BOTTOM,padx=10,pady=10)
    
    row(table, f3, c)

def close():
    root.destroy()
    
#Ce menu permet de naviguer entre les differentes options ajouter supprimer et modifier.
    
def main_menu():
    for c in root.winfo_children():
        c.destroy()
    root.title("Interface Administrateur")
    f1=Frame(root, relief = RIDGE, borderwidth=2, bg='#130797')
    f1.grid(column=0, row=0, padx=10)
    button = Button(f1, text='Ajouter des éléments', command=accueil_add, width = 20).pack(side=TOP, pady=2, padx=10)
    button = Button(f1, text='Modifier des élements', command=accueil_mod, width = 20).pack(side=TOP, pady=2, padx=10)
    button = Button(f1, text='Supprimer des élements', command=accueil_del, width = 20).pack(side=TOP, pady=2, padx=10)
    button = Button(root, text='Quitter', command=close, width = 15).grid(column=0, row=1, columnspan=2, padx=10, pady=5)
    f2=Frame(root, bg='#130797')
    f2.grid(column=1, row=0, padx=10, pady=10)
    
    text2 = Text(f2, height=7, width=50, state='normal')

    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#f7b90f',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                   '<1>',
                   lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\nSimpleAdministrator\n', 'big')
    
    text2.insert(END, 'Connecté à "serveur.db" [69 77 76 78 66]\n', 'follow')
    text2.pack(side=LEFT, padx=10, pady=5)
    text2.configure(state = 'disabled')


main_menu()
