from tkinter import * #tkinter kutubxonasi o'rnatiladi
from googletrans import Translator

oyna = Tk()
oyna.title('Google tarjimon😀')
oyna.geometry('500x400')
oyna.configure(bg='green')

natija = Label(text='UZB', bg='white')
natija.place(x=90, y=140, width=310, height=30)

matn = Entry()
matn.place(x=90, y=50, width=310, height=30)

def eng():
        tarjimon = Translator()
        natija.config(text = tarjimon.translate(matn.get(), dest='uz').text.capitalize())
        
tugma = Button(text='Tarjima qilish!', command=eng, bg='yellow', border='5')
tugma.place(x=180, y=90, width=120, height=40)

oyna.mainloop()

#2023,08,21 22:55