
import wx

class Menu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self,'Menu',0)
        wx.MenuBar.__init__(self)
        
    def menu(self):
        
        fichier=wx.Menu('Fichier',0)
        self.ouvri=fichier.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
        self.Bind(wx.EVT_MENU,self.OnOuvete,self.ouvri)
        
        fichier.Append(-1, '&Enregistre sous une copie archive','Enregistre sous une copie archive')
        ouvri=fichier.Append(-1, '&Changer de LecteurrtCtrl+D ','Changer de Lecteurr ')
        
        ouvri=fichier.Append(-1, '&Definir Mot de passe \tCtrl+P','Definir Mot de passe')
        fichier.AppendSeparator()
        
        ouvri=fichier.Append(-1, '&Copier Fichier Dans Papier Presse \tCtrl+C','Copier Fichier Dans Papier Presse')
        ouvri=fichier.Append(-1, '&Coller Fichier Dans Papier Presse \tCtrl+V','Coller Fichier Dans Papier Presse')
        ouvri=fichier.Append(-1, '&Copier Le Nom complete','Copier Le Nom complete')
        fichier.AppendSeparator()
        
        ouvri=fichier.Append(-1, '&Selection le Tout Fichier \tCtrl++','Selection le Tout Fichier ')
        
        ouvri=fichier.Append(-1, '&Selection le Tout Groupe \tCtrl+V','Selection le Tout Groupe ')
        
        ouvri=fichier.Append(-1, '&Quitter\tCtrl+V','Quitter')
        
        commande=wx.Menu('Commandes',0)
        commande.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
        
        outils=wx.Menu('Outils',0)
        outils.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
        favoris=wx.Menu('Favoriss',0)
        favoris.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
       
        options=wx.Menu('Options',0)
        options.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
        aides=wx.Menu('Aides',0)
        aides.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        
        mbar=wx.MenuBar()
        mbar.Append(fichier,'Fichier')
        mbar.Append(commande,'Commandes')
        mbar.Append(favoris,'Favoris')
        mbar.Append(outils,'Outils')
        mbar.Append(options,'Options')
        mbar.Append(aides,'Aides')
       
       
    def OnOuvete(self,event):
        print("c est ok")
        

    
