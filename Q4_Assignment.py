import glob
import os
import os.path
import pickle
pathname = r"C:\Users\Sreyas\Downloads\handson\Day2"
path_exist = os.path.isdir(pathname)
print(path_exist)
for dir_name, subdir_name, filenames in os.walk(pathname, topdown = False):
    print("filenames:", filenames)
    for file in filenames:
        filepath = os.path.join(dir_name,file)
        with open ( "filesdir_picklefile.pkl", "wb") as f:
            pickle.dump(filenames, f)
        print(f)