var wyliodrin = require("wyliodrin");


wyliodrin.pinMode (2, 0);



function loopCode()
{
  wyliodrin.sendSignal('Water_sensor', wyliodrin.digitalRead (2));
  if ((wyliodrin.digitalRead (2)) == true) {
    console.log('Empty');
  }
}
setInterval(loopCode, 1000);
