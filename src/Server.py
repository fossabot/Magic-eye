

from multiprocessing import parent_process
from time import sleep
from xmlrpc.client import Server
import gi
import socket
gi.require_version('GstRtspServer', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gst,Gtk,GLib
from gi.repository import GstRtspServer
from gi.repository import GObject
from Ui.Server import ServerAppWin as serverUi


class Init_Ui():
   
    def __init__(self): 
        serverUi()
# Create the RTSP server

def main():
        win = serverUi()
        win.set_icon_name("MagicEye-icon/magiceye-06")
        win.show_all()
        Gtk.main()

        Gst.init(None)

def on_button_toggled(self):
   server = GstRtspServer.RTSPServer() 
   server.attach(GLib.MainContext())
def Connect(self):
     
     state = True
     server = GstRtspServer.RTSPServer()
     if state == False:
            server.unref()
            state = True
            print(state)
     if state == True:
        ipAddr = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], 
            [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) 
            for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        print(ipAddr)
        
        print("I am not in the ui") 
        factory = GstRtspServer.RTSPMediaFactory()
        factory.set_launch('( videotestsrc ! x264enc ! rtph264pay name=pay0 pt=96 )')
        mount_points = server.get_mount_points()
        mount_points.add_factory("/tmp", factory)
        server.set_address(ipAddr)
        server.set_service("8554")
        server.attach(GLib.MainContext()) 
        serverUi.Set_Entry(ip=ipAddr)
        
       # connected +=1
        state=False
        
        #server = None
        print(server)

        
      


        

if __name__ == "__main__":
    #proc = Process(main())
    #proc.start() 
    #proc.join()
    main()
