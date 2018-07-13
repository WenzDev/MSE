import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import entry_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    entry_support.set_Tk_var()
    top = New_Toplevel (root)
    entry_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    entry_support.set_Tk_var()
    top = New_Toplevel (w)
    entry_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font12 = "-family Arial -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1689x878+102+86")
        top.title("Mailsafe Express")
        top.configure(background="#0066ab")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.e_lname = Entry(top)
        self.e_lname.place(relx=0.61, rely=0.16,height=30, relwidth=0.41)
        self.e_lname.configure(background="white")
        self.e_lname.configure(disabledforeground="#a3a3a3")
        self.e_lname.configure(font="TkFixedFont")
        self.e_lname.configure(foreground="#000000")
        self.e_lname.configure(highlightbackground="#d9d9d9")
        self.e_lname.configure(highlightcolor="black")
        self.e_lname.configure(insertbackground="black")
        self.e_lname.configure(selectbackground="#c4c4c4")
        self.e_lname.configure(selectforeground="black")
        self.e_lname.configure(width=694)

        self.ent41 = Entry(top)
        self.ent41.place(relx=0.0, rely=0.0,height=1, relwidth=0.0)
        self.ent41.configure(background="white")
        self.ent41.configure(disabledforeground="#a3a3a3")
        self.ent41.configure(font="TkFixedFont")
        self.ent41.configure(foreground="#000000")
        self.ent41.configure(highlightbackground="#d9d9d9")
        self.ent41.configure(highlightcolor="black")
        self.ent41.configure(insertbackground="black")
        self.ent41.configure(selectbackground="#c4c4c4")
        self.ent41.configure(selectforeground="black")

        self.e_fname = Entry(top)
        self.e_fname.place(relx=0.13, rely=0.16,height=30, relwidth=0.41)
        self.e_fname.configure(background="white")
        self.e_fname.configure(disabledforeground="#a3a3a3")
        self.e_fname.configure(font="TkFixedFont")
        self.e_fname.configure(foreground="#000000")
        self.e_fname.configure(highlightbackground="#d9d9d9")
        self.e_fname.configure(highlightcolor="black")
        self.e_fname.configure(insertbackground="black")
        self.e_fname.configure(selectbackground="#c4c4c4")
        self.e_fname.configure(selectforeground="black")

        self.ent50 = Entry(top)
        self.ent50.place(relx=0.0, rely=0.0,height=1, relwidth=0.0)
        self.ent50.configure(background="white")
        self.ent50.configure(disabledforeground="#a3a3a3")
        self.ent50.configure(font="TkFixedFont")
        self.ent50.configure(foreground="#000000")
        self.ent50.configure(highlightbackground="#d9d9d9")
        self.ent50.configure(highlightcolor="black")
        self.ent50.configure(insertbackground="black")
        self.ent50.configure(selectbackground="#c4c4c4")
        self.ent50.configure(selectforeground="black")

        self.e_email = Entry(top)
        self.e_email.place(relx=0.13, rely=0.31,height=30, relwidth=0.89)
        self.e_email.configure(background="white")
        self.e_email.configure(disabledforeground="#a3a3a3")
        self.e_email.configure(font="TkFixedFont")
        self.e_email.configure(foreground="#000000")
        self.e_email.configure(highlightbackground="#d9d9d9")
        self.e_email.configure(highlightcolor="black")
        self.e_email.configure(insertbackground="black")
        self.e_email.configure(selectbackground="#c4c4c4")
        self.e_email.configure(selectforeground="black")
        self.e_email.configure(width=1504)

        self.e_sta1 = Entry(top)
        self.e_sta1.place(relx=0.13, rely=0.44,height=30, relwidth=0.41)
        self.e_sta1.configure(background="white")
        self.e_sta1.configure(disabledforeground="#a3a3a3")
        self.e_sta1.configure(font="TkFixedFont")
        self.e_sta1.configure(foreground="#000000")
        self.e_sta1.configure(highlightbackground="#d9d9d9")
        self.e_sta1.configure(highlightcolor="black")
        self.e_sta1.configure(insertbackground="black")
        self.e_sta1.configure(selectbackground="#c4c4c4")
        self.e_sta1.configure(selectforeground="black")

        self.e_sta2 = Entry(top)
        self.e_sta2.place(relx=0.61, rely=0.44,height=30, relwidth=0.41)
        self.e_sta2.configure(background="white")
        self.e_sta2.configure(disabledforeground="#a3a3a3")
        self.e_sta2.configure(font="TkFixedFont")
        self.e_sta2.configure(foreground="#000000")
        self.e_sta2.configure(highlightbackground="#d9d9d9")
        self.e_sta2.configure(highlightcolor="black")
        self.e_sta2.configure(insertbackground="black")
        self.e_sta2.configure(selectbackground="#c4c4c4")
        self.e_sta2.configure(selectforeground="black")
        self.e_sta2.configure(width=694)

        self.e_city = Entry(top)
        self.e_city.place(relx=0.13, rely=0.59,height=30, relwidth=0.41)
        self.e_city.configure(background="white")
        self.e_city.configure(disabledforeground="#a3a3a3")
        self.e_city.configure(font="TkFixedFont")
        self.e_city.configure(foreground="#000000")
        self.e_city.configure(highlightbackground="#d9d9d9")
        self.e_city.configure(highlightcolor="black")
        self.e_city.configure(insertbackground="black")
        self.e_city.configure(selectbackground="#c4c4c4")
        self.e_city.configure(selectforeground="black")

        self.lblfname = Label(top)
        self.lblfname.place(relx=0.13, rely=0.1, height=41, width=694)
        self.lblfname.configure(activebackground="#0066ab")
        self.lblfname.configure(activeforeground="white")
        self.lblfname.configure(activeforeground="#000000")
        self.lblfname.configure(background="#0066AB")
        self.lblfname.configure(disabledforeground="#0066AB")
        self.lblfname.configure(font=font12)
        self.lblfname.configure(foreground="#ffffff")
        self.lblfname.configure(text='''First Name''')
        self.lblfname.configure(width=694)

        self.lbllname = Label(top)
        self.lbllname.place(relx=0.61, rely=0.1, height=41, width=694)
        self.lbllname.configure(activebackground="#f9f9f9")
        self.lbllname.configure(activeforeground="#000000")
        self.lbllname.configure(background="#0066AB")
        self.lbllname.configure(disabledforeground="#a3a3a3")
        self.lbllname.configure(font=font12)
        self.lbllname.configure(foreground="#ffffff")
        self.lbllname.configure(highlightbackground="#d9d9d9")
        self.lbllname.configure(highlightcolor="black")
        self.lbllname.configure(text='''Last Name''')

        self.lblemail = Label(top)
        self.lblemail.place(relx=0.13, rely=0.25, height=41, width=1504)
        self.lblemail.configure(activebackground="#f9f9f9")
        self.lblemail.configure(activeforeground="#000000")
        self.lblemail.configure(background="#0066AB")
        self.lblemail.configure(disabledforeground="#a3a3a3")
        self.lblemail.configure(font=font12)
        self.lblemail.configure(foreground="#ffffff")
        self.lblemail.configure(highlightbackground="#d9d9d9")
        self.lblemail.configure(highlightcolor="black")
        self.lblemail.configure(text='''Email Address''')
        self.lblemail.configure(width=1504)

        self.lblsta1 = Label(top)
        self.lblsta1.place(relx=0.13, rely=0.39, height=41, width=694)
        self.lblsta1.configure(activebackground="#f9f9f9")
        self.lblsta1.configure(activeforeground="#000000")
        self.lblsta1.configure(background="#0066AB")
        self.lblsta1.configure(disabledforeground="#a3a3a3")
        self.lblsta1.configure(font=font12)
        self.lblsta1.configure(foreground="#ffffff")
        self.lblsta1.configure(highlightbackground="#d9d9d9")
        self.lblsta1.configure(highlightcolor="black")
        self.lblsta1.configure(text='''Street Address 1''')

        self.lblsta2 = Label(top)
        self.lblsta2.place(relx=0.61, rely=0.39, height=41, width=694)
        self.lblsta2.configure(activebackground="#f9f9f9")
        self.lblsta2.configure(activeforeground="#000000")
        self.lblsta2.configure(background="#0066AB")
        self.lblsta2.configure(disabledforeground="#a3a3a3")
        self.lblsta2.configure(font=font12)
        self.lblsta2.configure(foreground="#ffffff")
        self.lblsta2.configure(highlightbackground="#d9d9d9")
        self.lblsta2.configure(highlightcolor="black")
        self.lblsta2.configure(text='''Street Address 2''')

        self.lblcity = Label(top)
        self.lblcity.place(relx=0.13, rely=0.54, height=41, width=694)
        self.lblcity.configure(activebackground="#f9f9f9")
        self.lblcity.configure(activeforeground="#000000")
        self.lblcity.configure(background="#0066AB")
        self.lblcity.configure(disabledforeground="#a3a3a3")
        self.lblcity.configure(font=font12)
        self.lblcity.configure(foreground="#ffffff")
        self.lblcity.configure(highlightbackground="#d9d9d9")
        self.lblcity.configure(highlightcolor="black")
        self.lblcity.configure(text='''City''')

        self.lblstate = Label(top)
        self.lblstate.place(relx=0.61, rely=0.54, height=41, width=694)
        self.lblstate.configure(activebackground="#f9f9f9")
        self.lblstate.configure(activeforeground="#000000")
        self.lblstate.configure(background="#0066AB")
        self.lblstate.configure(disabledforeground="#a3a3a3")
        self.lblstate.configure(font=font12)
        self.lblstate.configure(foreground="#ffffff")
        self.lblstate.configure(highlightbackground="#d9d9d9")
        self.lblstate.configure(highlightcolor="black")
        self.lblstate.configure(text='''State''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.61, rely=0.59, relheight=0.04
                , relwidth=0.41)
        self.value_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                           "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                           "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                           "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                           "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=entry_support.combobox)
        self.TCombobox1.configure(width=693)
        self.TCombobox1.configure(takefocus="")

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()
