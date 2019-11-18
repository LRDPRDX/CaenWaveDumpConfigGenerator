try:
    from tkinter import font
except( ImportError ):
    import tkFont as font 



class SStyle :
    def __init__( self ) :
        self.smallFont       = font.Font( family="Courier", size=8, weight="bold" )
        self.widgetFont      = font.Font( family="Courier", size=10, weight="bold" )
        self.pageTitleFont   = font.Font( family="Courier", size=16, weight="bold" )
        self.groupTitleFont  = font.Font( family="Courier", size=12, weight="bold" )

        self.darkTheme = { "bg":"#303033",
                           "fg":"#54b7f3",
                           "hb":"#ff57d7",
                           "ab":"#90908d",
                           "scale":"#524e44",
                           "darkgrey":"#524e44",
                           "red":"#ff57d7",
                           "yellow":"#ffdf87",
                           "blue":"#9c4bff",
                           "darkblue":"#364495",
                           "grey":"#303033",
                           "purple":"#9c7ac7",
                           "black":"#000000" }

        self.lightTheme = { "bg": "#dcdad5",
                            "fg":"#364495",
                            "hb":"#000000",
                            "ab":"#b9b7b3",
                            "scale":"#b9b7b3",
                            "darkgrey":"#524e44",
                            "red":"#f000b7",
                            "yellow":"#ffff87",
                            "blue":"#9c7ac7",
                            "black":"#000000" }

        self.theme = self.lightTheme 
