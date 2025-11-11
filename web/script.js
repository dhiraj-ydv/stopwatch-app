let timerInterval = null;

async function updateTime() {
  const time = await window.pywebview.api.get_time();
  document.getElementById('time').innerText = time.toFixed(2);
}

function start() {
  window.pywebview.api.start();
  if (!timerInterval) {
    timerInterval = setInterval(updateTime, 100);
  }
}

function stop() {
  window.pywebview.api.stop();
  clearInterval(timerInterval);
  timerInterval = null;
}

async function reset() {
  await window.pywebview.api.reset();
  document.getElementById('time').innerText = '0.00';
  clearInterval(timerInterval);
  timerInterval = null;
}
