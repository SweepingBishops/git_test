import mysql.connector as mc
import tabulate
import tkinter as tk
conn=mc.connect(host='localhost',user='root',database='minesweeper',passwd='')
cur=conn.cursor()
cur.execute('select * from gridsize6 order by time;')
b=list(cur)
d=[]
try:
	for i in range(5):
	    c=list(b[i])
	    c.insert(0,i+1)
	    d+=[c]
except IndexError:
	pass
    
a=tabulate.tabulate(d)

#tkinter
root=tk.Tk()
root.title('HIGHSCORE')
root.rowconfigure([0],minsize=150)
root.columnconfigure([0,1,2],minsize=70)
label=tk.Label(text=a)
label.grid(row=0,column=1)

