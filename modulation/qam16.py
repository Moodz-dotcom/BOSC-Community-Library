def qam16_modulate(bits):
    mapping = {
        (0,0,0,0): complex(-3,-3), (0,0,0,1): complex(-3,-1),
        (0,0,1,0): complex(-3,3), (0,0,1,1): complex(-3,1),
        (0,1,0,0): complex(-1,-3), (0,1,0,1): complex(-1,-1),
        (0,1,1,0): complex(-1,3), (0,1,1,1): complex(-1,1),
        (1,0,0,0): complex(3,-3), (1,0,0,1): complex(3,-1),
        (1,0,1,0): complex(3,3), (1,0,1,1): complex(3,1),
        (1,1,0,0): complex(1,-3), (1,1,0,1): complex(1,-1),
        (1,1,1,0): complex(1,3), (1,1,1,1): complex(1,1),
    }
    if len(bits) % 4 != 0:
        raise ValueError("Bits length must be multiple of 4")
    return [mapping[tuple(bits[i:i+4])] for i in range(0, len(bits), 4)]
