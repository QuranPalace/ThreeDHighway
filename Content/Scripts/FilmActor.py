import unreal_engine as ue
import json

class FilmActor:

	def begin_play(self):
		self.pawn = self.uobject.get_owner()
	
	def getjson(self):
		ue.log("@@@@video getting json:")
		loc = self.uobject.get_actor_location()
		rot = self.uobject.get_actor_forward()
		data = {
			"x":loc.x,"y":loc.y,"z":loc.z,
			"rx":rot.x, "ry":rot.y, "rz": rot.z
		}
		return json.dumps(data)
	def addtoworld(self):
		ue.log("@@@@video add to world")
		return ""
	def setjson(self,js):
		ue.log("@@@@video setting json:")
		data = json.loads(js)
		loc = self.uobject.get_actor_location()
		loc.x = data["x"]
		loc.y = data["y"]
		loc.z = data["z"]
		self.uobject.set_actor_location(loc)
		
		rot = self.uobject.get_actor_forward()
	
		return True
		
	def tick(self, delta_time):
		pass