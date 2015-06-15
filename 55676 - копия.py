import tkinter
import tkinter.filedialog
import tkinter.messagebox

import requests
import lxml.html

from PIL import ImageTk, Image

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.path = ''

        self.build_widgets()
        self.build_menu()
        
    def build_widgets(self):

        self.statistics_text = tkinter.Label(self.master, text='Откройте текст')
        self.statistics_text.grid(row=0,column=0)
        
        self.text = tkinter.Text(self.master, width=100, height=25 )
        self.text.grid(row=1,column=0)


        self.statistics = tkinter.Label(self.master)
        self.statistics.grid(row=3,column=0)

        self.img = ImageTk.PhotoImage(
            Image.open('text.jpg').resize((205, 200), Image.ANTIALIAS)
        )
        self.img_statistics = tkinter.Label(self.master, image=self.img)
        self.img_statistics.grid(row=1,column=1)

        

    def build_menu(self):
        menu = tkinter.Menu(self.master)
        self.master.config(menu=menu)
        filemenu = tkinter.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_command(label='Close', command=self.close)

    def open_file(self):
        self.path = tkinter.filedialog.askopenfilename()
        if self.path:
            self.text.delete('1.0', tkinter.END)
            self.text.insert(1.0, ''.join([i for i in open(self.path)]))
            self.count()

    def close(self):
        if tkinter.messagebox.askyesno("Выйти", "Вы действительно хотите закрыть файл?"):
            self.master.destroy()

    def save_file(self):
        if tkinter.messagebox.askyesno("Сохранить", "Вы действительно хотите сохранить файл?"):
            text = self.text.get(1.0, tkinter.END)
            out = open(self.path, "w")
            out.write(text)
            out.close()

            # Функция сохр файла конец

    def count(self):
        data = open(self.path)
        word = sum(len(line.split()) for line in data)
        data.seek(0)
        line = sum(1 for _ in data)
        self.statistics['text'] = 'Слов : {},\n Строк: {}'.format(word, line)


root = tkinter.Tk()
root.title('Statistics')
root.geometry('1000x600+50+50')
window = MainWindow(root)
root.mainloop()
