
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip install python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
RUN pip install matplotlib
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN export QT_DEBUG_PLUGINS=1
COPY . .


CMD [ "python", "./DesktopApp/interface.py" ]
