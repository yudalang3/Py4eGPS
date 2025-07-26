import jpype
import jpype.imports
from jpype.types import *
import json
from pathlib import Path

def get_jvm_configure():
    script_path = Path(__file__).resolve().parent
    file_path = script_path / 'data.json'
    with open(file_path, 'r') as f:
        loaded_data = json.load(f)
    return loaded_data['java_vm_path'], loaded_data['java_class_path']

def configure_jvm(java_class_path,java_vm_path):
    data = {'java_vm_path': java_vm_path, 'java_class_path': java_class_path}
    # save to the file
    with open('data.json', 'w') as f:
        json.dump(data, f)

def start_jvm():
    if jpype.isJVMStarted():
        return
    java_vm_path, java_class_path = get_jvm_configure()
    #jpype.startJVM(jvmpath=java_vm_path, classpath=[java_class_path])
    jpype.startJVM(
        java_vm_path,            # = jvmpath=...
        "-Xms256m",              # 初始堆 256 MB
        "-Xmx8g",                # 最大堆 2 GB
        "-Xss2m",                # 每线程栈 1 MB（默认 1 MB，示例演示）
        "-Dfile.encoding=UTF-8", # 还可加系统属性
        classpath=[java_class_path]  # 关键字参数必须写到位置参数之后
    )