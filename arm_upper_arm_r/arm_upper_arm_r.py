import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    
    spec = Const.UpperArm.spec
    upper_arm = sw.create_from_spec(spec)

    rib_tip_end = upper_arm.ribs[-1]
    rib_tip_end.edges = list(map(lambda t: deform_rib_tip_end(t[0], t[1]), rib_tip_end.edges))
    rib_tip_end.position = 1. - 0.5/spec.l

    rib_tip_end_scaled_edges = edges_util.scale(rib_tip_end.edges, 0.8)
    upper_arm.add_rib(1., rib_tip_end_scaled_edges)

    sw.chamfering(upper_arm, 0.5)

    sw.generate_stl_binary(path, fname, divided=False)

def deform_rib_tip_end(x,y):
    if y < 0:
        return (x, y+2.5)
    return (x, y-1.5)

if __name__ == "__main__":
    main()