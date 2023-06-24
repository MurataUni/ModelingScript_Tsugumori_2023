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

    tail_base_adapter = sw.pole(5., 1.5, 2.*np.pi, 32, True)

    tail_base_start_edges = [\
        (3.2, -2.8), (4.61, -2.8), (9.81, -2.8), (9.81, 2.8), (4.61, 2.8), \
        (3.2, 2.8), (0., 2.8), (0., -1.95), (0.8, -2.8)]
    tail_base_start_thickness = 4.4
    tail_base_start = sw.rotate(-np.pi/2.).parent(tail_base_adapter, 1.-1.5/5.).void(tail_base_start_thickness)
    tail_base_start.add_ribs([0.,1.], tail_base_start_edges)
    sw.deformation(tail_base_start, lambda x,y,z: (x,y,z-tail_base_start_thickness/2.))
    sw.deformation(tail_base_start, tail_base_start_deformation)

    tail_base_end_edges = [\
        (16.75,0.02),(18.82,1.01),(17.95,6.78),(15.98,6.71),(15.62,6.68),\
        (14.78,8.78),(12.59,10.07),(10.78,9.65),(9.58,8.38),(8.40,4.47),\
        (5.13,2.),(4.99,-0.68),(9.81,-2.9)]
    tail_base_end_thickness = 8.2
    tail_base_end = sw.rotate(-np.pi/2.).parent(tail_base_adapter, 1.-1.5/5.).void(tail_base_end_thickness)
    tail_base_end.add_ribs([0.,1.], tail_base_end_edges)
    sw.deformation(tail_base_end, lambda x,y,z: (x,y,z-tail_base_end_thickness/2.))
    sw.deformation(tail_base_end, tail_base_end_deformation)

    sw.generate_stl_binary(path, fname)

def tail_base_start_deformation(x,y,z):
    range = 0.1
    z_mod = (4.6-3.)/2.
    if 3.2 + range < x:
        if z < 0.:
            return (x,y,z+z_mod)
        else:
            return (x,y,z-z_mod)
    return None

def tail_base_end_deformation(x,y,z):
    range = 0.1
    z_mod = (8.2-4.4)/2.
    if 16.75 + range < x:
        if z < 0.:
            return (x,y,z+z_mod)
        else:
            return (x,y,z-z_mod)
    return None

if __name__ == "__main__":
    main()