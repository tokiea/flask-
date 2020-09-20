import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

modelpath1 = 'people_with_other_2.h5'
modelpath2 = 'VGG.h5'
model1 = load_model(modelpath1, compile=False)
model2 = load_model(modelpath2, compile=False)
# 一定要加 这个
model1.predict(np.zeros((1, 150, 150, 3)))
model2.predict(np.zeros((1, 150, 150, 3)))

basepath = os.path.join(os.path.dirname(__file__), 'static')


def discern(name_list, category):
    global model1
    global model2
    print(name_list)
    re_list = []
    if name_list:
        for i in name_list:
            img = image.load_img(os.path.join(basepath, i), target_size=(150, 150))
            x = image.img_to_array(img)

            x = np.expand_dims(x, axis=0)

            if category == 'dog':
                pres = model1.predict(x)
                if int(pres[0][0]) > 0.8:
                    re_list.append({'static': os.path.join('static', i), 'result': '小狗'})
                else:
                    re_list.append({'static': os.path.join('static', i), 'result': '其他'})
            else:  # category = 'people'
                pres = model2.predict(x)
                if int(pres[0][0]) > 0.8:
                    re_list.append({'static': os.path.join('static', i), 'result': '人'})
                else:
                    re_list.append({'static': os.path.join('static', i), 'result': '其他'})

            # print(int(pres[0][0]))

        return re_list
