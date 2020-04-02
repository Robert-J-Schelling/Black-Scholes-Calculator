
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip install python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
RUN pip install matplotlib
COPY . .
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libxkbcommon-x11-0
RUN apt-get -qq update && sudo apt-get -y -qq install bison build-essential gperf flex ruby python libasound2-dev libbz2-dev libcap-dev libcups2-dev libdrm-dev libegl1-mesa-dev libgcrypt11-dev libnss3-dev libpci-dev libpulse-dev libudev-dev libxtst-dev gyp ninja-build && sudo apt-get -qq clean
RUN apt-get -qq update && sudo apt-get -y -qq install libssl-dev libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libfontconfig1-dev libxss-dev libsrtp0-dev libwebp-dev libjsoncpp-dev libopus-dev libavutil-dev libavformat-dev libavcodec-dev libevent-dev libxslt1-dev && sudo apt-get -qq clean

RUN apt-get -qq update && sudo apt-get -y -qq install lxde xinit && sudo apt-get -qq clean
RUN /usr/share/debconf/fix_db.pl #or sudo apt-get -y -qq remove miscfiles dictionaries-common
RUN echo "exec startlxde" >> $HOME/.xinitrc
RUN startx &

CMD [ "python", "./DesktopApp/interface.py" ]
