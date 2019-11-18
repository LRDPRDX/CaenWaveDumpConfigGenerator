from SWidget import * 


class SErrorDialog( SOkDialog ) :
    def __init__( self, master, style, errorText, auxText, **kwargs ) : 
        self.errorText = errorText
        self.auxText = auxText

        SOkDialog.__init__( self, master, style, **kwargs )


    def Body( self, master, style ) :
        errorText = SText( master, style,
                           height=2,
                           width=(max( len(self.errorText)+7, len(self.auxText) ) ) + 2)
        errorText.insert( "1.0", "ERROR: " + self.errorText + "\n" )
        errorText.tag_config( "error", foreground=style.theme["red"] )
        errorText.tag_add( "error", "1.0", "1.5" )
        errorText.tag_config( "center", justify="center" )
        errorText.tag_add( "center", "1.0", "end" )
        errorText.insert( "2.0", self.auxText, "center" )
        errorText.tag_add( "center", "2.0", "end" )
        errorText.pack( padx=5, pady=5 )


    def Apply( self ) :
        pass


class SInfoDialog( SOkDialog ) :
    def __init__( self, master, style, infoText, **kwargs ) :
        self.infoText = infoText

        SOkDialog.__init__( self, master, style, **kwargs )


    def Body( self, master, style ) :
        infoText = SText( master, style,
                          height=1,
                          width=len(self.infoText)+8)
        infoText.insert( "1.0", "INFO: " + self.infoText )
        infoText.tag_config( "info", foreground=style.theme["yellow"] )
        infoText.tag_add( "info", "1.0", "1.4" )
        infoText.tag_config( "center", justify="center" )
        infoText.tag_add( "center", "1.0", "end" )
        infoText.pack( padx=5, pady=5 )


    def Apply( self ) :
        pass
