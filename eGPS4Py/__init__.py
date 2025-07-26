"""
eGPS4Py - A utility package for myutils and phylo functions

这个包提供了以下子模块:
- myutils: 包含sets等实用工具
- phylo: 包含evoltree等进化相关工具
"""

__version__ = "0.0.5"
__author__ = "Dalang Yu"
__email__ = "yudalang1994@outlook.com"

# 导入主要模块，方便用户使用
try:
    from . import myutils
    from . import phylo
except ImportError:
    # 在开发模式下可能会遇到导入问题，这里可以忽略
    pass

#导出 ete3相关的类
from .ete3egps.coretype.tree import *
from .ete3egps.coretype.seqgroup import *
from .ete3egps.coretype.arraytable import *
from .ete3egps.parser.newick import *

from .ete3egps.coretype.tree import *
from .ete3egps.coretype.seqgroup import *
from .ete3egps.coretype.arraytable import *
from .ete3egps.ncbi_taxonomy import ncbiquery
from .ete3egps.ncbi_taxonomy.ncbiquery import NCBITaxa
from .ete3egps.phylo.phylotree import *
from .ete3egps.clustering.clustertree import *

# from .evol import EvolTree
# from .evol.evoltree import *
# from .phyloxml import Phyloxml, PhyloxmlTree
# from .nexml import Nexml, NexmlTree
# 定义包的公共接口
__all__ = ["myutils", "phylo"]