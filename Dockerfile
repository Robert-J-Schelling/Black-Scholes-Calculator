
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip install python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
RUN pip install matplotlib
RUN apt install libgl1-mesa-glx
COPY . .


CMD [ "python", "./DesktopApp/interface.py" ]
