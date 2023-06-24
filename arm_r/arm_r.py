import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo
from spec_arm import Const as Const, apply_const

def modeling_arm_r(sw:Shipwright, posture_file:str):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    objects = sw.load_bones(pw, root="arm_base_r")
    return sw.load_submodules_name_match(objects, [PathInfo.dir_parts], Const.alias)

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    posture = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_model_pose_1)
    
    sw = Shipwright(Dock())
    
    apply_const(posture)
    modeling_arm_r(sw, posture)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()

