import wx


class Afficher(wx.Frame):
    def __init__(self,parant,titre,filen):
        wx.Frame.__init__(self,parant,-1,title=titre)
        
        #self.panel=wx.Panel(self,-1)
        self.Menu()
        self.txt=wx.TextCtrl(self,-1,style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.Ouvrier(filen)
        
    def Ouvrier(self,filee):
        with open(filee,'rb') as fi:
            while True:
                tr=fi.read(8192)
                if not tr:
                    break
                try:
                    
                    self.txt.AppendText(tr)
                except:
                    pass
            
                    
            
    def Menu(self):
        Fichier=wx.Menu()
        
        Fichier.Append(-1,'&Quitter\tCtrl+O','mama')
        
        Edition=wx.Menu()
        Edition.Append(-1,'&Copier\tCtrl+c','Copier')
        Edition.Append(-1,'&Selection tout\tCtrl+c','Selection')
        Edition.AppendSeparator()
        Edition.Append(-1,'&Rechercher\tCtrl+R','Rechercher')
        Edition.Append(-1,'&Rechercher Tout\tCtrl+R','Rechercher')
        
        Affi=wx.Menu()
        Affi.Append(-1,'&Afficher comme text\tCtrl+R','Afficher le tout')
        
        Affi.Append(-1,'&Afficher comme text dos\tCtrl+R','Afficher le tout')
        Affi.Append(-1,'&Afficher comme text unicode\tCtrl+R','Afficher unicode')
        Affi.AppendSeparator()
        
        Affi.Append(-1,'&Retour a la ligne\tCtrl+R','Retour a la ligne')
        Affi.Append(-1,'&Polices\tCtrl+R','Polices')
        
        Aides=wx.Menu()
        Aides.Append(-1,'Aides de lavisionneuse','Aides de lavisionneuse')
        menuB=wx.MenuBar()
        menuB.Append(Fichier,'Fichier')
        menuB.Append(Edition,'Edition')
        menuB.Append(Affi,'Afficher')
        
        menuB.Append(Aides,'Aides')
        self.SetMenuBar(menuB)
        
        
        