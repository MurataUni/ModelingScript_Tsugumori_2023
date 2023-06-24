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
    sw.parent(sw.move_z_back(Const.Wrist.wrap_offset))\
        .pole(Const.Wrist.length, Const.Wrist.radius, 2*np.pi, Const.Wrist.divid, True)

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()