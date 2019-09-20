# Remote controlled switch recorded and synthesized with a SDR

In this project I have recorded the transmitted signal from a remote to a power switch, commonly used turn off lamps with a remote instead of using the switch plased on the wall. There are many such products on the market and the one I have been using is from [Luxorparts](https://www.kjell.com/se/produkter/el-verktyg/smarta-hem/433-mhz/fjarrstrombrytare/utanpaliggande-brytare/luxorparts-fjarrstrombrytare-1000-w-2-pack-p50969). All (well most of them) similar products use the same part of the spectrum and often the same frequency, which is 433.92 Mhz which it was in my case.

Eaven though that do not need to walk all the way to the wall mounted switch i still need to have the remote nearby, but what if the remote is not next to me? The solution is to record the transmitted signal with a SDR and then replay them with the same SDR. Easy!


## Hardware used
* [HackRF one](https://greatscottgadgets.com/hackrf/one/)
* Homemade antenna (see images)
* Oscilloscope (for debugging)
* 433.92Mhx receiver (also for debugging)






## Tricks and tips
