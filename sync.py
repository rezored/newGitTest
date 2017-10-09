import os
import shutil

srcfile = 'E:/folder1'
destroot = "E:/folder2"

src_files = os.listdir(srcfile)
for file_name in src_files:
    full_file_name = os.path.join(srcfile, file_name)
    print(full_file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, destroot)
    #else:
        #print("Something went wrong")