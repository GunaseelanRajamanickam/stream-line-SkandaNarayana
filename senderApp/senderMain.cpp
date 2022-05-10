#include <chrono>
#include <thread>

#include "../test/catch.hpp"
#include "../Sender.h"

int main()
{
    std::unordered_map<std::string , std::vector<int>> temperature = {};
    std::unordered_map<std::string , std::vector<int>> soc = {};
    std::string temperatureValueFilePath = "../temperatureRangeOfValues.txt";
    std::string socValueFilePath = "../SoCValuesFromSensor.txt";
    Sender* senderObj = new Sender;
    temperature = senderObj->readFromFile(temperatureValueFilePath, "TEMPERATURE");
    soc = senderObj->readFromFile(socValueFilePath, "SOC");
    /*senderObj->writeToConsole();*/
    std::this_thread::sleep_for(std::chrono::milliseconds(500));

    return 0;
}
