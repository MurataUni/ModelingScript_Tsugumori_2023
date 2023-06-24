import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_arm import Const

def modeling_shield(sw: Shipwright):
    spec_upper = Const.Forearm.Shield.spec_upper
    spec_side = Const.Forearm.Shield.spec_side

    upper = sw.create_from_spec(spec_upper, only_keel=True)
    upper.name = 'upper'
    edges_upper = [(0., 0.), (0., -9.), (-spec_upper.width(), -spec_upper.height()), (-spec_upper.width(), 0.)]
    upper.add_ribs(edges=edges_upper)

    side = sw.parent(upper).create_from_spec(spec_side, only_keel=True)
    side.name = 'side'
    edges_side_root = [(0., 0.), (0., -spec_side.height()), (-(spec_side.width()-4.), -spec_side.height()), (-spec_side.width(), -(spec_side.height()-10.)), (-spec_side.width(), 0.)]
    edges_side_tip = [(0., 0.), (0., -spec_side.height()+0.7), (-(spec_side.width()-6.), -spec_side.height()+0.7), (-spec_side.width()+2., -(spec_side.height()-10.)), (-spec_side.width()+2., 0.)]
    side.add_rib(0.,edges_side_root)
    side.add_rib(1.,edges_side_tip)

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    modeling_shield(sw)
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
