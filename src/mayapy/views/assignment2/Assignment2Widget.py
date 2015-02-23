# Assignment2Widget.py
# (C)2013
# Scott Ernst

import nimble
import random
import math
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment2Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment2Widget, self).__init__(parent, **kwargs)
        self.okButton.clicked.connect(self._handleExample1Button)
        self.homeBtn.clicked.connect(self._handleReturnHome)

        #value = self.comboBox.currentText()
        #print material

#===================================================================================================
#                                                                                 H A N D L E R S

#                                                                                  H A N D L E R S

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

        cmds.select(allDagObjects=True)
        cmds.pointLight(rgb=(1,1,0.5))
        cmds.move(-10,15,14)
        cmds.pointLight(rgb=(1,0.1,0.2))
        cmds.move(-8,15,-10)
        cmds.pointLight(rgb=(1,0.1,0.2))
        cmds.move(-12,15,3)

        material = str(self.comboBox.currentText())
        object3 = str(self.comboBox_2.currentText())
        print material
        array=['plastic1','plastic2','red','gold', 'silver','bronze']
        object = ['captain','soldiers','carpet']
        print array
        # material 1
        #plastic1 = "plastic1"
        plastic1 = cmds.shadingNode('blinn', asShader=True)
        cmds.setAttr("%s.color" % plastic1, 0.95, 0.95, 0.95, type="double3")
        cmds.setAttr("%s.incandescence" % plastic1,0.5, 0.5, 0.5, type="double3")
        #cmds.setAttr("%s.transparency" % plastic1, 0.75, 0.75, 0.75, type="double3")
        #cmds.setAttr("%s.incandescence" % plastic1,0.5, 0.5, 0.5, type="double3")

        # material 2

        plastic2 = cmds.shadingNode('lambert',asShader=True)
        cmds.sets(name="%sSG" % plastic2,renderable=True,noSurfaceShader=True,empty=True)
        cmds.connectAttr("%s.outColor" % plastic2,"%sSG.surfaceShader" % plastic2)
        cmds.setAttr("%s.color" % plastic2,0.1, 1.0, 0.2, type="double3")
        #cmds.setAttr("%s.transparency" % plastic2,0.75, 0.75, 0.75, type="double3")
        cmds.setAttr("%s.incandescence" % plastic2,0.5, 0.5, 0.5, type="double3")

        # material 3
        red = cmds.shadingNode('blinn', asShader=True)
        cmds.setAttr("%s.color" % red, 1.0, 0.1, 0.1, type="double3")
        #cmds.setAttr("%s.transparency" % plastic1, 0.75, 0.75, 0.75, type="double3")
        #cmds.setAttr("%s.incandescence" % plastic1,0.5, 0.5, 0.5, type="double3")

        # material 4
        #metal1 = 'metal1'
        gold = cmds.shadingNode('blinn', asShader=True)
        cmds.setAttr("%s.color" % gold, 1.0, 0.8, 0.0, type="double3")

        # material 5
        silver = cmds.shadingNode('blinn', asShader=True)
        #cmds.setAttr("%s.color" % silver, 0.75, 075, 0.75, type="double3")
        cmds.setAttr("%s.color" % silver, 0.9, 0.9, 1.0, type="double3")

         # material 6
        bronze = cmds.shadingNode('blinn', asShader=True)
        cmds.setAttr("%s.color" % bronze, 0.8, 0.5, 0.2, type="double3")

        cmds.select(object3)
        if(material == array[0]):
            cmds.hyperShade(assign = plastic1)
        elif(material ==array [1]):
             cmds.hyperShade(assign = plastic2)
        elif(material ==array [2]):
             cmds.hyperShade(assign = red)
        elif(material ==array [3]):
             cmds.hyperShade(assign = gold)
        elif(material ==array [4]):
             cmds.hyperShade(assign = silver)
        elif(material ==array [5]):
             cmds.hyperShade(assign = bronze)


        #
        #cmds.hyperShade( assign=plastic2)
#___________________________________________________________________________________________________ _handleReturnHome
    #def getComboBoxdata(self):



    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
