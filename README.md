Control scripts for an H0 DC loco using [gpiozero](https://gpiozero.readthedocs.io/en/stable/api_output.html#motor)

#### Hardware:
- DC controlled set (e.g. [this](https://www.trix.de/en/products/details/article/21530/1851/?tx_torrpdb_pi1%5Bbacklink%5D=1851&tx_torrpdb_pi1%5Bpage%5D=1&tx_torrpdb_pi1%5Bperpage%5D=10&tx_torrpdb_pi1%5Bera%5D=&tx_torrpdb_pi1%5Bnewonly%5D=0&tx_torrpdb_pi1%5Bgaugechoice%5D=8&tx_torrpdb_pi1%5Bgroupchoice%5D=10&tx_torrpdb_pi1%5Bsubgroupchoice%5D=28&tx_torrpdb_pi1%5Bfilter%5D=1&tx_torrpdb_pi1%5Bpagesort%5D=artnrasc&tx_torrpdb_pi1%5BbrandId%5D=2&tx_torrpdb_pi1%5BnoPaging%5D=))
- RPi (I used a zero)
- L298N H-bridge (e.g. [this](https://www.amazon.com/Qunqi-Controller-Module-Stepper-Arduino/dp/B014KMHSW6?ref_=fsclp_pl_dp_1))
- [PIR motion sensor](https://wiki.dfrobot.com/PIR_Motion_Sensor_V1.0_SKU_SEN0171)
- DuPont cables
- 12v power supply

#### Software:
- Python 3

You'll need to run `pip install gpiozero`

Some scripts may not work that elegantly right now. `pir-pwm.py` is the most refined.

![alt text](https://github.com/mahtDFR/pytrain/blob/master/resources/demo.gif "Demo")

See a complete demo video of it running [here](resources/demo.mp4).

Comments and contributions welcome.