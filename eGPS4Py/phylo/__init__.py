"""
phylo模块 - 包含进化生物学相关工具

子模块:
- evoltree: 进化树相关功能
"""

import os
import json

try:
    from . import evoltree
except ImportError:
    pass

# 提供访问data.json的便捷方法
def load_data():
    """加载phylo模块的数据文件"""
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, 'data.json')

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"数据文件未找到: {data_path}")
    except json.JSONDecodeError:
        raise ValueError("数据文件格式错误")

__all__ = ["evoltree", "load_data"]