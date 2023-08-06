import networkx as nx
from pandas import DataFrame
from networkx import Graph,to_pandas_edgelist
from netbone.utils.utils import edge_properties
from netbone.backbone import Backbone
from netbone.filters import fraction_filter, threshold_filter
def global_threshold(data):

    if isinstance(data, DataFrame):
        table = data.copy()
    elif isinstance(data, Graph):
        table = to_pandas_edgelist(data)
        is_graph=True
    else:
        print("data should be a panads dataframe or nx graph")
        return

    table['score'] = table['weight']

    g = nx.from_pandas_edgelist(table, edge_attr=edge_properties(table))
    # average = table['weight'].mean()
    # for u,v in g.edges():
    #     if g[u][v]['score']>=average:
    #         g[u][v]['global_threshold'] = True
    #     else:
    #         g[u][v]['global_threshold'] = False
    # return Backbone(g, name="Global Threshold Filter", column="global_threshold", ascending=False, filters=[boolean_filter, fraction_filter, threshold_filter])
    return Backbone(g, name="Global Threshold Filter", column="score", ascending=False, filters=[fraction_filter, threshold_filter])