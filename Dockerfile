FROM python:3
WORKDIR /usr/src/app
RUN pip install QDarkStyle
RUN pip install matplotlib
RUN pip install PyQt5
RUN pip install QuantLib-Python
COPY . .

CMD [ "python","-u", "./DesktopApp/interface.py" ]
