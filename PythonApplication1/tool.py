import sys
from PIL import Image
argc = len(sys.argv)
#----------------------------------
dir=sys.argv[1]
filename=""
ext=""
dir=dir.replace("\\","/")
po=len(dir)-1
while 1:
    if dir[po]==".":
        ext=dir[po:len(dir)]
        extlen=len(dir)-po
    if dir[po]=="/":
        filename=dir[po+1:len(dir)-extlen]
        dir=dir[0:po+1]
        break
    po=po-1
#----------------------------------
if(argc == 2):#1pic

    imgin = Image.open(sys.argv[1])
    imgin = imgin.convert('RGBA')
    width=imgin.size[0]
    height=imgin.size[1]
    imgr = Image.new('RGBA',(width,height))
    imgg = Image.new('RGBA',(width,height))
    imgb = Image.new('RGBA',(width,height))
    if filename.count("_msk")==1:
        for x in range(width):
            for y in range(height):
                r,g,b,a = imgin.getpixel((x,y))
                imgr.putpixel((x,y),(255,255,255,r))
                imgg.putpixel((x,y),(255,255,255,g))
                imgb.putpixel((x,y),(255,255,255,b))

    if filename.count("_amb")==1:
        for x in range(width):
            for y in range(height):
                r,g,b,a = imgin.getpixel((x,y))
                r=255-r
                g=255-g
                b=255-b
                imgr.putpixel((x,y),(r,r,r,255))
                imgg.putpixel((x,y),(g,g,g,255))
                imgb.putpixel((x,y),(b,b,b,255))
    imgr.save(dir+filename+"_R"+ext)
    imgg.save(dir+filename+"_G"+ext)
    imgb.save(dir+filename+"_B"+ext)
if argc==4:#3pics
    filename=filename[0:len(filename)-2]
    for i in range(1,4):
        if sys.argv[i].count("_R")==1:
            imgr=Image.open(sys.argv[i])
            imgr = imgr.convert('RGBA')
        if sys.argv[i].count("_G")==1:
            imgg=Image.open(sys.argv[i])
            imgg = imgg.convert('RGBA')
        if sys.argv[i].count("_B")==1:
            imgb=Image.open(sys.argv[i])
            imgb = imgb.convert('RGBA')
    width=imgr.size[0]
    height=imgr.size[1]
    imgout=Image.new('RGBA',(width,height))
    if filename.count("_msk")==1:
        for x in range(width):
            for y in range(height):
                xy=x,y
                r1,g1,b1,a1 = imgr.getpixel(xy)
                r2,g2,b2,a2 = imgg.getpixel(xy)
                r3,g3,b3,a3 = imgb.getpixel(xy)
                imgout.putpixel(xy,(a1,a2,a3,255))
    if filename.count("_amb")==1:
        for x in range(width):
            for y in range(height):
                xy=x,y
                r1,g1,b1,a1 = imgr.getpixel(xy)
                r2,g2,b2,a2 = imgg.getpixel(xy)
                r3,g3,b3,a3 = imgb.getpixel(xy)
                imgout.putpixel(xy,(255-r1,255-g2,255-b3,255))
    imgout.save(dir+filename+ext)

    