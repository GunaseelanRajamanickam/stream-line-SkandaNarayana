
import sys

parameters = ["soc", "temp"]

def inferReceivedData(windowSize, readFromConsole, formulateReadings, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading, convertCSVFormat, printOnConsole):
    stream = readFromConsole()
    print(stream)
    mergedreadings = formulateReadings(stream)
    statisticsReading = []
    for parameter in parameters:
        readings = extractEachParameterReadings(mergedreadings, parameter)
        movingAverage = calculateMovingAverage(readings, windowSize)
        minMaxReading = calculateMinMaxReading(readings)
        formattedString = convertCSVFormat(parameter,minMaxReading,movingAverage)
        statisticsReading.append(formattedString)
        printOnConsole(formattedString)
    return statisticsReading

def readFromConsole():  # pragma: no cover
    lines = sys.stdin.readlines()
    return lines
    
def formulateReadings(stream):
    mergedReadings = []
    for reading in range(2):
        readings = stream[reading]
        readings = readings.strip(' \n')
        readings = readings[(readings.find(',')+1):]
        formattedreading = list(map(float,readings.split(' ')))
        mergedReadings.append(formattedreading)
    return mergedReadings

def extractEachParameterReadings(mergedReadings, parameter):
    index = getindex(parameter)
    return mergedReadings[index]

def getindex(parameter):
    for index, parameterName in enumerate(parameters):
        if parameterName == parameter:
            return index

def calculateMovingAverage(readings, windowSize):
    windows = createWindow(readings, windowSize)
    movingAverages = [roundOffAverage(calculateAverage(window), 2) for window in windows]
    return movingAverages

def roundOffAverage(value, digits):
    return round(value, digits)

def calculateAverage(array):
    return calculateSum(array) / len(array)

def calculateSum(array):
    return sum(array)

def createWindow(readings, windowSize):
    windows = [readings[index : index + windowSize] for index, value in enumerate(readings) if index < len(readings) - windowSize + 1]
    return windows

def calculateMinMaxReading(readings):
    minReading = calculateMinReading(readings)
    maxReading = calculateMaxReading(readings)
    return {'min': minReading, 'max': maxReading}

def calculateMinReading(readings):
    return min(readings)

def calculateMaxReading(readings):
    return max(readings)

def convertCSVFormat(parameter,minMaxReading,movingAverage):
  return f'{parameter}:{minMaxReading},{movingAverage}'

def printOnConsole(string):
    print(string)
    return True

if __name__ == '__main__':  # pragma: no cover
  inferReceivedData(5, readFromConsole, formulateReadings, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading, convertCSVFormat, printOnConsole)
