import wx
class motPass(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(350,380))
        vbxx=wx.BoxSizer(wx.VERTICAL)
        vbx=wx.BoxSizer(wx.VERTICAL)
        
        panelt=wx.Panel(self,-1)
        panelc=wx.Panel(self,-1)
        stc=wx.StaticText(panelt,-1,'Definir le mot de pass par defaut')
        #stc.Center()
        vbx.Add(10,10)
        vbx.Add(stc,0,wx.EXPAND|wx.CENTER)
        vbx.Add(20,50)
        panelt.SetSizer(vbx)
        panelt.Layout()
        vbx.Fit(panelt)
        
        
        bx=wx.StaticBox(panelc,-1)
        vbxc=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
     

        
      
        stc1=wx.StaticText(panelc,-1,'Saisir le mot de passer')
        txt=wx.TextCtrl(panelc,-1)
        
        cx=wx.CheckBox(panelc,-1,'Afficher le mot pass')
        cx1=wx.CheckBox(panelc,-1,'Chiffre le nom du fichier')
        cx2=wx.CheckBox(panelc,-1,'Chiffrement ZIP')
        cx3=wx.CheckBox(panelc,-1,'utiliser toutes archiver')
        btn=wx.Button(panelc,-1,'Organiser les mots de pass')
        vbxc.Add(stc1,0,wx.EXPAND)
        vbxc.Add(txt,0,wx.EXPAND)
        vbxc.Add(20,50)
        vbxc.Add(cx,0,wx.EXPAND)
        vbxc.Add(5,5)
        vbxc.Add(cx1,0,wx.EXPAND)
        vbxc.Add(5,5)
        vbxc.Add(cx2,0,wx.EXPAND)
        vbxc.Add(5,5)
        vbxc.Add(cx3,0,wx.EXPAND)
        vbxc.Add(5,5)
        vbxc.Add(btn,0,wx.EXPAND)
        vbxc.Add(5,5)
        panelc.SetSizer(vbxc)
        panelc.Layout()
        vbxc.Fit(panelc)

        
        
        
        pan=wx.Panel(self,-1)
        
        hbx1= wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn5=wx.Button(pan,-1,'  OK  ')
        
        #self.Bind(wx.EVT_BUTTON,self.OnFerme,self.btn5)
        
        btn6=wx.Button(pan,-1,'Anuler')
        
        
        btn7=wx.Button(pan,-1,'Aides')
        hbx1.Add(20,20)
        hbx1.Add(self.btn5,0,wx.ALIGN_LEFT)
        hbx1.Add(20,20)
        hbx1.Add(btn6,0,wx.ALIGN_LEFT)
        hbx1.Add(20,20)
        
        hbx1.Add(btn7,0,wx.ALIGN_RIGHT)
        
        pan.SetSizer(hbx1)
        
        pan.Layout()
        hbx1.Fit(pan)
        
        
        
        vbxx.Add(panelt,0,wx.EXPAND)
        vbxx.Add(panelc,0,wx.EXPAND)
        vbxx.Add(10,10)
        vbxx.Add(pan,0,wx.EXPAND)
        
        self.SetSizer(vbxx)
        