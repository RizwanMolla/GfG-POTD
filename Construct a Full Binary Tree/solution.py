class Solution:
    def constructBinaryTree(self, pre, preMirror):
        d = dict()
        for i in range(len(preMirror)):
            d[preMirror[i]] = i

        root = Node(pre[0])
        st = [root]

        for i in range(1, len(pre)):
            curr = Node(pre[i])

            while st and d[st[-1].data] > d[pre[i]]:
                st.pop()

            if st[-1].left == None:
                st[-1].left = curr
            else:
                st[-1].right = curr

            st.append(curr)

        return root
