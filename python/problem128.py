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
            return f'Node(number={self.number}, neighbours={self.neighbours}, pd={self.pd})'

        def add_neighbour(self, node):
            self.neighbours.append(node.number)
            node.neighbours.append(self.number)

    def gen_neighbours(layer):
        """Yield neighbours of each node in the inner layer."""
        if len(layer) == 6:  # all
            yield layer
        else:
            period = [3]+[2]*(len(layer)//6-2)
            yield layer[-1], layer[0], layer[1]
            i = 1
            for _ in range(len(layer)//6-2):
                yield layer[i:i+2]
                i += 1
            for _ in range(5):
                for n in period:
                    yield layer[i:i+n]
                    i += n-1

    target = 2000
    cnt = 0
    prev_layer = [Node(1)]
    next_num = 2
    nodes_per_layer = 6

    # keep adding layers, counting nodes for which PD(n) = 3
    while True:
        layer = [Node(num) for num in range(next_num, next_num + nodes_per_layer)]
        next_num += nodes_per_layer
        nodes_per_layer += 6

        for i, node in enumerate(layer):
            node.add_neighbour(layer[i-1])

            # only check the difference between the 1st and the last nodes in a ring
            if i == 0 and is_prime(layer[-1].number-node.number):
                layer[-1].pd += 1
                node.pd += 1

        for inner_node, neighbours in zip(prev_layer, gen_neighbours(layer)):
            for node in neighbours:
                inner_node.add_neighbour(node)

                if is_prime(node.number-inner_node.number):
                    node.pd += 1
                    inner_node.pd += 1

            if inner_node.pd == 3:
                cnt += 1
                print(inner_node, cnt)
                if cnt == target:
                    return inner_node.number
        prev_layer = layer


if __name__ == "__main__":
    print(main())
