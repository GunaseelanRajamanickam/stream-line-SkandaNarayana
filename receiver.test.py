from unittest import mock
import unittest
import receiver

class SenderTest(unittest.TestCase):
    def test_printOnConsole(self):
        self.assertTrue(receiver.printOnConsole('All is fine!') == True)
    
    def test_calculateMinMaxParameter(self):
        self.assertTrue(receiver.calculateMinMaxReading([5,10,2,3,10]) == {'min': 2, 'max': 10})
    
    def test_calculateMovingAverage(self):
        self.assertTrue(receiver.calculateMovingAverage([5,10,2,3,10,17,16,14], 5) == [6.0,8.4,9.6,12])
    
    def test_createWindow(self):
        self.assertTrue(receiver.createWindow([5,10,2,3,10,17,16,14], 5) == [[5, 10, 2, 3, 10], [10, 2, 3, 10, 17], [2, 3, 10, 17, 16], [3, 10, 17, 16, 14]])

    def test_getindex(self):
        self.assertTrue(receiver.getindex("soc") == 0)
        self.assertTrue(receiver.getindex("temp") == 1)
    
    def test_formulateReadings(self):
        self.assertTrue(receiver.formulateReadings(['soc,5 10 20\n','temp,6 15 30\n']) == [[5,10,20],[6,15,30]])

    def test_extractEachParameterReadings(self):
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "soc") == [5,10,20])
        self.assertTrue(receiver.extractEachParameterReadings([[5,10,20],[6,15,30]], "temp") == [6,15,30])

    @mock.patch('receiver.readFromConsole', return_value=['SOC,10 20 50 100 80 90 60 44 15 54\n', 'TEMPERATURE,1 4 7 9 2 5 2 20 15 30\n'])
    def test_inferReceivedData(self, mock_readFromConsole):
        expected_output = ["soc:{'min': 10.0, 'max': 100.0},[52.0, 68.0, 76.0, 74.8, 57.8, 52.6]", "temp:{'min': 1.0, 'max': 30.0},[4.6, 5.4, 5.0, 7.6, 8.8, 14.4]"]
        self.assertTrue(receiver.inferReceivedData(5, mock_readFromConsole, receiver.formulateReadings, receiver.extractEachParameterReadings, receiver.calculateMovingAverage, receiver.calculateMinMaxReading, receiver.convertCSVFormat, receiver.printOnConsole) == expected_output)

if __name__ == '__main__': # pragma: no cover
  unittest.main()
