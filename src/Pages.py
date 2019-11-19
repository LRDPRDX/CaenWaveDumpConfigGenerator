#external imports:
try:
    import tkinter as tk 
except( ImportError ):
    import Tkinter as tk
##for xterm:
import subprocess, shlex


#internal imports
from Frames import (DividedFrame, GroupFrame)
from SWidget import *
from Dialogs import * 



class BackSavePage( DividedFrame ) :
    """
        This class represents a DividedFrame (see above)
        with two buttons: BACK and SAVE in the bottom frame
    """

    def __init__( self, parent, controller, style, title ) :
        DividedFrame.__init__( self, parent, controller, style, title ) 

        self.CreateButtons()


    def CreateButtons( self ) :
        self.backButton = SButton( self.bottomFrame, self.style,
                                   text="Back",
                                   command=lambda: self.controller.ShowPage( "Start" ) )
        self.backButton.config( font=self.style.groupTitleFont,
                                bg=self.style.theme["fg"], fg=self.style.theme["bg"] )
        self.backButton.pack(side='left', pady=15, padx=10 )

        self.saveButton = SButton( self.bottomFrame, self.style,
                                   text="Save",
                                   command=lambda: self.controller.Save() )
        self.saveButton.config( font=self.style.groupTitleFont,
                                bg=self.style.theme["fg"], fg=self.style.theme["bg"] )
        self.saveButton.pack( side='right', pady=15, padx=10 )



class StartPage( DividedFrame ) :
    """
        Creates the starting page
    """
    def __init__( self, parent, controller, style, title ):
        DividedFrame.__init__( self, parent, controller, style, title )

        #Create working areas
        self.InitPageArea()
        self.InitConnectionArea()
        self.AlignColumns()

        #QUIT button at the bottom 
        quitButton = SButton( self.bottomFrame, self.style,
                              text="EXIT",
                              command=lambda: controller.Exit() )
        quitButton.config( font=self.style.groupTitleFont,
                           bg=self.style.theme["red"], fg=self.style.theme["bg"],
                           highlightbackground=self.style.theme["fg"] )
        quitButton.pack( pady=15 )


    def InitPageArea( self ):
        #button to common settings' page: settings for all channels
        self.settingsFrame = GroupFrame( self.midFrame, self.style, "SETTINGS" )
        self.settingsFrame.grid( row=0, column=0, pady=10, padx=10, sticky="ew" )

        self.commonButton = SButton( self.settingsFrame.contentFrame, self.style,
                                     text="Common Settings",
                                     command=lambda: self.controller.ShowPage( "Common" ),
                                     height=2 )
        self.commonButton.grid( row=0, column=0, padx=10, sticky="ew" )
        #button to individual settings' page: settings per channel
        self.individButton = SButton( self.settingsFrame.contentFrame, self.style,
                                      text="Individual Settings",
                                      command=lambda: self.controller.ShowPage( "Individual" ),
                                      height=2 )
        self.individButton.grid( row=0, column=1, padx=10, sticky="ew" )
        #terminal button
        self.terminalButton = SButton( self.settingsFrame.contentFrame, self.style,
                                       text="Terminal",
                                       command=lambda: self.controller.ShowPage( "Terminal" ),
                                       height=2 )
        self.terminalButton.grid( row=0, column=2, padx=10, sticky="ew" )
        #
        self.settingsFrame.AlignColumns()


    def InitConnectionArea( self ):
        self.connectionFrame = GroupFrame( self.midFrame, self.style, "CONNECTION" )
        self.connectionFrame.grid( row=1, column=0, padx=10, pady=5, sticky="ew" )

        self.linkTypeLabel = SLabel( self.connectionFrame.contentFrame, self.style,
                                     text="Link type:" )
        self.linkTypeLabel.grid( row=0, column=0, sticky="ew", padx=(10, 0) )

        self.linkTypeOption = SOptionMenu( self.connectionFrame.contentFrame, self.style,
                                           self.controller.conf.connection.linkType,
                                          *self.controller.conf.connection.linkTypes )
        self.linkTypeOption.grid( row=0, column=1, padx=( 0, 10 ), sticky="ew" )

        self.linkNumberLabel = SLabel( self.connectionFrame.contentFrame, self.style,
                                       text="Link number:" )
        self.linkNumberLabel.grid( row=0, column=2, sticky="ew" )

        self.linkNumberEntry = SEntry( self.connectionFrame.contentFrame, self.style,
                                       width=2,
                                       textvariable=self.controller.conf.connection.linkNumber )
        self.linkNumberEntry.grid( row=0, column=3, padx=( 0, 10 ) )

        self.nodeNumberLabel = SLabel( self.connectionFrame.contentFrame, self.style,
                                       text="Node number:" )
        self.nodeNumberLabel.grid( row=0, column=4, sticky="ew" )

        self.nodeNumberEntry = SEntry( self.connectionFrame.contentFrame, self.style,
                                       width=2,
                                       textvariable=self.controller.conf.connection.nodeNumber )
        self.nodeNumberEntry.grid( row=0, column=5, padx=( 0, 10 ) )

        self.baseAddressLabel = SLabel( self.connectionFrame.contentFrame, self.style,
                                        text="Base address:" )
        self.baseAddressLabel.grid( row=0, column=6, sticky="ew" )

        self.baseAddressEntry = SEntry( self.connectionFrame.contentFrame, self.style,
                                        width=8,
                                        textvariable=self.controller.conf.connection.baseAddress )
        self.baseAddressEntry.grid( row=0, column=7, padx=( 0, 10 ) )
        #
        self.connectionFrame.AlignColumns()

        #Check to skip DAC calibration at start up
        self.skipCalibCheck = SCheckButton( self.midFrame, self.style,
                                            text=" Skip startup calibration",
                                            variable=self.controller.conf.common.pd["SKIP_STARTUP_CALIBRATION"],
                                            onvalue="YES", offvalue="NO" )
        self.skipCalibCheck.grid( row=2, column=0, sticky="e", padx=(0, 10), pady=5 )



class CommonSettingsPage( BackSavePage ) :
    """
        Creates the common settings' page
    """
    def __init__( self, parent, controller, style, title ):
        BackSavePage.__init__( self, parent, controller, style, title )

        self.InitOutputArea()
        self.InitTriggerArea()
        self.InitLogicLevelArea()
        self.InitGNUArea()
        self.InitRecordingArea()

        self.AlignColumns()


    def InitOutputArea( self ):
        self.outputFrame = GroupFrame( self.midFrame, self.style, "OUTPUT" )
        self.outputFrame.grid( row=0, pady=5, padx=10, sticky="nsew", columnspan=2 )

        self.pathLabel = SLabel( self.outputFrame.contentFrame, self.style,
                                 text="Save to:" )
        self.pathLabel.grid( row=0, column=0, sticky="w", padx=(10, 0) )

        self.pathEntry = SEntry( self.outputFrame.contentFrame, self.style,
                                 width=30,
                                 textvariable=self.controller.conf.pathToFile )
        self.pathEntry.grid( row=0, column=1, padx=( 0, 10 ) )

        self.browseButton = SButton( self.outputFrame.contentFrame, self.style,
                                     text="Browse",
                                     command=lambda: self.controller.DefinePath() )
        self.browseButton.grid( row=0, column=2, padx=( 0, 30 ) )

        self.formatLabel = SLabel( self.outputFrame.contentFrame, self.style,
                                   text="Format:" )
        self.formatLabel.grid( row=0, column=3, sticky="w" )

        self.formatOption = SOptionMenu( self.outputFrame.contentFrame, self.style,
                                         self.controller.conf.common.pd["OUTPUT_FILE_FORMAT"],
                                        *self.controller.conf.common.formats )
        self.formatOption.config( width=6 )
        self.formatOption.grid( row=0, column=4, padx=( 0, 30 ), sticky="ew" )

        self.headerButton = SCheckButton( self.outputFrame.contentFrame, self.style,
                                          variable=self.controller.conf.common.pd["OUTPUT_FILE_HEADER"],
                                          onvalue="YES", offvalue="NO",
                                          text=" Save header" )
        self.headerButton.grid( row=0, column=5, sticky="ew", padx=(0, 10) )
        #
        self.outputFrame.AlignColumns()


    def InitTriggerArea( self ):
        self.triggerFrame = GroupFrame( self.midFrame, self.style, "TRIGGER" )
        self.triggerFrame.grid( row=1, pady=5, padx=10, columnspan=2, sticky="ew" )

        self.polarityLabel = SLabel( self.triggerFrame.contentFrame, self.style,
                                     text="Polarity:" )
        self.polarityLabel.grid( row=0, column=0, sticky="ew", padx=(10, 0) )

        self.polarityOption = SOptionMenu( self.triggerFrame.contentFrame, self.style,
                                           self.controller.conf.common.pd["PULSE_POLARITY"],
                                          *self.controller.conf.common.polarities )
        self.polarityOption.grid( row=0, column=1, padx=( 0, 30 ), sticky="ew" )

        self.externalLabel = SLabel( self.triggerFrame.contentFrame, self.style,
                                     text="External trigger:" )
        self.externalLabel.grid( row=0, column=2, sticky="ew" )

        self.externalOption = SOptionMenu( self.triggerFrame.contentFrame, self.style,
                                           self.controller.conf.common.pd["EXTERNAL_TRIGGER"],
                                          *self.controller.conf.common.extTriggers,
                                          command=self.ManageTrigger )
        self.externalOption.config( width=24 )
        self.externalOption.grid( row=0, column=3, padx=( 0, 30 ), sticky="ew" )

        self.postTriggerLabel = SLabel( self.triggerFrame.contentFrame, self.style,
                                        text="Post trigger (%):" )
        self.postTriggerLabel.grid( row=0, column=4, sticky="ew" )

        self.postTriggerEntry = SEntry( self.triggerFrame.contentFrame, self.style,
                                        width=4,
                                        textvariable=self.controller.conf.common.pd["POST_TRIGGER"] )
        self.postTriggerEntry.grid( row=0, column=5, padx=( 0, 10 ), sticky="ew" )
        #
        self.triggerFrame.AlignColumns()


    def InitLogicLevelArea( self ):
        self.ioLevelFrame = GroupFrame( self.midFrame, self.style, "I/O LEVEL" )
        self.ioLevelFrame.grid( row=2, column=0, padx=10, pady=5, sticky="nsew" )

        self.radioTTL = SRadioButton( self.ioLevelFrame.contentFrame, self.style,
                                      text=" TTL",
                                      variable=self.controller.conf.common.pd["FPIO_LEVEL"],
                                      value=self.controller.conf.common.ioLevels[0] )
        self.radioTTL.grid( row=0, column=0, sticky="ew", padx=10 )

        self.radioNIM = SRadioButton( self.ioLevelFrame.contentFrame, self.style,
                                      text=" NIM",
                                      variable=self.controller.conf.common.pd["FPIO_LEVEL"],
                                      selectcolor=self.style.theme["bg"],
                                      value=self.controller.conf.common.ioLevels[1] )
        self.radioNIM.grid( row=0, column=1, sticky="ew", padx=10 )
        #
        self.ioLevelFrame.AlignColumns()


    def InitGNUArea( self ):
        self.drawingFrame = GroupFrame( self.midFrame, self.style, "DRAWING" )
        self.drawingFrame.grid( row=3, column=0, padx=10, pady=5, sticky="nsew" )

        self.pathToGnuPlotLabel = SLabel( self.drawingFrame.contentFrame, self.style,
                                          text="Path to GNU Plot:" )
        self.pathToGnuPlotLabel.grid( row=0, column=0, sticky="w", pady=5, padx=(10, 0) )

        self.pathToGnuPlotEntry = SEntry( self.drawingFrame.contentFrame, self.style,
                                          width=20,
                                          textvariable=self.controller.conf.gnuPath )
        self.pathToGnuPlotEntry.grid( row=0, column=1, padx=(0, 10), sticky="ew" )
        #
        self.drawingFrame.AlignColumns()


    def InitRecordingArea( self ):
        self.recordFrame = GroupFrame( self.midFrame, self.style, "DATA & RECORDING" )
        self.recordFrame.grid( row=2, column=1, padx=10, pady=5, sticky="nsew", rowspan=2 )

        self.recordLengthLabel = SLabel( self.recordFrame.contentFrame, self.style,
                                         text="Record length (samples):" )
        self.recordLengthLabel.grid( row=0, column=0, sticky="nsw", pady=5, padx=(10, 0) )

        self.recordLengthEntry = SEntry( self.recordFrame.contentFrame, self.style,
                                         width=10,
                                         textvariable=self.controller.conf.common.pd["RECORD_LENGTH"] )
        self.recordLengthEntry.grid( row=0, column=1, sticky="nsew", pady=5, padx=(0, 10) )

        self.maxNumEventsLabel = SLabel( self.recordFrame.contentFrame, self.style,
                                         text="Maximum number of events per block:" )
        self.maxNumEventsLabel.grid( row=1, column=0, sticky="nsw", pady=5, padx=(10, 0) )

        self.maxNumEventsEntry = SEntry( self.recordFrame.contentFrame, self.style,
                                         width=9,
                                         textvariable=self.controller.conf.common.pd["MAX_NUM_EVENTS_BLT"] )
        self.maxNumEventsEntry.grid( row=1, column=1, sticky="nsew", pady=5, padx=(0, 10) )

        self.useInterruptLabel = SLabel( self.recordFrame.contentFrame, self.style,
                                         text="Set interrupt after (events):" )
        self.useInterruptLabel.grid( row=2, column=0, sticky="nsw", pady=5, padx=(10, 0) )

        self.useInterruptEntry = SEntry( self.recordFrame.contentFrame, self.style,
                                         width=9,
                                         textvariable=self.controller.conf.common.pd["USE_INTERRUPT"] )
        self.useInterruptEntry.grid( row=2, column=1, sticky="nsew", pady=5, padx=(0, 10) )

        self.testPatternButton = SCheckButton( self.recordFrame.contentFrame, self.style,
                                               variable=self.controller.conf.common.pd["TEST_PATTERN"],
                                               text=" Activate test pattern" )
        self.testPatternButton.grid( row=3, column=0, sticky="ne", columnspan=2, pady=5, padx=(0, 10) )
        self.recordFrame.AlignColumns()


    def ManageTrigger( self, value ):
        if( value != "DISABLED" ):
            if( value == "ACQUISITION_ONLY" ):
                #channel trigger can be either trigger out only or disabled
                for ch in self.controller.conf.channel:
                    if( ch.pd["CHANNEL_TRIGGER"].get() != "TRGOUT_ONLY" ):
                        ch.pd["CHANNEL_TRIGGER"].set( "DISABLED" )
            else:
                #channel trigger can be only disabled
                for ch in self.controller.conf.channel:
                    ch.pd["CHANNEL_TRIGGER"].set( "DISABLED" )
        else:
            #nothing to do if external trigger disabled
            pass



class ChannelFrame( GroupFrame ):
    def __init__( self, parent, controller, style, i ):
        GroupFrame.__init__( self, parent, style, "CH"+str(i)+" SETTINGS" )

        self.i          = i
        self.controller = controller

        self.checkEnable = SCheckButton( self.contentFrame, self.style,
                                         variable=self.controller.conf.channel[i].pd["ENABLE_INPUT"],
                                         onvalue="YES", offvalue="NO",
                                         text=" Enable input" )
        self.checkEnable.grid( row=0, column=0, sticky="nw", pady=5, padx=(10, 10) )

        self.InitTriggerArea()
        self.InitBaselineArea()

        self.AlignColumns()


    def InitTriggerArea( self ):
            self.triggerFrame = GroupFrame( self.contentFrame, self.style, "TRIGGER" )
            self.triggerFrame.grid( row=1, column=0, sticky="nsew", padx=10, pady=5 )

            self.channelTrigLabel = SLabel( self.triggerFrame.contentFrame, self.style,
                                            text="Channel trigger:" )
            self.channelTrigLabel.grid( row=0, column=0, padx=(10, 0) )

            self.channelTrigOption = SOptionMenu( self.triggerFrame.contentFrame, self.style,
                                                  self.controller.conf.channel[self.i].pd["CHANNEL_TRIGGER"],
                                                 *self.controller.conf.channel[self.i].triggers,
                                                 command=self.ManageTrigger )
            self.channelTrigOption.config( width=24 )
            self.channelTrigOption.grid( row=0, column=1, padx=(0, 10), sticky="ew" )

            self.triggerThreshLabel = SLabel( self.triggerFrame.contentFrame, self.style,
                                              text="Trigger threshold:" )
            self.triggerThreshLabel.grid( row=0, column=2, padx=(10, 0) );

            self.triggerThreshEntry = SEntry( self.triggerFrame.contentFrame, self.style,
                                              width=5,
                                              textvariable=self.controller.conf.channel[self.i].pd["TRIGGER_THRESHOLD"] )
            self.triggerThreshEntry.grid( row=0, column=3, padx=(0, 10) )
            #
            self.triggerFrame.AlignColumns()


    def InitBaselineArea( self ):
            self.baselineFrame = GroupFrame( self.contentFrame, self.style, "BASELINE" )
            self.baselineFrame.grid( row=2, column=0, sticky="nsew", padx=10, pady=5 )

            self.baseScale = SScale( self.baselineFrame.contentFrame, self.style,
                                     from_=100, to=0,
                                     variable=self.controller.conf.channel[self.i].pd["BASELINE_SHIFT"],
                                     label="Baseline shift" )
            self.baseScale.grid( row=0, column=0, pady=5, padx=(10, 10), sticky="nsew" )

            self.offsetScale = SScale( self.baselineFrame.contentFrame, self.style,
                                       from_=50, to=-50,
                                       variable=self.controller.conf.channel[self.i].pd["DC_OFFSET"],
                                       label="DC offset" )
            self.offsetScale.grid( row=0, column=1, pady=5, padx=(10, 10), sticky="nsew" )
            self.offsetScale.config( state="disabled", showvalue=False )

            self.offsetCheck = SCheckButton( self.baselineFrame.contentFrame, self.style,
                                             text=" Use DC offset",
                                             variable=self.controller.conf.channel[self.i].useOffset,
                                             command=self.ManageBaseline,
                                             onvalue=1, offvalue=0 )
            self.offsetCheck.grid( row=0, column=2, pady=5, padx=(0, 10), sticky="sew" )
            #
            self.baselineFrame.AlignColumns()


    def ManageBaseline( self ):
        if( self.controller.conf.channel[self.i].useOffset.get() ):
            self.baseScale.config( state="disabled", showvalue=False )
            self.offsetScale.config( state="normal", showvalue=True )
        else:
            self.baseScale.config( state="normal", showvalue=True )
            self.offsetScale.config( state="disabled", showvalue=False )


    def ManageTrigger( self, value ):
        if( value != "DISABLED" ):
            if( value == "TRGOUT_ONLY" ):
                #in this case external trigger can be acquisition only
                if( self.controller.conf.common.pd["EXTERNAL_TRIGGER"].get() != "ACQUISITION_ONLY" ):
                    self.controller.conf.common.pd["EXTERNAL_TRIGGER"].set( "DISABLED" )

                for (i,ch) in enumerate(self.controller.conf.channel):
                    if i != self.i:
                        #other channel can be either only acquisition or disabled
                        if( ch.pd["CHANNEL_TRIGGER"].get() != "ACQUISITION_ONLY" ):
                            ch.pd["CHANNEL_TRIGGER"].set( "DISABLED" )
            else:
                #in this case external trigger can be only disabled
                self.controller.conf.common.pd[ "EXTERNAL_TRIGGER"].set( "DISABLED" )

                if( value == "ACQUISITION_ONLY" ):
                    #other channel can be either trigger or disabled
                    for (i,ch) in enumerate(self.controller.conf.channel):
                        if i != self.i:
                            if( ch.pd["CHANNEL_TRIGGER"].get() != "TRGOUT_ONLY" ):
                                ch.pd["CHANNEL_TRIGGER"].set( "DISABLED" )
                else:
                    #other channel can be only disabled
                    for (i,ch) in enumerate(self.controller.conf.channel):
                        if i != self.i:
                            ch.pd["CHANNEL_TRIGGER"].set( "DISABLED" )
        else:
            #nothing to do if this channel disabled
            pass



class IndividSettingsPage( BackSavePage ) :
    """
        Creates the individual settings' page:
        settings per individual channel
    """
    def __init__( self, parent, controller, style, title ):
        BackSavePage.__init__( self, parent, controller, style, title )

        self.noteBook = ttk.Notebook( self.midFrame )
        self.noteBook.grid( row=0, column=0, sticky="news", padx=10, pady=5 )

        self.channelFrame = [ None for ch in self.controller.conf.channel ]
        for i, ch in enumerate( self.controller.conf.channel ) :
            self.channelFrame[i] = ChannelFrame( self.midFrame, self.controller, self.style, i )
            self.channelFrame[i].grid( row=0, column=0, padx=10, pady=5, sticky="nsew" )

            self.noteBook.add( self.channelFrame[i], text="CH"+str(i) )

        self.AlignColumns()



class TerminalPage( BackSavePage ) :
    def __init__( self, parent, controller, style, title ):
        BackSavePage.__init__( self, parent, controller, style, title )

        self.InitTerminalArea()
        self.InitHintArea()
        self.AlignColumns()


    def InitTerminalArea( self ):
        #place XTerm
        self.terminalFrame = SFrame( self.midFrame, self.style, width=700, height=90 )
        self.terminalFrame.grid( row=0, column=0, sticky="nsew", padx=10, pady=5 )
        self.terminalCommand = '/usr/bin/env xterm -into %d -geometry 120x5 -fa \'courier\' -fs 10 -fg \'#54b7f3\' +sb' % self.terminalFrame.winfo_id() 
        self.terminalProcess = subprocess.Popen( shlex.split( self.terminalCommand ) )


    def InitHintArea( self ):
        #Online wavedump commands area
        self.commandFrame = GroupFrame( self.midFrame, self.style, "ONLINE COMMANDS" )
        self.commandFrame.grid( row=1, column=0, sticky="nsew", padx=10, pady=10 )

        self.CreateTermHint()
        self.CreateGNUHint()

        self.commandFrame.AlignColumns()


    def CreateTermHint( self ):
        self.commandTerm = GroupFrame( self.commandFrame.contentFrame, self.style, "INSIDE THE TERMINAL WINDOW" )
        self.commandTerm.grid( row=0, column=0, sticky="nsew", padx=10, pady=5 )

        commands1 = SText( self.commandTerm.contentFrame, self.style,
                           width=39, height=8 )
        commands1.insert( "1.0", "s       - Start/Stop acquisition\n" )
        commands1.insert( "2.0", "q       - Quit WaveDump\n" )
        commands1.insert( "3.0", "R       - Restrart acquisition\n" )
        commands1.insert( "4.0", "c       - Perform channel calibration\n" )
        commands1.insert( "5.0", "m       - Display temperature\n\n\n" )
        commands1.insert( "8.0", "[Space] - Display online help\n" )
        for i in range(1, 9) :
            commands1.tag_add( "key", "%d.0" % i, "%d.7" % i )
            commands1.tag_config( "key", foreground=self.style.theme["yellow"] )
        commands1.config( state="disabled" )
        commands1.grid( row=0, column=0, padx=10, pady=5, sticky="ew" )

        commands2 = SText( self.commandTerm.contentFrame, self.style,
                           width=39, height=8 )
        commands2.insert( "1.0", "t - Single software trigger\n" )
        commands2.insert( "2.0", "T - Continuous software trigger\n" )
        commands2.insert( "3.0", "p - Single event-plot\n" )
        commands2.insert( "4.0", "P - Continuous plot\n" )
        commands2.insert( "5.0", "w - Save single event to disk\n" )
        commands2.insert( "6.0", "W - Continuous event saving\n" )
        commands2.insert( "7.0", "f - Toggle waveform/FFT\n" )
        commands2.insert( "8.0", "h - Toggle waveform/amplitude\n" )
        for i in range(1, 9) :
            commands2.tag_add( "key", "%d.0" % i, "%d.1" % i )
            commands2.tag_config( "key", foreground=self.style.theme["yellow"] )
        commands2.config( state="disabled" )
        commands2.grid( row=0, column=1, padx=10, pady=5, sticky="ew" )

        self.commandTerm.AlignColumns()


    def CreateGNUHint( self ):
        self.commandGNU = GroupFrame( self.commandFrame.contentFrame, self.style, "INSIDE THE GNUPLOT WINDOW" )
        self.commandGNU.grid( row=1, column=0, sticky="nsew", padx=10, pady=5 )

        commands3 = SText( self.commandGNU.contentFrame, self.style,
                           width=80, height=5 )
        commands3.insert( "1.0", "a - Autoscale\n" )
        commands3.insert( "2.0", "r - Enable/Disable ruler\n" )
        commands3.insert( "3.0", "g - Enable/Disable grid\n" )
        commands3.insert( "4.0", "y - Autoscale along y-axis\n" )
        commands3.insert( "5.0", "p - Return to previous zoom\n" )
        commands3.config( state="disabled" )
        commands3.grid( row=1, column=0, padx=10, pady=5, sticky="ew" )
        for i in range(1, 6) :
            commands3.tag_add( "key", "%d.0" % i, "%d.1" % i )
            commands3.tag_config( "key", foreground=self.style.theme["yellow"] )

        self.commandGNU.AlignColumns()
