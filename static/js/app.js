// Keep feedback visible long enough to read on narrow screens.
document.querySelectorAll('.flash').forEach(message => {
  window.setTimeout(() => { message.style.opacity = '0'; message.style.transition = 'opacity .3s'; }, 4800);
  window.setTimeout(() => message.remove(), 5150);
});
