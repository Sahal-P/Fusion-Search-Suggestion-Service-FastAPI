class Vertex:
    def __init__(self, id):
        self.id = id
        self.connections = []

    def add_connection(self, vertex):
        self.connections.append(vertex)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, vertex_id1, vertex_id2):
        if vertex_id1 in self.vertices and vertex_id2 in self.vertices:
            vertex1 = self.vertices[vertex_id1]
            vertex2 = self.vertices[vertex_id2]
            vertex1.add_connection(vertex2)
            vertex2.add_connection(vertex1)

    def get_vertex(self, vertex_id):
        return self.vertices.get(vertex_id)


# Usage example:

# Create graph and vertices
social_graph = Graph()
user1 = Vertex("user1")
user2 = Vertex("user2")
user3 = Vertex("user3")
user4 = Vertex("user4")

# Add vertices to the graph
social_graph.add_vertex(user1)
social_graph.add_vertex(user2)
social_graph.add_vertex(user3)
social_graph.add_vertex(user4)

# Create connections (edges) between users
social_graph.add_edge("user1", "user2")
social_graph.add_edge("user1", "user3")
social_graph.add_edge("user2", "user3")
social_graph.add_edge("user3", "user4")

# Get a vertex by its ID
user = social_graph.get_vertex("user1")
if user:
    print(user.connections) 
    for i in user.connections:
        print(i.id)