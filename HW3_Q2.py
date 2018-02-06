class Node: # this is a parent class/ base class
    """base class"""
    def __init__(self, name, cost, utility): # the common attributes of the two different classes below
        self.name = name
        self.cost = cost
        self.utility= utility

    def get_expected_cost(self): # all subclass of this base class will have this function even if the implemntation may be different
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")# this is an abstract function that needs to be over-written in the derived nodes
                                # need to implement get_expected_cost in ALL derived function. It could be null, but good practice to write it out still.

    def get_health_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class ChanceNode(Node): # class - what the object is going to do. Objects (food) are the products of the class (recipe)
    def __init__(self, name, cost, utility, probs, future_nodes): # the first step of the recipe by implementing the init function
        Node.__init__(self,name,cost,utility)
        """
        :param name: name of this chance node
        :param probs: probabilities of visiting future nodes
        :param future_nodes: a list of future node objects
        :param utility: health utility
        """
        self.probs = probs
        self.future_nodes = future_nodes # the immediate future node

    def get_expected_cost(self):
        """the cost of this chance node"""

        exp_cost = self.cost # expected cost of this node including the cost of visiting this node
        i = 0 # index to iterate over probabilities
        for thisNode in self.future_nodes: # for every node that is in the future node list, go over it
            exp_cost += self.probs[i] * thisNode.get_expected_cost()  # every node has this function, as long as within the child class.
            i += 1  # we need to increment i to go over the probabilities

        return exp_cost

    def get_health_utility(self):
        """the utility of this chance node"""

        exp_utility = self.utility  # expected cost of this node including the cost of visiting this node
        i = 0  # index to iterate over probabilities
        for thisNode in self.future_nodes:  # for every node that is in the future node list, go over it
            exp_utility += self.probs[i] * thisNode.get_health_utility()  # every node has this function, as long as within the child class.
            i += 1  # we need to increment i to go over the probabilities

        return exp_utility


class TerminalNode(Node): #info required: cost of each terminal node
    def __init__(self, name, cost, utility):
        Node.__init__(self,name,cost, utility)

    def get_expected_cost(self):
        """the cost of this terminal node"""

        return self.cost # the only purpose of this class to let the program know if this is the terminal node or if there's sth after that node

    def get_health_utility(self):
        """the health utility of this terminal node"""

        return self.utility

class DecisionNode(Node):
    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes #list of future objects

    def get_expected_cost(self): #expected costs of attached future nodes
        """return: the expected cost of associated future nodes"""
        outcomes1 = dict() # dictionary to store expected cost of future nodes
        for thisNode in self.futureNodes:
            outcomes1[thisNode.name] = thisNode.get_expected_cost() #dictionary also returns the key.

        return outcomes1

    def get_health_utility(self):
        """the expected utility of associated future nodes"""
        outcomes2=dict()
        for thisNode in self.futureNodes:
            outcomes2[thisNode.name] = thisNode.get_health_utility ()

        return outcomes2


# create five terminal nodes
T1 = TerminalNode("T1", cost = 10, utility = 0.9)
T2 = TerminalNode("T2", cost = 20, utility = 0.8)
T3 = TerminalNode("T3", cost = 30, utility = 0.7)
T4 = TerminalNode("T4", cost = 40, utility = 0.6)
T5 = TerminalNode("T5", cost = 50, utility = 0.5)

# create three chance nodes
C2 = ChanceNode("C2", cost=35, utility=0, probs=[0.7, 0.3], future_nodes= [T1, T2])
C1 = ChanceNode("C1", cost=25, utility=0, probs=[0.2, 0.8], future_nodes= [C2, T3])
C3 = ChanceNode("C3", cost=45, utility=0, probs=[0.1, 0.9], future_nodes= [T4, T5])

#create one decision node
D1 = DecisionNode("D1",cost=0,utility=0, future_nodes= [C1, C3])

#print the expected cost and health utility of decision node D1
print('Expected cost:', D1.get_expected_cost())
print('Health utility:', D1.get_health_utility())
