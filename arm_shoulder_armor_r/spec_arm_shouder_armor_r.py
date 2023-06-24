import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper, BoneKeys
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const as SpecArm
from path_info import Const as PathInfo

class Const:
    panel_interval = 2.
    panel_vertical_offset=44.

    bone_length = {
        "inner_center": 10.,
        "inner_front": 10.,
        "inner_back": 10.,
        "outer_front": 10.,
        "outer_back": 10.,
        "base": SpecArm.ShoulderArmor.spec_adapter_root.length_without_overwrap()-SpecArm.ShoulderArmor.spec_armor_base.wrap_offset,
        "panel_base": 1.,
    }

    bone_offset = {
        "panel_base": {
            "x" : 0.,
            "y" : panel_vertical_offset+bone_length["panel_base"],
            "z" : 0.,
        },
        "inner_front": {
            "x" : panel_interval,
            "y" : 0.,
            "z" : 0.,
        },
        "inner_back": {
            "x" : -panel_interval,
            "y" : 0.,
            "z" : 0.,
        },
        "outer_front": {
            "x" : 2*panel_interval,
            "y" : 0.,
            "z" : 0.,
        },
        "outer_back": {
            "x" : -2*panel_interval,
            "y" : 0.,
            "z" : 0.,
        },
    }

    alias = {
        "inner_center": "shoulder_armor_panel_inner",
        "inner_front": "shoulder_armor_panel_inner",
        "inner_back": "shoulder_armor_panel_inner",
        "outer_front": "shoulder_armor_r_panel_front",
        "outer_back": "shoulder_armor_r_panel_back",
        "base": "shoulder_armor_r_base",
    }

    rotation_symmetory = {
        "inner_front": "inner_back",
        "outer_front": "outer_back",
    }

def main():
    fnames = [PathInfo.file_posture_shoulder_armor, PathInfo.file_posture_shoulder_armor_no_rotation]
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

def adjust_rotation(posture_file): #front to back
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())

    # decay rotation
    decay = 1/2
    decay_rotation = pw.fetch_bone_rotate_dict("outer_front")
    decay_rotation[BoneKeys.y] = decay_rotation[BoneKeys.y]*decay
    decay_rotation[BoneKeys.z] = decay_rotation[BoneKeys.z]*decay
    pw.set_rotation("inner_front", decay_rotation)

    # symmetrise rotation: front to back
    for key, target in Const.rotation_symmetory.items():
        if pw.has_key(key) and pw.has_key(target):
            rotation = pw.fetch_bone_rotate_dict(key)
            rotation[BoneKeys.y] = -rotation[BoneKeys.y]
            rotation[BoneKeys.z] = -rotation[BoneKeys.z]
            pw.set_rotation(target, rotation)
    
    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
