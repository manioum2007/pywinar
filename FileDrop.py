
import wx
import zipfile
class FileDrop(wx.FileDropTarget):
    def __init__(self,parant):
        wx.FileDropTarget.__init__(self)
        self.parant=parant
        
    def OnDropFiles(self,x,y,filenames):
    
        zip=zipfile.ZipFile(filenames[0],'r')
        btm=wx.Bitmap('tool\\Extract.bmp', wx.BITMAP_TYPE_BMP)
        
        
        btm1=wx.Bitmap('tool\\View.bmp', wx.BITMAP_TYPE_BMP)
        il=wx.ImageList(16,16)
        
        mm=wx.ImageList(16,16)
        il.Add(btm)
        mm.Add(btm1)
        
        self.AssignImageList(il,wx.IMAGE_LIST_SMALL)
        for p in zip.infolist():
            m=str(p.filename)
            try:
                po=m.split('.')[-1]
                
                print(po)
            except:
                pass
            
            self.Append((str(p.filename),str(p.file_size),str(p.FileHeader),"",str(p.date_time),str(p.CRC)))
       
    
    
"""    
class FileDropTarget(wx.FileDropTarget):
    def __init__(self, obj):
        wx.FileDropTarget.__init__(self)
        self.obj = obj
    def OnDropFiles(self, x, y, filenames):
        self.obj.SetInsertionPointEnd()
        self.obj.updateText("\n{} files(s){},{}".format(len(filenames),x,y))
        #self.obj.Clear()
        with open(filenames[0],'r') as fi:
            mot=fi.read()
            self.obj.updateText(mot)
"""