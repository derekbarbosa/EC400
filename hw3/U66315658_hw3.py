## Derek Deoliveira Barbosa
## BU ID: U66315658
## Copyright 2022 dbarbosa@bu.edu



#class
class stateActionPair:
      def __init__(self, state,action,reward):
          self.state = state; ##char val
          self.action = action; ##int val
          self.reward = reward;

stateActionPairs = [stateActionPair('A',1,1),stateActionPair('A',2,0),stateActionPair('B',1,2)];
#returns reward based on state
def getRewards(stateValueItem):
    if(stateValueItem.state == 'A'):
        if(stateValueItem.action == stateActionPairs[0].action):
            return 1;
        if(stateValueItem.action == stateActionPairs[1].action):
            return 0;
    if(stateValueItem.state == 'B'):
        return 2;

#prints the path
def printPath(stateValueItem):
    if(stateValueItem.state == 'A'):
        if(stateValueItem.action == stateActionPairs[0].action):
            print("State: A \n Action: 1");
            print("\n\n");
        if(stateValueItem.action == stateActionPairs[1].action):
            print("State: A \n Action: 2");
            print("\n\n");
    if(stateValueItem.state == 'B'):
        print("State: B \n Action: 1");
        print("\n\n");

#finds the index based on curr state
def findStateValueIndex(stateValueItem):
    if(stateValueItem.state == 'A'):
        if(stateValueItem.action == stateActionPairs[0].action):
            stateValueIndex = 0;
        if(stateValueItem.action == stateActionPairs[1].action):
            stateValueIndex = 1;
    if(stateValueItem.state == 'B'):
        stateValueIndex = 2;

##this function finds the max reward based on current state we're in
def findOptimalReward(currState):
    if(currState != 'B'):
        return max([stateActionPair[0].action,stateActionPair[1].action]);
    else:
        return 2;
##this fn finds the optimal action based on curr_state
def findOptimalAction(currState,OptimalReward):
    if(currState != 'B'):
        if(OptimalReward == 1):
            return 1;
        else:
            return 2;
    else:
        return 1;

def calculateQ(qValArray,stateValueItem,time,bestReward,currReward):
    gamma = 0.5;

    #find the stateActionPair we are in
    stateValueIndex = findStateValueIndex(stateValueItem);

    prevQ = qValArray[stateValueIndex];
    nextQ = (prevQ + (1/time)*(currReward+(gamma*bestReward)-prevQ));
    qValArray[stateValueIndex] = nextQ;
    print(qValArray[stateValueIndex])


def main():
    qVals = [16,16,16];
    stateActionPath1 = [stateActionPairs[0],stateActionPairs[1]];
    path1Length = len(stateActionPath1);
    stateActionPath2 = [stateActionPairs[0],stateActionPairs[2],stateActionPairs[2]];
    path2Length = len(stateActionPath2);
    optimalStateActionPathLength = 1000;
    ##evaluate path1
    for i in range(path1Length):
        calculateQ(qVals,stateActionPath1[i],(i+1),stateActionPath1[i+1].reward,stateActionPath1[i].reward)

    ##evaluate path2
    for i in range(path2Length):
        calculateQ(qVals,stateActionPath2[i],(i+1),stateActionPath2[i+1].reward,stateActionPath2[i].reward)
    
    bestReward = findOptimalReward(stateActionPath1[i].state);
    bestAction = findOptimalAction(stateActionPath1[i].state,bestReward);
    currReward = getRewards(stateActionPath1[i].state);
    ##evaluate optimal path
    ##assume we start in state A and collect our first reward of 1

main();