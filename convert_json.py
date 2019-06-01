import json
import os


def convert(coordinates):
    x = []
    y = []

    for i in range(len(coordinates)):
        currentX = coordinates[i]['x']
        currentY = coordinates[i]['y']

        x.append(currentX)
        y.append(currentY)

    boxTopX = min(x)
    boxTopY = min(y)

    boxBottomX = max(x)
    boxBottomY = max(y)

    return f'{boxTopX},{boxTopY},{boxBottomX},{boxBottomY},0'


def list_contains(element_list, element):
    try:
        return element_list.index(element) > 0
    except:
        return False


fileNames = os.listdir('files/positive-examples')
negativeFileNames = os.listdir('D:\\Torrents\\World.of.Warcraft.3.3.5a.Truewow\\Screenshots\\Nothing')

with open('train.txt', 'w') as training_data:
    for i in range(len(negativeFileNames)):
        training_data.write(f'/content/drive/My Drive/Colab Notebooks/Negative/{negativeFileNames[i]}\n')

    with open('./files/positive-examples-mapping.json') as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            entry = data[i]
            fileName = entry['External ID']
            label = entry['Label']

            if label == 'Skip':
                continue

            coordinates = label['Node']

            textLine = f'/content/drive/My Drive/Colab Notebooks/Positive/{fileName}'

            for j in range(len(coordinates)):
                singleBoxCoordinates = coordinates[j]['geometry']

                textLine += '$$' + convert(singleBoxCoordinates)
            training_data.write(textLine + '\n')
            print(textLine)
        print(data)
