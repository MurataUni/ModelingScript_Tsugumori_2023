import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from path_info import Const as PathInfo

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from arm_forearm_r import modeling_forearm

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    modeling_forearm(sw)
    sw.load_submodule(os.path.join(PathInfo.dir_parts_arm, "shield_r_normal"))
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()