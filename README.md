# Willkommen
Hey! Du willst programmieren lernen? Dann bist du hier genau richtig. Hier wirst du Schritt für Schritt zu deinem ersten selbstprogrammierten Programm hingeführt.

## Voraussetzungen
- GitHub Account (github.com - kostenlos)
- Replit Account (replit.com - kostenlos)
- Motivation

## Setup
So, an diesem Punkt solltest du bereits Accounts für die beiden vorher genannten Profile haben. Falls nicht, kannst du ganz einfach mit deiner studentischen E-Mail bei den Plattformen einen gratis Account anlegen.

Öffne nun replit.com und klicke auf das Plus rechts oben **New Repl**.

Tippe auf den Knopf **Import from GitHub** und füge im Feld **GitHub Url** folgenden Link ein https://github.com/ndhbr-classroom/replit-template. Starte daraufhin den **Import**. Schließlich öffnet sich dein neuer Arbeitsbereich. Hier wirst du alle Aufgaben dieses Kurses erledigen.

## Aufbau Replit
Im Linken Teil des Fensters solltest du nun eine Toolbar sehen. Standardmäßig selektiert sollte der Reiter **Files** sein. Wenn alles geklappt hat, solltest du bereits mehrere Dateien sehen.

Im mittleren Teil befindet sich der Editor. Hier wirst du deine eigentliche Programmierarbeit leisten.

Im rechten Teil befindet sich neben der Vorschau dieser Markdown-Anleitung auch eine Shell und eine Console. Du hast die Wahl zwischen Shell und Console, sie basieren standardmäßig beide auf Bash, weshalb dort kein Unterschied für dich sichtbar sein wird.

### GitHub + Replit: Authentifizierung
Um private Projekte, auf die du Zugriff hast, in Replit zu importieren oder neue Lösungen dafür hochzuladen, musst du dich bei GitHub authentifizieren. Dies geht jedoch nicht einfach mit Username/Password. Das wäre auch zu umständlich bei jedem Kommando dich neu einzuloggen. Dies funktioniert über SSH-Keys. Im Folgenden wird dir erklärt, wie du so einen erstellst und nutzt. Gerne kannst du dich selbst im Internet weiter über das Thema informieren.

Folgende Schritte musst du nur einmal für den Kurs machen.

#### Schritt 1
Geh in Replit in die Shell und tippe ein:
```bash
ssh-keygen
```
Konsolen-Befehle schickst du immer mit der **Enter-Taste** ab.
Klicke dich einfach mit Enter durch die Fragen ohne etwas zu beantworten.
Wenn du damit fertig bist sollte so etwas Teil der Ausgabe sein:
```
Your public key has been saved in /home/runner/.ssh/id_rsa.pub.
```

#### Schritt 2
Nun musst du deinen Public Key auslesen. Nimm den ausgegebenen Pfad und kopiere folgendes in die Shell:
```bash
cat /home/runner/.ssh/id_rsa.pub
```
Jetzt sollte der Dateiinhalt deines Public-Keys ausgegeben worden sein.
Kopiere die Ausgabe in deine Zwischenablage.

#### Schritt 3
Wechsle nun in die Einstellungen von GitHub. Dort sollte es den Reiter **SSH-Keys** (https://github.com/settings/keys) geben. Erstelle nun einen neuen Key mit beliebigen Namen (z.B. Replit Zugang) und füge den Key aus deiner Zwischenablage ein.

#### Schritt 4
Nun musst du noch deinen git-User konfigurieren. Gebe hierzu nacheinander folgende Befehle in der Shell ein:
```bash
git config --global user.name 'Dein Name'
git config --global user.email 'deine@email.adresse'
```

Fertig, nun solltest du dich ohne Nachfrage bei GitHub authentifizieren können.

---

## Aufgaben
Eine Anleitung, wie du Aufgaben bearbeitest, findest du unten.
### Aufgabe 1: Intro
Hier geht's los. In dieser Aufgabe wirst du deine ersten Erfahrungen mit der Programmiersprache JavaScript machen.
>Teilnahmelink: https://classroom.github.com/a/23qpgD3v

---

## Cheat Sheet für die wichtigsten Kommandos (in Replit)
### Shell: ./get
Mit dem Befehl
```bash
./get EXERCISE_REPOSITORY_NAME
```
kannst du eine neue Aufgabe in deinen Arbeitsbereich kopieren.

>**Beispiel**
>```bash
>./get intro-ndhbr
>```
>wobei ndhbr in dem Fall durch deinen Nutzernamen ersetzt werden muss.

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

## Wie kann ich eine Aufgabe bearbeiten?
### Schritt 1
Benutze den Teilnahmelink der jeweiligen Aufgabe. Daraufhin sollte GitHub dir ein Repository erstellen. Das kannst du dir vorstellen, wie wenn dir die Kopie einer Klausur ausgeteilt wird. Diese kannst du unabhängig von anderen Studierenden bearbeiten und schließlich wieder abgeben.

### Schritt 2
Der Link des Repositories wird dir angezeigt. Der Name sollte aus dem Namen der Aufgabe, sowie aus deinem GitHub Namen bestehen. Gehe jetzt in Replit und lade dir mit dem oben beschriebenen Befehl **./get** (in der Shell) das Repository in deinen Replit-Arbeitsbereich. Nun kannst sollte ein neuer Ordner mit den Dateien der Aufgabe erstellt worden sein. Dort kannst du jetzt die Aufgabe bearbeiten.

Am Besten wechselst du dann direkt den Ordner in deiner Shell. Mit dem vorher beschriebenen Befehl **cd** kannst du in den Ordner der Aufgabe wechseln.

In jedem Aufgaben-Ordner befindet sich immer eine **README.md**-Datei. Dieser Datei kannst du jeweils alle Informationen über die aktuelle Aufgabe entnehmen.

Mit dem Befehl **./test** kannst du deine Lösung testen.

>Achtung: Um die Befehle **./get**, **./submit** und **./test** zu benutzen, musst du immer in den Hauptordner deines Arbeitsbereiches zurückkehren (Shell-Befehl: **cd ..**)

### Schritt 3
Mit dem oben beschriebenen Befehl **./submit** kannst du deine Lösung hochladen.