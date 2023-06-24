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
    
    spec_armor_panel_front = Const.ShoulderArmor.spec_armor_panel_front
    armor_panel_front = sw.create_from_spec(spec_armor_panel_front)

    edges = [(0., 0.), (2., 12.), (9., 20.), (18., 18.), (21., 15.), (47., 8.), (50., 0.)]
    edges = edges_util.translate(edges, x=-(50.-1.))
    edges_scaled = edges_util.scale_xy(edges.copy(), scale_x=0.9, scale_y=0.8)
    edges_scaled = edges_util.translate(edges_scaled,x=-50.*0.1/2,y=21.*0.2/2*2/3)
    
    armor_panel_front.add_rib(0., edges)
    armor_panel_front.add_rib(1., edges_scaled)

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()
