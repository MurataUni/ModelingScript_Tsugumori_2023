import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import numpy as np
import os

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    ankle_thickness = 8.
    heel_thickness = 2.8

    ankle_inner_edges = [(-4.92,1.05),(-1.30,-2.09),(2.32,-2.09),(3.14,-0.69),(4.08,-0.69),(6.13,0.49),(6.13,2.76),(5.61,3.90),(5.85,5.20),(7.57,6.48),(7.57,9.15),(7.43,9.46),(2.84,11.64),(-2.50,11.64),(-6.63,6.91),(-6.89,4.55),(-5.75,3.20)]
    ankle_outer_edges = [(-4.57,1.75),(-0.97,-1.29),(2.08,-1.29),(2.86,-0.17),(4.08,-0.17),(5.67,0.80),(5.67,2.62),(4.66,3.90),(4.62,5.20),(7.04,6.68),(7.04,9.33),(7.12,9.41),(2.50,11.02),(-1.85,11.02),(-6.05,6.58),(-6.34,4.57),(-5.20,3.46)]
    heel_edges = [(1.93,10.16),(6.76,8.47),(6.76,19.99),(6.16,21.60),(5.35,21.56),(2.96,18.67),(4.68,18.67),(4.45,14.32)] 

    ankle_geta_1 = sw.rotate(0., -np.pi/2.).void()
    ankle_geta_2 = sw.parent(ankle_geta_1).rotate_x(np.pi/2.)

    ankle = sw.parent(ankle_geta_2).void(ankle_thickness)
    ankle.add_ribs(edges=ankle_outer_edges)
    ankle.add_ribs([0.6/ankle_thickness, 1-0.6/ankle_thickness], edges=ankle_inner_edges)
    sw.deformation(ankle, lambda x,y,z: (x,y,z-ankle_thickness/2.))

    heel = sw.parent(ankle_geta_2).void(heel_thickness)
    heel.add_ribs(edges=heel_edges)
    sw.deformation(heel, lambda x,y,z: (x,y,z-heel_thickness/2.))

    sw.generate_stl_binary(path, fname)

if __name__ == "__main__":
    main()
