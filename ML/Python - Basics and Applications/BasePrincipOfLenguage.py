ans = 0
RepObjects = []
for obj in objects:
    if obj not in RepObjects:
        RepObjects.append(obj)
        ans += 1

print(ans)