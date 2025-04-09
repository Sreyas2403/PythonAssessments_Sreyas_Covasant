import glob
import os
import os.path
pathname = r"C:\Users\Sreyas\Downloads\handson\Day2"
path_exist = os.path.isdir(pathname)
print(path_exist)
for dir_name, subdir_name, filenames in os.walk(pathname):
    print("directory name:", dir_name)
    print("sub directory name:", subdir_name)
    print("filenames:", filenames)
    for file in filenames:
        filepath = os.path.join(dir_name,file)
        try:
            fsize = {file: os.path.getsize(file)}
            fname_maxsize = max(fsize)
        except:
            continue
print(fname_maxsize)