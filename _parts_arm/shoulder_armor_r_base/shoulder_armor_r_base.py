import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_arm import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    
    spec_adapter_root = Const.ShoulderArmor.spec_adapter_root
    spec_adapter_base = Const.ShoulderArmor.spec_adapter_base
    spec_armor_base = Const.ShoulderArmor.spec_armor_base
    spec_armor_core = Const.ShoulderArmor.spec_armor_core

    adapter_root = sw.create_from_spec(spec_adapter_root)

    adapter_base = sw.parent(adapter_root).create_from_spec(spec_adapter_base, only_keel=True)
    adapter_base.add_rib(0., [(2.5, 3.), (-2.5, 3.), (-2.5, -3.), (2.5, -3.)])
    adapter_base.add_ribs([0.4, 1.], [(2.5, 5.), (-2.5, 5.), (-2.5, -5.), (2.5, -5.)])

    armor_base = sw.parent(adapter_root).create_from_spec(spec_armor_base, only_keel=True)
    armor_base_top = 8.
    armor_base_mid1 = 11.
    armor_base_mid2 = 15.
    armor_base_bottom = 13.
    armor_base_edges = \
        [(-armor_base_mid2/2., 2.5), (-armor_base_bottom/2., -2.5), (armor_base_bottom/2., -2.5), (armor_base_mid2/2., 2.5),(armor_base_mid1/2., 7.5), \
        (armor_base_top/2., 7.5), (armor_base_top/2., 11.5), (-armor_base_top/2., 11.5), (-armor_base_top/2., 7.5), (-armor_base_mid1/2., 7.5)]
    armor_base.add_ribs(edges=armor_base_edges)

    armor_core = sw.parent(armor_base,0.5).create_from_spec(spec_armor_core)
    core_x_long_bottom = 15.
    core_x_long_upper = core_x_long_bottom*(2/3)
    core_x_short_bottom = 4.5
    core_x_short_upper = core_x_short_bottom*(2/3)
    core_y_long = 9.
    core_y_short = 2.7
    edges_root = [(core_x_long_upper/2., core_y_long), (-core_x_long_upper/2., core_y_long), (-core_x_long_bottom/2., 0.), (core_x_long_bottom/2., 0.)]
    edges_tip = [(core_x_short_upper/2., core_y_short), (-core_x_short_upper/2., core_y_short), (-core_x_short_bottom/2., 0.), (core_x_short_bottom/2., 0.)]
    armor_core.add_rib(0.,edges_root)
    armor_core.add_rib(1.,edges_tip)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()