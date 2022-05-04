import wx
import os
import wx.lib.agw.flatnotebook as fnb
class Sauvegarge(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(254,25,255))

class heur(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        vbx=wx.BoxSizer(wx.VERTICAL)
        
        stc=wx.StaticText(self,-1,'Commentaire de l Archive')
        
        txt=wx.TextCtrl(self,-1,style=wx.TE_MULTILINE,size=(-1,300))
        
        btn=wx.Button(self,-1,'Le charger depuis Fichier')
        vbx.Add(3,5)
        vbx.Add(stc,0,wx.EXPAND|wx.ALL)
        vbx.Add(10,10)
        vbx.Add(txt,0,wx.EXPAND|wx.ALL)
        vbx.Add(10,10)
        vbx.Add(btn,0,wx.ALIGN_LEFT)
        self.SetSizer(vbx)
        
        

class Commentaire(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
  

class General(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
class Avance(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))

class Options(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
class Fichiers(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(254,254,255))
        panel=wx.Panel(self,-1)
        vbx=wx.BoxSizer(wx.VERTICAL)
        vbxx=wx.BoxSizer(wx.VERTICAL)
        
        bx=wx.StaticBox(panel,-1,'Selection une Commande')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        rb=wx.RadioButton(panel,-1,'Ne pas changerde module')
        bxx.Add(rb,0,wx.EXPAND|wx.ALL)
        bxx.Add(7,7)
        rb1=wx.RadioButton(panel,-1,'ajouter un nouveau module')
        bxx.Add(rb1,0,wx.EXPAND|wx.ALL)
        bxx.Add(7,7)
        rb2=wx.RadioButton(panel,-1,'Supprimer le module existant')
        bxx.Add(rb2,0,wx.EXPAND|wx.ALL)
        bxx.Add(7,7)
        vbxx.Add(bxx,0,wx.EXPAND|wx.ALL)
        
        stc=wx.StaticText(panel,-1,'Selection du Module Sfx')
        vbxx.Add(10,10)
        
        vbxx.Add(stc,0,wx.EXPAND|wx.ALL)
        
        lit=wx.ListCtrl(panel,-1,style=wx.LC_REPORT,size=(-1,200))
        lit.InsertColumn(0,'Module')
        
        lit.InsertColumn(1,'Description',width=300)
        
        vbxx.Add(lit,0,wx.EXPAND|wx.ALL)
        
        
        btn=wx.Button(panel,-1,'Options Sfx Avances')
        vbxx.Add(40,20)
        vbxx.Add(btn,0)
        
        panel.SetSizer(vbxx)
        panel.Layout()
        vbxx.Fit(panel)
        
        vbx.Add(panel,0,wx.EXPAND|wx.ALL)
        
        self.SetSizer(vbx)
        
class AjouteComm(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(500,500))
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel=wx.Panel(self,-1)
        self.notb = fnb.FlatNotebook(self.panel)
        hbx= wx.BoxSizer(wx.HORIZONTAL)
        
        
        
        vv=Sauvegarge(self.notb)
        self.notb.AddPage(vv, "Sauvegarge")
        
        ss=heur(self.notb)
        self.notb.AddPage(ss, "Heur des fichiers")
        
        ii=Commentaire(self.notb)
        
        self.notb.AddPage(ii, "Commentaire")
        
        gg=General(self.notb)
        self.notb.AddPage(gg, "General")
        
        
        
        ch=Avance(self.notb)
        self.notb.AddPage(ch, "Avance")
        
        
        ll=Options(self.notb)
        self.notb.AddPage(ll, "Options")
        
        cc=Fichiers(self.notb)
        self.notb.AddPage(cc, "Fichiers")
        
        
        
        self.btn5=wx.Button(self.panel,-1,'  OK  ')
        
        self.Bind(wx.EVT_BUTTON,self.OnFerme,self.btn5)
        
        btn6=wx.Button(self.panel,-1,'Anuler')
        
        btn7=wx.Button(self.panel,-1,'Aides')
        
        hbx.Add(self.btn5,0,wx.ALIGN_LEFT)
        hbx.Add(10,10)
        hbx.Add(btn6,0,wx.ALIGN_LEFT)
        hbx.Add(10,10)
        hbx.Add(btn7,0,wx.ALIGN_RIGHT)
        

        
        self.sizer.Add(self.notb, 1, wx.EXPAND | wx.ALL)
        
        self.sizer.Add(10,10)  
        self.sizer.Add(hbx, 1, wx.ALIGN_RIGHT)    
        #self.panel.SetSizer(self.sizer)
        
        self.panel.SetSizer(self.sizer)
        
        wx.FileSelector('Selection un fichier',os.getcwd(),wildcard='*.*')
        
    def OnFerme(self,event):
        self.Destroy()
    
        