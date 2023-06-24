import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'
    
    sw = Shipwright(Dock())
    
    spec_adapter_root = Const.Shoulder.spec_adapter_root
    spec_outer = Const.Shoulder.spec_outer
    spec_inner = Const.Shoulder.spec_inner
    spec_adapter_tip = Const.Shoulder.spec_adapter_tip

    adapter_root = sw.create_from_spec(spec_adapter_root)

    outer = sw.parent(adapter_root).create_from_spec(spec_outer, only_keel=True)
    edges_outer = sw.rib_edges_circular(spec_outer.radius(), np.pi, spec_outer.divid(), True)
    edges_outer.insert(0, (4., -4))
    edges_outer.append((-4, -4.))
    outer.add_rib(0.5/5., edges_outer.copy())
    outer.add_rib(1.0-0.5/5., edges_outer.copy())
    outer.add_rib(0., edges_util.scale(edges_outer, 0.95))
    outer.add_rib(1., edges_util.scale(edges_outer, 0.95))

    inner = sw.parent(outer, 1./spec_outer.l).create_from_spec(spec_inner, only_keel=True)
    edges_inner = [(4.5, 0.), (-4.5, 0.), (-5., -4+0.4), (5., -4+0.4)]
    inner.add_rib(0., edges_inner.copy())
    inner.add_rib(1., edges_inner.copy())

    adapter_tip = sw.parent(outer, 1.-(spec_outer.length_without_overwrap()/2 + 1.)/spec_outer.l).create_from_spec(spec_adapter_tip)

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()