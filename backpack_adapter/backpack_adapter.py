import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo
from spec_backpack import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    sw.parent(sw.move_x(-7.)).load_submodule(os.path.join(PathInfo.dir_parts_backpack, "adapter_single"))
    sw.parent(sw.move_x(7.)).load_submodule(os.path.join(PathInfo.dir_parts_backpack, "adapter_single"))

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()