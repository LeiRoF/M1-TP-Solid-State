#!/usr/bin/python3
# [20220421-1108]

import pymatgen.core as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib.pyplot as plt

def print_bands (bs):
	for kpoint, band in zip (bs.kpoints, bs.bands [Spin.up]):
		kx = kpoint.frac_coords [0]
		ky = kpoint.frac_coords [1]
		kz = kpoint.frac_coords [2]
		for energy in band:
			print ("k = [{:+.3f} {:+.3f} {:+.3f}]    E(k) = {:+.6e}".format (kx, ky, kz, energy))

run = BSVasprun ("./vasprun.xml", parse_projected_eigen = True)
bs = run.get_band_structure ("KPOINTS")

print ("number of bands:", bs.nb_bands)
print ("number of k-points:", len (bs.kpoints))
print ("is metal:", bs.is_metal ())
print ("is spin polarized:", bs.is_spin_polarized)
print ("Fermi energy:", bs.efermi)

print ("band gap: {}".format (bs.get_band_gap ()))

#print (bs.bands)
#print (bs.bands [Spin.up])
#print_bands (bs)

bsplot = BSPlotter (bs)
bsplot.get_plot (ylim = (-20, 20), zero_to_efermi = True)
ax = plt.gca ()
ax.set_title ("Diamond band structure", fontsize = 18)
#xlim = ax.get_xlim ()
#ax.hlines (0, xlim [0], xlim [1], linestyles = "dashed", color = "black")
ax.plot (label = "spin up")
bsplot.show ()


