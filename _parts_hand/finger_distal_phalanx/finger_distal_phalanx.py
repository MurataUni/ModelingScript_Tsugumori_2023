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

    ht = Const.Finger.Distal.width/2
    length = Const.Finger.Distal.length

    base = sw.rotate(-np.pi, 0.).void(Const.Finger.Distal.wrap_offset)
    obj = sw.rotate(np.pi, 0.).parent(base, 1.).void(length)
    obj.add_rib(0., [(ht,0.5), (-ht,0.5), (-ht,-0.5), (ht,-0.5)])
    obj.add_rib(0.15, [(ht,1.), (-ht,1.), (-ht,-1.), (ht,-1.)])
    obj.add_rib(0.3, [(ht,1.), (-ht,1.), (-ht,-1.), (ht,-1.)])
    obj.add_rib(1., [(0.,0.)])

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()