import os.path
import json,codecs
import unreal_engine as ue
from unreal_engine import FVector,FRotator

from unreal_engine.classes import Actor, Pawn, Character, ProjectileMovementComponent, PawnSensingComponent, StaticMesh
from unreal_engine.classes import StaticMeshComponent, StaticMeshActor, PointLightComponent

import ctypes

def GetTextDimensions(text, points, font):
	class SIZE(ctypes.Structure):
		_fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]
	hdc = ctypes.windll.user32.GetDC(0)
	hfont = ctypes.windll.gdi32.CreateFontA(-points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
	hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)
	size = SIZE(0, 0)
	ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))
	ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
	ctypes.windll.gdi32.DeleteObject(hfont)
	return (size.cx, size.cy)

class TextUtils:
	def begin_play(self):
		self.pawn = self.uobject.get_owner()
		self.size = 48
		self.face = "IRLotus"
		
	def tick(self, delta_time):
		pass

	def setDefaultTextSize(self,size):
		self.size = int(size)
	def setDefaultTextFace(self,font):
		self.face = font
	def getWordDesireSize(self,word):
		r = GetTextDimensions(word,self.size,self.face)[0]
		ue.log("get word size of"+ word + ",%s,%s=%s"%(str(self.size),str(self.face),str(r)) )
		return r
	
