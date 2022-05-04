

import wx

import wx.lib.agw.flatnotebook as fnb
class Integration(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        bxP=wx.StaticBox(self,-1)
        bxxP=wx.StaticBoxSizer(bxP,wx.VERTICAL)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        
        bx=wx.StaticBox(self,-1,'Associer Winrar ',size=(150,-1))
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        bxx.Add(10,10)
        grid=wx.GridSizer(10,2,3,3)
        ch=wx.CheckBox(self,-1,'RAR')
        ch1=wx.CheckBox(self,-1,'Zip')
        ch2=wx.CheckBox(self,-1,'7Z')
        ch3=wx.CheckBox(self,-1,'ACE')
        ch4=wx.CheckBox(self,-1,'ARJ')
        ch5=wx.CheckBox(self,-1,'BZ2')
        ch6=wx.CheckBox(self,-1,'GZ')
        ch7=wx.CheckBox(self,-1,'ISO')
        ch8=wx.CheckBox(self,-1,'JAR')
        ch9=wx.CheckBox(self,-1,'LZ')
        ch10=wx.CheckBox(self,-1,'LZH')
        ch11=wx.CheckBox(self,-1,'TAR')
        ch12=wx.CheckBox(self,-1,'UUE')
        ch13=wx.CheckBox(self,-1,'XZ')
        ch14=wx.CheckBox(self,-1,'Z')
        ch15=wx.CheckBox(self,-1,'ZIPX')
        ch16=wx.CheckBox(self,-1,'001')
        
        grid.Add(ch,0,wx.EXPAND|wx.ALL)
        grid.Add(ch1,0,wx.EXPAND|wx.ALL)
        grid.Add(ch2,0,wx.EXPAND|wx.ALL)
        grid.Add(ch3,0,wx.EXPAND|wx.ALL)
        grid.Add(ch4,0,wx.EXPAND|wx.ALL)
        grid.Add(ch5,0,wx.EXPAND|wx.ALL)
        grid.Add(ch6,0,wx.EXPAND|wx.ALL)
        grid.Add(ch7,0,wx.EXPAND|wx.ALL)
        grid.Add(ch8,0,wx.EXPAND|wx.ALL)
        grid.Add(ch9,0,wx.EXPAND|wx.ALL)
        grid.Add(ch10,0,wx.EXPAND|wx.ALL)
        grid.Add(ch11,0,wx.EXPAND|wx.ALL)
        grid.Add(ch12,0,wx.EXPAND|wx.ALL)
        grid.Add(ch13,0,wx.EXPAND|wx.ALL)
        grid.Add(ch14,0,wx.EXPAND|wx.ALL)
        grid.Add(ch15,0,wx.EXPAND|wx.ALL)
        grid.Add(ch16,0,wx.EXPAND|wx.ALL)
        
        bxx.Add(grid,0,wx.EXPAND)
        btn=wx.Button(self,0,'Bascule Tous')
        bxx.Add(btn,0,wx.EXPAND)
        bxx.Add(5,5)
        hbx.Add(bxx,0,wx.EXPAND)
        hbx.Add(20,-1)
        
        
        bx1=wx.StaticBox(self,-1,'Interface',size=(300,-1))
        vbx1=wx.BoxSizer(wx.VERTICAL)
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        ch411=wx.CheckBox(self,-1,'Ajouter Winar au bureau')
        ch421=wx.CheckBox(self,-1,'Ajouter Winar au menu')
        ch431=wx.CheckBox(self,-1,'Creer un groupe winrar')
        
        bxx1.Add(ch411,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(ch421,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(ch431,0,wx.EXPAND)
        bxx1.Add(5,5)
        vbx1.Add(bxx1,0,wx.EXPAND)
        
        vbx1.Add(20,40)
        
        bx2=wx.StaticBox(self,-1,'Interface',size=(300,-1))
        
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        
        ch111=wx.CheckBox(self,-1,'Integrer winrar environement')
        ch211=wx.CheckBox(self,-1,'Menu contexuel')
        ch311=wx.CheckBox(self,-1,'Icone de Menu Contexuel')
        bxx2.Add(ch111,0,wx.EXPAND)
        bxx2.Add(5,5)
        bxx2.Add(ch211,0,wx.EXPAND)
        bxx2.Add(5,5)
        bxx2.Add(ch311,0,wx.EXPAND)
        bxx2.Add(5,5)
        btn1=wx.Button(self,0,'Mode d emploi de menu contextuel')
        bxx2.Add(btn1,0,wx.EXPAND)
        bxx2.Add(5,5)
        vbx1.Add(bxx2,0,wx.EXPAND)
        hbx.Add(vbx1,0,wx.EXPAND)
    
    
        bx3=wx.StaticBox(self,-1,'extraire l archives definie par l utilisateur')
        
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        cx=wx.ComboBox(self,-1)
        bxx3.Add(cx,0,wx.EXPAND)
        vbxP.Add(hbx,0,wx.EXPAND)
        vbxP.Add(10,10)
        vbxP.Add(bxx3,0,wx.EXPAND)
        vbxP.Add(10,85)
        bxxP.Add(vbxP,0,wx.EXPAND)
        self.SetSizer(bxxP)
        
class Vision(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        vbx=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        
        bx=wx.StaticBox(self,-1,'Type de visionneuse',size=(230,-1))
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        rb=wx.RadioButton(self,-1,'visionneuse interne')
        rb1=wx.RadioButton(self,-1,'visionneuse externe')
        rb2=wx.RadioButton(self,-1,'Programme associe')
        rb3=wx.RadioButton(self,-1,'Demander')
        bxx.Add(rb,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(rb1,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(rb2,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(rb3,0,wx.EXPAND)
        bxx.Add(5,5)
        hbx.Add(bxx,0,wx.EXPAND)
        
        
        
        
        bx1=wx.StaticBox(self,-1,'visionneuse Interne',size=(230,-1))
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        rb11=wx.CheckBox(self,-1,'visionneuse interne')
        rb22=wx.CheckBox(self,-1,'visionneuse externe')
        rb33=wx.CheckBox(self,-1,'Programme associe')
        rb44=wx.CheckBox(self,-1,'Demander')
        bxx1.Add(rb11,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(rb22,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(rb33,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(rb44,0,wx.EXPAND)
        hbx.Add(15,15)
        hbx.Add(bxx1,0,wx.EXPAND)
        vbx.Add(10,10)
        vbx.Add(hbx,0,wx.EXPAND)
        vbx.Add(15,15)
        stc=wx.StaticText(self,-1,'Tout Extraire pour')
        txt=wx.TextCtrl(self,-1,'*.exe *.html *.htm *.part *.rar')
        vbx.Add(stc,0,wx.EXPAND)
        vbx.Add(txt,0,wx.EXPAND)
        vbx.Add(10,10)
        
        
        stc1=wx.StaticText(self,-1,'Ignorer les modification pour')
        txt1=wx.TextCtrl(self,-1)
        vbx.Add(stc1,0,wx.EXPAND)
        vbx.Add(txt1,0,wx.EXPAND)
        vbx.Add(10,10)
        hxb1=wx.BoxSizer(wx.HORIZONTAL)
        
        btns=wx.Button(self,-1,'Parcour...')
        
        stc11=wx.StaticText(self,-1,'Nom de la visionneuse externe')
        txt11=wx.TextCtrl(self,-1,size=(390,-1))
        hxb1.Add(txt11,0,wx.EXPAND|wx.ALL)
        hxb1.Add(10,10)
        hxb1.Add(btns,0,wx.EXPAND|wx.ALIGN_RIGHT)
        
        vbx.Add(stc11,0,wx.EXPAND)
        vbx.Add(hxb1,0,wx.EXPAND)
        
        
        self.SetSizer(vbx)
        

class general(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        
        bxP=wx.StaticBox(self,-1,'Historique')
        bxxP=wx.StaticBoxSizer(bxP,wx.VERTICAL)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbxP=wx.BoxSizer(wx.HORIZONTAL)
        
        
        vbx1=wx.BoxSizer(wx.VERTICAL)
        
        vbx2=wx.BoxSizer(wx.VERTICAL)
        
        bx=wx.StaticBox(self,-1,'Systeme ')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        ch=wx.CheckBox(self,-1,'Priorite Fiable')
        
        ch1=wx.CheckBox(self,-1,'Traitement Multitransactionnel')
        
        bxx.Add(ch,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(ch1,0,wx.EXPAND)
        vbx1.Add(bxx,0,wx.EXPAND)
        vbx1.Add(10,10)
        
        
        bx1=wx.StaticBox(self,-1,'Historique')
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        ch3=wx.CheckBox(self,-1,'Conserver historique de l archiver')
        
        ch4=wx.CheckBox(self,-1,'Histoiriques des boites dialogue')
        bxx1.Add(10,10)
        bxx1.Add(ch3,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(ch4,0,wx.EXPAND)
        bxx1.Add(5,5)
        vbx1.Add(bxx1,0,wx.EXPAND)
        
        
        
        bx2=wx.StaticBox(self,-1,'Barre d outils')
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        
        cx=wx.ComboBox(self,-1,choices=['Boutton grand Format','Boutton petit Format','grands Format'])
        
        ch5=wx.CheckBox(self,-1,'Afficher le text dans Button')
        ch6=wx.CheckBox(self,-1,'AVerrouiller les barres d outils')
        
        hbx1=wx.BoxSizer(wx.HORIZONTAL)
        
        btn=wx.Button(self,-1,'Barre d outils')
        btn1=wx.Button(self,-1,'Buttons ...')
        hbx1.Add(btn,0,wx.EXPAND)
        hbx1.Add(5,5)
        hbx1.Add(btn1,0,wx.EXPAND)
        
        bxx2.Add(cx,0,wx.EXPAND)
        bxx2.Add(10,10)
        bxx2.Add(ch5,0,wx.EXPAND)
        bxx2.Add(5,5)
        bxx2.Add(ch6,0,wx.EXPAND)
        bxx2.Add(10,10)
        bxx2.Add(hbx1,0,wx.EXPAND)
        bxx2.Add(10,10)
        vbx1.Add(10,10)
        vbx1.Add(bxx2,0,wx.EXPAND)
        
        bx3=wx.StaticBox(self,-1,'Inteface')
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        
        ch7=wx.CheckBox(self,-1,'Activer l assistant de demerrage')
        
        ch8=wx.CheckBox(self,-1,'Activer les sons')
        ch9=wx.CheckBox(self,-1,'Afficher commentaire de l archives')
        ch10=wx.CheckBox(self,-1,'Reutiliser la fenetre existante')
        ch11=wx.CheckBox(self,-1,'Toujours au dessus')
        ch12=wx.CheckBox(self,-1,'Chemins Complete dans la barre de tache')
        ch13=wx.CheckBox(self,-1,'Barre de Progression Windows')
        ch14=wx.CheckBox(self,-1,'Barre de Progression de la barre des taches')
        bxx3.Add(ch7,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch8,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch9,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch10,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch11,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch12,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch13,0,wx.EXPAND)
        bxx3.Add(5,5)
        bxx3.Add(ch14,0,wx.EXPAND)
        bxx3.Add(5,5)
        vbx2.Add(bxx3,0,wx.EXPAND)
        
        
        bx4=wx.StaticBox(self,-1,'Journal')
        bxx4=wx.StaticBoxSizer(bx4,wx.VERTICAL) 
        
        ch14=wx.CheckBox(self,-1,'Consigner les erreur dans le journal')
        ch15=wx.CheckBox(self,-1,'limite la taille du journal')
        
        bxx4.Add(ch14,0,wx.EXPAND)
        bxx4.Add(5,5)
        bxx4.Add(ch15,0,wx.EXPAND)
        vbx2.Add(20,50)
        vbx2.Add(bxx4,0,wx.EXPAND)
        
        
        hbxP.Add(vbx1,0,wx.EXPAND)
        hbxP.Add(20,10)
        hbxP.Add(vbx2,0,wx.EXPAND)
        
        vbxP.Add(hbxP,0,wx.EXPAND)
        bxxP.Add(vbxP,0,wx.EXPAND)
        
        self.SetSizer(bxxP)

class Compression(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        bxP=wx.StaticBox(self,-1)
        bxxP=wx.StaticBoxSizer(bxP,wx.VERTICAL)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)

        bx=wx.StaticBox(self,-1,'Profile de compression',size=(230,-1))
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        btn=wx.Button(self,-1,'Creer un Profile')
        btn1=wx.Button(self,-1,'Organiser')
        
        bxx.Add(btn,0,wx.EXPAND)
        bxx.Add(btn1,0,wx.EXPAND)
        hbx.Add(bxx,0,wx.EXPAND)
        
        
        bx1=wx.StaticBox(self,-1,'Lister la tailles volumes',size=(230,-1))
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        btn3=wx.Button(self,-1,'Definir la tailles volumes')
        
        bxx1.Add(btn3,0,wx.EXPAND)
        bxx1.Add(10,30)
        hbx.Add(20,20)
        hbx.Add(bxx1,0,wx.EXPAND)
        vbxP.Add(hbx,0,wx.EXPAND)
        vbxP.Add(20,20)
        bx3=wx.StaticBox(self,-1,'Types de fichier a ouvrir en tant archives')
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        cx=wx.ComboBox(self,-1,choices=['*.exe'])
        bxx3.Add(cx,0,wx.EXPAND)
        vbxP.Add(bxx3,0,wx.EXPAND)
        bxxP.Add(vbxP,0,wx.EXPAND)
        self.SetSizer(bxxP)        
class chemin(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        bxP=wx.StaticBox(self,-1)
        bxxP=wx.StaticBoxSizer(bxP,wx.VERTICAL)
        
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        vbx=wx.BoxSizer(wx.VERTICAL)
        bx=wx.StaticBox(self,-1,'Dossier pour les fichier temporale ')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        btn=wx.Button(self,-1,'Parcours')
        txt=wx.TextCtrl(self,-1,size=(380,-1))
        ch=wx.CheckBox(self,-1,'Utiliser uniquement pour les support amovide')
        
        hbx.Add(txt,0,wx.EXPAND)
        hbx.Add(10,10)
        hbx.Add(btn,0,wx.EXPAND)
        vbx.Add(hbx,0,wx.EXPAND)
        vbx.Add(5,5)
        vbx.Add(ch,0,wx.EXPAND)
        vbx.Add(5,5)
        bxx.Add(vbx,0,wx.EXPAND)
        
        
        
        
        
        hbx1=wx.BoxSizer(wx.HORIZONTAL)
        vbx1=wx.BoxSizer(wx.VERTICAL)
        bx1=wx.StaticBox(self,-1,'Dossier de Demerrage')
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
       
        btn1=wx.Button(self,-1,'Parcours')
        txt1=wx.TextCtrl(self,-1,size=(380,-1))
        ch1=wx.CheckBox(self,-1,'Restaurer le dernier de travail au demarrage ')
        
        hbx1.Add(txt1,0,wx.EXPAND)
        hbx1.Add(10,10)
        hbx1.Add(btn1,0,wx.EXPAND)
        vbx1.Add(hbx1,0,wx.EXPAND)
        vbx1.Add(5,5)
        vbx1.Add(ch1,0,wx.EXPAND)
        vbx1.Add(5,5)
        bxx1.Add(vbx1,0,wx.EXPAND)
        
        
        hbx2=wx.BoxSizer(wx.HORIZONTAL)
        vbx2=wx.BoxSizer(wx.VERTICAL)
        bx2=wx.StaticBox(self,-1,'Dossier par defaut pour les archive')
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        
        btn2=wx.Button(self,-1,'Parcours')
        txt2=wx.TextCtrl(self,-1,size=(380,-1))
        
        
        hbx2.Add(txt2,0,wx.EXPAND)
        hbx2.Add(10,10)
        hbx2.Add(btn2,0,wx.EXPAND)
        vbx2.Add(hbx2,0,wx.EXPAND)
        vbx2.Add(5,5)
        bxx2.Add(vbx2,0,wx.EXPAND)
        
        
        
        
        
        
        hbx3=wx.BoxSizer(wx.HORIZONTAL)
        vbx3=wx.BoxSizer(wx.VERTICAL)
        bx3=wx.StaticBox(self,-1,'Dossier de Demmerrage')
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        btn3=wx.Button(self,-1,'Parcours')
        txt3=wx.TextCtrl(self,-1,size=(380,-1))
        ch3=wx.CheckBox(self,-1,'Ajouter le nom  del archiver au chemin d acces ')
        ch4=wx.CheckBox(self,-1,'Supprimer les dossier redondant du chemin d acces ')
        
        
        hbx3.Add(txt3,0,wx.EXPAND)
        hbx3.Add(10,10)
        hbx3.Add(btn3,0,wx.EXPAND)
        vbx3.Add(hbx3,0,wx.EXPAND)
        vbx3.Add(5,5)
        vbx3.Add(ch3,0,wx.EXPAND)
        vbx3.Add(5,5)
        
        vbx3.Add(ch4,0,wx.EXPAND)
        vbx3.Add(5,5)
        bxx3.Add(vbx3,0,wx.EXPAND)
    
        
        
        vbxP.Add(bxx,0,wx.EXPAND)
        
        vbxP.Add(15,15)
        
        vbxP.Add(bxx1,0,wx.EXPAND)
        
        vbxP.Add(15,15)
        
        vbxP.Add(bxx2,0,wx.EXPAND)
        
        vbxP.Add(15,15)
        
        vbxP.Add(bxx3,0,wx.EXPAND)
        
        bxxP.Add(vbxP,0,wx.EXPAND)
        
        self.SetSizer(bxxP)
        
        
        
        
        

class listeFichier(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        
        
        bxP=wx.StaticBox(self,-1)
        bxxP=wx.StaticBoxSizer(bxP,wx.VERTICAL)
        
        vbxP=wx.BoxSizer(wx.VERTICAL)
        hbxP=wx.BoxSizer(wx.HORIZONTAL)
        
        
        vbx1=wx.BoxSizer(wx.VERTICAL)
        
        vbx2=wx.BoxSizer(wx.VERTICAL)
        
        bx=wx.StaticBox(self,-1,'Type de liste ')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        
        ch=wx.RadioButton(self,-1,'Affichage en liste')
        
        ch1=wx.RadioButton(self,-1,'Details')
        
        bxx.Add(ch,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(ch1,0,wx.EXPAND)
        vbx1.Add(bxx,0,wx.EXPAND)
        vbx1.Add(10,10)
        
        
        bx1=wx.StaticBox(self,-1,'Style Liste',size=(200,-1))
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        ch3=wx.CheckBox(self,-1,'Affichage en grille')
        
        ch4=wx.CheckBox(self,-1,'Selectionner tout la ligner')
        bxx1.Add(10,10)
        bxx1.Add(ch3,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(ch4,0,wx.EXPAND)
        bxx1.Add(5,5)
        vbx1.Add(bxx1,0,wx.EXPAND)
        
        
        bx3=wx.StaticBox(self,-1,'Inteface',size=(255,-1))
        bxx3=wx.StaticBoxSizer(bx3,wx.VERTICAL)
        
        ch7=wx.RadioButton(self,-1,'clic simple pour ouvrir un element')
        
        ch8=wx.RadioButton(self,-1,'Ne pas souligner les noms')
        ch9=wx.RadioButton(self,-1,'souligner les noms actuel')

        ch10=wx.RadioButton(self,-1,'souligner tous les noms')
        
        
        bxx3.Add(ch7,0,wx.EXPAND)
        bxx3.Add(10,10)
        bxx3.Add(ch8,0,wx.EXPAND)
        bxx3.Add(10,10)
        bxx3.Add(ch9,0,wx.EXPAND)
        bxx3.Add(10,10)
        bxx3.Add(ch10,0,wx.EXPAND)
        bxx3.Add(10,30)
        vbx2.Add(bxx3,0,wx.EXPAND)
        
        
        bx4=wx.StaticBox(self,-1,'Fichiers')
        bxx4=wx.StaticBoxSizer(bx4,wx.VERTICAL) 
        
        ch14=wx.CheckBox(self,-1,'Afficher les archives en premier')
        ch15=wx.CheckBox(self,-1,'Afficher les fichiers NTFS compress ou chriffre')
        hbx2=wx.BoxSizer(wx.HORIZONTAL)
        ch16=wx.CheckBox(self,-1,'Fusionner le contenu du volumer')
        ch17=wx.CheckBox(self,-1,'Afficher les secondes')
        btn17=wx.Button(self,-1,'Polices')
        
        hbx2.Add(ch17,0,wx.EXPAND)
        hbx2.Add(230,20)
        hbx2.Add(btn17,0,wx.EXPAND)
        
        bxx4.Add(ch14,0,wx.EXPAND)
        bxx4.Add(5,5)
        bxx4.Add(ch15,0,wx.EXPAND)
        
        
        bxx4.Add(ch16,0,wx.EXPAND)
        bxx4.Add(5,5)
        
        bxx4.Add(hbx2,0,wx.EXPAND)
        bxx4.Add(5,5)
        
        
        #vbx2.Add(bxx3,0,wx.EXPAND)
        
        
        hbxP.Add(vbx1,0,wx.EXPAND)
        hbxP.Add(20,10)
        hbxP.Add(vbx2,0,wx.EXPAND)
        
        vbxP.Add(hbxP,0,wx.EXPAND)
        vbxP.Add(20,20)
        vbxP.Add(bxx4,0,wx.EXPAND)
        
        bxxP.Add(vbxP,0,wx.EXPAND)
        
        self.SetSizer(bxxP)
        
        
        
class securite(wx.Panel):
    def __init__(self,parant):
        wx.Panel.__init__(self,parent=parant)
        self.SetBackgroundColour(wx.Colour(254,254,255))
        
        vbx=wx.BoxSizer(wx.VERTICAL)
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        
        bx=wx.StaticBox(self,-1,'Type de Fichier non autorise ')
        bxx=wx.StaticBoxSizer(bx,wx.VERTICAL)
        ch=wx.CheckBox(self,-1,'Type de Fichiers a Exclure Extraction')
        txt=wx.TextCtrl(self,-1,'*.exe *.html *.htm *.part *.rar')
        bxx.Add(ch,0,wx.EXPAND)
        bxx.Add(5,5)
        bxx.Add(txt,0,wx.EXPAND)
        
        bx1=wx.StaticBox(self,-1,'Supprimer les fichiers temporaiment')
        bxx1=wx.StaticBoxSizer(bx1,wx.VERTICAL)
        
        
        rb=wx.RadioButton(self,-1,'Jamais')
        rb1=wx.RadioButton(self,-1,'Toujours')
        rb2=wx.RadioButton(self,-1,'Chiffre uniquement')
        bxx1.Add(rb,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(rb1,0,wx.EXPAND)
        bxx1.Add(5,5)
        bxx1.Add(rb2,0,wx.EXPAND)
        
        bx2=wx.StaticBox(self,-1,'Divers')
        bxx2=wx.StaticBoxSizer(bx2,wx.VERTICAL)
        ch=wx.CheckBox(self,-1,'Type de Fichiers a Exclure Extraction')
        bxx2.Add(ch,0,wx.EXPAND)
        bxx2.Add(5,5)
        vbx.Add(20,20)
        vbx.Add(bxx,0,wx.EXPAND)
        vbx.Add(20,20)
        vbx.Add(bxx1,0,wx.EXPAND)
        vbx.Add(20,20)
        vbx.Add(bxx2,0,wx.EXPAND)
        vbx.Add(20,20)
        self.SetSizer(vbx)
        
class parametre(wx.Dialog):
    def __init__(self,parant,titre):
        wx.Dialog.__init__(self,parant,-1,titre,size=(500,500))
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel=wx.Panel(self,-1)
        self.notb = fnb.FlatNotebook(self.panel)
        hbx= wx.BoxSizer(wx.HORIZONTAL)
        
        
        
        vv=Vision(self.notb)
        self.notb.AddPage(vv, "Visionneuse")
        
        ss=securite(self.notb)
        self.notb.AddPage(ss, "Securite")
        
        ii=Integration(self.notb)
        
        self.notb.AddPage(ii, "Integration")
        
        gg=general(self.notb)
        self.notb.AddPage(gg, "General")
        
        cc=Compression(self.notb)
        self.notb.AddPage(cc, "Compression")
        
        ch=chemin(self.notb)
        self.notb.AddPage(ch, "Chemin d acces")
        
        ll=listeFichier(self.notb)
        self.notb.AddPage(ll, "Listes des Fichier")
        
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
        
        
    def OnFerme(self,event):
        self.Destroy()
    
        