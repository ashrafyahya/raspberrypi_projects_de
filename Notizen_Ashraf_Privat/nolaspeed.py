from mpu6050 import mpu6050
import xlsxwriter
import time
import os
import RPi.GPIO as GPIO

# Sensor initialisieren
mpu = mpu6050(0x68)

# Speicherpfad definieren
speicherpfad = '/media/user1/USBNOLA/NolaACC.xlsx'

# überprüfen, ob die Datei existiert
if os.path.isfile(speicherpfad):
    try:
        os.remove(speicherpfad)
        print("Speicherpfad existiert bereits und wird gelöscht.")
    except OSError as e:
        print("Fehler beim Löschen der bestehenden Datei:", e)

# Neue Excel Datei erstellen und Worksheet erstellen
workbook = xlsxwriter.Workbook(speicherpfad)
worksheet = workbook.add_worksheet()

# Spaltengröße ändern
worksheet.set_column('A:G', 12)

# Formate erstellen
bold = workbook.add_format({'bold': True})
bold_red = workbook.add_format({'bold': True, 'font_color': 'red'})

# Pin-Nummer festlegen für Schalter
SWITCH_PIN = 23

# GPIO-Modus festlegen
GPIO.setmode(GPIO.BCM)

# Pins als Eingang festlegen und Pull-up-Widerstände aktivieren
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialer Zustand des Schalters
last_switch_state = GPIO.input(SWITCH_PIN)

# Pfad abrufen für LED Infos
led_brightness_path = "/sys/class/leds/ACT/brightness"
led_trigger_path = "/sys/class/leds/ACT/trigger"

# LED Counter für Entry und Exit blinken
ledcount1 = 0
ledcount2 = 0

# Funktion zum Setzen der LED-Helligkeit
def set_led_brightness(value):
    with open(led_brightness_path, 'w') as f:
        f.write(str(value))

# Funktion zum Setzen des LED-Triggers (um sicherzustellen, dass die LED manuell gesteuert wird)
def set_led_trigger(trigger):
    with open(led_trigger_path, 'w') as f:
        f.write(trigger)

# Funktion zum Herunterfahren des Pi
def shutdown():
    os.system("sudo shutdown -h now")

# Manuelle Steuerung der LED einstellen
set_led_trigger("none")

def blink():
    set_led_brightness(1)  # LED einschalten
    time.sleep(0.05)        # 0,05 Sekunden warten
    set_led_brightness(0)  # LED ausschalten
    time.sleep(0.05)        # 0,05 Sekunden warten
    set_led_brightness(1)  # LED einschalten
    time.sleep(0.05)        # 0,05 Sekunden warten
    set_led_brightness(0)  # LED ausschalten
    time.sleep(0.05)        # 0,05 Sekunden warten
    set_led_brightness(1)  # LED einschalten
    time.sleep(0.05)        # 0,05 Sekunden warten
    set_led_brightness(0)  # LED ausschalten
    time.sleep(0.5)         # 0,5 Sekunden warten

def main():
    global last_switch_state
    global ledcount1
    global ledcount2

    xcountermax = 1
    x_max = 0
    y_max = 0
    z_max = 0

    while True:
        # Blinken zum signalisieren dass Messung bereit ist
        while ledcount1 < 7:
            blink()
            ledcount1 += 1

        # Aktueller Zustand des Schalters
        current_switch_state = GPIO.input(SWITCH_PIN)

        # überprüfen, ob sich der Zustand des Schalters geändert hat
        if current_switch_state != last_switch_state:
            last_switch_state = current_switch_state

            if current_switch_state == GPIO.HIGH:
                print("Die Messung wird beendet und gespeichert!\n")
                worksheet.write(xcountermax, 4, x_max, bold_red)
                worksheet.write(xcountermax, 5, y_max, bold_red)
                worksheet.write(xcountermax, 6, z_max, bold_red)
                workbook.close()
                print("Excel Datei gespeichert!\n")
                while ledcount2 < 7:
                    blink()
                    ledcount2 += 1
                set_led_trigger("mmc0")
                shutdown()

            else:
                # Tabelle beschriften
                worksheet.write('A1', 'Acc X', bold)
                worksheet.write('B1', 'Acc Y', bold)
                worksheet.write('C1', 'Acc Z', bold)
                worksheet.write('E1', 'MaxAcc X', bold)
                worksheet.write('F1', 'MaxAcc Y', bold)
                worksheet.write('G1', 'MaxAcc Z', bold)

                # Berechnung
                xcounterall = 1
                y = 0

                while current_switch_state == GPIO.LOW:
                    accel_data = mpu.get_accel_data()
                    worksheet.write(xcounterall, y, accel_data['x'])
                    worksheet.write(xcounterall, y + 1, accel_data['y'])
                    worksheet.write(xcounterall, y + 2, (accel_data['z'] - 9.81))

                    x_temp = abs(accel_data['x'])
                    if x_temp > x_max:
                        x_max = x_temp

                    y_temp = abs(accel_data['y'])
                    if y_temp > y_max:
                        y_max = y_temp

                    z_temp = abs(accel_data['z'] - 9.81)
                    if z_temp > z_max:
                        z_max = z_temp

                    print("ACC X : " + str(accel_data['x']))
                    print("ACC Y : " + str(accel_data['y']))
                    print("ACC Z : " + str(accel_data['z'] - 9.81))
                    print("-------------------------------")
                    time.sleep(0.1)
                    xcounterall += 1
                    current_switch_state = GPIO.input(SWITCH_PIN)

if __name__ == "__main__":
    main()
