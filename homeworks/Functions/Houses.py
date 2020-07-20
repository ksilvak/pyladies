import turtle

def build_house(side, ang) :
  house=turtle.Turtle()
  diag = (2*(side**2))**0.5
  moves = [(side,ang),(side,ang),(side,ang),(side,ang),
          (0,ang/2),(diag,ang),(diag/2,ang),(diag/2,ang),(diag,ang)]
  
  for (move,turn) in moves:
    house.fd(move)
    house.lt(turn)

build_house(100, 90)
