from PIL import Image

# Open and analyze the GIF
with Image.open('animation.gif') as img:
    frame_count = 0
    try:
        while True:
            print(f"Frame {frame_count}: {img.size}, mode: {img.mode}")
            frame_count += 1
            img.seek(frame_count)
    except EOFError:
        pass
    
    print(f"Total frames found: {frame_count}")
    
    # Also check duration
    img.seek(0)
    print(f"Duration per frame: {img.info.get('duration', 'unknown')}ms")
    print(f"Loop count: {img.info.get('loop', 'unknown')}")