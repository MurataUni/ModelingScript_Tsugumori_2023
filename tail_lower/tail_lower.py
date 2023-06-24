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
    
    tail_lower_fin_adapter = sw.rectangular(3.4, 4., 5.6)

    tail_lower_fin_base_edges = [(0., 3.6), (4.5, -0.2), (3.6, -3.), (-3.6, -3.), (-4.5, -0.2)]
    tail_lower_fin_base = sw.rotate(0., np.pi).parent(tail_lower_fin_adapter, 0.5).void(9.)
    tail_lower_fin_base.add_ribs((0.,1.), tail_lower_fin_base_edges)

    tail_lower_fin_edges = [\
        (0., 0.), (3.5, -0.5), (7., -5.6), (11.3, 9.), (4.8, 58.8), (0., 64.4),\
        (-4.8, 58.8), (-11.3, 9.), (-7., -5.6), (-3.5, -0.5)]
    tail_lower_fin_thickness = 1.8
    tail_lower_fin_geta_1 = sw.parent(tail_lower_fin_base, 0.).rotate_x(-np.pi/2)
    tail_lower_fin_geta_2 = sw.parent(tail_lower_fin_geta_1, 0.).void(3.6)
    tail_lower_fin = sw.rotate(0., np.pi).parent(tail_lower_fin_geta_2).void(tail_lower_fin_thickness)
    tail_lower_fin.add_ribs([0.,1.], tail_lower_fin_edges)
    sw.deformation(tail_lower_fin, lambda x,y,z: (x,y,z-tail_lower_fin_thickness/2.))
    sw.deformation(tail_lower_fin, tail_lower_fin_deformation)

    sw.generate_stl_binary(path, fname)

def tail_lower_fin_deformation(x,y,z):
    range = 0.01
    z_mod_ratio = 3.8/4.5
    x_mod = 1.
    if x < 0. - range or 0. + range < x:
        if z < 0.:
            if x < 0.:
                return (x+x_mod,y,z-abs(x)*z_mod_ratio)
            else:
                return (x-x_mod,y,z-abs(x)*z_mod_ratio)
        else:
            return (x,y,z-abs(x)*z_mod_ratio)
    return None

if __name__ == "__main__":
    main()