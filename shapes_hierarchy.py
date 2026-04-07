def main():
    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(0, 0, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square")
    ]

    print("--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name} Area = {shape.area}")

    print("\n--- Getter/setter check ---")

    c = shapes[0]
    print(f"{c.name} Current: {c.radius} {c.area}")
    c.radius *= 2
    print(f"{c.name} Doubled: {c.radius} {c.area}")

    r = shapes[2]
    print(f"{r.name} Current: {r.length} {r.width} {r.area}")
    r.length *= 2
    r.width *= 2
    print(f"{r.name} Doubled: {r.length} {r.width} {r.area}")

    s = shapes[4]
    print(f"{s.name} Current: {s.side} {s.area}")
    s.side *= 2
    print(f"{s.name} Doubled: {s.side} {s.area}")


if __name__ == "__main__":
    main()
