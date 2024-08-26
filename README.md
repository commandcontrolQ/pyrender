# pyrender - 3D Model renderer in Python

> [!WARNING]
> This program can be very resource-intensive depending on the model used.
>
> There are no definitive **hardware requirements**, however the following are recommended:
> - Windows users should use at least Windows 10 (Extensions such as VxKex and the OneCore API have not been tested, use at your own discretion)
> - Linux (Debian) users should use at least Debian 11 (in theory backporting might work however it has not been tested)
> - AMD Ryzen 3 3000 series / Intel Core i3 5th Gen
> - Integrated Graphics **minimum**
> - At least 4GB of RAM

> [!NOTE]
> The 32-bit Windows compile of PyRender has not been released yet.
>
> This is because Panda3D applications must be compiled using their own tool, instead of using something like PyInstaller. Unfortunately, even with this information, I have not been able to successfuly compile PyRender.
>
> If you have been able to successfuly compile the Panda3D-based PyRender for 32-bit systems, please contact me.

### Requirements:
- Python (recommended 3.10 or newer)
- 'vtk' module for 64 bit installations
- 'panda3d' module for 32-bit installations
- A .ply polygon model (this repo comes with lots of sample .ply files for you to use, credits are located at the bottom)

[This website](https://3d-convert.com/en/convert/stl-to-ply.html) can be used to convert .stl models into .ply models.

# Controls
> [!IMPORTANT]
> The controls below are hardcoded by the renderer and cannot be changed.
### Controls (vtk renderer):
- "e": Exit application

- "f": Fly to cursor (if cursor is pointing to the model)

- "r": Reset camera

- "s": View actors as surfaces

- "w": View actors as wireframes

- Left click: Rotate camera

- Scroll wheel: Zoom in/out

### Controls (panda3d renderer):
The Panda3D renderer only makes use of the mouse for controls.

- Left click: Pan left and right

- Right click: Move forwards and backwards

- Middle click: Rotate around the application origin

- Right click + Middle click: Roll the point of view around the view axis

# Credits

Courtesy to:

- zzubnik for the teapot (https://cults3d.com/en/users/zzubnik/3d-models)

- Martin for the Endeavour space shuttle [WARNING: Can cause lag on lower-spec systems] (https://www.printables.com/@Martin)

- Matthias L for the low poly cat (https://www.printables.com/@MatthiasL)

- Marvin for the ring toy [WARNING: Can cause lag on lower-spec systems] (https://www.printables.com/@Marvin)

- BP for the low poly wolf (https://www.printables.com/@BPmakesthings)

- Thorin Oakenshield for the gear (https://www.printables.com/@ThorinOakenshield)

- Bing AI for helping me remember how to create a 'Open file' window

- ChatGPT for helping me understand how Panda3D works

- 3DJG for the platonic solids (https://www.printables.com/@3DJG_199655)

- Kijai for the moon city [WARNING: Can cause lag on lower-spec systems] (https://www.printables.com/@Kijai)

- Agustin Arroyo for the low poly snorlax [WARNING: Can cause lag on lower-spec systems] (https://www.printables.com/@flowalistik)

- Mothdotmonster for the calibration cat (https://www.printables.com/@mothdotmonster)

- Gdrag for the container [WARNING: Very likely to cause lag!*] (https://www.printables.com/@gdrag)

- Ruben Martins for the sand castle (https://www.printables.com/@RubenMartins_242064)

- Robert-HV for the trash can (https://www.printables.com/@RobertHV)

- ak for the low poly dachsund (https://www.printables.com/@ak_211779)

*This container is the largest polygon model (in file size) in the entire repository.
