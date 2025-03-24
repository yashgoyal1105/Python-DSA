from collections import deque

class TreeNode:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

    def bfs(self,root):
        if not root:
            return []
        
        queue = deque([root]) 
        result = []
        
        while queue:
            node = queue.popleft()   
            result.append(node.data) 
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

    def dfs_inorder(self, root): 
        if root:
            self.dfs_inorder(root.left) 
            print(root.data, end=" ")  
            self.dfs_inorder(root.right)  

    def dfs_preorder(self, root): 

        if root:
            print(root.data, end=" ")
            self.dfs_preorder(root.left)
            self.dfs_preorder(root.right)
    
    def dfs_postorder(self,root): 
        if root:
              self.dfs_postorder(root.left)
              self.dfs_postorder(root.right)
              print(root.data, end=" ")

def main():
    """
    desc: stores object and the script is run
    parameter: None
    return: None
    """
    root = TreeNode(50)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"\nBFS Traversal: {root.bfs(root)}")

    print("\nDFS Preorder Traversal:")
    root.dfs_preorder(root)
    print("\nDFS inorder Traversal:")
    root.dfs_inorder(root)
    print("\nDFS postorder Traversal:")
    root.dfs_postorder(root)
    

if __name__ == "__main__":
    main()
    