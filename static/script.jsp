// 點擊頭像顯示 QR Code 浮層
document.getElementById('avatar-trigger').addEventListener('click', () => {
  document.getElementById('qr-overlay').classList.add('active');
  new QRCode(document.getElementById('qrcode-overlay'), {
    text: "https://yourdomain.com/e-card",
    width: 192,
    height: 192,
    colorDark: "#000000",
    colorLight: "#ffffff",
    correctLevel: QRCode.CorrectLevel.H
  });
});

// 點擊浮層關閉 QR Code
document.getElementById('qr-overlay').addEventListener('click', () => {
  document.getElementById('qr-overlay').classList.remove('active');
  document.getElementById('qrcode-overlay').innerHTML = '';
});
