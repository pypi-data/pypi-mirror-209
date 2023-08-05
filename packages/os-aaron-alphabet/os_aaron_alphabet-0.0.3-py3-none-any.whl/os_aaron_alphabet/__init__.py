import os

def walk(*targets):
    ans = list()
    for target in targets:
        if os.path.isfile(target):
            if target not in ans:
                ans.append(target)
            continue
        for (root, dirnames, filenames) in os.walk(target):
            for filename in filenames:
                file = os.path.join(root, filename)
                if file not in ans:
                    ans.append(file)
    return ans 
