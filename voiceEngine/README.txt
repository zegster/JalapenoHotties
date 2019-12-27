=====Working with voice engine on a PC=====
1) Download latest version of sphinxbase and pocketsphinc
--> wget https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O sphinxbase.tar.gz
--> wget https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O pocketsphinx.tar.gz

2) Extract files into separate directories
--> tar -xzvf sphinxbase.tar.gz
--> tar -xzvf pocketsphinx.tar.gz

3) Install bison, ALSA, and swig
--> sudo apt-get install bison libasound2-dev swig

4) Compile sphinxbase
--> cd sphinxbase-5prealpha
    ./configure --enable-fixed
    make
    sudo make install

5) Compile pocketsphinx
--> cd ../pocketsphinx-5prealpha
    ./configure
    make
    sudo make install

6) Test installation
--> src/programs/pocketsphinx_continuous -samprate 48000

7) Additonal instruction: https://pypi.org/project/pocketsphinx/
8) In case you have pyaudio issue:
	1) sudo pip install pyaudio (if this doesn't work, you have to manually install it)
		- If it doesn't work, go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
			- Download your apprroriate version. For example, if you python is 3.7 and 64bit...
				PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
			- Video on how to: https://www.youtube.com/watch?v=AKymlea8sYM
	2) sudo pip install SpeechRecognition 

All instruction and additional steps is already documented in official link:
https://cmusphinx.github.io/wiki/tutorial/

Python Example: https://www.programcreek.com/python/example/107721/speech_recognition.Recognizer


=====Working with the Raspberry Pi=====
1. Install SWIG
	Link: https://cmusphinx.github.io/wiki/raspberrypi/
2. Open console and install the necessary packages
	sudo python3 -m pip3 install --upgrade pip setuptools wheel
	pip install --upgrade pocketsphinx
	Link: http://www.jamesrobertson.eu/blog/2016/jan/16/installing-pockets.html

=====From scratch instructions=====
1. Install Rasberrian
2. Run update
	(maybe-fix repositories)  (didn't have to on the raspberry)

3. Did the first 3 sets of command instructions
	https://cmusphinx.github.io/wiki/raspberrypi/

4. Followed all of the the website
	https://cmusphinx.github.io/wiki/tutorialpocketsphinx/

5. In sphinxbase
	sudo ./autogen.sh
	sudo ./configure
	sudo make
	sudo make install

6. In pocketsphinx
	sudo ./autogen.sh
	sudo ./configure
	sudo make
	sudo make install

7. Additional information
	https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
	https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
