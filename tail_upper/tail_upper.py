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

    tail_upper_fin_base_edges = [\
        (0.,-0.89),(0.,2.07),(1.95,2.31),(3.55,2.8),(5.74,4.92),
        (10.78,4.8),(10.78,4.4),(15.88,4.1)]
    tail_upper_fin_base_thickness = 3.
    tail_upper_fin_base = sw.rotate(-np.pi/2.).void(tail_upper_fin_base_thickness)
    tail_upper_fin_base.add_ribs([0.,1.], tail_upper_fin_base_edges)
    sw.deformation(tail_upper_fin_base, lambda x,y,z: (x,y,z-tail_upper_fin_base_thickness/2.))

    tail_upper_fin_edges = [(0.,0.), (-7.,7.6), (-1.3,89.), (0.,90.), (1.3,89.), (7.,7.6)]
    tail_upper_fin_thickness = 1.6
    tail_upper_fin = sw.rotate(np.pi/2., -np.pi/2.).parent(tail_upper_fin_base,0.).void(tail_upper_fin_thickness)
    tail_upper_fin.add_ribs([0.,1.], tail_upper_fin_edges)
    sw.deformation(tail_upper_fin, tail_upper_fin_deformation)
    sw.deformation(tail_upper_fin, lambda x,y,z: (x,y+(5.74+0.5),z-(4.4+0.4)))

    sw.generate_stl_binary(path, fname)

def tail_upper_fin_deformation(x,y,z):
    target = [(0.,0.), (-7.,7.6), (-1.3,89.), (0.,90.), (1.3,89.), (7.,7.6)]
    range = 0.01
    z_mod1_5 = 2.1
    z_mod2_4 = 0.39
    if target[1][0] - range < x and x < target[1][0] + range:
        return (x,y,z+z_mod1_5)
    elif target[2][0] - range < x and x < target[2][0] + range:
        return (x,y,z+z_mod2_4)
    elif target[4][0] - range < x and x < target[4][0] + range:
        return (x,y,z+z_mod2_4)
    elif target[5][0] - range < x and x < target[5][0] + range:
        return (x,y,z+z_mod1_5)
    return None

if __name__ == "__main__":
    main()