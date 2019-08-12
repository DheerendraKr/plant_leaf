class Centroid:
    def centroid(self,point_set):
        sumx,sumy=0,0
        for i in (point_set):
            sumx+=i[0]
            sumy+=i[1]
        meanx=sumx/point_set.__len__()
        meany=sumy/point_set.__len__()

        cent=[meanx,meany]
        return cent

