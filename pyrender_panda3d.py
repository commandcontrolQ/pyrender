# Alternate version of pyrender
# This version uses Panda3D instead of vtk
# This is better because:
#   - No OpenGL requirement
#   - 32-bit support
# This is worse because:
#   - Controls are very odd
#   - Lighting is buggy

import sys
from struct import calcsize
CHK32 = calcsize("P") * 8
if CHK32 != 32:
    print("Warning: This version of PyRender was made for 32-bit systems. Execution will continue, however it is recommended to use the vtk renderer instead.", file=sys.stderr)

from panda3d.core import Filename, AmbientLight, DirectionalLight, loadPrcFileData
from direct.showbase.ShowBase import ShowBase
import tkinter as tk
from tkinter import filedialog as tkfdialog


# Get window size
valid = False
while not valid:
    WIDTH = int(input("Window width? "))
    if not isinstance(WIDTH, int):
        print("Width entered is not an integer!")
    elif WIDTH < 800:
        print("Width cannot be less than 800!")
    else:
        HEIGHT = int(input("Window height? "))
        if not isinstance(HEIGHT, int):
            print("Height entered is not an integer!")
        elif HEIGHT < 600:
            print("Height cannot be less than 600!")
        else:
            valid = True

# Set window size
loadPrcFileData("", f"win-size {WIDTH} {HEIGHT}")
loadPrcFileData("", "window-title PyRender (32-bit, Panda3D)")

class PyRenderer(ShowBase):
    def __init__(self, modelPath):
        """
        modelPath: Path to .ply model
            string: "C://path//to//model.ply"
        winSize: Width and height of pyrender window
            tuple: (width, height)
        """
        super().__init__()

        # Load 3D model
        self.model = self.loader.loadModel(modelPath)
        self.model.reparentTo(self.render)

        # Initial position and scale
        self.model.setPos(0, 30, -5)

        # Add lighting
        self.initLights()

        # Set BG colour (each var represents a percentage of 255)
        r, g, b = 0.1, 0.2, 0.4
        self.setBGColour(r, g, b)

    def initLights(self):
        # Setup renderer light
        
        # Ambient light
        lightAmb = AmbientLight("ambientLight")
        lightAmb.setColor((.5, .5, .5, 1))
        lightAmbNP = self.render.attachNewNode(lightAmb)
        self.render.setLight(lightAmbNP)

        # Directional light
        lightDir = DirectionalLight("directionalLight")
        lightDir.setDirection((-5, -5, -5))
        lightDir.setColor((.7, .7, .7, 1))
        lightDirNP = self.render.attachNewNode(lightDir)
        self.render.setLight(lightDirNP)

    def setBGColour(self, r, g, b):
        self.win.setClearColor((r, g, b, 1))


# "Open file..." dialog
window = tk.Tk()
window.withdraw()
print("NOTICE: Sometimes, the 'Open file...' dialog can appear at the very back of the desktop.")
plyPath = tkfdialog.askopenfilename( filetypes=[("Polygon models", "*.ply")] )

# If the operation is cancelled, exit program.
# In this case, plyPath becomes an empty string.
if not plyPath:
    print("A polygon model was not selected, exiting the program...")
    sys.exit()

# Convert the file path to a format that Panda3D accepts
modelPath = Filename.fromOsSpecific(plyPath).getFullpath()

renderer = PyRenderer(modelPath)
renderer.run()
