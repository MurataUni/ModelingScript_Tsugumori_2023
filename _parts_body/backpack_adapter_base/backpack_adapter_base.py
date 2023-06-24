import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from path_info import Const as PathInfo

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    backpack_base_l = sw.parent(sw.move_x(7.)).load_submodule(
        os.path.join(PathInfo.dir_parts_body, 'backpack_adapter_base_r'),
        vertex_matching=False)
    sw.deformation(backpack_base_l, lambda x,y,z: (-x,y,z))
    for triangle in backpack_base_l.monocoque_shell.triangles:
        triangle.inverse()
    
    backpack_base_r = sw.parent(sw.move_x(-7.)).load_submodule(
        os.path.join(PathInfo.dir_parts_body, 'backpack_adapter_base_r'),
        vertex_matching=False)

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()