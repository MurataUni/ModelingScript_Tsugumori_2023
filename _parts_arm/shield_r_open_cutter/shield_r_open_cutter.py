import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_arm import Const
from path_info import Const as PathInfo

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]+['shield_r_normal']))
from shield_r_normal import modeling_shield

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    modeling_shield(sw)
    side = sw.fetch_by_name('side')[0]

    gap_front = 3.
    gap_back = 1.5
    spec_shield_side = Const.Forearm.Shield.spec_side
    spec_cutter = Const.Forearm.Shield.Cutter.spec
    cutter_gap = (spec_shield_side.height() - gap_front - gap_back - spec_cutter.width())/2

    cutter_module_path = os.path.join(PathInfo.dir_parts_arm, 'cutter')

    sw.parent(sw.parent(side, 0.5).move_xy(x=-spec_shield_side.width(),y=-gap_front - spec_cutter.width()/2)).rotate(-np.pi/2)
    sw.parent(sw.void()).rotate(0., np.pi/2).load_submodule(cutter_module_path, force_load_merged_stl=True, vertex_matching=False)
    sw.parent(sw.parent(side, 0.5).move_xy(x=-spec_shield_side.width(),y=-gap_front - spec_cutter.width()/2 - cutter_gap)).rotate(-np.pi/2)
    sw.parent(sw.void()).rotate(0., np.pi/2).load_submodule(cutter_module_path, force_load_merged_stl=True, vertex_matching=False)
    sw.parent(sw.parent(side, 0.5).move_xy(x=-(spec_shield_side.width()-3.),y=-gap_front - spec_cutter.width()/2 - cutter_gap*2)).rotate(-np.pi/2)
    sw.parent(sw.void()).rotate(-np.pi/8, np.pi/2).load_submodule(cutter_module_path, force_load_merged_stl=True, vertex_matching=False)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
