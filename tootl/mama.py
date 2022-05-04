import wx
import os
import sys
import wx.lib.agw.flatnotebook as fnb

class Mafenetre(wx.Frame):
    def __init__(self,titre):
        wx.Frame.__init__(self,None,-1,title=titre)

        self.Menu()
        sv=wx.StatusBar(self,-1)
        self.SetStatusBar(sv)
        pal=wx.Panel(self,-1)
        vbx=wx.BoxSizer(wx.VERTICAL)
        self.txt=wx.TextCtrl(pal,-1,style=wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_AUTO_URL,size=(-1,900))
        vbx.Add(self.txt,0,wx.EXPAND|wx.ALL)
        pal.Fit()
        pal.SetSizer(vbx)
        self.txt.SetForegroundColour( wx.Colour( 255, 20, 100 ) )
        self.txt.SetBackgroundColour( wx.Colour( 105, 205, 100 ) )
        #self.lireFichier('papao.txt')
        
        self.txt.CanRedo()
        #po=self.txt.GetValue()
        #print(po[-1])
        self.toolBa()
       
        fg=wx.Colour(25,130,247)
        yy=wx.TextAttr(fg)
        self.txt.SetStyle(3,5,yy)
        #self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEntre)
        
        #devnull = open(os.devnull, 'w')
        #sys.stdout = devnull
        
        self.txt.Bind(wx.EVT_TEXT,self.OnEntres)
        
        self.Show(True)


    def OnEntre(self,event):
        print('enter presse')
        
        
    def OnEntres(self,event):
       
        p=event.GetString()
        
        print(p)

        
        
    def Menu(self):
        menB=wx.MenuBar()
        fichi=wx.Menu('menu') 
        self.new=fichi.Append(1,'&NEW FILE\tCtrl+N','NEW FILE')
        self.Bind(wx.EVT_MENU,self.OnNew,self.new)
        #self.Bind(wx.EVT_MENU,self.lireFichier,fichi)
        fichi.AppendSeparator()
        
        self.open=fichi.Append(-1,'&OPEN FILE\tCtrl+O','OEN FILE')
        self.Bind(wx.EVT_MENU,self.OnOpen,self.open)
        fichi.AppendSeparator()
        
        self.savef=fichi.Append(-1,'&SAVE FILE\tCtrl+S','SAVE FILE')
        
        self.Bind(wx.EVT_MENU,self.OnSaveF,self.savef)
        
        eedit=wx.Menu()
        
        self.copi=eedit.Append(-1,'&COPIER\tCtrl+C','COPIER')
        self.Bind(wx.EVT_MENU,self.OnCopy,self.copi)
        
        self.couper=eedit.Append(-1,'&COUPER\tCtrl+X','COUPER')
        
        self.Bind(wx.EVT_MENU,self.OnCut,self.couper)
        self.coller=eedit.Append(-1,'&COLLER\tCtrl+P','COLLER')
        self.Bind(wx.EVT_MENU,self.OnPaste,self.coller)
        affiche=wx.Menu()
      
        
        menB.Append(fichi,'&FICHIER')
        menB.Append(eedit,'&EDITER')
        menB.Append(affiche,'&AFFICHER')
        self.SetMenuBar(menB)
    
        
    def OnNew(self,event):
       pass
       
            
    def lireFichier(self,nom):
        with open(nom,'r') as ma:
            while True:
                mot=ma.read(6000)
                if mot=='':
                    break
               
                self.txt.AppendText(mot)
                pi=mot.split()[-1]
                #print(pi)
    def toolBa(self):
        tool=wx.ToolBar(self,-1)
       
        self.new=tool.AddTool(-1,'new',wx.Bitmap('tootl\\new.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnFiles,self.new)
        
        self.open=tool.AddTool(-1,'open',wx.Bitmap('tootl\\open.png'))
        self.Bind(wx.EVT_TOOL,self.OnOpen,self.open)
        
        self.save=tool.AddTool(-1,'save',wx.Bitmap('tootl\\save.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnSave,self.save)
        
        tool.AddTool(-1,'print',wx.Bitmap('tootl\\print.png'))
        
        self.cut=tool.AddTool(-1,'cut',wx.Bitmap('tootl\\cut.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnCut,self.cut)
        
        self.copy=tool.AddTool(-1,'copy',wx.Bitmap('tootl\\copy.png'))
        self.Bind(wx.EVT_TOOL,self.OnCopy,self.copy)
        
        self.paste=tool.AddTool(-1,'paste',wx.Bitmap('tootl\\paste.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnPaste,self.paste)
        
        self.redo=tool.AddTool(-1,'redo',wx.Bitmap('tootl\\redo.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnRedo,self.redo)
        self.undo=tool.AddTool(-1,'undo',wx.Bitmap('tootl\\undo.png'))
        
        self.Bind(wx.EVT_TOOL,self.OnUndo,self.undo)
        
        tool.AddTool(-1,'find',wx.Bitmap('tootl\\find.png'))
        tool.AddTool(-1,'findr',wx.Bitmap('tootl\\findr.png'))
        tool.Realize()
        self.SetToolBar(tool)
    
        
    def OnFiles(self,event):
        print('passs')
    
    def OnOpen(self,event):
       
        mo=wx.FileDialog(None,'entrez nom fichier',os.getcwd(),wildcard='*.*')
        ok=mo.ShowModal()
        
        with open(mo.GetPath(),'r') as fi:
            mot=fi.read(6000)
            self.txt.AppendText(mot)
        self.SetTitle(mo.GetPath())
        print(mo.GetPath())
        
    def OnSave(self,event):
        
        mo=wx.FileDialog(None,'entrez nom fichier',os.getcwd(),wildcard='*.txt',style=wx.FD_SAVE)
        ok=mo.ShowModal()
        mot=self.txt.GetValue()
        with open(mo.GetPath(),'w') as fi:
            fi.write(mot)
        self.SetTitle(mo.GetPath())
        
    def OnUndo(self,event):
        self.txt.Undo()
        
    def OnRedo(self,event):
        self.txt.Redo()
    
    def OnCut(self,event):
        self.txt.Cut()
        
    def OnPaste(self,event):
        self.txt.Paste()
        
    def OnCopy(self,event):
        self.txt.Copy()


    def OnSaveF(self,event):
        mo=wx.FileDialog(None,'entrez nom fichier',os.getcwd(),wildcard='*.txt',style=wx.FD_SAVE)
        ok=mo.ShowModal()
        mot=self.txt.GetValue()
        
        with open(mo.GetPath(),'w') as fi:
            fi.write(mot)
app = wx.App()
Mafenetre('Editeur')
app.MainLoop()