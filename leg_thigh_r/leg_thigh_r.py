import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo
from spec_leg import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    thigh_thickness = 10.
    knee_joint_edges = (lambda r,y_o:\
        [(-r*np.sin((n/8)*np.pi/2.), y_o-r*np.cos((n/8)*np.pi/2.)) for n in range(8 + 1)])(Const.KneeJoint.joint_radius, Const.Thigh.bone_langth)
    thigh_edges = [(-3.25,0.00),(5.78,0.00),(10.48,2.44),(10.48,9.10),(4.04,14.04),(2.44,14.37)]\
        + knee_joint_edges\
        + [(-5.47,24.07),(-9.76,24.07),(-10.52,22.30),(-10.52,-10.30),(-6.63,-12.96),(-6.15,-3.07)]

    thigh_geta = sw.parent(sw.parent(sw.rotate(0., -np.pi/2.).void()).rotate_x(np.pi/2.)).void()
    thigh = sw.parent(thigh_geta).void(thigh_thickness)
    thigh.add_ribs(edges=thigh_edges)
    sw.deformation(thigh, lambda x,y,z: (x-Const.KneeJoint.move_y,y,z-thigh_thickness/2))

    sw.load_submodule(os.path.join(PathInfo.dir_parts_leg, "leg_cover_r"))

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()