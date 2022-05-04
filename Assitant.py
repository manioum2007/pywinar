
import wx

class Assitant(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(430,350))
        
        vbx=wx.BoxSizer(wx.VERTICAL)
        
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        
        hbx1=wx.BoxSizer(wx.HORIZONTAL)
        
        hbx2=wx.BoxSizer(wx.HORIZONTAL)
        
        self.stc=wx.StaticText(self,-1,'Coisir un dossier')
        
        hbx.Add(self.stc,0,wx.EXPAND)
        vbx.Add(hbx,0,wx.EXPAND)
        vbx.Add(20,40)
        
        self.stc1=wx.StaticText(self,-1,'Dossier de destination ')
        
        self.btn=wx.Button(self,-1,'Parcour')
        
        hbx1.Add(self.stc1,0,wx.EXPAND)
        hbx1.Add(210,10)
        hbx1.Add(self.btn,0,wx.ALIGN_RIGHT)
        
        vbx.Add(hbx1,0,wx.EXPAND,20)
        
        cx=wx.ComboBox(self,-1,choices=[])
        
        vbx.Add(cx,0,wx.EXPAND,20)
        vbx.Add(20,40)
        stcl=wx.StaticLine(self,-1)
        vbx.Add(20,110)
        vbx.Add(stcl,0,wx.EXPAND,20)
        vbx.Add(20,20)
        self.btn1=wx.Button(self,-1,'Precedent')
        hbx2.Add(self.btn1,0,wx.EXPAND)
        vbx.Add(20,-1)
        self.btn2=wx.Button(self,-1,'Terminer')
        hbx2.Add(self.btn2,0,wx.EXPAND)
        vbx.Add(20,-1)
        self.btn3=wx.Button(self,-1,'Annuler')
        hbx2.Add(self.btn3,0,wx.EXPAND)
        vbx.Add(20,-1)
        self.btn4=wx.Button(self,-1,'Aider')
        hbx2.Add(self.btn4,0,wx.EXPAND)
        
        vbx.Add(hbx2,0,wx.EXPAND|wx.ALIGN_RIGHT)
        
        self.SetSizer(vbx)
        
        
        