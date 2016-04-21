#Judas Iscaribot

Built with a Raspberry pi, two leds, and a wifi dongle
  Detects unsecured wifi networks 
  Connects to networks
  Captures network packets
  Tweets out pertinent information from packets
  May also shout things out via onboard speaker for funsies

##Dependencies
  Python Package Index
	- sudo apt-get install pyton-pip
  wifi python package
	- pip install wifi
  wireshark
	- sudo apt-get install wireshark
  airmon-ng
  libcap2-bin

Enable root privileges for wireshark dumpcap
  sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap


##Research docs
  Python wifi library https://wifi.readthedocs.org/en/latest/scanning.html#discovering-networks
  Reading packets https://www.wireshark.org/docs/man-pages/tshark.html
  Hootsuite via CL https://blog.hootsuite.com/termtter-acquisition/

