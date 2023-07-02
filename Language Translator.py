
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
language = LANGUAGES
langValue = list(language.values())



window = Tk()
window.title("Language Translator")
window.minsize(700, 600)
window.maxsize(700, 600)



combo1 = ttk.Combobox(window, values=langValue , state='r')
combo1.place(x=50, y=75)
combo1.set("choose a language")


frame1 = Frame(window, bg='black', bd=0)
frame1.place(x=50, y=100, width=290, height=250)
text1 = Text(frame1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=289.4, height=248.5)


combo2 = ttk.Combobox(window, values= langValue, state='r')
combo2.place(x=360, y=75)
combo2.set("Choose a language")




frame2 = Frame(window, bg='black', bd=0)
frame2.place(x=360, y=100, width=290, height=250)
text2 = Text(frame2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=289.4, height=248.5)


def translation():
    global language
    try:
      lang1 = text1.get(1.0, END)
      c1 = combo1.get()
      c2 = combo2.get()
      if lang1 == '':
          messagebox.showerror('Language Translator', 'Enter the text to translate!')
      else:
          translator = Translator()
          src_code = [i for i, j in language.items() if j == c1][0]
          destination_code = [k for k, v in language.items() if v == c2][0]
          text2.delete(1.0, END)
          output = translator.translate(lang1, destination_code,src_code)

          text2.insert(END,output.text)
    except Exception as e:
       messagebox.showerror("Try again")


def clear():
    text1.delete(1.0, END)
    text2.delete(1.0, END)




button = Button(window, text='Translate', font=('Roboto', 15), bg='#84FFE2', command=translation)
button.place(x=240, y=365)

button2 = Button(window, text='Clear', font=('Roboto', 15), bg='#84FFE2', command=clear)
button2.place(x=360, y=365)


window.mainloop()
