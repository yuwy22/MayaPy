# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
import random
import math
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment1Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment1Widget, self).__init__(parent, **kwargs)
        self.exampleBtn.clicked.connect(self._handleExample1Button)
        self.example2Btn.clicked.connect(self._handleExample2Button)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                  H A N D L E R S

#___
    def _handleExample2Button(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.


        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
        """


        # creat the transparent container
        cmds.polyCylinder(name='container', r=1.6, axis=(0, 1, 0), height=3.2)
        cmds.select('container')
        cmds.polyColorPerVertex(r=0.4, g=1, b=1, a=0.05, colorDisplayOption=True)
        cmds.move(0.0, 1.6, 0, relative=True)

        # create a bubble
        cmds.polySphere(name='bubble', radius=0.01)
        pos_x = 0
        pos_y = 0
        pos_z = 0
        total_bubbles = 50
        for nth_num in xrange(0, total_bubbles):
            bubble = 'bubble' + str(nth_num)
            cmds.duplicate('bubble', n=bubble)
            cmds.select(bubble)
            cmds.polyColorPerVertex(r=1, g=1, b=0.75, a=1, colorDisplayOption=True)
            x_vib = random.uniform(-1.0, 1.0)
            z_vib = random.uniform(-1.0, 1.0)
            cmds.move(x_vib, 0.0, z_vib, bubble)
            start_frame = int(random.uniform(0, 124 - 30))
            print start_frame
            xRot = random.uniform(0, 360 )
            yRot = random.uniform(0, 360 )
            zRot = random.uniform(0, 360 )
            for frame in xrange(0, 124):
                if ( frame - start_frame >= 0 and frame-start_frame < 30):  # the first 40 frames, the bubble remains at the bottom while growing bigger
                    cmds.setKeyframe(bubble, attribute='scaleX', value=0.5 * ((frame-start_frame) / 30.0), t=frame)
                    cmds.setKeyframe(bubble, attribute='scaleY', value=0.3 * ((frame-start_frame) / 30.0), t=frame)
                    cmds.setKeyframe(bubble, attribute='scaleZ', value=0.5 * ((frame-start_frame) / 30.0), t=frame)
                elif (frame- start_frame >= 30):
                    pos_y = 3.0 * ((frame- start_frame - 30) / 84.0)  # from frame 40, the bubble getting bigger and ascend to the top
                    pos_x = x_vib + random.uniform(-0.03,0.03)
                    pos_z = z_vib + random.uniform(-0.03,0.03)
                    xRot = xRot + 0.3
                    yRot = yRot + 0.03
                    zRot = zRot + 0.3
                    factor = 1.1*math.tan(3.14/4*frame/124.0)
                    #cmds.blendShape(edit=True,en=0.8)
                    cmds.setKeyframe(bubble, attribute='translateX', value= pos_x, t = frame)
                    cmds.setKeyframe(bubble, attribute='translateY', value=pos_y, t=frame)
                    cmds.setKeyframe(bubble, attribute='translateZ', value= pos_z, t = frame)
                    cmds.setKeyframe(bubble, attribute='scaleX', value = 0.5 + 3.0 * factor*((frame-start_frame)/ 84.0), t=frame)
                    cmds.setKeyframe(bubble, attribute='scaleY', value = 0.3 + 1.8 * factor*((frame-start_frame)/ 84.0), t=frame)
                    cmds.setKeyframe(bubble, attribute='scaleZ', value = 0.5 + 2.4 *factor* ((frame-start_frame) / 84.0), t=frame)
                    cmds.setKeyframe(bubble, attribute='rotateX', value= xRot, t=frame)
                    cmds.setKeyframe(bubble, attribute='rotateY', value= yRot, t=frame)
                    cmds.setKeyframe(bubble, attribute='rotateZ', value= zRot, t=frame)
        cmds.delete('bubble')

# ________________________________________________________________________________________________ _handleReturnHome
    def _handleExample1Button(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.


        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
        """
        cmds.polySphere(name = 'bubble', radius = 0.01)
        cmds.polyCylinder(name='container', r=1.6, axis=(0, 1, 0), height=3.2)
        cmds.select('container')
        cmds.polyColorPerVertex(r=0.4, g=1, b=1, a=0.05, colorDisplayOption=True)
        cmds.move(0.0, 1.6, 0, relative=True)
        pos_x = 0
        pos_y = 0
        pos_z = 0
        for frame in xrange(0,124):
            if frame < 40 :  # the first 40 frames, the bubble remains at the bottom while growing bigger
                cmds.setKeyframe('bubble', attribute= 'scaleX', value= 0.5*(frame/40.0), t = frame)
                cmds.setKeyframe('bubble', attribute= 'scaleY', value= 0.5*(frame/40.0), t = frame)
                cmds.setKeyframe('bubble', attribute= 'scaleZ', value= 0.5*(frame/40.0), t = frame)
            else :
                pos_y = 3.0*((frame-40)/84.0)  # from frame 40, the bubble getting bigger and ascend to the top
                cmds.setKeyframe('bubble', attribute= 'translateY', value= pos_y, t = frame)
                cmds.setKeyframe('bubble', attribute= 'translateX', value= pos_x, t = frame)
                cmds.setKeyframe('bubble', attribute= 'scaleX', value= 0.5 + 2.5*(frame/84.0), t = frame)
                cmds.setKeyframe('bubble', attribute= 'scaleY', value= 0.5 + 2.3*(frame/84.0), t = frame)
                cmds.setKeyframe('bubble', attribute= 'scaleZ', value= 0.5 + 2.5*(frame/84.0), t = frame)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
