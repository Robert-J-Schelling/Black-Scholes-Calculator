FROM ubuntu:18.04
WORKDIR /usr/src/app
# Add user
RUN adduser --quiet --disabled-password qtuser

# Install Python 3, PyQt5
RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pyqt5
      
FROM python:3

RUN pip install QDarkStyle
RUN pip install matplotlib
RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libxkbcommon-x11-0
RUN curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | sudo bash -s -- --update
RUN QT_QPA_PLATFORM=offscreen go test -v -race
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
