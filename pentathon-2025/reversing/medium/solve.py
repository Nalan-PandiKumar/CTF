#!/usr/bin/env python3
# solve_maze.py
# Reads struct direction[] from a binary and searches for a path from pos 0 to target 0x28
# struct direction { int a; int w; int s; int d; } (little-endian)
# Each struct = 16 bytes. data offset default = 0x21e0 (as you found).

import sys
import struct
from collections import deque

DATA_OFFSET = 0x21e0     # as reported in the disassembly
STRUCT_SIZE = 16         # 4 ints * 4 bytes
DEFAULT_COUNT = 39       # how many structs to attempt to read (adjust if needed)
TARGET = 0x28            # target position the binary checks for

def load_directions(path, offset=DATA_OFFSET, count=DEFAULT_COUNT):
    with open(path, 'rb') as f:
        f.seek(0, 2)
        filesize = f.tell()
        if offset >= filesize:
            raise ValueError(f"file too small ({filesize} bytes) for offset 0x{offset:x}")
        f.seek(offset)
        raw = f.read(count * STRUCT_SIZE)
    dirs = []
    for i in range(0, len(raw), STRUCT_SIZE):
        if i + STRUCT_SIZE > len(raw):
            break
        a, w, s, d = struct.unpack_from('<4i', raw, i)  # little-endian ints
        dirs.append({'a': a, 'w': w, 's': s, 'd': d})
    return dirs

def allowed_moves(dirs, pos):
    """Return list of (move_char, new_pos) permitted by the dirs at pos given the binary checks."""
    moves = []
    n = len(dirs)
    # bounds checks used by binary:
    # 'd' requires (d==1) and (pos % 8 != 7) -> pos+1
    # 'a' requires (a==1) and ((pos & 7) != 0) -> pos-1
    # 's' requires (s==1) and (pos < 0x38) -> pos+8
    # 'w' requires (w==1) and (pos > 7) -> pos-8
    if pos < 0 or pos >= n:
        return []
    cell = dirs[pos]
    if cell['d'] == 1 and (pos % 8) != 7:
        moves.append(('d', pos + 1))
    if cell['a'] == 1 and (pos & 7) != 0:
        moves.append(('a', pos - 1))
    if cell['s'] == 1 and pos < 0x38:
        moves.append(('s', pos + 8))
    if cell['w'] == 1 and pos > 7:
        moves.append(('w', pos - 8))
    return moves

def find_path(dirs, start=0, target=TARGET):
    # BFS with path reconstruction (shortest path)
    q = deque([start])
    prev = {start: None}
    prev_move = {}
    while q:
        p = q.popleft()
        if p == target:
            # reconstruct
            path = []
            cur = p
            while prev[cur] is not None:
                path.append(prev_move[cur])
                cur = prev[cur]
            return list(reversed(path)), p
        for mv, newp in allowed_moves(dirs, p):
            if newp < 0 or newp >= len(dirs):
                continue
            if newp not in prev:
                prev[newp] = p
                prev_move[newp] = mv
                q.append(newp)
    return None, None

def pretty_print_map(dirs, cols=8):
    # print grid of cells with open directions
    rows = (len(dirs) + cols - 1) // cols
    for r in range(rows):
        row_cells = []
        for c in range(cols):
            idx = r*cols + c
            if idx >= len(dirs):
                row_cells.append('   ')
                continue
            cell = dirs[idx]
            # show as [LUDR] where a,left -> L, w/up -> U, s/down -> D, d/right -> R
            flags = ''.join([
                'L' if cell['a'] == 1 else '.',
                'U' if cell['w'] == 1 else '.',
                'D' if cell['s'] == 1 else '.',
                'R' if cell['d'] == 1 else '.',
            ])
            row_cells.append(f"{idx:02d}:{flags}")
        print('  '.join(row_cells))

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 solve_maze.py <path-to-binary> [entries]")
        return
    path = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_COUNT
    dirs = load_directions(path, DATA_OFFSET, count)
    print(f"Read {len(dirs)} direction entries from offset 0x{DATA_OFFSET:x}")
    pretty_print_map(dirs)
    path, endpos = find_path(dirs, start=0, target=TARGET)
    if path is None:
        print(f"No path found to target 0x{TARGET:x} (decimal {TARGET}). Try increasing entries count.")
    else:
        print(f"Found path (length {len(path)}): {''.join(path)}")
        print("Moves separated by char (a/w/s/d) — this is the string you should input to the binary.")
        print(f"Final position reached: {endpos}")

if __name__ == '__main__':
    main()
