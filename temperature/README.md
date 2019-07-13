One-Wire Interface needs to be enabled first:

```
sudo dtoverlay w1-gpio gpiopin=4 pullup=0
```
Also w1thermsensor module needs to be installed:
```
pip install w1thermsensor
```

More details available here:

https://community.growbotics.ai/t/testing-temperature-sensor/90
