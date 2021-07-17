import multiprocessing

from panda3d.core import loadPrcFile    #to load .prc file
loadPrcFile("config\config.prc")        #it contains configurational settings

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec4                     #it is a 4 dimensional vector
from panda3d.core import AmbientLight
from panda3d.core import DirectionalLight

import menu
import SerialRead
import PlotGraph

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.models = Models()
        menu.Menu.first_frame(self)
        self.Head = 0.0;
        self.Pitch = 0.0;
        self.Roll = 0.0;

        self.lighting()


    def lighting(self):
        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(mainLight)
        # Turn it around by 45 degrees, and tilt it down by 45 degrees
        self.mainLightNodePath.setHpr(45, -45, 0)
        render.setLight(self.mainLightNodePath)


    def taskmanager(self):
        self.taskMgr.add(self.update, "update")


    def update(self, task):

        length_shared_data_time = len(shared_data_time)-1

        try:
            self.Head = shared_data_head[length_shared_data_time]
            self.Pitch = shared_data_pitch[length_shared_data_time]
            self.Roll = shared_data_roll[length_shared_data_time]

        except (IndexError, ValueError):
            return task.cont

        self.models.model.setHpr(self.Head, self.Pitch, self.Roll)
        return task.cont


    def screenManagement(self,port_baud_entered):
        port_baud[0] = port_baud_entered

        self.first_screen.hide()

        SerialRead_process1.start()
        PlotGraph_process2.start()

        menu.Menu.second_frame(self)





class Models(Game):

    def __init__(self):
        pass


    def Rocket(self):
        game.second_screen.hide()
        game.taskmanager()
        self.model = loader.loadModel("assets/characters/rocketdae.dae")
        self.model.reparentTo(render)
        self.model.setPos(0, 0, 0)
        self.model.setScale(10, 10, 10)


    def Drone(self):
        game.second_screen.hide()
        game.taskmanager()
        self.model = loader.loadModel("models/misc/rgbCube")
        self.model.reparentTo(render)
        self.model.setPos(0,0,0)
        self.model.setScale(20,20,5)


    def SelfBalancingRobot(self):
        game.second_screen.hide()
        game.taskmanager()
        self.model = loader.loadModel("models/panda")
        self.model.reparentTo(render)
        self.model.setPos(0,0,0)


    def Cuboid(self):
        game.second_screen.hide()
        game.taskmanager()
        self.model = loader.loadModel("models/misc/rgbCube")
        self.model.reparentTo(render)
        self.model.setPos(0,0,0)
        self.model.setScale(20,20,5)






if __name__ == '__main__':
    manager = multiprocessing.Manager()

    port_baud = manager.dict()

    shared_data_supervisor = manager.dict()
    shared_data_supervisor[0] = 'stop'

    shared_data_time = manager.list()
    shared_data_head = manager.list()
    shared_data_pitch = manager.list()
    shared_data_roll = manager.list()

    SerialRead_process1 = multiprocessing.Process(target = SerialRead.ReadData, args= (port_baud, shared_data_supervisor, shared_data_time, shared_data_head, shared_data_pitch, shared_data_roll,))

    PlotGraph_process2 = multiprocessing.Process(target = PlotGraph.PlotGraph_process, args = (shared_data_supervisor, shared_data_time, shared_data_head, shared_data_pitch, shared_data_roll,))

    game = Game()
    game.run()