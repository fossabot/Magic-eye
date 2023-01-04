
import gi
import os
from Ui.AboutSection import  aboutSection
from Ui.MagicEye import AppWin

gi.require_version('GstVideo', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Gst, GLib, GObject,Gtk,Gio,GdkPixbuf
from gi.repository import Gdk, GstVideo
import Ui.GstPlayer as Player 
#import Client as client
Gst.init(None)
Gst.init_check(None)


__author__ = "Sir_Thom"
__version__ = "0.9.0"
__license__ = "gpl3"

class Init_Ui():
    def __init__(self): 
        # initialze the gui element 
        AppWin()
        

       
    
def main():
    win = AppWin()
    win.set_icon_name("MagicEye-icon/magiceye-06")
    win.show_all()
    Gtk.main()
if __name__ == "__main__":
    main()




