FROM python:3
WORKDIR /usr/src/app
RUN pip install QDarkStyle
RUN pip install matplotlib
RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libxkbcommon-x11-0 \
    libqt5x11extras5 
RUN export QT_DEBUG_PLUGINS=1
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
