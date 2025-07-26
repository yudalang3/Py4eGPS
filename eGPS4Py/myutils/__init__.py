"""
myutils模块 - 包含各种实用工具函数

子模块:
- sets: 集合操作相关功能
"""

try:
    from . import sets
except ImportError:
    pass

__all__ = ["sets"]