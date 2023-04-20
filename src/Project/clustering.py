import math

import creation
import globals
import query
import utils
import random
from query import norm
import numpy as np

def half(data, rows=[], cols={}, above=[]):
    """
    Divides data using 2 far points.

    Args:
        data (dict): Data to be halved.
        rows (list, optional): List of rows to be halved. Defaults to data["rows"].
        cols (dict, optional): Factory that manages rows. Defaults to {}.
        above (list, optional): Single chosen row. Defaults to [].

    Returns:
        list: Left half of the rows.
        list: Right half of the rows.
        list: Single chosen row to calculate the distance from.
        row: Single chosen row around A to calculate the distance from.
        float: Distance from A to B.
        int: 1 if child splits reuse a parent pole and above exists, 2 otherwise.
    """

    left = []
    right = []
    def cos(a, b, c):
        return (a ** 2 + c ** 2 - b ** 2) / (2 * c)

    def proj(r):
        return {"row": r, "x": cos(query.dist(data, r, A, cols), query.dist(data, r, B, cols), c)}

    rows = rows or data["rows"]
    some = utils.many(rows, globals.Is["Halves"])
    A = above if (globals.Is["Reuse"] and above) else utils.any(some)
    tmp = sorted(list(map(lambda r: {"row": r, "d": query.dist(
        data, r, A, cols)}, some)), key=lambda x: x["d"])
    far = tmp[math.floor((len(tmp) - 1) * globals.Is["Far"])]
    B = far["row"]
    c = far["d"]

    for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
        left.append(two["row"]) if n <= len(rows) / \
            2 - 1 else right.append(two["row"])

    return left, right, A, B, c, (1 if (globals.Is["Reuse"] and above) else 2)

def half2(data, rows=[], cols={}, above=[]):
    
    rows = rows or data["rows"]
    some = utils.many(rows, globals.Is["Halves"])
    above = above if (globals.Is["Reuse"] and above) else utils.any(some)
    k = 2  
    max_iterations = 1000

    centroids = random.sample(rows, k)

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        # print(centroids)
        for row in rows:
            distances = [query.dist(data, row, centroid, cols) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(row)

        new_centroids = []
        if len(clusters[0])==0 or len(clusters[1])==0:
            break
        for cluster in clusters:
            # print(len(cluster))
            # print([row[4] for row in cluster])
            # print(cluster)
            cluster_mean = []
            int_rows = []
            for row in range(len(cluster)):
                flag = 0
                for col in range(len(data["cols"]["all"])):
                    if isinstance(cluster[row][col] , int)==False and isinstance(cluster[row][col] , float)==False:
                        # print(cluster[row][col])
                        flag = 1
                        break
                if flag == 0:
                    int_rows.append(row)
            # print("psdfwefwcwfwefwefwe", int_rows)
            # print("fwergfeg ",non_int_rows)
            for col in range(len(data["cols"]["all"])):
                s = 0 
                for row in int_rows:
                    # if row not in non_int_rows:
                        s+=cluster[row][col]
                s /= len(cluster)
                cluster_mean.append(s)
            # cluster_mean = [sum([row[col] for row in cluster]) / len(cluster) for col in range(5)]
            new_centroids.append(cluster_mean)

        if new_centroids == centroids:
            break
        centroids = new_centroids

    above_cluster = None
    # print(len(clusters[0]), len(clusters[1]))
    for i, cluster in enumerate(clusters):
        if above in cluster:
            above_cluster = i
            break
    print("above",above_cluster)
    
    farthest_distance = 0
    farthest_row = None
    for row in clusters[above_cluster]:
        distance = query.dist(data, row, above, cols)
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_row = row
    # print(above_cluster)
    
    left_half = []
    right_half = []
    # left_half = (clusters[0])
    # right_half =(clusters[1])
    for i, cluster in enumerate(clusters):
        # if i == above_cluster:
        #     continue
        if len(left_half) <= len(rows) / 2 -1:
            left_half.extend(cluster)
        else:
            right_half.extend(cluster)

    print("Left Half",len(left_half))
    print("Right Half", len(right_half))
    return left_half, right_half, above, farthest_row, farthest_distance, (1 if above else 2)

    # rows = rows or data["rows"]
    # above = above or utils.any(rows)

    # def proj(r):
    #     return {"row": r, "dist": query.dist(data, r, above, cols)}

    # # Project the rows onto a line using the chosen row as the origin
    # proj_rows = list(map(proj, rows))

    # # Sort the rows by their projection distance
    # sorted_rows = sorted(proj_rows, key=lambda r: r["dist"])

    # # Split the sorted rows into two halves
    # midpoint = len(sorted_rows) // 2
    # left_half = [r["row"] for r in sorted_rows[:midpoint]]
    # right_half = [r["row"] for r in sorted_rows[midpoint:]]

    # # Determine the farthest point from the above row
    # farthest_row = max(left_half + right_half, key=lambda row: query.dist(data, row, above, cols))
    # farthest_distance = query.dist(data, farthest_row, above, cols)

    # return left_half, right_half, above, farthest_row, farthest_distance, (1 if above else 2)



def tree(data, rows=[], cols={}, above=[]):
    """
    Recursively halves rows.

    Args:
        data (dict): Data to be halved.
        rows (list, optional): List of rows to be halved. Defaults to data["rows"].
        cols (dict, optional): Factory that manages rows. Defaults to data["cols"]["x"].
        above (list, optional): Single chosen row. Defaults to [].

    Returns:
        dict: Dictionary of remaining data to be recursively halved.
    """

    rows = rows or data["rows"]
    here = {"data": creation.DATA(data, rows)}

    if len(rows) >= 2 * len(data["rows"]) ** globals.Is["min"]:
        left, right, A, B, _, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)

    return here


def showTree(tree, lvl=0):
    """
    Prints the tree version of the data.

    Args:
        tree (dict): Tree of data to be printed.
        lvl (int, optional): Current tree level. Defaults to 0.
    """

    if tree:
        print("{}[{}] ".format("|.. " * lvl, len(tree["data"]["rows"])), end="")
        print(query.stats(tree["data"]) if (
            lvl == 0 or "left" not in tree) else "")

        if "left" in tree:
            showTree(tree["left"], lvl + 1)

        if "right" in tree:
            showTree(tree["right"], lvl + 1)
