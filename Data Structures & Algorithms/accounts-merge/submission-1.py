class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #accounts account[i] is a list of strings
        # two accounts belong to the same person
        # two account have the same name , can have any number of acccounts initalliy 
        #connection, classify as a same group
        # email as a key because it's unique

        parent = {}
        email_to_name= {}

        def find(i):
            #if it's parent it self neet@gmail.com .. 
            if parent[i] == i :
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(x,y):
            root_x = find(x)#root
            root_y = find(y)#root

            if root_x != root_y: # root1 != root2
                #부모가다르면
                parent[root_x] = root_y 

            
        for acc in accounts:
            #print(email)
            name = acc[0]
            first_email=acc[1]

            for email in acc[1:]: #slicing every email except for name
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

                union(first_email,email)
            # list   
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))
        return res