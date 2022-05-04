import wx
from Menu import *
import os,zipfile
from FileDrop import *
from Dialg import *
from Pile import *
from Afficher import *
from Sfx import *
from Recherche import *
from Antivirus import *
from Assitant import *
from motPass import *
from convertir import *
import time
from favoris import *
from genere import *
from testPerfo import *
from AjouteComm import *
from parametre import *
class Winars(wx.Frame):
    def __init__(self,titre):
    
        wx.Frame.__init__(self,None,-1,title=titre,size=(1035,535))
       
        self.sui=Pile()
        self.pre=Pile()
        self.Menu()
        self.ToolBar()
        self.path=None
        self.zip=None
        
    
        self.SetIcon(wx.Icon("tool\\RAR.ico"))
        vbxP=wx.BoxSizer(wx.VERTICAL)
        vbx=wx.BoxSizer(wx.VERTICAL)
        vbxP2=wx.BoxSizer(wx.VERTICAL)
        panel1=wx.Panel(self,-1)
        
        self.lo=os.listdir('C:\\Users\\user\\\Desktop')
        self.la=[]
        for i in self.lo:
          
            self.la.append(i)
                


        
        self.cc=wx.ComboBox(panel1,-1,self.la[0],choices=self.la)
    
        panel1.SetSizer( vbx )
        panel1.Layout()
        vbx.Fit(panel1)
        
        vbx.Add(self.cc,0,wx.EXPAND)
        
        panel2=wx.Panel(self,-1)
        
        self.lit=wx.ListCtrl(panel2,-1,style=wx.LC_REPORT,size=(-1,900))
        
        self.lit.InsertColumn(0,'Nom',format=wx.LIST_FORMAT_LEFT,width=350)
        
        #LIST_ITEM_SELECTED
        #self.Bind(wx.EVT_CLOSE,self.OnClose)
        
        #frr=FileDropTarget(self)        
        #self.txt.SetDropTarget(frr)
        
        
        self.lit.InsertColumn(1,'Taille')
        self.lit.InsertColumn(2,'Compress',wx.LIST_FORMAT_RIGHT)
        self.lit.InsertColumn(3,'Type')
        self.lit.InsertColumn(4,'Modifie')
        self.lit.InsertColumn(5,'CRC32')
        
        
        

       

        
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.OnList,self.lit)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnSelect, self.lit)
        
        self.Bind(wx.EVT_CLOSE,self.OnClose)

        


        
        
        #lit.SetStringItem(0,1,('gggr','gggr','gggr','gggr','gggr','gggr'),-1)
        
        panel2.SetSizer( vbxP2 )
        panel2.Layout()
        vbxP2.Fit(panel2)
        
        vbxP2.Add(self.lit,0,wx.EXPAND|wx.ALL)
        
        
        vbxP.Add(panel1,0,wx.EXPAND|wx.ALL)
        
        
        vbxP.Add(panel2,0,wx.EXPAND|wx.ALL)
        
        self.SetSizer(vbxP)
        
        ss=wx.StatusBar(self,-1)
        self.SetStatusBar(ss)
        self.Show(True)
        
    def Menu(self):
        fichier=wx.Menu('Fichier',0)
        self.ouvri=fichier.Append(-1, '&Ouvrir Archiver\tCtrl+O','Ouvrir Archiver')
        self.Bind(wx.EVT_MENU,self.OnOuvri,self.ouvri)
        self.enregist=fichier.Append(-1, '&Enregistre sous une copie archive','Enregistre sous une copie archive')

        self.Bind(wx.EVT_MENU,self.OnEnregist,self.enregist)

        lecteur=fichier.Append(-1, '&Changer de LecteurrtCtrl+D ','Changer de Lecteurr ')
        
        
        self.motpass=fichier.Append(-1, '&Definir Mot de passe \tCtrl+P','Definir Mot de passe')
        
        self.Bind(wx.EVT_MENU,self.OnMotpass,self.motpass)
        
        fichier.AppendSeparator()
        
        ouvri=fichier.Append(-1, '&Copier Fichier Dans Papier Presse \tCtrl+C','Copier Fichier Dans Papier Presse')

        ouvri=fichier.Append(-1, '&Coller Fichier Dans Papier Presse \tCtrl+V','Coller Fichier Dans Papier Presse')
        ouvri=fichier.Append(-1, '&Copier Le Nom complete','Copier Le Nom complete')
        fichier.AppendSeparator()
        
        ouvri=fichier.Append(-1, '&Selection le Tout Fichier \tCtrl++','Selection le Tout Fichier ')
        
        ouvri=fichier.Append(-1, '&Selection le Tout Groupe \tCtrl+V','Selection le Tout Groupe ')
        
        ouvri=fichier.Append(-1, '&Quitter\tCtrl+V','Quitter')
        
        commande=wx.Menu('Commandes',0)
        self.Ajou=commande.Append(-1, '&Ajoute des Fichiers l archive \tCtrl+O','Ajoute des Fichiers l archive')
        self.Bind(wx.EVT_MENU,self.OnAjou,self.Ajou)
        self.extr=commande.Append(-1, '&Extraire le fichier  Dans le Dossier specifique\tAlt+A','Extraire le fichier  Dans le Dossier specifique')
        
        self.Bind(wx.EVT_MENU,self.OnExtr,self.extr)
        
        
        self.visua=commande.Append(-1, '&Visualiser le Fichier\tAlt+A','Visualiser le Fichier')
        self.Bind(wx.EVT_MENU,self.OnVisua,self.visua)
        
        self.Sup=commande.Append(-1, '&Supprimer le Fichier\tAlt+A','Supprimerle Fichier')
        self.Bind(wx.EVT_MENU,self.OnSuppCom,self.Sup)
        commande.Append(-1, '&Renomer le Fichier\tAlt+A','Renomer le Fichier')
        
        self.imp=commande.Append(-1, '&Imprimer Fichier\tAlt+A','Ajouter un commentaire')
        self.Bind(wx.EVT_MENU,self.OnImp,self.imp)
       
        commande.Append(-1, '&Extraire sans confirmation Fichier\Alt+A','Extraire sans confirmation Fichier')
        
        self.Comm=commande.Append(-1, '&Ajouter un commentaire\tAlt+A','Renomer le Fichier')
        self.Bind(wx.EVT_MENU,self.OnComm,self.Comm)
        commande.Append(-1, '&Proteger l Archive contre domage\tAlt+A','Proteger l Archive')
        
        commande.Append(-1, '&Verouiller l Archive \tAlt+A','Proteger l Archive')
        
        outils=wx.Menu('Outils',0)
        self.assit=outils.Append(-1, '&Assitance\tAlt+A','Assitance')
        self.Bind(wx.EVT_MENU,self.OnAssit,self.assit)
        
        self.antivirus=outils.Append(-1, '&Analyser a la Recherche de virus\tAlt+A','Analyser a la Recherche de virus')
        
        self.Bind(wx.EVT_MENU,self.OnAntivirus,self.antivirus)
        self.conv=outils.Append(-1, '&Convertir l Archiver\tAlt+A','Convertir l Archiver')
        self.Bind(wx.EVT_MENU,self.OnConv,self.conv)
        outils.Append(-1, '&Reparer l Archiver\tAlt+A','Reparer Archiver')
        
        self.SfxConv=outils.Append(-1, '&Convertir l Archiver Sfx\tAlt+A','Convertir l Archiver Sfx')
        self.Bind(wx.EVT_MENU,self.OnSfxConv,self.SfxConv)
        
        self.RechCom=outils.Append(-1, '&Rechercher des Fichiers\tAlt+A','Rechercher des Fichiers')
        
        self.Bind(wx.EVT_MENU,self.OnRechCom,self.RechCom)
        
        self.InfoComm=outils.Append(-1, '&Afficher les Informations\tAlt+A','Afficher des Informations')
        self.Bind(wx.EVT_MENU,self.OnInfoComm,self.InfoComm)
        
        
        self.gener=outils.Append(-1, '&Generer des Rapport\tAlt+A','Generer des Rapport')
        self.Bind(wx.EVT_MENU,self.OnGener,self.gener)
        
        
        #self.Bind(wx.EVT_MENU,self.OnRechCom,self.RechCom)
        self.Perf=outils.Append(-1, '&Test de Performations \tAlt+A','Test de Performations')
        self.Bind(wx.EVT_MENU,self.OnPerf,self.Perf)
        
        favoris=wx.Menu('Favoriss',0)
        
        self.favo1=favoris.Append(-1, '&Ajouter Favoris\tCtrl+F','Ajouter Favoris')
        self.Bind(wx.EVT_MENU,self.OnFavo1,self.favo1)
        self.favo=favoris.Append(-1, '&Organiser Favoris','Organiser Favoris')
        self.Bind(wx.EVT_MENU,self.OnFavo,self.favo)
        
        options=wx.Menu('Options',0)
        self.para=options.Append(-1, '&Parametres...','Parametres...')
        self.Bind(wx.EVT_MENU,self.OnPara,self.para)
        ko=options.Append(-1, '&Import et Export','Import et Export')
        
        

        
        
        options.Append(-1, '&Lister des Fichiers','Lister des Fichiers')
        
        options.Append(-1, '&Arborescences','Arborescences')
        
        options.Append(-1, '&Themes','Themes')
        
        options.Append(-1, '&Encodages des noms','Encodages des noms')
        
        options.Append(-1, '&Afficher le journal','Afficher dans le journal')
        options.Append(-1, '&Effacer le journal','Afficher dans le journal')
        aides=wx.Menu('Aides',0)
        aides.Append(-1, '&Mode d emploi','Mode d emploi')
        
        aides.Append(-1, '&Aicheter winar','Aicheter winar')
        aides.Append(-1, '&Information sur la licence','Information sur la licence')
        aides.Append(-1, '&Page d accueil de winar','Page d accueil de winar')
        aides.AppendSeparator()
        aides.Append(-1, '&Propos de winar','Propos de winar')
        
        mbar=wx.MenuBar()
        mbar.Append(fichier,'Fichier')
        mbar.Append(commande,'Commandes')
        mbar.Append(favoris,'Favoris')
        mbar.Append(outils,'Outils')
        mbar.Append(options,'Options')
        mbar.Append(aides,'Aides')
        self.SetMenuBar(mbar)
    
    def ToolBar(self):
        tool=wx.ToolBar(self,-1)
        
        self.ajouter=tool.AddTool(-1,'Ajouter',wx.Bitmap('tool\\Add.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnAjouter,self.ajouter)
        
        self.extraire=tool.AddTool(-1,'Extraire',wx.Bitmap('tool\\Extract.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnExtraire,self.extraire)
        
        self.test=tool.AddTool(-1,'Test',wx.Bitmap('tool\\Test.bmp'))

        
        
        self.Bind(wx.EVT_TOOL, self.OnTest,self.test)
        
        self.Afficher=tool.AddTool(-1,'&Afficher',wx.Bitmap('tool\\View.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnAfficher,self.Afficher)
        
        self.supprime=tool.AddTool(-1,'Supprimer',wx.Bitmap('tool\\Delete.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnSupprimer,self.supprime)
        
        self.recherche=tool.AddTool(-1,'Rechercher',wx.Bitmap('tool\\Find.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnRechercher,self.recherche)
        
        self.assistant=tool.AddTool(-1,'Assistant',wx.Bitmap('tool\\Wizard.bmp'))
        self.Bind(wx.EVT_TOOL, self.OnAssistant,self.assistant)
        
        self.information=tool.AddTool(-1,'Information',wx.Bitmap('tool\\Info.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnInformation,self.information)
        
        self.Antivirus=tool.AddTool(-1,'Antivirus',wx.Bitmap('tool\\VirusScan.bmp'))
        self.Bind(wx.EVT_TOOL, self.OnAntivirus,self.Antivirus)
        
        self.Commentaire=tool.AddTool(-1,'Commentaire',wx.Bitmap('tool\\Comment.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnCommentaire,self.Commentaire)
        
        self.Proteger=tool.AddTool(-1,'Proteger',wx.Bitmap('tool\\Protect.bmp'))
        self.Bind(wx.EVT_TOOL, self.OnProteger,self.Proteger)
        
        self.sfx=tool.AddTool(-1,'SFX',wx.Bitmap('tool\\SFX.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnSfxs,self.sfx)
        
        self.add=tool.AddTool(-1,'ADDI',wx.Bitmap('tool\\Print.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnADDI,self.add)
        
        self.suiv=tool.AddTool(-1,'Suiv',wx.Bitmap('tool\\Convert.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnSuiv,self.suiv)
        
        
        self.prec=tool.AddTool(-1,'PREC',wx.Bitmap('tool\\Prec.bmp'))
        
        self.Bind(wx.EVT_TOOL, self.OnPrec,self.prec)
        
        
        tool.Realize()
        self.SetToolBar(tool)
        
    
    def OnMotpass(self,event):
        mott=motPass(self,'Mot de Pass')
        mott.ShowModal()
    def OnEnregist(self,event):
        fd=wx.FileDialog(None,'Enregistre une copie',os.getcwd(),wildcard='*.zip',style=wx.FD_SAVE)
        #fd=wx.FileDialog(None,'entrez nom fichier',os.getcwd(),wildcard='*.txt',style=wx.FD_SAVE)
        fd.ShowModal()
        po=fd.GetPath()
        print(po)

    def Ajouter(self,filename,file_size,FileHeader,date_time,CRC,i):
        btm=wx.Bitmap('tool\\Extract.bmp', wx.BITMAP_TYPE_BMP)
        
        
        btm1=wx.Bitmap('tool\\View.bmp', wx.BITMAP_TYPE_BMP)
        
        btm2=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        btm3=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        self.il=wx.ImageList(16,16)
        
        #mm=wx.ImageList(16,16)
        self.il.Add(btm)
        self.il.Add(btm1)
        self.il.Add(btm2)
        self.il.Add(btm3)
        #self.lit.AssignImageList(il,wx.IMAGE_LIST_SMALL)
        self.lit.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        j=i
        
        
        self.lit.SetItemImage(0, 3)
        
        m=str(filename)
            
        self.lit.InsertItem(j, str(filename))
            
        self.lit.SetItem(j,1, str(file_size))
            
        self.lit.SetItem(j,2,str(FileHeader))
            
        self.lit.SetItem(j,3, "Dossier")
        self.lit.SetItem(j,4, str(date_time))
        self.lit.SetItem(j,5, str(CRC))
            #self.lit.Append((,,,,,))
            
        po=m.split('.')[-1]
        if po=='py':
            #print(p.filename)
            self.lit.SetItemImage(j, 1)
            #self.lit.SetItemBackgroundColour(j, '#f0f1f5')
               
        elif po == 'txt':
            self.lit.SetItemImage(j, 2)
                #self.lit.SetItemBackgroundColour(j, '#a0f1f5')
        else :
            self.lit.SetItemImage(j, 0)
            #if (j % 2) == 0:
            #   self.lit.SetItemBackgroundColour(j, '#e6f1f5')
            
    
    def OnOuvri(self,event):
        ff=wx.FileDialog(self,'CHOSIR UN FICHIER ZIP',os.getcwd(),wildcard='*.*')
        path=ff.ShowModal()
        
        
        self.path=ff.GetPath()
        if self.zip is not None:
            self.lit.DeleteAllItems()
        self.zip=zipfile.ZipFile(self.path,'r')
        
        #Ajoute(filename,file_size,FileHeader,date_time,CRC,i)
        self.lit.InsertItem(0, '..')
        doss='jjj'
        j=1
        for p in self.zip.infolist():
            m=p.filename
            
            if m[-1]=='/':
                doss=m.strip('/')
                if '/' in doss:
                    pass
                else:
                    self.Ajouter(p.filename,p.file_size,p.FileHeader,p.date_time,p.CRC,j)
                    j=j+1
            else:
                if doss in m:
                    pass
                else:
                    if doss==m:
                        pass
                    else:
                        self.Ajouter(p.filename,p.file_size,p.FileHeader,p.date_time,p.CRC,j)
                        j=j+1
            


        
    def OnPerf(self,event):
        test=testPerfo(self,'Test de Perfomance')
        
        test.ShowModal()
    def OnFavo(self,evet):
        self.fff=favoris1(self,'Organisation des  Favoris')
        self.fff.Show()
    
    def OnFavo1(self,evet):
        self.ff=favoris(self,'Ajout Favoris')
        self.ff.Show()
    def OnExtr(self,event):
        ma=Dialg(self,'Mama')
        pp=ma.ShowModal()
        
    def OnAjou(self,event):
        ajo=AjouteComm(self,'Nom et Parametre de Archive')
        ajo.ShowModal()
        
    def OnAjouter(self,event):
        ff=wx.FileDialog(self,'CHOSIR UN FICHIER ZIP',os.getcwd(),wildcard='*.*')
        path=ff.ShowModal()
        
        
        self.path=ff.GetPath()
        if self.zip is not None:
            self.lit.DeleteAllItems()
        
        self.zip=zipfile.ZipFile(self.path,'r')
        btm=wx.Bitmap('tool\\Extract.bmp', wx.BITMAP_TYPE_BMP)
        
        
        btm1=wx.Bitmap('tool\\View.bmp', wx.BITMAP_TYPE_BMP)
        
        btm2=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        btm3=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        self.il=wx.ImageList(16,16)
        
        #mm=wx.ImageList(16,16)
        self.il.Add(btm)
        self.il.Add(btm1)
        self.il.Add(btm2)
        self.il.Add(btm3)
        #self.lit.AssignImageList(il,wx.IMAGE_LIST_SMALL)
        self.lit.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        j=1
        self.lit.InsertItem(0, '..')
        
        self.lit.SetItemImage(0, 3)
        doss=""
        for p in self.zip.infolist():
            
            
            m=str(p.filename)
            if m[-1]=='/':
                doss=m
                self.lit.InsertItem(j, p.filename)
                self.lit.SetItem(j,1, str(p.file_size))
                self.lit.SetItem(j,2,str(p.FileHeader))
                self.lit.SetItem(j,3, "Dossier")
                self.lit.SetItem(j,4, str(p.date_time))
                self.lit.SetItem(j,5, str(p.CRC))
            else:
                
                if doss in m and (len(m.split('/'))>1):
                    pass
                else:
                    self.lit.InsertItem(j, p.filename)
                    self.lit.SetItem(j,1, str(p.file_size))
                    self.lit.SetItem(j,2,str(p.FileHeader))
                    self.lit.SetItem(j,3, "Fichier")
                    self.lit.SetItem(j,4, str(p.date_time))
                    self.lit.SetItem(j,5, str(p.CRC))
            
            #self.lit.Append((,,,,,))
            
            po=m.split('.')[-1]
            if po=='py':
                #print(p.filename)
                self.lit.SetItemImage(j, 1)
                #self.lit.SetItemBackgroundColour(j, '#f0f1f5')
               
            elif po == 'txt':
                self.lit.SetItemImage(j, 2)
                #self.lit.SetItemBackgroundColour(j, '#a0f1f5')
            else :
                self.lit.SetItemImage(j, 0)
            #if (j % 2) == 0:
            #   self.lit.SetItemBackgroundColour(j, '#e6f1f5')
            
            j=j+1
            
        
    
    def OnAssit(self,event):
        self.ass=Assitant(self,'Aissant')           
        self.ass.ShowModal() 
    def OnSfxConv(self,event):
        sss=Sfx(self,'Archiver Controle')
        sss.ShowModal()
        
    
    def OnProteger(self,event):
        mott=motPass(self,'Mot de Pass')
        mott.ShowModal()
    def OnGener(self,event):
        gen=genere(self,'Genere un rapport')
        gen.Show()
    def OnAntivirus(self,event):
        ant=Antivirus(self,'Antivirus')
        ant.ShowModal()
    def OnClose(self,event):
        self.Destroy()
    def OnExtraire(self,event):
        ma=Dialg(self,'Mama')
        pp=ma.ShowModal()
    def OnTest(self,event):
        wx.MessageBox('La verification des fichiers','la verification ok')
        
    def OnAfficher(self,event):
        aff=Afficher(self,'Afficher','C:\\Users\\user\\Desktop\\python\\mmm.pdf')
        aff.Show()
    def OnSuppCom(self,event):
        wx.MessageBox('etes sur de supprimer le fichier','Supprimer',style= wx.YES)
        print("ok")
    def OnComm(self,event):
        ccc=Sfx(self,'Archiver Controle')
        ccc.ShowModal()
    def OnVisua(self,event):
        aff=Afficher(self,'Afficher','C:\\Users\\user\\Desktop\\python\\mmm.pdf')
        aff.Show()
        
    
    
    def OnInfoComm(self,event):
        iii=Sfx(self,'Archiver Controle')
        iii.ShowModal()
    
    def OnSupprimer(self,event):
        wx.MessageBox('etes sur de supprimer le fichier','Supprimer',style= wx.YES)
        print("ok")
    def OnRechercher(self,event):
        rer=Recherche(self,'Rechercher des fichiers')
        rer.ShowModal()
    def OnRechCom(self,event):
        rer=Recherche(self,'Rechercher des fichiers')
        rer.ShowModal()
    def OnImp(self,event):
        pp=wx.PrintDialog(self)
        pp.ShowModal()
    def OnADDI(self,event):
        pp=wx.PrintDialog(self)
        pp.ShowModal()
    def OnAssistant(self,event):
       
        self.ass=Assitant(self,'Aissant')           
        self.ass.ShowModal() 
            
        #print(path)
    def OnConv(self,event):
        
        cc=convertir(self,'convertir')    
        cc.ShowModal()
    def OnList(self,event):
        menu = wx.Menu()
        menu.Append(wx.ID_COPY)
        menu.Append(-1,'mmmmmmmm')
        menu.Append(wx.ID_SELECTALL)
        self.PopupMenu(menu)
        menu.Destroy()
        
    def OnPara(self,event):
        pa=parametre(self,'Parametre')
        pa.ShowModal()          
                  
                  
    
    def OnPrec(self,event):
        
        try:
            n=self.pre.depiler()
            #print(val)
            
            print(n)
            self.lit.DeleteAllItems()
            self.lit.InsertItem(0, '..')
            j=1
            
            d=''
            if n[-1]=='/':
                d=n
                self.lit.DeleteAllItems()
                self.lit.InsertItem(0, '..')
                j=1
               
                for i in self.zip.infolist():
                    
                    m=str(i.filename)
                    if n in m:
                        if d==m:
                            pass
                        else:
                            
                            po=m.replace(d,'')
                            
                            if po[-1]=='/' :
                                if(len(po.split('/'))<2):
                                    
                                    self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                    j=j+1
                                else:
                                    pass
                            else:
                                if(len(po.split('/'))<2):
                                    self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                    j=j+1
            
            
            self.sui.empiler(n)
        except:
            print ('erreur dans la Precedente')
    
    def OnInformation(self,event):
        iii=Sfx(self,'Archiver Controle')
        iii.ShowModal()
    def OnCommentaire(self,event):
        ccc=Sfx(self,'Archiver Controle')
        ccc.ShowModal()
    
    def OnSfxs(self,event):
        sss=Sfx(self,'Archiver Controle')
        sss.ShowModal()
    
    def OnSuiv(self,event):
        try:
            n=self.sui.depiler()
            #print(val)
            
            print(n)
            self.lit.DeleteAllItems()
            self.lit.InsertItem(0, '..')
            j=1
            
            d=''
            if n[-1]=='/':
                d=n
                
                
                self.lit.DeleteAllItems()
                self.lit.InsertItem(0, '..')
                j=1
               
                for i in self.zip.infolist():
                    
                    m=str(i.filename)
                    if n in m:
                        if d==m:
                            pass
                        else:
                            
                            po=m.replace(d,'')
                            
                            if po[-1]=='/' :
                                if(len(po.split('/'))<3):
                                    
                                    self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                    j=j+1
                                else:
                                    pass
                            else:
                                if(len(po.split('/'))<2):
                                    self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                    j=j+1
            
            
            self.pre.empiler(n)
        except:
            print ('erreur dans la suivante')
        
    
    def OnSelect(self,event):
       

        pp=self.lit.GetFocusedItem()
        
        d=''
        n=self.lit.GetItemText(pp)
        if n[-1]=='/':
            d=n
            self.sui.empiler(n)
            
            self.lit.DeleteAllItems()
            self.lit.InsertItem(0, '..')
            j=1
           
            for i in self.zip.infolist():
                
                m=str(i.filename)
                if n in m:
                    if d==m:
                        pass
                    else:
                        
                        po=m.replace(d,'')
                        
                        if po[-1]=='/' :
                            if(len(po.split('/'))<3):
                                
                                self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                j=j+1
                            else:
                                pass
                        else:
                            if(len(po.split('/'))<2):
                                self.Ajouter(i.filename,i.file_size,i.FileHeader,i.date_time,i.CRC,j)
                                j=j+1
        else:
            m=self.zip.extract(n)
            mp=str(n)
            mpp=mp.replace('\\','/')
            os.startfile(m)
        #print(mpp)
        
        
    def OnAntivirus(self,event):
      ant=Antivirus(self,'Antivirus')
      ant.ShowModal()
    
    #def OnClose(self,event):
    #    mp=wx.MessageBox('voulez vous quitter le programme','Action de fermeture')
   
    def Ajoute(self,filename,file_size,FileHeader,date_time,CRC,i):
        btm=wx.Bitmap('tool\\Extract.bmp', wx.BITMAP_TYPE_BMP)
        
        
        btm1=wx.Bitmap('tool\\View.bmp', wx.BITMAP_TYPE_BMP)
        
        btm2=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        btm3=wx.Bitmap('tool\\haut.bmp', wx.BITMAP_TYPE_BMP)
        self.il=wx.ImageList(16,16)
        
        #mm=wx.ImageList(16,16)
        self.il.Add(btm)
        self.il.Add(btm1)
        self.il.Add(btm2)
        self.il.Add(btm3)
        #self.lit.AssignImageList(il,wx.IMAGE_LIST_SMALL)
        self.lit.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        j=i
        self.lit.InsertItem(0, '..')
        
        self.lit.SetItemImage(0, 3)
        
        m=str(filename)
          
            
        self.lit.InsertItem(j, str(filename))
            
        self.lit.SetItem(j,1, str(file_size))
            
        self.lit.SetItem(j,2,str(FileHeader))
            
        self.lit.SetItem(j,3, "llll")
        self.lit.SetItem(j,4, str(date_time))
        self.lit.SetItem(j,5, str(CRC))
            #self.lit.Append((,,,,,))
            
        po=m.split('.')[-1]
        if po=='py':
            #print(p.filename)
            self.lit.SetItemImage(j, 1)
            #self.lit.SetItemBackgroundColour(j, '#f0f1f5')
               
        elif po == 'txt':
            self.lit.SetItemImage(j, 2)
                #self.lit.SetItemBackgroundColour(j, '#a0f1f5')
        else :
            self.lit.SetItemImage(j, 0)
            #if (j % 2) == 0:
            #   self.lit.SetItemBackgroundColour(j, '#e6f1f5')
            
        
        
app=wx.App()

Winars('Copie')

app.MainLoop()


