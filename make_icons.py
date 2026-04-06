#!/usr/bin/env python3
import os, struct, zlib

def make_png(size):
    bg = (13, 13, 13)
    fg = (200, 245, 66)
    
    pixels = []
    cx, cy = size // 2, size // 2
    r_outer = int(size * 0.38)
    r_inner = int(size * 0.10)
    stroke = max(2, size // 32)

    for y in range(size):
        row = []
        for x in range(size):
            dx, dy = x - cx, y - cy
            dist = (dx*dx + dy*dy) ** 0.5

            # Outer circle ring
            if abs(dist - r_outer) < stroke:
                row.extend(fg)
            # Vertical bar of plus
            elif abs(dx) < r_inner and dist < r_outer - stroke * 2:
                row.extend(fg)
            # Horizontal bar of plus
            elif abs(dy) < r_inner and dist < r_outer - stroke * 2:
                row.extend(fg)
            else:
                row.extend(bg)
        pixels.append(bytes(row))

    def chunk(name, data):
        c = struct.pack('>I', len(data)) + name + data
        return c + struct.pack('>I', zlib.crc32(name + data) & 0xffffffff)

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
    
    raw = b''
    for row in pixels:
        raw += b'\x00' + row
    idat = chunk(b'IDAT', zlib.compress(raw))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

os.makedirs('/home/claude/foodtracker/icons', exist_ok=True)

for size in [192, 512]:
    with open(f'/home/claude/foodtracker/icons/icon-{size}.png', 'wb') as f:
        f.write(make_png(size))
    print(f'Created icon-{size}.png')
