import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from PIL import Image, ImageTk

path = os.path.dirname(os.path.abspath(__file__))


class Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyInstaller GUI")
        self.geometry("506x400")
        self.resizable(False, False)
        self.wm_iconbitmap(os.path.join(path, "images", "python.ico"))
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        toolsmenu = tk.Menu(menubar, tearoff=0)
        toolsmenu.add_command(label="SetVersion", command=self.CallSetVersion)
        menubar.add_cascade(label="Tools", menu=toolsmenu)
        self.config(menu=menubar)
        self.logoImage = ImageTk.PhotoImage(
            Image.open(os.path.join(path, "images", "logo.png"))
        )
        label1 = tk.Label(self, image=self.logoImage)
        self.COLOR = "#ffffff"
        label1.pack(side=tk.TOP)
        self.ComboBoxVar1 = tk.StringVar()
        self.ComboBoxVar1.set("console")
        ComboBox1 = ttk.Combobox(
            self,
            values=["console", "windowed"],
            textvariable=self.ComboBoxVar1,
            state="readonly",
        )
        ComboBox1.place(width=143, height=21, x=10, y=124)
        ComboBox1.bind("<<ComboboxSelected>>", self.BuildCommand)

        self.CheckBoxVar1 = tk.StringVar()
        self.CheckBoxVar1.set("")
        CheckBox1 = ttk.Checkbutton(
            self,
            text="name",
            variable=self.CheckBoxVar1,
            onvalue=" --name",
            offvalue="",
            command=lambda: self.BuildCommand(""),
        )
        CheckBox1.place(width=63, height=21, x=245, y=124)
        self.entry1 = ttk.Entry(self)
        self.entry1.place(width=126, height=21, x=318, y=124)

        self.CheckBoxVar2 = tk.StringVar()
        self.CheckBoxVar2.set("")
        CheckBox2 = ttk.Checkbutton(
            self,
            text="onefile",
            variable=self.CheckBoxVar2,
            onvalue=" --onefile",
            offvalue="",
            command=lambda: self.BuildCommand(""),
        )
        CheckBox2.place(width=69, height=21, x=10, y=159)

        self.CheckBoxVar3 = tk.StringVar()
        self.CheckBoxVar3.set(" --noupx")
        CheckBox3 = ttk.Checkbutton(
            self,
            text=("noupx"),
            variable=self.CheckBoxVar3,
            onvalue=" --noupx",
            offvalue="",
            command=lambda: self.BuildCommand(""),
        )
        CheckBox3.place(width=66, height=21, x=164, y=159)

        self.CheckBoxVar4 = tk.StringVar()
        self.CheckBoxVar4.set("")
        CheckBox4 = ttk.Checkbutton(
            self,
            text="version-file",
            variable=self.CheckBoxVar4,
            onvalue=" --version-file",
            offvalue="",
            command=lambda: self.BuildCommand(""),
        )
        CheckBox4.place(width=92, height=21, x=10, y=194)

        button5 = ttk.Button(
            self, text="Browse", command=lambda: self.GetDirectoryString("versionfile")
        )
        button5.place(width=76, height=25, x=112, y=194)

        self.entry2 = ttk.Entry(self)
        self.entry2.place(width=248, height=21, x=198, y=197)

        label2 = tk.Label(self, text="Script", bg=self.COLOR)
        label2.place(width=36, height=21, x=10, y=229)
        button7 = ttk.Button(
            self, text="Browse", command=lambda: self.GetDirectoryString("script")
        )
        button7.place(width=76, height=25, x=56, y=229)
        self.entry3 = ttk.Entry(self)
        self.entry3.place(width=354, height=21, x=142, y=229)

        self.CheckBoxVar5 = tk.StringVar()
        self.CheckBoxVar5.set("")
        CheckBox5 = ttk.Checkbutton(
            self,
            text="icon",
            variable=self.CheckBoxVar5,
            onvalue=" --icon",
            offvalue="",
            command=lambda: self.BuildCommand(""),
        )
        CheckBox5.place(width=56, height=21, x=10, y=264)
        button8 = ttk.Button(
            self, text="Browse", command=lambda: self.GetDirectoryString("icon")
        )
        button8.place(width=76, height=25, x=76, y=264)

        self.entry4 = ttk.Entry(self)
        self.entry4.place(width=284, height=21, x=162, y=264)

        label3 = tk.Label(self, text="Command", bg=self.COLOR)
        label3.place(width=63, height=21, x=10, y=299)
        self.entry5 = ttk.Entry(self)
        self.entry5.place(width=363, height=21, x=83, y=299)
        self.BuildCommand("")

        button10 = ttk.Button(self, text="Build", command=self.RunBuild)
        button10.place(width=76, height=25, x=(506 / 2) - 86, y=340)
        button11 = ttk.Button(self, text="Close", command=self.destroy)
        button11.place(width=76, height=25, x=(506 / 2) + 10, y=340)

        ttk.Style().configure("TCheckbutton", background=self.COLOR)

    def CallSetVersion(self):
        CallSetVersionFile = SetVersionFile(self)

    def BuildCommand(self, event):
        combo_temp1 = ""
        if self.ComboBoxVar1.get() == "console":
            combo_temp1 = "--console"
        else:
            combo_temp1 = "--windowed"
        string = (
                "pyinstaller --clean "
                + combo_temp1
                + self.CheckBoxVar2.get()
                + self.CheckBoxVar3.get()
        )
        if self.CheckBoxVar1.get() == "" or self.entry1.get().strip() == "":
            pass
        else:
            string += self.CheckBoxVar1.get() + '="' + self.entry1.get().strip() + '"'
        if self.CheckBoxVar4.get() == "" or self.entry2.get().strip() == "":
            pass
        else:
            string += self.CheckBoxVar4.get() + '="' + self.entry2.get().strip() + '"'
        if self.entry3.get().strip() == "":
            pass
        else:
            string += ' "' + self.entry3.get() + '"'
        if self.CheckBoxVar5.get() == "" or self.entry4.get().strip() == "":
            pass
        else:
            string += self.CheckBoxVar5.get() + ' "' + self.entry4.get() + '"'
        self.entry5.delete(0, tk.END)
        self.entry5.insert(tk.END, string)

    def RunBuild(self):
        if self.entry3.get().strip() == "":
            pass
        else:
            os.system(str(self.entry5.get().strip()))
            self.ComboBoxVar1.set(" --console")
            self.CheckBoxVar1.set("")
            self.entry1.delete(0, tk.END)
            self.CheckBoxVar2.set("")
            self.CheckBoxVar3.set(" --noupx")
            self.CheckBoxVar4.set("")
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.CheckBoxVar5.set("")
            self.entry4.delete(0, tk.END)
            self.BuildCommand("")

    def GetDirectoryString(self, string):
        if string == "versionfile":
            filename = filedialog.askopenfilename(filetypes=[("Version File", "*.txt")])
            self.entry2.delete(0, tk.END)
            if filename == "":
                pass
            else:
                self.entry2.insert(tk.END, str(filename))
        elif string == "script":
            filename = filedialog.askopenfilename(
                filetypes=[("Python Script", "*.py | *.pyw")]
            )
            self.entry3.delete(0, tk.END)
            if filename == "":
                pass
            else:
                self.entry3.insert(tk.END, str(filename))
        elif string == "icon":
            filename = filedialog.askopenfilename(filetypes=[("Icon", "*.ico")])
            self.entry4.delete(0, tk.END)
            if filename == "":
                pass
            else:
                self.entry4.insert(tk.END, str(filename))

        self.BuildCommand("")

    """
        def GetDirectoryString(self, string):
        if string == 'fileversion':
            filename = filedialog.askopenfilename(filetypes=[('Version File', '*.txt')])
            self.entry1.delete(0, tk.END)
            if filename == '':
                pass
            else:
                self.entry1.insert(tk.END, str(filename))
        elif string == 'executable':
            filename = filedialog.askopenfilename(filetypes=[('Executable', '*.exe')])
            self.entry2.delete(0, tk.END)
            if filename == '':
                pass
            else:
                self.entry2.insert(tk.END, str(filename))

        self.entry3.delete(0, tk.END)
        string = 'pyi-set_version'
        if str(self.entry1.get().strip()) == '':
            pass
        else:
            string += ' "' + str(self.entry1.get()) + '"'
        if str(self.entry2.get().strip()) == '':
            pass
        else:
            string += ' "' + str(self.entry2.get()) + '"'
        self.entry3.insert(tk.END, string)
    """


class SetVersionFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 506
        h = 300
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry("{0}x{1}+{2}+{3}".format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.configure(background=parent.COLOR)
        self.title("Set Version File")
        self.wm_iconbitmap(os.path.join(path, "images", "python.ico"))

        def GetDirectoryString(string):
            if string == "fileversion":
                filename = filedialog.askopenfilename(
                    filetypes=[("Version File", "*.txt")]
                )
                entry1.delete(0, tk.END)
                if filename == "":
                    pass
                else:
                    entry1.insert(tk.END, str(filename))
            elif string == "executable":
                filename = filedialog.askopenfilename(
                    filetypes=[("Executable", "*.exe")]
                )
                entry2.delete(0, tk.END)
                if filename == "":
                    pass
                else:
                    entry2.insert(tk.END, str(filename))

            entry3.delete(0, tk.END)
            string = "pyi-set_version"
            if str(entry1.get().strip()) == "":
                pass
            else:
                string += ' "' + str(entry1.get()) + '"'
            if str(entry2.get().strip()) == "":
                pass
            else:
                string += ' "' + str(entry2.get()) + '"'
            entry3.insert(tk.END, string)

        self.logoImage = ImageTk.PhotoImage(Image.open("images/logo.png"))
        label1 = tk.Label(self, image=self.logoImage)
        label1.pack(side=tk.TOP)

        def SetVersion():
            os.system(
                'pyi-set_version "'
                + str(entry1.get().strip())
                + '" "'
                + str(entry2.get().strip())
                + '"'
            )
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)
            entry3.insert(tk.END, "pyi-set_version")

        label2 = tk.Label(self, text="File Version", bg=parent.COLOR)
        label2.place(x=10, y=120)
        button1 = ttk.Button(
            self, text="Browse", command=lambda: GetDirectoryString("fileversion")
        )
        button1.place(x=80, y=120)
        entry1 = ttk.Entry(self)
        entry1.place(width=506 - 76 - 100, height=21, x=165, y=122)

        label3 = tk.Label(self, text="Executable", bg=parent.COLOR)
        label3.place(x=10, y=155)
        button2 = ttk.Button(
            self, text="Browse", command=lambda: GetDirectoryString("executable")
        )
        button2.place(x=80, y=155)
        entry2 = ttk.Entry(self)
        entry2.place(width=330, height=21, x=165, y=157)

        label4 = tk.Label(self, text="Command", bg=parent.COLOR)
        label4.place(x=10, y=192)
        entry3 = ttk.Entry(self)
        entry3.place(width=365, height=21, x=80, y=192)
        entry3.insert(tk.END, "pyi-set_version")

        button4 = ttk.Button(self, text="Set Version", command=SetVersion)
        button4.place(width=76, height=25, x=(506 / 2) - 86, y=235)
        button5 = ttk.Button(self, text="Close", command=self.destroy)
        button5.place(width=76, height=25, x=(506 / 2) + 10, y=235)


if __name__ == "__main__":
    app = Panel()
    app.mainloop()
