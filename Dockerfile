FROM python:3
WORKDIR /usr/src/app
RUN pip install QDarkStyle
RUN pip install matplotlib
RUN pip install PyQt5
RUN pip install QuantLib-Python
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libxkbcommon-x11-0
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    apt-utils \
    dirmngr \
    gnupg \
    libasound2 \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    libxrender1 \
    libx11-xcb-dev \
    libx11-xcb1 \
    libxt6 \
    xz-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y python-pip \
      vim \
      wget \
      x11-utils \
      xfonts-base \
      xpra
COPY . .

CMD [ "python", "./DesktopApp/interface.py" ]
