import matplotlib.pyplot as plt
import numpy as np

# open and read the file

def loadFile():
    dataFile = open("spp_data.csv", "r")
    return dataFile.readlines()

# process the data line by line calculating statistics on it

def processData(contents):
    classResults = [0,0,0,0]
    totalMass = [0]
    totalSize = [0]
    animalCount = [0]
    iteration = 0
    for line in contents:
        splitLine = line.split(',')
        accumulateClass(splitLine, classResults)
        #print(classResults)
        #print(splitLine)
        if iteration > 0:
            accumulateMass(splitLine, totalMass, animalCount)
            accumulateSize(splitLine, totalSize)
        iteration += 1
    averageMass = computeAverageMass(totalMass, animalCount)
    averageSize = computeAverageSize(totalSize, animalCount)
    print "Average Mass: " + str(averageMass)
    print "Average Size: " + str(averageSize)
    plotClasses(classResults)

# accumulate of the number of animals in each class

def accumulateClass(splitLine, results):
    if splitLine[0] == "BIRD":
        results[0] += 1
    elif splitLine[0] == "FROG":
        results[1] += 1
    elif splitLine[0] == "REPT":
        results[2] += 1
    elif splitLine[0] == "MAMM":
        results[3] += 1
        
# accumulate the total mass of all the animals

def accumulateMass(splitLine, totalMass, animalCount):
    if splitLine[7] != '.':
        totalMass[0] += float(splitLine[7])
        animalCount[0] += 1
        
# accumulate the total size of all the animals

def accumulateSize(splitLine, totalSize):
    if splitLine[10] != '.':
        totalSize[0] += float(splitLine[10])
        
# compute the average size of all the animals

def computeAverageSize(totalSize, animalCount):
    #print totalSize
    #print animalCount
    return totalSize[0] / animalCount[0]

# compute the average mass of all the animals

def computeAverageMass(totalMass, animalCount):
    #print totalMass
    #print animalCount
    return totalMass[0] / animalCount[0]

# plot the animal class counts in a horizontal bar graph

def plotClasses(results):
    classes = ["Bird", "Frog", "Reptile", "Mammal"]
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.set_yticks(np.arange(len(classes)))
    ax.barh([0,1,2,3],results)
    ax.set_yticklabels(classes)
    ax.set_xlabel("Number of animals")
    ax.set_title("Classes of Rainforest Vertebrates of Australia")
    plt.show()

# main function

def main():
    contents = loadFile()
    processData(contents)

if __name__ == "__main__":
    main()
