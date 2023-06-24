import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())

    spec = Const.Elbow.spec
    
    elbow = sw.create_from_spec(spec)
    
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()