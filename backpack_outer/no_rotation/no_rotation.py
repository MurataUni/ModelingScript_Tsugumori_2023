import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from path_info import Const as PathInfo

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_backpack_outer import apply_const
from backpack_outer import modeling_backpack_outer

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    posture = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_backpack_outer_no_rotation)
    
    sw = Shipwright(Dock())
    apply_const(posture)
    modeling_backpack_outer(sw, os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_backpack_outer_no_rotation))
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
    