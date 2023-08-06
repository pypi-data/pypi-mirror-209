from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, Dict, List

__all__ = ["Tree"]


class BaseTree(ABC):
    @abstractmethod
    def tree_from_list(self, record_list: List[Dict]) -> List[Dict]:
        ...

    @abstractmethod
    def list_from_tree(self, record_list: List[Dict]) -> List[Dict]:
        ...


class MixinTree:
    def __init__(self) -> None:
        self._flow_key: str

    def make_parent_flow(self, node: Dict, parent_number: int) -> None:
        node[self._flow_key] = f"{parent_number + 1}"

    def make_child_flow(
        self, node: Dict, child_number: int, parent_number: int
    ) -> None:
        flow = f"{parent_number}-{child_number + 1}"
        node[self._flow_key] = flow

    def new_node(self, node: Dict) -> None:
        return


class Tree(BaseTree, MixinTree):
    def __init__(
        self,
        id_key: str = "id",
        parent_key: str = "parent",
        parent_start: Any = "0",
        child_key: str = "children",
        flow_key: str = "flow",
        flow: bool = True,
    ) -> None:
        self._child_key: str = child_key
        self._id_key: str = id_key
        self._parent_key: str = parent_key
        self._parent_start: str = parent_start
        self._flow_key: str = flow_key
        self._flow: bool = flow
        self._final_tree: List = []

    def tree_from_list(self, record_list: List[Dict]) -> List[Dict]:
        local_record_list = deepcopy(record_list)
        trees = []
        parent_number = 0
        for node in local_record_list:
            if str(node[self._parent_key]) == str(self._parent_start):
                self.new_node(node)
                if self._flow:
                    self.make_parent_flow(node, parent_number)
                    parent_number += 1
                trees.append(node)
                self._build_leaf(node, local_record_list)
        return trees

    def list_from_tree(self, record_list: List[Dict]) -> List[Dict]:
        local_record_list = deepcopy(record_list)
        for tree in local_record_list:
            self._build_list(tree)
        return self._final_tree

    def _build_list(self, tree):
        tree_new = [tree]
        for node in tree_new:
            item = deepcopy(node)
            item.pop(self._child_key, None)
            self._final_tree.append(item)
            if self._child_key in node and node[self._child_key]:
                for child in node[self._child_key]:
                    self._build_list(child)

    def _build_leaf(self, node: Dict, record_list: List) -> None:
        child_lst = self._get_child(node, record_list)
        child_number = 0
        if child_lst:
            node[self._child_key] = child_lst
            for child in child_lst:
                self.new_node(child)
                if self._flow:
                    self.make_child_flow(child, child_number, node[self._flow_key])
                    child_number += 1
                self._build_leaf(child, record_list)

    def _get_child(self, node: Dict, record_list: List) -> List:
        child_lst = []
        for item in record_list:
            parent = item[self._parent_key]
            if node[self._id_key] == parent:
                child_lst.append(item)
        return child_lst
