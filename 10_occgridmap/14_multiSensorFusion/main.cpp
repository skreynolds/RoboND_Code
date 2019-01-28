#include <iostream>
#include <math.h>

const int mapWidth =  2;
const int mapHeight = 2;

void sensorFusion(double m1[][mapWidth], double m2[][mapWidth])
{
    //*#############TODO: Code the Sensor Fusion Function############*//
    // Fuse the measurments of the two maps and print the resulting
    //map in a matrix form:
    //a  b
    //c  d

	//Initialise resulting map
	double res_m[mapHeight][mapWidth];

	//Calculate cell values for resulting map
	for (int i=0; i < mapHeight; i++){
		for (int j=0; j < mapWidth; j++){
			res_m[i][j] = 1 - (1 - m1[i][j]) * (1 - m2[i][j]);
		}
	}

	//Print cell values for resulting map
	for (int i=0; i < mapHeight; i++){
		for (int j=0; j < mapWidth; j++){
			std::cout<<res_m[i][j]<<" ";
		}
		std::cout<<std::endl;
	}

}

int main()
{

    double m1[mapHeight][mapWidth] = { { 0.9, 0.6 }, { 0.1, 0.5 } };
    double m2[mapHeight][mapWidth] = { { 0.3, 0.4 }, { 0.4, 0.3 } };
    sensorFusion(m1, m2);

    return 0;
}
