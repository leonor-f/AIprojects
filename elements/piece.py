class Piece:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_position(self):
        return self.x, self.y

    def get_image_path(self):
        return self.image_path