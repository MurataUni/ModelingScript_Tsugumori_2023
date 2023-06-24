import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

wrist_length = 2.
finger_height = 2.
finger_width = 1.7
thumb_width = 2.
finger_side_gap = 0.1
palm_base_width = (finger_width-0.3)*4+finger_side_gap*5

class Const:
    class Wrist:
        length = wrist_length
        radius = 1.5
        divid = 6
        wrap_offset = 1.
    class Palm:
        class Bottom:
            height = 3.
            width = 4.
            length = 4.
            wrap_offset = wrist_length*0.1
        class Base:
            height = finger_height
            width = palm_base_width
            length = 10.
        class Outer:
            height = 0.6
            width = palm_base_width + 0.8
    class Thumb:
        class Proximal:
            length = 5.6
            width = thumb_width
            wrap_offset = 1.
        class Middle:
            length = 5.5
            length_outer = 3.
            outer_width = thumb_width - 0.2
            inner_width = outer_width - 0.2
            wrap_offset = 1.
    class Finger:
        width = finger_width
        side_gap = finger_side_gap
        class Proximal:
            length = 4.
            width = finger_width
            wrap_offset = length/10.
        class Middle:
            length = 6.
            length_outer = 4.
            outer_width = finger_width
            inner_width = outer_width - 0.2
            wrap_offset = length/10.
        class Distal:
            length = 4.
            width = finger_width
            wrap_offset = length/8.

    bone_length = {
        "wrist": Wrist.length-Wrist.wrap_offset,
        "palm": Palm.Base.length,
        "thumb_proximal_phalanx": Thumb.Proximal.length-Thumb.Proximal.wrap_offset,
        "thumb_middle_phalanx": Thumb.Middle.length-Thumb.Middle.wrap_offset,
        "thumb_distal_phalanx": Finger.Distal.length-Finger.Distal.wrap_offset,
        "index_f_proximal_phalanx": Finger.Proximal.length-Finger.Proximal.wrap_offset,
        "index_f_middle_phalanx": Finger.Middle.length-Finger.Middle.wrap_offset,
        "index_f_distal_phalanx": Finger.Distal.length-Finger.Distal.wrap_offset,
        "middle_f_proximal_phalanx": Finger.Proximal.length-Finger.Proximal.wrap_offset,
        "middle_f_middle_phalanx": Finger.Middle.length-Finger.Middle.wrap_offset,
        "middle_f_distal_phalanx": Finger.Distal.length-Finger.Distal.wrap_offset,
        "ring_f_proximal_phalanx": Finger.Proximal.length-Finger.Proximal.wrap_offset,
        "ring_f_middle_phalanx": Finger.Middle.length-Finger.Middle.wrap_offset,
        "ring_f_distal_phalanx": Finger.Distal.length-Finger.Distal.wrap_offset,
        "little_f_proximal_phalanx": Finger.Proximal.length-Finger.Proximal.wrap_offset,
        "little_f_middle_phalanx": Finger.Middle.length-Finger.Middle.wrap_offset,
        "little_f_distal_phalanx": Finger.Distal.length-Finger.Distal.wrap_offset,
    }

    bones = bone_length.keys()

    bone_offset = {
        "thumb_proximal_phalanx": {
            "x" : 3.5,
            "y" : -0.75,
            "z" : -7.5
        },
        "index_f_proximal_phalanx": {
            "x" : Finger.side_gap*1.5+Finger.width*1.5,
            "y" : 0.,
            "z" : 0.
        },
        "middle_f_proximal_phalanx": {
            "x" : Finger.side_gap*0.5+Finger.width*0.5,
            "y" : 0.,
            "z" : 0.
        },
        "ring_f_proximal_phalanx": {
            "x" : -(Finger.side_gap*0.5+Finger.width*0.5),
            "y" : 0.,
            "z" : 0.
        },
        "little_f_proximal_phalanx": {
            "x" : -(Finger.side_gap*1.5+Finger.width*1.5),
            "y" : 0.,
            "z" : 0.
        }
    }

    alias = {
        "thumb_distal_phalanx": "finger_distal_phalanx",
        "index_f_proximal_phalanx": "finger_proximal_phalanx",
        "index_f_middle_phalanx": "finger_middle_phalanx",
        "index_f_distal_phalanx": "finger_distal_phalanx",
        "middle_f_proximal_phalanx": "finger_proximal_phalanx",
        "middle_f_middle_phalanx": "finger_middle_phalanx",
        "middle_f_distal_phalanx": "finger_distal_phalanx",
        "ring_f_proximal_phalanx": "finger_proximal_phalanx",
        "ring_f_middle_phalanx": "finger_middle_phalanx",
        "ring_f_distal_phalanx": "finger_distal_phalanx",
        "little_f_proximal_phalanx": "finger_proximal_phalanx",
        "little_f_middle_phalanx": "finger_middle_phalanx",
        "little_f_distal_phalanx": "finger_distal_phalanx",
    }
    

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_posture')
    fnames = PathInfo.files_posture_hand
    for fname in fnames:
        apply_const(os.path.join(path,fname))

def apply_const(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bone_length.keys():
        if pw.has_key(key):
            pw.set_length(key, Const.bone_length[key])
    
    for key in Const.bone_offset.keys():
        if pw.has_key(key):
            pw.set_offset_dict_on_bone_axis(key, Const.bone_offset[key])

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
