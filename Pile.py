class Pile():
    def __init__(self):
        self.lst=[]
        
    def Crer(self):
        pass
    
    def empiler(self,val):
        self.lst.append(val)
    
    def depiler(self):
        if self.vide():
            raise ValueError('pile vide')
        return self.lst.pop()
    
    def taille(self):
        i=0
        for j in self.lst:
            i+=1
        return i
    
    def vide(self):
        return self.lst==[]
    
    def sommet(self):
        for i in self.lst:
            print(i)
