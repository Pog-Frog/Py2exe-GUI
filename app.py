import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk, ImageOps

global path
path = os.path.dirname(os.path.abspath(__file__))


class panel:
    def __init__(self, window):
        self.window = window

    app = tk.Tk()
    app.geometry('550x640')
    app.resizable(False, False)
    app.title('Pyinstaller GUI')
    app.wm_iconbitmap(os.path.join(path, 'images', 'python.ico'))
    MenuBar = tk.Menu(app)
    FileMenu = tk.Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label='EXIT', command=app.destroy)
    MenuBar.add_cascade(label='File', menu=FileMenu)

    logo = ImageTk.PhotoImage(Image.open(os.path.join(path,'images','logo.png')))
    label1 = tk.Label(app, image=logo)
    label1.pack(side=tk.TOP)

    ToolsMenu = tk.Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label='Tools', menu=ToolsMenu)

    HelpMenu = tk.Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)

    app.config(menu=MenuBar)

    def execute(self):
        tmp = f"pyinstaller {self.combo_1_str.get()}{self.combo_2_str.get()}{self.combo_3_str.get()}"
        
    def BuildCommand(event):
        string = f""


    combo_1_str = tk.StringVar()
    combo_1_str.set('choose file')
    combo_1 = ttk.Combobox(app, textvariable=combo_1_str, state='readonly')
    combo_1.place(width=343, height=21, x=10, y=124)
    button7 = ttk.Button(app, text='Browse', command=lambda: GetDirectoryString('script'))
    button7.place(width=76, height=25, x=359, y=124)


    combo_1_str = tk.StringVar()
    combo_1_str.set('--console')
    combo_1 = ttk.Combobox(app, textvariable=combo_1_str, state='readonly')
    combo_1['values'] = ('--console', '--windowed')
    combo_1.place(width=143, height=21, x=10, y=124)
    combo_1.bind('<<ComboboxSelected>>', execute)


    

    '''checkbox_1_str = tk.StringVar()
    checkbox_1_str.set('')
    checkbox_1 = ttk.Checkbutton(
        app, text='--name', variable=checkbox_1_str, onvalue='--name', offvalue='')
    checkbox_1.place(width=63, height=21, x=245, y=124)
    entry1 = ttk.Entry(app)
    entry1.place(width=126, height=21, x=318, y=124)

    checkbox_2_str = tk.StringVar()
    checkbox_2_str.set('')
    checkbox_2 = ttk.Checkbutton(app, text='--onefile', variable=checkbox_2_str, onvalue=' --onefile',
                                offvalue='', command=lambda: BuildCommand(''))
    checkbox_2.place(width=69, height=21, x=10, y=159)

    checkbox_3_str = tk.StringVar()
    checkbox_3_str.set(' --noupx')
    checkbox_3 = ttk.Checkbutton(app, text=('--noupx'), variable=checkbox_3_str, onvalue=' --noupx',
                            offvalue='', command=lambda: BuildCommand(''))
    checkbox_3.place(width=66, height=21, x=164, y=159)

    checkbox_4_str = tk.StringVar()
    checkbox_4_str.set('')
    checkbox_4 = ttk.Checkbutton(app, text='--version-file', variable=checkbox_4_str,
                                onvalue=' --version-file', offvalue='', command=lambda: BuildCommand(''))
    checkbox_4.place(width=92, height=21, x=10, y=194)

    button5 = ttk.Button(app, text='Browse', command=lambda: GetDirectoryString('versionfile'))
    button5.place(width=76, height=25, x=112, y=194)'''

    app.mainloop()



if __name__ == '__main__':
    app = tk.Tk()
    app.geometry('550x640')
    app.resizable(False, False)
    app.title('Pyinstaller GUI')
    pane = panel(app)