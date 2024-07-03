import pylab as plt
from pprint import pprint
from blimpy import Waterfall
import matplotlib
# this might only be necessary on macos: run eg 'pip install PyQt5' first
matplotlib.use('qtagg')
obs = Waterfall('voyager_f1032192_t300_v2.fil')
obs.info()
# this the data printed by obs.info:
pprint(obs.header)
print(obs.data.shape)

my_dpi=200
# plot the entire power spectrum collected
plt.figure(figsize=(3456/my_dpi, 2234/my_dpi), dpi=my_dpi)
obs.plot_spectrum()
plt.xticks(rotation=-45, ha="left")
plt.title("full spectrum")
plt.savefig('spectrum.png')

plt.figure(figsize=(3456/my_dpi, 2234/my_dpi), dpi=my_dpi)
obs.plot_waterfall(f_start=8420.193, f_stop=8420.24, logged=True)
plt.title("waterfall")
plt.savefig('waterfall.png')

# plot a narrow area around frequency of interest
plt.figure(figsize=(8, 6))
plt.subplot(3,1,1)
plt.xticks(rotation=-45, ha="left")
obs.plot_spectrum(f_start=8420.193, f_stop=8420.195) # left sideband
plt.title("left sideband")
plt.subplot(3,1,2)
plt.xticks(rotation=-45, ha="left")
obs.plot_spectrum(f_start=8420.2163, f_stop=8420.2166) # carrier
plt.title("carrier")
plt.subplot(3,1,3)
plt.xticks(rotation=-45, ha="left")
obs.plot_spectrum(f_start=8420.238, f_stop=8420.24) # right sideband
plt.title("right sideband")
plt.tight_layout()
plt.savefig('bands.png')

# keep plots on screen until process is killed
plt.show()
