import numpy as np
from random import randrange
from scipy.spatial import distance as oklid
import copy

global RESULT
RESULT = []

def calculate_distance(partition, index):
    gec=[]
    for row in partition:
        gec.append(row[index])
    width = float(max(gec)-min(gec))
    return width

class VPTree(object):

    def __init__(self, points, k):

        self.mu = None
        self.point=points[:]
        self.allow=10
    
	def add_record(self, record):
        self.point.append(record)

a=10

def build_tree(partition, k, a):
    if a == 0:
        RESULT.append(partition)
        return

    vp = partition.point[randrange(len(partition.point))]
    distances = [oklid.euclidean(vp, p) for p in partition.point]
    partition.mu = np.median(distances)
    
	if partition.mu == 0:
        return
    lhs = VPTree([], k)
    rhs = VPTree([], k)
    left_points = []
    right_points = []

    for point, distance in zip(partition.point, distances):
        if distance >= partition.mu:
            rhs.add_record(point)
        else:
            lhs.add_record(point)

	x=k-1
    y=k*2
 
    if len(lhs.point) < k  or len(rhs.point) < k:
       a = 0
    if len(rhs.point) >= x and len(rhs.point) < y:
       a = 0

    build_tree(lhs, k, a)
    build_tree(rhs, k, a)

def run_canon(data,k):
    self = VPTree(data, k)
    build_tree(self, k, 10)

    dp = 0
    ncp = 0
    m = 0

    for partition in RESULT:
        points=partition.point
        rncp = 0
        for index in range(8):
            rncp += calculate_distance(points, index)
        rncp *= len(points)
        ncp += rncp
        dp += len(points) ** 2
        m = m + 1
    return (dp, m, ncp)
