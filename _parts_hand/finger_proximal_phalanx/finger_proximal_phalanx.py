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

    ht_obj = Const.Finger.Proximal.width/2
    length_obj = Const.Finger.Proximal.length

    base = sw.rotate(np.pi).void(Const.Finger.Proximal.wrap_offset)

    obj = sw.rotate(-np.pi).parent(base).void(length_obj)
    obj.add_rib(0., [(ht_obj,0.5), (-ht_obj,0.5), (-ht_obj,-0.5), (ht_obj,-0.5)])
    obj.add_rib(0.1, [(ht_obj,1.), (-ht_obj,1.), (-ht_obj,-1.), (ht_obj,-1.)])
    obj.add_rib(1.-1.2/length_obj, [(ht_obj,1.), (-ht_obj,1.), (-ht_obj,-1.), (ht_obj,-1.)])
    obj.add_rib(1., [(ht_obj,0.9), (-ht_obj,0.9), (-ht_obj,0.1), (ht_obj,0.1)])

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()