import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

from harbor3d.util import edges_util
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_arm import Const
from path_info import Const as PathInfo

def modeling_forearm(sw: Shipwright):
    spec = Const.Forearm.spec
    forearm = sw.create_from_spec(spec, only_keel=True)

    edges = [(spec.width()/2, spec.height()/2), (-spec.width()/2, spec.height()/2), (-spec.width()/2, -spec.height()/2), (spec.width()/2, -spec.height()/2)]

    edge_beginning = edges.copy()
    edge_beginning[0] = (edge_beginning[0][0], edge_beginning[0][1] - 1.5)
    edge_beginning[1] = (edge_beginning[1][0], edge_beginning[1][1] - 1.5)
    scaled_edges_beginning = edges_util.scale(edge_beginning, 0.8)
    center_edges_beginning = edges_util.center(edge_beginning)
    center_scaled_edges_beginning = edges_util.center(scaled_edges_beginning)
    y_translate = center_edges_beginning[1]-center_scaled_edges_beginning[1]
    edges_util.translate(scaled_edges_beginning, y=y_translate)
    mid_edges_1 = edges.copy()
    mid_edges_1[0] = (mid_edges_1[0][0] - 1.5, mid_edges_1[0][1])
    mid_edges_1[3] = (mid_edges_1[3][0] - 1.5, mid_edges_1[3][1])

    forearm.add_rib(0., scaled_edges_beginning)
    forearm.add_rib(0.5/spec.l, edge_beginning)
    forearm.add_rib(3./spec.l, edges.copy())
    forearm.add_rib(11./spec.l, edges.copy())
    forearm.add_rib(13./spec.l, mid_edges_1)
    forearm.add_rib(24./spec.l, mid_edges_1.copy())
    forearm.add_rib(26./spec.l, edges.copy())
    forearm.add_rib((spec.l - 1.)/spec.l, edges.copy())
    forearm.add_rib(1., edges_util.scale(edges, 0.8))

    forearm.order_ribs()
    sw.chamfering(forearm, 0.5)

    return forearm

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    sw.load_submodule(os.path.join(path, 'forearm_r_normal'), force_load_merged_stl=True, vertex_matching=False)
    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()