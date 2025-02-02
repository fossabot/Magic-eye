#!/bin/env python3
import gi
import os
from settings import Config
import configparser
import socket
from ui.Ui import ServerUI as ui
gi.require_version('GstVideo', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk','3.0')
from gi.repository import Gst, GLib, GObject, GstRtspServer,Gtk,GdkPixbuf
from gi.repository import Gdk, GstVideo




Gst.init(None)

class ServerGui(Gtk.Window):
    #global entry
    #entry = Gtk.Entry()
    Gdk.set_allowed_backends("wayland,x11")
    launchMode =""
    global state
    global port
    global mount_point
    state =""

    config = configparser.ConfigParser()
    config.read(Config.full_config_file_path)

    port =  config.get('NETWORK_OPTION',"port")
    mount_point = config.get('NETWORK_OPTION',"mount_point")

    def __init__(self):

        ui.Ui(self)
        hostname = socket.gethostname()
        
        #get the server public ip
        IPAddress = ipadr = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], 
        [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) 
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is: " + IPAddress)

        
    def quit(self, window):
        print(Gtk.main_level())
        Gtk.main_quit()
        print(Gtk.main_level())

    def on_button_toggled(self,CamMode, name):
        config = configparser.ConfigParser()
        config.read(Config.full_config_file_path)
        global state
        if CamMode.get_active() and name == "v4l2src":
            state = "v4l2src"
            self.launchMode = config.get("CAMERA_OPTION",'v4l2srcLaunch')
            #CamMode.set_sensitive(False) & name == "rpicamsrc"
        elif CamMode.get_active() and name == "rpicamsrc":
            state = "rpicamsrc"
            self.launchMode = config.get("CAMERA_OPTION",'rpicamsrc')
            print(self.launchMode)
            print(state)
            
        else:
            state = ""
            self.launchMode = ""
        print("Button", name, "was turned", state)

    @classmethod
    def Connect(self,cls):
        global state
        print("state: ",state)
        print("launchMethod: ",self.launchMode)
        config = configparser.ConfigParser()
        config.read(Config.full_config_file_path)
        if state == "v4l2src":
             self.launchMode =  config.get("CAMERA_OPTION",'v4l2srcLaunch')
             print("state: ",state)
        if state == "rpicamsrc":
             self.launchMode =  config.get("CAMERA_OPTION",'rpicamsrc')
             print("state: ",state)

        hostname = socket.gethostname()
        #get the server public ip
        ipAddr = ipadr = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], 
        [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) 
        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]#ip.format(ip)#socket.gethostbyname(hostname)
        

        server = GstRtspServer.RTSPServer.new()
        server.set_service(port)

        mounts = server.get_mount_points()
        factory = GstRtspServer.RTSPMediaFactory.new()

        factory.set_launch(self.launchMode)
        mounts.add_factory(mount_point, factory)

        #  start server
        if self.launchMode == "":
                print("launchMode is empty")
        else:
             print("launchMethod: ",self.launchMode)
             print ("stream ready at rtsp://"+ ipAddr +":" + port + mount_point)
             ui.Set_Entry(self,str(ipAddr))
             server.attach()
             




def main():
    app = ServerGui()
    filename = '/home/'+str(os.getlogin())+'/.local/share/icons/MagicEye-icon/magiceye-06.svg'
    print(filename)
    icon_app_path = filename
    pixbuf = GdkPixbuf.Pixbuf.new_from_file(icon_app_path)
    app.set_icon(pixbuf)
    app.show_all()
    Gtk.main()
    print(Gtk.main_level())
    app.__init__()
if __name__=="__main__":
    main()
