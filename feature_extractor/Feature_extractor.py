import cv2

from feature_extractor.pre_processing.Background_subtractor import Background_subtractor
from feature_extractor.features.Color_features import Color_features
from feature_extractor.features.Rectangularity import Rectangularity
from feature_extractor.features.Form_factor import Form_factor
from feature_extractor.features.Form_factor import Form_factor
from feature_extractor.features.Narrow_factor import Narrow_factor
from feature_extractor.features.Perimeter_ratio_of_diameter import Perimeter_ratio_of_diameter
from feature_extractor.features.Perimeter_ratio_of_length_width import Perimeter_ratio_of_length_width
from feature_extractor.leaf_image_capture import Capture_image
from feature_extractor.pre_processing import Rgbtogray
from feature_extractor.pre_processing import Graytobin
from feature_extractor.features import Perimeter
from feature_extractor.features import Imagearea
from feature_extractor.features import Phys_length
from feature_extractor.features import Phys_width
from feature_extractor.features import Leaf_terminals
from feature_extractor.pre_processing import Edges
from feature_extractor.features import Boundry_pixels
from feature_extractor.features.Aspect_ratio import Aspect_ratio
from feature_extractor.features.Irregularity import Irregularity

class Feature_extractor:

    def featureExtractor(self,path,plant_type,leaf_n):
        "Extract all the features of the leaf image"

        img=cv2.imread(path,cv2.IMREAD_COLOR)
        img_name=cv2.resize(img,(640,480))
        img_name= cv2.medianBlur(img_name, 3)

        img_name=Background_subtractor().backgroundSubtractor(img_name)

        geometric_features=Feature_extractor().image_features(img_name,plant_type,leaf_n)

        color_features=Color_features().colorFeatures(img_name)
        feature_vector=geometric_features+color_features
        return feature_vector

    def image_features(self,img_name,plant_type,leaf_n):
        features_list=list()
        gray_image=Rgbtogray().rgbToGray(img_name)

        bin_image=Graytobin().grayToBinary(gray_image)
        edge_image=Edges().detectEdges(bin_image)

        area=Imagearea().area(bin_image)
        #print("Area: ",area)
        features_list.append(area)

        perimeter=Perimeter().perimeter(edge_image)
        #print("Perimeter: ",perimeter)
        features_list.append(perimeter)

        #terminals=Leaf_terminals().points(edge_image,plant_type,leaf_n)
        terminals=Leaf_terminals().points(img_name,plant_type,leaf_n)
        pixels_set1,pixels_set2=Boundry_pixels().boundryPixels(bin_image,terminals)


        #print(pixels_set1)
        #print(pixels_set2)

        phy_length=Phys_length().phyLength(terminals)
        #print("Physiological_length: ",phy_length)
        features_list.append(phy_length)

        #print(pixels_set1[0][0])
        #print(pixels_set2[0][0])

        phy_width,diameter=Phys_width().width(pixels_set1,pixels_set2,terminals,phy_length)
        #print("Physiological Width: ",phy_width)
        #print("Diameter: ",diameter)
        features_list.append(phy_width)
        features_list.append(diameter)

        #aspect ratio
        aspect_ratio=Aspect_ratio().aspectRatio(phy_length,phy_width)
        #print("Aspect ratio: ",aspect_ratio)
        features_list.append(aspect_ratio)

        #form factor
        form_factor=Form_factor().formFactor(area,perimeter)
        #print("Form factor: ",form_factor)
        features_list.append(form_factor)

        #Narrow_factor
        narrow_factor=Narrow_factor().narrowFactor(diameter,phy_length)
        #print("Narrow factor: ",narrow_factor)
        features_list.append(narrow_factor)

        #perimeter to diameter ratio
        prd=Perimeter_ratio_of_diameter().perimeterRatioOfDiameter(perimeter,diameter)
        #print("Perimeter to diamter ratio: ",prd)
        features_list.append(prd)

        #perimeter to length and width ratio
        prlw=Perimeter_ratio_of_length_width().perimeterRatioOfLengthWidth(perimeter,phy_length,phy_width)
        #print("Ratio of Perimetre to length and width: ",prlw)
        features_list.append(prlw)

        #Rectangularity
        rectangularity=Rectangularity().rectangularity(phy_length,phy_width,area)
        #print("Rectangularity: ",rectangularity)
        features_list.append(rectangularity)

        #irregularity
        irregularity=Irregularity().irregularity(pixels_set1,pixels_set2)
        #print("Irregularity: ",irregularity)
        features_list.append(irregularity)

        return features_list
