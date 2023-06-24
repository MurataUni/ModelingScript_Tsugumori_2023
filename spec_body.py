import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:

    bone_length = {
        "body_upper": 6.,
        "body_lower": 6.,
        "body_neck_1": 4.,
        "body_neck_2": 4.,
        "body_neck_3": 4.,
        "body_head": 5.,
    }

    bones = bone_length.keys()

    alias = {
        "body_neck_1": "body_neck",
        "body_neck_2": "body_neck",
        "body_neck_3": "body_neck",
    }

    bone_offset = {
        "body_neck_1": {
            "x" : 0.,
            "y" : -7.5,
            "z" : 21.5,
        },
        "body_head": {
            "x" : 0.,
            "y" : 0.,
            "z" : -1.5,
        },
    }

def main():
    fnames = PathInfo.files_posture_model
    for fname in fnames:
        apply_const(os.path.join(PathInfo.dir_posture_json,fname))

def apply_const(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bone_length.keys():
        if pw.has_key(key):
            pw.set_length(key, Const.bone_length[key])
    
    for key in Const.bones:
        if pw.has_key(key): pw.remove_offset(key)
    
    for key in Const.bone_offset.keys():
        if pw.has_key(key):
            pw.set_offset_dict_on_bone_axis(key, Const.bone_offset[key])

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
