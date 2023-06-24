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

    ht = Const.Thumb.Proximal.width/2
    length = Const.Thumb.Proximal.length

    base_1 = sw.move_y(1.2/8)
    base_2 = sw.parent(base_1).rotate(np.pi).void(Const.Thumb.Proximal.wrap_offset)

    obj = sw.rotate(-np.pi).parent(base_2).void(length)
    obj.add_rib(0., [(ht,0.5), (-ht,0.5), (-ht,-0.5), (ht,-0.5)])
    obj.add_rib(0.1, [(ht,1.2), (-ht,1.2), (-ht,-1.2), (ht,-1.2)])
    obj.add_rib(1.-1.2/length, [(ht,1.2), (-ht,1.2), (-ht,-1.2), (ht,-1.2)])
    obj.add_rib(1., [(ht,0.9), (-ht,0.9), (-ht,0.1), (ht,0.1)])

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()