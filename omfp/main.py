import OverlapMatrixFingerprint

from ase.io import read
import ase.units
import logging

# set log level to info.
# that waz
logging.basicConfig(level=logging.INFO, 
                format='%(message)s'    
            )

# positions in bohr
ethanol = read("Ethanol.xyz")

positions = ethanol.get_positions()
positions = positions / ase.units.Bohr
elements = ethanol.get_atomic_numbers()

omfpCalculator = OverlapMatrixFingerprint.OverlapMatrixFingerprint.stefansOMFP(s=1, p=1, width_cutoff=7.0)
omfp = omfpCalculator.fingerprint(positions, elements)

print(omfp)