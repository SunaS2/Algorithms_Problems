def preorder(node):
    global pre
    if node == '.':
        return
    
    pre = pre + node
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    global ino
    if node == '.':
        return
    
    inorder(tree[node][0])
    ino = ino + node
    inorder(tree[node][1])

def postorder(node):
    global post
    if node == '.':
        return 
    
    postorder(tree[node][0])
    postorder(tree[node][1])
    post = post + node

N = int(input())

tree = {}
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left,right)

pre = ''
ino = ''
post = ''

preorder('A')
inorder('A')
postorder('A')

print(pre)
print(ino)
print(post)