import math

def Calculate_area(shape, dimensions):
    if shape.lower() == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle dimensions should be a list or tuple with two elements (length, width).")
        length, width = dimensions
        return length * width
    elif shape.lower() == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle dimensions should be a list or tuple with one element (radius).")
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape! Only 'rectangle' and 'circle' are supported.")

rectangle_area = Calculate_area("rectangle", (5, 3))
circle_area = Calculate_area("circle", (4,))

print(f"Rectangle area: {rectangle_area}")
print(f"Circle area: {circle_area}")
print("This is successfull")