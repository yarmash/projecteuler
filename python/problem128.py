#!/usr/bin/env python

"""Problem 128: Hexagonal tile differences"""

from functools import lru_cache

from utils import is_prime

is_prime = lru_cache(maxsize=None)(is_prime)


def main():

    class Node:
        __slots__ = ('number', 'neighbours', 'pd')

        def __init__(self, number):
            self.number = number
            self.neighbours = []
            self.pd = 0

        def __repr__(self):
            return f'Node(number={self.number}, pd={self.pd})'

    target = 2000
    cnt = 1
    prev_layer = [Node(1)]
    next_num = 2
    nodes_per_layer = 6

    # keep adding layers, counting nodes for which PD(n) = 3
    while True:
        layer = [Node(next_num), Node(next_num + 1), Node(next_num + nodes_per_layer - 2), Node(next_num + nodes_per_layer - 1)]
        next_num += nodes_per_layer
        nodes_per_layer += 6

        for i, node in enumerate(layer):
            # only check the difference between the 1st and the last nodes in a ring
            if i == 0 and is_prime(layer[-1].number-node.number):
                layer[-1].pd += 1
                node.pd += 1

        for inner_node, neighbours in zip((prev_layer[0], prev_layer[-1]), ((layer[-1], layer[0], layer[1]), (layer[-2], layer[-1]))):
            for node in neighbours:
                if is_prime(node.number-inner_node.number):
                    node.pd += 1
                    inner_node.pd += 1

            if inner_node.pd == 3:
                cnt += 1
                if cnt == target:
                    return inner_node.number
        prev_layer = layer


if __name__ == "__main__":
    print(main())
