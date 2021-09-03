import os 

# Folder Names
searches = "searches"
dataName = "data.json"

# Paths
path = os.getcwd().__str__().replace("\\", "/")
searchesFolderPath = os.path.join(path, searches)

# Chrome path 
# Mention your driver path here!
chromePath = "C:\\Users\\bella\\chromedriver_win32\\chromedriver.exe"

# Regex 
reviewsRegex = r"^[+-]?[0-9]*[.]?[0-9]+"

# Argsort 
def argsort(seq):
    # http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3383106#3383106
    #non-lambda version by Tony Veijalainen
    return [i for (v, i) in sorted((v, i) for (i, v) in enumerate(seq))]

def int_argsort(seq):
    return [i[0] for i in sorted(enumerate(seq), key=lambda x:x[1])]
# n products need to be printed 
n_sizebase_products = 2
n_cheapest_products = 3


delay = 5 # seconds