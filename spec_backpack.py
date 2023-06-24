import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:
    class Adapter:
        bone_length = 22.5
    class BackpackOuter:
        bone_length = 10.
    class BackpackInner:
        slide_out_ratio = 0.
        slide_out_length = 60.
        slide_out_origin = -45.
        slide_out = slide_out_origin+slide_out_ratio*slide_out_length
        bone_length = 10.

    bone_length = {
        "backpack_adapter": Adapter.bone_length,
        "backpack_outer": BackpackOuter.bone_length,
        "backpack_inner": BackpackInner.bone_length,
    }

    bones = bone_length.keys()

    bone_offset = {
        "backpack_adapter": {
            "x" : 0.,
            "y" : -27.,
            "z" : 29.,
        },
        "backpack_outer": {
            "x" : 0.,
            "y" : 1.8,
            "z" : 0.,
        },
        "backpack_inner": {
            "x" : 0.,
            "y" : BackpackInner.slide_out,
            "z" : -bone_length["backpack_outer"]+5.,
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
