mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)
while True:
    destination = input("Enter a destination: ")
    if destination in mission_route:
        print(f"{destination} is in mission route")
        print("Stops from start:", mission_route.index(destination))
        print("Stops from end:", len(mission_route)-mission_route.index(destination)-1)
        if len(mission_route)-mission_route.index(destination)-1 == 0:
            print("This is the final destination")
        else:
            print("The next stop is", mission_route[mission_route.index(destination)+1])
        break
    else:
        print(f"{destination} is not in mission route")