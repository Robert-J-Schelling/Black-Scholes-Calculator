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
ENV QT_DEBUG_PLUGINS=1
ENV QT_GRAPHICSSYSTEM=native
COPY . .

CMD [ "python","-u", "./DesktopApp/interface.py" ]
