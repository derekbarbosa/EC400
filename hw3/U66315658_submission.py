class stateActionPair:
      def __init__(self,state,action,reward):
          self.state = state; ##char val
          self.action = action; ##int val
          self.reward = reward;

def findStateValueIndex(stateValueItem):
    if(stateValueItem.state == 'A'):
        if(stateValueItem.action == 1):
            return 0;
        if(stateValueItem.action == 2):
            return 1;
    if(stateValueItem.state == 'B'):
        return 2;

def findOptimalReward(currPair):
    if(currPair != 'B'):
        return max(0,1);
    else:
        return 2;

def findOptimalAction(currPair,OptimalReward):
    if(currPair != 'B'):
        if(OptimalReward == 1):
            return 1;
        else:
            return 2;
    else:
        return 1;

def findNextState(currPair,action):
    if(currPair != 'B'):
        if(action == 1):
            return 'A';
        else:
            return 'B';
    else:
        return 'B';
def calculateQ(qValArray,pairItem,time,bestReward,currReward):
    gamma = 0.5;

    #find the stateActionPair we are in
    stateValueIndex = findStateValueIndex(pairItem)                                                                         

    prevQ = qValArray[stateValueIndex];
    nextQ = (prevQ + ((1/time) * (currReward + (gamma*bestReward) - prevQ)));
    qValArray[stateValueIndex] = nextQ;
    print(qValArray)

def main():
    qVals = [16,16,16]; 
    stateActionPairs = [stateActionPair('A',1,1),stateActionPair('A',2,0),stateActionPair('B',1,2)];
    stateActionPath1 = [stateActionPairs[0],stateActionPairs[1],stateActionPairs[2],stateActionPair(0,0,0)];
    path1Length = len(stateActionPath1)-1;


    ##evaluate path1
    for i in (range(path1Length)):
        idx = findStateValueIndex(stateActionPath1[i])
        calculateQ(qVals,stateActionPath1[i],(i+1),qVals[idx],stateActionPath1[i].reward)
    
    print("TWO ITERATIONS FOR PATH 1 COMPLETED")
    print("STARTING PATH 2\n")
    
    qVals = [16,16,16]; 
    for i in range(100):
        currPair = stateActionPairs[0]; #start at state A
        currReward = currPair.reward;
        idx = findStateValueIndex(currPair);

        bestReward = findOptimalReward(currPair.state);
        bestAction = findOptimalAction(currPair.state,bestReward);
        nextState = findNextState(currPair,bestAction);

        calculateQ(qVals,currPair,(i+1),qVals[idx],currReward)
        currPair = nextState;
        

main();