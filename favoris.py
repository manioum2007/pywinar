import wx

class favoris(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(350,240))
        vbx=wx.BoxSizer(wx.VERTICAL)
        bx=wx.StaticBox(self,-1)
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        stc=wx.StaticText(self,-1,'Ajout Objet Suivant au favoris')
        txt=wx.TextCtrl(self,-1)
        bxx.Add(stc,0,wx.EXPAND)
        bxx.Add(txt,0,wx.EXPAND)
        bxx.Add(10,10)
        
        stc1=wx.StaticText(self,-1,'Sous dossier de archive')
        txt1=wx.TextCtrl(self,-1)
        bxx.Add(stc1,0,wx.EXPAND)
        bxx.Add(txt1,0,wx.EXPAND)
        bxx.Add(10,10)
        stc2=wx.StaticText(self,-1,'Description falcultative')
        txt2=wx.TextCtrl(self,-1)
        bxx.Add(stc2,0,wx.EXPAND)
        bxx.Add(txt2,0,wx.EXPAND)
        vbx.Add(bxx,0,wx.EXPAND)
        
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        self.btn5=wx.Button(self,-1,'  OK  ')
        
        #self.Bind(wx.EVT_BUTTON,self.OnFerme,self.btn5)
        
        btn6=wx.Button(self,-1,'Anuler')
        
        btn7=wx.Button(self,-1,'Aides')
        hbx.Add(10,10)
        hbx.Add(self.btn5,0,wx.ALIGN_LEFT)
        hbx.Add(10,10)
        hbx.Add(btn6,0,wx.ALIGN_LEFT)
        hbx.Add(10,10)
        hbx.Add(btn7,0,wx.ALIGN_RIGHT)
        vbx.Add(10,10)
        vbx.Add(hbx,0,wx.EXPAND)
        
        self.SetSizer(vbx)
        
        
        
        

class favoris1(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(440,340))
        
        panel=wx.Panel(self,-1,style=wx.TAB_TRAVERSAL)
        
        panel1=wx.Panel(self,-1,style=wx.TAB_TRAVERSAL|wx.BORDER)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        vbx1=wx.BoxSizer(wx.VERTICAL)
        vbx2=wx.BoxSizer(wx.VERTICAL)
        lit=wx.ListCtrl(panel,-1,style=wx.LC_REPORT,size=(300,280))
        lit.InsertColumn(0,'Nom')
        lit.InsertColumn(1,'Chemin d acces')
        lit.InsertColumn(2,'Description')
        vbx1.Add(lit,0,wx.EXPAND)
        panel.SetSizer(vbx1)
        panel.Layout()
        vbx1.Fit(panel)
        
        btn=wx.Button(panel1,-1,'Ajouter')
        btn1=wx.Button(panel1,-1,'Supprimer')
        btn2=wx.Button(panel1,-1,'Editions')
        vbx2.Add(btn,0,wx.EXPAND)
        vbx2.Add(5,5)
        vbx2.Add(btn1,0,wx.EXPAND)
        vbx2.Add(5,5)
        vbx2.Add(btn2,0,wx.EXPAND)
        vbx2.Add(-1,15)
        btn3=wx.Button(panel1,-1,'Vers Haut')
        vbx2.Add(5,5)
        btn4=wx.Button(panel1,-1,'Vers Bas')
        vbx2.Add(btn3,0,wx.EXPAND)
        vbx2.Add(5,5)
        vbx2.Add(btn4,0,wx.EXPAND)
        vbx2.Add(-1,15)
        btn5=wx.Button(panel1,-1,'Ok')
        vbx2.Add(5,5)
        btn6=wx.Button(panel1,-1,'Annuler')
        vbx2.Add(5,5)
        btn7=wx.Button(panel1,-1,'Aides')
        vbx2.Add(btn5,0,wx.EXPAND)
        vbx2.Add(5,5)
        vbx2.Add(btn6,0,wx.EXPAND)
        vbx2.Add(5,5)
        vbx2.Add(btn7,0,wx.EXPAND)
        
        
        panel1.SetSizer(vbx2)
        panel.Layout()
        vbx2.Fit(panel1)
        hbx.Add(10,10)
        hbx.Add(panel,0,wx.EXPAND)
        hbx.Add(10,10)
        hbx.Add(panel1,0,wx.EXPAND)
        
        vbxP.Add(10,10)
        vbxP.Add(hbx,0,wx.EXPAND)
        
        self.SetSizer(vbxP)
   