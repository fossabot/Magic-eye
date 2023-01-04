from multiprocessing import parent_process
from multiprocessing.managers import Server
import gi
import os
gi.require_version('GstRtspServer', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Gst
from gi.repository import GstRtspServer
from Ui.AboutSection import  aboutSection
from gi.repository import Gst, GLib, GObject,Gtk,Gio,GdkPixbuf
import Server
class ServerAppWin(Gtk.ApplicationWindow):
    def onLoadDialogAbout(self,window):
            aboutSection.About(self)
    
    def on_button_toggled(self):
        print("penis")

    def __init__(self):
        super().__init__(title="headerBar")
        self.set_default_size(800, 450)
        self.set_border_width(10)
        self.init_ui()

    def init_ui(self):
        global state 
        global entry
        state =True
        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Magic Eye: Server"
        app_icon = Gtk.Image()
        filename = '/home/'+str(os.getlogin())+'/.local/share/icons/MagicEye-icon/magiceye-06'
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
        # Set the app icon for the image widget
        app_icon.set_from_icon_name("magiceye", Gtk.IconSize.BUTTON)

        # normal ui
        self.set_default_size(800, 450)
        self.set_border_width(10)
        entry = Gtk.Entry()


        grid = Gtk.Grid(row_spacing =10,column_spacing = 10,column_homogeneous = True)
        grid.set_row_homogeneous(False)
        grid.set_vexpand(True)
        grid.set_hexpand(True)
        self.add(grid)

        grid.set_column_spacing(10)
        grid.set_row_spacing(5)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        entry.set_editable(False)
        entry.set_placeholder_text("Server IP adress")
        grid.attach(entry,5 ,9, 1, 1)   
        frame = Gtk.Frame(label="Options")
        CamModeV4l2src = Gtk.CheckButton(label="v4l2src")
        CamModeV4l2src.connect("toggled", Server.on_button_toggled)
        vbox.add(CamModeV4l2src)
        frame.add(vbox)
        print(CamModeV4l2src.get_active())
        vbox.set_border_width(10)
        connectButton = Gtk.Button(label="start stream")
        connectButton.connect("clicked",Server.Connect)

        grid.attach(connectButton, 5,6, 1, 1)
        #for config['CAMERA_OPTION'].items in config['CAMERA_OPTION']:
         #    CamModeRpicam = Gtk.CheckButton(label="rpicamsrc")
          #   CamModeRpicam.connect("toggled", self.on_button_toggled, "rpicamsrc")
           #  grid.attach(frame,0,0,2,1)
            # vbox.add(CamModeRpicam)
        CamModeRpicam = Gtk.CheckButton(label="rpicamsrc")
        CamModeRpicam.connect("toggled", self.on_button_toggled, "rpicamsrc")
        grid.attach(frame,0,0,2,1)
        vbox.add(CamModeRpicam)

        CamModeV4l2src.set_tooltip_text("This option is for camera like a laptop webcam or any other external webcam and the raspberrypi (64 bits OS)")
        CamModeRpicam.set_tooltip_text("(Leagacy option )This option is made for the camera module of the raspberrypi.For best result use it if your OS is 32 bits. ")
        print(CamModeRpicam.get_active())
        def on_destroy(win):
            try:
                Gtk.main_quit()
            except KeyboardInterrupt:
                pass

        self.connect('destroy', on_destroy)

    def Set_Entry(ip):
         entry.set_text(ip)