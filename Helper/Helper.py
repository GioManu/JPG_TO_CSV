import csv
import cv2
import os
import numpy as np
from Settings import *

def SaveToCSV(table,destination):
    print("Saving Generated List")
    with open(destination, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(table)

    csvFile.close()

def GenerateLabels():
    print("Generating Labels")
    csvColumns = ["label"]

    for it in range(0, 784):
        csvColumns.append("pixel{}".format(it))

    RESULT_LIST.append(csvColumns)

def PutItem(item):
    print("Putting item - `{}` into list".format(item[0]))
    RESULT_LIST.append(item)

def generateMatrix(res,file):
    print("Generating matrix from - `{}` file".format(file))

    matrix = np.zeros((WIDTH_SIZE, HEIGTH_SIZE))

    for i in range(0, HEIGTH_SIZE):
        for j in range(0, WIDTH_SIZE):
            a = res[i][j].tolist()
            R, G, B = a[0], a[1], a[2]
            av = int(((R * 0.299) + (G * 0.587) + (B * 0.114)))
            matrix[i][j] = av if av != 255 else 0
    return matrix

def GenerateListOfBytes():
    print("Generating Started")
    GenerateLabels()

    sourcePath = os.path.join(os.getcwd(), SOURCE_FOLDER)
    dirs = [os.path.join(sourcePath,x) for x in os.listdir(sourcePath)]

    for dir in dirs:
        files = os.listdir(dir)

        for file in files:

            img = cv2.imread(os.path.join(dir,file))
            res = cv2.resize(img, dsize=(WIDTH_SIZE, HEIGTH_SIZE), interpolation=INTERPOLATION_MODE)

            matrix = generateMatrix(res,file)

            fileName = file.split('.')[0]

            csvItem = [fileName]
            for row in range(0, 28):
                for col in range(0, 28):
                    csvItem.append(int(matrix[row][col]))

            PutItem(csvItem)

    return RESULT_LIST

