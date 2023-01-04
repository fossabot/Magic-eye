import gi
import os
from Ui.AboutSection import  aboutSection
gi.require_version('GstVideo', '1.0')
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Gst, GLib, GObject,Gtk,Gio,GdkPixbuf
from gi.repository import Gdk, GstVideo

class GstWidget(Gtk.Grid):
    def __init__(self, pipeline):
        super().__init__()
        self.connect('realize', self._on_realize)
        self._bin = Gst.parse_bin_from_description('videotestsrc', True)

        quit = Gtk.Button(label="disconnect stream  ")
       # quit.connect("clicked", self.stop)
        self.attach(quit, 0, 2, 2, 1)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_column_spacing(10)
        self.set_row_spacing(5)
        global entry
        entry = Gtk.Entry()
        self.attach_next_to(entry, quit, Gtk.PositionType.RIGHT, 4, 1)
        entry.set_placeholder_text("Server IP adress")
        self.entry = entry
        
        link = Gtk.Button(label="Link IP")
        link.connect("clicked", self.on_link_clicked)
        
        
        # Create GStreamer pipeline
        self.attach_next_to(link, entry, Gtk.PositionType.RIGHT, 2, 1)
        

    def _on_realize(self, widget):
        rtsp_uri = self.entry.get_text()
        self._on_realize_stream(widget, rtsp_uri)
        pipeline = Gst.Pipeline()
        factory = pipeline.get_factory()
        gtksink = factory.make('gtksink')
        pipeline.add(gtksink)
        pipeline.add(self._bin)
        self._bin.link(gtksink)
        self.attach(gtksink.props.widget, 0, 1, 8, 1)
        gtksink.props.widget.set_hexpand(True)
        gtksink.props.widget.set_vexpand(True)
       
        gtksink.props.widget.show()
        pipeline.set_state(Gst.State.PLAYING)

    def on_link_clicked(self, button):
        self._on_realize(self)
    def _on_realize_stream(self, widget, rtsp_uri):
        pipeline = Gst.Pipeline()
        # Create the urisourcebin element
        urisource = Gst.ElementFactory.make("urisourcebin", "urisource")
       

       

        # Set the RTSP URI of the stream
        urisource.set_property("uri", rtsp_uri)

        # Remove the videotestsrc element from the pipeline
        pipeline.remove(self._bin)

        # Add the urisourcebin element to the pipeline
        pipeline.add(urisource)

        # Create the gtksink element
        factory = pipeline.get_factory()
        gtksink = factory.make('gtksink')
       # pipeline.add(gtksink)

        # Link the urisourcebin element to the gtksink element
        urisource.link(gtksink)
        #Gst.DebugCategory.get_threshold()
       

        # Set the pipeline to the PLAYING state
        pipeline.set_state(Gst.State.PLAYING)
       


    

    def exit_Stream(self):
        pipeline = Gst.Pipeline()
        factory = pipeline.get_factory()
        gtksink = factory.make('gtksink')
        pipeline.add(gtksink)
        pipeline.add(self._bin)
        self._bin.link(gtksink)
        self.pack_start(gtksink.props.widget, True, True, 0)
        gtksink.props.widget.show()
        pipeline.set_state(Gst.State.NULL)