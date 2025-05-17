#include <iostream>
#include <list>

std::vector<unsigned long long> calc(unsigned long long starting) {
    std::vector<unsigned long long> numList = {starting};
    std::cout << starting << std::endl;
    while (true) {
        if (starting % 2 == 0) {
            starting /= 2;
        } else {
            starting = 3 * starting + 1;
        }
        std::cout << starting << std::endl;
        numList.push_back(starting);
        
        
        if (starting == 1) {
            break;
        }
    }
    return numList;
}

int main() {
    unsigned long long starting;
    std::cout << "Enter a starting number: ";
    std::cin >> starting;
    //std::cout << "Starting: " << starting << std::endl;
    unsigned long long max_ull = std::numeric_limits<unsigned long long>::max();
    while (std::cin.fail()) {
        std::cout << "Invalid input/overflow error!" << std::endl;
        std::cout << "Maximum number size: " << max_ull << std::endl;
        std::cout << "Pick another number: ";
        std::cin.clear();
        std::cin >> starting;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    std::vector<unsigned long long> result = calc(starting);
    auto max_element_ptr = std::max_element(result.begin(), result.end());
    unsigned long long max_value = *max_element_ptr;
    std::cout << "\nIt took " + std::to_string(result.size() - 1) + " iterations to reach 1 from " + std::to_string(result[0]) + "." << std::endl;
    std::cout << "The maximum value was " + std::to_string(max_value) + "." << std::endl;
    return 0;
}