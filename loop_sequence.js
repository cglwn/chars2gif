const sequence = '·····✢✶✻✽✳✳✳✳✳✳✽✻✶✢·';
let index = 0;

// Hide cursor
process.stdout.write('\x1B[?25l');

function renderFrame() {
  process.stdout.write('\r\x1b[38;2;200;126;92m' + sequence[index] + '\x1b[0m');
  index = (index + 1) % sequence.length;
}

const interval = setInterval(renderFrame, 100);

// Handle termination cleanly
function cleanupAndExit(message) {
  clearInterval(interval);
  process.stdout.write('\x1B[?25h'); // Show cursor
  process.stdout.write('\n' + message + '\n');
  process.exit(0);
}

process.on('SIGTERM', () => cleanupAndExit('Received SIGTERM. Exiting...'));
process.on('SIGINT', () => cleanupAndExit('Interrupted. Exiting...'));
