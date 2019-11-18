try:
    import tkinter as tk
except( ImportError ):
    import Tkinter as tk

class Configuration :
    def __init__( self, nChannels ) :
        self.maxNumChannels = 16
        self.pathToFile     = tk.StringVar( value="./" )
        self.gnuPath        = tk.StringVar( value="/usr/bin/" )

        self.connection     = Connection()
        self.common         = Common()

        self.channel        = []
        for i in range( 0, nChannels ) : 
            self.channel.append( Channel() )


class Connection : 
    def __init__( self ) :
        self.linkTypes      = [ "USB", "PCI" ]
        self.linkType       = tk.StringVar( value="USB" )
        self.linkNumber     = tk.IntVar( value=0 )
        self.nodeNumber     = tk.IntVar( value=0 )
        self.baseAddress    = tk.IntVar( value=0 )


class Common :
    def __init__( self ) :
        self.pd                                 = {}

        self.pd[ "SKIP_STARTUP_CALIBRATION" ]   = tk.StringVar( value="NO" )
        self.formats                            = [ "BINARY", "ASCII" ]
        self.pd[ "OUTPUT_FILE_FORMAT" ]         = tk.StringVar( value="BINARY" )
        self.pd[ "OUTPUT_FILE_HEADER" ]         = tk.StringVar( value="YES" )
        self.polarities                         = [ "NEGATIVE", "POSITIVE" ]
        self.pd[ "PULSE_POLARITY" ]             = tk.StringVar( value="NEGATIVE" )
        self.extTriggers                        = [ "DISABLED", "ACQUISITION_ONLY", "ACQUISITION_AND_TRGOUT" ]
        self.pd[ "EXTERNAL_TRIGGER" ]           = tk.StringVar( value="DISABLED" )
        self.pd[ "POST_TRIGGER" ]               = tk.IntVar( value=50 )
        self.ioLevels                           = [ "TTL", "NIM" ]
        self.pd[ "FPIO_LEVEL" ]                 = tk.StringVar( value="TTL" )
        self.pd[ "RECORD_LENGTH" ]              = tk.IntVar( value=100 )
        self.pd[ "MAX_NUM_EVENTS_BLT" ]         = tk.IntVar( value=1 )
        self.pd[ "TEST_PATTERN" ]               = tk.StringVar( value="NO" )
        self.pd[ "USE_INTERRUPT" ]              = tk.IntVar( value=0 )


class Channel :
    def __init__( self ) :
        self.useOffset                          = tk.IntVar( value=0 )
        self.pd                                 = {}
        self.pd[ "ENABLE_INPUT" ]               = tk.StringVar( value="NO" )
        self.pd[ "BASELINE_SHIFT" ]             = tk.IntVar( value=50 )
        self.pd[ "DC_OFFSET" ]                  = tk.IntVar( value=0 )
        self.triggers                           = ["DISABLED", "ACQUISITION_ONLY", "ACQUISITION_AND_TRGOUT", "TRGOUT_ONLY"]
        self.pd[ "CHANNEL_TRIGGER" ]            = tk.StringVar( value="ACQUISITION_ONLY" )
        self.pd[ "TRIGGER_THRESHOLD" ]          = tk.IntVar( value=5 )
