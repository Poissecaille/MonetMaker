from tqdm import tqdm


def pixel_closest_color_from_palette(pixel_rgb: tuple, color_palette: dict) -> tuple:
    distances = []
    result = 0
    for rgb_tuple in color_palette.values():
        for i, rgb_value in enumerate(pixel_rgb):
            result += abs(rgb_value-rgb_tuple[i])
        distances.append(result)
        result = 0
    index_of_smallest_distance = distances.index(min(distances))
    return color_palette[index_of_smallest_distance]


def classify_pixels(matrix: list, color_palette: dict) -> list:
    print("PIXEL CLASSIFICATION")
    for pixel_row in tqdm(matrix):
        for i, rgb in enumerate(pixel_row):
            pixel_row[i] = pixel_closest_color_from_palette(
                rgb, color_palette)
    return matrix
