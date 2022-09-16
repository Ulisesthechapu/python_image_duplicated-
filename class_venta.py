from ast import Return
from tkinter.messagebox import RETRY
import cv2
import numpy as np

class venta:
    def __init__(self, venta ):
        self.venta = venta

class ltsImg:
    def __init__(self, Id,Venta,NameFile,RutaFile):
        self.Id = Id
        self.Venta = Venta
        self.NameFile = NameFile
        self.RutaFile = RutaFile
    
    def ltsImgCom(self,id1,id2,ruta):
        eq = 0
        print("Valor 1 : %s  , Valor 2 : %s" % (id1,id2))
        #print(ruta + id1 + '.jpg')
        img1 = cv2.imread(ruta + id1 + '.jpg')
        img2 = cv2.imread(ruta + id2 + '.jpg')
        # 1) Check if 2 images are equals
        if img1.shape == img2.shape:
            difference = cv2.subtract(img1, img2)
            b, g, r = cv2.split(difference)
            if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
                eq = 1
            else: 
                eq = 0
        return eq

        

          

        
