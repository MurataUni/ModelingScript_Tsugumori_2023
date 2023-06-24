import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    path_upper_arm = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1] + ['leg_coxa_joint_r'])
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    sw.load_submodule(path_upper_arm, force_load_merged_stl=True, vertex_matching=False)
    sw.deformation_all(lambda x,y,z: (-x,y,z))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()
