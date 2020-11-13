import os,shutil
from num2words import num2words as n2w
def getname(p):
    p=os.path.split(p)
    return p[len(p)-1]
def splitext(s):
    sl=s.split(".")
    ext="."+sl[len(sl)-1]
    del sl[len(sl)-1]
    s=".".join(sl)
    return (s,ext)
def main(sdirs=["./files_one","./files_two","./files_three","./files_four","./files_five"],*,odir="./out",dupedir=None):
    if type(dupedir)!=str:
        dupedir=None
    else:
        if dupedir.replace(" ","")=="":
            dupedir==None
    duped={}
    if os.path.exists(odir):
        shutil.rmtree(odir,ignore_errors=True)
    os.mkdir(odir)
    if dupedir!=None:
        dupes=True
        if os.path.exists(dupedir):
            shutil.rmtree(dupedir,ignore_errors=True)
        os.mkdir(dupedir)
    else:
        dupes=False
    for sdir in sdirs:
        files=[]
        for dp,dn,fns in os.walk(sdir):
            for f in fns:
                files.append(os.path.join(dp,f))
        for f in files:
            orig=f
            f=os.path.join(odir,getname(f))
            if not os.path.exists(f):
                shutil.copy(orig,f)
            elif dupes:
                fd=os.path.join(dupedir,getname(orig))
                try:
                    duped[getname(orig)]+=1
                except KeyError:
                    duped.update({getname(orig):2})
                    shutil.copy(f,f"{splitext(fd)[0]}_copy_{n2w(duped[getname(orig)]-1)}{splitext(fd)[1]}")
                shutil.copy(orig,f"{splitext(fd)[0]}_copy_{n2w(duped[getname(orig)])}{splitext(fd)[1]}")
    print("Done!!!")
if __name__=="__main__":
    main(dupedir="./dupes")