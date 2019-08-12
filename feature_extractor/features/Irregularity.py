from feature_extractor.features.Centroid import Centroid
import math

class Irregularity:

    def irregularity(self,set1,set2):
        point_set=set1+set2
        list_point=list()
        centroid=Centroid().centroid(point_set)
        for i in (point_set):
            val=math.pow((math.pow((i[0]-centroid[0]),2)+math.pow((i[1]-centroid[1]),2)),0.5)
            list_point.append(val)
        max_nu=max(list_point)
        min_de=min(list_point)
        irr=float(format(max_nu/min_de , '.6f'))
        return irr
