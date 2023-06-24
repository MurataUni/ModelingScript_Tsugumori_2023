import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
from harbor3d.util import edges_util
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    neck_thickness = 4.
    neck_depth = 4.
    neck_joint_length = 6.
    neck_thickness_cham = 2.
    neck_depth_cham = 2.

    neck_edge = [(neck_depth/2, neck_thickness/2), (-neck_depth/2, neck_thickness/2), (-neck_depth/2, -neck_thickness/2), (neck_depth/2, -neck_thickness/2)]
    neck_edge_end = [\
        ((neck_depth-neck_depth_cham)/2, (neck_thickness-neck_thickness_cham)/2), \
        (-(neck_depth-neck_depth_cham)/2, (neck_thickness-neck_thickness_cham)/2), \
        (-(neck_depth-neck_depth_cham)/2, -(neck_thickness-neck_thickness_cham)/2), \
        ((neck_depth-neck_depth_cham)/2, -(neck_thickness-neck_thickness_cham)/2)]

    neck_joint_geta = sw.rotate(np.pi, np.pi/2).void(1.5)
    neck_joint = sw.rotate(np.pi, 0.).parent(neck_joint_geta).void(neck_joint_length)
    neck_joint.add_ribs([0., 1.], neck_edge_end)
    neck_joint.add_ribs([2./neck_joint_length, 1.-(2./neck_joint_length)], neck_edge)
    neck_joint.order_ribs()

    neck_cover_joint_geta = sw.rotate(np.pi/2).parent(neck_joint, 0.).void(0.)
    neck_cover_joint = sw.rotate(0.,np.pi/2)\
        .parent(neck_cover_joint_geta)\
        .load_submodule(os.path.join(PathInfo.dir_parts_body, 'neck_cover'))

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
