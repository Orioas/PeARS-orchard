'''Index URLs from a csv or png sent by a friend.'''
from PIL import Image
from os.path import dirname,join,realpath,isfile

dir_path = dirname(dirname(dirname(realpath(__file__))))

def parse_line(l):
    fields = l.rstrip('\n').split(',')
    url = fields[1]
    title = fields[2]
    snippet = fields[3]
    vector = fields[4]
    freqs = fields[5]
    cc = False
    if fields[6] == "True":
        cc = True
    return url, title, snippet, vector, freqs, cc

def convert_img_to_csv():
    image = Image.open(join(dir_path, "urls_from_pod.png"))
    pixels = list(image.getdata())

    f = open(join(dir_path, "urls_from_pod.csv"),'w')
        
    for p in pixels:
        a = 255 - p[0]
        b = 255 - p[1]
        c = 255 - p[2]
        f.write(chr(a+b+c))

    f.close()
