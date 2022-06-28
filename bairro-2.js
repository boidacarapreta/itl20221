radio.onReceivedNumber(function (receivedNumber) {
  if (receivedNumber == bairro) {
    basic.showIcon(IconNames.Yes);
    basic.pause(1000);
    basic.showString("" + bairro);
  }
});
let bairro = 0;
let canal = 100;
bairro = 2;
radio.setGroup(canal);
basic.showString("" + bairro);
