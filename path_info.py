import sys
sys.dont_write_bytecode = True

import os

class Const:
    dir_posture_json = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_posture'])

    dir_parts_arm = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_arm'])
    dir_parts_leg = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_leg'])
    dir_parts_body = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_body'])
    dir_parts_backpack = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_backpack'])
    dir_parts_hand = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_hand'])
    dir_parts = os.path.dirname(os.path.abspath(__file__))
    
    folder_divided = 'divided'

    file_posture_shoulder_armor = 'static_parts_shoulder_armor.json'
    file_posture_shoulder_armor_no_rotation = 'static_parts_shoulder_armor_no_rotation.json'
    file_posture_backpack_outer = 'static_parts_backpack_outer.json'
    file_posture_backpack_outer_no_rotation = 'static_parts_backpack_outer_no_rotation.json'
    file_posture_body_upper = 'static_parts_body_upper.json'
    file_posture_body_upper_no_rotation = 'static_parts_body_upper_no_rotation.json'
    
    file_posture_hand_r_no_rotation = 'hand_no_rotation.json'
    file_posture_hand_r_grasp = 'hand_grasp.json'
    file_posture_hand_r_open = 'hand_open.json'
    file_posture_model_no_rotation = 'model_no_rotation.json'
    file_posture_model_pose_1 = 'model_pose_1.json'
    file_posture_model_pose_2 = 'model_pose_2.json'

    files_posture_hand = [file_posture_hand_r_no_rotation]
    files_posture_model = [file_posture_model_no_rotation, file_posture_model_pose_1]

def output_list():
    file_absdir = os.path.dirname(os.path.abspath(__file__))
    output = {
        "model": {
            "no_rotation": os.path.join(Const.dir_posture_json, Const.file_posture_model_no_rotation),
            "parts": os.path.join(file_absdir, '_modeling_no_rotation', Const.folder_divided),
            "pose_1": os.path.join(Const.dir_posture_json, Const.file_posture_model_pose_1),
        },
        "hand_r": {
            "no_rotation": os.path.join(Const.dir_posture_json, Const.file_posture_hand_r_no_rotation),
            "parts": os.path.join(file_absdir, 'hand_r', 'hand_r_no_rotation', Const.folder_divided),
            "hand_open": os.path.join(Const.dir_posture_json, Const.file_posture_hand_r_open),
            "hand_grasp": os.path.join(Const.dir_posture_json, Const.file_posture_hand_r_grasp),
        },
        "shoulder_armor_r(staic)": {
            "no_rotation": os.path.join(Const.dir_posture_json, Const.file_posture_shoulder_armor_no_rotation),
            "parts": os.path.join(file_absdir, 'arm_shoulder_armor_r', 'no_rotation', Const.folder_divided),
            "assembled": os.path.join(Const.dir_posture_json, Const.file_posture_shoulder_armor),
        },
        "backpack_outer(staic)": {
            "no_rotation": os.path.join(Const.dir_posture_json, Const.file_posture_backpack_outer_no_rotation),
            "parts": os.path.join(file_absdir, 'backpack_outer', 'no_rotation', Const.folder_divided),
            "assembled": os.path.join(Const.dir_posture_json, Const.file_posture_backpack_outer),
        },
        "body_upper(staic)": {
            "no_rotation": os.path.join(Const.dir_posture_json, Const.file_posture_body_upper_no_rotation),
            "parts": os.path.join(file_absdir, 'body_upper', 'no_rotation', Const.folder_divided),
            "assembled": os.path.join(Const.dir_posture_json, Const.file_posture_body_upper),
        },
    }
    file_full_name =  os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'path_list.txt'])
    f = open(file_full_name, "w", encoding="ascii")
    for name, path_dict in output.items():
        f.write("[" + name + "]\n")
        max_path_name = len(max(path_dict.keys(), key=len))
        for path_name, path_value in path_dict.items():
            f.write(path_name.ljust(max_path_name, ' ') + ": " + path_value + "\n")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    output_list()
