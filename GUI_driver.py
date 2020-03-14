import wx

WIDTH  = 1920
HEIGHT = 1080

class Window(wx.Frame):
    
    def __init__(self, parent, title): 
        super(Window, self).__init__(parent, title = title,size = (WIDTH,HEIGHT))  
        panel = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
        # add a text box to the screen
        text_read = wx.TextCtrl(self,size=(WIDTH,HEIGHT/2))
        send_button = wx.Button(self,label="Send", pos=(0,wx.ALIGN_RIGHT))
        send_button.Bind(wx.EVT_BUTTON, self.OnToggle)
        self.Show(True)

    def OnToggle(self, event):
        # Handle the event in here.
        # read the user input from the button.
        print ("Clicked")

app = wx.App()
Window(None,"CPSC 3600 Messenger App")
app.MainLoop()