from elements.piece import Piece

class Knight(Piece):
  def __init__(self, x, y, image_path, flag = False):
    super().__init__(x, y, image_path)
    self.flag = flag

