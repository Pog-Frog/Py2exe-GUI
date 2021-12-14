from tkinter import *
import logging
from threading import Thread
import sys

class IODirector(object):
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutDirector(IODirector):
    def write(self,str):
        self.text_area.insert(END,str)
    def flush(self):
        pass

class App(Frame):

    def __init__(self, master):
        self.master = master
        Frame.__init__(self,master,relief=SUNKEN,bd=2)
        self.start()

    def start(self):
        self.master.title("Test")
        self.submit = Button(self.master, text='Run', command=self.do_run, fg="red")
        self.submit.grid(row=1, column=2)
        self.text_area = Text(self.master,height=2.5,width=30,bg='light cyan')
        self.text_area.grid(row=1,column=1)

    def do_run(self):
        t = Thread(target=print_stuff)
        sys.stdout = StdoutDirector(self.text_area)
        t.start()

def print_stuff():
    logger = logging.getLogger('print_stuff')
    logger.info('This will not show')
    print ('This will show')
    print_some_other_stuff()

def print_some_other_stuff():
    logger = logging.getLogger('print_some_other_stuff')
    logger.info('This will also not show')
    print ('This will also show')

def main():    
    logger = logging.getLogger('main')
    root = Tk()
    app = App(root)
    root.mainloop() 

if __name__=='__main__':
    main()