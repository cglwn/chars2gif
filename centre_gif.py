"""Centres the frames in a transparent GIF.

Usage:
  python centre_gif.py input.gif output_centred.gif
"""

from PIL import Image, ImageDraw
import numpy as np
import argparse


def get_text_bounds(img):
    """Find the bounding box of non-transparent pixels"""
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Get non-transparent pixels
    alpha = np.array(img)[:, :, 3]
    rows = np.any(alpha > 0, axis=1)
    cols = np.any(alpha > 0, axis=0)

    if not np.any(rows) or not np.any(cols):
        return None

    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    return (cmin, rmin, cmax, rmax)


def centre_frame(frame, target_width, target_height):
    """Centre the content of a frame"""
    bounds = get_text_bounds(frame)
    if bounds is None:
        return frame

    cmin, rmin, cmax, rmax = bounds
    content_width = cmax - cmin + 1
    content_height = rmax - rmin + 1

    new_x = (target_width - content_width) // 2
    new_y = (target_height - content_height) // 2

    new_frame = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
    content = frame.crop((cmin, rmin, cmax + 1, rmax + 1))
    new_frame.paste(content, (new_x, new_y), content)

    return new_frame


def main():
    parser = argparse.ArgumentParser(
        description="Centre frames in a GIF to reduce jitter"
    )
    parser.add_argument("input", help="Input GIF filename")
    parser.add_argument("output", help="Output GIF filename")
    args = parser.parse_args()

    with Image.open(args.input) as gif:
        frames = []
        durations = []

        try:
            while True:
                frame = gif.copy().convert("RGBA")
                frames.append(centre_frame(frame, gif.width, gif.height))
                durations.append(gif.info.get("duration", 100))
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass

    frames[0].save(
        args.output,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        transparency=0,
        disposal=2,
    )

    print(f"Centred GIF created with {len(frames)} frames: {args.output}")


if __name__ == "__main__":
    main()
