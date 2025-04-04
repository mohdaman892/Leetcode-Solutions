# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(root,l,k):
            if root:
                root.par = k
                if l not in self.hm:
                    self.hm[l] = [root]
                else:
                    self.hm[l].append(root)
                f(root.left,l+1,root)
                f(root.right,l+1,root)
        
        def lca(root,p,q):
            if not root:
                return None
            if root==p:
                return p
            if root==q:
                return q
            l = lca(root.left,p,q)
            r = lca(root.right,p,q)
            if l and r:
                return root
            elif l and not r:
                return l
            elif r and not l:
                return r
            return None
            
        
        self.hm = {}
        f(root,0,root)
        a = self.hm[max(self.hm.keys())]
        if len(a)==1:
            return a[0]
        # print(a)
        return lca(root,a[0],a[-1])