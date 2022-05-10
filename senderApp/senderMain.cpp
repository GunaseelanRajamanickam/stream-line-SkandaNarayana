#include <chrono>
#include <thread>

#include "../Sender.h"

int main()
{
    
    std::string temperatureValueFilePath = "../temperatureRangeOfValues.txt";
    std::string socValueFilePath = "../SoCValuesFromSensor.txt";
    Sender senderObj;
    Sender* senderObj = new Sender;
    senderObj->readFromFile(temperatureValueFilePath, "TEMPERATURE");
    senderObj->readFromFile(socValueFilePath, "SOC");
    senderObj->writeToConsole();
    std::this_thread::sleep_for(std::chrono::milliseconds(500));

    return 0;
}
