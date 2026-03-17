import os, shutil

def gen_public(src, dest):
    
    os.mkdir(dest)
    contents = os.listdir(src)

    for content in contents:
        path = os.path.join(src, content)
        destpath = os.path.join(dest, content)
        
        if os.path.isfile(path):
            shutil.copy(path, destpath)
        else:
            gen_public(path, destpath)
