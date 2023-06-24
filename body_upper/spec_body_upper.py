import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo

class Const:
    bone_length = {
        "base": 10.,
        "backpack_adapter_base": 10.,
        "upper_back_core": 10.,
        "upper_front": 10.,
    }

    bone_offset = {
        "backpack_adapter_base": {
            "x" : 0.,
            "y" : 3.,
            "z" : -9.,
        },
        "upper_back_core": {
            "x" : 0.,
            "y" : -18.,
            "z" : 20.,
        },
        "upper_front": {
            "x" : 0.,
            "y" : 0.,
            "z" : 14.5,
        },
    }

def main():
    fnames = [PathInfo.file_posture_body_upper, PathInfo.file_posture_body_upper_no_rotation]
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
