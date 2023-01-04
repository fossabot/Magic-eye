import gi
import os
from Ui.AboutSection import aboutSection 
gi.require_version('GstVideo', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Gst, GLib, GObject,Gtk,Gio,GdkPixbuf
from gi.repository import Gdk, GstVideo
from Ui.GstPlayer import GstWidget as Player 
class ClientAppWin(Gtk.ApplicationWindow):

    def onLoadDialogAbout(self,window):
            aboutSection.About(self)

    def __init__(self):
        
        super().__init__(title="headerBar")
        self.set_default_size(800, 450)
        self.set_border_width(10)
        self.init_ui()
        self._bin = Gst.parse_bin_from_description('videotestsrc', True)
    def stop(self):
        Gst.Pipeline().set_state(Gst.State.NULL)
    def init_ui(self):
        headerBar = Gtk.HeaderBar()
        headerBar.set_show_close_button(True)
        headerBar.props.title = "Magic Eye: Client"
        
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
        #grid = Gtk.Grid(row_spacing=5, column_spacing=10, column_homogeneous=False)
        #self.add(grid)
       # self.drawingarea = Gtk.DrawingArea()
    # self.drawingarea.set_content_height = screenHeight
     #   self.drawingarea.set_content_width = screenWidth
        
        # Create a grid for the DrawingArea and buttons
        #grid = Gtk.Grid(row_spacing=10, column_spacing=10, column_homogeneous=False)
        #self.add(grid)
        #grid.set_column_spacing(10)
        #grid.set_row_spacing(5)
        #grid.attach(self.drawingarea, 0, 1, 8, 1)
        #print(grid.get_child_at(1, 1))
        #self.drawingarea.set_hexpand(True)
        #self.drawingarea.set_vexpand(True)
        
        
        #self.add(widget)
        #grid.attach(widget, 0, 1, 8, 1)
        widget = Player('videotestsrc')
        #widget.set_hexpand(True)
        #widget.set_vexpand(True)

        #widget.set_size_request(790, 440)
    
        self.add(widget)
       # grid.attach(widget, 0, 1, 8, 1)
        # Quit button
        #quit = Gtk.Button(label="disconnect stream  ")
        #quit.connect("clicked", self.stop)
        #grid.attach(quit, 0, 2, 2, 1)
"""
        global entry
        entry = Gtk.Entry()
        grid.attach_next_to(entry, quit, Gtk.PositionType.RIGHT, 4, 1)
        entry.set_placeholder_text("Server IP adress")
        self.entry = entry
        
        link = Gtk.Button(label="Link IP")
        #link.connect("clicked", self.connexion_rtsp)
        
        # Create GStreamer pipeline
        grid.attach_next_to(link, entry, Gtk.PositionType.RIGHT, 2, 1)
        """
        
       # def on_destroy(win):
      #          try:
       #             Gtk.main_quit()
        #        except KeyboardInterrupt:
         #           pass
        
        
        #self.connect('destroy', on_destroy)

