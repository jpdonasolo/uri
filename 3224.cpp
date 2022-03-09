#include <iostream>
#include <string>

int main()
{

    std::string jon, doctor;

    std::cin >> jon;
    std::cin >> doctor;

    if (jon.size() >= doctor.size())
    {
        std::cout << "go" << std::endl;
    }
    else
    {
        std::cout << "no" << std::endl;
    }

    return 0;
}