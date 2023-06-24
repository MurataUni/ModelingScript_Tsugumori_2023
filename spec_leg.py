import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

thigh_bone_langth = 19.84

class Const:
    class CoxaJoint:
        spec = Spec(l=9., r_d=(6.4, 32)).set_pole_end_chamfer(length=1.,r=1.4)
        bone_length = spec.l/2
        spec_adapter = Spec(l=5., move_xyz=(0.,-3.,bone_length), list_rotation_yz=[(np.pi/2., -np.pi/2.)])
    class Thigh:
        bone_langth = thigh_bone_langth
    class KneeJoint:
        move_y = 1.
        spec = Spec(l=13.54)
        joint_radius = thigh_bone_langth - 14.37
    class Shin:
        move_y = -3.31
        spec = Spec(l=45.66)
    class Ankle:
        move_y = 2.
        spec = Spec(l=8.3)
    class ToeAdapter:
        move_y = 1.79
        spec = Spec(l=10.5)
    class Toe:
        spec = Spec(l=6.5)

    bone_length = {
        "leg_coxa_joint_r": CoxaJoint.bone_length,
        "leg_coxa_joint_l": CoxaJoint.bone_length,
        "leg_thigh_r": Thigh.bone_langth,
        "leg_thigh_l": Thigh.bone_langth,
        "leg_knee_joint_r": KneeJoint.spec.l,
        "leg_knee_joint_l": KneeJoint.spec.l,
        "leg_shin_r": Shin.spec.l,
        "leg_shin_l": Shin.spec.l,
        "leg_ankle_r": Ankle.spec.l,
        "leg_ankle_l": Ankle.spec.l,
        "leg_toe_adapter_r": ToeAdapter.spec.l,
        "leg_toe_adapter_l": ToeAdapter.spec.l,
        "leg_toe_r": Toe.spec.l,
        "leg_toe_l": Toe.spec.l,
    }

    bones = bone_length.keys()

    alias = {
        "leg_knee_joint_r": "leg_knee_joint",
        "leg_knee_joint_l": "leg_knee_joint",
        "leg_ankle_r": "leg_ankle",
        "leg_ankle_l": "leg_ankle",
        "leg_toe_adapter_r": "leg_toe_adapter",
        "leg_toe_adapter_l": "leg_toe_adapter",
        "leg_toe_r": "leg_toe",
        "leg_toe_l": "leg_toe",
    }

    bone_offset = {
        "leg_coxa_joint_r": {
            "x" : 12.,
            "y" : 1.,
            "z" : 10.,
        },
        "leg_coxa_joint_l": {
            "x" : -12.,
            "y" : 1.,
            "z" : 10.,
        },
        "leg_thigh_r": {
            "x" : 0.,
            "y" : CoxaJoint.spec_adapter.move_y()-CoxaJoint.spec_adapter.l+1.,
            "z" : 0.,
        },
        "leg_thigh_l": {
            "x" : 0.,
            "y" : CoxaJoint.spec_adapter.move_y()-CoxaJoint.spec_adapter.l+1.,
            "z" : 0.,
        },
        "leg_knee_joint_r": {
            "x" : 0.,
            "y" : KneeJoint.move_y,
            "z" : 0.,
        },
        "leg_knee_joint_l": {
            "x" : 0.,
            "y" : KneeJoint.move_y,
            "z" : 0.,
        },
        "leg_shin_r": {
            "x" : 0.,
            "y" : Shin.move_y,
            "z" : 0.,
        },
        "leg_shin_l": {
            "x" : 0.,
            "y" : Shin.move_y,
            "z" : 0.,
        },
        "leg_ankle_r": {
            "x" : 0.,
            "y" : -1.,
            "z" : 3.2,
        },
        "leg_ankle_l": {
            "x" : 0.,
            "y" : -1.,
            "z" : 3.2,
        },
        "leg_toe_adapter_r": {
            "x" : 0.,
            "y" : ToeAdapter.move_y,
            "z" : 0.,
        },
        "leg_toe_adapter_l": {
            "x" : 0.,
            "y" : ToeAdapter.move_y,
            "z" : 0.,
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
