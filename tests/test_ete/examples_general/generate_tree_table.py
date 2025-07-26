from eGPS4Py import Tree
def from_parent_child_table(parent_child_table):
    """Converts a parent-child table into an ETE Tree instance.

    :argument parent_child_table: a list of tuples containing parent-child
       relationships. For example: [("A", "B", 0.1), ("A", "C", 0.2), ("C",
       "D", 1), ("C", "E", 1.5)]. Where each tuple represents: [parent, child,
       child-parent-dist]

    :returns: A new Tree instance

    :example:

    >>> tree = Tree.from_parent_child_table([("A", "B", 0.1), ("A", "C", 0.2), ("C", "D", 1), ("C", "E", 1.5)])
    >>> print tree

    """

    def get_node(nodename, dist=None):
        if nodename not in nodes_by_name:
            nodes_by_name[nodename] = Tree(name=nodename, dist=dist)
        node = nodes_by_name[nodename]
        if dist is not None:
            node.dist = dist
        node.name = nodename
        return nodes_by_name[nodename]

    nodes_by_name = {}
    for columns in parent_child_table:
        if len(columns) == 3:
            parent_name, child_name, distance = columns
            dist = float(distance)
        else:
            parent_name, child_name = columns
            dist = None
        parent = get_node(parent_name)
        parent.add_child(get_node(child_name, dist=dist))

    root = parent.get_tree_root()
    return root
