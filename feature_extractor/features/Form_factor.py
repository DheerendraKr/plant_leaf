import math
class Form_factor:

    def formFactor(self,area,perimeter):
        return float(format(((4*3.24*area)/(math.pow(perimeter,2))),'.6f'))
