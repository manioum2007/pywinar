import wx

class convertir(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(500,-1))
        vbxP=wx.BoxSizer(wx.VERTICAL)
        
        panel1=wx.Panel(self,-1,size=(300,-1))
        
        panel2=wx.Panel(self,-1)
        
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        vbx1=wx.BoxSizer(wx.VERTICAL)
        stc=wx.StaticText(panel1,-1,'Archiver a Convertir')
        self.lit=wx.ListCtrl(panel1,-1,style=wx.LC_REPORT)
        self.lit.InsertColumn(0,'Nom',width=200)
        self.lit.InsertColumn(1,'Chemin d Acces')
        vbx1.Add(stc,0,wx.EXPAND)
        vbx1.Add(self.lit,0,wx.EXPAND)
        hbx3=wx.BoxSizer(wx.HORIZONTAL)
        btn1=wx.Button(panel1,-1,'Ajouter')
        btn2=wx.Button(panel1,-1,'Supprimer')
        hbx3.Add(btn1,0,wx.EXPAND)
        hbx3.Add(10,10)
        hbx3.Add(btn2,0,wx.EXPAND)
        vbx1.Add(10,10)
        vbx1.Add(hbx3,0,wx.EXPAND)
        panel1.SetSizer(vbx1)
        panel1.Layout()
        vbx1.Fit(panel1)
        hbx.Add(panel1,0,wx.EXPAND)
        vbx2=wx.BoxSizer(wx.VERTICAL)
        stc2=wx.StaticText(panel2,-1,'Type d Archives')
        
        vbx2.Add(stc2,0,wx.EXPAND)
        bx=wx.StaticBox(panel2,-1)
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        bx.SetBackgroundColour(wx.Colour(255,255,255))
        grid=wx.GridSizer(8,2,3,50)
        
        ch=wx.CheckBox(panel2,-1,'001')
        ch1=wx.CheckBox(panel2,-1,'7z')
        ch2=wx.CheckBox(panel2,-1,'ace')
        ch3=wx.CheckBox(panel2,-1,'arj')
        ch4=wx.CheckBox(panel2,-1,'bz2')
        ch5=wx.CheckBox(panel2,-1,'cab')
        ch6=wx.CheckBox(panel2,-1,'gz')
        ch7=wx.CheckBox(panel2,-1,'iso')
        
        
        ch11=wx.CheckBox(panel2,-1,'lz')
        ch12=wx.CheckBox(panel2,-1,'lzh')
        ch13=wx.CheckBox(panel2,-1,'rar')
        ch14=wx.CheckBox(panel2,-1,'tar')
        ch15=wx.CheckBox(panel2,-1,'uue')
        ch16=wx.CheckBox(panel2,-1,'xz')
        ch17=wx.CheckBox(panel2,-1,'z')
        ch18=wx.CheckBox(panel2,-1,'zip')
        grid.Add(ch,0,wx.EXPAND)
        grid.Add(ch11,0,wx.EXPAND)
        
        grid.Add(ch1,0,wx.EXPAND)
        grid.Add(ch12,0,wx.EXPAND)
        
        grid.Add(ch2,0,wx.EXPAND)
        grid.Add(ch13,0,wx.EXPAND)
        
        grid.Add(ch3,0,wx.EXPAND)
        grid.Add(ch14,0,wx.EXPAND)
        
        grid.Add(ch4,0,wx.EXPAND)
        grid.Add(ch15,0,wx.EXPAND)
        
        grid.Add(ch5,0,wx.EXPAND)
        grid.Add(ch16,0,wx.EXPAND)
        grid.Add(ch6,0,wx.EXPAND)
        grid.Add(ch17,0,wx.EXPAND)
        grid.Add(ch7,0,wx.EXPAND)
        grid.Add(ch18,0,wx.EXPAND)
        bxx.Add(grid,0,wx.EXPAND)
        
        stc3=wx.StaticText(panel2,-1,'0 Selectione')
        vbx2.Add(bxx,0,wx.EXPAND)
        vbx2.Add(10,10)
        vbx2.Add(stc3,0,wx.EXPAND|wx.CENTER)
        panelf=wx.Panel(self,-1)
        
        bx1=wx.StaticBox(panelf,-1,'Options de Conversions')
        bx11=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        hbx4=wx.BoxSizer(wx.HORIZONTAL)
        
        chs=wx.CheckBox(panelf,-1,'meilleur taux possible')
        btns=wx.Button(panelf,-1,'Compression')
        hbx4.Add(chs,0,wx.EXPAND)
        hbx4.Add(260,10)
        hbx4.Add(btns,0,wx.EXPAND)
        bx11.Add(hbx4,0,wx.EXPAND)
       
        cx1=wx.ComboBox(panelf,-1,'Pourcentage')
        
        bx11.Add(cx1,0)
        hbx5=wx.BoxSizer(wx.HORIZONTAL)
        
        stc4=wx.StaticText(panelf,-1,'Destination des archiver')
        btns1=wx.Button(panelf,-1,'Parcours')
        hbx5.Add(stc4,0,wx.EXPAND)
        hbx5.Add(290,10)
        hbx5.Add(btns1,0,wx.EXPAND)
        txt1=wx.TextCtrl(panelf,-1,)
        
        bx11.Add(hbx5,0,wx.EXPAND)
        
        bx11.Add(txt1,0,wx.EXPAND)
        chs11=wx.CheckBox(panelf,-1,'Dupprimer l Archive d origine')
        chs12=wx.CheckBox(panelf,-1,'ignorer l archives d orgine')
        bx11.Add(chs11,0,wx.EXPAND)
        bx11.Add(10,10)
        bx11.Add(chs12,0,wx.EXPAND)
        panelf.SetSizer(bx11)
        panelf.Layout()
        bx11.Fit(panelf)
        
        
        panel2.SetSizer(vbx2)
        panel2.Layout()
        vbx2.Fit(panel2)
        hbx.Add(10,10)
        
        
        pane=wx.Panel(self,-1)
        hbx111=wx.BoxSizer(wx.HORIZONTAL)
        
        btn1111=wx.Button(pane,-1,'Ok')
        hbx111.Add(btn1111,0,wx.EXPAND)
        hbx111.Add(10,-1)
        btn111=wx.Button(pane,-1,'Annueler')
        hbx111.Add(btn111,0,wx.EXPAND)
        hbx111.Add(10,-1)
        btn311=wx.Button(pane,-1,'Enregistrer')
        hbx111.Add(btn311,0,wx.EXPAND)
        hbx111.Add(10,-1)
        btn211=wx.Button(pane,-1,'Aides')
        hbx111.Add(btn211,0,wx.EXPAND)
        hbx111.Add(10,-1)
        pane.SetSizer(hbx111)
        pane.Layout()
        hbx111.Fit(pane)
        
        
        hbx.Add(panel2,0,wx.EXPAND)
        vbxP.Add(10,10)
        vbxP.Add(hbx,0,wx.EXPAND)
        
        vbxP.Add(10,10)
        vbxP.Add(panelf,0,wx.EXPAND)
        vbxP.Add(10,10)
        vbxP.Add(pane,0,wx.EXPAND)
        self.SetSizer(vbxP)