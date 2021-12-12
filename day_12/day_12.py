import common


class Cave:

    def __init__(self, name):
        self.name = name
        self.connections = []
        self.is_large = name.isupper()

    def add_connection(self, connection):
        if self.name == connection.name:
            return
        self.connections.append(connection)

    def __str__(self):
        return self.name + "-> " + ",".join([conn.name for conn in self.connections])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class CaveSystem:

    caves = {}

    def __init__(self, cave_connections: list):
        for conn in cave_connections:
            c1, c2 = conn.split("-")
            if c1 not in self.caves:
                cave1 = Cave(c1)
                self.caves[c1] = cave1
            if c2 not in self.caves:
                cave2 = Cave(c2)
                self.caves[c2] = cave2
            cave1 = self.caves[c1]
            cave2 = self.caves[c2]
            cave1.add_connection(cave2)
            cave2.add_connection(cave1)

    def __str__(self):
        return str(self.caves)

    def __repr__(self):
        return str(self)


def day_12_1(path):
    cave_connections = [conn.strip() for conn in common.read_string_list(path)]
    # print(cave_connections)

    cs = CaveSystem(cave_connections)
    # print(cs)

    paths = []

    start = cs.caves["start"]
    seen = {}
    visit(start, seen, "", paths)

    # print(paths)
    return len(paths)


def visit(cave, seen, path, paths):
    if cave.name == "end":
        paths.append(path+"end")
        return

    if (cave in seen and seen[cave]) and not cave.is_large:
        return

    seen[cave] = True
    path += cave.name

    for c in cave.connections:
        if (c not in seen) or (not seen[c]) or c.is_large:
            visit(c, seen, path, paths)
    seen[cave] = False


def day_12_2(path):
    cave_connections = [conn.strip() for conn in common.read_string_list(path)]
    # print(cave_connections)

    cs = CaveSystem(cave_connections)
    # print(cs)

    all_paths = set()

    small_caves = [name for name, cave in cs.caves.items() if not cave.is_large and name != "start" and name != "end"]

    for small in small_caves:
        paths = []

        start = cs.caves["start"]
        seen = {}

        visit_2(start, seen, "", paths, small)

        [all_paths.add(p) for p in paths]

    # print(paths)
    return len(all_paths)


def visit_2(cave, seen, path, paths, exception):
    if cave.name == "end":
        paths.append(path+"end")
        return

    if (cave in seen and seen[cave] > 0) and not cave.is_large:
        if cave.name != exception or seen[cave] > 1:
            return

    if cave.name == exception and cave in seen:
        seen[cave] += 1
    else:
        seen[cave] = 1

    path += cave.name

    for c in cave.connections:
        if (c not in seen) or (seen[c] == 0) or c.is_large or (c.name == exception and seen[c] == 1):
            visit_2(c, seen, path, paths, exception)

    seen[cave] -= 1
