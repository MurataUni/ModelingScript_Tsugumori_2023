import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from path_info import Const as PathInfo

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    path_panel_front = os.path.join(PathInfo.dir_parts_arm, 'shoulder_armor_r_panel_front')
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    sw.load_submodule(path_panel_front, force_load_merged_stl=True, vertex_matching=False)
    sw.deformation_all(lambda x,y,z: (-x,y,z))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()