
FROM ubuntu:18.04

WORKDIR /usr/src/app

RUN adduser --quiet --disabled-password qtuser

# Install Python 3, PyQt5
RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pyqt5
      
RUN pip install QuantLib-Python
RUN pip install QDarkStyle
RUN pip install matplotlib
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
