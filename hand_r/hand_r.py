import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_hand import Const

def modeling_hand(sw: Shipwright, posture_file: str, modules_path:list):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    objects = sw.load_bones(pw)
    return sw.load_submodules_name_match(objects, modules_path, Const.alias)

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    sw.load_submodule(os.path.join(path, 'hand_r_grasp'), force_load_merged_stl=True, vertex_matching=False)
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()