#include <iostream>
#include <math.h>
#include <vector>
//using namespace std;

// Sensor characteristic: Min and Max ranges of the beams
double Zmax = 5000, Zmin = 170;
// Defining free cells(lfree), occupied cells(locc), unknown cells(l0) log odds values
double l0 = 0, locc = 0.4, lfree = -0.4;
// Grid dimensions
double gridWidth = 100, gridHeight = 100;
// Map dimensions
double mapWidth = 30000, mapHeight = 15000;
// Robot size with respect to the map
double robotXOffset = mapWidth / 5, robotYOffset = mapHeight / 3;
// Defining an l vector to store the log odds values of each cell
std::vector< std::vector<double> > l(mapWidth/gridWidth, std::vector<double>(mapHeight/gridHeight));


double inverseSensorModel(double x, double y, double theta, double xi, double yi, double sensorData[])
{
    // You will be coding this section in the upcoming concept!
    return 0.4;
}


void occupancyGridMapping(double Robotx, double Roboty, double Robottheta, double sensorData[])
{
    //1 - TODO: Generate a grid (size 300x150) and then loop through all the cells

	//Specify the number of rows and columns in the grid
	int rows = 300;
	int columns = 150;

	//Specify the grid (300x150)
	std::vector<std::vector<double>> grid;
	grid.resize(rows, std::vector<double>(columns, 0));

	//Cycle through the grid and update the binary bayes filter
	for (int x=0; x<rows; x++){
		for (int y=0; y<columns; y++){

			//2- TODO: Compute the center of mass of each cell xi and yi

			//Determine the the cell centroid
			double xi = x * gridWidth + gridWidth / 2 - robotXOffset;
			double yi = -(y * gridHeight + gridHeight / 2) + robotYOffset;

			//3- TODO: Check if each cell falls under the perceptual field of the measurements

			//Calculate the distance between the current cell and the robot
			double d = sqrt(pow(Robotx - xi, 2) + pow(Roboty - yi, 2));

			//Update the binary bayes filter if the distance to the cell is less than the max dist of sensor
			if (d <= Zmax){
				l[x][y] += inverseSensorModel(Robotx, Roboty, Robottheta, xi, yi, sensorData) - l0;
			}

		}
	}

}


int main(void)
{
    double timeStamp;
    double measurementData[8];
    double robotX, robotY, robotTheta;

    FILE* posesFile = fopen("poses.txt", "r");
    FILE* measurementFile = fopen("measurement.txt", "r");

    // Scanning the files and retrieving measurement and poses at each timestamp
    while (fscanf(posesFile, "%lf %lf %lf %lf", &timeStamp, &robotX, &robotY, &robotTheta) != EOF) {

    	fscanf(measurementFile, "%lf", &timeStamp);

        for (int i = 0; i < 8; i++) {
            fscanf(measurementFile, "%lf", &measurementData[i]);
        }

        occupancyGridMapping(robotX, robotY, (robotTheta / 10) * (M_PI / 180), measurementData);

    }

    // Displaying the map
    for (int x = 0; x < mapWidth / gridWidth; x++) {
        for (int y = 0; y < mapHeight / gridHeight; y++) {
            std::cout << l[x][y] << " ";
        }
    }

    return 0;
}
