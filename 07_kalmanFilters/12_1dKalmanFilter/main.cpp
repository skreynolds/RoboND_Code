#include <iostream>
#include <math.h>
#include <tuple>

using namespace std;

double new_mean, new_var;

tuple<double, double> measurement_update(double mean1, double var1, double mean2, double var2)
{
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2);
    new_var = 1 / (1 / var1 + 1 / var2);
    return make_tuple(new_mean, new_var);
}

tuple<double, double> state_prediction(double mean1, double var1, double mean2, double var2)
{
    new_mean = mean1 + mean2;
    new_var = var1 + var2;
    return make_tuple(new_mean, new_var);
}

int main()
{
    //Measurements and measurement variance
    double measurements[5] = { 5, 6, 7, 9, 10 };
    double measurement_sig = 4;

    //Motions and motion variance
    double motion[5] = { 1, 1, 2, 1, 1 };
    double motion_sig = 2;

    //Initial state
    double mu = 0;
    double sig = 1000;

    //Tuple output
    tuple<double, double> out_temp;

    //######TODO: Put your code here below this line######//

    //Determine the length of the input (note basic C array used)
    int length = sizeof(measurements)/sizeof(*measurements);

    // Loop through all the measurments
    for (int i = 0; i < length; i++){

        // Apply a measurment update
        out_temp = measurement_update(mu, sig, measurements[i], measurement_sig);
        mu = get<0>(out_temp);
        sig = get<1>(out_temp);
        printf("update:  [%f, %f]\n", mu, sig);

        // Apply a state prediction
        out_temp = state_prediction(mu, sig, motion[i], motion_sig);
        mu = get<0>(out_temp);
        sig = get<1>(out_temp);
        printf("predict: [%f, %f]\n", mu, sig);
    }

    return 0;
}