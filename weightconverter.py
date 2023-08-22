print("WEIGHT CONVERTER")

weight = int(input("Weight: "))

print(weight)

convert = input("(K)g or (L)bs: ")

if convert == "l":
    print(f"Weight in Kgs: {weight * 0.45}")

elif convert == "L":
    print(f"Weight in Kgs: {weight * 0.45}")

if convert == "k":
    print(f"Weight in Lbs: {weight / 2.2}")

elif convert == "K":
    print(f"Weight in Lbs: {weight / 2.2}")