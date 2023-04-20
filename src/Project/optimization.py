import clustering
import creation
import globals
import query
import utils
import math


def sway(data):
    """
    Recursively returns the best half of the dictionary of data.

    Args:
        data (dict): Dictionary of data to return the best half of.

    Returns:
        dict: Dictionary of remaining DATA to recursively return the best half of.
    """

    def worker(rows, worse, evals0, above=[]):
        if len(rows) <= len(data["rows"]) ** globals.Is["min"]:
            return rows, utils.many(worse, globals.Is["rest"] * len(rows)), evals0
        else:
            l, r, A, B, _, evals = clustering.half(data, rows, None, above)

            if query.better(data, B, A):
                l, r, A, B = r, l, B, A

            def function(row):
                return worse.append(row)

            list(map(function, r))

            return worker(l, worse, evals + evals0, A)

    best, rest, evals = worker(data["rows"], [], 0)

    return creation.DATA(data, best), creation.DATA(data, rest), evals

def agglomerativeHierarchalClustering(data, k):
    clusters = {}

    for row in data["rows"]:
        clusters[len(clusters)] = [row]
    
    while len(clusters) > k:
        closestClusters = findClosestClusters(data, clusters)
        clusters = mergeClusters(*closestClusters, clusters)
    
    return clusters

def mergeClusters(cIiD, cJiD, clusters):
    newClusters = {0: clusters[cIiD] + clusters[cJiD]}

    for clusterID in clusters.keys():
        if (clusterID == cIiD) | (clusterID == cJiD):
            continue
        newClusters[len(newClusters.keys())] = clusters[clusterID]
    return newClusters

def findClosestClusters(data, clusters):
    minDist = math.inf
    closestClusters = None

    clusterIDs = list(clusters.keys())

    for i, clusterI in enumerate(clusterIDs[:-1]):
        for j, clusterJ in enumerate(clusterIDs[i+1:]):
            dist = clusterMetric(data, clusters[clusterI], clusters[clusterJ])
            if dist < minDist:
                minDist, closestClusters = dist, (clusterI, clusterJ)
    return closestClusters

def clusterMetric(data, cI, cJ):
    # distances = [query.dist(data, rI, rJ) for rI in cI for rJ in cJ]
    # return sum(distances) / len(distances)
    # return max([query.dist(data, rI, rJ) for rI in cI for rJ in cJ])
    return min([query.dist(data, rI, rJ) for rI in cI for rJ in cJ])

def sway2(data, k = 3):
    k = globals.Is["k"]
    clusters = agglomerativeHierarchalClustering(data, k)
    best, rest, evals = bestCluster(data, clusters)
    rest = utils.many(rest, globals.Is["rest"] * len(best))
    return creation.DATA(data, best), creation.DATA(data, rest), evals

# def dbscan2(data, eps, minPts):
#     labels = [0]*len(data["rows"])

#     cID = 0

#     for i in range(0, len(data["rows"])):
#         if not (labels[i] == 0):
#             continue
#         neighbors = regionQuery(data, i, eps)

#         if len(neighbors) < minPts:
#             labels[i] = -1
#         else:
#             cID += 1
#             growCluster(data, labels, i, neighbors, cID, eps, minPts)

#     clusters = {}
#     noise = []

#     for j in range(0, len(labels)):
#         if labels[j] == -1:
#             noise.append(data["rows"][j])
#         else:
#             if labels[j] not in clusters:
#                 clusters[labels[j]] = [data["rows"][j]]
#             else:
#                 clusters[labels[j]].append(data["rows"][j])
    
#     return clusters, noise

# def growCluster(data, labels, i, neighbors, c, eps, minPts):
#     labels[i] = c

#     j = 0

#     while j < len(neighbors):
#         iN = neighbors[j]

#         if labels[iN] == -1:
#             labels[iN] = c
#         elif labels[iN] == 0:
#             labels[iN] = c

#             iNneighbors = regionQuery(data, iN, eps)

#             if len(iNneighbors) >= minPts:
#                 neighbors = neighbors + iNneighbors
#         j += 1

# def regionQuery(data, i, eps):
#     neighbors = []

#     for iN in range(0, len(data["rows"])):
#         if query.dist(data, data["rows"][i], data["rows"][iN]) < eps:
#             neighbors.append(iN)
    
#     return neighbors

# def sway2(data, eps= 0.3, minPoints= 4):
#     eps = globals.Is["eps"]
#     minPoints = globals.Is["minPts"]
#     clusters, noise = dbscan2(data, eps, minPoints)
#     best, rest, evals = bestCluster(data, clusters)
#     rest = utils.many(rest, globals.Is["rest"] * len(best))
#     return creation.DATA(data, best), creation.DATA(data, rest), evals

def bestCluster(data, clusters):
    bestCluster = None
    bestIndex = -1
    bestScore = float('-inf')
    evals = 0

    for n, cluster in clusters.items():
        score, evalsOne = computeScore(data, cluster)
        evals += 1
        if score > bestScore:
            bestCluster = cluster
            bestScore = score
            bestIndex = n

    rest = []

    for n, cluster in clusters.items():
        if (n != bestIndex):
            for c in cluster:
                rest.append(c)
    return bestCluster, rest, evals

def computeScore(data, cluster):
    score = 0
    count = 0
    for i, rowOne in enumerate(cluster):
        for j, rowTwo in enumerate(cluster):
            if i < j:
                count += 1
                if query.better(data, rowOne, rowTwo):
                    score += 1
                else:
                    score -= 1
    return score, count
