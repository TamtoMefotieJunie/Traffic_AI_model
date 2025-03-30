# Traffic_AI_model
AI model designed to identify traffic signs from given input image
To train the model i used  python traffic.py ../data/gtsrb best_model.h5
to run the gui i used python predict_sign.py

I encountered the problem of the model predicting the same class for every image i was uploading. finally fixed this by adding a class for labellings since the dataset had only numberings for each class. 
After identifying the content if each category in the dataset i was able to give a label to it because each category folder contained the same image
