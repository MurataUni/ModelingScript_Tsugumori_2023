import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    edges = [(0.,-0.5),(0.,0.8),(4.,3.),(11.,3.),(12.6,5.6),(14.4,5.6),(16.,0.),(16.,-0.5)]
    thickness = 1.
    interval = 1.

    base_1 = sw.rotate(-np.pi/2.).void()
    base_2 = sw.rotate(0.,-np.pi/2.).parent(base_1).void()

    panel_1 = sw.parent(base_2).void(thickness)
    panel_1.add_ribs([0.,1.], edges)
    sw.deformation(panel_1, lambda x,y,z: (x,y,z-1.5*interval-2*thickness))

    panel_2 = sw.parent(base_2).void(thickness)
    panel_2.add_ribs([0.,1.], edges)
    sw.deformation(panel_2, lambda x,y,z: (x,y,z-0.5*interval-thickness))

    panel_3 = sw.parent(base_2).void(thickness)
    panel_3.add_ribs([0.,1.], edges)
    sw.deformation(panel_3, lambda x,y,z: (x,y,z+0.5*interval))

    panel_4 = sw.parent(base_2).void(thickness)
    panel_4.add_ribs([0.,1.], edges)
    sw.deformation(panel_4, lambda x,y,z: (x,y,z+1.5*interval+thickness))

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()