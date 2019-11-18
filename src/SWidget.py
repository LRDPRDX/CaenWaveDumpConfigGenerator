try:
    import tkinter as tk
    from tkinter import ttk
except( ImportError ):
    import Tkinter as tk
    import ttk



class SButton( tk.Button ) :
    def __init__( self, master, style, **options ) :
        tk.Button.__init__( self, master, **options ) 
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     activebackground=style.theme["ab"],
                     borderwidth=2 )


class SFrame( tk.Frame ) :
    def __init__( self, master, style, **options ) :
        tk.Frame.__init__( self, master, **options )
        self.config( bg=style.theme["bg"] ) 


class SLabel( tk.Label ) :
    def __init__( self, master, style, **options ) :
        tk.Label.__init__( self, master, **options )
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"] )


class SScale( tk.Scale ) :
    def __init__( self, master, style, **options ) :
        tk.Scale.__init__( self, master, **options )
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     activebackground=style.theme["ab"],
                     troughcolor=style.theme["scale"] )


class SEntry( tk.Entry ) :
    def __init__( self, master, style, **options ) :
        tk.Entry.__init__( self, master, **options )
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     borderwidth=2, relief=tk.SUNKEN )


class SCheckButton( tk.Checkbutton ) :
    def __init__( self, master, style, **kwargs ) :
        tk.Checkbutton.__init__( self, master, **kwargs )
        self.config( font=style.widgetFont, selectcolor=style.theme["bg"],
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     activebackground=style.theme["ab"] )


class SRadioButton( tk.Radiobutton ) :
    def __init__( self, master, style, cnf={}, **kwargs ) :
        tk.Radiobutton.__init__( self, master, cnf, **kwargs )
        self.config( font=style.widgetFont, selectcolor=style.theme["bg"],
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     activebackground=style.theme["ab"] )


class SOptionMenu( tk.OptionMenu ) :
    def __init__( self, master, style, variable, value, *values, **kwargs ) :
        tk.OptionMenu.__init__( self, master, variable, value, *values, **kwargs )
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"],
                     activebackground=style.theme["ab"],
                     borderwidth=2 )
        self.nametowidget( self.menuname ).config( font=style.widgetFont,
                                                   bg=style.theme["bg"], fg=style.theme["fg"], activebackground=style.theme["ab"] )


class SText( tk.Text ) :
    def __init__( self, master, style, **kwargs ) :
        tk.Text.__init__( self, master, **kwargs )
        self.config( font=style.widgetFont,
                     bg=style.theme["bg"], fg=style.theme["fg"],
                     highlightbackground=style.theme["hb"] )


class SOkDialog( tk.Toplevel ) :
    def __init__( self, master, style, **kwargs ) :
        tk.Toplevel.__init__( self, master, **kwargs )
        self.config( bg=style.theme["bg"] )

        self.transient( master )
        self.parent = master

        body = SFrame( self, style )
        self.initial_focus = self.Body( body, style )
        body.pack( padx=5, pady=5 )

        self.Buttonbox( style ) 

        self.grab_set()

        if not self.initial_focus :
            self.initial_focus = self

        self.protocol( "WM_DELETE_WINDOW", self.OK )

        self.geometry( "+%d+%d" % (master.winfo_width()/2,
                                   master.winfo_height()/2) )

        self.initial_focus.focus_set()

        self.wait_window( self )


    def Body( self, master, style ) : 
        pass #override


    def Buttonbox( self, style ) :
        box = SFrame( self, style )

        okButton = SButton( box, style,
                            text="OK", width=10,
                            command=self.OK )
        okButton.pack( padx=5, pady=5 )

        self.bind( "<Return>", self.OK )

        box.pack()


    def OK( self, event=None ) :
        self.withdraw()
        self.update_idletasks()
        self.Apply()
        self.parent.focus_set()
        self.destroy()
