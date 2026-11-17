mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)
print("The total destinations in mission route is",len(mission_route))
print("The first destination is",mission_route[0])
print("The last destination is",mission_route[-1])
for destination in mission_route:
    print(destination)
if "Europa" in mission_route:
    print("Europa is part of mission route")