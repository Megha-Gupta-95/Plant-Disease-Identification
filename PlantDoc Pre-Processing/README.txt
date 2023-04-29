PlantDoc-Object-Detection-Dataset-master.rar is the original dataset. 
It contains train and test folders containing jpg and xml files. The xml files contains the bounding box coordinates.
csv files are also provided containing bounding box coordinates.

crop_images.py used xml files to crop each image in the dataset (both train and test)
Saved each cropped image under the class name folder.
The outcome is PlantDoc_cropped. It contains train_cropped and test_cropped folders.
Both these folders are merged. The merged folder is called Merged_PlantDoc.
Two classes are removed from this as they contained very less images.
-Potato Leaf
- Tomato two spotted spider mites leaf.
after removing this the dataset is named as Merged_PlantDoc2 dataset.

The images are augmented using Augmenting PlantDoc python script. The final dataset obtained is Merged_PlantDoc2_Augmented.
 