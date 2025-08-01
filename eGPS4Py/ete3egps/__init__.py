# #START_LICENSE###########################################################
#
#
# This file is part of the Environment for Tree Exploration program
# (ETE).  http://etetoolkit.org
#
# ETE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ETE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ETE.  If not, see <http://www.gnu.org/licenses/>.
#
#
#                     ABOUT THE ETE PACKAGE
#                     =====================
#
# ETE is distributed under the GPL copyleft license (2008-2015).
#
# If you make use of ETE in published work, please cite:
#
# Jaime Huerta-Cepas, Joaquin Dopazo and Toni Gabaldon.
# ETE: a python Environment for Tree Exploration. Jaime BMC
# Bioinformatics 2010,:24doi:10.1186/1471-2105-11-24
#
# Note that extra references to the specific methods implemented in
# the toolkit may be available in the documentation.
#
# More info at http://etetoolkit.org. Contact: huerta@embl.de
#
#
# #END_LICENSE#############################################################


# Note that the use of "from x import *" is safe here. Modules include
# the __all__ variable.

from warnings import warn

try:
    import numpy
except ImportError as e:
    numpy = None

from .coretype.tree import *
from .coretype.seqgroup import *
from .coretype.arraytable import *
from .ncbi_taxonomy import *
# from .phylo.phylotree import PhyloTree

# from .evol import EvolTree
# from .evol.evoltree import *
# from .phyloxml import Phyloxml, PhyloxmlTree
# from .nexml import Nexml, NexmlTree
# from .clustering.clustertree import *

try:
    from .phylomedb.phylomeDB3 import *
except ImportError as e:
    pass

