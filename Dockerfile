
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

CMD [ "python", "./DesktopApp/interface.py" ]
