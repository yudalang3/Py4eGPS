import jpype
import jpype.imports
import json
from pathlib import Path
import os
def configure_jvm(java_vm_path,java_class_path):
    """
    Configure JVM paths and save to user directory to avoid permission issues.
    
    Args:
        java_vm_path (str): Path to Java VM library
        java_class_path (str): Path to Java class files
    """
    data = {'java_vm_path': java_vm_path, 'java_class_path': java_class_path}
    # Save configuration to user home directory to avoid permission issues
    config_dir = Path.home() / '.eGPS4Py'
    config_dir.mkdir(exist_ok=True)
    config_file = config_dir / 'jvm_config.json'
    with open(config_file, 'w') as f:
        json.dump(data, f)

def get_user_jvm_configure():
    """
    Get user-specific JVM configuration from home directory.
    
    Returns:
        tuple: A tuple containing (java_vm_path, java_class_path)
        
    Raises:
        FileNotFoundError: If user configuration file does not exist
    """
    # Read configuration from user directory
    config_file = Path.home() / '.eGPS4Py' / 'jvm_config.json'
    if config_file.exists():
        with open(config_file, 'r') as f:
            loaded_data = json.load(f)
        return loaded_data['java_vm_path'], loaded_data['java_class_path']
    else:
        # If user configuration does not exist, raise exception
        raise FileNotFoundError("JVM configuration not found. Please call configure_jvm() first.")

def start_jvm():
    """
    Start JVM with configured paths. 
    User must configure JVM paths first using configure_jvm().
    
    Raises:
        FileNotFoundError: If no JVM configuration is found
    """
    if jpype.isJVMStarted():
        return
    try:
        # Get user configuration
        java_vm_path, java_class_path = get_user_jvm_configure()
    except FileNotFoundError:
        # If user configuration does not exist, raise exception
        raise FileNotFoundError("JVM configuration not found. Please call configure_jvm() first.")
    
    jpype.startJVM(
        java_vm_path,            # JVM path
        "-Xms256m",              # Initial heap size 256 MB
        "-Xmx8g",                # Maximum heap size 8 GB
        "-Xss2m",                # Stack size per thread 2 MB
        "-Dfile.encoding=UTF-8", # Set file encoding to UTF-8
        classpath=[java_class_path]  # Java classpath must be specified as keyword argument
    )
