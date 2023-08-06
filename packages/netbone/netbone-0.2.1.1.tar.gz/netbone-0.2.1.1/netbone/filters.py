import math

import networkx as nx
from netbone.utils.utils import edge_properties
def boolean_filter(backbone, narrate=True, value=[]):
    if boolean_filter in backbone.filters():
        data = backbone.graph
        column = backbone.column
        if isinstance(data, nx.Graph):
            data = nx.to_pandas_edgelist(data)
        if narrate:
            backbone.narrate()
        return nx.from_pandas_edgelist(data[data[column] == True], edge_attr=edge_properties(data))
    print("The accepted filters for " + backbone.name + " are: " + ', '.join([fun.__name__ for fun in backbone.filters()]))

def threshold_filter(backbone, value, narrate=True , secondary_column = 'weight', secondary_column_ascending = False, **kwargs):
    data = backbone.graph
    column = backbone.column
    ascending = backbone.ascending

    if isinstance(data, nx.Graph):
        data = nx.to_pandas_edgelist(data)

    keys = kwargs.keys()
    if "value" in keys:
        value = kwargs["value"]
    if "secondary_column" in keys:
        secondary_column = kwargs['secondary_column']

    if threshold_filter in backbone.filters():
        if boolean_filter in backbone.filters():
            column = 'score'
        data = data.sort_values(by=[column, secondary_column], ascending=[ascending, secondary_column_ascending])

        if narrate:
            backbone.narrate()

        if column == "p_value":
            return nx.from_pandas_edgelist(data[data[column] < value], edge_attr=edge_properties(data))
        elif column == "score":
            return nx.from_pandas_edgelist(data[data[column] > value], edge_attr=edge_properties(data))
        else:
            print("Column name can not be " + column)

    print("The accepted filters for " + backbone.name + " are: " + ', '.join([fun.__name__ for fun in backbone.filters()]))




def fraction_filter(backbone, value, narrate=True, secondary_column='weight', secondary_column_ascending=False, **kwargs):
    data = backbone.graph
    column = backbone.column
    ascending = backbone.ascending

    if isinstance(data, nx.Graph):
        data = nx.to_pandas_edgelist(data)

    keys = kwargs.keys()
    if "value" in keys:
        value = kwargs["value"]
    if "secondary_column" in keys:
        secondary_column = kwargs['secondary_column']

    value = math.ceil(value * len(data))

    if fraction_filter in backbone.filters():
        if boolean_filter in backbone.filters():
            column = 'score'
        data = data.sort_values(by=[column, secondary_column], ascending=[ascending, secondary_column_ascending])

        if narrate:
            backbone.narrate()
        return nx.from_pandas_edgelist(data[:value], edge_attr=edge_properties(data))

    print("The accepted filters for " + backbone.name + " are: " + ', '.join([fun.__name__ for fun in backbone.filters()]))

    
    


