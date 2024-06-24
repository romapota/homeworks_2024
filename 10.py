class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(cls):
        return cls._links


class Link:
    def __init__(self, v1, v2, _dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = _dist
        v1.links.append(self)
        v2.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        self._vertex.append(v)

    def add_link(self, link):
        if not (any((i._v1 == link._v1 and i._v2 == link._v2) or (i._v2 == link._v1 and i._v1 == link._v2) for i in
                    self._links)):
            if link._v1 != None and link._v1 not in self._vertex:
                self.add_vertex(link._v1)
            if link._v2 != None and link._v2 not in self._vertex:
                self.add_vertex(link._v2)
            self._links.append(link)

    def find_path(self, start_v, stop_v):

        visited_ver = {v: False for v in self._vertex}
        distance = {l: 10000 for l in self._vertex}
        shortest = {v: None for v in self._vertex}

        visited_ver[start_v] = True
        distance[start_v] = 0
        op_vert = start_v

        while visited_ver[stop_v] != True:
            min_vert_dist = 10000
            min_vert = None
            for i in op_vert.links:
                if i._v1 != op_vert:
                    ngb_vert = i._v1
                if i._v2 != op_vert:
                    ngb_vert = i._v2
                if visited_ver[ngb_vert] == False:
                    if i.dist + distance[op_vert] < distance[ngb_vert]:
                        distance[ngb_vert] = i.dist + distance[op_vert]
                        shortest[ngb_vert] = (op_vert, i)
                    if distance[ngb_vert] < min_vert_dist:
                        min_vert_dist = distance[ngb_vert]
                        min_vert = ngb_vert
            visited_ver[op_vert] = True
            op_vert = min_vert
        result = ([], [])
        i = stop_v
        result_vert = []
        while i != start_v:
            result_vert.append(shortest[i][0])
            result[1].append(shortest[i][1])
            i = shortest[i][0]
        result_vert = reversed(result_vert)
        for i in result_vert:
            result[0].append(i)
        result[0].append(stop_v)
        return result


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, _dist):
        super().__init__(v1, v2, _dist)
