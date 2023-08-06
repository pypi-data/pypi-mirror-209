# Tree Parsing

[![CI](https://github.com/scjorge/tree-parsing/workflows/CI/badge.svg?event=push)](https://github.com/scjorge/tree-parsing/actions)
[![codecov](https://codecov.io/gh/scjorge/tree-parsing/branch/master/graph/badge.svg?token=0HF8XRJDV1)](https://codecov.io/gh/scjorge/tree-parsing)
[![pypi](https://img.shields.io/pypi/v/tree-parsing)](https://pypi.org/project/tree-parsing/)
[![pypi](https://img.shields.io/pypi/pyversions/tree-parsing)](https://pypi.org/project/tree-parsing/)
[![license](https://img.shields.io/pypi/l/tree-parsing)](https://github.com/scjorge/tree-parsing/blob/master/LICENSE)


<p align="center">
    <img src="https://raw.githubusercontent.com/scjorge/tree-parsing/master/docs/assets/logo.png" width='200'/>
</p>

---

Documentation: https://tree-parsing.readthedocs.io/en/latest/

Source Code: https://github.com/scjorge/tree-parsing

---


This library lets you work with trees and lists.

So you can:

- Make a tree when you have all nodes in the list
- Convert the Tree to lists of nodes
- Customize how to generate 'flow key', 'children key'
- Do something for each node


## Install
Installation is as simple:

### With pip

```
pip install tree-parsing
```

### With Poetry

```
poetry add tree-parsing
```

## Exemplos

### Tree From List 

```{.py3 linenums=1}
import json

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]

tr = Tree(id_key="id", parent_key="parent", parent_start="0", child_key="children")
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "1-1",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "1-1-1"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "1-2"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "2"
    }
]
```

### List From Tree

```{.py3 linenums=1}
import json

from tree_parsing import Tree


my_tree = [
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "flow": "1-1",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "1-1-1"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "1-2"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "2"
    }
]

tr = Tree(id_key="id", parent_key="parent", child_key="children")
list_tree = tr.list_from_tree(my_tree)
print(json.dumps(list_tree, indent=1))
```

Output:

```
[
 {
  "id": 1,
  "parent": 0,
  "flow": "1"
 },
 {
  "id": 2,
  "parent": 1,
  "flow": "1-1"
 },
 {
  "id": 4,
  "parent": 2,
  "flow": "1-1-1"
 },
 {
  "id": 3,
  "parent": 1,
  "flow": "1-2"
 },
 {
  "id": 5,
  "parent": 0,
  "flow": "2"
 }
]
```

### Do something on the node

```{.py3 linenums=1}
import json
from typing import Dict

from tree_parsing import Tree


list_tree = [
    {"id": 1, "parent": 0},
    {"id": 2, "parent": 1},
    {"id": 3, "parent": 1},
    {"id": 4, "parent": 2},
    {"id": 5, "parent": 0},
]


class MyTree(Tree):
    def new_node(self, node: Dict) -> None:
        if node['id'] == 2:
            node['new_key'] = 'new value'
        

tr = MyTree(id_key="id", parent_key="parent", parent_start="0", child_key="children")
tree = tr.tree_from_list(list_tree)
print(json.dumps(tree, indent=4))
```

Output:

```
[
    {
        "id": 1,
        "parent": 0,
        "flow": "1",
        "children": [
            {
                "id": 2,
                "parent": 1,
                "new_key": "new value",
                "flow": "1-1",
                "children": [
                    {
                        "id": 4,
                        "parent": 2,
                        "flow": "1-1-1"
                    }
                ]
            },
            {
                "id": 3,
                "parent": 1,
                "flow": "1-2"
            }
        ]
    },
    {
        "id": 5,
        "parent": 0,
        "flow": "2"
    }
]
```
