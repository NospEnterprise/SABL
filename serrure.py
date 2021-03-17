from tkinter import *
from datetime import *
from sqlite3 import *
window = Tk()
window.title("Simulateur de serrure")

def comparer():
    test=0
    jour=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    now = time.localtime(time.time())
    hour=now[3]
    identifiant = entry_id.get()
    salle = entry_salle.get()
    conn=connect('serveur.db')
    c=conn.cursor()
    
    #Les responsables peuvent ouvrir toutes les portes à toute heure, et possèdent '*' au debut de leur id(voir interface administrateur)
    if identifiant[0]=='*':
        print("Vous pouvez entrer.")
        print("Bienvenue")
    else:
        for row in c.execute('SELECT * FROM utilisateur INNER JOIN horaire ON utilisateur.id=horaire.id WHERE utilisateur.id="'+identifiant+'";'):
            if row[6]==jour[date.weekday(date.today())]:
                if hour>=row[4] and hour<row[5]:
                    if str(row[7])==salle:
                        test+=1
        if test>0:
            print("Vous pouvez entrer.")
            print("Bienvenue")
        else:
            print("Vous n'êtes pas autorisé à entrer, pour tout problème, veuillez contacter le :XX.XX.XX.XX.XX.")
    conn.commit()
    conn.close()

entry_id=StringVar()
label = Label( window, text="Entrez votre id.").pack(padx=10, pady=5)
passEntry = Entry(window, textvariable=entry_id).pack(padx=10, pady=5)

"""Entrer la salle ne serait pas utile sur une serrure, mais il faudrait comparer grace à l'id de la serrure pour
savoir si la salle en particulier peut etre ouverte, et non toutes.
"""

entry_salle = StringVar()
label = Label(window, text="Entrez le numéro de la salle à ouvrir.").pack(padx=10, pady=5)
passEntry = Entry(window, textvariable=entry_salle).pack(padx=10, pady=5)
submit = Button(window, text='valider', command=comparer).pack(padx=10, pady=5)

