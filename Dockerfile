
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip istall python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
