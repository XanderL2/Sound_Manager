# Sound_Manager

## Bienvenida
Hola, en complemento al entorno Linux he creado un pequeño Script que automatiza la ejecucion de los comandos largos de la utilidad Pactl de Pulse audio, el cual te permite subir y bajar volumen de manera rapida y automatica. Es muy simple, solo almacenas el script de manera local y creas un alias en la configuracion de tu Shell de preferencia, en mi caso uso ZSH. Dicho eso dejo imagenes de la herramienta de terminal: 


## Preview
Menu de acciones: 

![enter image description here](https://raw.githubusercontent.com/XanderL2/sound_manager/main/preview/preview.jpeg)

![enter image description here](https://raw.githubusercontent.com/XanderL2/sound_manager/main/preview/preview1.jpeg)

## Dependencias:
Solo necesitamos instalar PulseAudio desde los repositorios de nuestra distribucion:

Para Distribuciones basadas en Debian:

    sudo apt install pulseaudio

Para ArchLinux:

    sudo pacman -S pulseaudio
