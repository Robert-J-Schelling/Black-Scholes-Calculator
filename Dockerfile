FROM ubuntu:18.04
# Add user
RUN adduser --quiet --disabled-password qtuser

# Install Python 3, PyQt5
RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pyqt5
      
FROM python:3

WORKDIR /usr/src/app

RUN pip install QDarkStyle
RUN pip install matplotlib
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN export QT_DEBUG_PLUGINS=1
RUN apt-get install -y libxkbcommon-x11-0
COPY . .
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
