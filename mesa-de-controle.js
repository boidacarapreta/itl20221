input.onButtonPressed(Button.A, function () {
  bairro = bairro + 1;
  if (bairro >= 10) {
    bairro = 1;
  }
  basic.showString("" + bairro);
});
input.onButtonPressed(Button.B, function () {
  if (bairro > 0) {
    radio.sendNumber(bairro);
    basic.showIcon(IconNames.Yes);
  } else {
    basic.showIcon(IconNames.No);
  }
  basic.pause(1000);
  basic.showString("" + bairro);
});
let bairro = 0;
let canal = 100;
bairro = 0;
radio.setGroup(canal);
basic.showString("" + bairro);
