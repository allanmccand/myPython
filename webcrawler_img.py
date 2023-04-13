import urllib.request
import requests
import shutil

#Syntax for url and url_short
#url: https://www.youraddress.com/page1/page2
#url_short: https://www.youraddress.com
#No trailing /
url = "https://www.shutterstock.com/search/cat"
url_short = "https://www.shutterstock.com"

def get_img(file_count,imgext,img):
    try:
        fileName = 'C:\\Users\\Allan\\PycharmProjects\\pythonProject\\test\\file' + str(file_count) + imgext

        if img is not None and img != '':
            if img[0] == '/':
                img = url_short + img

            print(img)

            req = requests.get(img,stream = True)

            with open(fileName, 'wb') as f:
                shutil.copyfileobj(req.raw, f)

            file_count+=1
    except Exception as e:
        print("Exception in get_img")
        print("Invalid image["+img+"]")
        print(type(e))
        print(e.args)
        print(e)
    return file_count

def main():
    file_count = 0
    try:
        fp = urllib.request.urlopen(url)
        for line in fp.readlines():
            if 'content' in str(line) \
                    or 'href' in str(line) \
                    or 'src' in str(line):

                imgstr = str(line).split('"')

                previmg = ""
                for unparsedimg in imgstr:
                    if unparsedimg != previmg:
                        if '.png' in unparsedimg:
                            file_count = get_img(file_count,'.png', unparsedimg)
                            previmg = unparsedimg
                        elif '.jpg' in unparsedimg:
                            file_count = get_img(file_count,'.jpg', unparsedimg)
                            previmg = unparsedimg
                        elif '.gif' in unparsedimg:
                            file_count = get_img(file_count,'.gif', unparsedimg)
                            previmg = unparsedimg
        fp.close()
    except Exception as e:
        print("Exception in main")
        print(type(e))
        print(e.args)
        print(e)

main()



