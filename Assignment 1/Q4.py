originalPixels = [[10, 20, 30], [40, 50, 60]]

class Image:
    def __init__(self, pixelList):
        self.pixels = pixelList

    def applyTransformation(self, transformationFunc):
        self.pixels = transformationFunc(self.pixels)

    def getCopy(self):
        return [row[:] for row in self.pixels]


def flipHorizontal(pixelData):
    return [row[::-1] for row in pixelData]


def adjustBrightness(pixelData, brightnessValue):
    for i in range(len(pixelData)):
        for j in range(len(pixelData[0])):
            pixelData[i][j] += brightnessValue
    return pixelData


def rotateNinetyDegrees(pixelData):
    rows = len(pixelData)
    cols = len(pixelData[0])
    return [[pixelData[rows - j - 1][i] for j in range(rows)] for i in range(cols)]


class AugmentationPipeline:
    def __init__(self):
        self.functionList = []

    def addStep(self, transformFunc):
        self.functionList.append(transformFunc)

    def processImage(self, originalImage):
        results = []
        for step in self.functionList:
            imgCopy = Image(originalImage.getCopy())
            imgCopy.applyTransformation(step)
            results.append(imgCopy.pixels)
        return results


img = Image(originalPixels)

pipeline = AugmentationPipeline()

pipeline.addStep(flipHorizontal)
pipeline.addStep(lambda pixels: adjustBrightness(pixels, 10))
pipeline.addStep(rotateNinetyDegrees)

augmentedImages = pipeline.processImage(img)

for i, imgData in enumerate(augmentedImages, 1):
    print("\nTransformation", i)
    for row in imgData:
        print(row)
