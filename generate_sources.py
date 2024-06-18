# ******************************************************************************************
# **  Copyright  2024             Michał Radomski                                         **
# **  All Rights Reserved         Politechnika śląska                                     **
# **                                                                                      **
# ******************************************************************************************

import os
from typing import *

SOURCE_DIR = os.getcwd()
PY_SRC_DIR = SOURCE_DIR + "/src/filamux_ui"
PYPROTO_OUTPUT_DIR = PY_SRC_DIR + "/backend/protobuf"

for subdir, dirs, files in os.walk(os.fsencode(PY_SRC_DIR)):
    subdirPath = subdir.decode()
    for file in files:
        fileName = file.decode()
        if fileName.endswith(".ui"):
            outputFileName = fileName.replace(".ui", ".py")
            outputFileName = "ui_" + outputFileName
            print(f"Generating: {subdirPath}/{outputFileName}")
            ret = os.system(f"pyside6-uic \"{subdirPath}/{fileName}\" -o \"{subdirPath}/{outputFileName}\"")
            if ret != 0:
                exit(1)

PROTO_FILES: List[str] = []
for subdir, dirs, files in os.walk(os.fsencode(SOURCE_DIR + "/filamux-proto")):
    for file in files:
        fileName = file.decode()
        subdirPath = subdir.decode()
        if fileName.endswith(".proto"):
            PROTO_FILES.append(fileName)
os.chdir(SOURCE_DIR + "/filamux-proto/src")
ret = os.system(f'protoc --python_out={PYPROTO_OUTPUT_DIR} --pyi_out={PYPROTO_OUTPUT_DIR} {" ".join(PROTO_FILES)}')
if ret != 0:
    exit(1)
