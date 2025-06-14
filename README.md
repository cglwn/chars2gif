Make a GIF from a text sequence.

I made this for a GIF similar to Claude Code's animation

![](./claude-code-centred.gif)

```
npm install
node create_gif.js "✳✳✳✳✳✳✽✻✶✢······✢✶✻✽" "#c87e5c" "claude-code.gif"
```

Optionally centre the frames in the GIF
```
pip install -r requirements.txt
python centre_gif.py claude-code.gif claude-code-centred.gif
```

- PIL had bad support for fonts so the GIF creation is done with JS instead
- The original GIF was jittery and `numpy` + `PIL` is good for gif2gif

