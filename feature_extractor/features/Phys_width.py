import math
import cv2
import sys
class Phys_width:
    def width(self,set1,set2,terminals,phy_length):
        ""
        #print(set1.__len__()+set2.__len__())
        if (terminals[1][0]-terminals[0][0])==0:
            m=sys.float_info[0]
        else:
            m=((terminals[1][1]-terminals[0][1])/(terminals[1][0]-terminals[0][0]))
            m=float(format(m,'.6f'))
        print("M:",m)
        len1=list()
        maxi1,maxj1=0,0

        len2=list()
        maxi2,maxj2=0,0
        print("set1: ",set1.__len__())
        print("set2: ",set2.__len__())
        for i in range(set1.__len__()):
            for j in range(set2.__len__()):
                if int(set2[j][0]-set1[i][0]) == 0:
                    slop=sys.float_info[0]

                else:
                    slop=(set2[j][1]-set1[i][1])/(set2[j][0]-set1[i][0])
                    slop=float(format(slop,'.6f'))

                #print(math.floor(slop*m))
                x1=(set2[j][0]-set1[i][0])**2
                x2=(set2[j][1]-set1[i][1])**2

                length=math.pow((x1+x2),0.5)
                #print(length)

                if (slop!=sys.float_info[0]) & (m != sys.float_info[0]):
                    if math.ceil(slop*m)==-1 | math.floor(slop*m)==-1:
                        len1.append(length)
                elif (int(m)==0) & (int(set2[j][0]-set1[i][0]) == 0):
                    len1.append(length)
                elif (m==sys.float_info[0]) & (slop==0.00):
                    len1.append(length)

                len2.append(length)

        biggest_width=float(format((math.pow((x1+x2),0.5)),'.6f'))
        #print(biggest_width)
        #biggest_line_point=list()
        #biggest_line_point.append((set1[maxi1][0],set1[maxi1][1]))
        #biggest_line_point.append((set2[maxj1][0],set2[maxj1][1]))

        diameter=float(format((max(len2)),'.6f'))
        #diameter_points=list()
        #if diameter < float(phy_length):
            #diameter=phy_length

            #diameter_points.append(terminals[0])
            #diameter_points.append(terminals[1])

        #diameter_points.append((set1[maxi2][0],set1[maxi2][1]))
        #diameter_points.append((set2[maxj2][0],set2[maxj2][1]))

        return biggest_width,diameter
