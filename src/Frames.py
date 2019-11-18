try:
    import tkinter as tk 
except( ImportError ):
    import Tkinter as tk

from SWidget import *



class DividedFrame( SFrame ) :
    """
        This class represents a frame which 
        is divided into three subframes: bottom, middle and top
        and has a title in the top subframe
    """
    def __init__( self, parent, controller, style, title ) :
        SFrame.__init__( self, parent, style )  

        self.controller = controller
        self.style      = style
        self.title      = title.upper()

        self.CreateFrames()
        self.FillFrames()


    def CreateFrames( self ) :    
        self.topFrame = SFrame( self, self.style )  
        self.topFrame.pack( side="top", fill='x' )

        self.midFrame = SFrame( self, self.style )
        self.midFrame.pack( pady=5, fill='x' )

        self.bottomFrame = SFrame( self, self.style )
        self.bottomFrame.pack( side="bottom", fill='x' )


    def FillFrames( self ) :
        self.titleLabel = SLabel( self.topFrame, self.style, text=str( self.title ) )
        self.titleLabel.config( font=self.style.pageTitleFont, borderwidth=4, relief=tk.SUNKEN, padx=5 )
        self.titleLabel.pack( padx=20, pady=5 )


    def AlignColumns( self ):
        for i in range( self.midFrame.grid_size()[0] ):
            self.midFrame.grid_columnconfigure( i, weight=1 )



class GroupFrame( SFrame ) :
    """
        This class represents a frame with a title at the top
    """
    def __init__( self, parent, style, title, **kwargs ) :
        SFrame.__init__( self, parent, style, **kwargs )
        self.config( borderwidth=5, relief=tk.SUNKEN )

        self.style = style
        self.title = title.upper()

        self.CreateFrames()
        self.FillFrames()


    def CreateFrames( self ) :
        self.titleFrame = SFrame( self, self.style ) 
        self.titleFrame.pack( side="top", pady=10 )

        self.contentFrame = SFrame( self, self.style )
        self.contentFrame.pack( side="bottom", pady=(0, 10), fill='x' )


    def FillFrames( self ) :
        self.titleLabel = SLabel( self.titleFrame, self.style, text=str( self.title ) )
        self.titleLabel.config( font=self.style.groupTitleFont, borderwidth=3, relief=tk.SUNKEN , padx=3)
        self.titleLabel.pack( pady=(1, 5) )


    def AlignColumns( self ):
        for i in range( self.contentFrame.grid_size()[0] ):
            self.contentFrame.grid_columnconfigure( i, weight=1 )
