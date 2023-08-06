
"""
NetBone - Easy Backbone extraction library
==================

A Library that simplifies Extracting backbones from networks.
and graphs.
"""

from netbone.statistical.disparity import disparity
from netbone.structural.h_backbone import h_backbone
from netbone.statistical.noise_corrected import noise_corrected
from netbone.structural.doubly_stochastic import doubly_stochastic
from netbone.structural.high_salience_skeleton import high_salience_skeleton
from netbone.statistical.marginal_likelihood import MLF
from netbone.statistical.lans import lans
from netbone.structural.ultrametric_distance_backbone import ultrametric_distance_backbone
from netbone.structural.metric_distance_backbone import metric_distance_backbone
from netbone.statistical.global_threshold import global_threshold
from netbone.structural.modulairy_backbone import modularity_backbone
from netbone.structural.maximum_spanning_tree import maximum_spanning_tree
from netbone.filters import threshold_filter, fraction_filter
from netbone import compare
from netbone import filters
from netbone import visualize
from netbone.backbone import Backbone
try:
    from netbone.statistical.maxent_graph.ecm_main import ecm
except ImportError:
    print("Can't load ECM Model in windows, try using it on linux")


def marginal_likelihood(data):
    data = data.copy()
    mlf = MLF(directed=False)
    return Backbone(mlf.fit_transform(data), name="Marginal Likelihood Filter", column="p_value", ascending=True, filters=[threshold_filter, fraction_filter])




# logger = logging.getLogger()
# logger.setLevel('DEBUG')



