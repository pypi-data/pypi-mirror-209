import networkx as nx
from pandas import DataFrame
from netbone.utils.utils import edge_properties

class Backbone:

    def __init__(self, graph, name, column, ascending, filters):
        if isinstance(graph, DataFrame):
            graph = nx.from_pandas_edgelist(graph, edge_attr=edge_properties(graph))

        self.graph = graph
        self.name = name
        self.column = column
        self.ascending = ascending
        self.compatible_filters = filters


    def to_dataframe(self):
        return nx.to_pandas_edgelist(self.graph)


    def narrate(self):
        match self.name:
            case "Disparity Filter":
                print(self.name)
            case "Enhanced Configuration Model Filter":
                print(self.name)
            case "Marginal Likelihood Filter":
                print(self.name)
            case "Locally Adaptive Network Sparsification Filter":
                print(self.name)
            case "Noise Corrected Filter":
                print(self.name)
            case 'High Salience Skeleton Filter':
                print(self.name)
            case 'Modularity Filter':
                print(self.name)
            case 'Ultrametric Distance Filter':
                print(self.name)
            case 'Maximum Spanning Tree':
                print(self.name)
            case 'Metric Distance Filter':
                print(self.name)
            case 'H-Backbone Filter':
                print(self.name)
            case 'Doubly Stochastic Filter':
                print(self.name)
            case 'Global Threshold Filter':
                print(self.name)
            case _:
                print("Citation here")


    def filters(self):
        return self.compatible_filters
        # match self.name:
        #     case "Disparity Filter" | 'Noise Corrected Filter' | "Enhanced Configuration Model Filter" | "Marginal Likelihood Filter" | 'Locally Adaptive Network Sparsification Filter' | 'Global Threshold Filter':
        #         return [fraction_filter, threshold_filter]
        #     case "H-Backbone Filter" | 'Metric Distance Filter' | 'Maximum Spanning Tree' | 'Ultrametric Distance Filter' | 'Modularity Filter':
        #         return [boolean_filter]
        #     case "Doubly Stochastic Filter" | "High Salience Skeleton Filter":
        #         return [boolean_filter, fraction_filter, threshold_filter]
        #     case _:
        #         print("Error " + self.name + " does not exist")
