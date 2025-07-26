[English](README.md) | [简体中文](README.zh.md)

# eGPS4Py

eGPS4Py is a Python toolkit designed for processing and analyzing phylogenetic tree data. It combines the capabilities of Java and Python, leveraging JPype to call underlying Java APIs for executing complex evolutionary biology computations.

## Introduction

eGPS4Py is a Python toolkit aimed at simplifying the process of handling and analyzing phylogenetic tree data. This toolkit integrates the ease of use of Python with the powerful computational capabilities of Java, enabling researchers to efficiently process complex evolutionary biology problems.

Note: This Python package is still under continuous development. Since developers cannot anticipate all the specific requirements of various application scenarios, we have proposed a general framework. The examples in the documentation are only for guidance, and users can extend and customize according to their own needs.

## Key Features

- **Set Operations**: The [myutils.sets](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/myutils/sets.py) module provides common set operations such as intersection, union, and difference.
- **Phylogenetic Tree Analysis**: The [phylo.evoltree](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/phylo/evoltree.py) module supports parsing Newick format phylogenetic trees and can extract OTU (Operational Taxonomic Unit) and HTU (Hidden Taxonomic Unit) node names.
- **Java Virtual Machine Integration**: Built-in JVM support enables seamless interaction with Java code through the JPype1 library, facilitating calls to powerful Java bioinformatics libraries.
- **Based on ete3**: Improved based on the ete3 library, removing Python 2 compatibility layers and GUI visualization functions, focusing on core data processing capabilities.

## Project Structure

```
eGPS4Py/
├── myutils/                # Utility modules
│   ├── __init__.py
│   └── sets.py             # Set operation functions
├── phylo/                  # Phylogenetic tree analysis module
│   ├── __init__.py
│   ├── data.json           # JVM path configuration file
│   └── evoltree.py         # Core phylogenetic tree functions
├── tests/                  # Test code directory
│   └── __init__.py
├── __init__.py
```

## Installation

### Install from PyPI (Coming soon)

```bash
pip install eGPS4Py
```

### Install Local Development Version

```bash
git clone https://github.com/yourusername/eGPS4Py.git
cd eGPS4Py
pip install -e .
```

### Build Distribution Package

```bash
python setup.py bdist_wheel
```

## Usage

### `myutils.sets` Module

This module provides utility functions for set operations.

```python
from eGPS4Py.myutils import sets

# Example: Get the intersection of two sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = sets.get_intersection(set_a, set_b)
print(intersection)  # Output: {2, 3}
```

### `phylo.evoltree` Module

This module interacts with the Java backend and extracts node names from phylogenetic trees.

```python
from eGPS4Py.phylo import evoltree

# Get all OTU and HTU node names from a phylogenetic tree
tree_path = "path/to/your/tree.nwk"
names = evoltree.get_node_names(tree_path, get_otu=True, get_htu=True)
print(names)
```

#### Function Description

- `get_node_names(tree_path, target_htu=None, get_otu=False, get_htu=False)`
  - **Parameters**:
    - `tree_path`: Path to the Newick format phylogenetic tree file.
    - `target_htu`: Target HTU name (optional).
    - `get_otu`: Whether to get OTU (leaf nodes), boolean value.
    - `get_htu`: Whether to get HTU (internal nodes), boolean value.
  - **Returns**: A list of strings containing node names that meet the criteria.

## Development Guide

### Data File Management

[data.json](file:///C:/Users/yudal/PycharmProjects/eGPS4Py/eGPS4Py/phylo/data.json) stores JVM path information to ensure the Java Virtual Machine can be properly started in different environments:

```json
{
  "java_vm_path": "C:/Users/yudal/Documents/project/eGPS2/PythonAndJDK/microsoft-jdk-21.0.6-windows-x64/jdk-21.0.6+7/bin/server/jvm.dll",
  "java_class_path": "C:/Users/yudal/Documents/project/eGPS2/eGPS_v2_windows_openJDK21_64bit/eGPS_lib/*"
}
```

### Dependencies

Ensure you have installed the following dependencies:

- `jpype1`: For Java interaction.
- `numpy`: For numerical computing support.
- `biopython`: Optional, for handling biological sequence data.

You can install dependencies with:

```bash
pip install numpy jpype1 biopython
```

### Unit Tests

We recommend running unit tests before committing code to ensure stability:

```bash
python -m unittest discover
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature').
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## License

MIT License

Copyright (c) 2025 Dalang Yu

See [LICENSE](LICENSE) for more information.