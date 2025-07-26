import jpype
import jpype.imports
from jpype.types import *
import json
from pathlib import Path

from eGPS4Py.ete3egps.egps2.jvm_launcher import start_jvm

FINAL_JAVA_CLASS = "api.rpython.EvolTreeManipulator"

def get_node_names(tree_path, target_htu=None, get_otu=False, get_htu=False):
    # Start the JVM
    start_jvm()
    JDClass = jpype.JClass(FINAL_JAVA_CLASS)
    jd = JDClass()
    names = jd.getNodeNames(
        JString(tree_path),
        JString(target_htu) if target_htu is not None else None,
        JBoolean(get_otu),
        JBoolean(get_htu)
    )
    ret = [str(name) for name in names]
    # Stop the JVM; Not stop the JVM
    # jpype.shutdownJVM()

    return ret


# Example usage
if __name__ == "__main__":
    tree_path = r"/path/to/your_tree.nwk"
    try:
        names = get_node_names(tree_path, target_htu=None, get_otu=True, get_htu=True)
        print(names)
    except Exception as e:
        print("An error occurred:")
        print(e)
