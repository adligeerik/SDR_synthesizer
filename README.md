# Remote controlled switch recorded and synthesized with a SDR

In this project I have recorded the transmitted signal from a remote to a power switch, commonly used turn off lamps with a remote instead of using the switch plased on the wall. There are many such products on the market and the one I have been using is from [Luxorparts](https://www.kjell.com/se/produkter/el-verktyg/smarta-hem/433-mhz/fjarrstrombrytare/utanpaliggande-brytare/luxorparts-fjarrstrombrytare-1000-w-2-pack-p50969). All (well most of them) similar products use the same part of the spectrum and often the same frequency, which is 433.92 Mhz which it was in my case.

Eaven though that do not need to walk all the way to the wall mounted switch i still need to have the remote nearby, but what if the remote is not next to me? The solution is to record the transmitted signal with a SDR and then replay SDR. Easy!


## Hardware used
* [HackRF one](https://greatscottgadgets.com/hackrf/one/)
* Homemade antenna (see images)
* Oscilloscope (for debugging)
* 433.92Mhx receiver (also for debugging)

## The programs

### Recorder
The recorder is listening on 433.92Mhz, the threshold block makes the sampled data "cleaner" and makes it easier post process it. In Fig 3 a recived signal is desplayed, "0" is coded as a short poulse and a "1" as a long pulse.

### Synthesizer
Construct a vector from the variables the maps a "0" to 0x3C0 (0b1111000000, "short" pulse), "1" to 0xffff (b01111111111111111, "long" pulse) and "2" to 0x000 for spacing between messages. Converts to float and then repeats them 265 times for the right time lenghts. The mulitply by one needs to because otherwise the float to complex would not work. And then the signal is transmitted on 433.92Mhz

## Flow graps and message plot

![Recorder](https://github.com/adligeerik/SDR_synthesizer/blob/master/plots_and_photos/record.png)
*Fig 1, recorder flow graph*

![synthesizer](https://github.com/adligeerik/SDR_synthesizer/blob/master/plots_and_photos/syntesiser.png)
*Fig 2, replayer flow graph*

![received message](https://github.com/adligeerik/SDR_synthesizer/blob/master/plots_and_photos/threshold_lamp_a_on.png)
*Fig 3, received message*

## Tricks and tips
Double check that the timeing and length on transmitted bits are right.


