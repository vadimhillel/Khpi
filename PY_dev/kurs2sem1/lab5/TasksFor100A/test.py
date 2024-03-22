def get_size(w,h,d):
    result = [];
    surfaceArea = (2 * (w * h)) + (2 * (w * d)) + (2 * (h * d));
    volume = w * h * d;
    result.append(surfaceArea);
    result.append(volume);
    return result;

print(get_size(2,2,2))

