import collections


class Solution:
    def accountsMerge(self, accounts):
        email2account = {}
        connections = []
        for index, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in email2account:
                    id = email2account[email]
                    connections.append([index, id])
                email2account[email] = index
        groups = self.unionFind(connections, len(accounts))
        email2group = collections.defaultdict(list)
        for key in email2account.keys():
            gourpId = groups[email2account[key]]
            email2group[gourpId].append(key)
        return [[accounts[id][0]] + sorted(email_list) for id, email_list in email2group.items()]


    def unionFind(self, connections, size):
        parents = [i for i in range(size)]
        for connection in connections:
            l, r = connection
            l_p = self.findParents(parents, l)
            r_p = self.findParents(parents, r)
            parents[r_p] = l_p

        for index in range(len(parents)):
            parents[index] = self.findParents(parents, index)
        return parents


    def findParents(self, parent, cur):
        if cur != parent[cur]:
            parent[cur] = self.findParents(parent, parent[cur])
        return parent[cur]