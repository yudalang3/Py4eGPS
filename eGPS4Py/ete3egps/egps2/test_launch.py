import jpype
import jpype.imports
from jpype.types import *

from eGPS4Py.ete3egps.egps2.jvm_launcher import start_jvm,configure_jvm

FINAL_JAVA_CLASS = "api.rpython.TestJFrame"

def launch_me(string:str):
    # Start the JVM
    start_jvm()
    JDClass = jpype.JClass(FINAL_JAVA_CLASS)
    jd = JDClass()
    jd.test1(JString(string))
    # Stop the JVM; Not stop the JVM
    # jpype.shutdownJVM()


def test_get_picture(width:int, height:int):
    start_jvm()
    JDClass = jpype.JClass(FINAL_JAVA_CLASS)
    jd = JDClass()
    return jd.test_picture(width,height)


if __name__ == "__main__":
    configure_jvm("C:/Users/yudal/Documents/project/eGPS2/PythonAndJDK/microsoft-jdk-21.0.6-windows-x64/jdk-21.0.6+7/bin/server/jvm.dll",
                  "C:/Users/yudal/Documents/project/eGPS2/eGPS_v2_for_self_test/eGPS_lib/*");
    launch_me("Hello world")