# Studienarbeit mit dem Raspberry Pi 5

Diese Studienarbeit beschäftigt sich mit der praktischen Anwendung von Jupyter Notebooks auf dem Raspberry Pi 5 zur Steuerung verschiedener elektronischer Komponenten und Schaltungen. Die Arbeit ist in sieben verschiedene Projekte gegliedert, die jeweils unterschiedliche Aspekte der Hardwaresteuerung und Datenerfassung abdecken. Das Ziel ist es, ein tiefes Verständnis für die grundlegende Elektronik und die Programmiermöglichkeiten mit dem Raspberry Pi zu vermitteln und dabei den Einsatz von Jupyter Notebooks als Entwicklungs- und Dokumentationsumgebung zu nutzen.

Die Studienarbeit deckt folgende Hauptthemen ab:
- **LED-Steuerung und PWM (Pulsweitenmodulation):** Wie einfache elektrische Komponenten über GPIO (General Purpose Input/Output) gesteuert werden können.
- **Temperatur- und Bewegungssensorik:** Erfassung und Visualisierung von Umweltdaten in Echtzeit mit Matplotlib.
- **Servomotorsteuerung:** Verwendung der PWM-Technik zur präzisen Steuerung von Motoren.
- **Komplexe Sensorik:** Erfassung und Auswertung von Daten eines 9-Achsen-Sensors.


## Überblick

Die Projekte wurden von Ashraf Yahya (AY) und Ahmad Sajad Faiz (AF) gemeinsam entwickelt, wobei sie sich jeweils auf bestimmte Teilprojekte konzentriert haben:
- **Gemeinsame Projekte:** [LED-Steuerung](./LED_Projekt/LED_Projekt.ipynb) und [Temperatursensor](./TempSensor_Projekt/TemperaturSensor_Projekt.ipynb)
- **Projekte von Ashraf Yahya:** [Servo Motor](./ServoMotor_Projekt/ServoMotor_Projekt.ipynb), [Temperatursensor mit Buzzer und LED](./BME680_Buzzer_LED_Projekt/Raspberry_Pi_LED_Buzzer_BME680_Notebook.ipynb) und [DEBO SENS 9AXIS Sensor](./DEBO_SENS_9AXIS/DEBO_SENS_9AXIS_Sensor_Notebook.ipynb) als extra Aufgabe
- **Projekte von Ahmad Sajad Faiz:** [LED Display](./LED_Display/LED_Disp.ipynb) und [Motion Sensor](./Motion_Sensor/MotionSensor.ipynb)

Diese Aufteilung ermöglicht es, die verschiedenen Fähigkeiten und Interessen der Autoren zur Geltung zu bringen und ihre jeweiligen Ansätze zur Lösung technischer Herausforderungen zu dokumentieren.


## Projekte

1. **Projekt 1: [LED-Steuerung](./LED_Projekt/LED_Projekt.ipynb) (Gemeinsam)**  
   Steuerung von LEDs mithilfe von PWM-Signalen auf dem Raspberry Pi, um grundlegende Konzepte der GPIO-Programmierung und Helligkeitssteuerung zu vermitteln.  
   Notebooks: [LED_Projekt.ipynb](./LED_Projekt/LED_Projekt.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

2. **Projekt 2: [Temperatursensor](./TempSensor_Projekt/TemperaturSensor_Projekt.ipynb) (Gemeinsam)**  
   Misst die Umgebungstemperatur und stellt die Daten in Echtzeit mit der Matplotlib-Bibliothek als Diagramm dar. Dieses Projekt bietet Einblicke in die Datenerfassung und -visualisierung.  
   Notebooks: [TemperaturSensor_Projekt.ipynb](./TempSensor_Projekt/TemperaturSensor_Projekt.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

3. **Projekt 3: [Servo Motor](./ServoMotor_Projekt/ServoMotor_Projekt.ipynb) (Ashraf Yahya)**  
   Der Servomotor wird in verschiedene Winkelpositionen zwischen 0 und 180 Grad gesteuert, um die Prinzipien der PWM-Anwendung auf Motorsteuerung zu demonstrieren.  
   Notebooks: [ServoMotor_Projekt.ipynb](./ServoMotor_Projekt/ServoMotor_Projekt.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

4. **Projekt 4: [Temperatursensor mit Buzzer und LED](./BME680_Buzzer_LED_Projekt/Raspberry_Pi_LED_Buzzer_BME680_Notebook.ipynb) (Ashraf Yahya)**  
   Ein BME680-Sensor überwacht die Temperatur und aktiviert bei einem bestimmten Schwellenwert eine LED und einen Buzzer, die ein SOS-Signal senden. Dieses Projekt zeigt den Einsatz von Sensoren zur Umgebungsüberwachung und Alarmierung.  
   Notebooks: [Raspberry_Pi_LED_Buzzer_BME680_Notebook.ipynb](./BME680_Buzzer_LED_Projekt/Raspberry_Pi_LED_Buzzer_BME680_Notebook.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

5. **Projekt 5: [DEBO SENS 9AXIS Sensor](./DEBO_SENS_9AXIS/DEBO_SENS_9AXIS_Sensor_Notebook.ipynb) (Ashraf Yahya)**  
   Der DEBO SENS 9AXIS Sensor wird zur Erfassung von Bewegungs- und Lageinformationen verwendet. Die erfassten Daten werden analysiert und mit geeigneten Funktionen dargestellt.  
   Notebooks: [DEBO_SENS_9AXIS_Sensor_Notebook.ipynb](./DEBO_SENS_9AXIS/DEBO_SENS_9AXIS_Sensor_Notebook.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

6. **Projekt 6: [LED Display](./LED_Display/LED_Disp.ipynb) (Ahmad Sajad Faiz)**  
   Die 8x8-LED-Matrix zeigt verschiedene Muster und Animationen an. Mithilfe des Freenove Projects Kit wird die Ansteuerung und kreative Nutzung der LED-Matrix demonstriert.  
   Notebooks: [LED_Disp.ipynb](./LED_Display/LED_Disp.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks

7. **Projekt 7: [Motion Sensor](./Motion_Sensor/MotionSensor.ipynb) (Ahmad Sajad Faiz)**  
   Der HC-SR501-Bewegungssensor erkennt Bewegung und signalisiert dies durch eine blinkende LED. Dieses Projekt verdeutlicht die Grundlagen der Bewegungserkennung.  
   Notebooks: [MotionSensor.ipynb](./Motion_Sensor/MotionSensor.ipynb)  
   Weiteres: Ordner, namens Bilder, mit verlinkten Bilder zu Notebooks
  
    

## Allgemeine Notebooks
- **[Einführung in Freenove Kit.ipynb](Einführung%20in%20Freenove%20Kit.ipynb)**: 
Einführung in die Nutzung des Freenove Kits, das in verschiedenen Projekten zur Steuerung und Sensorik verwendet wird.  

- **[Einführung in Matplotlib.ipynb](Einführung%20in%20Matplotlib.ipynb)**: 
Einführung in die Matplotlib-Bibliothek zur Datenvisualisierung, die in Projekten zur Anzeige von Sensordaten verwendet wird.  

- **[Installationen.ipynb](Installationen.ipynb)**: 
Notwendige Installationsanweisungen für Bibliotheken und Abhängigkeiten auf dem Raspberry Pi, um die Projekte auszuführen.  

- **[Rasp_Pi_Einrichtung.ipynb](Rasp_Pi_Einrichtung.ipynb)**: 
Einrichtung und Konfiguration des Raspberry Pi für die Nutzung mit Jupyter Notebooks und weiteren Projekten.  

- **[Raspberry_Pi_Kommunikation.ipynb](Raspberry_Pi_Kommunikation.ipynb)**: 
Einführung in die Kommunikation und Steuerung zwischen dem Raspberry Pi und externen Geräten.  

- **[Raspberry_Pi_AccessPoint_Setup.md](RaspberryPi_AccessPoint_Setup.md)**: 
Anleitung zur Konfiguration des Raspberry Pi als Access Point, um eine drahtlose Netzwerkverbindung für die Projekte bereitzustellen.  

- **[RaspberryPi_Jupyter_Grundlagen.ipynb](RaspberryPi_Jupyter_Grundlagen.ipynb)**: 
Grundlagen zur Nutzung von Jupyter Notebooks auf dem Raspberry Pi, inklusive Tipps zur Code-Entwicklung und -Ausführung.


## Ziel der Studienarbeit  

Das Ziel dieser Studienarbeit ist es, die Grundlagen der Elektronik, Sensortechnik und Aktorsteuerung auf dem Raspberry Pi zu vermitteln. Jedes Projekt wurde so gestaltet, dass es praktische Erfahrungen in der Arbeit mit elektronischen Komponenten bietet und einen fundierten Einstieg in die Entwicklung und Umsetzung von IoT-Anwendungen gibt. Zudem wird der Einsatz von Jupyter Notebooks als effektives Werkzeug für die Dokumentation und Ausführung von Code hervorgehoben.

Die Studienarbeit kann sowohl als Grundlage für Einsteiger in die Elektronik als auch als Referenz für fortgeschrittene Anwender dienen, die Interesse an IoT-Projekten und der Arbeit mit dem Raspberry Pi haben.

## Autoren

- **Ashraf Yahya (AY)**
- **Ahmad Sajad Faiz (AF)**  