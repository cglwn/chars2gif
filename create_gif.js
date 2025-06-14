const { createCanvas } = require('canvas')
const GIFEncoder = require('gifencoder')
const fs = require('fs')

const args = process.argv.slice(2)

if (args.length < 2) {
  console.log('Usage: node create_gif.js <sequence> <color> [output_filename]')
  console.log('Example: node create_gif.js "✳✳✳✳✳✳✽✻✶✢······✢✶✻✽" "#c87e5c" "my_animation.gif"')
  process.exit(1)
}

const sequence = args[0]
const color = args[1]
const outputFile = args[2] || 'animation.gif'
const width = 400
const height = 400
const fontSize = 500

const encoder = new GIFEncoder(width, height)
encoder.createReadStream().pipe(fs.createWriteStream(outputFile))

encoder.start()
encoder.setRepeat(0)
encoder.setDelay(100)
encoder.setQuality(1)
encoder.setTransparent(0x000000)

for (let i = 0; i < sequence.length; i++) {
  const canvas = createCanvas(width, height)
  const ctx = canvas.getContext('2d')

  ctx.fillStyle = color
  ctx.font = `${fontSize}px Arial`
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'

  ctx.fillText(sequence[i], width / 2, height / 2)

  encoder.addFrame(ctx)
  console.log(`Added frame ${i + 1}: '${sequence[i]}'`)
}

encoder.finish()
console.log(`GIF created: ${outputFile}`)
