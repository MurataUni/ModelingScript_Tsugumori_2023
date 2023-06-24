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
        "tail_base": 10.,
        "tail_upper": 10.,
        "tail_lower": 10.,
    }

    bones = bone_length.keys()

    bone_offset = {
        "tail_base": {
            "x" : 0.,
            "y" : -19.5,
            "z" : 0.,
        },
        "tail_upper": {
            "x" : 0.,
            "y" : 6.5,
            "z" : 5.5,
        },
        "tail_lower": {
            "x" : 0.,
            "y" : 3,
            "z" : 10.5,
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
