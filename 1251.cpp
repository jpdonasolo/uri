#include <iostream>
#include <string>
#include <algorithm>

#define ARRAY_SIZE 200

struct Ch
{
    int ascii_code, count;
};

bool cmp(const Ch &a, const Ch &b)
{
    return a.count < b.count;
}

Ch array[ARRAY_SIZE];

int main(int argc, char const *argv[])
{

    std::string line;
    bool first_case{true};

    while (std::getline(std::cin, line))
    {
        if (not first_case)
        {
            std::cout << std::endl;
        }
        first_case = false;

        for (int i = 0; i < ARRAY_SIZE; i++)
        {
            array[i].ascii_code = ARRAY_SIZE - i;
            array[i].count = 0;
        }

        for (char c : line)
        {
            array[ARRAY_SIZE - c].count++;
        }

        std::stable_sort(array, array + ARRAY_SIZE, cmp);

        for (Ch c : array)
        {
            if (c.count != 0)
            {
                std::cout << c.ascii_code << ' ' << c.count << std::endl;
            }
        }
    }

    return 0;
}
