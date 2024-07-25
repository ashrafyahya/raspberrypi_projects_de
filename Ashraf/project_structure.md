# Raspberry Pi Projekt mit Jupyter Notebook

## 1. Einführung
### Projektziel
Das Ziel dieses Projekts ist es, den Raspberry Pi mithilfe von Jupyter Notebook zu steuern und dabei verschiedene Schaltungen unter Berücksichtigung von Widerständen zu erstellen und zu testen.

### Hintergrund
Der Raspberry Pi ist ein vielseitiger Einplatinencomputer, der häufig in Elektronikprojekten verwendet wird. Jupyter Notebook ist ein interaktives Entwicklungswerkzeug, das es ermöglicht, Code in Echtzeit auszuführen und Ergebnisse direkt zu visualisieren.

### Relevanz
Dieses Projekt ist relevant, da es die Grundlagen der Elektronik und Programmierung kombiniert und praktische Anwendungen wie die Steuerung von Hardware und Datenerfassung ermöglicht.

## 2. Materialien und Werkzeuge
### Raspberry Pi Modell
- **Modell:** Raspberry Pi 4 Model B
- **Spezifikationen:** 4GB RAM, Quad-Core 64-bit ARM Cortex-A72

### Jupyter Notebook
Jupyter Notebook ist eine Open-Source-Webanwendung, die es ermöglicht, Dokumente mit Live-Code, Gleichungen, Visualisierungen und erläuterndem Text zu erstellen und zu teilen.

### Zusätzliche Hardware
- Breadboard
- Jumper-Kabel
- LEDs
- Widerstände (verschiedene Werte)
- Taster
- Sensoren (z.B. Temperatur, Feuchtigkeit)

### Software
- Raspbian OS
- Python 3
- Jupyter Notebook

## 3. Grundlagen und Theorie
### Elektrische Grundlagen
- **Spannung (V):** Der elektrische Potentialunterschied.
- **Strom (I):** Der Fluss von Elektronen durch einen Leiter.
- **Widerstand (R):** Der Widerstand gegen den Stromfluss, gemessen in Ohm (Ω).

### Schaltkreise
- **Serienschaltung:** Komponenten sind in einer Reihe geschaltet.
- **Parallelschaltung:** Komponenten sind parallel zueinander geschaltet.

### Widerstände
- **Funktion:** Begrenzen den Stromfluss und teilen Spannungen.
- **Berechnung:** Ohm'sches Gesetz: \( V = I \cdot R \)

## 4. Datenblatt und Komponenten
### Datenblattanalyse
- **Widerstände:** Lesen der Toleranz und Nennwerte.
- **LEDs:** Vorwärtsspannung und -strom.

### Beispiele
- Auszüge aus dem Datenblatt eines 220Ω Widerstands.
- Spezifikationen einer Standard-LED.

## 5. Schaltungsdesign
### Schaltplan
![Schaltplan](path/to/schaltplan.png)

### Komponentenauswahl
- **Widerstände:** 220Ω für LED-Schutz.
- **LED:** Standard 5mm LED.

## 6. Implementierung
### Hardware-Aufbau
1. Raspberry Pi aufstellen und mit Strom versorgen.
2. Komponenten auf dem Breadboard platzieren und verkabeln.

### Software-Setup
1. Raspbian OS installieren.
2. Python und Jupyter Notebook installieren:
    ```sh
    sudo apt-get update
    sudo apt-get install python3 jupyter
    ```

### Code
```python
import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# LED Blinken
try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


# Raspberry Pi Projekt mit Jupyter Notebook

## 7. Experimente und Ergebnisse
### Versuchsaufbau
Beschreibung der durchgeführten Experimente, z.B. LED-Blinken, Taster-Eingabe.

### Datenerfassung
Nutzung von Jupyter Notebook zur Datenerfassung und Analyse.

### Ergebnisse
Diagramme und Tabellen der erfassten Daten.

## 8. Diskussion und Fazit
### Diskussion
Analyse der Ergebnisse, z.B. erfolgreiche Steuerung der LED, Herausforderungen bei der Verkabelung.

### Verbesserungsmöglichkeiten
Einsatz von komplexeren Sensoren und Aktoren.
Automatisierte Datenerfassung und Analyse.

### Fazit
Zusammenfassung der wichtigsten Erkenntnisse und Erfolge des Projekts.

## 9. Anhänge
### Quellcode
Vollständiger Python-Code.

### Datenblätter
Datenblätter der verwendeten Komponenten.

### Zusätzliche Ressourcen
Links zu Tutorials, Dokumentationen, etc.

## 10. Literaturverzeichnis
Auflistung aller verwendeten Quellen und Literatur.

## 
