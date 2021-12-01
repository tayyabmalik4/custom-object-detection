from google.colab import drive
drive.mount('/content/drive')

!ls '/content/drive/MyDrive/yolo_custom_model_Training'


# !unzip '/content/drive/MyDrive/yolo_custom_model_Training/yolo_custom_model_training.zip' -d '/content/drive/MyDrive/yolo_custom_model_Training'

# !git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/MyDrive/yolo_custom_model_Training/darknet'

%cd '/content/drive/MyDrive/yolo_custom_model_Training/darknet'


!ls


!make


%cd '/content/drive/MyDrive/yolo_custom_model_Training'


!python classification_images/creating-files-data-and-name.py


!python classification_images/creating-train-and-test-txt-files.py



!darknet/darknet detector train classification_images/labelled_data.data darknet/cfg/yolov3_custom.cfg custom_weight/darknet53.conv.74 -dont_show









