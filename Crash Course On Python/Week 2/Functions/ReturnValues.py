def area_triangle(base,height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

Sum = area_a + area_b

print ("The sum of both areas is:",Sum)


def convert_seconds(Seconds):
    Hours = Seconds // 3600
    Minutes = (Seconds - Hours * 3600) // 60
    Remaining_seconds = Seconds - Hours * 3600 - Minutes * 60
    return Hours, Minutes, Remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)