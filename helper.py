import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from tkinter.constants import FALSE
from PIL import Image, ImageTk, ImageOps



class SetVersionFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        path = os.path.dirname(os.path.abspath(__file__)) 
        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 506
        h = 300
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.configure(background=parent.COLOR)
        self.title('Set Version File')
        self.wm_iconbitmap(os.path.join(path, 'images', 'python.ico'))

        # self.wm_iconbitmap('images/python.ico')

        def GetDirectoryString(string):
            if string == 'fileversion':
                filename = filedialog.askopenfilename(filetypes=[('Version File', '*.txt')])
                entry1.delete(0, tk.END)
                if filename == '':
                    pass
                else:
                    entry1.insert(tk.END, str(filename))
            elif string == 'executable':
                filename = filedialog.askopenfilename(filetypes=[('Executable', '*.exe')])
                entry2.delete(0, tk.END)
                if filename == '':
                    pass
                else:
                    entry2.insert(tk.END, str(filename))

            entry3.delete(0, tk.END)
            string = 'pyi-set_version'
            if str(entry1.get().strip()) == '':
                pass
            else:
                string += ' "' + str(entry1.get()) + '"'
            if str(entry2.get().strip()) == '':
                pass
            else:
                string += ' "' + str(entry2.get()) + '"'
            entry3.insert(tk.END, string)

        self.logoImage = ImageTk.PhotoImage(Image.open('images/logo.png'))
        # self.logoImage = ImageTk.PhotoImage(Image.open('images/logo.png'))
        label1 = tk.Label(self, image=self.logoImage)
        label1.pack(side=tk.TOP)

        def SetVersion():
            os.system('pyi-set_version "' + str(entry1.get().strip()) + '" "' + str(entry2.get().strip()) + '"')
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)
            entry3.insert(tk.END, 'pyi-set_version')

        label2 = tk.Label(self, text='File Version', bg=parent.COLOR)
        label2.place(x=10, y=120)
        button1 = ttk.Button(self, text='Browse', command=lambda: GetDirectoryString('fileversion'))
        button1.place(x=80, y=120)
        entry1 = ttk.Entry(self)
        entry1.place(width=506 - 76 - 100, height=21, x=165, y=122)

        label3 = tk.Label(self, text='Executable', bg=parent.COLOR)
        label3.place(x=10, y=155)
        button2 = ttk.Button(self, text='Browse', command=lambda: GetDirectoryString('executable'))
        button2.place(x=80, y=155)
        entry2 = ttk.Entry(self)
        entry2.place(width=330, height=21, x=165, y=157)

        label4 = tk.Label(self, text='Command', bg=parent.COLOR)
        label4.place(x=10, y=192)
        entry3 = ttk.Entry(self)
        entry3.place(width=365, height=21, x=80, y=192)
        entry3.insert(tk.END, 'pyi-set_version')

        button4 = ttk.Button(self, text='Set Version', command=SetVersion)
        button4.place(width=76, height=25, x=(506 / 2) - 86, y=235)
        button5 = ttk.Button(self, text='Close', command=self.destroy)
        button5.place(width=76, height=25, x=(506 / 2) + 10, y=235)
