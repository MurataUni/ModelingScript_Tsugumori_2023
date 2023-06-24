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

    base_panel_thickness = 2.

    tip_edges_start = [(-11.,0.),(11.,0.),(0.,-13.5)]
    tip_edges_end = [(-2.9,0.),(2.9,0.),(0.,-3.2)]
    tip_base_thickness = 2.4
    tip_base = sw.parent(sw.void(base_panel_thickness-0.4)).rectangular(8.,14.,tip_base_thickness)
    sw.deformation(tip_base, lambda x,y,z: (x,y+3.5,z))
    tip_geta_1 = sw.parent(tip_base, 1.-0.8/tip_base_thickness).rotate_x(-np.pi/2.)
    tip = sw.parent(tip_geta_1).void(95.)
    tip.add_rib(0., tip_edges_start)
    tip.add_rib(1., tip_edges_end)
    sw.deformation(tip, tip_deformation)

    sw.generate_stl_binary(path, fname)

def tip_deformation(x,y,z):
    range = 0.1
    if z < 0. + range:
        if y < 0. - range:
            return (x,y,z+6.)
    else:
        if y < 0. - range:
            return (x,y,z+4.)
    return None

if __name__ == "__main__":
    main()
