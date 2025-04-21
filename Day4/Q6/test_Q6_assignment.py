#MaxFile class 
from pkg.file import File 
import datetime
path = "."
fs = File("path")
max_size_files = fs.getMaxSizeFile(2) # gives two max file names 
print("largest two files:" , max_size_files)

latest_files =  fs.getLatestFiles(datetime.date(2018,2,1))
print("latest files:", latest_files)        

#Returns list of files after 1st Feb 2018 
