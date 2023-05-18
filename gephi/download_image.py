import pandas as pd
import requests
import os
print(os.path.exists("image"))

if not os.path.exists("image"):
    os.mkdir("image")
    df = pd.read_csv("node.csv")

    image_names = []

    for i, url in enumerate(df["Image"].tolist()):
        img_data = requests.get(url).content

        image_name = '{}.jpg'.format(i)
        image_names.append(image_name)
        with open("image/{}".format(image_name), 'wb') as handler:
            handler.write(img_data)

    df["Image"] = image_names
    df.to_csv("new_node.csv", index=False)
