
"""
https://www.iquilezles.org/www/articles/fbm/fbm.htm
"""

def fractional_brownian_motion(vec_x, H=0.5, num_octaves=3):

    noiseSeed(10)

    G = pow(2, -H)
    f = 1.0
    a = 1.0
    t = 0.0

    for i in range(num_octaves):

        t += a * noise(f * vec_x)
        f *= 2.0
        a *= G

    return t
