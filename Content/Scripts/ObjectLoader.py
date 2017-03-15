import os.path
import json,codecs
import unreal_engine as ue
from unreal_engine import FVector,FRotator

from unreal_engine.classes import Actor, Pawn, Character, ProjectileMovementComponent, PawnSensingComponent, StaticMesh
from unreal_engine.classes import StaticMeshComponent, StaticMeshActor, PointLightComponent

class ObjectLoader:
	def begin_play(self):
		ue.log("begin object loader")
		self.pawn = self.uobject.get_owner()
		#self.world = ue.get_editor_world()
		self.datapath = str(self.pawn.get_property('datafilename'))
		self.objects = []
		ue.log("------------------")
	
	def loadAndSpawnObjects(self):
		ue.log("+++++++++++++++++++")
		ue.log("loadAndSpawnObjects")
		ue.log("checking for "+self.datapath)
		if os.path.exists(self.datapath):
			with codecs.open(self.datapath,"r","utf-8") as f:
				data = json.loads(f.read())
				ue.log(data)
				for obj in data:
					objclass = ue.find_class(obj["type"])
					#ue.log(str(type(objclass))+str(objclass)+"="+obj["json"])
					objinst = self.uobject.actor_spawn(objclass, FVector(0, 0, 0),FRotator(0, 0, 0))
					jsonstr = obj["json"]
					self.objects.append(objinst)
					objinst.call_function("loadjson",jsonstr)
		ue.log("------------------")
					
		
	def clear(self):
		self.objects.clear()
		
	def add(self):
		self.objects.append(self.pawn.get_property('whattoadd'))
		#ue.log(len(self.objects))
		
	def printall(self):
		ue.log(len(self.objects))
	def saveAllObjects(self):
		with codecs.open(self.datapath,"w","utf-8") as f:
			res = []
			for obj in self.objects:
				res.append({"type":obj.get_class().get_name(),"json":obj.savejson()[0]})
				
			f.write(json.dumps(res))
		
	def tick(self, delta_time):
		pass

