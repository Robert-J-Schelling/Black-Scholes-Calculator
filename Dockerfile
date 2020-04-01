
FROM python:3

WORKDIR /usr/src/app


RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN pip install PyQt5-sip
RUN pip install python-qt
RUN pip install QDarkStyle
RUN pip install QtPy
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]

docker build -t xeyes - << __EOF__
FROM debian
RUN apt-get update
RUN apt-get install -qqy x11-apps
ENV DISPLAY :0
CMD xeyes
__EOF__
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
docker run -ti -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH xeyes
