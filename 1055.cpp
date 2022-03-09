#include <iostream>
#include <cmath>
#include <algorithm>


int main(){

    int T, n, k;
    int mlt;  
    int eps = 0;
    int i;


    std::cin >> T;

    for (int caseT = 1; caseT <= T; caseT++){

        std::cin >> n;
        k = n - 1;


        int numbers[n];
        int intervals[k];

        if (n == 1){
            std::cout << "Case " << T << ": 0\n";
            continue;
        }
        

        for (i = 0; i < n; i++){
            std::cin >> numbers[i];
        }
        
        std::sort(numbers, numbers + n - 1);

        for (i = 0; i < k; i++){
            intervals[i] = std::abs(numbers[i] - numbers[i + 1]);
        }


        for (i = 0; i < std::ceil(k / 2) - 1; i++){
            mlt = i + 1;
            eps = eps * 2 * mlt * intervals[i];
            eps = eps * 2 * mlt * intervals[k - i - 1];
        }
        

        i = std::ceil(k / 2) - 1;
        mlt = i + 1;

        if (k % 2 == 0){

            if (intervals[i] > intervals[i + 1]){
                eps = eps + intervals[i] * (2 * mlt);
                eps = eps + intervals[(i + 1)] * (2 * mlt - 1);
            }
            else{
                eps = eps + intervals[i] * (2 * mlt - 1);
                eps = eps + intervals[(i + 1)] * (2 * mlt);
            }
        }
        else{
            eps = eps + intervals[i] * (2 * mlt - 1);
        }

        std::cout << "Case " << caseT << ": " << eps << "\n";

    }

    return 0;

}
