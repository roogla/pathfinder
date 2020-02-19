class GridMatrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rects = []

    def create_rects(self):
        dim_x = self.width // 25
        dim_y = self.height // 25
        for n in range(0, dim_x):
            for m in range(0, dim_y):
                self.rects.append({
                    'coord': [n, m],
                    'grid': [0 + n * 25, 0 + m * 25, 25, 25],
                    'screen': None,
                    'color': None,
                    'fill': 1
                })
        return self.rects


def find_nine(coord, color):
    a = coord[0] - 1
    b = coord[1] - 1
    return_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            if a + i == coord[0] and b + j == coord[1]:
                pass
            else:
                return_list.append([a + i, b + j])
    return return_list
