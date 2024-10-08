
# Anleitung: Raspberry Pi 5 als WLAN Access Point einrichten

## Voraussetzungen

- Raspberry Pi 5 (oder ein Modell mit eingebautem WLAN)
- Raspberry Pi OS (Lite empfohlen, aber Desktop-Version funktioniert ebenfalls)
- Ethernet-Kabel für den Internetzugang

## Schritt 1: System aktualisieren

Stelle sicher, dass dein Raspberry Pi auf dem neuesten Stand ist, indem du diese Befehle ausführst:

```bash
sudo apt update
sudo apt upgrade
```

## Schritt 2: Installieren der benötigten Software

Um den Pi als Access Point einzurichten, benötigst du das `hostapd`-Paket (Access Point-Dienst) und `dnsmasq` (leichtgewichtiger DHCP-Server).

Installiere die Pakete mit:

```bash
sudo apt install hostapd dnsmasq
```

Aktiviere den `hostapd`-Dienst so, dass er beim Booten startet:

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
```

Wir starten die Dienste später, sobald alles konfiguriert ist.

## Schritt 3: Static IP für WLAN konfigurieren

Nun musst du dem WLAN-Interface `wlan0` eine statische IP-Adresse zuweisen.

Bearbeite die Datei `/etc/dhcpcd.conf`:

```bash
sudo nano /etc/dhcpcd.conf
```

Füge am Ende der Datei Folgendes hinzu:

```bash
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
```

Speichere die Datei und beende den Editor mit `Ctrl + X`, dann `Y` und `Enter`.

## Schritt 4: `dnsmasq` konfigurieren

Jetzt konfigurieren wir `dnsmasq`, um IP-Adressen an Geräte zu verteilen, die sich mit dem Access Point verbinden.

Benenne die Standardkonfigurationsdatei um:

```bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```

Erstelle dann eine neue Konfigurationsdatei:

```bash
sudo nano /etc/dnsmasq.conf
```

Füge Folgendes ein:

```bash
interface=wlan0      # Benutze das WLAN-Interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

Speichere die Datei und beende den Editor.

## Schritt 5: Konfiguration von `hostapd`

Bearbeite die Datei `/etc/hostapd/hostapd.conf`:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Füge Folgendes hinzu, um die Access Point-Einstellungen festzulegen:

```bash
interface=wlan0
ssid=MeinAccessPoint    # Name des WLANs
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=Passwort1234    # WLAN-Passwort
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

Speichere und beende den Editor.

Dann müssen wir noch sicherstellen, dass `hostapd` die Konfigurationsdatei verwendet:

Bearbeite die Datei `/etc/default/hostapd`:

```bash
sudo nano /etc/default/hostapd
```

Füge oder ändere die folgende Zeile:

```bash
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

## Schritt 6: Netzwerkweiterleitung aktivieren

Damit der Raspberry Pi als Router funktioniert und die Internetverbindung an die verbundenen Geräte weitergeben kann, musst du die Netzwerkweiterleitung aktivieren.

Bearbeite die Datei `/etc/sysctl.conf`:

```bash
sudo nano /etc/sysctl.conf
```

Entferne das `#` vor der Zeile:

```bash
net.ipv4.ip_forward=1
```

Aktiviere die Änderung sofort:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

## Schritt 7: IP-Tables konfigurieren

Um die Internetverbindung über das Ethernet-Interface `eth0` zu teilen, fügen wir eine Regel für `iptables` hinzu:

```bash
sudo apt install iptables
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

Speichere die Regel:

```bash
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

Bearbeite nun die Datei `/etc/rc.local`:

```bash
sudo nano /etc/rc.local
```

Füge die folgende Zeile **vor** `exit 0` hinzu:

```bash
iptables-restore < /etc/iptables.ipv4.nat
```

## Schritt 8: Dienste starten

Starte die Dienste, die du vorher konfiguriert hast:

```bash
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

Falls keine Fehlermeldungen erscheinen, wird der Access Point erfolgreich laufen!

## Schritt 9: Teste den Access Point

Jetzt kannst du versuchen, dich mit einem Gerät (z. B. Smartphone oder Laptop) mit dem WLAN `MeinAccessPoint` zu verbinden. Gib das zuvor festgelegte Passwort (`Passwort1234`) ein.

Wenn alles richtig konfiguriert ist, solltest du nun über den Raspberry Pi eine Internetverbindung haben.

---

**Hinweis:** Du kannst den WLAN-Namen (`ssid`) und das Passwort in der Datei `/etc/hostapd/hostapd.conf` jederzeit ändern, falls gewünscht.

https://www.elektronik-kompendium.de/sites/raspberry-pi/2002171.htm
