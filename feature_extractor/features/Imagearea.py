from feature_extractor.pre_processing.Countblackpixels import Countblackpixels
class Imagearea:
    def area(self,img):
        black=Countblackpixels().countBlackPixels(img)
        #height,width=img.shape
        return black
