class GridMatrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rects = []

    def create_rects(self):
        dim_x = self.width // 20
        dim_y = self.height // 20
        for n in range(0, dim_x):
            for m in range(0, dim_y):
                self.rects.append({
                    'coord': [n, m],
                    'grid': [0 + n * 20, 0 + m * 20, 20, 20],
                    'screen': None,
                    'color': None,
                    'fill': 1,
                    'wall': 0,
                    'cost': 0
                })
        return self.rects


def find_nine(coord, rectal_dict):
    a = coord[0] - 1
    b = coord[1] - 1
    return_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            if a + i == coord[0] and b + j == coord[1]:
                pass
            else:
                for rectal in rectal_dict:
                    if rectal['coord'] == [a + i, b + j]:
                        return_list.append(rectal)
    return return_list
