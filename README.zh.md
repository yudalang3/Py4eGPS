[English](README.md) | [简体中文](README.zh.md)

# eGPS4Py

eGPS4Py 是一个基于 Python 的工具包，专为处理和分析进化树（phylogenetic tree）数据而设计。它结合了 Java 和 Python 的能力，通过 JPype 调用底层的 Java API 来执行复杂的演化生物学计算。

## 简介

eGPS4Py 是一个 Python 工具包，旨在简化进化树数据的处理和分析过程。该工具包整合了 Python 的易用性和 Java 的强大计算能力，使研究人员能够高效地处理复杂的进化生物学问题。

注意：此 Python 包仍在不断完善中。由于开发者无法预知所有具体应用场景的需求，我们提出了一个通用框架。文档中的示例仅作为引导，用户可以根据自己的需求进行扩展和定制。

## 主要特性

- **集合操作功能**：通过 [myutils.sets](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/myutils/sets.py) 模块提供常用的集合运算，如交集、并集、差集等。
- **进化树分析**：[phylo.evoltree](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/phylo/evoltree.py) 模块支持 Newick 格式进化树的解析，并能提取 OTU（操作分类单元）和 HTU（隐藏分类单元）节点名称。
- **Java 虚拟机集成**：内置 JVM 支持，通过 JPype1 库实现与 Java 代码的无缝交互，便于调用强大的 Java 生物信息学库。
- **基于 ete3**：以 ete3 库为基础进行改进，去除了 Python 2 兼容层和 GUI 可视化功能，专注于核心数据处理功能。

## 项目结构

```
eGPS4Py/
├── myutils/                # 实用工具模块
│   ├── __init__.py
│   └── sets.py             # 集合操作相关功能
├── phylo/                  # 进化树分析模块
│   ├── __init__.py
│   ├── data.json           # JVM路径配置文件
│   └── evoltree.py         # 进化树核心功能
├── tests/                  # 测试代码目录
│   └── __init__.py
├── __init__.py
```

## 安装

### 从 PyPI 安装 (即将推出)

```bash
pip install eGPS4Py
```

### 本地安装开发版本

```bash
git clone https://github.com/yourusername/eGPS4Py.git
cd eGPS4Py
pip install -e .
```

### 构建分发包

```bash
python setup.py bdist_wheel
```

## 使用方法

### `myutils.sets` 模块

该模块提供集合操作相关的实用函数。

```python
from eGPS4Py.myutils import sets

# 示例：获取两个集合的交集
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = sets.get_intersection(set_a, set_b)
print(intersection)  # 输出: {2, 3}
```

### `phylo.evoltree` 模块

该模块用于与 Java 后端交互并提取进化树中的节点名称。

```python
from eGPS4Py.phylo import evoltree

# 获取进化树中所有 OTU 和 HTU 节点名称
tree_path = "path/to/your/tree.nwk"
names = evoltree.get_node_names(tree_path, get_otu=True, get_htu=True)
print(names)
```

#### 函数说明

- `get_node_names(tree_path, target_htu=None, get_otu=False, get_htu=False)`
  - **参数**:
    - `tree_path`: Newick 格式的进化树文件路径。
    - `target_htu`: 目标 HTU 名称（可选）。
    - `get_otu`: 是否获取 OTU（叶节点），布尔值。
    - `get_htu`: 是否获取 HTU（内部节点），布尔值。
  - **返回**: 字符串列表，包含符合条件的节点名称。

## 开发指南

### 数据文件管理

[data.json](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/phylo/data.json) 存储了 JVM 的路径信息，确保在不同环境中可以正确启动 Java 虚拟机：

```json
{
  "java_vm_path": "C:/Users/yudal/Documents/project/eGPS2/PythonAndJDK/microsoft-jdk-21.0.6-windows-x64/jdk-21.0.6+7/bin/server/jvm.dll",
  "java_class_path": "C:/Users/yudal/Documents/project/eGPS2/eGPS_v2_windows_openJDK21_64bit/eGPS_lib/*"
}
```

### 依赖项

确保你已经安装了以下依赖：

- `jpype1`: 用于与 Java 交互。
- `numpy`: 数值计算支持。
- `biopython`: 可选，用于处理生物序列数据。

你可以使用以下命令安装依赖：

```bash
pip install numpy jpype1 biopython
```

### 单元测试

我们建议在提交代码前运行单元测试以确保稳定性：

```bash
python -m unittest discover
```

## 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库。
2. 创建一个新的分支 (`git checkout -b feature/your-feature`)。
3. 提交更改 (`git commit -am 'Add some feature')。
4. 推送至远程分支 (`git push origin feature/your-feature`)。
5. 创建 Pull Request。

## 许可证

MIT License

版权所有 (c) 2025 Dalang Yu

更多信息请查看 [LICENSE](LICENSE)。