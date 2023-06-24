import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_leg import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    foot_adapter_thickness = 4.
    foot_adapter_height = 7.2

    foot_adapter_edges = [\
        (-0.8*foot_adapter_height/2.,-foot_adapter_height/(2.*2.)),(-0.8*foot_adapter_height/2.,foot_adapter_height/(2.*2.)),\
        (0.,foot_adapter_height/2.),(Const.ToeAdapter.spec.l,foot_adapter_height/2.),\
        (Const.ToeAdapter.spec.l+0.8*foot_adapter_height/2.,foot_adapter_height/(2.*2.)),(Const.ToeAdapter.spec.l+0.8*foot_adapter_height/2.,-foot_adapter_height/(2.*2.)),\
        (Const.ToeAdapter.spec.l,-foot_adapter_height/2.),(0.,-foot_adapter_height/2.)]

    foot_adapter = sw.rotate(-np.pi/2.).void(foot_adapter_thickness)
    foot_adapter.add_ribs(edges=foot_adapter_edges)
    sw.deformation(foot_adapter, lambda x,y,z: (x,y,z-foot_adapter_thickness/2.))

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()