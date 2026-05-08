def qpsk_demodulate(symbols):
    # Missing feature: no error handling for empty list
    return [complex(1,0) if s > 0 else complex(-1,0) for s in symbols]
