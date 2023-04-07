import pandas as pd
import xml.etree.ElementTree as ET
import cv2
import os


df = pd.read_csv (r'train_labels.csv')
print (df.head())

df_2 = pd.read_csv(r'test_labels.csv')
print(df_2.head())

train_path = 'TEST/'
train_list = os.listdir(train_path)

print(len(train_list))

cnt = 1
for image_name in train_list:
    #print(cnt)
    cnt = cnt+1
    if 'jpg' in image_name[-3:]:
        #print(image_name)
        image = cv2.imread(r'TEST/' + image_name)
        #print(image.shape)
        
        #cv2.imshow("Image",image)

        # Passing the path of the
        # xml document to enable the
        # parsing process

        if os.path.exists('TEST/'+image_name[:-3]+'xml'):
            tree = ET.parse('TEST/'+image_name[:-3]+'xml')

            #print(tree)
            root = tree.getroot()
            #cnt = 1
            for obj in root.findall('object'):
                #print(obj)
                for name in obj.findall('name'):
                    #print(name)
                    dir_name = 'test_cropped/' + name.text;
                    #print(dir_name)
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)
                    cropped_img_name = str(len(os.listdir(dir_name))) + '.jpg'
                
                for bndbx in obj.findall('bndbox'):
                    #print(bndbx)
                    x_min = int(bndbx.find('xmin').text)
                    y_min = int(bndbx.find('ymin').text)
                    x_max = int(bndbx.find('xmax').text)
                    y_max = int(bndbx.find('ymax').text)

                    #print(x_min,y_min,x_max,y_max)

                    cropped_img = image[y_min:y_max,x_min:x_max]
                    #print(cropped_img_name)
                    #print(cropped_img.shape)
                    flag = True
                    for i in cropped_img.shape:
                        if i<=0:
                            flag = False
                    if flag:
                        cv2.imwrite(dir_name + '/' + cropped_img_name,cropped_img)
                    else:
                        print(dir_name + '/' + cropped_img_name,image_name,"error")
                    
                    #cv2.imshow(str(cnt),cropped_img)
                    #cnt = cnt+1

