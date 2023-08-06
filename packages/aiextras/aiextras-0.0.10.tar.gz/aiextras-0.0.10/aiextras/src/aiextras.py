program = '''# for creating Bayesian Belief Networks (BBN)
import pandas as pd
from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
# the guest's intitial door selection is completely random
guest = BbnNode(Variable(0, 'guest', ['A', 'B', 'C']), [1.0/3, 1.0/3, 1.0/3])
# the door the prize is behind is also completely random
prize = BbnNode(Variable(1, 'prize', ['A', 'B', 'C']), [1.0/3, 1.0/3, 1.0/3])
# monty is dependent on both guest and prize
monty = BbnNode(Variable(2, 'monty', ['A', 'B', 'C']), [0, 0.5, 0.5,  # A, A
                                                        0, 0, 1,  # A, B
                                                        0, 1, 0,  # A, C
                                                        0, 0, 1,  # B, A
                                                        0.5, 0, 0.5,  # B, B
                                                        1, 0, 0,  # B, C
                                                        0, 1, 0,  # C, A
                                                        1, 0, 0,  # C, B
                                                        0.5, 0.5, 0  # C, C
                                                        ])

bbn = Bbn() \
    .add_node(guest) \
    .add_node(prize) \
    .add_node(monty) \
    .add_edge(Edge(guest, monty, EdgeType.DIRECTED)) \
    .add_edge(Edge(prize, monty, EdgeType.DIRECTED))

# Convert the BBN to a join tree
join_tree = InferenceController.apply(bbn)

# Define a function for printing marginal probabilities


def print_probs():
    for node in join_tree.get_bbn_nodes():
        potential = join_tree.get_bbn_potential(node)
        print("Node:", node)
        print("Values:")
        print(potential)
        print('----------------')


print_probs()
'''
