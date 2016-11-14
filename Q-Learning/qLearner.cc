#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include "mdp-simulation.h"
#include <time.h>
#include <fstream>
using namespace std;


vector<vector<float> > QLearner(int nActions, int nStates)
{

	float gamma = 0.9;
	vector<vector<float> > QTable(nStates, vector<float>(nActions));
	vector<vector<float> > nVisited(nStates, vector<float>(nActions));
	int ep = 0;
	ofstream myFile;
    myFile.open("rewards.txt");
    float epsilon, alpha;
    int nEpisodes = 100000;

	while(ep < nEpisodes)
	{
		int x = rand() % MAX_GRID;
		int y = rand() % MAX_GRID;
		int initID = MAX_GRID * x + y;
		State initState = State(x,y);
		double cumReward = 0;
		int currentID = initID;
		State currentState = initState;
		epsilon = 1.0*(nEpisodes - ep)/(1.0*nEpisodes);
		int select;
		int nIter = 0;	
	    while (nIter < 100)
	    {
	    	//cout<<nIter<<endl;
	    	double randomE = (double)rand()/((double)RAND_MAX);
	    	if (randomE < epsilon)
	    	{
	    		select = rand() % 4;
	    	}

	    	else
	    	{
	    		select = max_element(QTable[currentID].begin(), QTable[currentID].end()) - QTable[currentID].begin();
	    	}

	    	alpha = 1.0/(1.0+nVisited[currentID][select]);
	    	cumReward = cumReward + my_reward(currentState);
	    	State next = my_next_state(currentState, Action(select));
	    	int nextID = MAX_GRID * next.x + next.y;
	    	//QTable[currentID][select] = my_reward(next) + (gamma * (*max_element(QTable[nextID].begin(), QTable[nextID].end())));
	    	double value = my_reward(currentState) + (gamma * (*max_element(QTable[nextID].begin(), QTable[nextID].end())));	    	
	    	nVisited[currentID][select] ++;
	    	QTable[currentID][select] = (1.0-alpha)*QTable[currentID][select]  + (alpha*value);
	    	
	    	currentID = nextID;
	    	currentState = next;
	    	nIter++;
	    	 

	    }

	myFile<<cumReward<<"\n";
	ep++;
	}
/*  PRINT Q TABLE
    for (int i=0; i<nStates; i++)
    {
    	for(int j=0; j<nActions; j++)
    	{
    		cout << " ";
    		cout << QTable[i][j];

    	}
    	cout << endl;
    }
*/
    myFile.close();
    return QTable;
}

vector<vector<Action> > generatePolicy(vector<vector<float> > QTable)
{
	vector<vector<Action> > optimal(MAX_GRID, vector<Action>(MAX_GRID));
	for (int i = 0; i < QTable.size(); i++)
	{
		int x = i/MAX_GRID;
		int y = i%MAX_GRID;
		int select = max_element(QTable[i].begin(), QTable[i].end()) - QTable[i].begin();
		optimal[x][y] = Action(select);

	}

	cout << "OPTIMAL POLICY IS:" << endl;

	for (int i = 0; i < MAX_GRID; i++)
    {
    	for (int j = 0; j < MAX_GRID; j++)
    	{
	      if (optimal[i][j] == 0)
	        cout<<"N"<<"  ";
	      else if (optimal[i][j] == 1)
	        cout<<"S"<<"  ";
	      else if (optimal[i][j] == 2)
	        cout<<"E"<<"  ";
	      else if (optimal[i][j] == 3)
	        cout<<"W"<<"  ";
    	}
    cout<<endl;
    }
    return optimal;
}


int main (void)
{
  srand(time(NULL));
  int nActions = 4;
  int nStates = MAX_GRID * MAX_GRID;
  vector<vector<float> > QTable = QLearner(nActions, nStates);
  generatePolicy(QTable);
  return 0;
}
