## 51. Binary Search Tree to Greater Sum Tree

<aside>
💡 **Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.**

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.
</aside>

---

**Constraints:**

- The number of nodes in the tree is in the range `[1, 100]`.
- `0 <= Node.val <= 100`
- All the values in the tree are **unique**.

---

- **`bstToGst` method**
    - 재귀적인 호출
    - `root` 노드가 None이 아닌 경우, 오른쪽 subtree를 방문
    - `val` 변수에 현재 노드의 값(root.val)을 더하고, 노드의 값(root.val)을 `val` 로 update ⇒ 변환된 ******BST******가 반환