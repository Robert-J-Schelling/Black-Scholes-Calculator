
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip install python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
COPY . .

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev

CMD [ "python", "./DesktopApp/interface.py" ]
