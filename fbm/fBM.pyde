from brownian_motion import fractional_brownian_motion

X = 1
x_move = 1

def setup():
    size(800, 800)
    # background(0)
    blendMode(ADD)


def draw():

    background(0)

    global x_move
    x_move += 10

    # stroke(255)
    # strokeWeight(5)
    # point(5 + x_move, height/2 + t*fbm_mult)

    # if x_move >= width:
    #     background(0)
    #     x_move = 1


    n_rows = 15
    n_cols = 60
    point_size = 20
    x_padding = 10
    y_padding = 30
    offset_mult = 2
    fbm_mult = 10
    alpha = 200
    for y_row in range(n_rows):

        for x_col in range(n_cols):

            t = fractional_brownian_motion(
                vec_x=X, 
                H=0.5, 
                num_octaves=1
            )
            global X
            X += 0.1
            print(t)    

            # 0,0,255
            stroke(0,0,255,alpha)
            strokeWeight(point_size)
            
            x_spacing = (width + width*0.5)/n_cols
            y_spacing = height/n_rows
            
            x_pos = x_col * x_spacing + x_padding
            y_pos = y_row * y_spacing + y_padding

            random_offset = random(-0.5, 0.5) * offset_mult
            point(x_pos + random_offset, y_pos + t*fbm_mult + random_offset)

            # 255,0,0
            stroke(255,0,0,alpha)
            strokeWeight(point_size)
            
            x_spacing = (width + width*0.5)/n_cols
            y_spacing = height/n_rows
            
            x_pos = x_col * x_spacing + x_padding
            y_pos = y_row * y_spacing + y_padding

            random_offset = random(-0.5, 0.5) * offset_mult
            point(x_pos + random_offset, y_pos + t*fbm_mult + random_offset)

            # 0,255,0
            stroke(0,255,0,alpha)
            strokeWeight(point_size)
            
            x_spacing = (width + width*0.5)/n_cols
            y_spacing = height/n_rows
            
            x_pos = x_col * x_spacing + x_padding
            y_pos = y_row * y_spacing + y_padding

            random_offset = random(-0.5, 0.5) * offset_mult
            point(x_pos + random_offset, y_pos + t*fbm_mult + random_offset)

            # 255,255,255
            # stroke(255)
            # strokeWeight(point_size)
            # x_spacing = (width + width*0.5)/n_cols
            # y_spacing = height/n_rows
            # x_pos = x_col * x_spacing + x_padding
            # y_pos = y_row * y_spacing + y_padding
            # point(x_pos, y_pos + t*fbm_mult)





    



    

    




