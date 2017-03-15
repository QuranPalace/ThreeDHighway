import unreal_engine as ue
import json

class TextActor:

	def begin_play(self):
		self.pawn = self.uobject.get_owner()
	
	def getjson(self):
		ue.log("@@@@getting json:")
		loc = self.uobject.get_actor_location()
		rot = self.uobject.get_actor_forward()
		data = {
			"x":loc.x,"y":loc.y,"z":loc.z,
			"rx":rot.x, "ry":rot.y, "rz": rot.z,
			"title":self.pawn.get_property("title")
		}
		return json.dumps(data)
	def addtoworld(self):
		ue.log("@@@@ add to world")
	def setjson(self,js):
		ue.log("@@@@setting json:")
		data = json.loads(js)
		loc = self.uobject.get_actor_location()
		loc.x = data["x"]
		loc.y = data["y"]
		loc.z = data["z"]
		self.uobject.set_actor_location(loc)
		
		rot = self.uobject.get_actor_forward()
		
		self.pawn.set_property("title", data["title"])
		
	def tick(self, delta_time):
		pass