import cv2
import math
import numpy as np

class Color_features:

    def colorFeatures(self,image):
        ""

        height, width,channel=image.shape

        b,g,r=cv2.split(image)

        #count=height*width

        count=0
        val=[255,255,255]
        valb,valg,valr=0,0,0
        for i in range(height):
           for j in range(width):
               if (b[i][j]==255) &(g[i][j]==255) & (r[i][j]==255):
                   ""
               else:
                   count+=1
                   valb+=b[i][j]
                   valg+=g[i][j]
                   valr+=r[i][j]

        mb=valb/count
        mg=valg/count
        mr=valr/count
        #avg = np.average(image, axis=0)
        #avg = np.average(avg, axis=0)

        mb=float(format(mb,'.6f'))
        mg=float(format(mg,'.6f'))
        mr=float(format(mg,'.6f'))

        sb,sg,sr=0,0,0
        tb,tg,tr=0,0,0
        gb,gg,gr=0,0,0
        for i in range(height):
            for j in range(width):
                if (b[i][j]==255) &(g[i][j]==255) & (r[i][j]==255):
                    ""
                else:
                    sb+=math.pow((b[i][j]-mb),2)
                    tb+=math.pow((b[i][j]-mb),3)
                    gb+=math.pow((b[i][j]-mb),4)

                    sg+=math.pow((g[i][j]-mg),2)
                    tg+=math.pow((g[i][j]-mg),3)
                    gg+=math.pow((g[i][j]-mg),4)

                    sr+=math.pow((r[i][j]-mr),2)
                    tr+=math.pow((r[i][j]-mr),3)
                    gr+=math.pow((r[i][j]-mr),4)



        sigmab=float(format(math.pow((sb/count),0.5),'.6f'))
        thetab=float(format((tb)/(count*math.pow(sigmab,3)),'.6f'))
        gammab=float(format((gb)/(count*math.pow(sigmab,4)),'.6f'))

        sigmag=float(format(math.pow((sg/count),0.5),'.6f'))
        thetag=float(format((tg)/(count*math.pow(sigmag,3)),'.6f'))
        gammag=float(format((gg)/(count*math.pow(sigmag,4)),'.6f'))

        sigmar=float(format(math.pow((sr/count),0.5),'.6f'))
        thetar=float(format((tb)/(count*math.pow(sigmar,3)),'.6f'))
        gammar=float(format((gb)/(count*math.pow(sigmar,4)),'.6f'))

        color_features=[mb,sigmab,thetab,gammab]+[mg,sigmag,thetag,gammag]+[mr,sigmar,thetar,gammar]

        #print ("count: ",count)
        #print("B:")
        #print("mean: ",mb)
        #print("deviation: ",sigmab)
        #print("skewness: ",thetab)
        #print("kurtosis: ",gammab)
        #print("\n")

        #print("G: ")
        #print("mean: ",mg)
        #print("deviation: ",sigmag)
        #print("skewness: ",thetag)
        #print("kurtosis: ",gammag)
        #print("\n")

        #print("R: ")
        #print("mean: ",mr)
        #print("deviation: ",sigmar)
        #print("skewness: ",thetar)
        #print("kurtosis: ",gammar)

        #print(color_features)
        return color_features

