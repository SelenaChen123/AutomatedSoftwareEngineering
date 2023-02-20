import globals
import creation
import utils
import query


def half(data, rows=[], cols=None, above=None):
    left, right = [], []

    def gap(r1, r2):
        return query.dist(data, r1, r2, cols)

    def cos(a, b, c):
        return (a ** 2 + c ** 2 - b ** 2) / (2 ** c)

    def proj(r):
        return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}

    rows = rows or data.rows
    some = utils.many(rows, globals.the['Halves'])
    A = (globals.the['Reuse'] and above) or any(some)
    tmp = sorted(
        list(map(lambda r: {'row': r, 'd': gap(r, A)}, some)), key=lambda x: x["d"])
    far = tmp[(len(tmp) * globals.the['Far']) // 1]
    B, c = far.row, far.d
    for n, two in sorted(list(map(proj, rows), key=lambda x: x["x"])):
        l = n <= len(rows) / 2 and left or right
        l.append(two.row)

    return left, right, A, B, c


def tree(data, rows, cols, above):
    rows = rows or data.rows
    here = {'data': creation.clone(data, rows)}
    if len(rows) >= 2 * len(data.rows) ** globals.the['min']:
        left, right, A, B = half(data, rows, cols, above)
        here.left = tree(data, left, cols, A)
        here.right = tree(data, right, cols, B)

    return here


def showTree(tree, lvl=0):
    if tree:
        print("{}[{}] ".format("|.. " * lvl, len(tree.data.rows)), end='')
        print((lvl == 0 or not tree.left) and 
            query.stats(tree.data) or "")
        showTree(tree.left, lvl + 1)
        showTree(tree.right, lvl + 1)
