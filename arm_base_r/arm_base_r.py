import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    edges = [(0., 0.), (0., 13.3), (-1.3, 15.), (-1.3, 20.5), (16., 20.5), (30., 9.), (19.2, 0.)]
    down_modification = 10.5
    back_modification = 12.5
    base = sw.create_from_spec(Const.Base.spec, only_keel=True)
    base.add_ribs([0., 1.], edges)
    sw.deformation(base, base_deformation)
    sw.deformation(base, lambda x,y,z: (x-back_modification, y-down_modification, z))

    sw.generate_stl_binary(path, fname, divided=False)

def base_deformation(x,y,z):
    target = [(0., 0.), (0., 13.3), (-1.3, 15.), (-1.3, 20.5), (16., 20.5), (30., 9.), (19.2, 0.)]
    range = 0.1
    tickness = 5.7
    if target[4][0]-range < x and x < target[4][0]+range:
        if z < tickness/2.:
            return (x+1.5, y, z-1.5)
    elif target[5][0]-range < x and x < target[5][0]+range:
        if z < tickness/2.:
            return (x+2.2, y, z-1.6)
        else:
            return (x, y, z-0.5)
    elif target[6][0]-range < x and x < target[6][0]+range:
        if z < tickness/2.:
            return (x+1.5, y, z-1.5)
    else:
        if z < tickness/2.:
            return (x, y, z-1.5)
    return None

if __name__ == "__main__":
    main()