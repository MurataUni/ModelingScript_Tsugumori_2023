import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright, Rib
import numpy as np
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from spec_weapon import Const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    fname = path.split(os.sep)[-1]+'.stl'

    sw = Shipwright(Dock())
    
    shaft = sw.create_from_spec(Const.Weapon.spec_shaft)
    shaft_rib = shaft.ribs[0]
    for i in range(1,Const.Weapon.spec_shaft.rib_divid):
        shaft.add_rib(1.-i/Const.Weapon.spec_shaft.rib_divid,shaft_rib.edges)
    for i in range(0,8):
        shaft.add_rib(1.-(Const.Weapon.spec_tip.wrap_offset*i/8)/Const.Weapon.spec_shaft.l,shaft_rib.edges)
    for i in range(1,8):
        shaft.add_rib(1.-(Const.Weapon.spec_tip.wrap_offset+3.*i/8)/Const.Weapon.spec_shaft.l,shaft_rib.edges)
    shaft.order_ribs()
    shaft.ribs.insert(0, Rib([(0.,0.)],0.))
    shaft.ribs.append(Rib([(0.,0.)], 1.))
    sw.deformation(shaft, shaft_deformation)

    tip = sw.parent(shaft).create_from_spec(Const.Weapon.spec_tip)
    tip.ribs.insert(0, Rib([(0.,0.)],0.))
    tip.ribs.append(Rib([(0.,0.)], 1.))
    sw.deformation(tip, tip_deformation)

    sw.generate_stl_binary(path, fname)

def shaft_deformation(x,y,z):
    deform_center = Const.Weapon.spec_shaft.l-Const.Weapon.spec_tip.wrap_offset
    deform_range_to_tip = Const.Weapon.spec_shaft.l-deform_center
    deform_range_to_root = 3.5
    epsilon = 0.001
    r_default = Const.Weapon.spec_shaft.radius()
    r_x = 3.5
    r_y = 2.5
    deformed = (x,y,z)

    if deform_center < z + epsilon:
        if epsilon < x or x < -epsilon:
            deformed = (deformed[0]*(r_x/r_default)*shaft_deform_decay_to_tip((z-deform_center)/deform_range_to_tip), deformed[1], deformed[2])
        if epsilon < y or y < -epsilon:
            deformed = (deformed[0], deformed[1]*(r_y/r_default)*shaft_deform_decay_to_tip((z-deform_center)/deform_range_to_tip), deformed[2])

    elif z < deform_center and deform_center-z < deform_range_to_root:
        if epsilon < x or x < -epsilon:
            deformed = (deformed[0]*(r_x/r_default)*shaft_deform_decay_to_root((deform_center-z)/deform_range_to_root), deformed[1], deformed[2])
        if epsilon < y or y < -epsilon:
            deformed = (deformed[0], deformed[1]*(r_y/r_default)*shaft_deform_decay_to_root((deform_center-z)/deform_range_to_root), deformed[2])
    return deformed
    
def shaft_deform_decay_to_tip(z_ratio):
    return np.sqrt(abs(1.2-z_ratio))

def shaft_deform_decay_to_root(z_ratio):
    return np.sqrt(abs(1.2-z_ratio))


def tip_deformation(x,y,z):
    length_center = Const.Weapon.spec_tip.l/2-Const.Weapon.spec_tip.wrap_offset
    epsilon = 0.01
    r = 2.8

    deformed = (x,y,z)
    if epsilon < x:
        if length_center < z:
            deformed = (x*1./r, deformed[1], deformed[2])
    elif x < -epsilon:
        if length_center < z:
            deformed = (x*1./r, deformed[1], deformed[2])
    
    if epsilon < y:
        if length_center < z:
            deformed = (deformed[0], y*0.6/r, deformed[2])
        else:
            deformed = (deformed[0], y*1.8/r, deformed[2])
    elif y < -epsilon:
        if length_center < z:
            deformed = (deformed[0], y*0.6/r, deformed[2])
        else:
            deformed = (deformed[0], y*1.8/r, deformed[2])
    
    if length_center < z:
        deformed = (deformed[0], deformed[1], z-np.sqrt(1.-abs(deformed[0]))/2)
    return deformed

if __name__ == "__main__":
    main()