def preorder(root):
    global pre
    if root !=".":
        pre += root
        preorder(nodeinfo[root][0])
        preorder(nodeinfo[root][1])
    else:
        return
def midorder(root):
    global mid
    if root == ".":
        return
    midorder(nodeinfo[root][0])
    mid+=root
    midorder(nodeinfo[root][1])

def endorder(root):
    global end
    if root ==".":
        return
    endorder(nodeinfo[root][0])
    endorder(nodeinfo[root][1])
    end+=root


pre = ""
mid = ""
end = ""
N = int(input())
node=[0]*N
info = []
for _ in range(N):
    nn = list(map(str,input().split()))
    info.append(nn)

nodeinfo = {}

for i in info:
    nodeinfo[i[0]] = [i[1],i[2]]
preorder("A")
midorder("A")
endorder("A")

print(pre)
print(mid)
print(end)