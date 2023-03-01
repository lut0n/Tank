class Bullet():
    def __init__(self,x,y,x1,y1):
        if x == x1 or y == y1:
            return True
        else:
            return False
