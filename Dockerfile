FROM python:3.7.5-buster

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY volux volux
COPY README.md .
COPY setup.py .
RUN python3 setup.py bdist_wheel
RUN pip install dist/*.whl

WORKDIR /usr/src/app/modules/voluxgui
COPY modules/voluxgui/requirements.txt .
RUN pip install -r requirements.txt
COPY modules/voluxgui/voluxgui voluxgui
COPY modules/voluxgui/README.md .
COPY modules/voluxgui/setup.py .
RUN python3 setup.py bdist_wheel
RUN pip install dist/*.whl

WORKDIR /usr/src/app
RUN apt-get update
RUN git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
WORKDIR /usr/src/app/pyaudio
# RUN apt-get --yes install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
# RUN apt-get --yes install libasound-dev portaudio19-dev libportaudiocpp0
RUN apt-get --yes install portaudio19-dev
RUN CACHEBUST=1 ls /usr/include
# RUN apt-get --yes install python3-dev
# RUN apt-get --yes install python3-pip
RUN CACHEBUST=1 ls
RUN CACHEBUST=1 python3 setup.py install
# RUN pip install pyaudio/dist/*.tar.gz

WORKDIR /usr/src/app/modules/voluxaudio
COPY modules/voluxaudio/requirements.txt .
RUN pip install -r requirements.txt
COPY modules/voluxaudio/voluxaudio voluxaudio
COPY modules/voluxaudio/README.md .
COPY modules/voluxaudio/setup.py .
RUN python3 setup.py bdist_wheel
RUN pip install dist/*.whl

RUN env

CMD [ "volux", "launch" ]

# FROM python:3.7.5-buster
#
# WORKDIR /usr/src/app
# COPY package.json .
# RUN npm install
# COPY . .
#
# CMD [ "npm", "start" ]
