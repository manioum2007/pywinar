import wx


class testPerfo(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(275,260))
        vbx=wx.BoxSizer(wx.VERTICAL)
        bx=wx.StaticBox(self,-1,'Vitesse')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        grid=wx.GridSizer(2,2,3,70)
        stc=wx.StaticText(self,-1,'Resultat, Ko/s') 
        stc1=wx.StaticText(self,-1,'Merci de patient') 
        
        stc2=wx.StaticText(self,-1,'Actuel, Ko/s') 
        stc3=wx.StaticText(self,-1,'Merci de patient') 
        grid.Add(stc,0,wx.EXPAND)
        grid.Add(stc1,0,wx.EXPAND)
        grid.Add(stc2,0,wx.EXPAND)
        grid.Add(stc3,0,wx.EXPAND)
        bxx.Add(grid,0,wx.EXPAND)
        


        bx1=wx.StaticBox(self,-1,'Total')
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        grid1=wx.GridSizer(3,2,3,150)
        stc4=wx.StaticText(self,-1,'Temp ecoule') 
        stc5=wx.StaticText(self,-1,'00:00:00') 
        
        stc6=wx.StaticText(self,-1,'Traiter Mo') 
        stc7=wx.StaticText(self,-1,'8') 
        
        stc8=wx.StaticText(self,-1,'Ereur trouver') 
        stc9=wx.StaticText(self,-1,'Non') 
        grid1.Add(stc4,0,wx.EXPAND)
        grid1.Add(stc5,0,wx.EXPAND)
        grid1.Add(stc6,0,wx.EXPAND)
        grid1.Add(stc7,0,wx.EXPAND|wx.ALIGN_RIGHT)
        grid1.Add(stc8,0,wx.EXPAND)
        grid1.Add(stc9,0,wx.EXPAND)
        bxx1.Add(grid1,0,wx.EXPAND)
        
        ch=wx.CheckBox(self,-1,'Traitement Multitransactionnel')
        
        grid2=wx.GridSizer(2,2,5,5)
        btn=wx.Button(self,-1,'Arriere-plan')
        btn1=wx.Button(self,-1,'Continuer')
        btn2=wx.Button(self,-1,'Annuler')
        btn3=wx.Button(self,-1,'Aide')
        
        grid2.Add(btn,0,wx.EXPAND)
        grid2.Add(btn1,0,wx.EXPAND)
        grid2.Add(btn2,0,wx.EXPAND)
        grid2.Add(btn3,0,wx.EXPAND)


        vbx.Add(5,5)

        vbx.Add(bxx,0,wx.EXPAND)
        vbx.Add(5,5)
        vbx.Add(bxx1,0,wx.EXPAND)
        vbx.Add(5,5)
        vbx.Add(ch,0,wx.EXPAND)
        vbx.Add(grid2,0,wx.EXPAND)
        
        
        self.SetSizer(vbx)