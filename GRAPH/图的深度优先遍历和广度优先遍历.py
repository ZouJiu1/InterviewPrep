# coding=gbk
class Graph(object):
    #邻接矩阵表示无向图
    def __init__(self, nodes, sides):
        self.sequence = {}
        self.side = []
        for node in nodes:
            for side in sides:
                u, v = side
                if node==u:
                    self.side.append(v)
                if node == v:
                    self.side.append(u)
            self.sequence[node] = self.side
            self.side = []

    def depth_first_traverse(self, node):
        '''
        深度优先遍历
        使用栈
        :param node:
        :return:
        '''
        queue, traversed = [], []
        queue.append(node)
        while queue:
            v = queue.pop()
            traversed.append(v)
            for i in self.sequence[v]:
                if i not in traversed and i not in queue:
                    queue.append(i)
        return traversed

    def breadth_first_search(self, node):
        '''
        广度优先遍历
        使用队列
        :param node:
        :return:
        '''
        queue, traversed = [], []
        queue.append(node)
        traversed.append(node)
        while queue:
            v = queue.pop(0)
            for i in self.sequence[v]:
                if i not in traversed:
                    queue.append(i)
                    traversed.append(i)
        return traversed

def main():
    nodes = [i+1 for i in range(9)]
    sides = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), \
             (5, 8), (3, 6), (3, 7), (6, 7), \
             (7, 9), (2, 8), (6, 8), (3, 9)]
    G = Graph(nodes, sides)
    print(G.depth_first_traverse(1))
    print(G.breadth_first_search(1))

if __name__=='__main__':
    main()