import os

os.chdir("/home/anu/Documents/Checkforrename")
print(os.getcwd())
for f in os.listdir():
    os.path.splitext(f)
    (f_name, f_ext) = os.path.splitext(f)
    (f_title, f_num) = f_name.split("-")
    f_title = f_title.strip()
    # strip() removes whitespace & [1:] helps in removing the hash as it removes no. at index 0
    #.zfill() helps here in arranging size of digits
    f_num = f_num.strip()[1:].zfill(2)
    new_name = "{} - {}{}".format(f_num, f_title, f_ext)
    os.rename(f,new_name)