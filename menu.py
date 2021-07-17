from direct.gui.DirectGui import *



class Menu():

    def first_frame(self):

        self.first_screen = DirectDialog(frameSize=(base.a2dLeft, base.a2dRight,base.a2dBottom, base.a2dTop),
                                           fadeScreen=0.4,
                                           relief=DGG.FLAT)

        label = DirectLabel(text="Orientation Simulator",
                            parent=self.first_screen,
                            scale=0.2,
                            pos=(0, 0, 0.8))

        label = DirectLabel(text="please enter the serial port name and baud rate",
                            parent=self.first_screen,
                            scale=0.1,
                            pos=(0, 0, 0.2))

        entry = DirectEntry(scale=0.06,
                            width= 12,
                            pos=(-0.4,0,0),
                            color=(1,1,1,1),
                            command = self.screenManagement, #sends the entered port_name and baud_rate to SerialRead.py through portBaudSender in main class
                            initialText="PORT NAME , BAUD RATE",
                            parent=self.first_screen)


        self.first_screen.show()

    def second_frame(self):

        self.second_screen = DirectDialog(frameSize=(base.a2dLeft, base.a2dRight,base.a2dBottom, base.a2dTop),
                                           fadeScreen=0.4,
                                           relief=DGG.FLAT)

        label = DirectLabel(text="PLEASE SELECT YOUR MODEL",
                            parent=self.second_screen,
                            scale=0.18,
                            pos=(0, 0, 0.6))

        btn = DirectButton(text="ROCKET",
                           command=self.models.Rocket,
                           pos=(0, 0, 0.2),
                           parent=self.second_screen,
                           scale=0.09)

        btn = DirectButton(text="DRONE",
                           command=self.models.Drone,
                           pos=(0, 0, 0),
                           parent=self.second_screen,
                           scale=0.09)


        btn = DirectButton(text="SELF BALANCING ROBOT",
                           command=self.models.SelfBalancingRobot,
                           pos=(0, 0, -0.2),
                           parent=self.second_screen,
                           scale=0.09)


        btn = DirectButton(text="CUBOID",
                           command=self.models.Cuboid,
                           pos=(0, 0, -0.4),
                           parent=self.second_screen,
                           scale=0.09)


        self.second_screen.show()





