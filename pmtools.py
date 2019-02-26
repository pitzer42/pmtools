import sys
import csv
import graphviz

class Need:
    def __init__(self):
        self.id = None
        self.partent = None
        self.direction = None
        self.metric = None
        self.subject = None
        self.connecting_word = None

    def __str__(self):
        str_components = [
            str(self.direction),
            str(self.metric),
            str(self.connecting_word),
            str(self.subject)
        ]
        return ' '.join(str_components)

def plot_needs(needs):
    graph = graphviz.Digraph()
    print(needs)
    for key in needs.keys():
        need = needs[key]
        print(need)
        graph.node(str(need))
        if need.parent:
            graph.edge(str(need), str(needs[need.parent]))
    graph.render('needs', view=True)


def load_needs(source_file):
    def parse_need_from_csv_line(line):
        need = Need()
        need.id = line[0]
        need.parent = line[1]
        need.direction = line[2]
        need.metric = line[3]
        need.connecting_word = line[4]
        need.subject = line[5]
        return need

    needs = dict()
    skip_header = True
    with open(source_file) as src:
        reader = csv.reader(src)
        for line in reader:
            if skip_header:
                skip_header = False
                continue
            need = parse_need_from_csv_line(line)
            print(need)
            needs[need.id] = need
    return needs


args = sys.argv[1:]
for i in args:
    print(i)

"""
if args[0] == 'load':
    if args[1] == 'needs':
        print(load_needs(args[2]))
"""
plot_needs(load_needs(args[0]))
