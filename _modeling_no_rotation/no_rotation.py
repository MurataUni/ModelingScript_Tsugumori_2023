import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo
from spec_arm import Const as ArmConst, apply_const as apply_arm_const
from spec_leg import Const as LegConst, apply_const as apply_leg_const
from spec_backpack import apply_const as apply_backpack_const
from spec_tail import apply_const as apply_tail_const
from spec_body import Const as BodyConst, apply_const as apply_body_const
from spec_weapon import apply_const as apply_weapon_const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    posture = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_model_no_rotation)
    
    sw = Shipwright(Dock())
    apply_arm_const(posture)
    apply_leg_const(posture)
    apply_backpack_const(posture)
    apply_tail_const(posture)
    apply_body_const(posture)
    apply_weapon_const(posture)

    alias = ArmConst.alias | LegConst.alias | BodyConst.alias

    json_loader = JsonLoader(posture)
    pw = PostureWrapper(json_loader.fetch())
    objects = sw.load_bones(pw)
    sw.load_submodules_name_match(objects, [PathInfo.dir_parts], alias)

    sw.generate_stl_binary(path, fname="", concatinated=False)

if __name__ == "__main__":
    main()