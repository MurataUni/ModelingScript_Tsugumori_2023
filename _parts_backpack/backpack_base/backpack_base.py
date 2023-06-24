import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    base_edges = [(-3.71,-5.46),(-3.71,4.13),(4.30,15.74),(6.02,15.74),(6.02,-7.17)]
    base_thickness = 6.

    base_1 = sw.parent(sw.move_x(-7.)).rotate(-np.pi/2.).void(base_thickness)
    base_1.add_ribs(edges=base_edges)
    sw.deformation(base_1, lambda x,y,z: (x,y,z-base_thickness/2.))

    base_2 = sw.parent(sw.move_x(7.)).rotate(-np.pi/2.).void(base_thickness)
    base_2.add_ribs(edges=base_edges)
    sw.deformation(base_2, lambda x,y,z: (x,y,z-base_thickness/2.))
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()