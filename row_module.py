##from row_module import *
##row("utilisateur", root, c)
def row(tab, window, cursor):
    c.execute("SELECT * FROM "+tab+" limit 0,10")
    i=0 
    for element in c: 
        for j in range(len(element)):
            e = Entry(window, width=10, fg='black') 
            e.grid(row=i, column=j) 
            e.insert(END, element[j])
            e.configure(state = 'disabled')
        i=i+1