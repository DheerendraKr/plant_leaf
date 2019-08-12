from feature_extractor.features.Leaf_terminals import Leaf_terminals
import math
class Phys_length:

    def phyLength(self,positions):
        #positions= Leaf_terminals().points(image)
        #print(positions)
        x1=math.pow((positions[0][0]-positions[1][0]),2)
        x2=math.pow((positions[0][1]-positions[1][1]),2)

        length=float(format((math.pow((x1+x2),0.5)),'.6f'))

        return length

