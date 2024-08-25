# 3D model renderer in Python
# This version uses the vtk module - NOT FOR 32-bit systems!

from struct import calcsize
CHK32 = calcsize("P") * 8
if CHK32 == 32:
    raise SystemError("You are running a 32-bit operating system! VTK cannot run on 32-bit operating systems! This program will now terminate.")

import vtk
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Initialise an object (at this point the object has no values so the object is nothing)

vtkobject = vtk.vtkPolyData()

vtkobject.SetPoints(vtk.vtkPoints())
vtkobject.SetPolys(vtk.vtkCellArray())
vtkobject.SetVerts(vtk.vtkCellArray())
vtkobject.SetLines(vtk.vtkCellArray())
vtkobject.SetStrips(vtk.vtkCellArray())

vtk.vtkPolyDataWriter().WriteToOutputStringOn()

# Load the geometry

reader = vtk.vtkPLYReader()

# Load the polygon file

path = filedialog.askopenfilename(filetypes=[("Polygon models", "*.ply")])

# If the user cancels the operation, an empty string is returned.
# "if not path" can be used in this scenario to prevent errors.
if not path:
    quit()

reader.SetFileName(path)
reader.Update()
vtkobject.DeepCopy(reader.GetOutput())

# Create a mapper (with the vtkobject as input data) and an actor (using the newly created mapper) for the object

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(vtkobject)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer (with the newly created actor) and a window.

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

r = 0.1
g = 0.2
b = 0.4

# This function sets the background color using an RGB color specification (each float is a percentage amount of 255)
renderer.SetBackground(r, g, b)


window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

# Set the size of the newly created window to the user's input

WIDTH = int(input("Window width? "))
HEIGHT = int(input("Window height? "))

window.SetSize(WIDTH, HEIGHT)

# Start the interactor loop

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.Initialize()
interactor.Start()
