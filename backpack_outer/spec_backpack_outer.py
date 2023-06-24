import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper, BoneKeys
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo

class Const:
    bone_length = {
        "backpack_base": 5.5,
        "backpack_outer": 10.,
        "backpack_canard": 10.,
        "backpack_thruster": 10.,
    }

    bone_offset = {
        "backpack_outer": {
            "x" : 0.,
            "y" : 3.5,
            "z" : 0.,
        },
        "backpack_canard": {
            "x" : 0.,
            "y" : 39.,
            "z" : -bone_length["backpack_outer"],
        },
        "backpack_thruster": {
            "x" : 0.,
            "y" : -49.,
            "z" : -bone_length["backpack_outer"]+2.,
        },
    }

def main():
    fnames = [PathInfo.file_posture_backpack_outer, PathInfo.file_posture_backpack_outer_no_rotation]
    for fname in fnames:
        apply_const(os.path.join(PathInfo.dir_posture_json,fname))

def apply_const(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bone_length.keys():
        if pw.has_key(key):
            pw.set_length(key, Const.bone_length[key])
    
    pw.remove_offset_all()
    for key in Const.bone_offset.keys():
        if pw.has_key(key):
            pw.set_offset_dict_on_bone_axis(key, Const.bone_offset[key])

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()