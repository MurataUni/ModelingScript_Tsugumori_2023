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

    ht_obj1 = Const.Thumb.Middle.inner_width/2
    length_obj1 = Const.Thumb.Middle.length

    base = sw.rotate(-np.pi).void(Const.Thumb.Middle.wrap_offset)
    obj1 = sw.rotate(np.pi).parent(base).void(length_obj1)
    obj1.add_rib(0., [(ht_obj1,0.25), (-ht_obj1,0.25), (-ht_obj1,-0.25), (ht_obj1,-0.25)])
    obj1.add_rib(0.25/length_obj1, [(ht_obj1,0.8), (-ht_obj1,0.8), (-ht_obj1,-0.8), (ht_obj1,-0.8)])
    obj1.add_rib(1.-0.25/length_obj1, [(ht_obj1,0.8), (-ht_obj1,0.8), (-ht_obj1,-0.8), (ht_obj1,-0.8)])
    obj1.add_rib(1., [(ht_obj1,0.25), (-ht_obj1,0.25), (-ht_obj1,-0.25), (ht_obj1,-0.25)])

    ht_obj2 = Const.Thumb.Middle.outer_width/2
    length_obj2 = Const.Thumb.Middle.length_outer

    base2 = sw.rotate(np.pi).parent(base).void((length_obj1 - length_obj2)/2.)
    obj2 = sw.rotate(0., 0.).parent(base2, 1.).void(length_obj2)
    obj2.add_rib(0., [(ht_obj2,0.9), (-ht_obj2,0.9), (-ht_obj2,0.1), (ht_obj2,0.1)])
    obj2.add_rib(0.9/length_obj2, [(ht_obj2,1.), (-ht_obj2,1.), (-ht_obj2,-1.), (ht_obj2,-1.)])
    obj2.add_rib(1.-0.7/length_obj2, [(ht_obj2,1.), (-ht_obj2,1.), (-ht_obj2,-1.), (ht_obj2,-1.)])
    obj2.add_rib(1., [(ht_obj2,0.9), (-ht_obj2,0.9), (-ht_obj2,0.1), (ht_obj2,0.1)])

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()