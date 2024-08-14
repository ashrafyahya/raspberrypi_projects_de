# Kommunikartion mit Raspberry Pi

## Steuerung durch SSH Verbindung  

**Schritt 1:** SSH auf dem Raspberry Pi aktivieren  
- Verbinden Sie sich direkt mit Ihrem Raspberry Pi (Monitor und Tastatur) oder greifen Sie über ein anderes Medium zu.  
- Öffnen Sie das Terminal und geben Sie ein:  
	```sudo raspi-config```  
- Navigieren Sie zu Interfacing Options > SSH und wählen Sie Enable.  

**Schritt 2:** SSH-Client auf Windows verwenden  
Auf Ihrem Windows Rechner gehen Sie die folgenden Anweisungen durch.  

- CMD öfnnen  
- Folgendes im Terminal bzw. im CMD eingeben  
	```ssh <username>@ <raspPi-IP>```  
	in meinem Fall ist das $ssh ashraf@192.168.0.104  
- Passwort eingeben  
- Navigieren Sie zu Ihrem Notebook
- Folgendes im Terminal bzw. im CMD eingeben  
	```ipython```  
	```%run your_script.ipynb```  
	in meinem Fall ist das dann $ %run 1_LED_Morsecode.ipynb.  
So wird der Code auf Ihrem RaspPi ausgeführt.  
--------------------------------------------------------------------
## Steuerung durch Netzwerkfreigabe
Steueren Sie Ihr Jupyter Notebook und somit das RaspberryPi aus eigenem Rechner, der sich im gleichen Netzwerk befindet.  
Gehen Sie die folgenden Schritten durch.  

- Zur virtuellen Umgebung wechseln, indem Sie im Terminal folgendes eingeben:  
	```cd venv```  
	$source bin/activate  
- Nutze den Befehl für die Freigabe im Netzwerk:  
	```jupyter notebook --ip <your_LAN_ip> --port 8888```  
- So ermitteln Sie Ihre Ip in RaspPi Terminal:  
	```hostname -I```  
- Im eignen Rechner in Browser folgendes eingeben:  
	```http://your_LAN_ip:8888```  
- Passwort eigeben, falls nicht vorhanden, geben Sie im Terminal von RaspPi folgendes:  
	```jupyter notebook password```  
    - Passwort eingeben und bestätigen  
- Gehen Sie zurück zu Ihrem Browser und geben Sie das Passwort ein.  
- Für weiteres folgendes gucken:  
	https://stackoverflow.com/questions/39155953/exposing-python-jupyter-on-lan  
--------------------------------------------------------------------
## Steuerung durch Kobination von SSH und Freigabe im Netzwerk  
Gehen Sie bitte die folgenden Schritte durch:  

- CMD öfnnen  
- Folgendes im Terminal bzw. im CMD eingeben  
	```ssh <username>@ <raspPi-IP>```  
- Passwort eingeben  
- Zur virtuellen Umgebung wechseln, indem Sie im Terminal folgendes eingeben:  
	```cd venv```  
	```source bin/activate```
- Nutze den Befehl für die Freigabe im Netzwerk:  
	```jupyter notebook --ip <your_LAN_ip> --port 8888```  
- Im eignen Rechner in Browser folgendes eingeben:  
	```http://your_LAN_ip:8888```  
--------------------------------------------------------------------  
**Vergewissen Sie sich, dass die virtuelle Umgebung venv heißt oder passen Sie anhand dessen die obigen Schritte.** 