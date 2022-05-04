
import wx 
import wx.lib.agw.flatnotebook as fnb

#import wx.lib.flatnotebook as fnb

class Tab(wx.Panel):
    # Initialize Tab
    def __init__(self, parent):
        # Initialize wxPanel
        wx.Panel.__init__(self, parent=parent)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbxH1=wx.BoxSizer(wx.HORIZONTAL)
        hbxH2=wx.BoxSizer(wx.HORIZONTAL)
        vbxH=wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        panelH=wx.Panel(self,-1)
        
        stc=wx.StaticText(panelH,-1,'Chemin d acces du destinateur',size=(480,-1))
        btn1=wx.Button(panelH,-1,'Afficher')
        
        cbx=wx.ComboBox(panelH,-1,'comlobe',choices=[],size=(480,-1))
        
        btn2=wx.Button(panelH,-1,'Nouveau')
        
        hbxH1.Add(stc,0,wx.EXPAND,10)
        hbxH1.Add(btn1,0,wx.EXPAND,10)
        
        hbxH2.Add(cbx,0,wx.EXPAND,10)
        #hbxH2.Add(5,5)
        hbxH2.Add(btn2,0,wx.EXPAND,10)
        
        vbxH.Add(hbxH1,0,wx.EXPAND|wx.ALL,)
        vbxH.Add(5,5)
        vbxH.Add(hbxH2,0,wx.EXPAND|wx.ALL)
        
        panelH.SetSizer( vbxH )
        panelH.Layout()
        vbxH.Fit(panelH)
        
        
        
        panelC=wx.Panel(self,-1)
        hbxC=wx.BoxSizer(wx.HORIZONTAL)
        
        vbxC1=wx.BoxSizer(wx.VERTICAL)
        
        vbxC2=wx.BoxSizer(wx.VERTICAL)
        
       
        
        #bx=wx.StaticBox( panelC, -1, 'mama')
       
        bx=wx.StaticBox(panelC,-1,'Mettre a jour')
        
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        radio1=wx.RadioButton(panelC,-1,'Extraire ou Remplacer fichier')
        radio2=wx.RadioButton(panelC,-1,'Extraire ou Mettre fichier')
        radio3=wx.RadioButton(panelC,-1,'Mettre a jour uniquement les fichier existant')
        
        bxx.Add(radio1,0,wx.EXPAND,5)
        bxx.Add(5,5)
        bxx.Add(radio2,0,wx.EXPAND,5)
        bxx.Add(5,5)
        bxx.Add(radio3,0,wx.EXPAND,5)
        
        vbxC1.Add(bxx,0,wx.EXPAND)
        vbxC1.Add(5,5)
        bx1=wx.StaticBox(panelC,-1,'Mode de remplacement')
        
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        radio4=wx.RadioButton(panelC,-1,'Demander avant remplacer')
        radio5=wx.RadioButton(panelC,-1,'Demander sans remplacer')
        radio6=wx.RadioButton(panelC,-1,'Ignore les fichier existant')
        radio7=wx.RadioButton(panelC,-1,'Renommer automatiquer')
        
        bxx1.Add(radio4,0,wx.EXPAND,5)
        bxx1.Add(5,5)
        bxx1.Add(radio5,0,wx.EXPAND,5)
        bxx1.Add(5,5)
        bxx1.Add(radio6,0,wx.EXPAND,5)
        
        bxx1.Add(5,5)
        bxx1.Add(radio7,0,wx.EXPAND,5)
        
       
        vbxC1.Add(bxx1,0,wx.EXPAND)
        
        vbxC1.Add(5,5)
        
        
        
        
        
        
         
        
        bx2=wx.StaticBox(panelC,-1,'Divers')
        
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        
 
        radio22=wx.CheckBox(panelC,-1,'Extraire archives dans le sous dossier')
        radio33=wx.CheckBox(panelC,-1,'Conserver les fichier alter')
        radio44=wx.CheckBox(panelC,-1,'Afficher les Fichier dans l exploration')
        
        

        bxx2.Add(radio22,0,wx.EXPAND,5)
        bxx2.Add(5,5)
        bxx2.Add(radio33,0,wx.EXPAND,5)
        
        bxx2.Add(5,5)
        bxx2.Add(radio44,0,wx.EXPAND,5)
        
        btn4=wx.Button(panelC,-1,'Enregistrer la Configuration')
        
        vbxC1.Add(bxx2,0,wx.EXPAND)
        
        vbxC1.Add(10,10)
        
        vbxC1.Add(btn4,0,wx.EXPAND)
        
        hbxC.Add(vbxC1,0,wx.EXPAND)
        
        tree=wx.TreeCtrl(panelC,-1,size=(300,1))
        
        hbxC.Add(10,10)
        
        hbxC.Add(tree,0,wx.EXPAND)

        #root = tree.AddRoot("wx.Object")
        #self.AddTreeNodes(root, 'data.tree')
        
        
        
        
        
        
        
        
        panelC.SetSizer( hbxC )
        panelH.Layout()
        hbxC.Fit(panelC)
        
        
        
        vbxP.Add(panelH,0,wx.EXPAND|wx.ALL)
        vbxP.Add(10,10)
        vbxP.Add(panelC,0,wx.EXPAND)
        
        self.SetSizer(vbxP)
        
        
        



class TabB(wx.Panel):
    # Initialize Tab
    def __init__(self, parent):
        # Initialize wxPanel
        wx.Panel.__init__(self, parent=parent)
        panel=wx.Panel(self,1)
        grid=wx.GridSizer(2,2,20,5)
        vbxP=wx.BoxSizer(wx.VERTICAL)
        
        bx=wx.StaticBox(panel,-1,'Heure des fichier')
        
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        radio1=wx.CheckBox(panel,-1,'Activer l heur modification')
        radio2=wx.CheckBox(panel,-1,'Activer l heur Creation')
        radio3=wx.CheckBox(panel,-1,'Activer l heur du dernier acces')
        
        bxx.Add(radio1,0,wx.EXPAND,5)
        bxx.Add(5,5)
        bxx.Add(radio2,0,wx.EXPAND,5)
        bxx.Add(5,5)
        bxx.Add(radio3,0,wx.EXPAND,5)
        
        grid.Add(bxx,0,wx.EXPAND)
        
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        
        bx1=wx.StaticBox(panel,-1,'Les Attributs')
        
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        radio1=wx.CheckBox(panel,-1,'Effacer l attribut archive')
        radio2=wx.CheckBox(panel,-1,'Activer la securite')
        radio3=wx.CheckBox(panel,-1,'Definir l attribut compresse')
        
        bxx1.Add(radio1,0,wx.EXPAND,5)
        bxx1.Add(5,5)
        bxx1.Add(radio2,0,wx.EXPAND,5)
        bxx1.Add(5,5)
        bxx1.Add(radio3,0,wx.EXPAND,5)
        
        grid.Add(bxx1,0,wx.EXPAND)
        

        
        bx2=wx.StaticBox(panel,-1,'Chemin Acces aux fichiers')
        
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        
        radio1=wx.RadioButton(panel,-1,'Extraire les chemins d acces relatif')
        
        radio2=wx.RadioButton(panel,-1,'Extraire les chemins d acces complet')
        radio3=wx.RadioButton(panel,-1,'Ne pas Extraire les chemins d acces')
        radio4=wx.RadioButton(panel,-1,' Extraire les chemins d acces')
        bxx2.Add(radio1,0,wx.EXPAND,5)
        bxx2.Add(5,5)
        bxx2.Add(radio2,0,wx.EXPAND,5)
        bxx2.Add(5,5)
        bxx2.Add(radio3,0,wx.EXPAND,5)
        
        bxx2.Add(5,5)
        bxx2.Add(radio4,0,wx.EXPAND,5)
        
        
        grid.Add(bxx2,0,wx.EXPAND)
        
        
        
        
        bx3=wx.StaticBox(panel,-1,'Supprimer l Archive')
        
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        
        radio1=wx.RadioButton(panel,-1,'Jamais')
        radio2=wx.RadioButton(panel,-1,'Demander confirmation')
        radio3=wx.RadioButton(panel,-1,'Toujours')
        
        bxx3.Add(radio1,0,wx.EXPAND,5)
        bxx3.Add(5,5)
        bxx3.Add(radio2,0,wx.EXPAND,5)
        bxx3.Add(5,5)
        bxx3.Add(radio3,0,wx.EXPAND,5)
        
        grid.Add(bxx3,0,wx.EXPAND)


        
        
        
        panel.SetSizer(grid)
        panel.Layout()
        grid.Fit(panel)
        
       
        
        
        vbxP.Add(panel,0,wx.EXPAND|wx.ALL)
        #vbxP.Add(10,10)
        
        
        self.SetSizer(vbxP)
        




class Dialg(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(600,-1))
        
        self.panel=wx.Panel(self,-1)
        self.notb = fnb.FlatNotebook(self.panel)
        
        
        
        #self.notb.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT,wx.FONTWEIGHT_NORMAL, wx.FONTSTYLE_NORMAL))
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        hbx= wx.BoxSizer(wx.HORIZONTAL)
        self.tab = Tab(self.notb)
        
        self.tabs = TabB(self.notb)
        
        self.notb.AddPage(self.tab, "General")
        
        self.notb.AddPage(self.tabs, "Avancee")
        
        self.btn5=wx.Button(self.panel,-1,'  OK  ')
        
        self.Bind(wx.EVT_BUTTON,self.OnFerme,self.btn5)
        
        btn6=wx.Button(self.panel,-1,'Anuler')
        
        btn7=wx.Button(self.panel,-1,'Aides')
        
        hbx.Add(self.btn5,0,wx.ALIGN_LEFT)
        
        hbx.Add(btn6,0,wx.ALIGN_LEFT)
        
        hbx.Add(btn7,0,wx.ALIGN_RIGHT)
        
        self.sizer.Add(self.notb, 1, wx.EXPAND | wx.ALL)
        self.sizer.Add(10,10)  
        self.sizer.Add(hbx, 1, wx.ALIGN_RIGHT)    
        self.panel.SetSizer(self.sizer)
        #self.ShowModal()
        
        
    def OnFerme(self,event):
        self.Destroy()
    
