import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    path_hand_r = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1] + ['hand_r'])
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    sw.load_submodule(os.path.join(path_hand_r, "hand_r_open"), force_load_merged_stl=True, vertex_matching=False)
    sw.deformation_all(lambda x,y,z: (-x,y,z))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()