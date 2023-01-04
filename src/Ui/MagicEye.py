#!/bin/env python3
import gi
import os
from Ui.AboutSection import  aboutSection
from Ui.Client import ClientAppWin
gi.require_version('GstVideo', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Gst, GLib, GObject,Gtk,Gio,GdkPixbuf
from gi.repository import Gdk, GstVideo




class AppWin(Gtk.ApplicationWindow):
    def onLoadDialogAbout(self,window):
        aboutSection.About(self)
   

    def __init__(self):
        super().__init__(title="headerBar")
        self.set_default_size(800, 450)
        self.set_border_width(10)
        self.init_ui()
       
       # self.connect("destroy", self.on_destroy)
    def Load_client(self,window):
        import Client as client
        print("client loaded")
        client.main()
        client.Player.__init__

    def Load_server(self,window):
        import Server as server
        print("s")
        server.main()
        server.Init_Ui.__init__
    def init_ui(self):
        self.set_default_size(800, 450)
        self.set_border_width(10)

        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Magic Eye"
        app_icon = Gtk.Image()
        filename = '/home/'+str(os.getlogin())+'/.local/share/icons/MagicEye-icon/magiceye-06'

        # Set the app icon for the image widget
        app_icon.set_from_icon_name("magiceye", Gtk.IconSize.BUTTON)

        grid = Gtk.Grid(row_spacing =10,column_spacing = 10,column_homogeneous = True)
        clientBtn = Gtk.Button(label="client")
        #module1 = client.import_module('module1')
        clientBtn.connect("clicked",self.Load_client)

        serverBtn = Gtk.Button(label="Server")
        serverBtn.connect("clicked",self.Load_server)
        headerBar.pack_start(app_icon)
        self.set_titlebar(headerBar)

        self.popover = Gtk.Popover()

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        aboutBtn=Gtk.Button(label="About",relief=2)
        optionBtn=Gtk.Button(label="Option",relief=2)

        vbox.pack_start(aboutBtn, False, True, 10)
        vbox.pack_end(optionBtn,False, True, 10)

        #optionBtn.connect("clicked",self.onLoadOption)
        aboutBtn.connect("clicked",self.onLoadDialogAbout)

        vbox.show_all()
        

        self.popover.add(vbox)
        self.popover.set_position(Gtk.PositionType.BOTTOM)

        button = Gtk.MenuButton(popover=self.popover)

        #look in user icon dir
        icon = Gio.ThemedIcon(name="open-menu-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        headerBar.pack_end(button)

        grid.add(clientBtn)
        grid.attach(serverBtn, 1, 0, 1, 1)
        self.add(grid)
        
        def on_destroy(win):
            try:
                Gtk.main_quit()
            except KeyboardInterrupt:
                pass

        self.connect('destroy', on_destroy)
 

      
