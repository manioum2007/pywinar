import wx

class Antivirus(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(320,250))
        vbx=wx.BoxSizer(wx.VERTICAL)
        stc=wx.StaticText(self,-1,'Antivirus Trouve par winar')
        vbx.Add(stc,0,wx.ALL|wx.EXPAND)
        cx=wx.ComboBox(self,-1,' ',choices=[])
        vbx.Add(cx,0,wx.ALL|wx.EXPAND)
        vbx.Add(10,10)
        
        btn=wx.Button(self,-1,'Pacour')
        vbx.Add(btn,0,wx.ALIGN_RIGHT)
        stc1=wx.StaticText(self,-1,'Nom Antivirus')
        
        vbx.Add(stc1,0,wx.ALL|wx.EXPAND)
        txt=wx.TextCtrl(self,-1)
        vbx.Add(txt,0,wx.ALL|wx.EXPAND)
        vbx.Add(10,10)
        stc2=wx.StaticText(self,-1,'Parametre Antivirus')
        txt1=wx.TextCtrl(self,-1)
        vbx.Add(stc2,0,wx.ALL|wx.EXPAND)
        vbx.Add(txt1,0,wx.ALL|wx.EXPAND)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        
        btn=wx.Button(self,-1,'Ok')
        hbx.Add(btn,0,wx.EXPAND)
        hbx.Add(10,-1)
        btn1=wx.Button(self,-1,'Annueler')
        hbx.Add(btn1,0,wx.EXPAND)
        hbx.Add(10,-1)
        btn2=wx.Button(self,-1,'Aides')
        hbx.Add(btn2,0,wx.EXPAND)
        hbx.Add(10,-1)
        vbx.Add(10,10)
        vbx.Add(hbx,0,wx.ALL|wx.EXPAND)
        vbx.Add(10,10)
        self.SetSizer(vbx)