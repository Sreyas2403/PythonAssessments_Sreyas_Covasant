import os 
import datetime
from datetime import datetime
path = r"C:\Users\Sreyas\Downloads\handson\pkg"
path_exist = os.path.isdir(path)

class File:
    
    def __init__(self,path):
        self.path = path
    
    def getMaxSizeFile(self,n):
        files_list = []
        for root_dir, sub_dir, files in os.walk(path):
            print("files in folder:" ,files)
            for file in files:
                filepath = os.path.join(root_dir,file)
                try:
                    filesize = os.path.getsize(filepath)
                    files_list.append((filepath,filesize))
                except:
                    continue            
        sorted_list = sorted(files_list, key = lambda x: x[1])
        return sorted_list[:n]
    
    
    def getLatestFiles(self, date):
        target_date = "2018-02-01"
        parsed_date = datetime.strptime(target_date, "%Y-%m-%d").date()
        latest_files = []
        for root_dir, sub_dir, files in os.walk(path):
            for file in files:
                filepath = os.path.join(root_dir,file)
                try:
                    file_ctime = os.path.getctime(filepath)
                    file_date = datetime.fromtimestamp(file_ctime).date()
                    if file_date > parsed_date:
                        latest_files.append((file,file_ctime))
                except:
                    continue
        return latest_files
          
