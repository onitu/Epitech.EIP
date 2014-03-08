from sys import argv

with open(argv[1]) as f:
  root = {"name": "Onitu", "children": []}

  f.next()
  f.next()
  f.next()

  for line in f:
    line = line.split(',')
    wbs = line[0].split('.')[2:]
    branch = root

    if len(wbs) > 1:
      for nb in wbs[:-1]:
        branch = branch["children"][int(nb) - 1]

    branch["children"].append({"name": line[1], "children": []})

def print_branch(branch):
  for child in branch["children"]:
    print "{} -> {}".format(branch["name"], child["name"])
    print_branch(child)

  if branch["children"]:
    print "{rank=same; " + " ".join([c["name"] for c in branch["children"]]) + "}"


print "digraph Onitu {"
print "node [shape=plaintext; headclip=true];"
print "rankdir=\"LR\"; splines=spline;"
print_branch(root)
print "}"