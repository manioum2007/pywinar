import wx


class Resultat(wx.Frame):
    def __init__(self,parant,titre):
        wx.Frame.__init__(self,parant,-1,titre,size=(500,420),style=wx.FRAME_FLOAT_ON_PARENT|wx.CAPTION|wx.CLOSE_BOX)
        tool=wx.ToolBar(self,-1)
        vbx=wx.BoxSizer(wx.VERTICAL)
        tool.AddTool(-1,'EXTRAIRE VERS',wx.Bitmap('tool\\Add.bmp'))
        tool.AddTool(-1,'AFFICHER',wx.Bitmap('tool\\Add.bmp'))
        tool.AddTool(-1,'LOCALISER',wx.Bitmap('tool\\Add.bmp'))
        tool.Realize()
        st=wx.StatusBar(self,-1)
        self.SetStatusBar(st)
        vbx.Add(tool,0,wx.EXPAND,5)
        
        lit=wx.ListCtrl(self,-1,style=wx.LC_REPORT,size=(-1,270))
        lit.InsertColumn(0,'Fichier')
        lit.InsertColumn(0,'Emplacement')
        lit.InsertColumn(0,'Context')
        vbx.Add(lit,0,wx.EXPAND,5)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        btn=wx.Button(self,-1,'Arriere plan')
        btn1=wx.Button(self,-1,'Pause')
        btn2=wx.Button(self,-1,'Fermer')
        btn3=wx.Button(self,-1,'Aide')
        hbx.Add(btn,0,wx.EXPAND)
        hbx.Add(10,10)
        hbx.Add(btn1,0,wx.EXPAND)
        hbx.Add(10,5)
        hbx.Add(btn2,0,wx.EXPAND)
        hbx.Add(10,5)
        hbx.Add(btn3,0,wx.EXPAND)
        hbx.Add(10,5)
        vbx.Add(10,5)
        self.CenterOnParent()
        vbx.Add(hbx,0,wx.EXPAND,5)
        self.SetSizer(vbx)
        self.Show()





class Recherche(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(470,350))
        
        paneld=wx.Panel(self,-1)
        
        #panelg=wx.Panel(self,-1)
        vbx=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        vbs=wx.StaticBox(paneld,-1,'Rechercher')
        vbss=wx.StaticBoxSizer(vbs,wx.VERTICAL)
        
        stc=wx.StaticText(paneld,-1,'Nom du fichier a rechercher')
        
        vbss.Add(stc,0,wx.EXPAND|wx.ALL)
        cc=wx.ComboBox(paneld,-1,' ',choices=[])
        vbss.Add(cc,0,wx.EXPAND|wx.ALL)
        vbss.Add(10,10)
        stc1=wx.StaticText(paneld,-1,'chaine  a rechercher')
        vbss.Add(stc1,0,wx.EXPAND|wx.ALL)
        
        cc1=wx.ComboBox(paneld,-1,' ',choices=[])
        vbss.Add(cc1,0,wx.EXPAND|wx.ALL)
        vbss.Add(10,10)
        ch=wx.CheckBox(paneld,-1,'Respect la casse')
        vbss.Add(ch,0,wx.EXPAND|wx.ALL)
        vbss.Add(10,10)
        ch1=wx.CheckBox(paneld,-1,'tout table de chaine de caractere')
        vbss.Add(ch1,0,wx.EXPAND|wx.ALL)
        vbss.Add(10,10)
        ch2=wx.CheckBox(paneld,-1,'Rechercher hexadecimal')
        vbss.Add(ch2,0,wx.EXPAND|wx.ALL)
        vbss.Add(10,10)
        hbx.Add(vbss,0,wx.EXPAND|wx.ALL)
        
        hbx.Add(20,20)
        
        
        vbs1=wx.StaticBox(paneld,-1,' Ou Rechercher')
        vbss1=wx.StaticBoxSizer(vbs1,wx.VERTICAL)
        
        stc11=wx.StaticText(paneld,-1,'Disque et Dossier')
        
        vbss1.Add(stc11,0,wx.EXPAND|wx.ALL)
        
        cc11=wx.ComboBox(paneld,-1,' ',choices=[])
        vbss1.Add(cc11,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        stc111=wx.StaticText(paneld,-1,'Types d archives')
        vbss1.Add(stc111,0,wx.EXPAND|wx.ALL)
        
        cc111=wx.ComboBox(paneld,-1,' ',choices=[])
        vbss1.Add(cc111,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        ch11=wx.CheckBox(paneld,-1,'Rechercher dans le sous dossier')
        vbss1.Add(ch11,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        ch111=wx.CheckBox(paneld,-1,'Rechercher dans le fichier')
        vbss1.Add(ch111,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        ch211=wx.CheckBox(paneld,-1,'Rechercher dans le fichier')
        vbss1.Add(ch211,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        
        ch2111=wx.CheckBox(paneld,-1,'Ignore les fichiers chiffre')
        vbss1.Add(ch2111,0,wx.EXPAND|wx.ALL)
        vbss1.Add(10,10)
        hbx.Add(vbss1,0,wx.EXPAND|wx.ALL)
        
        pan=wx.Panel(self,-1)
        
        hbx1= wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn5=wx.Button(pan,-1,'  OK  ')
        self.Bind(wx.EVT_BUTTON,self.OnRech,self.btn5)
        #self.Bind(wx.EVT_BUTTON,self.OnFerme,self.btn5)
        
        btn6=wx.Button(pan,-1,'Anuler')
        
        btn8=wx.Button(pan,-1,'Enregistrer')
        
        
        btn7=wx.Button(pan,-1,'Aides')
        hbx1.Add(20,20)
        hbx1.Add(self.btn5,0,wx.ALIGN_LEFT)
        hbx1.Add(20,20)
        hbx1.Add(btn6,0,wx.ALIGN_LEFT)
        hbx1.Add(20,20)
        hbx1.Add(btn8,0,wx.ALIGN_RIGHT)
        
        hbx1.Add(20,20)
        hbx1.Add(btn7,0,wx.ALIGN_RIGHT)
        
        pan.SetSizer(hbx1)
        
        pan.Layout()
        hbx1.Fit(pan)
        
        
        
        
        
        
        
        paneld.SetSizer(hbx)
        
        paneld.Layout()
        hbx.Fit(paneld)
        
        vbx.Add(paneld,0,wx.EXPAND|wx.ALL,10)
        vbx.Add(10,10)
        vbx.Add(pan,0,wx.EXPAND|wx.ALL)
        vbx.Add(20,20)
        self.SetSizer(vbx)
        
        
        
        
        
        
        
    
    def OnRech(self,event):
        Resultat(self,'Resultat de la recherche')
        
        self.Show(False)