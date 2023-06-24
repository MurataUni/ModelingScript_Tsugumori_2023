import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from spec_hand import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    palm_bottom_geta = sw.move_z_back(Const.Palm.Bottom.wrap_offset)
    palm_bottom = sw.parent(palm_bottom_geta).rectangular(Const.Palm.Bottom.width, Const.Palm.Bottom.height, Const.Palm.Bottom.length)

    palm = sw.rectangular(Const.Palm.Base.width, Const.Palm.Base.height, Const.Palm.Base.length)

    palm_outer = sw.parent(palm, 0.1/Const.Palm.Base.length).void(Const.Palm.Base.length)
    palm_outer.add_rib(0., [
        (Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height), 
        (-Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height), 
        (-Const.Palm.Outer.width/2, 0.), 
        (Const.Palm.Outer.width/2, 0.)
    ])
    palm_outer.add_rib(0.45, [
        (Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, 0.),
        (Const.Palm.Outer.width/2, 0.)
    ])
    palm_outer.add_rib(0.55, [
        (Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, -Const.Palm.Base.height/2+0.1),
        (Const.Palm.Outer.width/2, -Const.Palm.Base.height/2+0.1)
    ])
    palm_outer.add_rib(1., [
        (Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, Const.Palm.Base.height/2+Const.Palm.Outer.height),
        (-Const.Palm.Outer.width/2, -Const.Palm.Base.height/2+0.1),
        (Const.Palm.Outer.width/2, -Const.Palm.Base.height/2+0.1)
    ])

    for rib in palm_outer.ribs:
        rib.edges[1:1] = [
            (0.1, Const.Palm.Base.height/2+Const.Palm.Outer.height),
            (0., Const.Palm.Base.height/2+Const.Palm.Outer.height-0.1),
            (-0.1, Const.Palm.Base.height/2+Const.Palm.Outer.height)
        ]

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()