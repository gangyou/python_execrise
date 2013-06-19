import wx
import Image as images

class ToolbarFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, "Toolbars", size=(300, 200))
		panel = wx.Panel(self)
		panel.SetBackgroundColour("White")
		statusBar = self.CreateStatusBar()
		toolbar = self.CreateToolBar()
		toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Long help for 'New'")
		toolbar.Realize()
		menuBar = wx.MenuBar()
		menu1 = wx.Menu()
		menuBar.Append(menu1)
		menu2 = wx.MenuBar()
		menu2.Append(wx.NewId(), " ", "Copy in status bar")
		menu2.Append(wx.NewId(), "C ", "")
		menu2.Append(wx.NewId(), "Paste", "")
		menu2.AppendSeparator()
		menu2.Append(wx.NewId(), " ", "Display Options")
		menuBar.Append(menu2, " ")
		self.SetMenuBar(menuBar)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = ToolbarFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
