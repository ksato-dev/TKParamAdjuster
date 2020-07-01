# refer to https://python.keicode.com/advanced/tkinter-widget-scale.php
from tkinter import *
from tkinter import ttk

def button_click():
    print('value = %d' % myval.get())

def value_changed(*args):
    print('value = %d' % myval.get())
    
if __name__ == '__main__':
    
    root = Tk()
    root.title('Scale')
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(sticky=(N,W,S,E))
    frame1.columnconfigure(0, weight=1);
    frame1.rowconfigure(0, weight=1);
    
    # スケールの作成
    myval = DoubleVar()
    myval.trace("w", value_changed)
    
    sc = ttk.Scale(
        frame1,
        variable=myval,
        orient=HORIZONTAL, 
        length=200,
        from_=0,
        to=255)
    sc.grid(row=0, column=0, sticky=(N,E,S,W))

    #Button
    button1 = ttk.Button(
        frame1, 
        text='OK', 
        command=button_click)
    button1.grid(row=0, column=1, padx=5, sticky=(E))
        
    root.mainloop()
