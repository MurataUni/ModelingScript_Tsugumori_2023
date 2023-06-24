import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo

from spec_backpack_outer import apply_const

def modeling_backpack_outer(sw:Shipwright, posture_file:str):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    objects = sw.load_bones(pw)
    return sw.load_submodules_name_match(objects, [PathInfo.dir_parts_backpack])

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'
    posture = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_backpack_outer)

    sw = Shipwright(Dock())
    apply_const(posture)
    modeling_backpack_outer(sw, posture)
    
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
