from PIL import Image
import os, glob
import numpy as np
#from sklearn import cross_validation
from sklearn import model_selection

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み

X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)


# TensorFlowが扱いやすいデータに変える
X = np.array(X)
Y = np.array(Y)

# 学習用とテスト用でデータを分類する
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save("./animal.npy", xy)
