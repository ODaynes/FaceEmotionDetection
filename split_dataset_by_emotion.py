# This script has been written to split the images in the
# Karolinska Directed Emotional Faces (KDEF) dataset into different
# folders, based on which emotion is in the picture.

import os
import shutil

for root, dirs, files in os.walk('media/KDEF'):
    for file in files:
        rel_path = os.path.join(root, file)

        emotion = ""

        expression_code = file[4:6]

        if expression_code == "AF":
            emotion = "afraid"
        elif expression_code == "AN":
            emotion = "angry"
        elif expression_code == "DI":
            emotion = "disgusted"
        elif expression_code == "HA":
            emotion = "happy"
        elif expression_code == "NE":
            emotion = "neutral"
        elif expression_code == "SA":
            emotion = "sad"
        elif expression_code == "SU":
            emotion = "surprised"

        print("%s - %s" % (rel_path, emotion))

        shutil.copy2(os.path.abspath(rel_path), "media/KDEF_sorted/" + emotion + "/")
