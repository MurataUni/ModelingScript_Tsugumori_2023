import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_arm import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    
    spec_armor_panel_inner = Const.ShoulderArmor.spec_armor_panel_inner

    edges = [(0., 0.), (0., 7.), (-1., 11.), (2., 13.), (4., 10.), (32., 3.), (34., -3.), (2., -3.)]
    edges = edges_util.translate(edges, x=-34., y=3.)

    panel_inner = sw.create_from_spec(spec_armor_panel_inner)
    panel_inner.add_ribs(edges=edges)

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()
