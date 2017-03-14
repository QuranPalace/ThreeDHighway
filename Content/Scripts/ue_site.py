import os,os.path,sys
import inspect
import unreal_engine as ue

def helloworld():
    ue.log('بسم الله الرحمن الرحيم')

ue.add_menu_extension('بسم الله', helloworld,'ابزارها')

ue.log("---------------------")
ue.log(__file__)
ue.log(os.getcwd())
ue.log(os.path.realpath(__file__))
ue.log(sys.path[0])
ue.log(os.path.abspath(inspect.getfile(inspect.currentframe())))

#os.chdir(sys.path[0])

for script in [ x for x in os.listdir(sys.path[0]) if x.endswith(".py") and x.startswith("_")]:
	ue.log(script+"---"+os.path.realpath(os.path.join(sys.path[0],script)))
	ue.add_menu_extension(script[:-3], lambda : exec(open(os.path.realpath(os.path.join(sys.path[0],script))).read()),'Py')