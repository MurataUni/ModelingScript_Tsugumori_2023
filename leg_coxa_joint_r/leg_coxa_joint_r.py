import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_leg import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    coxa_joint = sw.create_from_spec(Const.CoxaJoint.spec)

    adapter_edges_start = [(2.,6.),(-2.,6.),(-2.,-6.),(2.,-6.)]
    adapter_edges_end = [(2.,4.6),(-2.,4.6),(-2.,-4.6),(2.,-4.6)]
    coxa_joint_adapter = sw.create_from_spec(spec=Const.CoxaJoint.spec_adapter, only_keel=True)
    coxa_joint_adapter.add_rib(0., adapter_edges_start)
    coxa_joint_adapter.add_rib(1., adapter_edges_end)
    
    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()