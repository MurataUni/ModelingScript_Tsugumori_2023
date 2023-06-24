import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:
    class Forearm:
        spec = Spec(l=30., h_w=(7.,6.), wrap_offset=3.)
        class Shield:
            spec_upper = Spec(l=1., h_w=(22.5,9.)).set_move_xyz(x=4.,y=4.,z=0.5)\
                .add_rotation_x(-np.pi/2)
            spec_side = Spec(l=2., h_w=(40.,13.)).set_move_xyz(x=-8.,y=8.)\
                .add_list_rotation_yz([(-np.pi/2,0.)])
            class Cutter:
                spec = Spec(l=14., h_w=(1.1,8.), wrap_offset=3.)
    class Elbow:
        spec = Spec(l=8., h_w=(4.5,3.), wrap_offset=3.).set_rect_end_chamfered_ratio(length=2.,h_ratio=0.75)
    class UpperArm:
        spec = Spec(l=20., h_w=(9.,7.), wrap_offset=0.).set_rect_tip_end_chamfered_ratio(length=5.)
    class Shoulder:
        spec_adapter_root = Spec(l=5., r_d=(2.5, 8), wrap_offset=2.)
        spec_outer = Spec(l=6., r_d=(5., 16), wrap_offset=1.)
        spec_inner = Spec(l=4.)
        length_bone = spec_adapter_root.length_without_overwrap()+spec_outer.length_without_overwrap()/2-1.
        spec_adapter_tip = Spec(l=2., r_d=(2., 8), move_xyz=(0.,-(4.-0.5),0.), list_rotation_yz=[(np.pi/2, -np.pi/2)])
    class ShoulderArmor:
        spec_adapter_root = Spec(l=10., r_d=(2.5,8), wrap_offset=5.)
        spec_adapter_base = Spec(l=5., wrap_offset=4.5)
        spec_armor_base = Spec(l=5., wrap_offset=4.)
        spec_armor_core = Spec(l=34.).set_move_xyz(0.,8.,0.).add_rotation_x(-np.pi/2).add_list_rotation_yz([(0.,np.pi)])
        spec_armor_panel_inner = Spec(l=1.).set_move_xyz(x=-0.5).add_list_rotation_yz([(np.pi/2,0.)])
        spec_armor_panel_front = Spec(l=3.).add_list_rotation_yz([(np.pi/2,0.)])
        length_bone = spec_adapter_root.length_without_overwrap()+spec_armor_base.length_without_overwrap()
    class Base:
        spec = Spec(l=5.5)

    bone_length = {
        "hand_r": 5.,
        "hand_l": 5.,
        "arm_forearm_r": Forearm.spec.length_without_overwrap(),
        "arm_forearm_l": Forearm.spec.length_without_overwrap(),
        "arm_elbow_r": Elbow.spec.length_without_overwrap(),
        "arm_elbow_l": Elbow.spec.length_without_overwrap(),
        "arm_upper_arm_r": UpperArm.spec.length_without_overwrap(),
        "arm_upper_arm_l": UpperArm.spec.length_without_overwrap(),
        "arm_shoulder_r": Shoulder.length_bone,
        "arm_shoulder_l": Shoulder.length_bone,
        "arm_shoulder_armor_r": ShoulderArmor.length_bone,
        "arm_shoulder_armor_l": ShoulderArmor.length_bone,
        "arm_base_r": Base.spec.l,
        "arm_base_l": Base.spec.l
    }

    bones = bone_length.keys()

    bone_offset = {
        "arm_upper_arm_r": {
            "x" : Shoulder.spec_adapter_tip.move_x(),
            "y" : Shoulder.spec_adapter_tip.move_y()-1.,
            "z" : Shoulder.spec_adapter_tip.move_z()
        },
        "arm_upper_arm_l": {
            "x" : -Shoulder.spec_adapter_tip.move_x(),
            "y" : Shoulder.spec_adapter_tip.move_y()-1.,
            "z" : Shoulder.spec_adapter_tip.move_z()
        },
        "weapon_r": {
            "x" : 0,
            "y" : -0.2,
            "z" : 0
        },
        "arm_base_r": {
            "x" : 11.5,
            "y" : -8.,
            "z" : 17.
        },
        "arm_base_l": {
            "x" : -11.5,
            "y" : -8.,
            "z" : 17.
        },
    }

    alias = {
        "arm_elbow_r": "arm_elbow",
        "arm_elbow_l": "arm_elbow",
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
