import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:
    class Weapon:
        spec_shaft = Spec(l=250.,r_d=(1.8,20),rib_divid=25,wrap_offset=130.)
        spec_tip = Spec(l=20.,r_d=(2.8,20),wrap_offset=4.)

    bone_length = {
        "weapon_r": Weapon.spec_shaft.length_without_overwrap()+Weapon.spec_tip.length_without_overwrap()
    }

    bones = bone_length.keys()

    bone_offset = {
        "weapon_r": {
            "x" : 0.,
            "y" : -2.,
            "z" : 3.,
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
