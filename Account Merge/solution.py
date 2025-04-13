#User function Template for python3
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        email_to_name = {}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(email, first_email)
                email_to_name[email] = name

        roots = defaultdict(list)
        for email in parent:
            root_email = find(email)
            roots[root_email].append(email)

        result = []
        for root_email, email_list in roots.items():
            name = email_to_name[root_email]
            result.append([name] + sorted(email_list))

        return result