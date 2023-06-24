import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_hand import Const
from path_info import Const as PathInfo

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from hand_r import modeling_hand

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    posture_file = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_hand_r_grasp)

    sw = Shipwright(Dock())
    modeling_hand(sw, posture_file, [PathInfo.dir_parts_hand])
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()