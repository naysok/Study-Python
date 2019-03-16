#
# https://qiita.com/pashango2/items/145d858eff3c505c100a

from PIL import Image
image = Image.open('ImageSample.jpg')
image.show() ## open preview.app
r,g,b = image.split()

## RGB to BGR
convert_image = Image.merge('RGB',(b,g,r))
convert_image.show()
#convert_image.save('ImageSample_rgb_to_bgr.jpg')



# グレイスケール
gray0 = image.convert("L")
gray0.show()
#gray0.save('ImageSample_gray.jpg')


# 二値化（グレイスケールとセットで）
def filter(col):
    if col>128:
        return 255
    else:
        return 0
gray1 = gray0.point(filter)
gray1.show()
#gray1.save('ImageSample_2_BW.jpg')

# 逆二値化（グレイスケールとセットで）
def flip(col):
    if col>128:
        return 0
    else:
        return 255
gray2 = gray0.point(flip)
gray2.show()
#gray2.save('ImageSample_2_WB.jpg')


## RGB to RBG
convert_image2 = Image.merge('RGB',(r,b,g))
convert_image2.show()
#convert_image2.save('ImageSample_rgb_to_rbg.jpg')

## RGB to BRG
convert_image3 = Image.merge('RGB',(b,r,g))
convert_image3.show()
#convert_image3.save('ImageSample_rgb_to_brg.jpg')

## RGB to BGR
convert_image4 = Image.merge('RGB',(b,g,r))
convert_image4.show()
#convert_image4.save('ImageSample_rgb_to_bgr.jpg')

## RGB to GBR
convert_image5 = Image.merge('RGB',(g,b,r))
convert_image5.show()
#convert_image5.save('ImageSample_rgb_to_gbr.jpg')

## RGB to GRB
convert_image6 = Image.merge('RGB',(g,r,b))
convert_image6.show()
#convert_image6.save('ImageSample_rgb_to_grb.jpg')
