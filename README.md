# Willkommen
Hey! Du willst programmieren lernen? Dann bist du hier genau richtig. Hier wirst du Schritt für Schritt zu deinem ersten selbstprogrammierten Programm hingeführt.

## Voraussetzungen
- GitHub Account (github.com - kostenlos)
- Replit Account (replit.com - kostenlos)
- Motivation

## Setup
So, an diesem Punkt solltest du bereits Accounts für die beiden vorher genannten Profile haben. Falls nicht, kannst du ganz einfach mit deiner studentischen E-Mail bei den Plattformen einen gratis Account anlegen.

Öffne nun replit.com und klicke auf das Plus rechts oben **New Repl**. Bei dem sich öffnenden Dialog, solltest du eine 
Dies ist ein eigener Arbeitsbereich, nur für dich. In diesem Arbeitsbereich wirst du all deine Programmieraufgaben erledigen.

Klicke auf den Knopf **Import from GitHub** und füge im Feld **GitHub Url** folgenden Link ein https://github.com/ndhbr-classroom/replit-template. Klicke auf **Import** und schon geht's los.

## Aufbau Replit
Im Linken Teil des Fensters solltest du nun eine Toolbar sehen. Standardmäßig selektiert sollte der Reiter **Files** sein. Wenn alles geklappt hat, solltest du bereits mehrere Dateien sehen.

Im mittleren Teil befindet sich der Editor. Hier wirst du deine eigentliche Programmierarbeit leisten.

Im rechten Teil befindet sich neben der Vorschau dieser Markdown-Anleitung auch eine Shell und eine Console. Du hast die Wahl zwischen Shell und Console, sie basieren standardmäßig beide auf Bash, weshalb dort kein Unterschied für dich sichtbar sein wird.

## Cheat Sheet für die wichtigsten Kommandos (in Replit)
### Shell: ./get
Mit dem Befehl
```bash
./get EXERCISE_REPOSITORY_NAME
```
kannst du eine neue Aufgabe in deinen Arbeitsbereich kopieren.

> **Beispiel**
> ```bash
> ./get intro-ndhbr
> ```
> wobei ndhbr in dem Fall durch deinen Nutzernamen ersetzt werden muss.

---

### Shell: ./submit
Mit dem Befehl
```bash
./submit EXERCISE_REPOSITORY_NAME
```
kannst du einen Versuch deiner Lösung hochladen.

---

### Shell: ./test
Mit dem Befehl
```bash
./test EXERCISE_REPOSITORY_NAME
```
kannst du deinen Versuch überprüfen. Der Test wird automatisiert deine Lösung bewerten.

---

### Shell: Ordner wechseln
Den Ordner in der Shell wechselst du mit dem Befehl **cd**.

Mit dem Befehl
```bash
cd ORDNER
```

wechselst du in einen Ordner. Mit dem Befehl
```bash
cd ..
```
kehrst du in den vorherigen Ordner zurück.

Mehr Informationen dazu findest du hier: https://www.howtoforge.de/anleitung/linux-cd-befehl-tutorial-fuer-anfaenger-8-beispiele/

---

## ‼️ GitHub: Anmeldung? Passwort?
Um private Projekte, auf die du Zugriff hast, in Replit zu importieren oder neue Lösungen dafür hochzuladen, musst du dich bei GitHub authentifizieren. Dies geht jedoch nicht einfach mit Username/Password. Das wäre auch zu umständlich bei jedem Kommando dich neu einzuloggen. Dies funktioniert über SSH-Keys. Im Folgenden wird dir erklärt, wie du so einen erstellst und nutzt. Gerne kannst du dich selbst im Internet weiter über das Thema informieren.

### Schritt 1
Geh in Replit in die Shell und tippe ein:
```bash
ssh-keygen
```
Klicke dich einfach mit Enter durch die Fragen ohne etwas zu beantworten.
Wenn du damit fertig bist sollte so etwas Teil der Ausgabe sein:
```
Your public key has been saved in /home/runner/.ssh/id_rsa.pub.
```

### Schritt 2
Nun musst du deinen Public Key auslesen. Nimm den ausgegebenen Pfad und kopiere folgendes in die Shell:
```bash
cat /home/runner/.ssh/id_rsa.pub
```
Jetzt sollte der Dateiinhalt deines Public-Keys ausgegeben worden sein.
Kopiere die Ausgabe in deine Zwischenablage.

### Schritt 3
Wechsle nun in die Einstellungen von GitHub. Dort sollte es den Reiter **SSH-Keys** geben. Erstelle nun einen neuen Key mit beliebigen Namen (z.B. Replit Zugang) und füge den Key aus deiner Zwischenablage ein.

Fertig, nun solltest du dich ohne Nachfrage bei GitHub authentifizieren können.
