#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Print 2D vectors coordinate values
void print2DVector(vector<vector<int> > vec)
{
     // Sorting the vector for grading purpose
    sort(vec.begin(), vec.end());
    for (int i = 0; i < vec.size(); ++i) {
        for (int j = 0; j < vec[0].size(); ++j) {
                cout << vec[i][j] << "  ";
        }
        cout << endl;
    }
}

// ***TODO: Check for duplicate coordinates inside a 2D vector and delete them*** //
vector<vector<int> > delete_duplicate(vector<vector<int> > C){

	// Initialise empty return vector
	vector< vector<int> > return_C;

	// Parse through all of the points
	for (int i=0; i<C.size(); i++){

		// Initialise duplicate indicator to false
		bool duplicate = false;

		// Cycle through remaining points
		for (int ii=(i+1); ii<C.size(); ii++){
			if (C[i][0] == C[ii][0] && C[i][1] == C[ii][1]){
				duplicate = true;
				break;
			}
		}

		// Add point to return vector if not a duplicate
		if (not duplicate){
			vector<int> C_j = {C[i][0], C[i][1]};
			return_C.push_back(C_j);
		}

	}

	return return_C;

}

// ***TODO: Compute the Minkowski Sum of two vectors***//
vector<vector<int> > minkowski_sum(vector<vector<int> > A, vector<vector<int> > B){

	// Create final 2D vector to be returned
	vector< vector<int> > C(A.size()*B.size(), vector<int> (2,0));

	// Add (and subtract) vectors to the coordinates of the other shape
	int pos = 0; // Initialise result vector position
	for (int i=0; i<A.size(); i++){
		for (int j=0; j<A.size(); j++){
			C[pos][0] = A[i][0] + B[j][0];
			C[pos][1] = A[i][1] + B[j][1];

			pos += 1; // Increment position by 1
		}
	}

	// Delete duplicated points
    C = delete_duplicate(C);
    return C;
}

int main(){
    // ***TODO: Define the vertices of triangle A and B using 2D vectors*** //
	vector< vector<int> > A = {{0, 1},
							   {1, 0},
							   {0,-1}};

	vector< vector<int> > B = {{1, 1},
							   {1,-1},
							   {0, 0}};

    // Compute the minkowski sum of triangle A and B
    vector<vector<int> > C;
    C = minkowski_sum(A, B);

    // Print the resulting vector
    print2DVector(C);

    return 0;
}
