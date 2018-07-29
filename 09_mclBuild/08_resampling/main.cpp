#include <iostream>

using namespace std;

double w[] = { 0.6, 1.2, 2.4, 0.6, 1.2 };//You can also change this to a vector

//TODO: Define a  ComputeProb function and compute the Probabilities
double ComputeProb(double prob_i, double prob_sum){
	double alpha = prob_i/prob_sum;
	return alpha;
}

int main()
{
    //TODO: Print Probabilites each on a single line:
    //P1=Value
    //:
    //P5=Value

	//Create the vector total
	double sum = 0.0;
	for (int i=0; i<(sizeof(w))/(sizeof(w[0])); i++){
		sum += w[i];
	}

	for (int i=0; i<(sizeof(w))/(sizeof(w[0])); i++){
		cout << "P" << (i+1) << "=" << ComputeProb(w[i], sum) << endl;
	}

    return 0;
}
