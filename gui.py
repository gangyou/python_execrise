import wx

def load(event):
	f = open(filename.GetValue())
	contents.SetValue(f.read())
	f.close()

def save(event):
	f = open(filename.GetValue(), 'w')
	f.write(contents.GetValue())
	f.close()

app = wx.App()

#win
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)

load_button = wx.Button(bkg, label="Open")
save_button = wx.Button(bkg, label="Save")
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

hx = wx.BoxSizer()
hx.Add(filename, proportion=1, flag=wx.EXPAND)
hx.Add(load_button, proportion=0, flag = wx.LEFT, border = 5)
hx.Add(save_button, proportion=0, flag=wx.LEFT, border=5)

vx = wx.BoxSizer(wx.VERTICAL)
vx.Add(hx, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vx.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vx)

#event handler
load_button.Bind(wx.EVT_BUTTON, load)
save_button.Bind(wx.EVT_BUTTON, save)

#show the window
win.Show()
app.MainLoop()
