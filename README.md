# LoRaRasP
Библиотека для общения с LoRa-модулем по шине SPI

LoRa_receiver - стартовый файл;  
print_LoRa_receiver - тот же файл, но отправляет в консоль, а не на сервер (для проверки);  
zip-архив содержит файлы для контейнеров docker-compose. 

Для работы необходимо установить следующие библиотеки:  
- spidev
- RPi.GPIO
- pika

Также для работы нужно, чтобы был включён SPI-модуль, проверить можно введя в терминале команду "ls /dev/".  
Если есть 'spidev0.0' и 'spidev0.1', то SPI включена.  
Если их нет вводим в терминал команду "sudo raspi-config"  
Далее выбираем: Interfacing options -> SPI -> Enabled  
Если spidev сразу не появились - перезагружаемся.  

Для работы docker-compose в файле docker-compose.yml в строчке пути файла:  
volumes:  
  - "/home/pi/GH/lora_receiver/text.txt:/home/pi/Documents/text.txt"  
прописать путь к папке lora_receiver, в левой части пути:  
  - "{путь}/lora_receiver/text.txt:/home/pi/Documents/text.txt"  

Выходы Raspberry PI:  
SPI1: 21(GPIO09), 19(GPIO10), 23(GPIO11), 24(GPIO08).   
DIO0 - 36 (GPIO16); DIO1 - 38 (GPIO20);
Reset: 22 (GPIO25).  

Настроить их можно в файле LoRa_receiver.
