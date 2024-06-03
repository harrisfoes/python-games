def area_sum(rectangles):
    area_per_rect = []
    area_sum = 0 

    for rect in rectangles:
        print(rect, "dadadadada")
        print(f"h: {rect['height']}, w: {rect['width']}")
        area_per_rect.append(rect['height'] * rect['width'])

        area_sum = area_sum + (rect['height'] * rect['width'])


    return area_sum



'''
<BS>Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, then sum them all up and return the result.
'''
