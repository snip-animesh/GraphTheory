class Graph:
    def __init__(self, Nodes,is_directed=False):
        self.nodes=Nodes
        self.adj_lst={}
        self.is_directed=is_directed
        for node in self.nodes:
            self.adj_lst[node]=[]

    def printing_adj_lst(self):
        for node in self.nodes:
            print(f'{node} --> {self.adj_lst[node]}')

    def add_edges(self,u,v):
        self.adj_lst[u].append(v)
        if not self.is_directed:
            self.adj_lst[v].append(u)

    def degree(self,u):
        return len(self.adj_lst[u])


all_edges=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]
Nodes=["A","B","C","D","E"]
graph=Graph(Nodes,is_directed=True)

for u,v in all_edges:
    graph.add_edges(u,v)

graph.add_edges("A","D")
graph.printing_adj_lst()
print(f'Degree --> {graph.degree("A")}')

#https://www.youtube.com/watch?v=8x7omPbQrPw&list=PL2q4fbVm1Ik6DCzm9XZJbNwyHtHGclcEh&index=2
#https://www.youtube.com/watch?v=QsAUil2eBZs
