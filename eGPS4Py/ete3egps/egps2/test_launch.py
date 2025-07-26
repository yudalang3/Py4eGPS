import jpype
import jpype.imports
from jpype.types import *

from eGPS4Py.ete3egps.egps2.jvm_launcher import start_jvm

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
    launch_me()