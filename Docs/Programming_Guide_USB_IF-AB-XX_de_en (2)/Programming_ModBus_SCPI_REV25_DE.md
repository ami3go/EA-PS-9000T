kitamotuA-ortkelE
Programmieranleitung
ModBus & SCPI
Für USB, GPIB, Ethernet
und AnyBus-Module
Achtung! Dieses Dokument gilt
nur für die in Abschnitt 1.1.2
aufgelisteten Geräteserien und
Doc ID: PGMBDE
nur ab der dort aufgeführten
Revision: 25
Firmwareversion!
Stand: 15.05.2023

ModBus & SCPI
INHALT
1. ALLGEMEINES 5
1.1 Zu diesem Dokument ...................................................................................................................................5
1.1.1 Urheberschutz (Copyright) ..................................................................................................................5
1.1.2 Geltungsbereich ..................................................................................................................................5
1.2 Symbolerläuterungen ...................................................................................................................................6
1.3 Gewährleistung und Garantie.......................................................................................................................6
1.4 Haftungsbeschränkungen ............................................................................................................................6
2. ANYBUS-MODULE 7
2.1 Übersicht ......................................................................................................................................................7
2.2 Anybus-Unterstützung ..................................................................................................................................8
2.3 Bevor Sie beginnen ......................................................................................................................................8
2.4 Installation eines Anybus-Moduls .................................................................................................................9
2.5 Netzwerk in Linientopologie .........................................................................................................................9
2.6 Netzwerkzugriff über HTTP ..........................................................................................................................9
2.7 Netzwerkzugriff über TCP ............................................................................................................................9
3. EINFÜHRUNG 10
3.1 Zugriff auf das Gerät ..................................................................................................................................10
3.2 Bedienorte ..................................................................................................................................................10
3.3 Timing und Befehlsausführungszeit ...........................................................................................................10
3.3.1 Ausführungszeiten beim Schreiben ..................................................................................................11
3.3.2 Antwortenzeit beim Lesen .................................................................................................................11
3.3.3 Befehlsintervall ..................................................................................................................................12
3.4 Übersicht der Kommunikationsprotokolle ...................................................................................................13
3.5 Besonderheiten der Fernsteuerung............................................................................................................14
3.6 Fragmentierte Nachrichten bei serieller Übertragung ................................................................................14
3.7 Verbindungs-Timeout .................................................................................................................................14
3.8 Effektive Auflösung beim Programmieren ..................................................................................................14
3.9 Minimale Steigung bei Rampen (Arbiträrgenerator) ...................................................................................15
3.9.1 Minimale Steigung bei Frequenzen (Arbiträrgenerator) ....................................................................16
3.10 Besondere Situationen ...............................................................................................................................16
3.10.1 Alarm "Power fail" .............................................................................................................................16
4. DAS MODBUS-PROTOKOLL 17
4.1 Allgemeines zu ModBus RTU ....................................................................................................................17
4.2 Allgemeines zu ModBus TCP .....................................................................................................................17
4.3 Format der Sollwerte und Auflösung ..........................................................................................................17
4.4 Umrechnung der Soll- und Istwerte ............................................................................................................18
4.5 Kommunikation mit dem Gerät über ein AnyBus-Modul.............................................................................18
4.5.1 Ethernet .............................................................................................................................................18
4.5.2 Profinet / Profibus ..............................................................................................................................18
4.5.3 CANopen ...........................................................................................................................................18
4.5.4 CAN ...................................................................................................................................................18
4.5.5 ModBus TCP .....................................................................................................................................18
4.5.6 EtherCAT ...........................................................................................................................................18
4.5.7 RS232 ...............................................................................................................................................18
4.6 Kommunikation über einen USB-Port (COM).............................................................................................19
4.6.1 USB-Treiberinstallation .....................................................................................................................19
4.6.2 Erste Schritte .....................................................................................................................................19
4.7 Über die Register-Listen.............................................................................................................................19
4.7.1 Spalten "ModBus-Adresse" ...............................................................................................................19
4.7.2 Spalten "Funktion" .............................................................................................................................19
4.7.3 Spalte „Datentyp“ ..............................................................................................................................20
4.7.4 Spalte „Zugriff“ ..................................................................................................................................20
4.7.5 Spalte „Anzahl Register“ ...................................................................................................................20
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 2
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.7.6 Spalte „Daten“ ...................................................................................................................................20
4.7.7 Spalten „Profibus slot/Profinet subslot" und "Profinet index“ ............................................................20
4.7.8 Spalte „EtherCAT PDO/SDO?“ .........................................................................................................20
4.8 ModBus RTU im Detail ...............................................................................................................................21
4.8.1 Telegrammtypen ................................................................................................................................21
4.8.2 Funktionen ........................................................................................................................................21
4.8.3 Sendetelegramm (Schreiben) ...........................................................................................................22
4.8.4 Anfragetelegramm .............................................................................................................................22
4.8.5 Antworttelegramm (Lesen) ................................................................................................................23
4.8.6 Die ModBus-Checksumme ...............................................................................................................23
4.8.7 Beispiele für ModBus RTU-Telegramme ...........................................................................................24
4.9 ModBus TCP im Detail ...............................................................................................................................26
4.9.1 Beispiel für ein ModBus TCP-Telegramm .........................................................................................26
4.10 ModBus-Kommunikationsfehler .................................................................................................................27
4.11 Erläuterungen zu bestimmten Registern ....................................................................................................28
4.11.1 Register 171 .....................................................................................................................................28
4.11.2 Register 411 ......................................................................................................................................28
4.11.3 Register 500-503 (Sollwerte) ............................................................................................................28
4.11.4 Register 498, 499 und 504 (weitere Sollwerte) .................................................................................28
4.11.5 Register 505 (1. Zustandsregister) ....................................................................................................28
4.11.6 Register 511 (2. Zustandregister) ......................................................................................................29
4.11.7 Register 650 - 662 (Konfiguration Master-Slave-Betrieb) .................................................................29
4.11.8 Register 850 - 6695 (Funktionsgenerator) ........................................................................................29
4.11.9 Register 850 - 1692 (Sequenzgenerator in ELR 5000) .....................................................................32
4.11.10 Register 850 - 854 und 900 - 908 (Funktionsgenerator in EL 3000 B) .............................................32
4.11.11 Register 9000 - 9009 (Einstellgrenzen).............................................................................................33
4.11.12 Register 10007 - 10900.....................................................................................................................33
4.11.13 Register ab 11000 (MPP-Tracking) ...................................................................................................34
4.11.14 Register ab 11500 (Batterietest) .......................................................................................................34
4.11.15 Register ab 12000 (PV-Simulation nach DIN EN 50530) ..................................................................35
5. SCPI-PROTOKOLL 37
5.1 Format der Soll- und Istwerte .....................................................................................................................37
5.2 Syntax ........................................................................................................................................................37
5.2.1 Groß-/Kleinschreibung ......................................................................................................................37
5.2.2 Langform und Kurzform ....................................................................................................................37
5.2.3 Befehlsverkettung .............................................................................................................................38
5.2.4 Abschlußzeichen ...............................................................................................................................38
5.2.5 Kommunikationsfehler .......................................................................................................................38
5.3 Beispiele zum Einstieg ...............................................................................................................................39
5.3.1 Ping bzw. Geräteinformationen abfragen ..........................................................................................39
5.3.2 Fernsteuerung aktivieren oder beenden ...........................................................................................39
5.4 Befehlsgruppen ..........................................................................................................................................40
5.4.1 Standard-IEEE-Befehle .....................................................................................................................40
5.4.2 Statusregister ....................................................................................................................................41
5.4.3 Sollwertbefehle ..................................................................................................................................45
5.4.4 Meßbefehle .......................................................................................................................................48
5.4.5 Zustandsbefehle ................................................................................................................................49
5.4.6 Befehle für Schutzfunktionen ............................................................................................................51
5.4.7 Befehle für Überwachungsfunktionen ...............................................................................................53
5.4.8 Befehle für Einstellgrenzen ...............................................................................................................54
5.4.9 Befehle für den Master-Slave-Modus................................................................................................55
5.4.10 Allgemeine Abfragebefehle ...............................................................................................................56
5.4.11 Befehle zur Konfiguration des Gerätes .............................................................................................58
5.4.12 Befehle zur Fernbedienung des Funktionsgenerators ......................................................................65
5.4.13 Befehle zur Fernbedienung des Sequenzgenerators (nur ELR 5000) ..............................................72
5.4.14 Befehle zur Fernbedienung des MPP-Tracking ................................................................................74
5.4.15 Befehle für das Alarmmanagement ...................................................................................................76
5.4.16 Befehle für Sollwert-Sätze (Recall, nur PSI 5000) ............................................................................77
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 3
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.17 Befehle für die erweiterte PV-Simulation...........................................................................................79
5.4.18 Befehle für die Batterietest-Funktion .................................................................................................85
5.4.19 Spezifische Befehle und Syntax bei Serie PS 2000 B TFT ...............................................................90
5.4.20 Spezifische Befehle bei Serie EL 3000 B ..........................................................................................92
5.5 Beispielanwendungen ................................................................................................................................94
5.5.1 Master-Slave über SCPI konfigurieren und steuern..........................................................................94
5.5.2 Programmier-Beispiele zum Funktionsgenerator ..............................................................................95
5.5.3 Programmier-Beispiele zur PV-Simulation (DIN EN 50530) .............................................................99
5.5.4 Programmier-Beispiele für MPP-Tracking .......................................................................................104
5.5.5 Programmierbeispiele zum Rampengenerator der Serie EL 3000 B ..............................................107
6. PROFIBUS & PROFINET 109
6.1 Allgemeines ..............................................................................................................................................109
6.2 Vorbereitung .............................................................................................................................................109
6.3 Slot-Konfiguration für Profibus .................................................................................................................109
6.4 Slot-Konfiguration für Profinet ..................................................................................................................110
6.5 Zyklische Kommunikation über Profibus/Profinet .....................................................................................110
6.6 Azyklische Kommunikation über Profibus/Profinet ...................................................................................110
6.7 Beispiele für azyklische Kommunikation ...................................................................................................111
6.7.1 Fernsteuerung aktivieren/deaktivieren .............................................................................................111
6.7.2 Einen Sollwert setzen .......................................................................................................................111
6.7.3 Etwas auslesen ..............................................................................................................................112
6.8 Interpretation von Eingangsdaten ............................................................................................................113
7. CANOPEN 114
7.1 Einschränkungen......................................................................................................................................114
7.2 Vorbereitung (nicht EtherCAT) .................................................................................................................114
7.3 Anwendung der Benutzerobjekte (Indexe) ...............................................................................................114
7.3.1 Umrechnung Index -> Register .......................................................................................................114
7.4 Konkrete Beispiele ...................................................................................................................................115
7.5 Besonderheiten gegenüber ModBus ........................................................................................................115
7.5.1 Bei Verwendung des Arbiträrgenerators .........................................................................................115
7.6 CANopen-spezifische Fehlercodes ..........................................................................................................116
8. CAN 117
8.1 Vorbereitung .............................................................................................................................................117
8.2 Einführung ................................................................................................................................................117
8.3 Telegrammtypen .......................................................................................................................................117
8.3.1 Normales Schreiben ........................................................................................................................117
8.3.2 Zyklisches Schreiben ......................................................................................................................118
8.3.3 Abfragen ..........................................................................................................................................119
8.3.4 Normales Lesen ..............................................................................................................................119
8.3.5 Zyklisches Lesen ............................................................................................................................120
8.3.6 Kommunikationsfehlercodes ...........................................................................................................122
8.3.7 Beispiele ..........................................................................................................................................123
9. ETHERCAT 124
9.1 Einleitung..................................................................................................................................................124
9.2 Einschränkungen......................................................................................................................................124
9.3 Einbindung des Gerätes in TwinCAT ........................................................................................................124
9.4 Datenobjekte ............................................................................................................................................124
9.4.1 Unterobjekte im RxPDO ..................................................................................................................125
9.4.2 Unterobjekte im TxPDO ..................................................................................................................125
9.4.3 SDOs ...............................................................................................................................................126
9.5 Steuerung .................................................................................................................................................126
9.5.1 Verwendung der CANopen-Datenobjekte .......................................................................................126
A. ANHANG 127
A1. Geräteklassen ..........................................................................................................................................127
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 4
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
1.  Allgemeines
1.1  Zu diesem Dokument
1.1.1  Urheberschutz (Copyright)
Nachdruck, Vervielfältigung oder auszugsweise, zweckentfremdete Verwendung dieser Bedienungsanleitung sind
nicht	gestattet	und	können	bei	Nichtbeachtung	rechtliche	Schritte	nach	sich	ziehen.
1.1.2  Geltungsbereich
Diese Programmieranleitung gilt für Geräte der nachfolgend aufgelisteten Serien, inklusive deren Abvarianten.
Die	Zugehörigkeit	wird	in	erster	Linie	von	der	Firmwareversion	der	Kommunikationseinheit	(KE)	bestimmt.	Ältere
KE-Firmwares sind daher eventuell nur zum Teil mit dieser Anleitung kompatibel. Es wird empfohlen, sich das
Serienkürzel aus der Tabelle zu merken, weil es in dieser Anleitung weiter hinten als Referenz dient.
Wenn in der Tabelle unten für Ihr Gerät eine Firmware gelistet wird, die noch nicht freigegeben
ist, dann bedeutet das, daß die Ausgabeversion dieses Dokuments nur bedingt gilt und daß
die angezeigt Firmware noch in Arbeit ist. Sie können dann auf die vorherige Ausgabe dieser
Anleitung zurückgreifen.
| Serie     | Firmware ab | Kürzel |
| --------- | ----------- | ------ |
| EL 3000 B | KE: 2.04    |        |
EL3
EL 9000 B 3U - 24U / HP / 2Q KE: 2.31 (Standard) bzw. KE: 2.12 (GPIB) ELR9
| EL 9000 B Slave        | KE: 2.31  | ELR9 |
| ---------------------- | --------- | ---- |
| EL 9000 DT / EL 9000 T | KE: 3.08  | DT   |
| ELR/ELM 5000           | HMI: 2.03 | ELR5 |
ELR 9000 / ELR 9000 HP KE: 2.29 (Standard) bzw. KE: 2.14 (GPIB)
ELR9
| ELR 10000 | KE: 2.06 | ELR1 |
| --------- | -------- | ---- |
PS 2000 B TFT (nur Modell mit farbiger Anzeige) HMI: 2.02 PS2
| PS 5000                           | KE: 2.05 | PS5   |
| --------------------------------- | -------- | ----- |
| PSI 5000                          | KE: 3.08 | PSI5  |
| PS 9000 1U/2U/3U (Serien ab 2014) | KE: 3.08 | PS9   |
| PS 9000 T                         | KE: 3.08 | PST   |
| PS 10000                          | KE. 3.01 | PS1   |
| PSB 9000                          | KE: 2.31 | PSB   |
| PSB 10000 / PSB 10000 Slave       | KE: 2.06 | PSB1  |
| PSBE 9000                         | KE: 2.31 | PSBE  |
| PSBE 10000                        | KE: 2.06 | PSBE1 |
| PSE 9000                          | KE: 2.31 | PSE   |
PSI 9000 2U / 3U / WR / SLAVE (Serien ab 2014) KE: 2.31 (Standard) bzw. KE: 2.14 (GPIB) PSI9
| PSI 9000 15U / 24U                            | KE: 2.29 | PSI9 |
| --------------------------------------------- | -------- | ---- |
| PSI 9000 DT                                   | KE: 3.08 | DT   |
| PSI 9000 T                                    | KE: 3.08 | PSIT |
| PSI 10000                                     | KE: 2.06 | PSI1 |
| PS 3000 C                                     | KE: 2.04 | PS3  |
| Alle 10000er Serien (PSB, PSBE, PSI, PS, ELR) | KE: 3.02 | 10K  |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 5
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
1.2 Symbolerläuterungen
Warn- und Sicherheitshinweise, sowie allgemeine Hinweise in diesem Dokument sind stets in einer umrandeten
Box und mit einem Symbol versehen:
Hinweissymbol für Hinweise, die auf wichtige bzw. unerläßliche Gegebenheiten aufmerksam machen.
Allgemeiner Hinweis
1.3 Gewährleistung und Garantie
Der Hersteller garantiert die Funktionsfähigkeit der angewandten Verfahrenstechnik und die ausgewiesenen Lei-
stungsparameter. Die Gewährleistungszeit beginnt mit der mangelfreien Übergabe.
Die Garantiebestimmungen sind den allgemeinen Geschäftsbedingungen (AGB) des Herstellers zu entnehmen.
1.4 Haftungsbeschränkungen
Alle Angaben und Hinweise in dieser Anleitung wurden unter Berücksichtigung geltender Normen und Vorschrif-
ten, des Stands der Technik sowie unserer langjährigen Erkenntnisse und Erfahrungen zusammengestellt. Der
Hersteller übernimmt keine Haftung für Schäden aufgrund:
• Nicht bestimmungsgemäßer Verwendung
• Einsatz von nicht ausgebildetem und nicht unterwiesenem Personal
• Eigenmächtiger Umbauten von Geräten
• Technischer Veränderungen von Geräten
• Verwendung nicht zugelassener Ersatzteile
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 6
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
2. Anybus-Module
Neben einer oder mehreren eingebauten Schnittstellen wie z. B. USB oder analog können manche Serien um
eine zusätzliche, digitale Schnittstelle erweitern. Diese kommt in Modulform, ist nachkauf- und nachrüstbar und
wird vom Gerät automatisch erkannt, außer das Gerät und dessen Firmware sind älter als das Modul. Dann kann
es zwecks Erkennung und Verwendung der Schnittstelle nötig sein, ein Firmwareupdate auf dem Gerät und/oder
dem Anybus-Modul zu installieren.
2.1 Übersicht
Funktion /
Modul LED-Anzeigen Abbildung
Anschlüsse
IF-AB-CAN CAN 2.0B, RUN Zeigt Datenverkehr an (grün, Flackern)
1x Sub-D 9polig
männlich ERR Leuchtet (grün), solange ein Fehler anliegt.
IF-AB-CANO CANopen, RUN Zeigt den Status mit nach DR303-3 (CiA)
definierten Blinksequenzen an
1x Sub-D 9polig
männlich ERR Zeigt den Status mit nach DR303-3 (CiA)
definierten Blinksequenzen an
IF-AB-RS232 RS 232, PWR Modul ist spannungsversorgt
1x Sub-D 9polig,
männlich, für
Nullmodemkabel
IF-AB-PBUS Profibus OP Betriebszustand:
DP-V1 Slave, an (grün) = Datenverkehr
blinkend (grün) = Klar
1x Sub-D 9polig,
blinkend (rot, 1mal) = Parameterfehler
weiblich
blinkend (rot, 2mal) = Profibusfehler
ST Status
aus = nicht initialisiert
an (grün) = initialisiert
blinkend (grün) = Erweiterte Diagnose
an (rot) = Ausnahmefehler
IF-AB-ETH1P Ethernet, NS Netzwerkstatus:
blinkend (grün) = Standard, kann ignoriert
1x RJ45
werden
an (rot) = Doppelte IP, fataler Fehler
MS Modulstatus:
blinkend (grün) = Standard, kann ignoriert
IF-AB-ETH2P Ethernet, werden
an (rot) = Ausnahmefehler
2x RJ45
blinkend (rot) = Behebbarer Fehler
LINK Verbindungsstatus:
an (grün) = Verbindung hergestellt
blinkend (grün) = Datenverkehr
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 7
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Funktion /
Modul LED-Anzeigen Abbildung
Anschlüsse
IF-AB-PNET1P ProfiNET IO, NS Netzwerkstatus:
an (grün) = online mit Controller in RUN
1x RJ45
blinkend (grün) = Controller in STOP
MS Modulstatus:
an (grün) = alles OK
an (rot) = Ausnahmefehler
blinkend (rot, 1mal) = Konfigurationsfehler
IF-AB-PNET2P ProfiNET IO, blinkend (rot, 2mal) = IP-Adresse nicht gesetzt
blinkend (rot, 3mal) = Stationsname nicht
2x RJ45
gesetzt
blinkend (rot, 4mal) = Interner Fehler
LINK Verbindungsstatus:
an (grün) = Verbindung hergestellt
blinkend (grün) = Datenverkehr
IF-AB-ECT EtherCAT Slave, RUN Zeigt den Status mit nach DR303-3 (CiA)
definierten Blinksequenzen an
2x RJ45
ERR Zeigt den Status mit nach DR303-3 (CiA)
definierten Blinksequenzen an
IF-AB-MBUS1P ModBus TCP, NS Netzwerkstatus:
an (grün) = Modul aktiv
1x RJ45
blinkend (grün) = Modul wartet auf Verbindung
an (rot) = Doppelte IP oder fataler Fehler
blinkend (rot) = Prozess-Timeout
MS Modulstatus:
an (grün) = alles OK
IF-AB-MBUS2P ModBus TCP, an (rot) = Primärer Fehler
blinkend (rot) = Sekundärer Fehler
2x RJ45
LINK Verbindungsstatus:
an (grün) = Verbindung hergestellt
blinkend (grün) = Datenverkehr
2.2 Anybus-Unterstützung
Folgende Geräteserien unterstützen die in 2.1 genannten Anybus-Module (Stand: 15.05.2023):
• ELR 9000 / ELR 9000 HP
• ELR 10000
• EL 9000 B / EL 9000 B HP / EL 9000 B 2Q
• PSE 9000
• PSI 9000 2U - 24U
• PSI 10000
• PSB 9000 / PSBE 9000
• alle 10000er Serien
Falls die Unterstützung eines bestimmten Moduls nach der Installation zunächst nicht gegeben
ist, kann es erforderlich sein, die Firmware „KE“ des Gerätes zu aktualisieren.
2.3 Bevor Sie beginnen
Bevor Sie das erste Mal ein Gerät über eins dieser Schnittstellenmodule in ein bereits bestehendes System ein-
binden oder planen, ein neues aufzubauen, nehmen Sie Folgendes zur Kenntnis:
• Alle Module, jedoch besonders die Ethernetvarianten, die eine Webseite bereitstellen, habe eine gewisse Hoch-
laufzeit nach dem Einschalten des Gerätes und bevor Sie bereit sind, kontaktiert zu werden. Üblicherweise ist
das Modul bereit, wenn das Gerät fertig gestartet ist
• Die Betriebsbereitschaft wird von den Modulen möglicherweise durch die an den Modulen befindlichen LEDs
schon vorher angezeigt, aber wenn man versuchen würde, die Webseite über die IP-Adresse aufzurufen, be-
vor das Modul tatsächlich bereit ist, kann ein Timeout auftreten oder die Webseite wird unvollständig geladen
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 8
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
2.4 Installation eines Anybus-Moduls
Die Installation ist im Handbuch des Gerätes beschrieben, in dem das Modul installiert werden soll, ebenso das
eventuell nötige Setup. Für die weitere Installation und Verbindung mit Feldbussen und Netzwerken lesen Sie bitte
in der einschlägigen Dokumentation zu diesen nach.
Das CANopen-Modul IF-AB-CANO bietet keinen Busabschlußwiderstand. Daher muß die
Busterminierung hier am Kabel oder anderweitig erfolgen, z. B. mit einem IXXAT 120Ω D-Sub
Stecker.
2.5 Netzwerk in Linientopologie
Die Ethernet-basierten Module für Standard-LAN, ModBus TCP und Profinet/IO gibt es auch als Ausführung mit
zwei Ports. Diese ermöglichen eine linienförmige Vernetzung mehrerer Geräte untereinander und sogar den Aufbau
eines Rings (DLR, device level ring) für erweiterten Schutz gegen Leitungsunterbrechnungen. Externe Switches
können entfallen und die sonst erforderlichen, vielen langen Netzwerkleitungen bei sternförmiger Topologie werden
auf ein Minimum reduziert.
Das EtherCAT-Modul dagegen hat standardmäßig zwei Ports, weil das EtherCAT-System ein ringförmiges Netz-
werk erfordert. Auch wenn dieses Modul Ethernet-basiert arbeitet, kann es nicht als LAN-Port betrachtet und wie
eins der normalen Ethernetmodule verwendet werden.
2.6 Netzwerkzugriff über HTTP
Die Ethernet-basierten Module, wie für Standard-LAN, ModBus TCP oder Profinet, sowie Geräte mit eingebautem
LAN-Port bieten eine über einen Browser zugängliche Webseite. Um diese aufzurufen, muß im Browser (Firefox,
Chrome, Safari) lediglich die IP-Adresse des Gerätes oder dessen Hostname eingegeben werden. Ein Aufruf über
den Hostnamen (Standardname: Client) ist nur möglich, wenn sich im Netzwerk ein DNS befindet bzw. auf dem
PC einer läuft und Domäne/Hostname bereits registriert sind.
Die Standard-IP bei Auslieferung ist 198.168.0.2. Die Netzwerkparameter können Sie jederzeit im Einstellmenü
(wo vorhanden) des Gerätes verändern oder auch auf Standard-Werte zurücksetzen.
Die aktuelle IP-Adresse ist bei Geräten, die ein Einstellmenü haben, meist auch in einer Übersicht zusammen
mit anderen netzwerkrelevanten Informationen wie Gateway, DNS, Subnetzmaske oder MAC-Adresse zu finden.
Nach Eingabe der IP-Adresse oder des Hostnamen öffnet sich eine Webseite, über die das Gerät komplett
fernsteuerbar ist, jedoch nur mit SCPI-Befehlen die per Hand eingetippt werden müssen. Daher eignet sich
die Webseite in erster Linie zu einfachen Testzwecken. Falls Sie hiermit das Gerät fernsteuern oder zumindest
überwachen wollen, lesen Sie bitte im Abschnitt „5. SCPI-Protokoll“ weiter.
Über die Webseite, genauer über die Unterseite CONFIGURATION, können auch netzwerkspezifische Parameter
konfiguriert und an das Gerät übergeben werden, sofern es vorher mit SYST:LOCK ON in Fernsteuerung versetzt
wurde.
2.7 Netzwerkzugriff über TCP
Alle Anybus-Netzwerkmodule und auch der bei einigen Gerätenserien (z. B. PSI 5000, PS 9000 ab 2014) fest
eingebaute Ethernet/LAN-Anschluß können über den Standardport 5025 oder einen anderen (einstellbar, siehe
Gerätemenü) mittels ModBus RTU oder SCPI angesprochen werden. Für ModBus TCP (wo unterstützt) ist der
Port 502 reserviert.
Der Standardport und die anderen Netzwerkparameter sind teils im Menü am Gerät einstellbar (sofern Menü
vorhanden, siehe jeweiliges Handbuch) bzw. können von außen über USB- oder Netzwerkzugriff, z. B. über die
Webseite des Gerätes (siehe 2.6), konfiguriert werden.
Für den normalen Fernsteuerungsbetrieb des Gerätes über eine Ethernetschnittstelle ist TCP/IP-Zugriff als Sok-
ketverbindung (IP:Port) vorgesehen.
Die TCP-Verbindung kann durch ein Timeout vom Gerät automatisch getrennt werden, wenn
eine bestimmte Zeitlang kein Datenverkehr stattfindet. Die Dauer des Timeouts ist einstellbar
(Standard = 5 s). Durch eine zusätzlich aktivierbare Option namens „TCP keep-alive“ wird die
gleichnamige TCP-Funktionalität aktiviert, die das Timeout unwirksam macht solange „TCP
keep-alive“ im Netzwerk aktiv ist. Ab bestimmten Firmwareversionen (siehe Firmwarehistorie
des Gerätes) wird auch unterstützt, das Timeout dauerhaft zu deaktivieren.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 9
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
3. Einführung
3.1 Zugriff auf das Gerät
Nach der Anbindung des Gerätes über eine digitale Schnittstelle kann auf das Gerät zugegriffen werden. Dies
kann auf verschiedene Art und Weise geschehen:
• Über eine vom Hersteller des Gerätes bereitgestellte Steuerungssoftware
• Über vom Hersteller angebotene LabView-VIs
• Über eine vom Anwender selbst erstellte Steuerungsapplikation
• Über andere Software, wie z. B. ein Terminalprogramm zum Versenden von Textnachrichten (SCPI) oder auch
hexadezimalen Bytes (ModBus)
• Über international standardisierte Software wie für CAN, CANopen, Profibus oder EtherCAT usw.
3.2 Bedienorte
Bedienorte sind die Positionen, von wo aus ein Gerät bedient wird. Grundsätzlich gibt es da zwei: am Gerät (manu-
elle Bedienung) und außerhalb (Fernsteuerung). Der Anwender kann beliebig zwischen den Bedienorten wechseln.
Folgende Bedienorte sind definiert:
Bedienort laut Anzeige Erläuterung
Nichts oder Fern: Keine Wird kein Bedienort im Statusfeld angezeigt, ist manuelle Bedienung aktiv und
der Zugriff von der analogen bzw. digitalen Schnittstelle ist freigegeben.
Fern: Analog, Fern: USB usw. Fernsteuerung ist aktiv
Remote Fernsteuerung ist aktiv (alle Schnittstellen, nur PS 5000 / PSI 5000)
Lokal / Local Fernsteuerung ist gesperrt, Gerät kann nur manuell bedient werden
Digitale Fernsteuerung muß grundsätzlich immer mittels eines bestimmten, an das Gerät zu
sendenden Befehls aktiviert werden. Sie kann am Gerät nicht aktiviert, sondern nur freigegeben
oder gesperrt werden und aktiviert sich auch nicht automatisch bei irgendeinem ersten Befehl.
Bestimmte Geräteserien, jedoch nicht alle, bieten eine Möglichkeit, die Fernsteuerung über die Einstellung Fern-
steuerung erlauben (oder ähnlich, siehe Handbuch des Gerätes) komplett zu sperren. Im gesperrten Zustand ist
meist in der Anzeige der Status Lokal zu lesen. Die Aktivierung der Sperre kann dienlich sein, wenn normalerweise
eine Software das Gerät ständig fernsteuert, man aber zwecks Einstellung oder auch im Notfall am Gerät hantieren
muß, was bei Fernsteuerung sonst nicht möglich wäre.
Die Aktivierung des Zustandes Lokal bewirkt folgendes:
• Falls Fernsteuerung über digitale Schnittstelle aktiv ist (Fern: Ethernet usw.), wird die Fernsteuerung sofort
beendet und kann später vom Anwender bzw. einer Software, sofern Lokal nicht mehr aktiv ist, erneut über-
nommen werden.
• Falls Fernsteuerung über analoge Schnittstelle aktiv ist (Fern: Analog), wird die Fernsteuerung nur solange
unterbrochen bis Lokal wieder beendet, sprich die Fernsteuerung wieder erlaubt wird, denn der Pin REMOTE
an der Analogschnittstelle gibt weiterhin das Signal „Fernsteuerung = ein“ vor. Ausnahme: der Pegel von RE-
MOTE wird während der Phase Lokal auf HIGH geändert oder der Stecker von der Analogschnittstelle entfernt.
3.3 Timing und Befehlsausführungszeit
Timing, also die Steuerung des zeitlichen Ablaufs zwischen zwei aufeinanderfolgenden, vom Anwender initiierten
Telegrammen, wird nicht vom Gerät übernommen und obliegt daher dem Anwender.
Es gilt generell: das Gerät kann eintreffende Telegramme nicht so schnell verarbeiten, wie die Hardwareschnittstelle
sie theoretisch übertragen könnte. Daher ist wichtig, zwischen zwei Telegrammen eine Mindestzeit zu warten, in
der keine Kommunikation stattfindet. Dabei ist egal, welche Schnittstelle verwendet wird. Protokolldatenverkehr,
wie er zum Beispiel zwischen einem Profibus-Master und einem Profibus-Slave stattfindet, ist davon nicht betroffen,
weil dieser vom Schnittstellenmodul selbst und nicht vom Gerät abgehandelt wird.
Es gilt außerdem:
• Anfragen an das Gerät, also Lesebefehle, sind schneller ausführbar und dürfen daher schneller aufeinander-
folgend an das Gerät gesendet werden
• Setzbefehle werden nicht direkt nach dem Empfang ausgeführt, sondern eine variierende Zeit später
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 10
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
3.3.1 Ausführungszeiten beim Schreiben
Aufgrund von unterschiedlichem Aufbau der Serien, unterschiedlichen Firmwares und auch unterschiedlich langen
Durchlaufzeiten von Mikrocontrollern, welche die Geräte steuern und nebenbei die Kommunikation mit dem PC
abarbeiten, können nur typische Ausführungszeiten genannt werden. Das bedeutet auch, daß die Zeit, bis ein
Sollwert, den Sie setzen möchten, am DC-Ausgang/Eingang anliegt, variabel ist.
3.3.2 Antwortenzeit beim Lesen
Beim Lesen, das heißt Abfragen von Informationen vom Gerät, antwortet das Gerät in der Regel sofort. Es gibt
zwei Methoden der Kommunikation mit dem Gerät über einen Port:
1) Port öffnen -> Anfrage über den Port senden -> Antwort lesen -> Port schließen
2) Port öffnen -> Anfrage über den Port senden -> Antwort lesen -> Schreiben/Lesen x-mal wiederholen -> Port
schließen
Nach dem Schreiben von ModBus-Nachrichten sollte immer auch die Antwort vom Port gelesen werden, denn es
könnte statt eines "OK" auch eine Fehlermeldung zurückkommen. Bei SCPI antwortet das Gerät nur auf Anfrage-
befehle, also jene die mit einem Fragezeichen („?“) enden.
Beide Methoden haben Vor- und Nachteile. Der Hauptvorteil von Methode 2 gegenüber Methode 1 ist, daß das
Wegfallen des ständigen Öffnens und Schließens des Ports insgesamt die Antwortzeit verringern kann, jedoch nicht
zwangsweise muß. Der Hauptvorteil von Methode 1 gegenüber Methode 2 ist, daß eine Kommunikation stabiler sein
kann, wenn man den Port immer schließt. Das gilt insbesondere dann, wenn zwischen zwei Schreib-/Lesezyklen
viel Zeit vergeht. Bei Ethernet ist die Methode jedoch nachteilig, da zu viele lokale Ports gleichzeitig belegt würden.
Die Werte in der Tabelle unten wurden mit Methode 2 ermittelt.
Die Antwortzeiten über die diversen Schnittstellen sind von der auf dem Gerät installierten
KE-Firmwareversion abhängig und können auch länger sein als unten aufgeführt. Die unten
genannten Zeiten gelten für die bzw. ab den in Abschnitt 1.1.2 gelisteten Firmwareversionen.
Die unten aufgeführten Antwortzeiten beinhalten die Übertragungszeiten zwischen Gerät und
der Steuerungseinheit. Bei Schnittstellen mit variablen Baudraten (CAN, CANopen) gelten die
Werte nur für die jeweils höchste Baudrate.
Typische Antwortzeiten (außer RS232)
Geräteserie Protokoll USB Ethernet-basiert CAN/CANopen
Profibus
PS 2000 B TFT SCPI <5 ms - -
ModBus <5 ms - -
EL 3000 B SCPI <5 ms <5 ms -
EL 9000 B HP & 2Q
ModBus (1 <5 ms <5 ms <3 ms
EL 9000 DT
ELR 5000
ELR 9000
ELR 10000
PS 3000 C
PS 5000
PS 9000 (alle Serien ab 2014)
PSB 9000 / PSBE 9000
PSB 10000 / PSBE 10000
PSE 9000
PSI 5000
PSI 9000 (alle Serien ab 2014)
PS 10000 / PSI 10000
(1 Inkludiert davon abgewandelte Formate bei CAN, CANopen, Profinet usw.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 11
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
3.3.3 Befehlsintervall
Die unten gelisteten zeitlichen Minimalabstände zwischen zwei Telegrammen orientieren sich nach der in 3.3.1
aufgeführten Antwortzeit, weil eine Anfrage an das Gerät die meiste Zeit verbraucht. Bei Feldbussen wie Ether-
CAT oder Profinet ist die Kommunikation zwar getaktet, auch mit geringeren Zeiten als unten angegeben, ist aber
unabhängig davon. Es bedeutet somit, daß z. B. bei 1 ms Taktung frühestens alle 5 Takte ein neuer Sollwert oder
Anfrage geschickt werden darf.
Geräteserien Minimalabstand zwischen zwei Tele- Empfohlene Zeit zwischen zwei
grammen Telegrammen
PS 2000 B TFT USB: 5 ms USB: 10-15 ms
EL 3000 B USB / CAN / CANopen: 5 ms USB / CAN / CANopen: 10-15 ms
EL 9000 B HP & 2Q Ethernet: 5 ms Ethernet: 10 ms
EL 9000 DT EtherCAT: 5 ms EtherCAT: 10 ms
ELR 5000
Profibus / Profinet: 5 ms Profibus / Profinet: 10 ms
ELR 9000
ELR 10000
PS 3000 C
PS 5000
PS 9000 (alle Serien ab 2014)
PSB 9000 / PSBE 9000
PSB 10000 / PSBE 10000
PSE 9000
PSI 5000
PSI 9000 (alle Serien ab 2014)
PS 10000 / PSI 10000
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 12
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 3.4  Übersicht der Kommunikationsprotokolle |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- |
Die in der Tabelle unten aufgeführten Serien, außer PS 5000, unterstützen zwei Kommunikationsprotokolle:
ModBus und SCPI.	Grundsätzlich	können	beide	Protokolle	über	RS232,	USB	und	den	meisten	Ethernet-basierten
Schnittstellen	übertragen	werden.	Ausnahmen	sind	dedizierte	Standards	wie	CAN,	CANopen,	Profinet,	Profibus
oder EtherCAT.
Bei Verwendung eines Ethernetports wird noch zwischen ModBus RTU und ModBus TCP unterschieden. Bei
manchen Serien mit fest installiertem Ethernetport ist das Nachrichtenformat ModBus TCP erst ab einer bestimm-
ten Firmwareversion verfügbar. Die Unterstützung kann also nachträglich installiert werden. Die Übertragung von
Befehlen über Ethernet in den Formaten "ModBus RTU over Ethernet" oder SCPI ist über alle freien Ports außer
502 zulässig, während Befehle im Format "ModBus TCP" nur über den zugewiesenen Port 502 akzeptiert werden.
Bei installierter Option 3W (GPIB zusammen mit USB und Analog), wie ab Q3/2014 optional
für bestimmte Serien erhältlich, ist über den GPIB-Port nur SCPI als Kommunikationsprotokoll
unterstützt, über USB hingegen auch ModBus RTU.
Welche Geräteserie unterstützt welche Kommunikationsprotokolle grundsätzlich?
ModBus
SCPI
| Geräteserie                     |     | RTU |                     | TCP |                   |
| ------------------------------- | --- | --- | ------------------- | --- | ----------------- |
| EL 3000 B / PS 3000 C           |     |    | ab Firmware KE 2.04 |     |                  |
| EL 9000 B / HP / 2Q             |     |    |                     |    |                  |
| EL 9000 DT / T                  |     |    | nicht unterstützt   |     |                  |
|                                 |     |    |                     |     |                  |
| ELR 5000                        |     |     | nicht unterstützt   |     |                   |
| ELR 9000 / ELR 9000 HP          |     |    |                     |    |                  |
| PS 2000 B TFT (nur Farbanzeige) |     |    | nicht unterstützt   |     |                  |
| PS 5000                         |     |    | nicht unterstützt   |     | nicht unterstützt |
|                                 |     |    |                     |     |                  |
| PS 9000 1U                      |     |     | nicht unterstützt   |     |                   |
| PS 9000 2U / 3U                 |     |    |                     |    |                  |
| PSB 9000 / PSBE 9000            |     |    |                     |    |                  |
| PSE 9000                        |     |    |                     |    |                  |
|                                 |     |    |                     |    |                  |
PSI 5000
| PSI 9000 2U - 24U   |     |    |                     |    |    |
| ------------------- | --- | --- | ------------------- | --- | --- |
| PSI 9000 DT / T     |     |    | ab Firmware KE 3.05 |     |    |
| Alle 10000er Serien |     |    |                     |    |    |
Besonderheit: über USB oder Ethernet die Protokolle SCPI und ModBus abwechselnd verwendet werden. Das
Gerät erkennt das Protokoll automatisch am ersten gesendeten Byte, welches bei einer ModBus RTU-Nachricht
daher immer 0x00 oder 0x01 sein muß.
Je	nach	dem	welche	Schnittstelle	und	welches	Protokoll	man	benutzen	möchte,	ergibt	sich	ein	anderer	Teil	dieser
Anleitung, der relevant ist. Anwender mit einem Gerät, das die optionalen Schnittstellenmodule (siehe Abschnitt
2.2)	unterstützt,	haben	eine	größere	Auswahl.	Die	Tabelle	unten	listet	auf,	welches	Anybus-Modul	welche	Proto-
kolle unterstützt:
| Modultyp | ModBus?                           | SCPI?                       |     | Anderes Protokoll            |     |
| -------- | --------------------------------- | --------------------------- | --- | ---------------------------- | --- |
| CAN      | nein                              | nein                        |     | ja (siehe „8. CAN“)          |     |
| CANopen  | nein                              | nein                        |     | CANopen (siehe „7. CANopen“) |     |
| RS232    | ja                                | ja                          |     | nein                         |     |
|          | (siehe „4. Das ModBus-Protokoll“) | (siehe „5. SCPI-Protokoll“) |     |                              |     |
| Profibus | nein                              | nein                        |     | Profibus	                    |     |
(siehe „6. Profibus & Profinet“)
| Ethernet   | ja, ModBus RTU                    | ja                          |     | nein                                      |     |
| ---------- | --------------------------------- | --------------------------- | --- | ----------------------------------------- | --- |
|            | (siehe „4. Das ModBus-Protokoll“) | (siehe „5. SCPI-Protokoll“) |     |                                           |     |
| ProfiNet   | nein                              | nein                        |     | Profinet	(siehe	„6. Profibus & Profinet“) |     |
| ModBus TCP | ja, ModBus TCP                    | ja                          |     | ModBus RTU                                |     |
|            |                                   | (siehe „5. SCPI-Protokoll“) |     | (siehe „4. Das ModBus-Protokoll“)         |     |
(siehe „4.5.5. ModBus TCP“)
| EtherCAT | nein | nein |     | EtherCAT (siehe „9. EtherCAT“) |     |
| -------- | ---- | ---- | --- | ------------------------------ | --- |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 13
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
3.5 Besonderheiten der Fernsteuerung
Bei Gebrauch der Fernsteuerung gibt es einige Besonderheiten zu beachten:
• Konfiguration oder Steuerung des Funktionsgenerators (wo verfügbar) erfordern eine gewisse Reihenfolge des
Vorgehens. Diese wird für ModBus in 4.11.8 und für SCPI in 5.4.12 näher erläutert. Die für ModBus erläuterte
Methode gilt grundsätzlich auch für andere Schnittstellen wie CAN, CANopen, EtherCAT usw.
• Einige Register bzw. SCPI-Befehle dienen zur Konfiguration des Gerätes, wie man sie auch manuell im Ge-
rätemenü (wo vorhanden) vornehmen kann, z. B. um zu festzulegen, wie sich das Gerät in Bezug auf den
DC-Eingang/Ausgang verhalten soll. Diese Register/Befehle sind weder extra gruppiert, noch farblich markiert
und sollten nur benutzt werden, wenn man verschiedene Konfigurationen für ein Gerät laden können möchte.
• Die am Gerät einstellbaren Einstellgrenzen („Limits“, wo vorhanden, siehe Gerätehandbuch) begrenzen alle
darauf bezogenen Sollwerte und können zu Fehlermeldungen von seiten des Gerätes führen, die zunächst
nicht erwartet werden. Bei Verwendung von SCPI werden zudem die Fehler üblicherweise nicht direkt zurück-
gegeben, sondern nur auf Anfrage. Somit kann es sein, daß ein Sollwert nicht angenommen wird, weil zu groß
oder zu klein. Die Akzeptanz eines Sollwertes seitens des Gerätes kann dann nur überprüft werden, indem er
zurückgelesen wird.
3.6 Fragmentierte Nachrichten bei serieller Übertragung
Bei RS232, Ethernet und auch USB möglich: fragmentierte Nachrichten. Das betrifft in erster Linie SCPI-Befehle,
die aus Text bestehen und besonders bei seriellen Schnittstellen auch zeichenweise übertragen werden könnten,
jenachdem wie das ausführende System auf der Steuerungsseite (PC) es verarbeitet. Das führt, weil kein Ende-
zeichen (engl. termination character) erwartet wird, zu Kommunikationsfehlern.
Das Gerät interpretiert eine Nachricht als „vollständig erhalten“ , wenn nach einem übertragenen Byte eine gewisse
Zeitlang kein weiteres Byte mehr gesendet wurde. Besteht eine Nachricht aus mehr als einem Fragment, könnte
das Gerät die einzelnen Fragmente als mehrere einzelne, aber dann fehlerhafte Befehle interpretieren.
Ab einem bestimmten Firmwarestand ist ein variables Timeout für USB eingeführt worden, das man manuell am
Gerät (außer bei PS/PSI 5000) oder per Fernsteuerung konfigurieren kann, z. B. über SCPI (siehe 5.4.11). Kom-
munikationsfehler durch fragmentierte Nachrichten können weitestgehend eliminiert werden, indem der Timeout-
Wert schrittweise erhöht wird. Es gilt dabei jedoch zu bedenken, daß am Ende jeder Nachricht, bevor das Gerät
den Befehl umsetzt bzw. auf eine Anfrage antwortet, das vom Anwender gewählte Timeout ablaufen muß. Daher
wird empfohlen, den Timeout-Wert stets so niedrig wie möglich zu setzen.
Bei Verwendung von SCPI hilft das Senden eines zusätzlichen, aber nicht immer erforderlichen Endezeichens
(engl: termination character, z. B. die typischen Werte LF, CR oder CRLF) das Timeout sofort abzubrechen und
die Nachricht vom Gerät als vollständig erhalten zu betrachten.
3.7 Verbindungs-Timeout
Ethernet-Verbindungen zu Geräten, die einen Ethernetport installiert haben können, haben ein sog. „socket ti-
meout“. Das ist eine variable, vom Anwender einstellbare Zeit (siehe Handbuch des Gerätes) nach der sich die
Socket-Verbindung seitens des Gerätes automatisch trennt, wenn für die eingestellte Zeit keinerlei Kommunikation
zwischen Gerät und steuernder Einheit (PC, SPS usw.) stattgefunden hat. Nach der Trennung kann die Verbindung
jederzeit wiederhergestellt werden. Dieses Timeout wird unwirksam, wenn die ab einer bestimmten Firmwarever-
sion unterstützte Einstellung „TCP keep-alive“ am Gerät aktiviert und „keep-alive“ vom vorhandenen Netzwerk
generell unterstützt wird. Ab einer bestimmten Firmwareversion (siehe Firmwarehistorie) kann das Timeout auch
ganz deaktiviert werden.
3.8 Effektive Auflösung beim Programmieren
Alle Soll- und Istwerte von Spannung, Strom, Leistung und Widerstand eines Gerätes, die transferiert werden
können und letztendlich von den Leistungsstufen am DC-Eingang/-Ausgang umgesetzt bzw. dort erfaßt werden,
haben eine programmierbare Auflösung für 0-100% und eine effektive Auflösung. Während die programmierbare
Auflösung bei allen Serien gleich ist (0-100% = 0-0xCCCC = 0-52428), selbst bei Verwendung von SCPI, wird die
effektive Auflösung durch die im Gerät verwendeten Wandler (ADC/DAC) bestimmt und ist nicht überall gleich.
Siehe die Tabelle unten.
Die effektive Auflösung bestimmt die am DC-Eingang/-Ausgang erreichbare Schrittweite. Diese errechnet sich für
alle Werte als Schrittweite = Nennwert ÷ Auflösung. So hat beispielsweise ein PSI 9080-510 3U eine erreichbare
Schrittweite bei der Spannung von 80 V / 26214 = ca. 3 mV. Beim Strom wären es dann 510 A / 26214 = ca. 19 mA.
Zu dieser theoretisch erreichbaren Schrittweite kommen aber noch Gerätetoleranzen hinzu, die sich aus den Anga-
ben in den technischen Daten des Gerätes errechnen lassen. Das PSI 9080-510 3U aus dem Beispiel hat bei der
Spannung laut Handbuch eine Toleranz von max. 0,1% Nennwert. Das sind rechnerisch bis zu 80 mV. Wenn man
also einen Sollwert von 24 V setzt, dürfte dieser durch die zulässige Toleranz zwischen 23,92 V und 24,08 V betragen
und man könnte ihn, sofern extern nachgemessen und nicht genau genug, in etwa 3 mv-Schritten nachkorrigieren.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 14
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Der vom Gerät auslesbare Istwert enthält die Toleranz (oder Fehler) bereits. Angenommen, man würde mit einem
Multimeter nachmessen und die Spannung ist aktuell 24,03 V und man will näher an den Zielwert 24 V heran,
könnte man per Software und durch die Schrittweite von etwa 3 mV bei diesem Gerät nachkorrigieren und den
Istwert weiter an den Sollwert annähern.
Serie ADC/DAC Effektive Auflösung
EL 3000 B 12 Bit 4096
EL 9000 B 3U-24U / EL 9000 B HP / EL 9000 B 2Q 16 Bit 26214
EL 9000 DT 16 Bit 26214
EL 9000 T 14 Bit 16384
ELR 5000 16 Bit 26214
ELR 9000 / ELR 9000 HP 16 Bit 26214
PS 2000 B TFT 12/32 Bit 4096/26214
PS 5000 / PSI 5000 16 Bit 26214
PSB 9000 / PSBE 9000 / PSE 9000 / PSI 9000 2U - 24U / PSI 9000 DT 16 Bit 26214
PS 9000 T / PSI 9000 T 14 Bit 16384
PS 3000 C 12 Bit 4096
Alle 10000er Serien 16 Bit 26214
3.9 Minimale Steigung bei Rampen (Arbiträrgenerator)
Dieser Abschnitt betrifft nur folgende Serien mit Funktionsgenerator:
• EL 9000 B / EL 9000 B HP / EL 9000 B 2Q / EL 9000 DT / EL 9000 T
• ELR 9000 / ELR 9000 HP / ELR 10000
• PSI 9000 2U - 24U / PSI 10000
• PSI 9000 DT / PSI 9000 T
• PSB 9000 / PSB 10000
Anwender von Geräten der 10000er Serien bitte lesen:
Mit der Freigabe der Firmwares KE 3.02 und DR 1.0.20 für alle 10000er Serien wurde die
Erfordernis einer minimalen Steigung für Rampen, wie generiert durch den internen arbiträren
Funktionsgenerator, komplett entfernt. Gleichzeitig hebt das auch die bisher max. Zeit von 1379
Sekunden für eine Rampe auf. Das bedeutet, dieser Abschnitt gilt dann nicht mehr für ein Gerät
mit mindestens diesen installierten Firmwares.
Sollten Sie diese Änderung nutzen wollen, können Sie diese Firmware entweder einfach als
Update installieren, sofern das jeweilige Gerät dafür qualifiziert ist (die Update-App in unserer
Software regelt das), oder kontaktieren Sie unseren Support für Einzelheiten, wie die Firmwares
installiert werden können
Bei der Programmierung des sog. "arbiträren Funktionsgenerators", egal über welche digitale Schnittstelle, kann
das Gerät Fehler zurückgeben, die sich auf falsche Wertevorgaben für die sog. Sequenzpunkte beziehen. Neben
Werten, die einfach nur außerhalb des zulässigen Wertebereichs liegen, gibt es auch eine minimale Steigung.
Gemäß der Beschreibung des Arbiträrgenerators im Handbuch des Gerätes haben alle Sequenzpunkte veränder-
liche Werte für einen AC-Anteil, der nur zur Erzeugung einer Sinusfunktion dient, bzw. auch für einen DC-Anteil,
aus dem Rampen generiert werden, wodurch auch Dreiecke, Rechtecke oder Trapeze entstehen. „Veränderlich“
bedeutet hierbei, daß der Endwert anders ist als der Startwert.
Ist dieser Unterschied ungleich 0 entsteht eine Steigung nach ΔU/t oder ΔI/t. Diese Steigung kann nicht beliebig
klein sein. Um zu prüfen, ob eine gewisse Steigung machbar ist, sollte die minimale Steigung des zu programmie-
renden Gerätes berechnet werden. Formel: min. Steigung = (0,000725 * Nennwert von U oder I) pro Sekunde.
In Bezug auf die Parameter eines Sequenzpunktes berechnet das Gerät die gesetzte Steigung aus dem Startwert
vom DC-Anteil, dem Endwert vom DC-Anteil und der Sequenzzeit und vergleicht dann mit der min. Steigung.
Beispiel: das Zielgerät ist eine el. Last mit 500 V Nennspannung und 30 A Nennstrom. Es soll eine Rampe auf den
Strom erzeugt werden. Die minimale Steigung errechnet sich als: ΔI/t = 0,000725 * 30 A / s = 21,75 mA/s. Wollte
man nun die Rampe programmieren mit einer ansteigenden Flanke von 0-20 A über 5 s, dann ergeben sich 4 A/s
Steigung und das ist somit gültig. Ein Anstieg von 0-20 A über 20 Minuten hingegen würde die minimale Steigung
nicht erfüllen und vom Gerät angelehnt werden.
Die machbare Zeit für ein bestimmtes ΔU oder ΔI ist auch errechenbar: t = ΔU oder ΔI / min. Steigung. Für
Max
das Beispiel mit 0-20 A erhalten wir demnach eine t = 20 A / 0,02175 A/s = ca. 919 Sekunden.
Max
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 15
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Fazit: sehr lange Rampen über viele Minuten oder gar Stunden sind mit dem Arbiträrgenerator nicht machbar.
Abhilfe schafft eine schrittweise, vom PC per Software gesteuerte Werteänderung über die Zeit.
Dabei kommt die effektive Auflösung (siehe 3.8) ins Spiel. Die elektronische Last aus dem Beispiel oben könnte
eine ELR 9500-30 sein, mit einer setzbaren Auflösung von 52428 Schritten für 0-100% und einer effektiven von
26214. Um es sinnvoll zu halten würde die effektive betrachtet. 26214 Schritte für 0-100% = 0-30 A ergeben bei
0-20 A also 17476 Schritte. Wollte man eine Rampe über 10 h fahren wollen, könnte man z. B. 10 h / 17476 = ca.
all 2 Sekunden einen Wert setzen, der jeweils um 20 A / 17476 = ca. 1,15 mA erhöht wird. Das ist eine recht feine
Auflösung, die durch unvermeidbare Toleranzen stark beeinflußt würde. Daher empfiehlt es sich, das Raster zu
vergröbern, also z. B. alle 20 s einen Schritt von 11,5 mA oder einmal pro Minute einen von 34 mA. Durch das
gleichmäßige Setzraster ergibt sich eine Rampe mit Stufen die gleich breit sind und mit einer Höhe von 1,15 mA
oder 34 mA oder anders, ganz wie gewünscht.
3.9.1 Minimale Steigung bei Frequenzen (Arbiträrgenerator)
Beim Funktionsgenerator der 9000er und 10000er Serien, der auch DC-Sinuskurven generieren kann, gibt es noch
eine Einschränkung, sollte eine Frequenzänderung zwischen Anfang bis Ende einer generierten Welle stattfinden.
Dann muß auch eine minimale Frequenzänderung pro Sekunde (Δf/s) von 9,3 eingehalten werden, wie auch in
den Handbüchern der Serien im Abschnitt zum Arbiträrgenerator vermerkt. Somit kann, nach dem Schreiben bzw.
Übernehmen von Arbiträrgenerator-Konfigurationsdaten ein Fehler zurückgegeben werden, was bei ModBus direkt
erfolgt, bei SCPI jedoch nur auf Anfrage. Bei SCPI wäre das ein -222.
Wenn man beispielsweise eine Startfrequenz von 1 Hz und eine Endfrequenz von 10 Hz erzielen möchte, ist
die Frage: Wieviel Zeit benötigt der Generator bis die Sinuskurve bei 10 Hz ankommt? Diese Zeit wird von der
Steuerungssoftware gesondert berechnet. Das Ende der in dieser Zeit generierten Wave muß dabei vom Winkel
her nicht zwangsweise dort enden wo sie anfing. Zeitberechnung:
ModBus: t (μs) = |Endfrequenz - Startfrequenz| / 9,3 * 1000000 -> weil Zeitwert in μs
SCPI: t (s) = |Endfrequenz - Startfrequenz| / 9,3 -> weil Zeitwert in s
Für eine Welle von 1 bis 10 Hz ergeben sich also 967741 μs oder 0.9677 s. Stellt man diese Zeit ein und bildet
die ganze Well auf einem Oszilloskop ab, dann hat die letzte Sinuswelle eine Periodendauer, die 10 Hz entspricht.
3.10 Besondere Situationen
Besondere Situationen in der Fernsteuerung eines oder mehrerer Geräte sind im Allgemeinen Ausnahmesituatio-
nen, egal ob unerwartet oder erwartet. Sie erfordern manchmal eine besondere Handhabung.
3.10.1 Alarm "Power fail"
Der Power Fail Alarm (siehe Gerätehandbuch für mehr Einzelheiten) ist einer von mehreren Gerätealarmen, der
z. B. durch einen kurzen Spannungseinbruch der AC-Versorgung entstehen kann und welcher den DC-Ausgang/
Eingang ausschaltet, zumindest zeitweise. Nach seinem Auftreten muß die steuernde Einheit extra warten, bis sie
den DC-Ausgang/Eingang wieder einschalten kann, sofern das Gerät das nicht automatisch selbst machen soll.
Leider ist zum Einen die Wartezeit nicht bei jeder Serie gleich und zum Anderen gibt es keine Signalisierung eines
Zustandes "nun kann es weitergehen". Diese Wartezeit fängt zudem erst an, wenn der PF-Alarm wieder weg ist,
was wiederum periodisch abgefragt werden kann.
Die meisten Serien, wie die 9000er und 10000er, haben eine Einstellung "DC-Ausgang nach PF Alarm" oder ähnlich
formuliert. Stell man diese auf "Auto", schaltet sich der DC-Ausgang/Eingang irgendwann nach Weggehen von
PF automatisch wieder ein, worauf die Steuerung warten könnte, indem der DC-Status gepollt wird. Sollte das
automatische Einschalten aus bestimmten Gründen nicht aktiviert sein, muß die Steuerung das selbst managen.
Es erfordert a) den PF-Alarm zu löschen, wenn möglich, und danach b) mindestens zwei weitere Sekunden zu
warten, bevor der DC-Ausgang/Eingang wieder eingeschaltet werden kann.
Bei allen 10000er Serien ist mit Stand 05/2022 diese Wartezeit nach PF und vorm Löschen des PF ca. 12 Se-
kunden lang.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 16
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4. Das ModBus-Protokoll
Wichtig, unbedingt lesen! Auch Anwender, die bereits mit unseren Geräten vertraut sind:
Mit der Freigabe bestimmter Firmwareversionen in 2020 wurde eine wichtige Anpassung einge-
führt, die es ermöglicht, daß unsere Geräte die ModBus-Spezifikation dort einhalten wo es bisher
nicht geschah. Um kompatibel zu auf der Benutzerseite (PC, SPS) bestehenden Softwares und
Steuerungen zu bleiben, kann diese Einhaltung über Register 10013 zwischen Modus "Voll" und
"Limitiert" (Standard) umgeschaltet werden. "Limitiert" ist hierbei der Zustand wie in den früheren
Firmwares, so daß nach einem Update zunächst keine Probleme auftreten sollten. Unterschiede:
• "Voll" unterstützt die Slave-Adressen 0 und 1 und Antworten auf die Funktion READ COILS
haben das korrekte Format
• "Limitiert" unterstützt nur Adresse 0, wie bisher, demnach muß man die Aktivierung von "Voll"
an Adresse 0 senden
Allgemeines über Modus "Voll":
• Nach der Umschaltung auf "Voll" werden Schreib-/Lese-Befehle immer mit der Adresse be-
antwortet mit der sie gesendet wurden, also 0 oder 1
• Der Zustand wird im Gerät als Einstellung gespeichert
• READ COILS wird dann nur noch im korrekten Format beantwortet
• Schreib-/Lese-Befehle an die Adresse 0 werden beantwortet, auch wenn das bei ModBus
nicht erwartet wird. Die ModBus-Spezifikation gibt das nur für Kommunikationsstränge mit
"Serial line"-Topologie vor, die von unseren Geräten jedoch nicht verwendet wird.
4.1 Allgemeines zu ModBus RTU
Eine Nachricht oder Telegramm nach ModBus RTU-Protokoll besteht aus hexadezimalen Bytes, wovon das erste
Byte hier nur 0 oder 1 sein darf, weil unsere Geräte keine einstellbare Adresse unterstützen, weil nicht nötig. Im
Modus "Voll" (siehe Hinweis in 4. oben) kann die steuernde Einheit die Adressen 0 oder 1 verwenden. Ist die-
ser nicht aktiviert, wird nur Adresse 0 zwecks Abwärtskompatibilität zu älteren Firmwares unterstützt, und muß
daher bei "Limitiert" benutzt werden. Das erste Byte des Telegramms wird auch zur Erkennung benutzt, ob das
Telegramm einen ModBus-Befehl oder einen Textbefehl in SCPI-Befehlssprache enthält. Ein Wert zwischen 2
und 41 im ersten Byte führt zu einer ModBus-Fehlermeldung, ab 42 (ASCII-Zeichen: *) wird das Telegramm als
SCPI-Befehl in Textform interpretiert.
Das Format und die Länge eines Telegramms sind vorgegeben. Das Telegramm wird nach den Spezifikationen
der jeweils verwendeten Schnittstelle übertragen. Der Anwender muß hierbei meist nur Sorge für den richtigen
Inhalt des Telegramms tragen, bei manchen Schnittstellen auch für dessen korrekte Übertragung, weil diese keine
Kommunikationssicherheit bieten, wie z. B. RS232. Einige Schnittstellen unterstützen den Anwender dabei durch
eigene Checksummen bzw. Software-Handshaking.
4.2 Allgemeines zu ModBus TCP
Das Übertragungsprotokoll nach ModBus TCP-Spezifikation wird von den Anybus-Schnittstellenmodulen ModBus
TCP 1-Port und 2-Port (siehe Abschnitt 2.2), sowie ab einer bestimmten Firmwareversion auch bei den einigen
Serien mit fest installierten Ethernetport unterstützt, in beiden Fällen über den dedizierten ModBus TCP-Port 502.
Der Port 502 ist für ModBus TCP reserviert und daher für "normale" Ethernetmodule gesperrt.
Die separaten ModBus-TCP-Module bzw. der eingebaute LAN-Port bestimmter Serien haben
dann quasi zwei Sockets, den reservierten 502 und den anderen einstellbaren, dessen Stan-
dardwert 5025 ist. Somit ist Port 502 automatisch vorhanden und muß nicht eingestellt werden
Per Definition erfordert das Telegramm hier einen zusätzlichen Header, welcher die Verwendung von SCPI-Befehlen
über diesen Port unmöglich macht. Ansonsten ist der Aufbau eines ModBus TCP-Telegramms nahezu identisch
mit ModBus RTU, bis auf den bereits erwähnten Header und die nicht benötigte Checksumme. Die folgenden Ab-
schnitte gelten, was den Kern eines ModBus-Telegrammes betrifft, gleichermaßen für ModBus RTU und ModBus
TCP. Für weitere Information zu ModBus TCP siehe dann „4.9. ModBus TCP im Detail“.
4.3 Format der Sollwerte und Auflösung
Sollwerte, die über die digitalen Schnittstellen für das Gerät vorgegeben werden können, sind immer Prozentwerte
und entsprechen bei 100% (als Hexwert: 0xCCCC, als Dezimalwert: 52428) den Nennwerten des Gerätes.
Man kann einen Sollwert generell zwischen 0% und 102% mit den Werten 0x0000-0xD0E5 setzen bzw. Überwa-
chungsgrenzen für Gerätealarme mit 0x0000-0xE147 für 0% bis 110% oder mit 0x0000-0xD2F1...103%.
Es ergeben sich für 0-100% 52429 mögliche Werte, die intern halbiert werden (das höchste Bit ist als Vorzeichen
reserviert) . Die effektive Stellauflösung bei 0-100 % ist demnach 26214 Schritte oder geringer. Zu dem Thema
siehe auch „3.8. Effektive Auflösung beim Programmieren“.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 17
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.4 Umrechnung der Soll- und Istwerte
Reale Werte müssen vor der Übertragung in Prozentwerte umgerechnet und gelesene Werte können nach dem
Empfang in reale Werte umgerechnet werden. Dabei gilt stets: 100% = 0xCCCC (hexadezimal) = 52428 (dezimal).
Die Umrechnung erfolgt mit der Umsetzung dieser Formeln in der eigenen Software:
Prozentwert zu Realwert Realwert zu Prozentwert
Nennwert * Prozentwert 52428 * Realer Wert
Realer Wert = Prozentwert =
52428 Nennwert Gerät
Beispiel: Nennspannung des Gerätes ist 80 V, der prozentuale Span- Beispiel: die Leistung soll auf 3150 W gesetzt werden, der Nenn-
nungsistwert kam als 0x2454 = 9300. Nach der Formel ergibt sich ein wert des Gerätes ist 3500 W. Nach der Formel ergibt sich:
realer Istwert von (80 * 9300) / 52428 = 14,19 V. Prozentsollwert = (52428 * 3150) / 3500 = 47185 = 0xB851.
Alle Sollwerte, die über die Fernsteuerung an das Gerät gesendet werden, sind nicht nur durch
die Nennwerte des Gerätes begrenzt, sondern können zusätzlich durch die justierbaren Einstell-
grenzen („Limits“, wo verfügbar) begrenzt sein! Werte, die diese Einstellgrenzen überschreiten
würden, werden vom Gerät nicht akzeptiert.
Bei der Umrechnung in die ganzzahligen Prozentwerte (dezimal oder hexadezimal) ist es oft
erforderlich, natürlich zu runden. Achtung! Am oberen Ende des Einstellbereiches können
Rundungsfehler zu einem um 1 zu hohen Umrechnungswert führen.
4.5 Kommunikation mit dem Gerät über ein AnyBus-Modul
4.5.1 Ethernet
Bitte weiterlesen ab Abschnitt 4.7.
4.5.2 Profinet / Profibus
Mit entsprechender Software für SPS-Systeme und ähnlichen Tools kann das Gerät über das Profinet/IO-Modul
(1-Port oder 2-Port) oder Profibus-Modul ferngesteuert und überwacht werden. Bei Profinet/IO wählt die Software
den passenden TCP-Port aus, dieser kann daher am Gerät für das Modul nicht eingestellt werden. Über diesen
wird das Feldbusprotokoll mit entsprechender Software genutzt. Die grundlegende Einbindung des Gerätes in das
Profinet bzw. in den Profibus wird in „6. Profibus & Profinet“ erläutert. Ansonsten bitte weiterlesen ab Abschnitt 4.7.
4.5.3 CANopen
Bitte weiterlesen ab Abschnitt 4.7. Siehe auch Abschnitt „7. CANopen“.
4.5.4 CAN
Bitte weiterlesen ab Abschnitt 4.7. Siehe auch Abschnitt „8. CAN“.
4.5.5 ModBus TCP
Als Protokoll greift hier ModBus TCP, ein erweitertes TCP/IP-Frame-Format. Die Übertragung per TCP/IP wird in
diesem Dokument nicht erläutert. Bitte weiterlesen ab Abschnitt 4.7. bzw. auch „4.5.5. ModBus TCP“.
4.5.6 EtherCAT
Für EtherCAT wird im Allgemeinen fertige Software zur Verfügung gestellt und genutzt, die das Protokoll CANo-
pen over Ethernet (CoE) verwendet. Lesen Sie dazu auch in „7. CANopen“ und „9. EtherCAT“. Ansonsten bitte
weiterlesen ab Abschnitt 4.7.
4.5.7 RS232
Das RS232-Modul arbeitet mit variabler Baudrate, aber die restlichen seriellen Einstellungen sind fix:
Datenbits: 8
Stoppbits: 1
Parität: keine
Bitte weiterlesen ab Abschnitt 4.7.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 18
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.6 Kommunikation über einen USB-Port (COM)
Nach der Anbindung des Gerätes über den USB-Port und erfolgreicher Treiberinstallation kann per virtuellem
COM-Port (VCOM) auf das Gerät zugegriffen werden. Der dem Gerät zugeordnete COM-Port (siehe Windows
Gerätemanager oder andere) muß nicht konfiguriert werden, da er von einem sogenannten CDC-Treiber (Com-
munication Device Class). Dieser ist verfügbar für Windows 7 (auch Embedded), 10 und 11, sowie ggf. weitere
Betriebssysteme und simuliert der Einfachheit halber einen COM-Port im System, wickelt die Datenübertragung
aber so schnell ab, wie es USB 2.0 Port am Gerät es zuläßt. Dabei werden die typischen seriellen Einstellungen
ignoriert, was auch bedeutet, daß sie nicht konkret gesetzt werden müssen.
4.6.1 USB-Treiberinstallation
Der für den rückseitigen, teils auch frontseitig vorhandenen USB-B-Port benötigte Treiber wird mit dem Gerät auf
USB-Stick mitgeliefert und installiert einen signierten Treiber für virtuelle COM-Ports auf 32 bit und 64 bit Windows
Betriebssystemen ab Windows 7. Er ist alternativ als Download auf der Webseite des Geräteherstellers erhältlich.
Für Embedded OS Versionen von Windows sind auf dem USb-Stick INF-Dateien vorhanden.
4.6.2 Erste Schritte
Um mit dem Gerät zu kommunizieren, wird auf der PC-Seite lediglich eine einfache Software benötigt, die in der
Lage ist, einen COM-Port zu öffnen und darüber byteweise, d. h. seriell, Nachrichten im binären ModBus RTU-
Protokollformat oder als ASCII-Strings (hier: SCPI) zu verschicken. Für letzteres eignen sich Terminalprogramme,
wie z. B. das in Windows XP noch vorhandene HyperTerminal. Für binäre Telegramme im Hexadezimalformat,
wie bei ModBus RTU, sind andere Terminalprogramme wie Docklight (www.docklight.de) erforderlich. Für Dock-
light sind bei uns auf Anfrage fertige Docklight-Projekte für unterschiedliche Geräteserien erhältlich, welche die
grundlegendsten Telegramme bereits als per Mausklick an das Gerät schickbare Sequenzen enthalten und als
Einstiegshilfe dienen sollen.
Um das Gerät nun über den USB-Port anzusprechen, muß man nur...
1. das Gerät per USB verbinden.
2. den USB-Treiber installieren (siehe 4.6.1).
3. ein Terminalprogramm oder ähnliches starten.
4.7 Über die Register-Listen
Zusammen mit dieser Programmieranleitung werden sogenannte Register-Listen als PDFs mitgeliefert, die eine Über-
sicht über die vom Gerät unterstützten Funktionen bei Fernsteuerung über das binäre ModBus-Protokoll bieten. Es
gibt meist eine Liste pro Geräteserie, manchmal umfaßt eine Liste auch mehrere Serien. Diese Listen unterscheiden
sich hauptsächlich in der Anzahl der Funktionen und sind in erster Linie für die Verwendung mit dem ModBus-Protokoll
gedacht, dienen jedoch auch als Referenz bei der Fernsteuerung eines Gerätes über Feldbusse (CAN, CANopen,
Profibus, Profinet, EtherCAT) oder bei der Verwendung von Programmierumgebungen wie LabView oder MatLab,
z. B. wenn es um die Interpretation von Werten geht oder das Verständnis der Funktion eines Befehls.
Die Listen erläutern in Kurzform, wie die Daten aufgebaut sind, welche für die jeweilige Funktion an ein bestimmtes
Register (bei CANopen bzw. EtherCAT „Index“ genannt) geschickt werden müssen. Das hilft dem Programmierer
bei der Implementation der Geräte-Kommunikation in eigene Applikationen. Anwender, die mit SCPI arbeiten, be-
nötigen diese Listen im Allgemeinen nicht. Weiter hinten in diesem Dokument werden die Befehle der textbasierten
SCPI-Sprache gesondert behandelt.
4.7.1 Spalten "ModBus-Adresse"
Die hier aufgeführte Zahl ist als Adresse eines ModBus-Registers zu verstehen. Die Adresse wird in ModBus-Nach-
richten 1:1 und hexadezimal verwendet.
4.7.2 Spalten "Funktion"
Die Köpfe der 5 Spalten enthalten die Namen und Codes der ModBus-Funktionen, die unterstützt werden. Ein "x"
kennzeichnet für ein Register die zugehörige Funktion. Z. B. ist ein sog. Coil-Register meist schreib- und lesbar
und daher mit den Funktionen "Read Coils (0x01)" und "Write Single Coil (0x05)" verknüpft.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 19
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 4.7.3    | Spalte „Datentyp“ |                                          |
| -------- | ----------------- | ---------------------------------------- |
| Datentyp | Länge             |                                          |
| char     | 1 Byte            | Einzelnes Byte, wird für Strings benutzt |
| uint(8)  | 1 Byte            | Einzelnes vorzeichenloses Byte           |
uint(16) 2 Bytes Doppelbyte, auch genannt Wort oder vorzeichenloser 16-Bit-Integer
uint(32) 4 Bytes Doppelwort, auch genannt Long oder vorzeichenloser 32-Bit-Integer
| float  | 4 Bytes          | Fließkommawert nach IEEE745 Standard |
| ------ | ---------------- | ------------------------------------ |
| 4.7.4  | Spalte „Zugriff“ |                                      |
Definiert	für	jedes	Register,	ob	man	auf	das	Register	nur	lesend,	nur	schreibend	oder	schreibend/lesend	zugreifen
kann.
R = Register kann nur gelesen werden
W = Register kann nur geschrieben werden bzw. würde beim Lesen keinen sinnvollen Wert zurückgeben
RW = Register kann geschrieben oder gelesen werden
Generell gilt: Schreiben auf ein Register, auf das geschrieben werden kann (Zugriff: W, RW),
ist nur bei aktivierter Fernsteuerung möglich!
| 4.7.5  | Spalte „Anzahl Register“ |     |
| ------ | ------------------------ | --- |
Bei ModBus ist ein Register immer zwei Bytes oder ein Vielfaches von zwei Bytes groß. Diese Spalte gibt an,
wieviele Zwei-Byte-Werte die Register belegen. Der Wert ist jeweils die Hälfte des Wertes in der Spalte „Daten-
länge in Bytes“.
| 4.7.6  | Spalte „Daten“ |     |
| ------ | -------------- | --- |
Gibt zusätzliche Information zum Format der Daten, die in ein Register zu schreiben sind bzw. daraus gelesen
werden	können.	Zwei,	vier	oder	mehr	Bytes	können	unterschiedlich	interpretiert	werden,	je	nach	Datentyp.
4.7.7  Spalten „Profibus slot/Profinet subslot" und "Profinet index“
Diese Spalten sind nur enthalten in Registerlisten für Serien, welche die optionalen Anybus-Schnittstellenmodule
unterstützen,	hier	speziell	für	Profibus	oder	Profinet.	Sie	dienen	zur	Querverbindung	der	ModBus-Register	zu	den
bei	Profibus	bzw.	Profinet	verwendeten	SFBs	(Datenbausteine)	und	deren	Eingangs-Parametern	„ID“	und	„Index“.
Bei	neueren	Softwares	wie	TIA	Portal	sollten	diese	Werte	auch	Verwendung	finden.	Mehr	dazue	in	„6. Profibus
& Profinet“.
| 4.7.8  | Spalte „EtherCAT PDO/SDO?“ |     |
| ------ | -------------------------- | --- |
Diese Spalte ist nur enthalten in Registerlisten für Serien, welche die optionalen Anybus-Schnittstellenmodule,
hier speziell EtherCAT, unterstützen. Sie markiert, welche der für das Gerät über andere Schnittstellen verfügba-
ren	ModBus-Register	für	das	CANopen	over	Ethernet	(CoE)	bei	EtherCAT	als	Indexe	genutzt	werden	können.
Einige der in dieser Spalte markierten Register werden auch im PDO verwendet, während alle markierte Register
grundsätzlich als SDOs addressierbar sind. Geräte, die das EtherCAT-Modul unterstützen, enthalten eine herun-
terladbare Datenobjektliste. Das PDO sind ist im Abschnitt „9. EtherCAT“ beschrieben.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 20
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.8 ModBus RTU im Detail
Wie in Absatz „3.4. Übersicht der Kommunikationsprotokolle“ beschrieben, kann ModBus RTU über die eingebaute
USB-Schnittstelle (wo vorhanden), einen Ethernetanschluß, sowie einige der optionalen AnyBus-Module kommu-
niziert werden. Beim ModBus-Protokoll nennt man adressierte Objekte "Register". Dieses Dokument verwendet
dazu die Begriffe Adresse, Register oder Registeradresse.
Wenn ModBus RTU über Ethernet übertragen wird, dann nennt man es „ModBus RTU über
Ethernet“, aber nicht „ModBus TCP“. Das ModBus TCP Frame-Format wird bei manchen Serien
mit eingebautem Ethernetport zusätzlich unterstützt, aber erst ab einer gewissen Firmwarever-
sion. Mehr dazu im Abschnitt 3.4.
4.8.1 Telegrammtypen
Grundsätzlich wird zwischen Anfrage-Telegrammen, Sende-Telegrammen und Antwort-Telegrammen un-
terschieden. Ein Anfrage-Telegramm veranlaßt das Gerät ein Antwort-Telegramm zu schicken, während Sende-
Telegramme nur ein 1:1 Echo verursachen, als Bestätigung des Empfangs auf der Gegenseite.
4.8.2 Funktionen
Das zweite Byte einer ModBus-Nachricht ist die sogenannte Funktion (FN, blau markiert in den Aufbaudarstellun-
gen unten). Die Funktion bestimmt, ob etwas geschrieben (WRITE) oder gelesen (READ) werden soll. Weiterhin
wird beim Schreiben und Lesen unterschieden, ob man ein bzw. mehrere ganze Register schreiben/lesen will.
Das hier beschriebene Protokoll unterstützt mit Stand 15.05.2023 folgende Funktionen aus der ModBus-Spezifi-
kation:
Funktion Funktionsname Beschreibung Verwendungsbeispiel
Hex Dez Lang Kurz
0x01 1 READ Coils RC Läßt nur das Lesen von 1 Coil zu, weil Zustand des Eingangs /
bei unseren Serien die Coils nicht auf Ausgangs abfragen
fortlaufenden Adressen liegen. Bei älteren
Firmwares wurden hier immer 16 Bits, also
eigentlich mehrere Coils zurückgegeben,
die als 0xFF00 oder 0x0000 jedoch nur
ein boolsches TRUE oder FALSE reprä-
sentierten. Siehe dazu auch den Hinweis
im Abschnitt 4.
0x03 3 READ Holding RHR Lesen von n aufeinanderfolgenden Regi- Gerätebezeichnung
Registers stern. Ergibt n*2 Bytes. Das Lesen über auslesen (1-40 Bytes)
die Registergruppe hinweg ist nur möglich,
wenn die nächste Gruppe das gleiche
Datenformat hat
0x05 5 WRITE Single WSC Schreiben einer Coil (TRUE/FALSE) eines Gerät in Fernsteuerung
Coil boolschen Registers. umschalten
0x06 6 WRITE Single WSR Schreiben eines Registers. Sollwert (U, I, P usw.)
Register
0x10 16 WRITE Multiple WMR Schreiben mehrerer aufeinanderfolgender Mehrere Werte inner-
Registers Register. Kann jedoch nicht verwendet, halb eines Register-
werden, um die Grenze eines Register- blocks oder den sog.
blocks hinweg zuschreiben, also wenn Benutzertext schreiben
man z. B. mehrere Sollwerte wie U, I und
P auf einmal schreiben wollte.
In der Registerliste ist für jedes Register angegeben, welche der Funktionen auf das Register
anwendbar sind.
Die Daten in einer ModBus-Nachricht sind, mit Ausnahme der Checksumme, von links nach
rechts zu lesen (big endian). Bei der 16 Bit-ModBus RTU-Checksumme werden Highbyte und
Lowbyte jedoch vertauscht.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 21
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 4.8.3  Sendetelegramm (Schreiben) |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- |
Das Protokoll überprüft die plausible Länge des Telegramms beim Schreiben nur dahingehend, daß die maximale
Länge des Registers nicht überschritten wird. Nach den Daten im Telegramm wird die Checksumme erwartet.
Wenn	z.	B.	die	Daten	nur	die	mindestens	benötigten	2	Bytes	lang	sind	und	damit	die	Vorgaben	für	die	gewählte
Registeradresse erfüllen, würde die Checksumme ab dem 7. Byte erwartet. Stünde dort ein anderer Wert und die
Checksumme ist erst weiter hinten im Telegramm, würde das Gerät einen Fehler zurückgeben.
Somit wird, egal ob das Telegramm zu kurz oder zu lang ist, ein Fehler zurückgegeben, weil die Checksumme
nicht stimmt. Für einige Beispiele siehe „4.8.7. Beispiele für ModBus RTU-Telegramme“.
WRITE Single Register
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 | Bytes 6+7 |     |
| ------------- | --------- | --------- | --------- | --- |
| Kopf FN       | Startreg. | Datenwort | CRC       |     |
0x01 0x06 0...65535 Zu schreibender Wert Checksumme ModBus-CRC16 (1
WRITE Multiple Registers
Byte 0 Byte 1 Bytes 2+3 Bytes 4+5 Byte 6 Bytes 7-253 Letzte 2 Bytes
| Kopf FN | Startreg. | Anzahl | Zähler Datenbytes | CRC |
| ------- | --------- | ------ | ----------------- | --- |
0x01 0x10 0...65535 0...123 Anzahl*2 Daten Checksumme ModBus-CRC16 (1
WRITE Single Coil
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 | Bytes 6+7 |     |
| ------------- | --------- | --------- | --------- | --- |
| Kopf FN       | Register  | Datenwort | CRC       |     |
0x01 0x05 0...65535 0x0000 oder 0xFF00 Checksumme ModBus-CRC16 (1
| 4.8.4  Anfragetelegramm |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
Bei einer Anfrage	an	das	Gerät	wird	eine	möglichst	unverzügliche	Antwort	erwartet,	die	-	je	nach	Inhalt	-	von
unterschiedlicher Länge, aber stets vom gleichen Aufbau ist. Es muß das Startregister angegeben werden, ab
dem man die gewünschten Informationen lesen will, sowie die zu lesende Anzahl von Registern. Die Basis des
ModBus-Datenformats ist ein 16-Bit-Wert, also eine Gruppe von 2 Bytes. Somit werden bei Anzahl = 1 genau zwei
Bytes oder ein 16-Bit-Wert angefragt und bei Anzahl = 2 dann vier Bytes bzw. zwei 16-Bit-Werte usw. Bei READ
COILS werden entweder 1 Byte (= 1 Coil) oder 2 Byte (=16 Coils, falsche Antwortform in früheren Firmwares)
zurückgegeben. Für einige Beispiele siehe „4.8.7. Beispiele für ModBus RTU-Telegramme“.
READ Holding Registers
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 |     | Bytes 6+7 |
| ------------- | --------- | --------- | --- | --------- |
| Kopf FN       | Startreg. | Anzahl    |     | CRC       |
0x01 0x03 0...65535 Anzahl zu lesender Register (1...125) Checksumme ModBus-CRC16 (1
READ Coils
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 |     | Bytes 6+7 |
| ------------- | --------- | --------- | --- | --------- |
| Kopf FN       | Startreg. | Anzahl    |     | CRC       |
0x01 0x01 0...65535 Muß immer 1 sein Checksumme ModBus-CRC16 (1
(1 Siehe „4.8.6. Die ModBus-Checksumme“
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 22
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.8.5  Antworttelegramm (Lesen)
Eine Antwort vom Gerät kommt entweder nach einer Anfrage oder bei einem Kommunikationsfehler oder beim
Setzen eines Wertes, Zustand o. ä., wenn das Setzen angenommen wurde.
Erwartete Antwort bei WRITE Single Register:
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 | Bytes 6+7 |     |
| ------------- | --------- | --------- | --------- | --- |
| Kopf FN       | Startreg. | Daten     | CRC       |     |
0x01 0x06 0...65535 Geschriebener Wert Checksumme ModBus-CRC16 (1
Erwartete Antwort bei WRITE Single Coil:
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 | Bytes 6+7 |     |
| ------------- | --------- | --------- | --------- | --- |
| Kopf FN       | Startreg. | Daten     | CRC       |     |
0x01 0x05 0...65535 Geschriebener Wert Checksumme ModBus-CRC16 (1
Erwartete Antwort bei WRITE Multiple Registers:
| Byte 0 Byte 1 | Bytes 2+3 | Bytes 4+5 |     | Bytes 6+7 |
| ------------- | --------- | --------- | --- | --------- |
| Kopf FN       | Startreg. | Daten     |     | CRC       |
0x01 0x10 0...65535 Anzahl geschriebene Register Checksumme ModBus-CRC16 (1
Erwartete Antwort bei READ Holding Registers:
| Byte 0 Byte 1 | Byte 2              |     | Bytes 3-252 | Letzte 2 Bytes |
| ------------- | ------------------- | --- | ----------- | -------------- |
| Kopf FN       | Datenlänge in Bytes |     | Daten       | CRC            |
0x01 0x03 2...250 Angefragte Register Checksumme ModBus-CRC16 (1
Achtung! Beachten Sie die Hinweise im Abschnitt „4. Das ModBus-Protokoll“.
Erwartete Antwort bei READ Coils (früheres Format, Einstellung "Limitiert", Standard):
| Byte 0 Byte 1 | Byte 2              |     | Bytes 3+4 | Bytes 5+6 |
| ------------- | ------------------- | --- | --------- | --------- |
| Kopf FN       | Datenlänge in Bytes |     | Daten     | CRC       |
Checksumme ModBus-CRC16 (1
| 0x01 0x01 | 2   |     | 0xFF00 oder 0x0000 |     |
| --------- | --- | --- | ------------------ | --- |
Erwartete Antwort bei READ Coils (neues Format, Einstellung "Voll"):
| Byte 0 Byte 1 | Byte 2              |     | Byte 3         | Bytes 4+5                  |
| ------------- | ------------------- | --- | -------------- | -------------------------- |
| Kopf FN       | Datenlänge in Bytes |     | Daten          | CRC                        |
| 0x01 0x01     | 1                   |     | 0x00 oder 0x01 | Checksumme ModBus-CRC16 (1 |
Unerwartete Antwort (Kommunikationsfehler):
| Byte 0 Byte 1 |     | Byte 2 | Letzte 2 Bytes |     |
| ------------- | --- | ------ | -------------- | --- |
| Kopf FN       |     |        | CRC            |     |
0x01 0x80 + Funktionscode Fehlercode Checksumme ModBus-CRC16 (1
Ein Kommunikationsfehler kann verschiedene Ursachen haben, wie z. B. eine falsche Checksumme
im Telegramm oder wenn man versucht, auf Fernsteuerung umzuschalten, während Fernsteuerung
gegenwärtig nicht erlaubt ist. Für die Fehlercodes siehe „4.10. ModBus-Kommunikationsfehler“.
4.8.6  Die ModBus-Checksumme
Die Checksumme am Ende eines ModBus RTU-Telegramms ist eine 16 Bit-Checksumme, aber laut Vorgabe der
ModBus-Spezifikation	anders	berechnet	als	sonstige	CRC16	und	wird	zudem	noch	mit dem Low-Byte zuerst
angegeben. Informationen und Sourcecode zur Berechnung der Checksumme sind im Internet zugänglich, unter
Anderem hier: http://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf, Abschnitt 2.5.1.2
(1 Siehe „4.8.6. Die ModBus-Checksumme“
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 23
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 4.8.7  | Beispiele für ModBus RTU-Telegramme |     |     |     |     |     |
| ------ | ----------------------------------- | --- | --- | --- | --- | --- |
Diese Nutzdaten dieser Beispiele sind auch für ModBus TCP verwendbar.
| 4.8.7.1  | Einen Sollwert setzen |     |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- | --- |
Sollwerte sind setzbare Obergrenzen für die physikalischen Größen Strom, Spannung, Leistung
oder Widerstand (wo vorhanden). Sollwerte können nur an das Gerät geschickt werden, wenn
es vorher über eine digitale Schnittstelle in Fernsteuerungsbetrieb versetzt wurde.
Beispiel: Den Strom-Sollwert	auf	50%	setzen.	Laut	Registerliste	ist	der	„Sollwert	Strom“	auf	Registeradresse	501
(0x1F5) festgelegt und die zu verwendende ist Funktion „WRITE Single Register“. Vorausgesetzt das Gerät ist
bereits in Fernsteuerung, müßte das Telegramm muß dann so aussehen:
Sende-  Kopf FN Start Daten CRC Erwartete Kopf FN Start Daten CRC
►
telegramm: 0x01 0x06 0x01F5 0x6666 0x338E Antwort: 0x01 0x06 0x01F5 0x6666 0x338E
Durch	ein	Echo	des	Telegramms	meldet	das	Gerät,	daß	der	Befehl	akzeptiert	wurde.	Am	Display	könnte	man	nun
den Stromsollwert überprüfen, bei einer Last bzw. Netzgerät mit 510 A Nennstrom müßte dieser dann als 255.0 A
auf der Frontanzeige abzulesen sein bzw. bei einem Modell mit 170 A Nennstrom dann 85.00 A.
| 4.8.7.2  | Alle Istwerte auf einmal anfragen |     |     |     |     |     |
| -------- | --------------------------------- | --- | --- | --- | --- | --- |
Das Gerät bietet drei auslesbare Istwerte für Spannung, Strom und Leistung. Bei elektronischen Lasten ist in der
Anzeige noch ein Widerstandsistwert ablesbar. Dieser ist aus Iststrom und Istspannung berechnet und wird daher
nicht extra übertragen. Der Anwender kann ihn ebenso aus den gelesenen Werten berechnen.
Die	Istwerte	können	einzeln	oder	zusammen	angefragt	werden.	Der	Vorteil	bei	der	gleichzeitigen	Anfrage	aller
Istwerte ist, daß man damit den Gesamtzustand der Eingangs-/Ausgangswerte zu einem bestimmten Zeitpunkt
erhält.	Bei	Einzelabfrage	könnten	sich	die	Werte	zwischen	zwei	Anfragen	bereits	geändert	haben.
Laut	Registerliste	sind	die	Istwerte	ab	Register	507	zu	finden,	es	sollen	drei	Register	gelesen	werden:
| Anfrage-  | Kopf FN | Start Daten | CRC |     |     |     |
| --------- | ------- | ----------- | --- | --- | --- | --- |
►
telegramm:
|           | 0x01 0x03 | 0x01FB 0x0003 | 0x75C6 |     |     |     |
| --------- | --------- | ------------- | ------ | --- | --- | --- |
| Mögliche	 | Kopf FN   | Länge Daten   |        | CRC |     |     |
Antwort:
|          | 0x01 0x03             | 0x06 0x2620 0x0C9B 0x091B |     | 0x9350 |     |     |
| -------- | --------------------- | ------------------------- | --- | ------ | --- | --- |
| 4.8.7.3  | Nennspannung auslesen |                           |     |        |     |     |
Die Gerätenennspannung, sowie auch die Nennwerte für Strom, Leistung und Widerstand sind wichtige Referenz-
werte	für	die	Umrechnung	der	Soll-	und	Istwerte	und	sollten	nach	dem	Öffnen	der	Kommunikationsverbindung	zu
einem Gerät mit als Erstes ausgelesen werden. Die Nennspannung ist laut Registerliste ein Floatwert mit 4 Bytes
Länge ab Adresse 121.
Anfrage- Kopf FN Start Anzahl CRC Mögliche	 Kopf FN Länge Daten CRC
►
| telegramm: |     |     | Antwort: |     |     |     |
| ---------- | --- | --- | -------- | --- | --- | --- |
0x01 0x03 0x0079 0x0002 0x15D2 0x01 0x03 0x04 0x42A00000 0xEE69
Siehe auch 4.8.5. Die Beispielantwort enthält einen Floatwert im IEEE754-Format, der sich zu 80.0 umrechnet.
| 4.8.7.4  | Gerätestatus auslesen |     |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- | --- |
Laut Registerliste liefert ein Gerät ab Adresse 505 einen 32 Bit-Wert mit mehreren Statusbits.
|          | Kopf FN | Start Anzahl | CRC | Kopf FN   | Länge Daten | CRC |
| -------- | ------- | ------------ | --- | --------- | ----------- | --- |
| Anfrage- |         |              |     | Mögliche	 |             |     |
►
telegramm: 0x01 0x03 0x01F9 0x0002 0x15C6 Antwort: 0x01 0x03 0x04 0x00000483 0xB952
Siehe auch 4.8.5. Die Antwort 0x00000483 sagt nach Aufschlüsselung per Registerliste (Adresse 505) aus, daß das
Gerät in Fernsteuerung über den USB-Port ist, der Eingang/Ausgang eingeschaltet und die Regelungsart CC ist.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 24
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.8.7.5 Fernsteuerung aktivieren oder beenden
Bevor Sie das Gerät fernsteuern können, ist Umschalten auf digitalen Fernsteuerbetrieb mittels eines entspre-
chenden Befehls erforderlich.
Das Gerät schaltet sich niemals automatisch in den Fernsteuerbetrieb und kann ohne diesen
nicht ferngesteuert werden. Auslesen von allen lesbaren Registern ist jedoch auch ohne akti-
vierten Fernsteuerbetrieb möglich.
Das Gerät verläßt die Fernsteuerung niemals automatisch, außer es wird während des Fern-
steuerbetriebs ausgeschaltet oder es tritt ein Netzausfall auf. Die Fernsteuerung kann per Befehl
beendet bzw. manuell am Gerät abgebrochen werden.
Das Umschalten auf Fernsteuerung kann durch folgende bestimmte Umstände blockiert sein und wird durch die
Rückgabe eines Fehlertelegramms gekennzeichnet:
• Es ist Zustand Lokal aktiv (siehe Anzeige des Gerätes bzw. den auslesbaren Gerätestatus), der jegliche Fern-
steuerung verhindert
• Es ist bereits Fernsteuerung über eine andere Schnittstelle aktiv
• Das Gerät befindet sich im Setup-Modus (Einstellmenü aktiv)
► So schalten Sie das Gerät in die Fernsteuerung:
1. Wenn Sie das ModBus RTU-Protokoll verwenden, ist ein Telegramm nach dem oben beschriebenen Aufbau
zu erstellen und zu senden, z. B. 01 05 01 92 FF 00 2C 2B.
2. Bei erfolgreicher Umschaltung des Gerätes in Fernsteuerung, also wenn das Gerät den Befehl akzeptiert
hat, wird der Zustand im Allgemeinen in der Anzeige des Gerätes angezeigt, sowie der Befehl 1:1 als Be-
stätigung zurückgegeben (Echo).
Falls Fernsteuerung beim Gerät aktuell nicht möglich wäre, weil die Einstellung Fernsteuerung erlauben = Nein
im HMI des Gerätes gesetzt wurde, würde das Gerät mit einem Fehler antworten, z. B. 01 85 17 02 9E (laut
ModBus-Spezifikation ist das Fehler 0x85 mit Fehlercode 0x17).
Fernsteuerung kann auf zwei Arten beendet werden: per Befehl oder durch Sperrung derselbigen am Bedienfeld
des Gerätes. Da es hier um Programmierung geht, wird die erstgenannte Möglichkeit betrachtet.
► So beenden Sie die Fernsteuerung:
1. Wenn Sie das ModBus RTU-Protokoll verwenden, ist ein Telegramm nach dem oben beschriebenen Aufbau
zu erstellen und zu senden, z. B. 01 05 01 92 00 00 6D DB.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 25
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.9 ModBus TCP im Detail
ModBus TCP baut auf ModBus RTU auf, daher werden hier nur die Unterschiede erläutert. Für den Kern einer
ModBus TCP-Nachricht lesen Sie bitte in „4.8. ModBus RTU im Detail“ nach. Unterschiede bei ModBus TCP im
Vergleich zu ModBus RTU:
• Die Nachricht erfordert einen zusätzlichen, 6 bzw. 7 Byte langen MBAP-Header
• Die Checksumme entfällt
• Verwendung nur über den reservierten TCP-Port 502; jeder andere Port funktioniert nicht für ModBus TCP
• Wir nur über TCP übertragen, im Gegensatz zu ModBus RTU, das über diverse Übertragungswege geht
Per Definition ist ein Modus-TCP-Telegramm immer 4 Bytes länger als das zugrundeliegende ModBus RTU-
Telegramm. Der MBAP-Header ist wie folgt aufgebaut:
Bytes Bedeutung Erläuterung
0 + 1 Transaktionskennung Kennzeichnet das Telegramm. Die Kennung wird bei einer Antwort durch das
antwortende Gerät in das Antworttelegramm kopiert und dient zum Zuordnen der
Antwort zu einer Anfrage, falls mehrere Geräte im Netzwerk angesprochen werden
und die erwartete Antwort nicht immer sofort auf die Anfrage folgt. Die Kennung
ist beliebig. Wertebereich 0...65535
2 + 3 Protokollkennung 0 = ModBus-Protokoll (hier daher immer 0)
4 + 5 Länge Anzahl der nachfolgenden Bytes, also Länge des ModBus RTU-Telegramms
minus 2.
6 Identifikator (UID) Wird vom ModBus TCP Slave immer auf 0 gesetzt. Das Gerät über einen Gateway
auf diese Art zu adressieren, z. B. Ethernet auf USB, ist nicht möglich.
4.9.1 Beispiel für ein ModBus TCP-Telegramm
Das Beispiel für READ Holding Registers aus „4.8.7.3. Nennspannung auslesen“ , erweitert um den MBAP-Header
mit beliebiger Transaktionskennung 0x4711:
MBAP-Header UID FN Start Daten
Anfragetelegramm:
0x4711 0x0000 0x0006 0x00 0x03 0x0079 0x0002
MBAP-Header UID FN Länge Daten
Mögliche Antwort:
0x4711 0x0000 0x0007 0x00 0x03 0x04 0x43FA0000
Vergleichend mit ModBus RTU wird die typische Checksumme am Ende weggelassen, dafür hat es am Anfang
einen 6 Byte langen Kopf. Die Steuereinheit schickt damit eine Anfrage zum Auslesen der Gerätenennspannung.
Die Antwort (im Nachrichtenteil „Daten“) enthält einen Floatwert der umgerechnet 500 ergibt, also Nennspannung
500 V.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 26
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.10 ModBus-Kommunikationsfehler
Kommunikationsfehler beziehen sich lediglich auf die digitale Kommunikation mit dem Gerät und sind nicht zu
verwechseln mit Alarmen und sonstigen Ereignissen, die das Gerät melden kann. Sie werden sofort vom Gerät
zurückgegeben, wenn z. B. versucht wird schreibend auf das Gerät zuzugreifen während es nicht in Fernsteue-
rung ist oder auch, wenn z. B. über die Funktion READ HOLDING REGISTER versucht wird, ein Zustands-Bit
auszulesen, das laut Zugriffstyp mit READ COILS gelesen werden müßte.
Bei einem Fehler sendet das Gerät die zuvor verwendete Funktionsnummer, jedoch um den Wert 0x80 erhöht,
sowie einen Fehlercode zurück. Übersicht der Funktionsnummern in den Kommunikationsfehlertelegrammen:
FN-Fehler Gehört zu
0x81 READ COILS
0x83 READ HOLDING REGISTERS
0x85 WRITE SINGLE COIL
0x86 WRITE SINGLE REGISTER
0x90 WRITE MULTIPLE REGISTERS
Übersicht der Kommunikationsfehlercodes, die ein Gerät melden kann:
Code Fehlerbezeichnung Erläuterung
0x01 1 Falsche Funktionsnummer Es wurde ein ModBus-Funktionscode in 2. Byte der Nachricht verwen-
det, der vom Gerät nicht unterstützt wird. Siehe „4.8.2. Funktionen“,
welche unterstützt werden. Der Fehler tritt außerdem auf, wenn für den
Zugriff auf eine Adresse die falsche Funktion verwendet wurde, z. B.
Read Holding Registers beim Schreiben eines Bits, für das Write Single
Coil richtig gewesen wäre.
0x02 2 Adresse nicht definiert Mehrere Ursachen:
• Es wurde versucht, schreibend oder lesend auf eine Adresse zuzu-
greifen, die für das Gerät nicht definiert wurde. Siehe die separaten
ModBus-Register-Listen, welche Register/Adressen für die jeweilige
Serie verfügbar sind, zu der das zu steuernde Gerät gehört.
• Es wurde bei ModBus RTU Slaveadresse 0x01 benutzt, obwohl
das Gerät aufgrund älterer Firmware nur 0x00 unterstützt oder der
Schalter "Einhaltung der ModBus-Spezifikation" stand auf "Limitiert".
0x03 3 Fehlerhafte Daten oder Da- Es wurden Daten mit falscher Länge oder falsche Daten gesendet. Zum
tenlänge falsch Beispiel erfordert ein Sollwert immer 2 Bytes. Wenn stattdessen nur 1
Byte gesendet würde, wäre die Nachricht zu kurz und wenn 3 Bytes
(vor der Checksumme) gesendet würden, wäre die Nachricht zu lang.
„Fehlerhafte Daten“ könnte z. B. ein zu hoher Sollwert sein, also wenn
ein Sollwert als max. 0xCCCC definiert ist und man würde 0xE000
schicken.
0x04 4 Execution Befehl nicht ausführbar, situationsabhängig
0x05 5 CRC CRC16-Checksumme am Ende der ModBus RTU-Nachricht ist falsch
oder fehlt. Das kann durch eine falsche Bytereihenfolge (High-Byte zu-
erst statt Low-Byte zuerst) oder durch falsche Berechnung oder durch
am Ende fehlende Bytes entstehen, z. B. bei geteilten TCP-Paketen.
0x07 7 Zugriff verweigert Zugriff auf eine Adresse generell nicht erlaubt, oder nur lesend oder
nur schreibend oder Zugriff zwar schreibend erlaubt, Gerät aber nicht
in Fernsteuerung bzw. in Fernsteuerung durch eine andere Schnittstelle
0x17 23 Gerät in Lokal-Modus Dieser Fehler kommt, wenn irgendeine Nachricht gesendet wird, die
steuernd auf das Gerät zugreifen will, während die Fernsteuerung
gesperrt ist (lokal).
Beispiel, wann welcher Fehlercode zurückkommen kann: Sie versuchen, das Gerät in Fernsteuerung zu
versetzen und bekommen statt des erwarteten Echos eine Antwort wie diese: 01 85 07 03 52. Das ist eine Feh-
lermeldung. An der Position der Funktion steht der Wert 0x85, laut Tabelle oben ist das ein Fehler bei WRITE
SINGLE COIL. Der Fehlercode ist 0x7, laut der zweiten Tabelle oben bedeutet dieser, daß der Zugriff auf das Gerät
mit dem zuletzt gesendeten Befehl verweigert wurde. Das kann u. A. bedeuten, daß es bereits über eine andere
Schnittstelle, z. B. eine analoge, ferngesteuert wird.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 27
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.11 Erläuterungen zu bestimmten Registern
Für die Kürzel der Geräteserien siehe „1.1.2. Geltungsbereich“.
Nicht alle Funktionen aller ModBus-Register bzw. der zugehörigen SCPI-Befehle sind selbsterklärend. Daher werden
hier zusätzliche Hinweise und Beispiele gegeben. Außerdem haben nicht alle Geräteserien dieselbe Anzahl von
Befehlen zur Verfügung, was in der erster Linie von der Ausstattung abhängig ist. Unten wird bei den einzelnen
Beispielen jeweils in Form einer kleinen Tabelle angezeigt, in welcher Geräteserie Sie verfügbar sind:
ELR9 PS9 PSI9 PSI5
 ─  ─
Für die Kürzel in der Kopfzeile siehe „1.1.2. Geltungsbereich“. Wobei
 bedeutet, der Befehl oder eine Befehlsgruppe wird ganz oder teilweise von der Geräteserie unterstützt.
─ bedeutet, der Befehl oder eine ganze Befehlsgruppe wird von der Geräteserie nicht unterstützt.
4.11.1 Register 171
Dieses Register kann der Anwender mit einem bis zu 40 Zeichen langen, beliebigen Text beschreiben, der z. B.
zur besonderen Identifikation des Gerätes unter mehreren gleichartigen dienen kann. Der Text wird automatisch
und dauerhaft gespeichert.
4.11.2 Register 411
Für SCPI beschrieben in „5.4.15. Befehle für das Alarmmanagement“.
Bei ModBus setzt dieses Bitregister die Gerätealarme zurück, die im Gerätestatus (Register 505, siehe unten)
auslesbar sind. Das heißt, solange man einen oder mehrere Gerätealarme nicht per Fernsteuerung bzw. manuell
am Gerät zurücksetzt, bleiben sie im Gerätestatus als aktiv enthalten, auch wenn sie nicht mehr anliegen. Alarme,
die noch anliegen, werden im Gerätestatus nicht zurückgesetzt. Nach dem Löschen der Alarmbits kann später nur
noch ein allgemeiner Alarmzähler (Register 520 - 524) ausgelesen werden.
4.11.3 Register 500-503 (Sollwerte)
Das sind mit die wichtigsten Register für die vier Sollwerte für Strom, Spannung, Leistung und Widerstand (wo
vorhanden). Bei ModBus werden die Sollwerte als prozentualer Anteil (0...100%) des jeweiligen Nennwertes an-
gegeben, bei SCPI als realer Wert.
Um den Widerstandsmodus (engl.: R mode) - wo unterstützt - nutzen zu können, muß er zuvor aktiviert werden
(Register 409), ansonsten wird der Sollwert ignoriert und hat keinen Effekt.
Bei Netzgeräten der Serien PSI 9000 (ab 2014) und PSI 10000 und der nur dort verfügbaren einfachen PV-
Funktion wird der Stromsollwert (Register 501) im PV-Betrieb anders interpretiert und bestimmt dann nicht die
maximale Stromgrenze, sondern die bei der Simulation von Solarpaneelen gebräuchlichen Beschattung als einen
Stromfaktor. Die Beschattung ist bei manueller Bedienung nur in 1%-Schritten zwischen 0 und 100% einstellbar,
in Fernsteuerung ist eine deutlich feinere Auflösung machbar.
4.11.4 Register 498, 499 und 504 (weitere Sollwerte)
Mit Stand 03/2020 haben die Serien PSB 9000, PSBE 9000 und PSB 10000 drei weitere Sollwertregister für den
sog. Senke-Betrieb. Da sind 498 (Leistung), 499 (Strom) und 504 (Widerstand).
4.11.5 Register 505 (1. Zustandsregister)
Ein weiteres wichtiges Register. Bei ModBus spiegelt es den Zustand des Gerätes in einem 32 Bit-Wert dar. Einige
Bits können zu Gruppen zusammengefaßt sein und müssen auch so interpretiert werden. Zum Beispiel stellen laut
Registerliste die Bits 0-4 des Registers 505 den Bedienort dar (siehe auch „3.2. Bedienorte“). Durch das Auslesen
des Registers kann man so feststellen, ob sich das Gerät bereits in Fernsteuerung befindet und wenn ja, über welche
Schnittstelle. Das hilft auch dabei festzustellen, ob das Senden des Befehls „Fernsteuerung = ein“ erfolgreich war.
Bei SCPI ist ein Teil der Statusbits aus Register 505 in den Statusregistern „Questionable“ und „Operation“ erfaßt.
Siehe „5.4.2. Statusregister“.
4.11.5.1 Bei Master-Slave-Betrieb
Für Master-Slave (MS, wo vorhanden) gibt das Register zusätzlich ein Bit (29, „MSS“) heraus, das den sog. Master-
Slave-Sicherheitsmodus anzeigt. Dieser wird immer bei einer Störung aktiv, also wenn z. B. der Master einen Slave
nicht mehr kontaktieren kann, weil ausgefallen o. ä. Der Master wird daraufhin sich und die noch erreichbaren Slaves
DC-seitig ausschalten. Die getrennten Slaves versetzen sich selbst in einen ähnlichen Zustand und schalten ab.
Nach Beseitigung der Problemursache muß das MS-System neu initialisiert werden, was u. A. auch das Bit löscht.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 28
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.11.5.2 Bit 31
Nur vorhanden bei PSB-Geräten signalisiert dieses Bit die aktuelle Betriebsart hinsichtlich Quelle und Senke.
4.11.6 Register 511 (2. Zustandregister)
Die Serien PSB 10000, ELR 10000 und PSI 10000 haben ein zweites Statusregister, hauptsächlich weil sie zu-
sätzlich Gerätealarme anzeigen müssen.
4.11.7 Register 650 - 662 (Konfiguration Master-Slave-Betrieb)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─  ─ ─ ─  ─  ─ ─     
Diese Registergruppe dient zur Konfiguration des Master-Slave-Betriebs, kurz: MS. Wenn der MS konfiguriert und
initialisiert wurde, verhält sich das MS-System wie ein Einzelgerät. Sprich, die sonst verwendeten Register zum
Sollwertesetzen, Gerätezustand lesen und setzen usw. sind dann auch zu benutzen. Für die hardwaremäßige
Konfiguration, manuelle Bedienung und Betrieb des MS lesen Sie bitte im Gerätehandbuch nach.
Die ferngesteuerte softwaremäßige Konfiguration des MS setzt voraus, daß die Geräte hardwareseitig (DC, MS-Bus)
bereits verbunden wurden. Vor dem MS-Betrieb können auch Slave-Geräte ferngesteuert konfiguriert werden, sind
jedoch nach der Initialisierung des MS-System nur noch lesend ansprechbar. Man kann alternativ die komplette
Konfiguration des MS-System manuell vornehmen und später, nachdem der Master das System fertig initialisiert
hat, die Fernsteuerung übernehmen.
Sofern die Konfiguration noch nicht manuell erledigt wird, muß sie mittels der Register in einer bestimmten Rei-
henfolge bei jedem Gerät konfiguriert werden:
1. Fernsteuerung aktivieren mit Register 402.
2. Aktivierung des MS mit Register 653.
3. Mit Register 650 festlegen, ob die Einheit Master oder Slave sein soll.
Weitere Schritte nur am Master-Gerät:
4. MS-System initialisieren mit Register 654.
5. Nur wenn Zwei-Quadranten-Betrieb gefahren werden soll und mehrere el. Lasten ein MS-System bilden:
Master-Last mit Register 652 als Share-Bus-Slave definieren, ansonsten funktioniert die Quadrantenumschal-
tung über den Share-Bus nicht.
6. (optional) MS-Initialisierung mit Register 655 überprüfen, ob erfolgreich.
7. (optional) Anzahl der tatsächlich durch den Master initialisierten Slaves abfragen mit Register 662 --> sollte
die ausgelesene Anzahl nicht mit der geplanten übereinstimmen, so ist die Konfiguration hardwareseitig zu
überprüfen und softwaremäßig zu wiederholen.
8. (optional) Nennwerte (Register 656-660) des zuvor initialisierten MS-Systems auslesen, um diese als Referenz
für die Umrechnung der Soll-/Istwerte zu verwenden solange MS in Benutzung ist.
Ab Firmware KE 2.13 (9000er Geräte ohne GPIB) bzw. KE 2.04 (9000er Geräte mit GPIB) ist
Schritt 8 nicht mehr nötig. Die Nennwerte für Spannung, Strom, Leistung und Widerstand (min,
max) des initialisierten MS-Systems können auch im MS-Modus über die Register 121 - 129
ausgelesen werden.
9. (optional) Weitere Werte wie Alarmschwellen, Event-Schwellen oder Einstellgrenzen konfigurieren.
Während des MS-Betriebes kann der ferngesteuerte Master wie ein Einzelgerät angesprochen werden, mit ein paar
Einschränkungen (siehe Gerätehandbuch). Soll- und Istwerte sind bei ModBus immer Prozentwerte, bezogen auf
die aktuell gültigen Nennwerte. Zugriff auf diese Werte über die diversen Register ist in den anderen Abschnitten
erläutert.
4.11.8 Register 850 - 6695 (Funktionsgenerator)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─  ─   ─ ─ ─ ─ ─   ─ 
Der interne Funktionsgenerator ist eine sehr komplexe Funktionalität. Er wird über mehrere Register konfiguriert und
geladen. Es ist vor der eigentlichen Anwendung einer Funktion auf einen DC-Ausgangs- bzw. DC-Eingangswert eine
Konfiguration in einer bestimmten Reihenfolge vorzunehmen. Die am HMI direkt verfügbaren Standardfunktionen
wie Rechteck, Sinus usw. sind in Fernsteuerung nur indirekt verfügbar, über den arbiträren Funktionsgenerator.
Zu allererst müssen Sie bestimmen, welcher Generator genau verwendet werden soll, Arbiträr oder XY. Von dieser
Auswahl hängen weitere Schritte ab. Andere Funktionen, wie z. B. Batterietest oder MPP-Tracking, sind am HMI
zwar zum Funktionsgenerator zugehörig, werden aber rein softwaremäßig umgesetzt.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 29
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Alle über Fernsteuerung getroffenen Einstellungen bezüglich des Funktionsgenerators, sowie
alle in das Gerät geladenen Sequenzen oder XY-Tabellendaten werden nicht im Gerät gespei-
chert und sind somit nur temporär. Sie müssen vor dem Start einer Funktion immer komplett
neu in das Gerät geladen werden. Alle diese Werte und Einstellungen sind getrennt von denen
an der Bedieneinheit einstellbaren.
4.11.8.1 Vorgehensweise beim Arbiträrgenerator
Schritt 1:
Auswahl, ob die Funktion auf die Spannung U (Register 851) oder den Strom I (Register 852) angewendet werden
soll. Bevor das nicht erfolgt ist, kann das Gerät keine Sequenzpunktdaten annehmen, weil diese auf Plausibilität
überprüft werden, was mittels Prüfung der Sequenzpunktwerte gegen die Einstellgrenzen des Gerätes geschieht.
Schritt 2:
Endsequenzpunkt (Register 860), Startsequenzpunkt (Register 859), sowie Durchläufe (Register 861) festlegen.
Schritt 3:
Sequenzpunktdaten laden (Register 900 - 2468, pro Sequenzpunkt 8 Werte), beliebige Anzahl von Sequenzpunkten,
wie benötigt.
Schritt 3.1:
Nicht immer erforderlich: Submit-Befehl (Register 862) senden. Der Befehl ist bei manchen Schnittstellen, welche
die Daten in Stücken senden, immer erforderlich. Z. B. bei CANopen. Dort wird er nur nicht als ModBus-Nachricht
geschickt. Bei ModBus ist er nicht erforderlich, wenn die Register 859, 860 sowie 861 vor dem Laden der Sequenz-
daten schon festgelegt wurden. Werden diese jedoch danach beschrieben oder, was viel wichtiger ist, irgendwann
später neu gesetzt, dann muß 862 beschrieben werden, um die Änderungen zu übernehmen oder man müßte sonst
die Daten der benutzten Sequenzpunkte neu schreiben.
Schritt 4:
Obergrenze für den Strom (Register 501, plus 499 für die PSB-Serien) setzen, falls Funktion auf die Spannung
angewendet. Ansonsten Obergrenze für die Spannung (Register 500) setzen, falls Funktion auf den Strom an-
gewendet wird. Obergrenze für die Leistung (Register 502, plus 498 für die PSB-Serien) für beide Modi setzen.
Schritt 5:
Funktionsgenerator starten bzw. stoppen (Register 850). Dabei wird der DC-Eingang/Ausgang automatisch mit
eingeschaltet, sofern noch aus. Alternativ und falls man die statischen Sollwerte vor dem Start der Funktion anlie-
gen haben wollte, könnte man den DC-Eingang/Ausgang vor dem Start der Funktion einschalten (Register 405).
Nach einem Stopp kann der FG auch umkonfiguriert werden, indem z. B. der Start- und/oder Endsequenzpunkt
verschoben wird. In diesem Fall muß der Submit-Befehl geschickt werden, siehe Schritt 3.1.
Schritt 6:
Zum Verlassen des Funktionsgenerators die Auswahl U (Register 851) bzw. I (Register 582) von Schritt 1 wieder
rückgängig machen.
4.11.8.2 Programmierbeispiel für den Arbiträrgenerator
Bevor Sie den Arbiträrgenerator mit Daten füttern können, sollte überlegt werden, wie man eine Rampe oder
Rechteck oder Trapez usw. mit dem Arbiträrgenerator realisieren kann. Wichtig dabei ist, daß der Arbiträrgenerator
am Ende des Ablaufs automatisch stoppt. Dabei bleibt der DC-Eingang/Ausgang des Gerätes jedoch an und das
Gerät geht wieder in den statischen Modus und setzt die Sollwerte, die global für den Betrieb festgelegt wurden. Die
statischen Werte gelten aber auch für den Zeitraum vor dem Start der Funktion, zumindest falls der DC-Eingang/
Ausgang vorher schon eingeschaltet ist.
Das mit dem Stopp am Ende und Setzen des statischen Wertes ist für eine Rampe oft nicht gewollt, weil ihr
Endwert für eine Zeit x konstant bleiben soll. Der statische Wert wäre zwar auch konstant, soll hier aber u. U. gar
nicht wirken. Warum? Angenommen, bei einem Netzgerät soll die Rampe bei 0 V starten. Dann würde man den
statischen Wert der Spannung, den Spannungssollwert auf 0 V einstellen, den DC-Ausgang einschalten und da-
nach die Funktion ablaufen lassen. Am Ende der Funktion würde das Gerät aber wieder statisch 0 V setzen. Also
muß die konstante Spannung am Ende der Rampe zum Teil der Funktion werden. Es ergibt sich daraus, daß die
Rampe aus zwei Abschnitten besteht: der ansteigenden bzw. abfallenden Flanke und dem konstanten Wert am
Ende. Mittels des Arbiträrgenerators setzt man das mit zwei Sequenzen um.
Annahme: die Rampe soll bei einem Netzgerät einen Spannungsanstieg von 0 V auf 50 V in einer Zeit von 6 s
darstellen. Die Endspannung von 50 V soll für 3 Minuten konstant bleiben (die Zeit hier ist beliebig variabel). Die
zwei Sequenzen, die wir dazu verwenden, sind Sequenz 1 und 2. Fernsteuerung ist bereits aktiv, es wird zunächst
konfiguriert.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 30
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Da eine Rampe die Spannung linear ansteigen läßt, also nur den DC-Anteil einer Sequenz nutzt, sollten die
Parameter	die	zum	hier	nicht	genutztem	AC-Anteil	gehören	zur	Sicherheit	alle	auf	0	gesetzt	werden,	damit	nicht
irgendwelche	Restparameter	den	späteren	Ablauf	stören	können.
Als erstes muß der Funktionsgenerator-Modus aktiviert werden (Register 851, Modus U, WSC):
| Adr. FN   | Start Daten    | CRC    |     |
| --------- | -------------- | ------ | --- |
| 0x01 0x05 | 0x0353 0xFF00  | 0x7C6F |     |
Nun zur Erstellung der ModBus-Nachricht für die Konfiguration von Sequenz 1, die ansteigende Flanke. Laut
Registerliste ist das Startregister 900 für Sequenz 1 ein WMR-Register (Funktionsnummer 0x10). Da der Datenteil
hier im Dokument in der gesamten Breite nicht hereinpaßt, werden die 8 Float-Werte untereinander aufgeführt:
| Adr. FN | Start Regs | Bytes Daten | CRC Beschreibung |
| ------- | ---------- | ----------- | ---------------- |
0x01 0x10 0x0384 0x0010 0x20 0x00000000  Startwert AC-Anteil: 0 V
|     |     | 0x00000000 | Endwert AC-Anteil: 0 V                            |
| --- | --- | ---------- | ------------------------------------------------- |
|     |     | 0x00000000 | Startfrequenz AC-Anteil: 0 Hz                     |
|     |     | 0x00000000 | Endfrequenz AC-Anteil: 0 Hz                       |
|     |     | 0x00000000 | Winkel AC-Anteil: 0°                              |
|     |     | 0x00000000 | Startwert DC-Anteil: 0V                           |
|     |     | 0x42480000 | Endwert DC-Anteil: 50V                            |
|     |     | 0x4AB71B00 | 0x52B8 Anstiegszeit	in	μs:	6.000.000	(6	Sekunden) |
Jetzt die ModBus-Nachricht für die Konfiguration von Sequenz 2, die statische Spannung. Startregister ist
hier dann 916:
| Adr. FN | Start Regs | Bytes Daten | CRC Beschreibung |
| ------- | ---------- | ----------- | ---------------- |
0x01 0x10 0x0394 0x0010 0x20 0x00000000  Startwert AC-Anteil: 0 V
0x00000000 Endwert AC-Anteil: 0 V
0x00000000 Startfrequenz AC-Anteil: 0 Hz
0x00000000 Endfrequenz AC-Anteil: 0 Hz
0x00000000 Winkel AC-Anteil: 0°
0x42480000 Startwert DC-Anteil: 50V
0x42480000 Endwert DC-Anteil: 50V
Sequenzzeit	in	μs:	180.000.000	(180	Sekunden
|     |     | 0x4D2BA950 | 0x627B |
| --- | --- | ---------- | ------ |
= 3 Minuten)
Dann	noch	den	Arbiträrgenerator	konfigurieren:
| Adr. FN | Start Daten | CRC Beschreibung |     |
| ------- | ----------- | ---------------- | --- |
0x01 0x06 0x035B 0x0001  0x399D Register 859, WSR, Startsequenz: 1
0x01 0x06 0x035C 0x0002  0xC85D Register 860, WSR, Endsequenz: 2
0x01 0x06 0x035D 0x0001  0xD99C Register 861, WSR, Sequenzzyklen: 1
0x01 0x05 0x035E 0xFF00  0xEDAC Register 862, WSC, Einstellungen für den FG jetzt übernehmen
0x01 0x06 0x01F5 0xCCCC 0xCD51 Register	501,	WSR,	globaler	Stromsollwert:	100%
0x01 0x06 0x01F6 0xCCCC 0x3D51 Register	502,	WSR,	globaler	Leistungssollwert:	100%
Das Setzen der globalen Sollwerte (Strom, Leistung) auf ihr Maximum oder einen anderen
sinnvollen Wert, der die Rampenerzeugung nicht stört, ist immer erforderlich. Das gilt besonders,
wenn mehrere Geräte im Master-Slave arbeiten. Dort begrenzen diese Sollwerte auch die Slaves.
Danach	ist	die	Rampenfunktion	fertig	konfiguriert	und	kann	gestartet	werden.	Ist	der	DC-Ausgang	noch	aus,	wird
er durch den Start des Funktionsgenerators automatisch eingeschaltet. Alternativ kann das auch vorher mit dem
entsprechenden	Befehl	geschehen,	was	hier	aber	nicht	nötig	ist,	weil	bei	0	V	gestartet	wird.	Soll	eine	Funktion	bei
einem Wert ungleich 0 starten, muß der DC-/Ausgang vorher schon eingeschaltet sein.
Bei der Anzahl der Durchläufe reicht 1x. Das kann aber nach Belieben geändert werden. Dann würde die Funktion
nach 3 m 6 s mindestens einmal erneut ablaufen. Die Spannung würde jedoch nicht schlagartig von 50 V auf 0 V
absinken	können,	so	wie	für	die	steigende	Flanke	gefordert.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 31
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Die zweite und weitere Rampen sähen dann etwas unförmiger aus. Um das zu verhindern, könnte eine dritte
Sequenz programmiert werden, die der Spannung einfach eine gewisse Zeit gibt, um wieder auf 0 zu sinken. Wie
schnell die Spannung sinkt hängt in erster Linie von der Belastung am DC-Ausgang ab.
Adr. FN Start Daten CRC Erläuterung
0x01 0x05 0x0352 0xFF00 0x2DAF Register 850, WSC, Funktionsablauf starten
4.11.8.3 Vorgehensweise beim XY-Generator
Schritt 1:
Moduswahl des XY-Generators über folgende Register:
Modus Serien PSB 9000 / PSB 10000 / ELR Alle anderen Serien mit XY-Generator
10000 / PSI 10000
UI nicht verfügbar 854
IU 856 855
Einfache PV (nur Netzgeräte) 856 426
FC (nur Netzgeräte) 856 854 (als UI-Modus)
Schritt 2:
Tabellendaten in 256 Blöcken mit 16 Werten (Register 2600 - 6695) laden. Das entspricht 4096 Werten und einem
Meßbereich von 0-125% U oder I . Es können auch weniger Werte geladen werden, z. B. von 0-100% dann
Nenn Nenn
3277 Werte. Alle nicht gesetzten Tabellenwerte entsprechen 0 V oder 0 A.
Schritt 3:
Dieser Schritt war nur in älteren Firmwareständen erforderlich. Es gilt: wenn in der dem älteren Stand entspre-
chenden Registerliste das Register 858 noch aufgeführt ist, muß es verwendet werden
Tabellendaten übernehmen (Register 858).
Schritt 4:
Die statischen Sollwerte setzen, die nicht durch die Tabelle selbst bestimmt werden.
UI-Tabelle: Strom (Register 501 bzw. CURR-Befehl) und Leistung (Register 502 bzw. POW-Befehl).
IU-Tabelle: Spannung (Register 500 bzw. VOLT-Befehl) und Leistung (Register 502 bzw. POW-Befehl).
Schritt 5:
Funktionsgenerator starten indem der DC-Eingang/Ausgang eingeschaltet wird (Register 405). Bei einer PV-Funktion
zusätzlich während des Funktionsablaufs über den Stromsollwert (Register 501) die Beschattung variieren, falls
benötigt. Dabei entsprechen 100% Stromsollwert einem Faktor von 1 und 0% einem Faktor von 0. Dieser Faktor
wird mit dem Stromwert I des MPP des simulierten Solarmoduls multipliziert, der irgendwo auf der PV-Kurve
MPP
sitzt, die in Schritt 2 geladen wurde.
Schritt 6:
Zum Verlassen des Funktionsgenerator die in Schritt 1 getroffene Moduswahl mit denselben Registern rückgängig
machen.
4.11.9 Register 850 - 1692 (Sequenzgenerator in ELR 5000)
Der sogenannte Sequenzgenerator der ELR/ELM 5000 Series ist eine vereinfachte Version des Arbiträrgenerators
anderer Serien und belegt daher zum Teil dieselben Register. Gemäß der Registerliste für Serie ELR 5000 werden
über den Registerbereich 850 bis 1692 die 100 Sequenzpunkte der „Sequenz“ konfiguriert, sowie der Sequenz-
generator selbst konfiguriert und gesteuert.
4.11.10 Register 850 - 854 und 900 - 908 (Funktionsgenerator in EL 3000 B)
Der Funktionsgenerator der in 2017 neu veröffentlichten Serien EL 3000 B basiert auf einem Rampengenerator
und bietet daher die Funktionen Rampe, Dreieck, Rechteck und Trapez. Es werden hier teils dieselben Register
wie bei anderen Serien verwendet, aber mit unterschiedlicher Verwendung.
4.11.10.1 Programmierbeispiel
Angenommen, Sie möchten bei einer EL 3080-60 B ein Rechteck mit 50 Hz auf den Strom anwenden, bei ei-
ner Amplitude von 8 A, einem Offset von 1 A und einem Tastverhältnis von 9:1. Es wären zur Konfiguration laut
Registerliste folgende Register in der Reihenfolge von oben nach unten zu laden:
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 32
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| Register | Name |     | Verwendung  |     |     |     |     |     |     |
| -------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Funktionsgenerator auf den Strom anwenden. Muß als erstes gesetzt werden,
| 852 | Wähle Modus "I" |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
damit das Gerät die nachfolgenden Parameter gegenprüfen kann.
Offset,	soll	auf	1	A	gesetzt	werden.	Das	wäre	als	hexadezimaler	Prozentwert
| 900 | Statischer Pegel 1 |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
0x369
901 Statischer Pegel 2 Amplitude	+	Offset,	soll	auf	9	A	gesetzt	werden,	also	0x1EB1
Da es ein Rechteck werden soll, wäre die Zeit eigentlich auf 0 zu setzen, aber
| 902 / 906 | Anstiegszeit / Abfallzeit |     |     |     |     |     |     |     |     |
| --------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3	μs	sind	das	Minimum.	Also	eine	3	als	Fließkommazahl	setzen.
Entspricht	den	90%	Puls.	Bei	50	Hz	ist	die	Periode	20	ms,	also	sind	90%
904 Haltezeit Pegel 2 dann	18	ms	bzw.	18000	μs.	Das	Register	wird	mit	einer	Fließkommazahl
von 18000 beschrieben.
Entspricht	den	10%	Pause.	Bei	50	Hz	ist	die	Periode	20	ms,	also	sind	10%
908 Haltezeit Pegel 1 dann	2	ms	bzw.	2000	μs.	Das	Register	wird	mit	einer	Fließkommazahl	von
2000 beschrieben.
Nach dem Setup kann bereits gestartet werden.
| Register | Name |     | Verwendung  |     |     |     |     |     |     |
| -------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Funktionsgenerator starten mit 0xFF00. Er läuft mit den eingestellten Parame-
| 850 | Start / Stop |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tern solange bis durch Senden von 0x0000 oder einen Gerätealarm gestoppt.
Dieser	FG	ist	eine	Ausnahme,	denn	er	kann	neue	Werte	übernehmen	während	er	läuft.	Diese	können	über	Register
900	-	908	umdefiniert	werden	und	erst	beim	Schreiben	auf	Register	854	werden	sie	aktiv	bzw.	erst	nach	Ablauf
der gegenwärtigen Periode, die durch die vorher gültigen Zeitwerte festgelegt wurde. Man kann eine Periode so
nicht mittendrin stoppen, um ein andere zu fahren. Das geht nur über Stopp des FG.
| Register | Name |     | Verwendung  |     |     |     |     |     |     |
| -------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Übernehme neue Wer- Die zuvor geschriebenen Daten mit 0xFF00 übernehmen. Sollten noch keine
854
te zur Laufzeit neuen geschrieben worden sein, bleiben die alten gültig.
| 4.11.11  | Register 9000 - 9009 (Einstellgrenzen) |     |     |     |     |     |     |     |     |
| -------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|   |   | ─  |   |   |   |   |   |   |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Für SCPI sind die Einstellgrenzen in „5.4.8. Befehle für Einstellgrenzen“ erläutert. ModBus-Anwender sollten den
Abschnitt jedoch auch lesen, weil die generelle Handhabung der Einstellgrenzen erläutert wird. Ansonsten ist das
Setzen dieser Parameter wie bei den Sollwerten U, I, P und R.
| 4.11.12  | Register 10007 - 10900 |     |     |     |     |     |     |     |     |
| -------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|   |   |   |   |   |   |  ─ |   |   |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Diese	Register	dienen	der	ferngesteuerten	Konfiguration	der	verschiedenen	digitalen	Schnittstellen,	die	teils	seri-
enmäßig eingebaut, teils optional für die genannten Serien erhältlich sind. Diese Register sind verknüpft mit den
über die Bedieneinheit einstellbaren Parametern.
Im Gegensatz zur manuellen Bedienung kann bei den steck- und nachrüstbaren Schnittstellenmodulen der IF-
AB-Serie	(für	Serie	PSI	9000	3U	usw.)	die	ferngesteuerte	Konfiguration	bereits	stattfinden,	wenn	das	Modul	noch
nicht installiert ist.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 33
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
4.11.13 Register ab 11000 (MPP-Tracking)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
  ─ ─ ─ ─  ─ ─   ─ ─ ─ ─ ─  ─ 
Das Feature MPP-Tracking wird nur von bestimmten Serien elektronischer Lasten und auch von den bidirektionalen
Netzgeräten der PSB-Serien unterstützt. Mit dieser Funktion simuliert das Gerät als Senke das Verhalten eines
Solarwechselrichters, wenn er das typische Suchen (engl.: tracking) nach dem MPP (maximum power point) an
einem Solarpaneel ausführt. Einzelheiten über dieses Features und dessen Modi sind in den Handbüchern der
Geräteserien zu finden, die MPP-Tracking unterstützen.
Register 11000 - 11016 sind verknüpft mit den Konfigurations-Parametern wie man sie auch in der Anzeige des
Gerätes einstellen könnte. Register 11100 - 11199 entsprechen der Funktion „Spannungswerte von USB-Stick“
laden, wie man es bei manueller Bedienung für Modus MPP4 tun könnte, während die Register 11200 - 11499 der
Funktion „Resultatdaten auf USB-Stick speichern“ entsprechen, wie sie verfügbar werden, wenn Modus MPP4
fertig ist mit seinem Durchlauf.
4.11.13.1 Programmierbeispiel für Modus MPP4
Modus MPP4 ist in allen der o. g. Serien per Fernsteuerung verfügbar, jedoch nicht bei allen auch am HMI und
deshalb nicht im Handbuch beschrieben. Wenn weitere Informationen zu diesem Modus benötigt werden, z. B.
in das Handbuch der Serie EL 9000 B 3U schauen. Die Tabelle unten zeigt die Reihenfolge der zu schreibenden
Register auf. Es werden hier 75 Punkte auf der benutzerdefinierbaren Kurve geladen.
Register Name Verwendung
11000 Wähle MPP4 Funktionsgenerator auf Modus MPP4 setzen.
75 Spannungswerte auf einer benutzerdefinierbaren (PV) Kurve laden. Die
11000 - nächsten beiden Schritte definieren zudem den Bereich an Punkten für den
Kurvendaten laden
11174 späteren Durchlauf. Sollte ein Punkt angefahren werden, der nicht vom Anwender
geladen wurde, wird für diesen 0 V gesetzt.
Definiert den letzten Punkt für den Durchlauf. Beliebiger Wert zwischen 1 und
11015 Endpunkt setzen 100. Da der Startpunkt nicht größer sein kann als der Endpunkt, wird der End-
punkt zuerst gesetzt.
Definiert den ersten Punkt für den Durchlauf. Beliebiger Wert zwischen 1 und
11014 Startpunkt setzen
dem Endpunkt. Kann nicht größer sein als der Endpunkt.
11013 Trackingintervall Definiert die Zeit (in Millisekunden) zwischen zwei Punkten der Kurve.
Definiert die Anzahl der zusätzlichen Durchläufe. Die später auslesbaren Ergeb-
11016 Wiederholungen nisdaten enthalten immer nur die Meßwerte des letzten Durchlaufs. Wenn die
Kurve nur einmal durchlaufen werden soll, wäre hier 0 zu setzen.
Nach dem Start beginnt das Gerät mit dem ersten Punkt aus dem gesetzten
Bereich, läuft alle Punkte und Wiederholungen durch und stoppt dann. Die Ge-
11010 Tracking starten samtzeit ergibt aus dem Trackingintervall, dem Punktebereich und den Durch-
läufen. Der Test kann jederzeit über dieses Register wieder gestoppt werden.
Die bis dato ermittelten Daten werden dann verfügbar.
11011 Status auslesen optional: Dient während des Tests zur Ermittlung, wann er beendet ist.
optional: Dient während oder nach dem Test zur Ermittlung, ob der Test an sich
11012 Fehler auslesen
erfolgreich beendet wurde.
4.11.14 Register ab 11500 (Batterietest)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─ ─ ─ ─  ─ ─   ─ ─ ─ ─ ─  ─ 
Geräteserien, deren Modelle als elektronischen Last arbeiten können wie z. B. EL, ELR oder PSB, und einen
eingebauten Functionsgenerator, bieten eine am Gerät bedienbare Batterietestfunktion. Diese Funktion ist auch
per Fernsteuerung konfigurier- und steuerbar und entweder bereits auf dem Gerät installiert oder kann durch ein
Firmware-Update nachgerüstet werden.
Wie auch bei der manuellen Bedienung am HMI gibt es in der Fernsteuerung mehrere Modi und nicht alle Serien
bieten dieselben Features, was sich bereits aus der Art des Gerätes ergibt. Parameter werden teils getrennt, teils
allgemein vorgegeben, jedoch sind Steuerung sowie Auswertung nach Testende für alle Modi gleich. Die Register
sind direkt verknüpft mit den entsprechenden, am HMI einstellbaren Werten. Daher wird empfohlen, zunächst
den Abschnitt zum Batterietest im Handbuch des Gerätes zu lesen und dann am Gerät mit den Einstellungen und
Abläufen zu "spielen", um diesen Test kennenzulernen.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 34
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Hier eine Übersicht der involvierten Register:
| Register | Verwendung                                   |     |     |     |     |     |     | EL(R)? | PSB? |
| -------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ---- |
| 11535    | Aktivierung und Wahl des Batterietest-Modus‘ |     |     |     |     |     |     | x      | x    |
11500 - 11513 Konfiguration	des	Batterietest-Modus‘	"Entladung"	mit	statischem	Strom x x
11514 - 11531 Konfiguration	des	Batterietest-Modus‘	"Entladung"	mit	gepulstem	Strom x x
11545 - 11558 Konfiguration	des	Batterietest-Modus‘	"Ladung"	mit	statischem	Strom - x
11559 - 11584 Konfiguration	des	dynamischen	Batterietest-Modus‘	"Ladung/Entladung"	 - x
| 11532         | Steuerung des Testablaufs                           |     |     |     |     |     |     | x   | x   |
| ------------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11536 - 11544 | Auswertung (Zeit, Ah, Wh)                           |     |     |     |     |     |     | x   | x   |
| 4.11.15       | Register ab 12000 (PV-Simulation nach DIN EN 50530) |     |     |     |     |     |     |     |     |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT PSB EL3 PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
| ─ ─ | ─  | ─ ─ | ─ ─ | ─  | ─ ─ | ─ ─ | ─  |  ─ | ─   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PV-Simulation wird generell nur von Netzgeräte-Serien unterstützt und dabei nur von jenen, die einen sog. XY-
Generator haben. Das sind mit Stand 03/2020):
•	 PSI 9000 2U - 24U
•	 PSI 9000 WR
•	 PSB 9000 / PSB 10000
Die Variante nach DIN EN 50530 ist eine erweiterte Version der einfachen PV-Simulation und wird von den Geräten
ab Firmware KE 2.19/HMI 2.11 (9000er Serien ohne GPIB) bzw. KE 2.05/HMI 2.11 (9000er Serien mit GPIB) und
KE 2.25/HMI 2.04 (PSB 9000) unterstützt. Alle über die Register einstellbaren Parameter sowie die auslesbaren
Daten	sind	in	der	Norm	definiert,	werden	dort	beschrieben	und	daher	ist	die	Norm	für	den	Anwender	die	Referenz
zum Gebrauch der Funktion.
Die Vorgehensweise bei der Programmierung über die kompatiblen Schnittstellen ist bei Verwendung des ModBus
-Protokolls nicht anders als bei manueller Bedienung (siehe Geräte-Handbücher) oder bei Verwendung des SCPI-
Protocols (siehe Beispiele im Abschnitt „5.5.3. Programmier-Beispiele zur PV-Simulation (DIN EN 50530)“). Die
dortigen	Beispiele	enthalten	je	eine	Spalte	mit	der	zugehörigen	ModBus-Registernummer.	Davon	Beispiel	2	als
Umsetzung für ModBus RTU (prozentuale Sollwerte umgerechnet für ein PSI 9080-170):
Konfiguration (vor dem Start)
| Nr. Befehl                |     |     |     | Beschreibung             |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
| 1 01 05 01 92 FF 00 2C 2B |     |     |     | Fernsteuerung aktivieren |     |     |     |     |     |
2 01 06 2E E1 00 03 90 D5 PV-Simulation aktivieren, Simulations-Modus DAYET
3 01 06 2E F0 00 00 80 D1 Technologie wählen: Manuell (alle erforderlichen Techno-
logie-Parameter müssen angegeben werden)
4 01 10 2F 02 00 02 04 3F 4C CC CD F3 11 Füllfaktor Spannung (FF U ): 0,8
| 5 01 10 2F 04 00 02 04 3F 47 AE 14 EA 03 |     |     |     | Füllfaktor Strom (FF): 0,78 |     | I   |     |     |     |
| ---------------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
6 01 10 2F 06 00 02 04 39 9D 49 52 80 AB Temperaturkoeffizient	α	zu	I SC : 0,0003 /°C
7 01 10 2F 08 00 02 04 BB 44 9B A6 A5 83 Temperaturkoeffizient	β	zu	U : -0,003 /°C
OC
8 01 10 2F 0A 00 02 04 3D 94 7A E1 04 89 Korrekturfaktor C  zu U : 0,0725
U OC
9 01 10 2F 0C 00 02 04 39 66 AF CD 7B 2D Korrekturfaktor C  zu U : 0,00022 m²/W
R OC
10 01 10 2F 0E 00 02 04 3B 4E 70 3B A3 32 Korrekturfaktor C  zu U : 0,00315 W/m²
G OC
| 11 01 05 2E F1 FF 00 D4 E1  |     |     |     | Eingabemodus wählen: ULIK |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
12 01 06 2F 10 61 47 E9 79 Leerlaufspannung setzen: 38 V (=0x6147)
13 01 06 2F 11 08 6F 96 F7 Kurzschlußstrom setzen: 7 A (=0x086F)
| 14 01 05 2E F2 FF 00 24 E1 |     |     |     | Datenaufzeichnung aktivieren |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
15 01 05 2E E5 00 00 D5 15 Interpolation der Tagesdaten deaktivieren
16 01 06 01 F4 61 47 A0 66 Globalen	Spannungssollwert	setzen:	≥Uoc	(=0x6147)
17 01 06 01 F6 CC CC 3D 51 Globalen	Leistungssollwert	setzen:	100%	(=0xCCCC)
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 35
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Tagesdaten laden (vor dem Start)
Nr. Befehl Beschreibung
18 01 05 2E E6 FF 00 64 E5 Zugriffsmodus Schreiben wählen
19 01 05 2E E7 FF 00 35 25 Alte Daten löschen (sollte vor dem Laden neuer Daten immer
ausgeführt werden)
20 01 10 2E EA 00 06 0C 00 00 00 01 44 44 66 Ersten Tages-Datensatz in Index 1 schreiben mit:
66 00 00 03 E8 B5 76 Einstrahlungsstärke: 500 W/m² (=0x4444)
Temperatur: 20°C (=0x6666)
Verweildauer: 1000 ms (=0x000003E8)
Die Verweildauer ist zwar auf minimal 500 ms definiert, der Wert für den ersten
Tagesdatensatz muß 1000 ms oder höher betragen, sonst könnte der Ablauf fehlschlagen.
21 01 10 2E EA 00 06 0C 00 00 00 02 6D 3A 74 Zweiten Tages-Datensatz in Index 2 schreiben mit:
0D 00 00 05 DC D9 3F Einstrahlungsstärke: 800 W/m² (=0x6D3A)
Temperatur: 28°C (=0x740D)
Verweildauer: 1500 ms (=0x000005DC)
... Weitere Tages-Datensätze schreiben, insgesamt 500
519 01 10 2E EA 00 06 0C 00 00 01 F4 A3 D6 7F 500. Tagesdaten-Satz in Index 500 schreiben mit:
FF 00 00 4E 20 09 53 Einstrahlungsstärke: 1200 W/m² (=0xA3D6)
Temperatur: 35°C (=0x7FFF)
Verweildauer: 20000 ms (=0x000034AF)
Steuerung
Nr. Befehl Beschreibung
520 01 05 2E E0 FF 00 84 E4 Simulation starten (Register 12000) -> die Simulation läuft ab
und stoppt automatisch nach der Gesamtzeit, die sich aus
den Verweildauern aller geladenen Tages-Datensätze ergibt
Während die Simulation läuft, wird der Indexzähler in Register 12010 mit jedem angefahrenen
Tagesdatenpunkt aktualisiert, so daß man ihn auslesen und die Simulation ggf. an einem be-
stimmten Index abbrechen kann oder nach einem unerwarteten Stopp durch z. B. einen Gerä-
tealarm ermitteln, an welchem Punkt die Kurve gestoppt wurde.
Auswertung nach dem Ende der Simulation
Nr. Befehl Beschreibung
521 01 03 2E F4 00 02 8C D1 Anzahl (n) der aufgezeichneten Datensätze ermitteln. Die
Anzahl ist nicht gleichbedeutend mit der Anzahl der Tages-
Datensätze, weil die Aufzeichnung kontinuierlich alle 100
ms aufzeichnet. Je nach Gesamtdauer der Simulation
könnte der Aufzeichnungsspeicher vollgelaufen (max. 16
h Aufzeichnungsdauer) und Daten überschrieben worden
sein. Es kann daher notwendig werden, vor dem Start die
Gesamtdauer aus den Tages-Datensätzen zu ermitteln und
die aufgezeichneten Daten bereits während der Simulation
auszulesen, den Speicher zu löschen und später den Rest
auszulesen.
522 01 10 2E F6 00 02 04 00 00 00 01 68 A0 Index 1 anwählen zum Auslesen
523 01 03 2E F8 00 08 CC D5 Daten von Index 1 auslesen
... Weitere n-1 Datensätze auslesen:
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 36
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5. SCPI-Protokoll
SCPI ist ein internationaler Standard für eine klartextbasierte Befehlssprache. Näheres zum Standard selbst finden
Sie im Internet.
5.1 Format der Soll- und Istwerte
Bei SCPI werden alle Werte immer als reale Werte dargestellt, mit oder ohne Einheit. Wenn Sie z. B. den Ein-
gangsstrom auf 177,5 A festlegen möchten, dann könnte das mit dem Befehl CURR 177.5 oder mit CURR 177.5A
geschehen. Eine genauere Erläuterung der Syntax finden Sie unten.
5.2 Syntax
Spezifikation nach „1999 SCPI Command reference”.
Folgende Formate für Werte und Parameter können in Befehlen bzw. Antworten auftreten:
<value> Der Zahlenwert entspricht dem Zahlenformat im Display des Gerätes und ist abhängig von den
Nennwerten des Gerätes. Es gilt:
- Der Wert wird vom voranstehenden Befehl immer mit einem Leerzeichen getrennt eingeben
- Anstatt eines Zahlenwertes können alternativ eingegeben werden:
MIN Entspricht dem Minimalwert des Parameters
MAX Entspricht dem Maximalwert des Parameters
<NR1> Zahlenformat ohne Dezimalpunkt und ohne phys. Einheit
<NR2> Zahlenformat mit Dezimalpunkt (Fließkomma), inkludiert NR1, mit oder ohne phys. Einheit
<NR3> Wie <NR2>, aber plus Größenordnung (unterstützt werden: k/K für Kilo)
<NRf> <NR1> oder <NR2> oder <NR3>, negatives Vorzeichen möglich
Unit V (Volt), A (Ampere), W (Watt), OHM, s (Sekunden)
<CHAR> 0..255: Dezimalzahl
<+INT> 0..32768: positive Integerzahl (Ausgabe)
<B0> 1 oder ON: Funktion wird eingeschaltet
0 oder OFF: Funktion wird ausgeschaltet
<B1> NONE: lokaler Betrieb, eine Umschaltung auf Fernbedienung ist möglich
LOCal: nur lokaler Betrieb möglich, Auslesen von Daten ist zulässig
REMote: Fernbedienung des Gerätes ist aktiviert
<ERR> Fehlernummer und Fehlerbeschreibung
<SRD> Stringdaten, verschiedene Formate:
- eine IP-Adresse als Zahlenstring mit Punkten als Trennzeichen, z. B. „192.168.0.2“
- Schlüsselwörter, wie z. B. AUTO oder OFF
<Time1> <NR2>s (Fließkomma-Zeitformat in Sekunden)
<Time2> <SRD> als HH:MM:SS oder HH:MM:SS.MS (Stunden/Minuten/Sekunden/Millsekunden)
<Time3> <NR1>s oder <NR1>ms (ganzzahliges Zeitformat in Sekunden oder Millisekunden)
; Das Semikolon wird verwendet, um innerhalb einer Message mehrere Befehle zu senden.
: Der Doppelpunkt trennt höherwertige Schlüsselwörter von niederwertigeren Schlüsselwörtern
[ ] Kleinbuchstaben und der Inhalt in rechteckigen Klammern sind optional.
? Das Fragezeichen kennzeichnet eine Abfrage. Die Abfrage kann gleichzeitig mit einer Daten-
sendung verknüpft werden. Hierbei ist darauf zu achten, daß, bevor eine neue Datensendung
erfolgt, die Antwort des Systems abgewartet werden muß.
-> Antwort vom Gerät
5.2.1 Groß-/Kleinschreibung
Bei SCPI ist Großschreibung üblich. Die Geräte akzeptieren jedoch auch Kleinschreibung.
5.2.2 Langform und Kurzform
SCPI-Befehle haben immer eine Lang- und eine Kurzform. Die Kurzform (z. B. SOUR) oder die Langform (z. B.
SOURCE) sind beliebig verwendbar. Um die beiden Formen zu unterscheiden sind nachfolgend die Befehle teils
mit Großbuchstaben (markiert die Kurzform) und Kleinbuchstaben geschrieben (markiert den zusätzlichen Teil
der Langform).
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 37
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.2.3 Befehlsverkettung
Es ist möglich, bis zu fünf (5) Befehle auf einmal an das Gerät zu schicken. Zur Trennung ist das Semikolon (;)
zu verwenden. Beispiel:
VOLT 80;CURR 20;POW 3kW
Befehle werden in der gesendeten Reihenfolge verarbeitet und, sofern der Ausgang/Eingang des Gerätes ein-
geschaltet ist, auch sofort aktiv. Die Reihenfolge der Sollwerte kann daher von Bedeutung sein bzw. ob sie bei
Eingang/Ausgang = aus oder = ein gesendet werden. Wenn mehrere Werte oder Parameter auf einmal angefragt
werden, kommen diese auch zusammen in einer Antwort, in der angefragten Reihenfolge und auch durch Semi-
kolons getrennt zurück.
Der SCPI-Zeichenpuffer im Gerät ist 256 Bytes groß. Sollte der verkettete Antwortstring einer
verketteten Anfrage mehr als 256 Zeichen ergeben, so wird keine Antwort gesendet, sondern
stattdessen Fehler -225 generiert.
5.2.4 Abschlußzeichen
Manche Schnittstellen erfordern zwingend ein Abschlußzeichen, andere (z. B. USB) nicht. Bei diesen kann es
optional gesendet werden, damit Steuerungssoftwares über verschiedene Schnittstellen hinweg kompatibel bleiben.
Bei Geräten mit der optionalen GPIB-Schnittstelle (3W) sowie bei einer socketbasierten Verbindung über Ethernet
muß immer ein Abschlußzeichen gesendet werden, ansonsten führt das zu einem Kommunikations-Timeout auf
der PC-Seite.
Unterstützt wird: 0xA (LF, line feed)
Die Erfordernis eines Abschlußzeichens wurde nachträglich ab einer bestimmten Firmwarever-
sion eingefügt. Es kann also vorkommen, daß wenn ein Gerät mit einem alten Stand aktualisiert
wird, eine bereits bestehende Steuerungssoftware zunächst nicht mehr funktioniert, wenn diese
das nach dem Update nun erforderliche Abschlußzeichen nicht sendet.
5.2.5 Kommunikationsfehler
Fehlermeldungen im Sinne von SCPI sind normalerweise nur Kommunikationsfehler, können jedoch durch ge-
rätespezifische ergänzt sein. Gemäß IEEE-Standard melden Geräte bei Kommunikation über SCPI Fehler nicht
automatisch zurück. Der oder die möglicherweise aufgetretenen Fehler müssen per Befehl abgefragt werden.
Das kann direkt über Abfragebefehle (siehe 5.4.5.4) oder indirekt (Signal „err“ im Register STB, siehe „5.4.2.
Statusregister“) geschehen.
Das Antwortformat ist im Standard vorgegeben und besteht immer aus einer Zahl (Fehlercode) und einem kurzen,
erläuternden Text. Folgende SCPI-Fehler können generiert werden:
Fehlercode / Fehlertext Beschreibung
0,"No error" Kein Fehler
-100,"Command error" Befehl unbekannt
-102,"Syntax error" Befehl nicht richtig geschrieben
-108,"Parameter not allowed" Der Befehl wurde mit einem Parameter gesendet, obwohl dieser Befehl keine
verwendet
-200,"Execution error" Befehl konnte nicht ausgeführt werden
-201,"Invalid while in local" Ein Steuerungsbefehl konnte nicht ausgeführt werden, weil sich das Gerät im
LOCAL-Modus befindet
-220,"Parameter error" Falscher Parameter wurde verwendet
-221,"Settings conflict" Befehl konnte wegen des gegenwärtigen Zustandes des Gerätes nicht ausgeführt
werden (Gerät ist im Setup-Menü oder noch nicht im Fernsteuerungsmodus)
-222,"Data out of range" Parameter konnte nicht gesetzt werden, weil er eine Grenze überschritt
-223,"Too much data" Zu viele Parameter pro Befehl oder zu viele Befehle auf einmal
-224,"Illegal parameter value" Es wurde ein Parameter vorgegeben, der für den Befehl nicht definiert ist
-225,"Out of memory" Es wurde eine verkettete Anfrage gestellt, deren ebenso verkettete Antwort eine
Länge von 256 Zeichen (SCPI-Puffer) überschreiten würde, wie z. B. 5x *IDN?
-999,"Safety OVP" Ausnahmefall (Gerätealarm), da kein Kommunikationsfehler: Safety OVP wur-
de ausgelöst (nur vorhanden bei den 60 V-Modellen bestimmter Serien), siehe
Handbuch der Geräte. Erfordert, die Geräte auszuschalten und neu zu starten.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 38
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.3 Beispiele zum Einstieg
5.3.1 Ping bzw. Geräteinformationen abfragen
Um zu testen, ob das anzusprechende Gerät überhaupt reagiert, könnte man immer als erstes die Gerätekennung
abfragen:
Protokoll Befehl
SCPI *IDN?
Als Antwort sollte das Gerät sofort senden (Beispiel):
Protokoll Beispielantwort
SCPI EA Elektro-Automatik GmbH&Co.KG, EL 9080-340, 1240210002, V2.14 14.05.2018 V2.24
04.06.2018 V1.6.5
5.3.2 Fernsteuerung aktivieren oder beenden
Bevor Sie das Gerät fernsteuern können, ist Umschalten auf digitalen Fernsteuerbetrieb mittels eines entspre-
chenden Befehls erforderlich. Siehe Dokumentation der einzelnen SCPI-Befehle unten.
Das Gerät schaltet sich niemals automatisch in den Fernsteuerbetrieb und kann ohne diesen
nicht ferngesteuert werden. Auslesen von Istwerten und Status ist dann trotzdem möglich.
Das Gerät verläßt die Fernsteuerung niemals automatisch, außer es wird während des Fern-
steuerbetriebs ausgeschaltet oder es tritt ein Stromausfall auf. Die Fernsteuerung kann gewollt
per Befehl bzw. manuell am Gerät beendet werden.
Das Umschalten auf Fernsteuerung kann durch folgende bestimmte Umstände blockiert sein und wird durch Ab-
legen eines abfragbaren Fehlerstrings quittiert, jedoch zunächst ohne den Anwender zu benachrichtigen:
• Es ist Zustand Lokal aktiv (siehe Anzeige auf der Front), der jegliche Fernsteuerung verhindert
• Es ist bereits Fernsteuerung über eine andere Schnittstelle aktiv
• Das Gerät befindet sich im Setup-Modus (Einstellmenü aktiv)
► So schalten Sie das Gerät in die Fernsteuerung:
1. Wenn Sie die SCPI-Befehlssprache verwenden, schicken Sie den Textbefehl:
SYST:LOCK˽1 oder SYST:LOCK˽ON
Fernsteuerung kann auf zwei Arten beendet werden: per Befehl oder durch Sperrung derselbigen am Bedienfeld
des Gerätes. Da es hier um Programmierung geht, wird die erstgenannte Möglichkeit betrachtet.
► So beenden Sie die Fernsteuerung:
1. Wenn Sie die SCPI-Befehlssprache verwenden, schicken Sie den Textbefehl:
SYST:LOCK˽0 oder SYST:LOCK˽OFF
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 39
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4 Befehlsgruppen
Befehle sind der Zuordnung zu Gerätefunktionen nach in Gruppen sortiert. Nicht alle Geräteserien haben die
gleiche Anzahl von Befehlen zur Verfügung, was in der erster Linie von der Ausstattung abhängig ist. Unten wird
bei den einzelnen Befehlen jeweils angezeigt, in welcher Geräteserie Sie verfügbar sind. Beispiel:
ELR9 PS9 PSI9 PSI5
 ─  ─
Für die Kürzel in der Kopfzeile siehe „1.1.2. Geltungsbereich“. Wobei
 bedeutet, der Befehl oder eine Befehlsgruppe wird ganz oder teilweise von der Geräteserie unterstützt.
─ bedeutet, der Befehl oder eine ganze Befehlsgruppe wird von der Geräteserie nicht unterstützt.
5.4.1 Standard-IEEE-Befehle
In Anlehnung an GPIB und den Standard IEEE 488 wurden einige Standardbefehle implementiert, die in allen
unseren Geräten verfügbar sind, die SCPI unterstützen.
5.4.1.1 *CLS
Löscht die Fehler-Queue, Statusbyte (STB) und alle Bits im Event Status Register (ESR), außer Bit 0.
5.4.1.2 *IDN?
Fragt den Beschreibungsstring des Gerätes ab, der kommagetrennt folgendes enthält:
1. Hersteller
2. Gerätebezeichnung
3. Seriennummer
4. Firmwareversion(en) des Gerätes (falls mehrere, dann mit Leerzeichen getrennt)
5. Benutzertext (wie per SCPI-Befehl syst:config:user:text definierbar)
5.4.1.3 *RST
Setzt das Gerät auf folgenden definierten Zustand, falls Fernsteuerung nicht durch das Gerät blockiert ist:
1. Fernsteuerung einschalten (identisch zu SYST:LOCK 1)
2. DC-Eingang/Ausgang = aus
3. Alarmspeicher leeren
4. Zustandsregister löschen (QUEStionable Event, OPERation Event, STB)
5.4.1.4 *STB?
Der Befehl liest das STatus Byte Register aus. Der Signallauf für die diversen Gerätezustände und Ereignisse
ist im Registerdiagramm unten dargestellt. Die Bits des STB im Einzelnen:
Bit 0: sec_ques, das zweite Questionable Status Rgister ist aktiv (ein oder mehrere Ereignisse stehen an)
Bit 1: nicht verwendet
Bit 2: err, Error Queue --> es sind ein oder mehrere Fehler im Fehlerspeicher. Durch Auslesen des Fehlerspei-
chers oder Befehl *CLS wird dieser gelöscht und das Bit err zurückgesetzt
Bit 3: ques, Questionable Status Register ist aktiv (ein oder mehrere Ereignisse stehen an)
Bit 4: nicht verwendet
Bit 5: esr, Event Status Register ist aktiv (ein oder mehrere Ereignisse stehen an)
Bit 6: Master Summary Status, Sammelmeldung aus dem Service Request Enable Register
Bit 7: oper, Operation Status Register ist aktiv (ein oder mehrere Ereignisse stehen an)
5.4.1.5 *ESR?
Liest das Event Status Register. Dieses Register enthält Signale, welche auf die Übertragung und Ausführung
von SCPI-Befehle bezogen sind.
5.4.1.6 *ESE˽<NR1>
Liest mit *ESE? oder setzt das Event Status Enable Register, das einen Signalfilter für das ESR darstellt. Der
maximal setzbaren Wert ergibt sich aus den unterstützten Bits (siehe Registermodell weiter unten).
5.4.1.7 *SRE˽<NR1>
Liest mit *SRE? oder setzt das Service Request Enable Register.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 40
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 5.4.2  |     | Statusregister |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Es gibt nur für bestimmte Gerätezustände einzelne SCPI-Befehle, daher werden die meisten anderen Zustände
in den Bits von abrufbaren Statusregistern gesammelt. Diese kann man nach Belieben abfragen, entweder direkt
oder indirekt. Indirekt wäre regelmäßig das Statusbyte (STB) zu lesen (Polling), um festzustellen, ob Ereignisse
in den verknüpften Registern (siehe Modell unten) erfaßt wurden. Der Unterschied beim direkten Auslesen wäre
dann der, daß man selbst herausfinden müßte, ob und in welchen Registern sich etwas geändert hat. Dafür genau
ist  das Statusbyte da.
Nachdem ein Bit im STB signalisiert, daß sich im QUES oder OPER ein Zustand geändert hat, sollte man bei den
Registern	OPER	und	QUES	das	zugehörige	Event-oder	Condition-Register	auslesen,	um	zu	wissen,	welche	Bits
sich	verändert	haben.	Nachteil	beim	Lesen	des	Event-Registers:	der	Wert	ändert	sich	nur	bei	positiven	Änderun-
gen (0->1). Das bedeutet, daß z. B. das Bit OVP im Condition-Register, nachdem es 1 war, schon wieder auf 0
sein	könnte	(OVP	gelöscht),	während	das	zugehörige	Bit	im	Event-Register	noch	1	ist	und	sich	erst	ändert,	wenn
man es erneut liest. Vorteil ist hierbei wiederum, daß man nachträglich noch erkennen kann, daß ein OVP-Alarm
aufgetreten war.
Nach dem Start eines Gerätes sind alle :ENABle-Register auf 0 gesetzt
Statusregistermodell (außer Serie PS 2000 B TFT):
Questionable Status
Operation Status
|     |                 |        |           |        | QUES  |     |                     |             |         |     | OPER   |                  |                |
| --- | --------------- | ------ | --------- | ------ | ----- | --- | ------------------- | ----------- | ------- | --- | ------ | ---------------- | -------------- |
|     |                 |        | CONDITION | ENABLE | EVENT |     |                     |             |         |     | EVENT  | ENABLE CONDITION |                |
|     |                 | OVP    | 0 0/1     | U/D    | 0/1   |     | U = User defineable |             |         |     | 0      | 0                | 0/1 0          |
|     |                 |        | 1         |        |       |     | D = Is 1 by default |             |         |     |        |                  | 1              |
|     |                 | OCP    | 0/1       | U/D    | 0/1   |     |                     |             |         |     | 0      | 0                | 0/1            |
|     |                 | OPP    | 2 0/1     | U/D    | 0/1   |     |                     |             |         |     | 0      | 0                | 0/1 2          |
|     |                 | OT     | 3 0/1     | U/D    | 0/1   |     |                     |             |         |     | 0      | 0                | 0/1 3          |
|     |                 |        | 4         |        |       |     |                     |             |         |     |        |                  | 4              |
|     |                 | OVD    | 0/1       | U/D    | 0/1   |     |                     |             |         |     | 0/1    | U/D              | 0/1 REM-SB     |
|     |                 | UVD    | 5 0/1     | U/D    | 0/1   |     |                     |             |         |     | 0/1    | U/D              | 0/1 5 Semi F47 |
|     |                 | OCD    | 6 0/1     | U/D    | 0/1   |     |                     |             |         |     | OR 0/1 | U/D              | 0/1 6 Derating |
|     |                 |        | 7         |        |       |     |                     |             |         |     |        |                  | 7              |
|     |                 | UCD    | 0/1       | U/D    | 0/1   | OR  |                     |             |         |     | 0/1    | U/D              | 0/1 CTO        |
|     |                 |        | 8         |        |       |     |                     |             |         |     |        |                  | 0/1 8          |
|     |                 | OPD    | 0/1       | U/D    | 0/1   |     |                     | Error Queue |         |     | 0/1    | U/D              | CV             |
|     |                 | Local  | 9 0/1     | U/D    | 0/1   |     |                     |             |         |     | 0/1    | U/D              | 0/1 9 CC       |
|     |                 |        | 10        |        |       |     |                     |             | Error 1 |     |        |                  |                |
|     |                 | Remote | 0/1       | U/D    | 0/1   |     |                     |             |         |     | 0/1    | U/D              | 0/1 10 CP      |
|     |                 |        | 11        |        |       |     |                     | <>0         | ...     |     |        |                  | 11             |
|     | Output/Input on |        | 0/1       | U/D    | 0/1   |     |                     |             |         |     | 0/1    | U/D              | 0/1 CR         |
Function 12 0/1 U/D 0/1 Error 5 0/1 U/D 0/1 12 Source (=0)/Sink(=1)
|     |     | Power fail | 13 0/1 | U/D | 0/1 |     |     |     |     |                 |     |                 |     |
| --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- |
|     |     |            | 14     |     |     |     |     |     |     | STAT:OPER:EVEN? |     | STAT:OPER:COND? |     |
|     |     | MSP        | 0/1    | U/D | 0/1 |     |     |     |     |                 |     |                 |     |
STAT:OPER?
|     |     |     | STAT:QUES:COND? |     |     | STAT:QUES:EVEN? |     |     |     |     | STAT:OPER:ENAB <n> |     |     |
| --- | --- | --- | --------------- | --- | --- | --------------- | --- | --- | --- | --- | ------------------ | --- | --- |
STAT:OPER:ENAB?
|     |     |     | STAT:QUES:ENAB <n> |     |     | STAT:QUES? |     |     |                  |                  |        |     |     |
| --- | --- | --- | ------------------ | --- | --- | ---------- | --- | --- | ---------------- | ---------------- | ------ | --- | --- |
|     |     |     | STAT:QUES:ENAB?    |     |     |            |     |     |                  | Service Request  |        |     |     |
|     |     |     |                    |     |     |            |     | err | oper Status Byte |                  | Enable |     |     |
|     |     |     |                    |     |     |            |     |     | STB              |                  | SRE    |     |     |
0
|     |               |     |           | Second Questionable Status  |       |            |     |      | 0/1   |     | U/D  |     |     |
| --- | ------------- | --- | --------- | --------------------------- | ----- | ---------- | --- | ---- | ----- | --- | ---- | --- | --- |
|     |               |     |           | SEC QUES                    |       |            |     |      | 1 0   |     | 0    |     |     |
|     |               |     |           |                             |       |            |     |      | 2 0/1 |     | U/D  |     |     |
|     |               |     | CONDITION | ENABLE                      | EVENT |            |     |      | 3     |     |      |     |     |
|     |               |     |           |                             |       |            |     | ques | 0/1   |     | U/D  |     |     |
|     | OCP/OPP cause |     | 0 0/1     | U/D                         | 0/1   |            |     |      | 4 0   |     | 0 OR |     |     |
|     |               |     | 1         |                             |       |            |     |      | 5     |     |      |     |     |
|     |               |     | 0/1       | 0                           |       | 0 sec_ques |     |      | 0/1   |     | U/D  |     |     |
|     |               |     | 2         |                             |       |            |     |      | 6     |     |      |     |     |
|     |               | SF  | 0/1       | U/D                         | 0/1   |            |     |      | 00/1  |     | 0    |     |     |
|     |               |     | 3 0/1     | 0                           |       | 0          |     |      | 7 0/1 |     | U/D  |     |     |
4
|     |     |     | 0/1 | 0   |     | 0   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5
|     |                    |     | 0/1    | 0   |     | 0    |     |     | *STB? |                       | *SRE?    |     |     |
| --- | ------------------ | --- | ------ | --- | --- | ---- | --- | --- | ----- | --------------------- | -------- | --- | --- |
|     |                    |     | 6 0/1  | 0   |     | 0    |     |     |       |                       | *SRE <n> |     |     |
|     |                    |     | 7 0/1  | 0   |     | 0 OR |     |     |       |                       |          |     |     |
|     | 10 k series only   |     | 8      |     |     |      |     |     |       |                       |          |     |     |
|     | Nur 10000er Serien |     | 0/1    | 0   |     | 0    |     |     |       |                       |          |     |     |
|     |                    |     | 9 0/1  | 0   |     | 0    |     |     |       |                       |          |     |     |
|     |                    |     | 10 0/1 | 0   |     | 0    |     |     |       |                       |          |     |     |
|     |                    |     | 11     |     |     |      |     |     |       | Master Summery Status |          |     |     |
|     |                    |     | 0/1    | 0   |     | 0    |     |     |       |                       |          |     |     |
12
|     |     |                     | 0/1    | 0   |                     | 0   |     |     |     |     |     |     |     |
| --- | --- | ------------------- | ------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |                     | 13 0/1 | 0   |                     | 0   |     |     |     |     |     |     |     |
|     |     |                     | 14     |     |                     |     |     | esr |     |     |     |     |     |
|     |     |                     | 0/1    | 0   |                     | 0   |     |     |     |     |     |     |     |
|     |     | STAT:SEC:QUES:COND? |        |     | STAT:SEC:QUES:EVEN? |     |     |     |     |     |     |     |     |
STAT:SEC:QUES?
STAT:SEC:QUES:ENAB <n>
STAT:SEC:QUES:ENAB?
Event status
ESR
|                              |                     |                      | OPC | 0 0/1     | U/D |     |     |     |     |     |     |     |     |
| ---------------------------- | ------------------- | -------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OPC = OPeration Complete bit |                     |                      |     | 1         |     |     |     |     |     |     |     |     |     |
|                              |                     |                      |     | 0/1       |     | 0   |     |     |     |     |     |     |     |
| EXE= EXecution Error         |                     |                      | QYE | 2 0/1     | U/D |     |     |     |     |     |     |     |     |
| Q YE                         | =   Q u e r Y  E    | r r o r              |     |           |     |     |     |     |     |     |     |     |     |
|                              |                     |                      | D D | E 3 0 / 1 | U   | / D |     |     |     |     |     |     |     |
| C M                          | E =   C o M m       | a n d   E rr o r s   |     | 4         |     | OR  |     |     |     |     |     |     |     |
| D D                          | E =   D e v i c e   | D e p e n d   E rror | E   | XE 0 / 1  | U   | / D |     |     |     |     |     |     |     |
|                              |                     |                      | CME | 5 0/1     | U/D |     |     |     |     |     |     |     |     |
PON = Power On
|     |     |     |     | 6 0/1 |     | 0   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7
|     |     |     | PON | 0/1   | U/D  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | *ESR? | *ESE |     |     |     |     |     |     |     |     |
*ESE?
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 41
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Statusregistermodell (nur für Serie PS 2000 B TFT):
|     |                |           | Questionable Status  |       |     |                     |     |     |     | Operation Status |        |           |
| --- | -------------- | --------- | -------------------- | ----- | --- | ------------------- | --- | --- | --- | ---------------- | ------ | --------- |
|     |                |           | QUES                 |       |     |                     |     |     |     |                  | OPER   |           |
|     |                | CONDITION | ENABLE               | EVENT |     |                     |     |     |     | EVENT            | ENABLE | CONDITION |
|     | OVP (Output 1) | 0         | 0/1 U/D              | 0/1   |     | U = User defineable |     |     |     | 0                | 0      | 0/1 0     |
|     |                | 1         |                      |       |     | D = Is 1 by default |     |     |     |                  |        |           |
|     | OCP (Output 1) |           | 0/1 U/D              | 0/1   |     |                     |     |     |     | 0                | 0      | 0/1 1     |
|     |                | 2         |                      |       |     |                     |     |     |     |                  |        | 2         |
|     | OPP (Output 1) |           | 0/1 U/D              | 0/1   |     |                     |     |     |     | 0                | 0      | 0/1       |
|     | OT (Output 1)  | 3         | 0/1 U/D              | 0/1   |     |                     |     |     |     | 0                | 0      | 0/1 3     |
|     | OVP (Output 2) | 4         | 0/1 U/D              | 0/1   |     |                     |     |     |     | 0                | 0      | 0/1 4     |
5
|     | OCP (Output 2) |     | 0/1 U/D | 0/1 |     |     |             |     |     | 0    | 0   | 0/1 5               |
| --- | -------------- | --- | ------- | --- | --- | --- | ----------- | --- | --- | ---- | --- | ------------------- |
|     |                | 6   |         |     |     |     |             |     |     |      |     | 6                   |
|     | OPP (Output 2) |     | 0/1 U/D | 0/1 |     |     |             |     |     | OR 0 | 0   | 0/1                 |
|     | OT (Output 2)  | 7   | 0/1 U/D | 0/1 | OR  |     |             |     |     | 0    | 0   | 0/1 7               |
|     |                | 8   | 0/1 0   |     | 0   |     | Error Queue |     |     | 0/1  | U/D | 0/1 8 CV (Output 1) |
9
|     |                   |     | 0/1 0   |     | 0   |     |     |         |     | 0/1 | U/D | 0/1 9 CC (Output 1) |
| --- | ----------------- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- | --- | ------------------- |
|     |                   | 10  |         |     |     |     |     | Error 1 |     |     |     | 10                  |
|     | Remote (Output 1) |     | 0/1 U/D | 0/1 |     |     |     |         |     | 0/1 | U/D | 0/1 CV (Output 2)   |
Output on (Output 1) 11 0/1 U/D 0/1 <>0 ... 0/1 U/D 0/1 11 CC (Output 2)
Error 5
|     | Tracking (only Triple) | 12  | 0/1 U/D | 0/1 |     |     |     |     |     | 0/1 | U/D | 0/1 12 |
| --- | ---------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
13
|     | Remote (Output 2) |     | 0/1 U/D | 0/1 |     |     |     |     |        |                 |     |                     |
| --- | ----------------- | --- | ------- | --- | --- | --- | --- | --- | ------ | --------------- | --- | ------------------- |
|     |                   | 14  |         |     |     |     |     |     | STAT:O | P ER : EV E N ? |     | ST A T :O PER:COND? |
Output on (Output 2) 0/1 U/D 0/1 STATUS ST A T: O P E R ?STAT:OPER:EN
A B  < n>
|     |     | STAT:QUES:COND? |     |     | STAT:QUES:EVEN? |     |     | STB |     | STAT:OPER:ENAB? |     |     |
| --- | --- | --------------- | --- | --- | --------------- | --- | --- | --- | --- | --------------- | --- | --- |
0
|     |     |     | STAT:QUES:ENAB <n> |     | STAT:QUES? |     |     | 0   |     |     |     |     |
| --- | --- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | STAT:QUES:ENAB?    |     |            |     |     | 1 0 |     |     |     |     |
err
|     |     |     | Event Status  |     |     |     |     | 2 0/1 |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
3
|     |     |     |     | ESR |     |     | ques | 0/1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
4
|                              |                              |              | 0             |     |     |     |     | 0         |     |     |     |     |
| ---------------------------- | ---------------------------- | ------------ | ------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|                              |                              |              | OPC 0 / 1     | U   | /D  | esr |     | 5 0 /1    |     |     |     |     |
|                              |                              |              | 1 0 / 1       |     | 0   |     |     |           |     |     |     |     |
| OPC = OPeration Complete bit |                              |              |               |     |     |     |     | 6 0       |     |     |     |     |
| E X E =                      |   E X e c u t i o n   E rror |              | Q YE 2 0 / 1  | U   | / D |     |     |           |     |     |     |     |
|                              |                              |              | 3             |     |     |     |     | 7 0/1     |     |     |     |     |
| Q Y E                        | =   Q u e r Y   E r r o r    |              | D D E 0 / 1   | U   | / D |     |     |           |     |     |     |     |
| C M E                        | =   C o M m a n d            | E rr o r s   | 4             |     | OR  |     |     |           |     |     |     |     |
|                              |                              |              | E X E 0 / 1   | U   | / D |     |     | * S T B ? |     |     |     |     |
| D DE                         | =   D e v ic e  D e p e      | n d   E rror | C M E 5 0 / 1 | U   | / D |     |     |           |     |     |     |     |
|                              |                              |              |               |     |     |     |     | o p e r   |     |     |     |     |
|                              |                              |              | 6 0/1         |     | 0   |     |     |           |     |     |     |     |
7
|     |     |     | 0/1 |     | 0   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
*ESR? *ESE
*ESE?
Die im CONDition-Register von OPERation und QUEStionable signalisierten Bits sind mit den Statusbits in den
ModBus-Registern 505 bzw. 511 verknüpft. Da die obere der beiden Übersichten für viele Serien gilt und nicht alle
jedes Bit unterstützen, gilt die Regel: wenn irgendein Statusbit im Registermodell nicht auch in der jeweils zum
Gerät	gehörenden	ModBus-Registerliste	aufgeführt	ist,	wird	es	vom	Gerät	nicht	unterstützt.
Gerätealarme wie OVP werden über die Subregister :CONDition und :EVENT erfaßt und müs-
sen nach dem Auslesen von :CONDition noch separat gelöscht werden. Das geschieht durch
Abfrage mit SYST:ERR? oder SYST:ERR:ALL?, was als Bestätigung der Kenntnisnahme des
Alarms gilt und das jeweilige Bit in :CONDition löscht, sofern der Status nicht immer noch
anliegt. Bestätigte Alarme können später nur als Alarmzähler vom Gerät abgefragt werden
(wo unterstützt, erfordert ggf. ein Firmwareupdate). Daher sollte die Erfassung von Alarmen
regelmäßig erfolgen (intervallartiges Polling) und STAT:QUES? stets vor einem SYST:ERR?
abgefragt werden.
Nur für 60 V-Modelle (in bestimmten Serien verfügbar): der bei diesen Modellen zusätzlich
vorhandene Alarm "Safety OVP" (SOVP) wird nicht als separates Bit in das Statusregister gege-
ben, sondern er wird bei Auftreten als gleichzeitige Signalisierung von Alarm PF (Questionable
Status, Bit 13) und Alarm OVP (Questionable Status, Bit 0) abgebildet. Zusätzlich wird der nicht
löschbare Fehler -999 in die Error Queue gelegt. Ein SOVP-Alarm kann nur durch Aus- und
Wiedereinschalten des Gerätes gelöscht werden.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 42
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.2.1 STATus:QUEStionable?
Liest das Questionable Status EVENT oder CONDITION Register aus. Zurückgegeben wird ein dezimaler 16 bit-
Wert, dessen einzelne Bits Gerätezustände gemäß des Registermodells in 5.4.2 abbilden.
Abfrageform 1: STATus:QUEStionable:CONDition?
Abfrageform 2: STATus:QUEStionable:EVENt?
Abfrageform 3: STATus:QUEStionable?
Beispiele:
STAT:QUES? --> 3072 Liest das Event-Register. Der Wert gibt an, daß Bits 10 und 11 gesetzt sind und
gemäß Registermodell sagt das aus, daß Fernsteuerung aktiv ist, sowie der Aus-
gang/Eingang eingeschaltet ist.
STAT:QUES:COND? Liest das Condition-Register des Questionable Status Registers aus. Der Wert
enthält den aktuellen Zustand diverser Status-Bits
5.4.2.2 STATus:QUEStionable:ENABle˽<NR1>
Setzt oder liest das Enable-Register des Questionable Status Registers. Das Enable-Register ist ein Filter, eine
Freigabe für einzelne Bits, ob ein Ereignis im Questionable im Statusbyte STB gemeldet wird. Standardmäßig sind
alle Bits des Filters auf 1 gesetzt. Möchten Sie ein oder mehrere Bits herausfiltern, brauchen Sie nur die Wertigkeit
der übrigbleibenden Bits addieren (siehe Registermodell) und an das Enable-Register schicken.
Abfrageform: STATus:QUEStionable:ENABle?
Wertebereich: 0...32767 (Standardwert: 0)
Beispiel:
STAT:QUES:ENAB˽3072 Setzt das Enable-Register des Questionable Status Registers auf 3072 und gibt
die Bits „OVP“, „OT“, „Remote“ und „Input/Output on“ frei zur Meldung an das STB.
5.4.2.3 STATus:OPERation?
Liest das Operation Status EVENT oder CONDITION Register aus. Zurückgegeben wird ein dezimaler 16 bit-Wert,
dessen einzelne Bits Gerätezustände gemäß des Registermodells in 5.4.2 angeben.
Abfrageform 1: STATus:OPERation[:CONDition?
Abfrageform 2: STATus:OPERation:EVENt?
Abfrageform 3: STATus:OPERation?
Beispiele:
STAT:OPER? --> 256 Fragt das Operation Register ab (identisch mit :EVENt?). Eine mögliche Antwort
wäre 256, welche angibt, daß Bit 8 gesetzt ist, welches nach dem Registermodell
mit dem Zustand „CV“ meldet, daß Konstantspannungsregelung aktiv ist.
STAT:OPER:COND? Liest das Condition-Register des Operation Status Registers aus.
5.4.2.4 STATus:OPERation:ENABle˽<NR1>
Setzt oder liest das Enable-Register des Questionable Status Registers. Das Enable-Register ist ein Filter, eine
Freigabe für einzelne Bits, ob ein Ereignis im Operation Status Register im Statusbyte STB gemeldet wird. Stan-
dardmäßig sind alle Bits des Filters auf 1 gesetzt. Möchten Sie ein oder mehrere Bits herausfiltern, brauchen Sie
nur die Wertigkeit der übrigbleibenden Bits addieren (siehe Registermodell) und an das Enable-Register schicken.
Abfrageform: STATus:OPERation:ENABle?
Wertebereich: 0, 256...3840
Beispiel:
STAT:OPER:ENAB˽1792 Setzt das Enable-Register des Operation Registers auf 1792 und gibt die Bits
„CV“, „CC“ und „CP“ frei zur Meldung an das STAT:OPER:EVENT und das STB.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 43
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.2.5 Weitere Statusregister
Die 10000 Serien erfordern zusätzliche Alarmbits, die in einem zweiten "questionable" Statusregister verbunden
sind. Siehe Registermodell oben. Zu diesem Register gibt es separate Befehle, die in ihrer Funktion den in 5.4.2.1
bis 5.4.2.4 beschriebenen entsprechen. Daher dort bitte für Einzelheiten nachlesen. Das bedeutet auch, daß diese
Befehle zunächst auch nur von diesen Serien unterstützt werden:
STATus:SECond:QUEStionable?
STATus:SECond:QUEStionable:ENABle?
STATus:SECond:QUEStionable:ENABle˽<NR1>
STATus:SECond:QUEStionable:CONDition?
STATus:SECond:QUEStionable:EVENt?
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 44
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.3 Sollwertbefehle
Alle Werte, die per einzelnem Befehl setzbar sind und während Fernsteuerung an das Gerät
gesendet werden, sind nicht nur durch die Nennwerte des Gerätes begrenzt, sondern noch
zusätzlich durch die an der Bedieneinheit oder per digitaler Fernsteuerung justierbaren Ein-
stellgrenzen!
5.4.3.1 [SOURce:]VOLTage˽<NR2>
Setzt die Eingangs- bzw. Ausgangsspannungsgrenze des Gerätes innerhalb eines minimalen und eines maxima-
len Einstellwertes bzw. fragt den Wert ab. Hat ein Gerät variable Einstellgrenzen („Limits“) bestimmen diese den
Einstellbereich, der ansonsten als 0...102% Nennwert definiert ist. Das gilt ebenso für die alternativ benutzbaren
Parameter MIN oder MAX, die direkt auf den MINimalen oder MAXimalen Einstellwert setzen.
Abfrageform: [SOURce:]VOLTage?
Wertebereich: <NRf> = 0...1,02 * Nennspannung laut techn. Daten
Beispiele:
VOLT˽12 Absolute Kurzform. Setzt 12 V.
SOUR:VOLTAGE˽24.5V Gemischte Form kurz/lang, mit Einheit. Setzt 24,5 V, sofern nicht durch eine Ein-
stellgrenze („Limits“), wo vorhanden, anderweitig begrenzt.
SOURCE:VOLTAGE˽MIN Setzt die Spannung auf das definierte Minimum, normalerweise 0 V.
5.4.3.2 [SOURce:]CURRent˽<NR2>
Setzt die Eingangs- bzw. Ausgangsstromgrenze des Gerätes innerhalb eines minimalen und eines maximalen Ein-
stellwertes bzw. fragt den Wert ab. Bei bidirektionalen Netzgeräten ist der Befehl dem Quelle-Betrieb zugeordnet.
Hat ein Gerät variable Einstellgrenzen („Limits“) bestimmen diese den Einstellbereich, der ansonsten als 0...102%
Nennwert definiert ist. Das gilt ebenso für die alternativ benutzbaren Parameter MIN oder MAX, die direkt auf den
MINimalen oder MAXimalen Einstellwert setzen.
Abfrageform: [SOURce:]CURRent?
Wertebereich: <NRf> = 0...1,02 * Nennstrom laut techn. Daten
Beispiele:
CURR˽170 Absolute Kurzform. Setzt 170 A.
SOUR:CURRENt˽45.3A Gemischte Form kurz/lang, mit Einheit. Setzt 45,3 A, sofern nicht durch eine Ein-
stellgrenze („Limits“), wo vorhanden, anderweitig begrenzt.
SOURCE:CURRENT˽MAX Setzt den Strom auf das definierte Maximum, also auf 102% vom Stromnennwert
des Gerätes oder auf den Wert der zugehörige Einstellgrenze „I-max“, sofern diese
für das Gerät existiert (siehe 5.4.8).
5.4.3.3 [SOURce:]POWer˽<NR3>
Nicht verfügbar für Serie PSB 2000 B TFT. Diese hat eine indirekte Leistungsbegrenzung.
Setzt die Eingangs- bzw. Ausgangsleistungs-Grenze des Gerätes innerhalb eines minimalen und eines maximalen
Einstellwertes bzw. fragt den Wert ab. Bei bidirektionalen Netzgeräten ist der Befehl dem Quelle-Betrieb zugeordnet.
Hat ein Gerät variable Einstellgrenzen („Limits“) bestimmen diese den Einstellbereich, der ansonsten als 0...102%
Nennwert definiert ist. Das gilt ebenso für die alternativ benutzbaren Parameter MIN oder MAX, die direkt auf den
MINimalen oder MAXimalen Einstellwert setzen.
Abfrageform: [SOURce:]POWer?
Wertebereich: <NRf> = 0...1,02 * Nennleistung laut techn. Daten
Beispiele:
POW˽3000 Absolute Kurzform. Setzt 3000 W.
SOUR:POWER˽3.5kW Gemischte Form kurz/lang, mit Einheit und Größenordnung Kilo. Setzt 3,5 kW,
sofern nicht durch eine Einstellgrenze („Limits“), wo vorhanden, anderweitig be-
grenzt.
SOURCE:POWER˽MIN Setzt die Leistung auf das definierte Minimum, hier 0 W.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 45
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 5.4.3.4  | [SOURce:]RESistance˽<NR2> |     |     |     |     |     |     |     |     |
| -------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|  ─ | ─  | ─ ─ |  ─ |   |  ─ | ─ ─ | ─  |  ─ |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Setzt	bei	elektronischen	Lasten	den	Eingangswiderstand	in	Ohm	innerhalb	des	definierten	Minimalwertes	des
Modells und einem einstellbaren Maximalwert, genannt „Limit“. Bei normalen Netzgeräten bzw. bidirektionalen
Netzgeräten im Quelle-Betrieb wird bei aktiviertem „R-Modus“ ein interner Widerstand simuliert, indem die
Ausgangsspannung um den Betrag von der eingestellten abweicht, der sich rechnerisch aus dem gemessenen
Ausgangsstrom	und	dem	gewünschten	Widerstand	ergibt,	sofern	das	in	der	jeweiligen	Situation	rechnerisch	möglich
ist.	Das	Setzen	des	Widerstandswertes	an	sich	ist	bei	allen	Geräten	jedoch	identisch.	Alternativ	können	auch	hier
die Parameter MIN und MAX verwendet werden, um den Widerstandswert schnell auf das einstellbare MINimum
oder MAXimum zu setzen. Bei bidirektionalen Netzgeräten ist der Befehl dem Quelle-Betrieb zugeordnet.
| Abfrageform:  |     | [SOURce:]RESistance? |     |     |     |     |     |     |     |
| ------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
Wertebereich:  <NRf> = Min. Widerstand...max. Widerstand, laut technischen Daten
Beispiele:
RES?  Absolute Kurzform. Fragt den momentan gesetzten Widerstandswert ab.
SOUR:RESISTANCE˽10	 Gemischte	Form	kurz/lang.	Setzt	10	Ω,	sofern	nicht	durch	eine	Einstellgrenze
(„Limits“), wo vorhanden, anderweitig begrenzt.
SOURCE:RES˽MIN	 Setzt	den	Widerstand	auf	den	für	das	Gerät	definierten	Minimalwert.
| 5.4.3.5  | SINK:CURRent˽<NR2> |     |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|     |     |     |     |     |   |     |     |   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ─ ─ | ─ ─ | ─ ─ | ─ ─ | ─ ─ |     | ─ ─ | ─ ─ |     | ─   |
Dieser Befehl wird nur von den bidirektionalen Geräten der PSB-Serien unterstützt und setzt den Stromsollwert
für den Senke-Betrieb, der getrennt vom Stromsollwert des Quelle-Betriebs (siehe 5.4.3.2) einstellbar ist.
Gegenüber	dem	„normalen“	CURRent-Befehl	ist	hier	das	Hauptsystem	SINK	nicht	optional,	sonst	könnte	das
Gerät nicht unterscheiden. Es gelten aber auch hier genauso Einstellgrenzen. Ebenso wie es einen separaten
Stromsollwert für den Senke-Betrieb gibt, gibt es auch die separaten Einstellgrenzen „Senke: I-max“ und „Senke:
I-min“,	wie	am	Bedienteil	einstellbar,	sowie	die	dazu	gehörigen	SCPI-Befehle	(siehe	5.4.8).	Alternativ	können	auch
hier die Parameter MIN und MAX verwendet werden, um den Strom schnell auf das einstellbare MINimum oder
MAXimum zu setzen.
| Abfrageform:   |     | SINK:CURRent?         |     |     |     |     |     |     |     |
| -------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
| Wertebereich:  |     | <NRf> = I-min...I-max |     |     |     |     |     |     |     |
Beispiele:
SINK:CURR˽120	 Setzt	den	Stromsollwert	(oder	auch	Stromobergrenze)	für	den	Senke-Betrieb	eines
PSB auf 120 A, sofern die Einstellgrenzen dies zulassen. Der Sollwert kann erst
wirksam werden, wenn das Gerät tatsächlich in den Senke-Betrieb geht.
| 5.4.3.6  | SINK:POWer˽<NR3> |     |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
| ─ ─ | ─ ─ | ─ ─ | ─ ─ | ─ ─ |   | ─ ─ | ─ ─ |   | ─   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dieser Befehl wird nur von den bidirektionalen Netzgeräten unterstützt und setzt den Leistungswert für den Senke-
Betrieb, der getrennt vom Leistungssollwert des Quelle-Betriebs (siehe 5.4.3.3) einstellbar ist.
Gegenüber	dem	„normalen“	POWer-Befehl	ist	hier	das	Hauptsystem	SINK	nicht	optional,	sonst	könnte	das	Gerät
nicht unterscheiden. Es gelten aber auch hier genauso Einstellgrenzen. Ebenso wie es einen separaten Leistungs-
sollwert für den Senke-Betrieb gibt, gibt es auch die separate Einstellgrenze „Senke: P-max“, wie am Bedienteil
einstellbar,	sowie	den	dazugehörigen	SCPI-Befehl	(siehe	5.4.8).	Alternativ	können	auch	hier	die	Parameter	MIN
und MAX verwendet werden, um die Leistung schnell auf das einstellbare MINimum oder MAXimum zu setzen.
| Abfrageform:   |     | SINK:POWer?       |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| Wertebereich:  |     | <NRf> = 0...P-max |     |     |     |     |     |     |     |
Beispiele:
SINK:POW˽4500	 Setzt	den	Leistungssollwert	(oder	auch	Leistungsobergrenze)	für	den	Senke-
Betrieb des PSB 9000 auf 4500 W, sofern die Einstellgrenze P-max dies zuläßt.
Der Sollwert kann erst wirksam werden, wenn das Gerät tatsächlich in den Senke-
Betrieb geht.
| SINK:POWER˽MIN	 |     | Setzt	die	Leistung	auf	0	W. |     |     |     |     |     |     |     |
| --------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 46
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.3.7 SINK:RESistance˽<NR2>
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─ ─ ─   ─
Dieser Befehl wird nur von den bidirektionalen Netzgeräten unterstützt und setzt den Widerstandssollwert für den
Senke-Betrieb, der getrennt vom Widerstandssollwert des Quelle-Betriebs (siehe 5.4.3.4) einstellbar ist.
Gegenüber dem „normalen“ RESistance-Befehl ist hier das Hauptsystem SINK nicht optional, sonst könnte das
Gerät nicht unterscheiden. Es gelten aber auch hier genauso Einstellgrenzen. Ebenso wie es einen separaten
Widerstandssollwert für den Senke-Betrieb gibt, gibt es auch die separate Einstellgrenze „Senke: R-max“, wie
am Bedienteil einstellbar, sowie den dazugehörigen SCPI-Befehl (siehe 5.4.8). Alternativ können auch hier die
Parameter MIN und MAX verwendet werden, um den Widerstand schnell auf das einstellbare MINimum oder
MAXimum zu setzen.
Abfrageform: SINK:RESistance?
Wertebereich: <NRf> = min. einstellbarer Widerstand (siehe techn. Daten)...R-max
Beispiele:
SINK:RESISTANCE˽MIN Setzt den Widerstandssollwert für den Senke-Betrieb auf das durch die technischen
Daten des jeweiligen Gerätemodells definierte Minimum. Die Nennwerte des
Gerätes sind mit weiteren Befehlen abfragbar.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 47
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.4 Meßbefehle
Meßbefehle geben die vom Gerät ermittelten (U, I) bzw. berechneten (P, R) Istwerte zurück, also die tatsächlichen
Werte am DC-Ausgang bzw. DC-Eingang des Gerätes. Die Werte werden asynchron ermittelt. Das heißt, die Abfra-
ge löst keinen Meßforgang aus. Istwerte müssen nicht zwangsweise mit den gewünschten (Soll)Werten identisch
sein und geben zu jedem Abfragezeitpunkt den zuletzt ermittelten Zustand am DC-Anschluß des Gerätes wieder.
Die Meßwerte werden periodisch erfaßt.
5.4.4.1 MEASure:[SCALar:]VOLTage[:DC]?
Fragt beim Gerät an, den zuletzt erfaßten Meßwert der DC-Eingangs- bzw. DC-Ausgangsspannung des Gerätes
in Volt wiederzugeben.
Beispiel:
MEAS:VOLT? Absolute Kurzform. Die Istspannung wird abgefragt. Als Antwort, die sofort vom
Gerät kommen sollte, wird ein Wert zwischen 0% und max. 125% Spannungs-
nennwert des Gerätes zurückgegeben, z. B. „43.50V“. Die Anzahl der Nachkom-
mastellen ist identisch mit denen in der Anzeige des Gerätes und variiert zwischen
Gerätemodellen.
5.4.4.2 MEASure:[SCALar:]CURRent[:DC]?
Gibt den zuletzt erfaßten Meßwert des DC-Eingangs- bzw. DC-Ausgangsstroms des Gerätes in Ampere wieder.
Bei den Geräten der Serien PSB und PSBE 9000 der zurückgegebene Istwert zum Quelle-
oder Senkebetrieb gehören. Hat dieser ein negatives Vorzeichen, gehört der Istwert aktuell
zum Senke-Betrieb.
Beispiel:
MEASURE:CURRENT? Der Iststrom wird abgefragt. Als Antwort, die sofort vom Gerät kommen sollte, wird
ein Wert zwischen 0% und max. 125% Strom-Nennwert des Gerätes zurückge-
geben, z. B. „100.1A“. Die Anzahl der Nachkommastellen ist identisch mit denen
in der Anzeige des Gerätes und variiert zwischen Gerätemodellen.
5.4.4.3 MEASure:[SCALar:]POWer[:DC]?
Gibt den zuletzt aus Istspannung und Iststrom berechneten Istwert der DC-Eingangs- bzw. DC-Ausgangsleistung
des Gerätes in Watt wieder.
Bei den Geräten der Serien PSB und PSBE der zurückgegebene Istwert zum Quelle- oder
Senkebetrieb gehören. Hat dieser ein negatives Vorzeichen, gehört der Istwert aktuell zum
Senke-Betrieb.
Beispiel:
MEAS:POW? Absolute Kurzform. Die Istleistung, also die aufgenommene (E-Last) bzw. abge-
gebene (Netzgerät), Leistung wird abgefragt. Als Antwort, die sofort vom Gerät
kommen sollte, wird ein Wert zwischen 0% und max. 125% Leistungsnennwert
des Gerätes zurückgegeben, z. B. „2534W“. Unabhängig von der Darstellung in
der Anzeige des Gerätes kommt dieser Wert immer in Watt.
5.4.4.4 MEASure:[SCALar:]ARRay?
Gibt alle drei zuletzt erfaßten bzw. berechneten Istwerte in der Reihenfolge Spannung, Strom, Leistung wieder,
mit Kommas getrennt und mit Einheit und eventuell Größenordnung. Dieser Befehl vereint die drei einzelnen
Meßbefehle.
Bei den Geräten der Serien PSB und PSBE können die zurückgegebenen Istwerte zum Quel-
le- oder Senkebetrieb gehören. Hat ein Wert ein negatives Vorzeichen, gehört er aktuell zum
Senke-Betrieb.
Beispiel:
MEAS:ARR? Absolute Kurzform. Als Antwort, die sofort vom Gerät kommen sollte, werden drei
Werte zwischen 0 und 125% Nennwert des Gerätes zurückgegeben, z. B. „12.5V,
33.3A, 420W“
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 48
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 5.4.5  | Zustandsbefehle |     |     |     |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
Zustandsbefehle verändern den Zustand des Gerätes im Sinne von Fernsteuerung ein/aus oder DC-Ausgang/
DC-Eingang ein/aus bzw. fragen den Zustand ab.
| 5.4.5.1  | SYSTem:LOCK˽<B0> |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Mit dem Befehl wird die Fernsteuerung des Gerätes über die momentan verwendete digitale Schnittstelle übernom-
men, sofern die Übernahme zu dem Zeitpunkt zulässig ist. Fernsteuerung des Gerätes muß generell immer dann
zuerst aktiviert werden, bevor man etwas setzen will (Sollwerte, Zustand). Dabei kann immer nur die Schnittstelle
steuernd auf das Gerät zugreifen, über welche die Fernsteuerung aktiviert wurde.
Die Aktivierung der Fernsteuerung kann durch das Gerät blockiert werden. Dies wird durch einen Fehler mitgeteilt,
der	im	SCPI-Fehlerpuffer	hinterlegt	wird,	welcher	mit	dem	Fehlerabfragebefehl	(siehe	„5.4.5.4. SYSTem:ERRor?“)
auslesbar ist.
| Abfrageform:               |     | SYSTem:LOCK:OWNer?    |     |     |     |     |     |     |
| -------------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| Wertebereich für Setzen:   |     | ON, OFF               |     |     |     |     |     |     |
| Wertebereich für Abfrage:  |     | {REMOTE, NONE, LOCAL} |     |     |     |     |     |     |
Beispiele:
SYST:LOCK˽ON  Absolute Kurzform. Der Befehl schaltet das Gerät auf Fernsteuerung um. Das
Gerät sollte dies anzeigen, in Form eines Statustextes in der Anzeige oder mit
einer LED.
SYSTEM:LOCK:OWNER?	 Abfrage	des	Zugriffbesitzers.	Kann	verwendet	werden,	um	festzustellen,	ob
Fernsteuerung überhaupt übernommen werden kann bzw. nach dem Senden des
Befehls, ob sich der Zustand entsprechend geändert hat. Die Anfrage kann drei
verschiedene Zustände zurückgeben:
  REMOTE = Gerät ist in Fernsteuerung durch irgendeine Schnittstelle
  NONE = Das Gerät ist für die Übernahme der Fernsteuerung verfügbar
  LOCAL = Fernsteuerung ist gesperrt, üblicherweise am Gerät selbst
| 5.4.5.2  | INPut˽<B0> |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|   | ─ ─ | ─ ─ (1  | ─ ─ |  ─ | ─ ─ | ─ ─ | ─ ─ | ─  |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Schaltet bei Geräten mit einem DC-Eingang, hier: elektronische Lasten, den Eingang ein oder aus bzw. kann der
Zustand dessen abgefragt werden.
| Abfrageform:   |     | INPut?  |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| Wertebereich:  |     | ON, OFF |     |     |     |     |     |     |
Beispiele:
INP˽ON	 Absolute	Kurzform.	Schaltet	den	DC-Eingang	ein,	sofern	Fernsteuerung	aktiv
INPUT?  Abfrage des Zustandes des DC-Eingangs, zurückgegeben mit ON oder OFF.
| 5.4.5.3  | OUTPut˽<B0> |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
| ─ ─ |   |   (2  |   | ─  |   |  ─ |   |  ─ |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Schaltet bei Geräten mit einem DC-Ausgang (hier: Netzgeräte) und bidirektionalen Geräte, welche auch als Netz-
geräte betrachtet werden, den Ausgang ein oder aus bzw. kann dessen Zustand abgefragt werden.
| Abfrageform:   |     | OUTPut? |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| Wertebereich:  |     | ON, OFF |     |     |     |     |     |     |
Beispiele:
OUTP˽ON	 Absolute	Kurzform.	Schaltet	den	DC-Ausgang	ein,	sofern	Fernsteuerung	aktiv
OUTPUT?  Abfrage des Zustandes des DC-Ausgangs, zurückgegeben mit ON oder OFF.
1)  Gilt nur für EL 9000 DT
2)  Gilt nur für PSI 9000 DT
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 49
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.5.4 SYSTem:ERRor?
Der Befehl dient zum Auslesen einzelner oder aller Fehler, die sich im SCPI-Fehlerpuffer des Gerätes befinden
können. Er kann nur Fehler im Zusammenhang mit der Syntax der SCPI-Befehle bzw. Zugriffsfehler enthalten,
jedoch keine Gerätealarme mit Ausnahme des SOVP (siehe auch „5.2.5. Kommunikationsfehler“). Gerätealarme
können über Bits in den Statusregistern (OPER, QUES, siehe „5.4.2. Statusregister“) abgefragt werden.
Die Anzahl der Fehler im SCPI-Fehlerpuffer kann nicht ausgelesen werden. Um sicherzugehen könnte man daher
immer alle Fehler abfragen. Nach der Abfrage eines Fehlers wird dieser aus dem Fehlerpuffer gelöscht, bei Abfrage
aller Fehler geschieht dies ebenso für alle.
Der Fehlerpuffer ist vom Typ FIFO (first in, first out). Das bedeutet, der zuerst aufgetretene Fehler wird bei Abfrage
auch zuerst ausgegeben.
Abfrageform 1: SYSTem:ERRor? Fragt den zuletzt aufgetretenen Fehler ab
Abfrageform 2: SYSTem:ERRor:NEXT? Fragt den zuletzt aufgetretenen Fehler ab
Abfrageform 3: SYSTem:ERRor:ALL? Fragt alle im Fehlerspeicher vorhandenen Fehler
ab (bis zu 5)
Beispiel:
SYST:ERR:NEXT? Absolute Kurzform. Auf diese Abfrage antwortet das Gerät mit einem String, der
als erstes einen Fehlercode laut Fehlercodeliste und als zweites eine Fehlerbe-
schreibung enthält, z. B.: 0,“No error“. Diese Antwort kommt immer dann, wenn
kein Fehler (mehr) vorliegt.
SYSTEM:ERROR:ALL? Auf diese Abfrage antwortet das Gerät mit bis zu 5 verketteten Fehlerstrings,
voneinander mit Komma+Leerzeichen getrennt.
Die Abfrage von Fehlern über SYST:ERR? löscht auch Gerätealarme aus dem QUEStionable
Statusregister (siehe „5.4.2. Statusregister“), sofern ein durch das Register angezeigter Alarm
nicht mehr vorhanden ist. Das wird als Bestätigung der Kenntnisnahme des Alarms gewertet.
So bestätigte Alarme können über das Register nachträglich nicht mehr erfaßt werden.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 50
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.6 Befehle für Schutzfunktionen
Das Gerät bietet eine Reihe von Gerätealarmen, die teils zum Selbstschutz, teils zum Schutz des angeschlosse-
nen Verbrauchers bzw. der angeschlossenen Quelle dienen. Weiterhin gibt es einige Überwachungsfunktionen,
die Eingangs- bzw. Ausgangswerte wie Spannung, Strom oder Leistung auf einstellbare Grenzen hin überwachen
und dann vom Anwender konfigurierbare Aktionen auslösen können, wie ein akustisches Alarmsignal oder Ab-
schalten des DC-Eingangs bzw. DC-Ausgangs. Die entsprechenden Funktionen können natürlich auch am Gerät
im Benutzerprofil konfiguriert werden.
5.4.6.1 [SOURce:]VOLTage:PROTection[:LEVel]˽<NR2>
Dieser Befehl gehört zum am Gerät einstellbaren Wert „OVP“ (Überspannungsschutz). Er ist einstellbar zwischen
0 und 110% der Maximalspannung des Gerätes, sowie bei allen EL 9000-Serien zwischen 0 und 103%, ggf. die
technischen Daten im Gerätehandbuch einsehen. Der Wert definiert eine Schwelle, an der das Gerät den DC-
Eingang bzw. DC-Ausgang ausschaltet. Bei Quellen, also Netzgeräten, dient dies in erster Linie zum Schutz der
Anwendung vor zu hoher Spannung, die durch ungewolltes Verstellen bzw. einen Defekt der Spannungsquelle
auftreten kann.
Abfrageformat: [SOURce:]VOLTage:PROTection[:LEVel]?
Wertebereich: 0...1,1 * oder 1,03 * Nennspannung des Gerätes
Beispiele:
VOLT:PROT˽88 Absolute Kurzform. Setzt die „OVP-Schwelle“ auf 88 V. Bei einem 80 V-Modell
(außer EL 9000 Serien) sind das 110% der Maximalspannung, also der maximale
OVP-Wert.
5.4.6.2 [SOURce:]CURRent:PROTection[:LEVel]˽<NR2>
Dieser Befehl gehört zum am Gerät einstellbaren Wert „OCP“ (Überstromschutz). Einstellbar zwischen 0 und
110% des Maximaleingangsstromes bzw. -ausgangsstromes des Gerätes. Der Wert definiert eine Schwelle, an
der das Gerät den DC-Eingang bzw. DC-Ausgang ausschaltet. Bei Senken, wie z. B. elektronischen Lasten,
dient dies in erster Linie zum Schutz der Anwendung vor zu hoher Stromentnahme, welche die Quelle eventuell
durch Überbelastung beschädigen könnte. Wird die Schwelle erreicht, schaltet das Gerät den DC-Eingang bzw.
DC-Ausgang aus. Sollte der Maximalstrom (Isoll) geringer eingestellt sein und den Strom des Gerätes begrenzen,
ist die Schutzfunktion unwirksam. Bei identischen Einstellwerten von Sollwert und OCP hat die Schwelle Priorität.
D. h., die OCP-Schutzfunktion schaltet dann ab, anstatt daß der Strom nur begrenzt wird.
Abfrageformat: [SOURce:]CURRent:PROTection[:LEVel]?
Wertebereich: 0...1,1*Nennstrom des Gerätes
Beispiele:
CURR:PROT˽100 Absolute Kurzform. Setzt die „OCP-Schwelle“ auf 100 A.
5.4.6.3 [SOURce:]POWer:PROTection[:LEVel]˽<NR3>
Dieser Befehl gehört zum am Gerät einstellbaren Wert „OPP“ (Überleistungsschutz). Einstellbar zwischen 0 und
110% der Maximaleingangsleistung bzw. -ausgangsleistung des Gerätes. Der Wert definiert eine Schwelle, an
der das Gerät den DC-Eingang bzw. DC-Ausgang ausschaltet. Diese Funktion soll helfen, eine Quelle oder einen
Verbraucher nicht über eine gewisse Leistung hin zu belasten. Wird die Schwelle erreicht, schaltet das Gerät den
DC-Eingang bzw. DC-Ausgang aus. Sollte die Maximalleistung (Psoll) geringer eingestellt sein und die Leistung
des Gerätes begrenzen, ist die Schutzfunktion unwirksam. Bei identischen Einstellwerten von Sollwert und OPP hat
die Schwelle Priorität. D. h., die OPP-Schutzfunktion schaltet dann ab, anstatt daß die Leistung nur begrenzt wird.
Abfrageformat: [SOURce:]POWer:PROTection[:LEVel]?
Wertebereich: 0...1,1*Nennleistung des Gerätes
Beispiele:
POW:PROT˽1.5kW Absolute Kurzform. Setzt die „OPP-Schwelle“ auf 1,5 kW.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 51
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 5.4.6.4  | SINK:CURRent:PROTection[:LEVel]˽<NR2> |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
| ─ ─ | ─ ─ | ─ ─ | ─ ─ | ─ ─ |   | ─ ─ | ─ ─ |   | ─   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dieser Befehl wird nur von den bidirektionalen Netzgeräten unterstützt und setzt die sog. OCP-Schwelle für den
Senke-Betrieb, die getrennt von der OCP-Schwelle des Quelle-Betriebs (siehe 5.4.6.2) einstellbar ist.
Gegenüber	dem	Befehl	für	den	Quelle-Betrieb	ist	hier	das	Hauptsystem	SINK	nicht	optional,	sonst	könnte	das	Gerät
nicht	unterscheiden.	Es	gelten	hier	keine	Einstellgrenzen.	Alternativ	zu	Werten	können	auch	hier	die	Parameter
MIN und MAX verwendet werden, um die Schwelle direkt auf das einstellbare MINimum oder MAXimum zu setzen.
| Abfrageform:   |     | SINK:CURRent:PROTection[:LEVel]?            |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Wertebereich:	 |     | <NRf>	=	0...1,1	*	Stromnennwert	des	Gerätes |     |     |     |     |     |     |     |
Beispiele:
SINK:CURR_PROT˽MAX	 Absolute	Kurzform.	Setzt	die	OCP-Schwelle	auf	110%	Nennstrom.
| 5.4.6.5  | SINK:POWer:PROTection[:LEVel]˽<NR3> |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
| ─ ─ | ─ ─ | ─ ─ | ─ ─ | ─ ─ |   | ─ ─ | ─ ─ |   | ─   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dieser Befehl wird nur von den bidirektionalen Netzgeräten unterstützt und setzt die sog. OPP-Schwelle für den
Senke-Betrieb, die getrennt von der OPP-Schwelle des Quelle-Betriebs (siehe 5.4.6.3) einstellbar ist.
Gegenüber	dem	Befehl	für	den	Quelle-Betrieb	ist	hier	das	Hauptsystem	SINK	nicht	optional,	sonst	könnte	das	Gerät
nicht	unterscheiden.	Es	gelten	hier	keine	Einstellgrenzen.	Alternativ	zu	Werten	können	auch	hier	die	Parameter
MIN und MAX verwendet werden, um die Schwelle direkt auf das einstellbare MINimum oder MAXimum zu setzen.
| Abfrageform:  |     | SINK:POWer:PROTection[:LEVel]? |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Wertebereich:	 <NRf>	=	0...1,1	*	Leistungsnennwert	des	Gerätes
Beispiele:
SINK:POWER:PROT˽3000	 Setzt	die	OPP-Schwelle	auf	3000	W,	sofern	das	Gerät	mindestens	3000	W
Nennleistung hat.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 52
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.7 Befehle für Überwachungsfunktionen
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─  ─  ─  ─ ─ ─ ─   ─ 
Diese Befehle ermöglichen die ferngesteuerte Konfiguration der Überwachungsfunktionen ("Events", wo vorhan-
den) des Gerätes bezüglich der Spannung, des Stromes oder der Leistung am DC-Eingang bzw. DC-Ausgang.
Bei den Serien PSB und PSBE dienen die Befehle nur zur Überwachung des sog. Quelle-
Betriebs. Für die Überwachung des Senke-Betriebs siehe unten bei 5.4.7.1.
Befehl Beschreibung
SYSTem:CONFig:UVD[?]˽<NR2> Identisch mit dem am Gerät
SYSTem:CONFig:UVD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} einstellbaren Event UVD
SYSTem:CONFig:UCD[?]˽<NR2> Identisch mit dem am Gerät
SYSTem:CONFig:UCD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} einstellbaren Event UCD
SYSTem:CONFig:OVD[?]˽<NR2> Identisch mit dem am Gerät
SYSTem:CONFig:OVD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} einstellbaren Event OVD
SYSTem:CONFig:OCD[?]˽<NR2> Identisch mit dem am Gerät
SYSTem:CONFig:OCD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} einstellbaren Event OCD
SYSTem:CONFig:OPD[?] <NR3> Identisch mit dem am Gerät
SYSTem:CONFig:OPD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} einstellbaren Event OPD
Für den :ACTion-Befehl können angegeben werden (siehe auch Gerätehandbuch):
NONE = Event inaktiv, es erfolgt keine Überwachung
SIGNAL = Beim Auftreten des Events wird eine Statusmeldung im Statusfeld der Anzeige des Gerätes ausgegeben
bzw. ein Bit im auslesbaren Questionable Register (STAT:QUES?) gesetzt (siehe „5.4.2. Statusregister“). Das Bit
zeigt an, daß ein bestimmtes Events aufgetreten ist. So kann das Ereignis auch per Fernabfrage erfaßt werden.
WARNING = Beim Auftreten des Events wird ein Warnmeldung in der Anzeige des Gerätes ausgegeben bzw. ein
Bit im auslesbaren Questionable Register (STAT:QUES?) gesetzt (siehe „5.4.2. Statusregister“). Das Bit zeigt an,
daß ein bestimmtes Events aufgetreten ist. So kann das Ereignis auch per Fernabfrage erfaßt werden.
ALARM = Beim Auftreten des Events wird eine Warnmeldung in der Anzeige des Gerätes, sowie ein akustisches
Signal ausgegeben (sofern die Einstellung „Alarmton = ein“ gesetzt wurde im Geräte-Setup) bzw. ein Bit im aus-
lesbaren Questionable Register (STAT:QUES?) gesetzt (siehe „5.4.2. Statusregister“). Das Bit zeigt an, daß ein
bestimmtes Events aufgetreten ist. So kann das Ereignis auch per Fernabfrage erfaßt werden. Zusätzlich schaltet
das Gerät den DC-Eingang bzw. DC-Ausgang aus.
Die Aktion ALARM ist mit den Gerätealarmen wie OVP usw. vergleichbar. Gerätealarme haben
jedoch Vorrang. Das heißt, falls z. B. OVP und OVD auf den gleichen Wert eingestellt würden
und die Eingangs- bzw. Ausgangsspannung erreicht diesen Wert, dann wird ein OV-Alarm
ausgelöst statt eines OVD-Events.
5.4.7.1 Weitere Befehle
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ─ ─ ─ ─ ─  ─ ─
Diese Befehle sind nur für die Überwachung (Events) des sog. Quelle-Betriebs der Serien PSB und nutzen das
zusätzliche Subsystem :SINK zur Unterscheidung.
Befehl Beschreibung
SYSTem:SINK:CONFig:UCD[?]˽<NR2> Identisch mit dem am
SYSTem:SINK:CONFig:UCD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} Gerät einstellbaren
Event „Senke: UCD“
SYSTem:SINK:CONFig:OCD[?]˽<NR2> Identisch mit dem am
SYSTem:SINK:CONFig:OCD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} Gerät einstellbaren
Event „Senke: OCD“
SYSTem:SINK:CONFig:OPD[?]˽<NR3> Identisch mit dem am
SYSTem:SINK:CONFig:OPD:ACTion[?]˽{NONE | SIGNal | WARNing | ALARm} Gerät einstellbaren
Event „Senke: OPD“
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 53
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.8 Befehle für Einstellgrenzen
Einstellgrenzen sind zusätzliche, global wirkende, einstellbare Grenzen, die verhindern sollen, daß ein bestimmter
Sollwert aus Versehen zu hoch oder zu tief eingestellt werden kann. Zum Schutz gegen z. B. Überspannung am
Verbraucher gibt es noch den Überspannungsschutz (OVP), aber generell ist es besser, einen falschen Sollwert
gar nicht erst zuzulassen.
Wird ein Sollwert an das Gerät gesendet, der höher als eine obere bzw. kleiner als eine untere Einstellgrenze ist,
wird der Sollwert ignoriert und ein Fehler in die Fehlerqueue geschrieben. Die untere Grenze kann dabei nicht höher
gesetzt werden als der jeweilige Sollwert aktuell eingestellt ist und umgekehrt genauso gilt das für die obere Grenze.
Die Befehle sind verknüpft mit den Einstellgrenzen („Limits“) wie sie im Menü des Gerätes gesetzt werden können
(wo vorhanden). Siehe dazu auch die Gerätehandbücher.
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 54
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP 1SP 1iSP 1BSP
1EBSP
1RLE
[SOURce:]VOLTage:LIMit:LOW[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze     ─              
U-min
[SOURce:]VOLTage:LIMit:HIGH[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze     ─              
U-max
[SOURce:]CURRent:LIMit:LOW[?] ˽NRf>[Unit]
Identisch mit der am Gerät einstellbaren Einstellgrenze     ─              
I-min
[SOURce:]CURRent:LIMit:HIGH[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze     ─              
I-max
[SOURce:]POWer:LIMit:HIGH[?]˽<NR3>
Identisch mit der am Gerät einstellbaren Einstellgrenze     ─         ─     
P-max
[SOURce:]RESistance:LIMit:HIGH[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze   ─  ─ ─  ─    ─ ─ ─ ─    
R-max
SINK:CURRent:LIMit:LOW[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─ ─ ─   ─
„Quelle: I-min“
SINK:CURRent:LIMit:HIGH[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─ ─ ─   ─
„Quelle: I-max“
SINK:POWer:LIMit:HIGH[?]˽<NR3>
Identisch mit der am Gerät einstellbaren Einstellgrenze ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─ ─ ─   ─
„Quelle: P-max“
SINK:RESistance:LIMit:HIGH[?]˽<NR2>
Identisch mit der am Gerät einstellbaren Einstellgrenze ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─ ─ ─   ─
„Quelle: R-max“

ModBus & SCPI
5.4.9 Befehle für den Master-Slave-Modus
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─  ─ ─ ─ ─   ─ ─     
Die nachfolgenden Befehle dienen sowohl zur ferngesteuerten Konfiguration, als auch zur Bedienung des Master-
Slave-Modus (kurz: MS). Die Befehle sind, wie bei anderen Funktionen auch, mit den am Gerät vorhandenen
Einstellmöglichkeiten verknüpft. Einzelheiten zum Master-Slave-Betrieb finden Sie im Gerätehandbuch.
Da hier mehrere Befehle zusammenwirken, ist eine bestimmte Reihenfolge erforderlich, wie unten aufgelistet.
Alternativ kann MS auch komplett am HMI der Geräte konfiguriert werden.
5.4.9.1 Konfigurationsbefehle
Befehl Beschreibung
SYSTem:MS:ENABle˽{ON | OFF} Aktiviert (ON) oder deaktiviert (OFF) den MS-Modus
SYSTem:MS:ENABle? Abfrage, ob der MS-Modus aktiviert ist
SYSTem:MS:LINK˽{MASTER | SLAVE} Legt die Rolle des Gerätes im MS-System fest oder fragt die mo-
SYSTem:MS:LINK? mentane ab:
MASTER = Gerät ist Master
SLAVE = Gerät ist Slave (wird auch zurückgegeben, wenn MS deak-
tiviert ist)
SYSTem:MS:INITialisation Startet die Initialisierung (Init) des Master-Slave-Verbunds, siehe
dazu auch das Gerätehandbuch. Nach erfolgreicher Initialisierung
können weitere, auf MS bezogene Befehle gesendet werden. Ob die
Init erfolgreich war, kann mit dem nächsten Befehl abgefragt werden
SYSTem:MS:CONDition? Fragt den Zustand der zuvor erfolgten Initialisierung ab. Zurückge-
geben werden kann:
INIT = Init war erfolgreich
NO INIT = Init war nicht erfolgreich
Um festzustellen, ob und wieviele Geräte vom Master in das MS-
System aufgenommen wurden, müßte nach der Initialisierung noch
die Anzahl mit SYST:MS:UNITS? abgefragt werden (siehe unten). Bei
Rückgabewert 0 ist das MS-System nicht richtig initialisiert worden.
SYSTem:MS:UNITs? Abfrage der Anzahl der Geräte, die initialisiert wurden. Die Anzahl
kann von der erwarteten abweichen, wenn der Master einen oder
mehrere Slaves nicht initialisiert hat. Falls nur der Master initialisiert
wurde, liefert der Befehl eine 1 zurück.
Abhängig von der auf Ihrem Gerät installierten
KE-Firmwareversion kann es sein, daß der Befehl
den Master als initialisiertes Gerät mitzählt.
SYSTem:SHARe:LINK˽{SLAVe}
Dieser Befehl ist nur gültig für Geräte der Serien
SYSTem:SHARe:LINK?
EL 9000 und ELR 9000, die einen Share-Bus
haben.
Dieser Befehl ist nur für elektronische Lasten gedacht, die in einem
Zwei-Quadranten-Betrieb (2QB) am Share-Bus als Slave arbeiten
müssen, selbst wenn eine Last ein Master eine Master-Slave-Systems
aus Lasten ist. Der Befehl funktioniert nur, wenn
• das Gerät als MASTER für Master-Slave definiert und
• Master-Slave aktiviert wurde und
• das Gerät eine elektronische Last ist,
ansonsten wird Fehler „Settings conflict“ zurückgegeben.
SYSTem:MS:TERMination˽{ON | OFF} Ausnahme: Nur bei den 10000er Serien verfügbar.
SYSTem:MS:TERMination? Dient zur digital geschalteten Aktivierung/Deaktivierung des Busab-
schlußwiderstandes am Master-Slave-Bus.
SYSTem:MS:BIAS˽{ON | OFF} Ausnahme: Nur bei den 10000er Serien verfügbar.
SYSTem:MS:BIAS? Dient zur digital geschalteten Aktivierung/Deaktivierung der zusätz-
lichen Bias-Widerstände am Master-Slave-Bus. Hinweis: dieser
Schalter wird automatisch auf ON gesetzt, wenn das Gerät ein MS-
Master ist.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 55
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.9.2 Andere MS-Befehle
Ab KE-Firmware 2.20 (9000er Serien) werden die Nennwerte eines initialisierten MS-System, inklusive des Ge-
samtwiderstandes, vom Master über die regulären Abfragebefehle für Gerätenennwerte (siehe 5.4.10) ausgelesen.
Die unten gelisteten Befehle werden daher u. U. nicht mehr von Ihrem Gerät unterstützt.
Befehl Beschreibung
SYSTem:MS:NOMinal:VOLTage? Abfrage der Gesamtspannung des aktuellen, initialisierten MS-Sy-
stem. Der Wert ist immer gleich der Nennspannung des Einzelgerätes.
SYSTem:MS:NOMinal:CURRent? Abfrage des Gesamtstroms des aktuellen, initialisierten MS-System.
Der Strom erhöht sich gegenüber dem Einzelgerät nur bei Parallel-
schaltung.
SYSTem:MS:NOMinal:POWer? Abfrage der Gesamtleistung des aktuellen, initialisierten MS-System.
Die Leistung erhöht sich gegenüber dem Einzelgerät immer.
5.4.10 Allgemeine Abfragebefehle
Hier werden weitere Befehle zum Abfragen von Informationen vom Gerät gelistet. Diese werden eher selten benötigt.
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 56
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP 1SP 1ISP 1BSP
1EBSP
1RLE
SYSTem:NOMinal:VOLTage?
Abfrage des Spannungsnennwertes eines einzelnen                   
Gerätes bzw. eines initialisierten Master-Slave-Systems
SYSTem:NOMinal:CURRent?
Abfrage des Stromnennwertes eines einzelnen Gerätes                   
bzw. eines initialisierten Master-Slave-Systems
SYSTem:NOMinal:POWer?
Abfrage des Leistungsnennwertes eines einzelnen                   
Gerätes bzw. eines initialisierten Master-Slave-Systems
SYSTem:NOMinal:RESistance:MINimum?
Abfrage des minimalen Widerstands eines einzelnen
Gerätes bzw. eines initialisierten Master-Slave-Systems.  ─ ─  ─ ─  ─    ─ ─ ─ ─    
Dieser ist bei elektronischen Lasten normalerweise
ungleich Null.
SYSTem:NOMinal:RESistance:MAXimum?
Abfrage des maximalen (Innen-)Widerstandswertes
 ─ ─  ─ ─  ─    ─ ─ ─ ─    
eines einzelnen Gerätes bzw. eines initialisierten Master-
Slave-Systems
SYSTem:DEVice:CLASs?
Abfrage der Geräteklasse. Zurückgegeben wird ein Wert,
der kennzeichnet, zu welcher Serie das Gerät gehört.
Man kann hiermit u. A. eindeutig und mit geringem                   
Aufwand bestimmen, ob das Gerät eine elektronische
Last oder ein Netzgerät ist. Eine Liste der Geräteklassen
ist in „A1. Geräteklassen“ zu finden.
DIAGnostic:INFormation:DEVice:OTIMe?
Betriebsstundenzähler. Abfrage der "operation time",
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─     
der Betriebsdauer des Gerätes. Die Rückgabe erfolgt
in Stunden.
DIAGnostic:INFormation:DEVice:ONTime?
Betriebsstundenzähler. Abfrage der globalen "on time",
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─     
also der Zeit, die der DC-Ausgang/Eingang des Gerätes
eingeschaltet war. Die Rückgabe erfolgt in Stunden.

ModBus & SCPI
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 57
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP 1SP 1ISP 1BSP
1EBSP
1RLE
DIAGnostic:INFormation:DEVice:OFFTime?
Betriebsstundenzähler. Abfrage der globalen "off time",
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─     
also der Zeit, die der DC-Ausgang/Eingang des Gerätes
ausgeschaltet war. Die Rückgabe erfolgt in Stunden.
FETCh:AHOur?
Betriebsstundenzähler. Abfrage der Amperestunden,
die das Gerät während der "on time" abgegeben oder
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─     
aufgenommen hat, je nach Gerätetyp. Bei bidirektionalen
Netzgeräten bezieht sich dieser Wert nur auf die Abgabe
von Strom im Quelle-Betrieb. Die Rückgabe erfolgt in Ah.
FETCh:WHOur?
Betriebsstundenzähler. Abfrage der Wattstunden, die
das Gerät während der "on time" abgegeben oder ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─     
aufgenommen hat, je nach Gerätetyp. Die Rückgabe
erfolgt in kWh.
FETCh:SINK:AHOur?
Betriebsstundenzähler. Nur verfügbar bei bidirektionalen
Netzgeräten. Abfrage der Amperestunden, die das Gerät ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─
während der "on time" aufgenommen hat. Die Rückgabe
erfolgt in Ah.
FETCh:SINK:WHOur?
Betriebsstundenzähler. Nur verfügbar bei bidirektionalen
Netzgeräten. Abfrage der Wattstunden, die das Gerät ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─
während der "on time" aufgenommen hat. Die Rückgabe
erfolgt in kWh.

ModBus & SCPI
5.4.11 Befehle zur Konfiguration des Gerätes
Hier werden Befehle zum Setzen von Geräteeinstellungen aufgelistet. Die mit den Befehlen veränderbaren
Einstellungen können Teil des aktuellen Benutzerprofils sein (siehe auch Gerätehandbuch). Das Verändern der
Einstellungen setzt aktivierte Fernsteuerung voraus. Die Einstellungen werden automatisch gespeichert.
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 58
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP K01
POWer:STAGe:AFTer:REMote˽{ AUTO | OFF }
POWer:STAGe:AFTer:REMote?
Legt fest, wie sich der DC-Eingang bzw. DC-Ausgang des Gerätes
 ─            ─ 
nach dem Verlassen der Fernsteuerung verhalten soll.
AUTO = Zustand bleibt erhalten
OFF = DC-Eingang / DC-Ausgang wird ausgeschaltet (Standard)
[SOURce:]VOLTage:CONTrol:SPEed˽{FAST | SLOW}
[SOURce:]VOLTage:CONTrol:SPEed?
Umschaltung der Regelungsgeschwindigkeit des Spannungsreglers
 ─ ─ ─ ─ ─ ─ ─ ─  ─ ─ ─ ─ ─
auf der Leistungsstufe von elektronischen Lasten bzw. Geräten
mit Last-Funktion zwischen schnell (FAST) und langsam (SLOW,
Standard).
SYSTem:CONFig:CONTroller:SPEed˽{FAST | SLOW | NORMal}
SYSTem:CONFig:CONTroller:SPEed?
─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ 
Erweiterung für 10000er Serien: drei Geschwindigkeiten. NORMAL
entspricht dem, was die Geräte früher als Standardwert hatten.
SYSTem:CONFig:INPut:RESTore[?]˽{AUTO | OFF}
SYSTem:CONFig:OUTPut:RESTore[?]˽{AUTO | OFF}
Legt fest, wie sich der DC-Eingang (bei el. Lasten) bzw. DC-Ausgang
(bei Netzgeräten) nach dem Einschalten des Gerätes verhalten soll.
             ─ 
Diese Befehle sind verknüpft mit den Einstellungen „Eingang nach
Power On“ bzw. „Ausgang nach Power On“ im Geräte-Setup.
AUTO = DC-Eingang/Ausgang wiederherstellen
OFF = DC-Eingang/Ausgang nach dem Einschalten immer aus
SYSTem:CONFig:USER:TEXT˽<SRD>
SYSTem:CONFig:USER:TEXT?
Schreibt einen bis zu 40 Zeichen langen Benutzertext in das Gerät,
              
der abfragbar ist und eine benutzerdefinierte, aus ASCII-Zeichen
gebildete Kennung darstellen kann, um ein bestimmtes Gerät unter
x gleichen Modellen zu identifizieren.
SYSTem:CONFig:ANALog:MONitor˽{DEFault | EL | PS | ELPS |
PSEL | COMBination}
SYSTem:CONFig:ANALog:MONitor?
Konfiguriert die Pins 9 (VMON) und 10 (CMON) der analogen
Schnittstelle bidirektionaler Geräte.
DEFault = Standardverhalten (VMON zeigt Spannungsistwert,
CMON zeigt Stromistwert von Quelle- oder Senke-Betrieb)

EL = Pin 10 zeigt nur den Stromistwert vom Senke-Betrieb ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ─ ─
(1
PS = Pin 10 zeigt nur den Stromistwert vom Quelle-Betrieb
ELPS = Pin 9 zeigt Stromistwert vom Senke-Betrieb, Pin 10 den
vom Quelle-Betrieb
PSEL = Umkehrung von ELPS
COMBination = Pin 10 zeigt den Strom vom Quelle- und Senke-
Betrieb in jeweils dem halben Signalbereich als -100%...0...100%.
Mehr siehe Gerätehandbuch.
1) Ausnahme: Befehl nur von den bidirektionalen Serien PSB und PSBE unterstützt

ModBus & SCPI
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 59
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP K01
SYSTem:CONFig:ANALog:PIN6˽{OT | PF | ALL}
SYSTem:CONFig:ANALog:PIN6?
Legt fest, welche Alarme Pin 6 signalisieren soll.
 ─            ─ 
OT = Pin 6 signalisiert nur Übertemperatur
PF = Pin 6 signalisiert nur Power Fail
All = Pin 6 signalisiert beide (Standard)
SYSTem:CONFig:ANALog:PIN14˽{OVP | OCP | OPP | OVP/OCP
| OVP/OPP | OCP/OPP | ALL}
SYSTem:CONFig:ANALog:PIN14?
 ─            ─ 
Legt fest, welche Alarme Pin 14 signalisieren soll. Möglich ist es, die
drei Alarme OVP, OCP und OPP einzeln oder in Kombination von
zweien oder alle auszugeben (logisch ODER).
SYSTem:CONFig:ANAlog:PIN15˽{CONT | POW}
SYSTem:CONFig:ANAlog:PIN15?
Legt fest, welchen Status Pin 15 signalisieren soll.  ─            ─ 
CONT = Regelungsart CV (Standardeinstellung)
POW = DC-Anschluß ein/aus
SYSTem:CONFig:ANALog:REFerence˽{5 | 10}
SYSTem:CONFig:ANALog:REFerence?
Wählt den Spannungsbereich für die Analogschnittstelle. Dies ist eine
Einstellung, die auf die Fernsteuerung über digitale Schnittstelle keine  ─            ─ 
Auswirkung hat.
5 = 0...5 V-Bereich
10 = 0...10 V-Bereich (Standardeinstellung)
SYSTem:CONFig:ANALog:REMSB:LEVel˽{NORMal | INVerted}
SYSTem:CONFig:ANALog:REMSB:LEVel?
Legt fest, wie der Pegel des Eingangs-Pins REM-SB der analogen
Schnittstelle (siehe Handbuch des Gerätes) vom Gerät interpretiert
 ─            ─ 
werden soll:
NORMAL = Pegel und Zustände wie im Handbuch beschrieben
(Standard)
INVERTED = Pegel und Zustände werden invertiert verarbeitet
SYSTem:CONFig:ANALog:REMSB:ACTion˽{OFF | AUTO}
SYSTem:CONFig:ANALog:REMSB:ACTion?
Legt fest, wie sich der Eingangs-Pin REM-SB der analogen
Schnittstelle in Bezug auf den DC-Eingang/Ausgang des Gerätes
auswirken soll:  ─            ─ 
OFF = der Pin kann den DC-Eingang/Ausgang nur ausschalten
AUTO = der Pin kann aus- und wiedereinschalten, wenn der DC-
Eingang/Ausgang vorher mindestens einmal per Taste am Bedienfeld
oder digitalem Befehl eingeschaltet wurde
SYSTem:CONFig:MODe˽{UIP | UIR}
SYSTem:CONFig:MODe?
Wählt die Betriebsart zwischen U/I/P und U/I/R. Bei Wahl von U/I/R

wird die Widerstandseinstellung über Befehl [SOURce]:RESistance  ─ ─  ─ ─  ─    ─ ─ ─
(1
bzw. SINK:RESistance freigegeben. Erkennbar ist der aktivierte
U/I/R-Modus am Gerät im Display lediglich am dann angezeigten
Widerstandssollwert.
SYSTem:CONFig:SEMif47˽{DISable | ENAble}
SYSTem:CONFig:SEMif47?
Aktiviert bzw. deaktiviert eine Funktionalität namens SEMIF47. ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ 
Dieses ist in Geräten verfügbar, die ab ca. 04/2022 produziert wurden.
Für Einzelheiten siehe das aktuelle Gerätehandbuch ab ca. 04/2022.
1) Ausnahme: Befehl wird nicht von Serie PS 10000 unterstützt

ModBus & SCPI
Befehl
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 60
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
9RLE 5RLE 9SP 9ISP 5ISP ESP
TD
TSP TISP 3LE BSP EBSP 3SP 2SP K01
SYSTem:COMMunicate:PROTocol:MODBus˽{ENABle | DISable}
SYSTem:COMMunicate:PROTocol:MODBus?
Aktivieren (enable) oder deaktivieren (disable) des ModBus-
Protokolls. Diese Einstellung wird gespeichert. Nach dem Befehl
             ─ 
zur Deaktivierung ist bis auf Weiteres keine Kommunikation mit
ModBus-Protokoll mehr möglich, es ist nur noch SCPI verfügbar.
Es kann jeweils nur eins der beiden Protokolle deaktiviert werden,
standardmäßig sind jedoch beide aktiviert.
SYSTem:COMMunicate:TIMeout˽<NR1>
SYSTem:COMMunicate:TIMeout?
Definiert ein Timeout in Millisekunden (Bereich: 5...65535, Werks-
einstellung: 5) das bei der Übertragung einer Nachricht zwischen  ─            ─ 
zwei aufeinanderfolgenden Bytes einer seriell gesendeten Nachricht
(USB, RS232) vergehen darf, bevor die Nachricht als „unvollständig
erhalten“ vom Gerät verworfen wird. Für mehr siehe Abschnitt 3.6.
SYSTem:COMMunicate:MONitoring:TIMeout˽<NR1>
SYSTem:COMMunicate:MONitoring:TIMeout?
Definiert ein Timeout in Sekunden (Bereich: 1...36000, Werksein-
stellung: 5) für die sogenannte "Schnittstellenüberwachung", auch
 ─            ─ 
genannt "connection timeout" (kurz: CTO). Details über diese Funk-
tionalität sind im Handbuch des Gerätes zu finden, zumindest in der
neuesten Ausgabe. Sollte in dem Handbuch für Ihr Gerät noch nichts
zu finden sein, bitte das einer anderen Serie nehmen.
SYSTem:COMMunicate:MONitoring:ACTion˽{ON | OFF}
SYSTem:COMMunicate:MONitoring:ACTion?
Schaltet die Schnittstellenüberwachung (CTO), an sich ein oder aus.
Die Einstellung wird automatisch und dauerhaft gespeichert. Die
eigentliche Überwachung und das zugehörige Timeout startet mit
dem Herstellen einer Verbindung zum Gerät über eine der digitalen  ─            ─ 
Schnittstellen. Sollte das Timeout ablaufen, wird die beschriebene
Reaktion ausgelöst und im Statusregister STAT:OPER das CTO-Bit
gesetzt.
ON = Aktiviert die CTO
OFF = Deaktiviert die CTO (Standardwert nach Rücksetzen)
SYSTem:ALARm:ACTion:PFAil˽{AUTO | OFF}
SYSTem:ALARm:ACTion:PFAil?
Legt fest, wie sich der DC-Eingang bzw. DC-Ausgang des Gerätes
nach einem Power Fail (PF) Alarm verhalten soll. PF bedeutet
             ─ 
z. B. kurzzeitiger Netzausfall; das Gerät könnte demnach nach
Netzwiederkehr automatisch weiterarbeiten.
AUTO = Zustand wie vor PF wird wiederhergestellt
OFF = DC-Eingang / DC-Ausgang bleibt (Standardeinstellung)
SYSTem:ALARm:ACTion:OTEMperature˽{AUTO | OFF}
SYSTem:ALARm:ACTion:OTEMperature?
Legt fest, wie sich der DC-Eingang bzw. DC-Ausgang des Gerätes
nach erfolgter Abkühlung nach einem Übertemperaturalarm (OT)
 ─            ─ 
verhalten soll.
AUTO = Zustand wie vor OT wird wiederhergestellt (Standardein-
stellung)
OFF = DC-Eingang / DC-Ausgang bleibt ausgeschaltet

ModBus & SCPI
| 5.4.11.1  | Befehle für Einstellungen zu Anybus-Modulen |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|  ─ | ─  | ─  | ─ ─ | ─ ─ |   | ─ ─ |   |   |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Die	meisten	Anybus-Module	können	für	Befehle	im	SCPI-Format	verwendet	und	somit	über	die	Schnittstelle	selbst
oder	die	eingebaute	USB-Schnittstelle	des	Gerätes	auch	„fernkonfiguriert“	werden.	Diese	Einstellungen	werden
automatisch gespeichert, sobald sie verändert wurden.
| Befehl |     |     |     |     | Beschreibung |     |     |     |     |
| ------ | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
SYSTem:COMMunicate:INTerface:CODe? Diese Abfrage gibt einen Zahlenwert zurück, der
das	im	Gerät	befindliche	Anybus-Schnittstellen-
modul bestimmt:
|     |     |     |     |     | 		5	=	Profibus      |     | 21 = Ethernet 2P    |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | ------------------- | --- | --- |
|     |     |     |     |     |   9 = RS232         |     | 22 = ModBus TCP 2P  |     |     |
|     |     |     |     |     | 16 = CANopen        |     | 23	=	Profinet/IO	2P |     |     |
|     |     |     |     |     | 18 = ModBus TCP 1P  |     | 25 = CAN            |     |     |
|     |     |     |     |     | 19	=	Profinet/IO	1P |     | 26 = EtherCAT       |     |     |
|     |     |     |     |     | 20 = Ethernet 1P    |     | 255 = kein Modul    |     |     |
SYSTem:COMMunicate:INTerface:TYPe? Gibt die Bezeichnung des Anybus-Schnittstellen-
moduls	als	String	zurück,	z.	B.	„Profibus“
SYSTem:COMMunicate:INTerface:SERial? Gibt die Sereinnummer des Anybus-Schnittstellen-
moduls als String zurück
Legt	die	Adresse	des	Gerätes	für	das	Profibus-
SYSTem:COMMunicate:INTerface:ADDRess˽<NR1>
SYSTem:COMMunicate:INTerface:ADDRess? modul IF-AB-PBUS oder CANopen-Modul IF-AB-
CANO fest bzw. fragt diese ab.
Zulässiger	Adressbereich	Profibus:	1...125
Zulässiger Adressbereich CANopen: 1...127
SYSTem:COMMunicate:PROFibus:ID? Fragt	die	Profibus-ID	des	Herstellers	ab.
SYSTem:COMMunicate:PROFibus:FTAG˽<SRD> Setzt	bzw.	fragt	den	Profibus-/Profinet-spezifischen
SYSTem:COMMunicate:PROFibus:FTAG? „Function Tag“ (Funktionskennung) ab, ein String
von bis zu 32 Zeichen
SYSTem:COMMunicate:PROFibus:LTAG˽<SRD> Setzt	bzw.	fragt	den	Profibus-/Profinet-spezifischen
SYSTem:COMMunicate:PROFibus:LTAG? „Location Tag“ (Ortskennung) ab, ein String von
bis zu 22 Zeichen
SYSTem:COMMunicate:PROFibus:DATe˽<SRD> Setzt	bzw.	fragt	das	Profibus-/Profinet-spezifische
SYSTem:COMMunicate:PROFibus:DATe? „Installation Date“ (Installationsdatum) ab, ein Da-
tums-/Zeitstring von bis zu 40 Zeichen
SYSTem:COMMunicate:PROFibus:DESCription˽<SRD> Setzt	bzw.	fragt	eine	Profibus-/Profinet-spezifi-
SYSTem:COMMunicate:PROFibus:DESCription? schen „Description“ (Beschreibung) ab, ein String
von bis zu 54 Zeichen
SYSTem:COMMunicate:PROFibus:NAMe˽<SRD> Setzt bzw. fragt den „Station name“ (Beschreibung)
SYSTem:COMMunicate:PROFibus:NAMe? ab, ein String von bis zu 200 Zeichen
SYSTem:COMMunicate:INTerface:BAUD˽<NR1> Dient zur Festlegung der Übertragungsgeschwin-
digkeit des Busses für das CANopen-, CAN oder
SYSTem:COMMunicate:INTerface:BAUD?
RS232-Modul. Gespeichert wird nur der Wert
0-9. Das heißt, bei Wert 3 gespeichert, würde ein
CANopen mit 100 kbps laufen und ein RS232 mit
19200 Baud.
|     |     |     |     |     | Wert | CANopen  | CAN      | RS232     |     |
| --- | --- | --- | --- | --- | ---- | -------- | -------- | --------- | --- |
|     |     |     |     |     | 0    | 10 kbps  | 10 kbps  | 2400 Bd   |     |
|     |     |     |     |     | 1    | 20 kbps  | 20 kbps  | 4800 Bd   |     |
|     |     |     |     |     | 2    | 50 kbps  | 50 kbps  | 9600 Bd   |     |
|     |     |     |     |     | 3    | 100 kbps | 100 kbps | 19200 Bd  |     |
|     |     |     |     |     | 4    | 125 kbps | 125 kbps | 38400 Bd  |     |
|     |     |     |     |     | 5    | 250 kbps | 250 kbps | 57600 Bd  |     |
|     |     |     |     |     | 6    | 500 kbps | 500 kbps | 115200 Bd |     |
|     |     |     |     |     | 7    | 800 kbps | 1 Mbps   | -         |     |
|     |     |     |     |     | 8    | 1 Mbps   | -        | -         |     |
|     |     |     |     |     | 9    | Auto     | -        | -         |     |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 61
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
SYSTem:COMMunicate:CAN:BROadcast˽<NR1> Legt die Broadcast-ID für normale CAN-Kommu-
SYSTem:COMMunicate:CAN:BROadcast? nikation fest. Zulässiger Bereich: 0...2047 (11 Bit)
bzw. 0...536870911 (29 Bit)
SYSTem:COMMunicate:CAN:DLC˽{AUTO | FILL} Datenlänge der CAN-Nachricht einer Antwort vom
SYSTem:COMMunicate:CAN:DLC? Gerät.
AUTO = die Anzahl der Datenbytes variiert je nach
Befehl/Register (Standard)
FILL = die Anzahl der Datenbytes ist immer 8, ggf.
mit Nullen aufgefüllt
SYSTem:COMMunicate:CAN:FORMat˽{BASe | EXTen- Wählt das CAN-Adress-Format.
ded} BASe = 11 Bit (CAN 2.0A) (Standard nach Zu-
SYSTem:COMMunicate:CAN:FORMat? rücksetzen)
EXTended = 29 Bit (CAN 2.0B)
SYSTem:COMMunicate:CAN:NODE˽<NR1> Legt die Basis-ID für die normale CAN-Kommu-
SYSTem:COMMunicate:CAN:NODE? nikation fest. Zulässiger Bereich: 0...2047 (11 Bit)
bzw. 0... 536870911 (29 Bit)
SYSTem:COMMunicate:CAN:READ:NODE˽<NR1> Legt die Base-ID für das zyklische Lesen fest.
SYSTem:COMMunicate:CAN:READ:NODE? Siehe Abschnitt 8.3.5 für Information darüber, was
zyklisches Lesen ist. Zulässiger Bereich: 0...2047
(11 Bit) bzw. 0... 536870911 (29 Bit)
SYSTem:COMMunicate:CAN:READ:ACTual˽<NR1> Definiert ein Intervall (in Millisekunden) für zykli-
SYSTem:COMMunicate:CAN:READ:ACTual? sches Lesen der Istwerte (U, I, P) des Gerätes
über eine CAN-Schnittstelle. Siehe auch Abschnitt
8.3.5. Zulässiger Bereich: 0 oder 20...5000 (0 =
zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:READ:ALIMits˽<NR1> Definiert ein Intervall (in Millisekunden) für zykli-
SYSTem:COMMunicate:CAN:READ:ALIMits? sches Lesen der Einstellgrenzen (Limits) von U
und I (bei Serien PSB/PSBE: Strom für den Quelle-
Betrieb) des Gerätes über eine CAN-Schnittstelle.
Siehe auch Abschnitt 8.3.5. Zulässiger Bereich:
0 oder 20...5000 (0 = zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:READ:BLIMits˽<NR1> Definiert ein Intervall (in Millisekunden) für zy-
SYSTem:COMMunicate:CAN:READ:BLIMits? klisches Lesen der Einstellgrenzen (Limits) von
Leistung (P) und Widerstand (R) (bei Serien
PSB/PSBE: P und R für den Quelle-Betrieb)
des Gerätes über eine CAN-Schnittstelle. Sie-
he auch Abschnitt 8.3.5. Zulässiger Bereich:
0 oder 20...5000 (0 = zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:READ:CLIMits˽<NR1> Nur für die Serien PSB und PSBE:
SYSTem:COMMunicate:CAN:READ:CLIMits? Definiert das Intervall (in Millisekunden) für zykli-
sches Lesen der Einstellgrenzen (Limits) von I, P
und R (Senke-Betrieb) über eine CAN-Schnittstelle.
Siehe auch Abschnitt 8.3.5. Zulässiger Bereich:
0 oder 20...5000 (0 = zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:READ:SETS˽<NR1> Definiert das Intervall (in Millisekunden) für zykli-
SYSTem:COMMunicate:CAN:READ:SETS? sches Lesen der Sollwerte (U, I, P, R) des Gerätes.
Siehe auch Abschnitt 8.3.5. Zulässiger Bereich: 0
oder 20...5000 (0 = zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:READ:BSETs˽<NR1> Nur für die Serien PSB und PSBE:
SYSTem:COMMunicate:CAN:READ:BSETs? Definiert das Intervall (in Millisekunden) für zykli-
sches Lesen der Sollwerte I, P, R (Senke-Betrieb)
des Gerätes. Siehe auch Abschnitt 8.3.5. Zuläs-
siger Bereich: 0 oder 20...5000 (0 = zyklisches
Lesen deaktiviert)
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 62
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
SYSTem:COMMunicate:CAN:READ:STAT˽<NR1> Definiert das Intervall (in Millisekunden) für zy-
SYSTem:COMMunicate:CAN:READ:STAT? klisches Lesen des Status des Gerätes. Siehe
auch Abschnitt 8.3.5. Zulässiger Bereich: 0 oder
20...5000 (0 = zyklisches Lesen deaktiviert)
SYSTem:COMMunicate:CAN:SEND:NODE˽<NR1> Legt die Base-ID für das zyklische Schreiben fest.
SYSTem:COMMunicate:CAN:SEND:NODE? Siehe auch Abschnitt 8.3.2. Zulässiger Bereich:
0...2047 (11 Bit) bzw. 0... 536870911 (29 Bit)
SYSTem:COMMunicate:CAN:TERMination˽{ON | OFF} Schaltet den CAN-Bus-Abschlußwiderstand im
SYSTem:COMMunicate:CAN:TERMination? Schnittstellenmodul ein (ON) oder aus (OFF)
(Standardeinstellung)
5.4.11.2 Befehle für Einstellungen zu Ethernetschnittstellen
Diese Befehle gelten für alle Geräte, die eine Ethernetschnittstelle unterstützen, egal ob eingebaut oder steckbar.
Einige werden jedoch nur unterstützt, wenn ein steckbares Anybus-Schnittstellenmodul vorhanden ist.
Die sog. 10000er Serien unterstützen sogar zwei Ethernetschnittstellen pro Gerät. Dabei wird der eingebaute
Ethernetport als der sekundäre Port betrachtet, egal ob ein Anybus-Ethernetmodul gesteckt ist oder nicht. Der
Zugriff auf die Einstellungen des sekundären Ports muß daher immer umgeschaltet werden. Siehe den Extrabefehl
weiter unten. Übersicht:
ELR 5000, EL 3000 B, PS 3000 ELR 9000, PSI 9000, PSB 9000, alle 10000er Serien
C, PS 9000, PS 9000 T, PSI 9000 PSE 9000, PSBE 9000
T, PSI 5000, PSI 9000 DT
Primär fest eingebauter Port Anybus (optional) Anybus (optional)
Sekundär - - fest eingebauter Port
Befehl Beschreibung
SYSTem:COMMunicate:LAN:1SPEed[?]˽{AUTO | Nur für Standard Ethernet-Anybusmodule und
10HALF | 10FULL | 100HALF | 100FULL ModBus TCP: Legt die Übertragungsgeschwindig-
keit der Ports P1 (gehörig zu :1SPEED) bzw. P2
SYSTem:COMMunicate:LAN:2SPEed[?]˽{AUTO | (gehörig zu :2SPEED) fest, wo vorhanden:
10HALF | 10FULL | 100HALF | 100FULL AUTO = Auto-Aushandlung
10HALF = 10MBit, Halbduplex
10FULL = 10MBit, Vollduplex
100HALF = 100MBit, Halbduplex
100FULL = 100MBit, Vollduplex
SYSTem:COMMunicate:LAN:ADDRess[?]˽<SRD> Legt die IP-Adresse der gewählten Ethernetschnitt-
stelle fest bzw. fragt diese ab. Der String muß die
IP-Adresse im typischen Format enthalten, wie
192.168.0.2.
SYSTem:COMMunicate:LAN:CONTrol[?]˽<NR1> Legt den TCP-Port (0...65535) für die gewählte
Ethernetschnittstelle fest bzw. fragt diesen ab. Die-
ser Port ist standardmäßig auf 5025 gesetzt und
dient zur ModBus RTU- bzw. SCPI-Kommunikation.
Er darf nicht auf 502 gesetzt werden, auch wenn das
Gerät ModBus TCP unterstützt. Port 502 ist parallel
aktiv und reserviert.
SYSTem:COMMunicate:LAN:DHCP[?]˽{ON | OFF} Aktiviert mit ON bzw. deaktiviert mit OFF die DHCP-
Funktionalität der gewählten Ethernetschnittstelle.
Standardeinstellung ist OFF. Bei OFF wird die mit
Befehl :ADDR (siehe oben) gesetzte IP benutzt.
SYSTem:COMMunicate:LAN:DNS1[?]˽<SRD> Legt die DNS-Adresse für den ersten (DNS1) oder
SYSTem:COMMunicate:LAN:DNS2[?]˽<SRD> zweiten (DNS2) Domänenserver bzw. fragt die
Adressen ab.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 63
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
SYSTem:COMMunicate:LAN:DOMain[?]˽<SRD> Legt die Domäne fest (siehe Netzwerkterminologie)
fest bzw. fragt diesen ab. Parameter für die Festle-
gung ist ein String mit bis zu 54 Zeichen Länge. Die
Domäne kann benutzt werden, um ein bestimmtes
Gerät im Netzwerk zu identifizieren oder dessen
Webseite aufzurufen, ohne dessen IP-Adresse zu
kennen.
SYSTem:COMMunicate:LAN:GATeway[?] <SRD> Legt die Gateway-Adresse der gewählten Ethernet-
schnittstelle fest bzw. fragt diese ab. Format wie bei
der IP-Adresse. Wird nicht unbedingt benötigt, kann
daher auf der Standardadresse gelassen werden.
SYSTem:COMMunicate:LAN:HOSTname[?]˽<SRD> Legt den Hostnamen (siehe Netzwerkterminologie)
fest bzw. fragt diesen ab. Parameter für die Fest-
legung ist ein String mit bis zu 54 Zeichen Länge
SYSTem:COMMunicate:LAN:KEEPalive[?]˽{ON | OFF} Aktiviert bzw. deaktiviert das sog. „TCP keep-alive“
für die gewählte Ethernetschnittstelle. Siehe auch
„3.7. Verbindungs-Timeout“. Standardeinstellung:
OFF (aus)
SYSTem:COMMunicate:LAN:MAC? Fragt die MAC-Adresse der gewählten Ethernet-
schnittstelle ab, sofern physikalisch vorhanden.
SYSTem:COMMunicate:LAN:SMASk[?]˽<SRD> Legt die Subnetzmaske des der gewählten Ether-
netschnittstelle fest bzw. fragt diese ab. Format wie
bei der IP-Adresse.
SYSTem:COMMunicate:LAN:TIMeout[?]˽<NR1> Legt für gewählte Ethernetschnittstelle ein Verbin-
dungs-Timeout in Sekunden fest. Mit Wert 0 wird der
Timeout deaktiviert. Siehe auch „3.7. Verbindungs-
Timeout“. Einstellbereich: B oder 5...65535. Stan-
dardeinstellung: 5
Für die 10000er Serien gibt es einen weiteren Befehl. Dieser dient zur Umschaltung des Zugriffs auf die Parame-
ter zwischen der eingebauten, sekundären Ethernetschnittstelle (RJ45) und der zusätzlich möglichen, primären
Ethernetschnittstelle (Slot, Anybus-Modul). Dabei ist primäre Schnittstelle nach dem Hochfahren standardmäßig
ausgewählt (INDex = 1), auch wenn kein Modul gesteckt ist.
Befehl Beschreibung
SYSTem:COMMunicate:LAN:INDex˽{1 | 2} Temporäre Umschaltung zwischen sekundärer
SYSTem:COMMunicate:LAN:INDex? (=2) und primärer (=1, Standard nach Hochfahren)
Ethernetschnittstelle.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 64
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.12 Befehle zur Fernbedienung des Funktionsgenerators
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─  ─  ─  ─ ─ ─ ─   ─ 
Die mittels dieser Befehle ladbaren Sequenzen und Tabellen werden nicht im Gerät gespeichert!
Der Funktionsgenerator ist ein komplexer Teil der Bedienmöglichkeiten des Gerätes. Er ist über eine Reihe von
SCPI-Befehlen konfigurier- und steuerbar. Die Bedienung des Funktionsgenerators am Gerät erzwingt eine gewisse
Abfolge von Auswahl und Einstellungen, bis hin zum eigentlichen Startpunkt. Die einzelnen Befehle können diese
Abfolge nicht erzwingen, daher ist der Anwender gefordert, die richtige Reihenfolge anzuwenden:
1) Art des Funktionsgenerators wählen
Der Funktionsgenerator muß nach dem Hochfahren des Gerätes mindestens einmal konfiguriert werden. Dazu
wird als erstes die Art des Funktionsgenerators gewählt, wovon die weiteren Schritte abhängen. Zur Verfügung
stehen zwei unterschiedliche Generatoren: XY und Arbiträr.
Der XY-Funktionsgenerator ist nichts weiter als ein Speicher für eine Tabelle aus bis zu 4096 Werten, die auf 0-125%
Istwert von Spannung oder Strom des Gerätes verteilt sind. Bidirektionale Geräte aus den PSB-Serien haben zwei
Tabellen, eine für Quelle-Betrieb (Generatormodus; IUPS) und eine für den Senke-Betrieb (Generatormodus:
IUEL). Der Modus IU kombiniert diese beiden Modi, so daß bei PSB-Geräten während der Funktionsgenerator
aktiv ist, zwischen den beiden Quadranten gewechselt werden, deren IU-Tabellen daher unterschiedlich sein kön-
nen. Der Wechsel geschieht wie in den anderen Betriebsarten auch durch das Verhältnis von Spannungssollwert
zu Spannungsistwert. Senke-Betrieb funktioniert nur, wenn die anliegende Spannung höher ist als der gesetzte
Spannungssollwert.
Der Arbiträrgenerator hingegen ist für Funktionen wie Sinus, Rechteck, Dreieck, Trapez und Rampe.
2) Funktionsgenerator konfigurieren (Teil 1)
Wenn der Arbiträrgenerator genutzt werden soll, ist der nächste Schritt die Auswahl, ob die Funktion auf die Span-
nung (U) oder den Strom (I) angewendet wird. Anwendung auf die Leistung (P) wird nicht unterstützt. Als dritter
Teil der Konfiguration sollte noch die Anzahl der zu verwendenden Stützpunkte (hier: Sequenzpunkte) festgelegt
werden. Das geschieht nicht automatisch durch Laden einer bestimmten Anzahl Sequenzpunkte in das Gerät.
Wenn der XY-Generator genutzt werden soll, ist der nächste Schritt die Auswahl, was für eine XY-Kurve später
geladen und gestartet werden soll. In Abhängigkeit davon werden die zu schreibenden Tabellenwerte interpretiert
und auf Plausibilität geprüft.
3) Funktionsgenerator konfigurieren (Teil 2)
Der letzte Schritt ist, Daten in den Funktionsgenerator zu laden. Beim Arbiträrgenerator werden dazu bis zu 99
Sequenzpunkte mit jeweils 8 Parametern befüllt. Die Anzahl der effektiv verwendeten Punkte ist beliebig, jedoch
mindestens eins. Beim XY-Generator werden 1-4096 Werte pro Tabelle geschrieben.
XY-Kurvendaten und Sequenzdaten müssen mittels eines "Übernehmen"-Befehls bestätigt wer-
den. Das erfordert eine gewisse Wartezeit vor dem nächsten Befehl. Es wird nach Abschicken
des Extrabefehls bzw. vor Start des Generators eine Wartezeit von mindestens 2 Sekunden
empfohlen.
4) Funktionsgenerator benutzen
Der Funktionsgenerator ist dann fertig konfiguriert und kann nun gestartet werden.
Ein Wechsel des Funktionsgeneratormodus' erfordert immer, den Funktionsgenerator quasi zu
verlassen, indem [SOURce:]FUNCtion:GENerator:SELect˽NONE gesendet wird. Erst danach
kann ein anderer Modus gewählt werden. Zuvor geladene Tabellen- oder Sequenzpunktdaten
gehen hierdurch verloren.
5.4.12.1 Funktionsübersicht
Nicht allen Serien mit einem Funktionsgenerator - nicht zu verwechseln mit dem Sequenzgenerator bei ELR 5000
oder dem Rampengenerator beiden 3000er Serie - haben den gleichen Umfang an Funktionen. Hier eine Übersicht,
welche Serien welchen Funktionen bieten:
ELR9 PSI9 DT PSIT PSB PSI1 PSB1 ELR1
Arbiträrgenerator        
XY-Generator   ─ ─    
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 65
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.12.2 XY-Generator: Moduswahl und Konfiguration (9000er Serien, außer PSB 90000)
Dieser Abschnitt gilt nur für 9000er Serien der ersten Generation mit einer XY-Tabelle. Der erste Schritt ist immer
den XY-Generator zu aktivieren und gleichzeitig dessen Modus zu wählen:
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:SELect˽{UI | IU | Wählt den XY-Funktionsgeneratormodus aus:
PV | NONE} UI = UI-Kurve, wird auch für die FC-Funktion verwendet
[SOURce:]FUNCtion:GENerator:SELect? IU = IU-Kurve
PV = Einfach PV-Kurve bzw. -Funktion (siehe auch
5.4.12.8)
Für die erweiterte PV-Kurve nach EN 50530 siehe Ab-
schnitt 5.4.17.
NONE = Funktionsgenerator verlassen, wird auch ver-
wendet, bevor man den Modus wechseln kann
Nach der Moduswahl können bzw. sollten Tabellendaten geladen werden. Siehe dazu 5.4.12 bzw. auch die Be-
schreibung des XY-Generators und wie dieser funktioniert im Gerätehandbuch.
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:XY:LEVel˽<NR1> 1. Wählt einen Tabelleneintrag (Bereich: 0...4095) zum
Schreiben aus bzw. liest dessen Nummer.
[SOURce:]FUNCtion:GENerator:XY:DATa˽<NRf> 2. Schreibt einen Wert ohne Einheit in den zuvor mit
[SOURce:]FUNCtion:GENerator:XY:DATa? :LEVel gewählten Tabelleneintrag. Dient auch zur Abfrage
des aktuellen Wertes.
[SOURce:]FUNCtion:GENerator:XY:SUBMit 3. Bis dato geschriebene Tabellendaten übernehmen.
Danach kann die Funktion gestartet werden.
5.4.12.3 XY-Generator: Moduswahl und Konfiguration (10000er Serie und PSB 9000)
Die Konfiguration des XY-Generators bei den PSB-Serien ist etwas komplizierter, da diese Geräte aufgrund der
Bidirektionalität und ihren Quelle- und Senke-Modi zwei Tabellen haben, die es zu unterscheiden gilt. Tabelle 1 ist
dabei dem Quelle-Betrieb zugeordnet, Tabelle 2 dem Senke-Betrieb. Je nach gewähltem Modus wird die eine,
die andere oder beide Tabellen genutzt. Übersicht und Vergleich der Modi:
XY- Beschreibung PSB- Nutzt Nutzbar für Anmerkungen
Modus Betrieb Tabelle nicht-PSB
IU IU-Kurve Quelle 1 und 2 nein Der aktive Quadrant kann zur Laufzeit durch
o. Senke Setzen des Spannungssollwertes umgeschal-
tet werden
IUEL IU-Kurve für elektroni- Senke 2 ELR ELR arbeiten immer im Senke-Betrieb
sche Last
IUPS IU-Kurve für Netzgerät Quelle 1 PSI PSI arbeiten immer im Quelle-Betrieb
PV Einfache PV-Funktion, Quelle 1 PSI, PSB
wird zu PVA umgeleitet
PVA PV-Kurve A Quelle 1 PSI PVA ist die Standardkurve, die auch für den
einfachen PV-Modus und den erweiterten
PVB PV-Kurve B Quelle 2 PSI
PV-Modus genutzt wird. PVB ist ein zweite
nutzbare.
FC F-Kurve Quelle 1 PSI Eine FC-Kurve ist eine UI-Kurve die hier für
einen IU-Generator geladen wird. Die Daten
müssen daher vorher entweder transponiert
oder direkt als Stromwerte berechnet werden.
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:SELect˽{FC | Wählt den XY-Funktionsgeneratormodus gemäß der Tabelle
IUPS | IUEL | IU | PV | PVA | PVB | NONE} oben. Für die erweiterte PV-Kurve nach EN 50530 siehe
[SOURce:]FUNCtion:GENerator:SELect? Abschnitt 5.4.17.
NONE = Funktionsgenerator verlassen, wird auch verwendet,
bevor man den Modus wechseln kann
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 66
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Alle 10000er Serien unterstützen alle 6 Modi des XY-Generators, egal ob ELR, PSB oder PSI.
Die Modi, welche vom jeweiligen Gerätetyp physikalisch-logisch nicht umgesetzt werden können,
würden nach Konfiguration und Start einfach nicht funktionieren.
Nach der Moduswahl können bzw. sollten Tabellendaten geladen werden. Siehe dazu 5.4.12 bzw. auch die Beschrei-
bung des XY-Generators und wie dieser funktioniert im Gerätehandbuch. Gemäß der Unterscheidung der Modi in
Hinsicht auf die jeweils genutzte XY-Tabelle müssen unterschiedliche Befehle zum Laden dieser verwendet werden:
Befehle für XY-Tabelle 1 Beschreibung
[SOURce:]FUNCtion:GENerator:XY:LEVel˽<NR1> 1. Wählt einen Tabelleneintrag (Bereich: 0...4095)
[SOURce:]FUNCtion:GENerator:XY:LEVel? zum Schreiben aus bzw. liest dessen Nummer.
[SOURce:]FUNCtion:GENerator:XY:DATa˽<NRf> 2. Schreibt einen Wert ohne Einheit in den zuvor
[SOURce:]FUNCtion:GENerator:XY:DATa? mit :LEVel gewählten Tabelleneintrag. Dient auch
zur Abfrage des aktuellen Wertes.
[SOURce:]FUNCtion:GENerator:XY:SUBMit˽FIRSt 3. Bis dato geschriebene Tabellendaten über-
nehmen. Danach kann die Funktion gestartet
werden.
Befehle für XY-Tabelle 2 Beschreibung
[SOURce:]FUNCtion:GENerator:XY:SECond:LEVel˽<NR1> 1. Wählt einen Tabelleneintrag (Bereich: 0...4095)
[SOURce:]FUNCtion:GENerator:XY:SECond:LEVel? zum Schreiben aus bzw. liest dessen Nummer.
[SOURce:]FUNCtion:GENerator:XY:SECond:DATa˽<NR2> 2. Schreibt einen Wert ohne Einheit in den zuvor
[SOURce:]FUNCtion:GENerator:XY:SECond:DATa? mit :LEVel gewählten Tabelleneintrag. Dient auch
zur Abfrage des aktuellen Wertes.
[SOURce:]FUNCtion:GENerator:XY:SUBMit˽SECond 3. Bis dato geschriebene Tabellendaten über-
nehmen. Danach kann die Funktion gestartet
werden.
5.4.12.4 Arbiträrgenerator: Moduswahl und Konfiguration
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:SELect˽{VOLTage | CUR- Wählt den Arbiträrgenerator aus.
Rent | NONE} VOLTage = Arbiträr für U
[SOURce:]FUNCtion:GENerator:SELect? CURRent = Arbiträr für I
NONE = Funktionsgenerator verlassen
[SOURce:]FUNCtion:GENerator:WAVe:STARt˽<NR1> Legt den ersten abzuarbeitenden Sequenzpunkt
[SOURce:]FUNCtion:GENerator:WAVe:STARt? (1...99) fest bzw. fragt dessen Nummer ab. Wird
nur ein Sequenzpunkt genutzt, muß :STARt =
:END gesetzt werden.
[SOURce:]FUNCtion:GENerator:WAVe:END˽<NR1> Legt den letzten abzuarbeitenden Sequenzpunkt
[SOURce:]FUNCtion:GENerator:WAVe:END? (1...99) fest bzw. fragt deren Nummer ab. Wird nur
ein Sequenzpunkt genutzt, muß :STARt = :END
gesetzt werden.
[SOURce:]FUNCtion:GENerator:WAVe:NUMBer˽<NR1> Legt fest, wie oft der Block aus Sequenzpunkten,
[SOURce:]FUNCtion:GENerator:WAVe:NUMBer? wie mit :STARt und :END festgelegt, durchlaufen
werden soll bzw. fragt die eingestellte Anzahl ab.
Bereich: 0 (unendlich oft) oder 1...999
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 67
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.12.5 Arbiträrgenerator: Sequenzpunktdaten laden
Sequenzpunktdaten sollten erst an das Gerät geschickt werden, wenn vorher in den Funktionsgenerator-Modus
umgeschaltet und die Zuordnung des Arbiträrgenerator zu U oder I festgelegt wurde.
Eine Funktion kann aus einer oder mehreren Sequenzpunkten bestehen, die dann einen Teil oder eine ganze
Funktion bilden. Mehrere Punkte, sofern so festgelegt, werden immer hintereinander ausgeführt und können teils
auch komplexe Funktionen abbilden. Sequenzpunktdaten werden mit drei Befehlen geladen, die daher auch eine
gewissen Reihenfolge der Übermittlung an das Gerät erfordern:
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVe:LEVel˽<NR1> 1. Wählt einen Sequenzpunkt von 99, ähnlich wie
[SOURce:]FUNCtion:GENerator:WAVe:LEVel? im Bedienfeld (HMI) des Gerätes, zum Schreiben
aus bzw. liest die aktuelle Sequenzpunktnummer
[SOURce:]FUNCtion:GENerator:WAVe:INDex˽<NR1> 2. Für jeden Sequenzpunkt (0...7) sind eine
[SOURce:]FUNCtion:GENerator:WAVe:INDex? Reihe Parameter zu setzen. INDex wählt aus,
welcher Parameter mit dem nächsten Befehl
(:DATa)geschrieben werden soll. Die Indexe
sind unten erläutert. Dient auch zur Abfrage des
aktuellen Index‘.
[SOURce:]FUNCtion:GENerator:WAVe:DATa˽<NR2> 3. Schreibt einen Wert, z. B. eine Frequenz, in
[SOURce:]FUNCtion:GENerator:WAVe:DATa? den zuvor gewählten Parameter, als Teil einer
Sequenz. Auswahl des Wertes über :INDex.
Dient auch zur Abfrage des letzten Wertes.
[SOURce:]FUNCtion:GENerator:WAVe:SUBMit 4. Übernehmen aller Daten. Ohne diesen Befehl
kann der FG zwar gestartet werden, aber alle
Werte sind noch auf 0.
Wenn man den Arbiträrgenerator am Bedienfeld des Gerätes konfiguriert, werden bestimmte Parameter gegen-
einander abgegrenzt, damit das resultierende Signal am DC Eingang/Ausgang später so aussieht, wie man es
erwartet. In der Fernsteuerung ist diese Art von Plausibilität auch vorhanden, die Prüfung kann aber nicht direkt
beim Setzen der Werte erfolgen, sondern erst nachdem die Daten per :SUBMit-Befehl übernommen wurden.
Zum Beispiel ist Index 0 an Index 5 geknüpft und Index 1 an Index 6, weil die Mittellinie einer Sinuskurve, hier der
AC-Anteil, einen Offset zu 0 darstellt und somit der DC-Anteil (Index 5 oder 6) vom Wert her immer mindestens
so groß sein muß wie der AC-Anteil (Index 0 oder 1, der höhere von beiden), ansonsten würde die Sinuskurve
gekappt werden. Siehe Abbildungen unten.
In Anlehnung an die Einstellmöglichkeiten am Gerät, wenn der Arbiträr-Generator gewählt wurde, sind folgende
Indexe mit :INDex auswählbar und mit :DATa schreibbar:
Index Parameter Datentyp Einheit Wertebereich Hinweis
0 Startwert (Amplitude) Fließkomma A, V 0...Nennwert von U oder I Für AC-Anteil
1 Endwert (Amplitude) Fließkomma A, V 0...Nennwert von U oder I Für AC-Anteil
2 Startfrequenz in Hz Ganzzahl Hz 0...10000 Für AC-Anteil
3 Endfrequenz in Hz Ganzzahl Hz 0...10000 Für AC-Anteil
4 Startwinkel in ° Ganzzahl - 0...359 Für AC-Anteil
5 Startwert (Offset) Fließkomma A, V 0...Nennwert von U oder I Für DC- und
Nur PSB-Geräte, beim Strom: AC-Anteil
-Nennwert I...+ Nennwert I
6 Endwert (Offset) Fließkomma A, V 0...Nennwert von U oder I Für DC- und
Nur PSB-Geräte, beim Strom: AC-Anteil
-Nennwert I...+ Nennwert I
7 Sequenzdauer Fließkomma s 0,0001...36000
Falls Startwert ungleich Endwert (Indexe 0+1, sowie 5+6), dann erwartet das Gerät eine gewisse
Mindeststeigung von ±0,058%/s über die Sequenzpunktdauer, sowie eine Frequenzänderung
von ±9,3 Hz/s (Indexe 2+3), ansonsten werden die Werte nicht angenommen. Dies wird nicht in
Form eines SCPI-Fehlers mitgeteilt. Es ist somit z. .B. nicht möglich, den Eingangsstrom einer
elektronischen Last um 1 A über 1 h verteilt ansteigen zu lassen (Rampe). Weiteres Beispiel:
bei einer Sequenzpunktdauer = 2 s würden Startfrequenz = 1 Hz und Endfrequenz = 10 Hz
nicht akzeptiert, jedoch Startfrequenz = 30 Hz und Endfrequenz = 5 Hz schon.
Zuordnung der Parameter anhand einer Beispielkurve
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 68
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 69
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
)CD(
tratS
U,I
Start (AC) End (AC)
t
Seq.time
)CD(
tratS
)CD(
dnE
U,I
Start (AC) End (AC)
t
Seq.time
)CD(
dnE
bzw.
5
xednI
U,I
Index 0 Index 1
t
5.4.12.6 XY-Generator: Steuerung
Nach der Konfiguration des XY-Generators und Laden von Tabellendaten ist es ausreichend, nur den DC-Eingang
bzw. DC-Ausgang des Gerätes einzuschalten. Die Kurve ist sofort aktiv. Es findet kein Ablauf oder automatischer
Stopp statt, außer es tritt ein abstellender Gerätealarm auf.
5.4.12.7 Arbiträrgenerator: Steuerung
Im Gegensatz zum XY-Generator, dessen Kurve sofort aktiv ist sobald man den DC-Eingang/-Ausgang einschaltet,
wird der Arbiträrgenerator gezielt gesteuert. Eine Pausierung ist dabei nicht möglich. Stoppt der Ablauf, egal ob
durch Erreichen der erwarteten Ablaufzeit oder durch einen Gerätealarm, beginnt der nächste Start den gesamten
Ablauf von vorn.
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVe:STATe˽{RUN | STOP} Startet bzw. stoppt den arbiträren Funkti-
[SOURce:]FUNCtion:GENerator:WAVe:STATe? onsgenerator oder fragt den Zustand ab

ModBus & SCPI
5.4.12.8 Sonderfunktion "Einfache PV" (Photovoltaik)
ELR9 PSI9 DT PST PSIT PSB PSBE PSI1 PSB1 PSBE1 ELR1
─  ─ ─ ─  ─   ─ ─
Für die erweiterte PV-Funktion nach EN 50530 siehe Abschnitt „5.4.17. Befehle für die erwei-
terte PV-Simulation“.
Die einfache PV-Funktion, wie verfügbar bei Netzgeräten bestimmter Serien, basiert auf dem XY-Generator und
simuliert ein Solarmodul. Die dazu benötigte PV-Kurve wird als komplette, vorberechnete IU-Tabelle in das Gerät
geladen, im Gegensatz zur Bedienung am HMI wo das Gerät die Kurve aus vier zu definierenden Parametern
selbst berechnet. Diese Möglichkeit kann man jedoch auch in der Fernsteuerung nutzen, auch wenn das etwas
umständlich erscheint. Die Tabelle kann man auf zwei Wegen erhalten:
1. Berechnung mit externen Mitteln und Abspeicherung als z. B. CSV-Datei, was erlaubt, die Tabelle auch vom
USB-Stick zu laden oder direkt in einer Steuerungssoftware berechnen und transferieren.
2. Man läßt das Gerät die Tabelle über das HMI berechnen, in den FG laden und geht danach wieder zurück. An
dieser Stelle kann man die Tabelle für spätere Verwendung direkt am HMI auf USB-Stick speichern.
Während des Funktionsablaufs kann die Beschattung zwischen 0 und 100% eingestellt werden, um verschiedene
Lichtverhältnisse zu simulieren. Sie wirkt als ein Faktor auf den Strom Isc.
Befehl Beschreibung
[SOURce:]IRRadiation˽<NR1> Stellt den Beschattungswert (engl. irradiation) während der Solar-Panel-
[SOURce:]IRRadiation? Simulation ein oder fragt ihn als Prozentwert ab (Bereich 0...100). Der
Wert wirkt auf den DC-Ausgangsstrom und verschiebt den MPP auf der
X-Achse
Davon ausgehend, das Gerät ist bereits in Fernsteuerung und die PV-Tabelle liegt berechnet vor, ist folgender
Ablauf vorgesehen:
► So konfigurieren Sie das Gerät für die einfache PV-Funktion
Nr. Befehl Beschreibung
1 FUNC:GEN:SEL˽PV Wählt XY-Generator mit PV-Funktion. Ab hier befindet sich das Gerät im
Funktionsgenerator-Modus. Ein PSB-Gerät leitet auf Modus PVA um,
siehe dazu 5.4.12.3.
2 FUNC:GEN:XY:LEV˽0 Schreibt alle Tabellenwerte der PV-Funktion nacheinander in das Gerät
3 FUNC:GEN:XY:DAT˽<NR2>
...
8193 FUNC:GEN:XY:LEV˽4095
8194 FUNC:GEN:XY:DAT˽<NR2>
8195 FUNC:GEN:XY:SUBM Die geschriebenen Werte übernehmen
Nach der Übernahme der Werte und einer Wartezeit (empfohlen: >1 s) kann die Funktion gestartet werden. Optional,
falls noch nicht geschehen, könnten noch globale Grenzwerte für Spannung und Leistung so gesetzt werden, daß
sie den Ablauf der PV-Funktion nicht stören. Dabei ist es ratsam, die Ausgangsspannung auf die Leerlaufspannung
(Uoc) des simulierten Solarmoduls zu setzen, alternativ auf das Maximum:
Nr. Befehl Beschreibung
8196 VOLT˽MAX Spannung auf Maximum setzen, das wäre unabhängig vom Modell.
Alternativ kann man die Spannung auch auf mindesten Uoc setzen für
unbelasteten Zustand
8197 POW˽MAX Leistungssollwert auf Maximum setzen, unabhängig vom Modell
Nachdem alles eingerichtet und geladen ist, kann die Simulation gestartet und die Beschattung variiert werden.
Diese wirkt wie ein Faktor auf den Strom, so daß sich die PV-Kurve auf der Y-Achse verschiebt, wenn der Wert
verändert wird. Für eine Darstellung und mehr Informationen siehe Handbuch Ihres Gerätes.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 70
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
► So steuern Sie das Gerät während die Photovoltaik-PV-Funktion läuft
| Nr. Befehl |     |     | Beschreibung |     |     |     |
| ---------- | --- | --- | ------------ | --- | --- | --- |
8198 OUTP˽ON Einschalten des DC-Ausgangs und Starten der Funktion
| 8199 IRR˽85 |     |     | Beschattung	setzen,	beispielsweise	85% |     |     |     |
| ----------- | --- | --- | -------------------------------------- | --- | --- | --- |
8200 OUTP˽OFF Ausschalten des DC-Ausgangs, um die Funktion zu stoppen
8201 FUNC:GEN:SEL˽NONE Mit NONE wird kein Funktionsgeneratortyp gewählt und der Modus damit
wieder verlassen.
| 5.4.12.9  | Sonderfunktion: FC (fuel cell) |          |           |            |      |     |
| --------- | ------------------------------ | -------- | --------- | ---------- | ---- | --- |
| ELR9 PSI9 | DT PST                         | PSIT PSB | PSBE PSI1 | PSB1 PSBE1 | ELR1 |     |
| ─        | ─ ─                            | ─       | ─        |  ─        | ─    |     |
Die	Brennstoffzellensimulation	(fuel	cell,	FC)	läuft	als	eine	Funktion	auf	dem	XY-Generator,	wie	er	bei	Netzgeräten
bestimmter	Serien	verfügbar	ist.	Die	dazu	benötigte	FC-Kurve	wird	als	komplette,	vorberechnete	Tabelle	aus	4096
Werten in das Gerät geladen. Die FC-Kurve ist grundsätzliche eine UI-Kurve, also würde für ein PSI 9000 der UI-
Modus aktiviert. Bei den Serien PSB 9000, PSI 10000 und PSB 10000 gibt es keinen UI-Modus, dafür aber einen
direkten FC-Modus. Bei den Tabellenwerten an sich gibt es auch einen Unterschied. Übersicht zur Moduswahl:
|                                |     |     | PSI 9000       |     |     | PSB 9000 / PSB 10000 / PSI 10000 |
| ------------------------------ | --- | --- | -------------- | --- | --- | -------------------------------- |
| XY-Generatormodus              |     |     | UI             |     |     | FC                               |
| Geladene Kurvendaten enthalten |     |     | Spannungswerte |     |     | Stromwerte                       |
Das	Laden	der	Kurve	steht	im	Gegensatz	zur	Bedienung	am	HMI,	wo	das	Gerät	die	Kurve	aus	vier	zu	definieren-
den	Stützpunkten	selbst	berechnet.	Diese	Möglichkeit	kann	man	jedoch	auch	in	der	Fernsteuerung	nutzen,	auch
wenn etwas umständlich erscheint. Die Tabelle kann man auf zwei Wegen erhalten:
1. Berechnung mit externen Mitteln, z. B. in MS Excel.
2. Man läßt das Gerät die Tabelle über das HMI berechnen und in den FG laden lassen, sowie dann das Funk-
tionsgenerator-Menü	verlassen.	An	dieser	Stelle	könnte	man	die	Tabelle	für	spätere	Verwendung	direkt	am	HMI
auf USB-Stick speichern bzw. aus dem Gerät auslesen.
Die zweite Methode empfiehlt sich zur Verwendung mit den Geräten, wo transponiert werden
muß, weil es keine offizielle Formel zur Berechnung von Stromwerten aus einer UI-FC-Kurve gibt.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 71
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.13 Befehle zur Fernbedienung des Sequenzgenerators (nur ELR 5000)
Die mittels dieser Befehle ladbaren Sequenzpunktdaten und anderen Einstellungen werden im
Gerät gespeichert und auch mit den an der Bedieneinheit einstellbaren Werten synchronisiert.
Der Sequenzgenerator der Serie ELR/ELM 5000 ist eine vereinfachte Variante des Arbiträrgenerators anderer
Geräteserien und ist daher recht ähnlich zu konfigurieren und zu bedienen.
Die Bedienung des Funktionsgenerators am Gerät erzwingt eine gewisse Abfolge von Auswahl und Einstellungen,
bis hin zum eigentlichen Startpunkt. Die einzelnen Befehle können diese Abfolge nicht erzwingen, daher ist der
Anwender gefordert, die richtige Reihenfolge anzuwenden:
1) Als erstes muß der Sequenzgenerator konfiguriert werden. Dazu gehört zum Einen das Laden der Sequenz-
punktdaten, sofern andere als die zuletzt gespeicherten verwendet werden sollen. Zum Anderen sollten jedesmal
die weiteren Einstellungen festgelegt werden, wie Startsequenzpunkt, Endsequenzpunkt usw. Welche von den
beiden Aufgaben zuerst erledigt wird, ist nicht relevant.
2) Den Sequenzgenerator starten und ggf. stoppen.
5.4.13.1 Konfiguration des Sequenzgenerators
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVE:STARt˽<NR1> Legt den ersten abzuarbeitenden Sequenzpunkt
[SOURce:]FUNCtion:GENerator:WAVE:STARt? (1...100) fest bzw. fragt dessen Nummer ab. Wird
nur ein Sequenzpunkt benutzt, muß :END = :STARt
gesetzt werden.
[SOURce:]FUNCtion:GENerator:WAVE:END˽<NR1> Legt den letzten abzuarbeitenden Sequenzpunkt
[SOURce:]FUNCtion:GENerator:WAVE:END? (1...100) fest bzw. fragt dessen Nummer ab.
[SOURce:]FUNCtion:GENerator:WAVE:NUMBer˽<NR1> Legt fest, wie oft der Block aus Sequenzpunkten, wie
[SOURce:]FUNCtion:GENerator:WAVE:NUMBer? mit :STARt und :END festgelegt, durchlaufen werden
soll bzw. fragt die eingestellte Anzahl ab.
Bereich: 0 (unendlich oft) oder 1...999
5.4.13.2 Steuerung des Sequenzgenerators
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVE:STATe˽{RUN | Startet bzw. stoppt den Sequenzgenerator oder fragt
STOP} den Zustand ab. Das Gerät wechselt beim Start des
[SOURce:]FUNCtion:GENerator:WAVE:STATe? Generators über Fernsteuerung automatisch die
Anzeige.
5.4.13.3 Sequenzdaten laden
Sequenzdaten können jederzeit an das Gerät geschickt, wenn der DC-Eingang ausgeschaltet ist. Ein bestimmter
Modus muß dafür nicht aktiviert werden. Es ist lediglich erforderlich, daß die Daten jedes geschriebenen Sequenz-
punktes für das Gerät gültig sein müssen. Da bei SCPI mit realen Werten gearbeitet wird, ist es besonders wichtig
darauf zu achten, welche Sequenzdaten für welches Gerätemodell geladen werden.
Welche der 100 Sequenzpunkte mit Daten beschrieben werden sollen bestimmt der Anwender genauso wie den
Start- und End-Sequenzpunkt und die Anzahl der Durchläufe der Sequenz. Es sind beliebig große Blöcke nutzbar.
Ein nicht mit Daten beschriebener Sequenzpunkt würde, wenn beim Durchlauf verarbeitet, Spannung und Strom auf
0 setzen, die minimale Sequenzpunktzeit von 300 ms ausführen und demnach eine kurze Unterbrechung darstellen.
Befehle zum Laden von Daten für Sequenzpunkte:
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVE:LEVel˽<NR1> Wählt einen Sequenzpunkt (1...100) zum Schreiben
[SOURce:]FUNCtion:GENerator:WAVE:LEVel? aus bzw. liest die Nummer des aktuell gewählten
[SOURce:]FUNCtion:GENerator:WAVE:INDex˽<NR1> Für jeden Sequenzpunkt sind 4 Parameter zu setzen.
[SOURce:]FUNCtion:GENerator:WAVE:INDex? Der Wert INDex wählt mit 0 - 3 aus, welcher Para-
meter mit dem nächsten Befehl (:DATa) geschrieben
werden soll. Die Indexe sind unten erläutert. Dient
auch zur Abfrage des aktuellen Index‘.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 72
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:WAVE:DATa˽<NR2> Schreibt einen Wert in den zuvor gewählten Para-
[SOURce:]FUNCtion:GENerator:WAVE:DATa? meter, als Teil der Definition eines Sequenzpunktes.
Auswahl des Parameters erfolgt über :INDex. Dient
auch zur Abfrage des letzten Wertes.
[SOURce:]FUNCtion:GENerator:WAVE:SUBMit Übernehmen aller Daten. Ohne diesen Befehl würden
die vorherigen Werte verwendet werden.
Das Ganze wird für jeden zu schreibenden Sequenzpunkt wiederholt. Im Fall, daß alle 100 Sequenzpunkte geladen
werden sollen, sind demnach 901 Befehle nötig (siehe Schritte 1-10 im Beispiel unten).
In Anlehnung an die Einstellmöglichkeiten am Gerät, wenn ein Sequenzpunkt zur Einstellung gewählt wurde, sind
folgende Parameter mit :INDex auswählbar und mit :DATa schreibbar:
Index Parameter Wertebereich
0 Spannung für den Sequenzpunkt in Volt 0...Nennwert von U
1 Strom für den Sequenzpunkt in Ampere 0...Nennwert von I
2 Leistung für den Sequenzpunkt in Watt 0...Nennwert von P
3 Dauer des Sequenzpunktes in Millisekunden 1...36.000.000, Schrittweite 1 ms
Wird einer der drei Sollwerte nicht gesetzt, behält er den zuletzt gespeicherten Wert bei. Daher
wird empfohlen, immer alle drei Werte vorzugeben, um das gewünschte Resultat zu erzielen.
Die am HMI setzbaren Einstellgrenzen („Limits“) gelten nicht für Sequenzpunktdaten.
5.4.13.4 Programmierbeispiel zum Sequenzgenerator
Annahme: die Quelle soll mit 20 A für 60 Sekunden belastet werden. Da ein ELM 5000 Lastmodul max. 320 W
Leistung aufnehmen kann, darf die Eingangsspannung 16 V nicht überschreiten, sonst greift die Leistungsbegren-
zung und der Strom sinkt. Der Leistungssollwert sollte für dieses Beispiel auf das Maximum gesetzt sein.
Nr. Befehl Beschreibung
1 FUNC:GEN:WAVE:LEV˽12 Wählt den 12. Sequenzpunkt zum Schreiben aus, in diesem Beispiel wird
nur einer beschrieben und verwendet
2 FUNC:GEN:WAVE:IND˽0 Index 0 wählen: Spannungssollwert
3 FUNC:GEN:WAVE:DAT˽0 Setzt den Spannungssollwert für Sequenzpunkt 12 auf 0 V. Möglich wäre
0...80 bei einem 80 V-Modell. Bei elektronischen Lasten ist die Spannung
zweitranging und wird, wenn Betrieb der Last in CC-Modus geplant ist,
auf 0 gesetzt.
4 FUNC:GEN:WAVE:IND˽1 Index 1 wählen: Stromsollwert
5 FUNC:GEN:WAVE:DAT˽20 Setzt den Stromsollwert für Sequenzpunkt 12 auf 20 A. Möglich wäre
0...25 bei einem 80 V-Modell
6 FUNC:GEN:WAVE:IND˽2 Index 2 wählen: Leistungssollwert
7 FUNC:GEN:WAVE:DAT˽320 Setzt die Leistung für Sequenzpunkt 12 auf 320 W. Möglich wäre 0...320.
Soll die Leistung nicht unter Nennwert begrenzt werden, sollten alle ver-
wendeten Sequenzpunkte auf den Maximalwert gesetzt werden. Es gibt
keinen globalen Leistungssollwert.
8 FUNC:GEN:WAVE:IND˽3 Index 3 wählen: Zeit
9 FUNC:GEN:WAVE:DAT˽60000 Setzt die Zeit, die mit den durch Sequenzpunkt 12 gesetzten Sollwerten
vergehen soll, auf 60 s.
10 FUNC:GEN:WAVE:SUBM Sequenzdaten übernehmen
11 FUNC:GEN:WAVE:STAR˽12 Setzt den ersten Sequenzpunkt der Sequenz auf 12
12 FUNC:GEN:WAVE:END˽12 Setzt den letzten Sequenzpunkt der Sequenz auch auf 12
13 FUNC:GEN:WAVE:NUMB˽1 Setzt 1 Durchlauf, d. h. es findet keine Wiederholung der Sequenz statt
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 73
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Das Ergebnis: mit dem Start des Sequenzgenerators werden die Sollwerte des einen Sequenzpunktes (0 V, 20 A,
320 W) gesetzt und ggf. der DC-Eingang eingeschaltet. Die elektronische Last nimmt dann für 60 Sekunden lang
max. 20 A Strom auf. Nach Ablauf der 60 Sekunden stoppt der Sequenzgenerator automatisch nach 1 Durchlauf.
Der DC-Eingang bleibt eingeschaltet und die Last macht weiter mit dem gesetzten Strom.
Wollte	man	aber,	daß	die	Last	nach	der	Sequenz	keinen	Strom	mehr	zieht,	wäre	ein	weiterer	Sequenzpunkt	nötig,
der	0	A	setzt.	Da	Sequenzpunkte	immer	nacheinander	ablaufen,	böte	sich	an,	auch	Sequenzpunkt	13	zu	program-
mieren. Die Befehlsfolge oben würde sich dann nach Schritt 9 wie folgt ändern:
| Nr. Befehl |     | Beschreibung |     |     |     |     |     |     |
| ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
10 FUNC:GEN:WAVE:LEV˽13 Wählt den 13. Sequenzpunkt zum Schreiben aus
| 11 FUNC:GEN:WAVE:IND˽1 |     | Index 1 wählen: Stromsollwert |     |     |     |     |     |     |
| ---------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
12 FUNC:GEN:WAVE:DAT˽0 Setzt den Stromsollwert für Sequenzpunkt 13 auf 0 A
| 13 FUNC:GEN:WAVE:SUBM |     | Sequenzpunktdaten übernehmen |     |     |     |     |     |     |
| --------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
14 FUNC:GEN:WAVE:STAR˽12 Setzt den ersten Sequenzpunkt der Sequenz auf 12
15 FUNC:GEN:WAVE:END˽13 Setzt den letzten Sequenzpunkt der Sequenz auf nun 13
16 FUNC:GEN:WAVE:NUMB˽1 Setzt	1	Durchlauf,	d.	h.	es	findet	keine	Wiederholung	der	Sequenz	statt
Die Spannung und die Zeit für diesen Sequenzpunkt sind irrelevant. Der Sequenzgenerator stoppt nach Sequenz
13	mit	0	A	Strom,	auch	wenn	der	DC-Eingang	an	bleibt.	Da	kein	Strom	mehr	in	die	Last	fließt,	kann		man	das	als
"DC-Eingang = aus" betrachten.
| 5.4.14  | Befehle zur Fernbedienung des MPP-Tracking |     |     |     |     |     |     |     |
| ------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|   | ─ ─ | ─ ─ ─	(1 | ─ ─ | ─  | ─ ─ | ─ ─ |   | ─  |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- |
(1 Nicht PSI 9000 DT
Das sogenannte „Maximum Power Point Tracking“ (MPPT) ist ein Vorgang den z. B. Solarwechselrichter benut-
zen,	um	den	MPP,	den	maximalen	Leistungspunkt	eines	Solarpaneels	zu	finden.	Die	elektronische	Last	bildet
das	Tracking	nach.	Die	Erläuterung	dieser	Funktion	und	ihrer	4	Modi	ist	im	Handbuch	des	Gerätes	zu	finden.	Hier
werden nur die Befehle aufgelistet, mit denen die Funktion fernbedienbar wird.
| 5.4.14.1  | Konfiguration des MPP-Tracking |     |     |     |     |     |     |     |
| --------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Die	Konfiguration	vor	dem	Start	des	Tracking-Vorgangs	wird	mittels	14	Indexen	und	entsprechenden	:DATa-
Befehlen erledigt:
| Befehl |     |     |     | Beschreibung |     |     |     |     |
| ------ | --- | --- | --- | ------------ | --- | --- | --- | --- |
[SOURce:]FUNCtion:GENerator:MPP:INDex˽0 Index 0: Wahl des MPP-Tracking-Modus‘
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽{NONE |  MPP1:	MPP-Tracking-Modus	1	(MPP	finden)
MPP1 | MPP2 | MPP3 | MPP4} MPP2: MPP-Tracking-Modus 2 (Folgen)
MPP3: MPP-Tracking-Modus 3 (Direkt)
MPP4: MPP-Tracking-Modus 4 (Benutzerkurve)
NONE: MPPT deaktivieren
[SOURce:]FUNCtion:GENerator:MPP:INDex˽1 Index 1: Setzen der sog. Open circuit voltage (Uoc)
| [SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> |     |     |     | Uoc (0-Unom) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
[SOURce:]FUNCtion:GENerator:MPP:INDex˽2 Index 2: Setzen des sog. Short-circuit current (Isc)
| [SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> |     |     |     | Isc (0-Inom) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
[SOURce:]FUNCtion:GENerator:MPP:INDex˽3 Index 3: Setzen der Spannungsgrenze für den Direkt-
Modus 3 (Umpp). Empfehlung: immer auf 0 setzen
| [SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> |     |     |     | Umpp (0-Unom) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
[SOURce:]FUNCtion:GENerator:MPP:INDex˽5 Index 5: Setzen des MPP im Modus 3 (Pmpp, füh-
rende	Regelgröße)
| [SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> |     |     |     | Pmpp (0-Pnom) |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
[SOURce:]FUNCtion:GENerator:MPP:INDex˽6 Index	6:	Setzt	ΔP	(in	Watt),	eine	Differenzgröße	zum
MPP, oberhalb der das Gerät wieder anfängt, den
MPP zu suchen (nur Modus 2 und Modus 3)
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> Der stellbare Bereich ist bei manchen Serien auf 0-50
W begrenzt, bei anderen auf 0-Pnom
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 74
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:MPP:INDex˽7 Index 7: ermittelter MPP
[SOURce:]FUNCtion:GENerator:MPP:DATa? Liest drei Werte aus (Uist, Iist, Pist), die den gefun-
denen MPP definieren (Modi 1, 2 und 4)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽8 Index 8: Spannungswerte für Modus 4 setzen
[SOURce:]FUNCtion:GENerator:MPP:LEVel[?]˽<NR1> Spannungswert zum Setzen anwählen (1...100)
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR2> Spannungswert setzen (0-Unom)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽9 Index 9: Meßergebnisse von Modus 4
[SOURce:]FUNCtion:GENerator:MPP:LEVel[?]˽<NR1> Meßwert anwählen (1...100)
[SOURce:]FUNCtion:GENerator:MPP:DATa? Meßwert auslesen (drei Werte: Uist, Iist, Pist)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽10 Index 10: Regelintervall festlegen, für das Abfahren
der Spannungswert im Modus 4 bzw. zeitliches
Raster beim MPP-Finden (dieser Parameter ist nur
in Fernsteuerung verfügbar und bei manueller Be-
dienung auf das Minimum gesetzt)
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR1> Intervall in Millisekunden (5...60000)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽12 Index 12: Festlegen der Endnummer der 100 Span-
nungswerte (Index 8) für Modus 4
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR1> Endnummer (1...100)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽11 Index 11: Festlegen der Startnummer der 100 Span-
nungswerte (Index 8) für Modus 4
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR1> Startnummer (1...100)
[SOURce:]FUNCtion:GENerator:MPP:INDex˽13 Index 13: Festlegen der Wiederholungen der Durch-
läufe im Modus 4
[SOURce:]FUNCtion:GENerator:MPP:DATa[?]˽<NR1> Anzahl Wiederholungen (0...65535)
5.4.14.2 Steuerung des MPP-Tracking
Das MPP-Tracking wird per separatem Befehl gestartet bzw. gestoppt. Dabei ist es unerheblich, ob der DC-Eingang
noch ausgeschaltet ist. Er würde beim Start automatisch mit eingeschaltet.
Befehl Beschreibung
[SOURce:]FUNCtion:GENerator:MPP:STATe[?]˽{RUN | RUN = Startet den Vorgang des MPP-Tracking im
STOP} zuvor gewählten Modus
STOP = Stoppt MPP-Tracking jederzeit, egal ob es
schon zu einem Ergebnis geführt hat oder nicht
? = Status des Tracking auslesen
Der mit FUNC:GEN:MPP:STAT? auslesbare Status des Tracking-Vorgangs gibt an, ob er noch läuft oder schon
beendet ist. Dabei unterscheidet sich der Status STOP bei den vier Modi etwas:
Modus 1: STOP heißt, der MPP wurde gefunden und das Tracking wurde beendet.
Modi 2 und 3: Diese Modi stoppen nicht automatisch, daher meldet STOP nur den per Befehl gesetzten Zustand.
Modus 4: STOP heißt, die gesetzte Anzahl Durchläufe der Benutzerkurve (Spannungswerte) wurde erreicht.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 75
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.15 Befehle für das Alarmmanagement
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
             ─     
Auch bei Fernsteuerung ist ein Alarmmanagement für Gerätealarme wie Überspannung (OV), Übertemperatur (OT)
usw. möglich. Diese Alarme werden bei Nutzung der SCPI-Befehlssprache vom Gerät in Statusregistern angezeigt,
die zwecks Aufzeichnung von Alarmen regelmäßig gelesen werden sollten (engl. polling).
5.4.15.1 Auslesen von Gerätealarmen
Das Auslesen erfolgt mit dem Questionable Statusregister, entweder über das Teilregister :CONDITION oder
:EVENT. STAT:QUES:COND? oder STAT:QUES? bzw. STAT:QUES:EVEN? geben eine Zahl zurück, welche
die Bits im Register repräsentiert (siehe Registermodell in „5.4.2. Statusregister“). Ein gesetztes Bit bedeutet,
ein bestimmter Alarm liegt momentan an. Für die Definition der Gerätealarme siehe das Handbuch des Gerätes.
5.4.15.2 Bestätigen bzw. Löschen von Gerätealarmen
Das Löschen ein oder mehrerer Gerätealarme im CONDITION-Register sollte üblicherweise erst nach dem Aus-
lesen erfolgen, weil bereits nicht mehr vorhandene Alarme sonst nicht mehr erfaßt werden können. Zum Löschen
wird der auch zur Abfrage von anderen Fehlern benutzte Befehl SYST:ERR? bzw. SYST:ERR:ALL? genommen.
Sollten ein oder mehrere Alarme weiterhin anliegen, können sie nicht gelöscht werden.
5.4.15.3 Alarmzähler
Ab einer gewissen Version der KE-Firmware (siehe 1.1.2) haben die Geräte einen internen Zähler für alle Geräte-
alarme, der jederzeit auslesbar ist und der die Anzahl der aufgetretenen Gerätealarme seit dem letzten Einschalten
des Gerätes zählt. Das Auslesen löscht die Zähler nicht und sie werden beim Ausschalten nicht gespeichert.
Für alle Netzgeräte im Quelle-Betrieb, sowie elektronische Lasten:
Befehl Beschreibung
SYSTem:ALARm:COUNt:OVOLtage? Zählt Überspannungsalarme (OVP, einstellbare Schwelle)
SYSTem:ALARm:COUNt:OTEMperature? Zählt Übertemperaturalarme (OT, nicht einstellbar)
SYSTem:ALARm:COUNt:OPOWer? Zählt Überleistungsalarme (OPP, einstellbare Schwelle)
SYSTem:ALARm:COUNt:OCURrent? Zählt Überstromalarme (OCP, einstellbare Schwelle)
SYSTem:ALARm:COUNt:PFAil? Zählt Power fail Alarme (PF, nicht einstellbar)
Für alle bidirektionalen Netzgeräte im Senke-Betrieb zusätzlich unterstützt:
Befehl Beschreibung
SYSTem:SINK:ALARm:COUNt:OCURrent? Zählt Überstromalarme (OCP, einstellbare Schwelle), wenn
diese im Senke-Betrieb auftreten, zwecks Unterscheidung vom
Quelle-Betrieb
SYSTem:SINK:ALARm:COUNt:OPOWer? Zählt Überleistungsalarme (OPP, einstellbare Schwelle), wenn
diese im Senke-Betrieb auftreten, zwecks Unterscheidung vom
Quelle-Betrieb
Zusätzlich und nur bei den 10000er Serien implementiert:
Befehl Beschreibung
SYSTem:ALARm:COUNt:SHARebusfail? Zählt Share-Bus-Fail Alarme (SF, nicht einstellbar)
5.4.15.4 Beispiel
Sie steuern das Gerät fern und lesen intervallartig STAT:QUES:COND? und erhalten z. B. stets den Wert 3072
zurück. Gemäß dem Registermodell für das Questionable Statusregister ist das die Summe der Wertigkeiten von
Bit 10 (Remote) und Bit 11 (Output/Input on). Es ist also Fernsteuerung aktiv und der DC-Ausgang/Eingang ist
eingeschaltet. Nun tritt eine Alarmsituation ein, zum Beispiel Übertemperatur (OT). Das Gerät müßte nun den
Gerätealarm OT über Bit 3 melden. Zusätzlich kann es sein, daß der DC-Ausgang/Eingang von seinem Status
her abgeschaltet wird, nicht nur die Leistungsstufe(n). Das ist nicht bei jeder Geräteserie gleich, somit kann bei
einem OT-Alarm also entweder der Wert 1032 oder 3080 zurückgegeben werden. Beide enthalten die Wertigkeit
8 von Bit 3.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 76
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.16 Befehle für Sollwert-Sätze (Recall, nur PSI 5000)
Die bei der Serie PSI 5000 A vorhandene Recall-Funktion für Sollwertsätze kann auch ferngesteuert konfiguriert
werden. Dabei werden SCPI-Befehle aus dem Standard verwendet, so daß die Abfolge bei Verwendung von SCPI
hier anders ist als vergleichsweise bei ModBus. Übersicht der allein für Recall zugeordneten Befehle:
Befehl Beschreibung
*RCL˽{1...9} Lädt einen von neun Sollwertsätzen, bestehend aus vier Werten (U-Sollwert,
I-Sollwert, OVP-Wert, OCP-Wert) aus dem internen Speicher und überschreibt
die aktuell für den DC-Ausgang gesetzten Werte. Kann nur bei Zustand
„DC-Ausgang = aus“ ausgeführt werden.
*SAV˽{1...9} Speichert die vier aktuell für den DC-Ausgang eingestellten Werte (U-Sollwert,
I-Sollwert, OVP-Wert, OCP-Wert) in den gewählten Sollwertsatz ab, damit
dieser später mit *RCL {1...9} wieder abgerufen werden kann. Kann nur bei
Zustand „DC-Ausgang = aus“ ausgeführt werden.
MEMory:STATe:DELete˽{1...9} Löscht den gewählten Sollwertsatz, indem alle vier Werte darin auf Null gesetzt
werden. Der Sollwertsatz kann später jederzeit neu überschrieben werden.
Ähnlich der Bedienung der Recall-Funktion am Bedienfeld des Gerätes werden die Befehle nur akzeptiert, wenn
der DC-Ausgang des Gerätes ausgeschaltet ist.
Für das Setzen der eigentlichen vier Werte, die in den neun Sollwertsätzen mit den o.g. Befehlen gespeichert
werden können, werden Standardbefehle wie [SOURce:]VOLTage verwendet. Siehe Beispiele unten.
5.4.16.1 Beispielabfolge zum Speichern eines Sollwertsatzes
Sie haben beispielsweise ein Netzgerät PSI 5040-20 A mit 40 V Nennspannung und 20 A Nennstrom. Sie wollen
Sollwertsatz 5 mit den Werten U = 10 V, I = 5 A und Überspannungsschutz (OVP) = 12 V beschreiben. Letzteres,
damit die Ausgangsspannung bei einem Überschwingen nicht wesentlich höher als 12 V geht und sicherheitshalber
den Ausgang abschaltet, um die angeschlossene Last zu schützen. Der Überschwinger ist Resultat eines typischen
Regelverhaltens, wie es auftreten kann, wenn der Strom auf 0 gesetzt wurde, während die Spannung noch 10 V
ist und das Gerät dann keinen Strom und keine Spannung abgibt, und man den Strom schlagartig wieder freigibt.
Die Überstromabschaltung ist Ihnen für die Anwendung unwichtig, daher wäre es sinnvoll, diese auf den Maximal-
wert zu setzen (hier: 22 A), damit der OCP nicht unerwartet auslöst. Wird der Wert nicht extra gesetzt, wird der
letzte irgendwann mal eingestellte Wert übernommen, der dann zunächst unbekannt ist. Somit wäre über SCPI
folgende Abfolge an das Gerät zu senden:
Nr. Befehl Beschreibung
1 OUTP˽OFF DC-Ausgang ausschalten (egal, ob bereits aus), damit der Sollwertsatz geschrieben
werden kann
2 VOLT˽10 Setze 10 V für den Ausgang (normaler Sollwert)
3 CURR˽5 Setze 5 A für den Ausgang (normaler Sollwert)
4 VOLT:PROT˽12 Setze OVP-Schwelle auf 12 V
5 CURR:PROT˽22 Setze OCP-Schwelle auf 22 A
6 *SAV˽5 Speichere Sollwertsatz 5
5.4.16.2 Beispielabfolge zum Abrufen ein Sollwertsatzes
In der Fernsteuerung sind die vier Werte, die man durch das Abrufen eines Sollwertsatzes schnell ändern könnte,
auch durch Einzelbefehle schnell geändert. Daher wird das Abrufen über Fernsteuerung selten genutzt werden.
Ein wichtiger Unterschied ist auch, daß der Sollwertsatz nur bei Ausgang = aus geschrieben und abgerufen werden
kann, während die Sollwerte jederzeit gesetzt werden können.
Möchten Sie trotzdem z. B. den vormals gespeicherten Sollwertsatz 3 abrufen, gehen Sie folgendermaßen vor:
Nr. Befehl Beschreibung
1 OUTP˽OFF DC-Ausgang ausschalten (optional, wenn schon aus), damit der Sollwertsatz abgerufen
werden kann
2 *RCL 3 Lädt die vier im Sollwertsatz 3 gespeichert Werte für den DC-Ausgang und übernimmt
sie gleichzeitig
3 OUTP ON (optional) Gegebenenfalls noch den DC-Ausgang einschalten
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 77
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Um sozusagen auszulesen, was nun eigentlich für Werte im Sollwertsatz 3 gespeichert sind, könnte man diese
abfragen. Das geht nur indirekt, nach dem vorherigen Laden eines Sollwertsatzes, wie oben geschehen:
Nr. Befehl Beschreibung
1 VOLT? Abfrage des Spannungswertes,wie im zuvor geladenen Sollwertsatz enthalten
2 CURR? Abfrage des Stromwertes,wie im zuvor geladenen Sollwertsatz enthalten
3 VOLT:PROT? Abfrage des OVP-Wertes,wie im zuvor geladenen Sollwertsatz enthalten
4 CURR:PROT? Abfrage des OCP-Wertes,wie im zuvor geladenen Sollwertsatz enthalten
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 78
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.17 Befehle für die erweiterte PV-Simulation
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
─ ─ ─  ─ ─ ─ ─ ─ ─  ─ ─ ─ ─   ─ ─
PV-Simulation wird generell nur von Netzgeräte-Serien unterstützt, solchen mit XY-Generator. Das sind aktuell
(Stand 05/2022):
• PSI 9000 2U - 24U
• PSI 10000
• PSB 9000 / PSB 10000
Die Variante nach DIN EN 50530 ist eine zusätzliche, erweiterte Version der bei einigen Serien vorhandenen
einfachen PV-Simulation und wird von den o. g. Geräten ab Firmware KE 2.19/HMI 2.11 (PSI 9000), KE 2.25/
HMI 2.04 (PSB 9000) sowie KE/HMI 2.01 (PSB/PSI 10000) unterstützt. Das bedeutet, daß die Funktion für ältere
Geräte durch ein Firmwareupdate nachträglich installiert werden könnte.
Alle über die unten gelisteten Befehle einstellbaren Parameter sowie die auslesbaren Daten sind in der Norm
definiert, werden dort beschrieben und daher dient die Norm dem Anwender als zusätzliche Referenz.
5.4.17.1 Allgemeine Konfiguration
Befehl Beschreibung
FUNCtion:PHOTovoltaics:MODe˽{OFF | ET | UI Moduswahl für die PV-Simulation
| DAYET | DAYUI} OFF = Simulation ausgeschaltet (Standardeinstellung)
FUNCtion:PHOTovoltaics:MODe? ET = Kontinuierlicher Modus, während der Simulation kön-
nen Temperatur und Einstrahlungsstärke variiert werden
UI = Kontinuierlicher Modus, während der Simulation können
Spannung und Strom im MPP variiert werden
DAYET = Simuliert einen voreingestellten Tagesverlauf,
während der Simulation können keine Werte verändert
werden. Die Datensätze (Index) bestehen aus einer Index-
nummer, einem Temperaturwert, einer Einstrahlungsstärke
und einer Verweildauer
DAYUI = Simuliert einen voreingestellten Tagesverlauf,
während der Simulation können keine Werte verändert
werden. Die Datensätze (Indexe) bestehen aus einer In-
dexnummer, Spannungs- und Stromwerten im MPP und
einer Verweildauer
FUNCtion:PHOTovoltaics:IMODe˽{MPP | ULIK} Eingabemodus (gilt für alle mit :MODe wählbaren Modi,
FUNCtion:PHOTovoltaics:IMODe? siehe Matrix und Beispiele in 5.5.3)
MPP = Die Grundwerte zur Berechnung der PV-Kurve wer-
den als Umpp und Impp eingegeben. Diese Werte sind dann
im Simulations-Modus UI veränderlich(Standardeinstellung)
ULIK = Die Grundwerte zur Berechnung der PV-Kurve wer-
den als U (Leerlaufspannung) und I (Kurzschlußstrom)
OC SC
eingegeben. Diese Werte sind dann im Simulations-Modus
ET veränderlich.
5.4.17.2 Konfiguration für Tagesdaten-Modus
Die nachfolgend gelisteten Befehle können nur bei gewähltem Tagesdaten-Modus (DAYET oder DAYUI, siehe
oben) benutzt werden und erzeugen ansonsten Fehler.
Es empfiehlt sich, vor dem Schreiben neuer Daten den alten Datensatz mit :DAY CLEAR zu
löschen, besonders wenn der nächste kürzer ist als der vorherige.
Befehl Beschreibung
FUNCtion:PHOTovoltaics:DAY:INTerpolate˽{ON Nur für Simulations-Modi DAYET und DAYUI:
| OFF} ON = Interpolation ein
FUNCtion:PHOTovoltaics:DAY:INTerpolate? OFF = Interpolation aus (Standardeinstellung)
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 79
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
FUNCtion:PHOTovoltaics:DAY:MODe˽{READ | Nur für Simulations-Modi DAYET und DAYUI:
WRITe} Zugriffmodus auf die Tagesdaten
FUNCtion:PHOTovoltaics:DAY:MODe?
READ = Daten nur lesbar (Standardeinstellung)
WRITe = Daten nur schreibbar
FUNCtion:PHOTovoltaics:DAY˽CLEar Nur für Simulationsmodi DAYET und DAYUI:
Alle Daten löschen
FUNCtion:PHOTovoltaics:DAY:INDex˽<NR1> Nur für Simulationsmodi DAYET und DAYUI:
FUNCtion:PHOTovoltaics:DAY:INDex? Festlegen des Index‘ (1...100000) eines Datensatzes
zwecks Rücklesen der Tagesdaten. Beim Schreiben von
Tagesdaten wird dieser Index ignoriert. Dafür muß der
Indexwert in FUNC:PHOT:DAY:DAT verwendet werden.
FUNCtion:PHOTovoltaics:DAY:DATa˽{<NR1>, Nur für Simulationsmodi DAYET und DAYUI:
<NR2>, <NRf>, <NR1>} Tagesdaten (4 Werte) schreiben oder aus dem voher zu
FUNCtion:PHOTovoltaics:DAY:DATa? wählenden Index lesen. Jenachdem, ob Simulationsmo-
dus DAYET oder DAYUI gewählt wurde, werden die Daten
anders interpretiert:
Modus DAYET:
1. Wert = Index, Einstellbereich: 1- 100000
2. Wert = Einstrahlstärke in W/m²,
Einstellbereich: 0-1500
3. Wert = Temperatur in °C,
Einstellbereich: -40...+80
4. Wert = Verweilzeit des Indexes in ms,
Einstellbereich: 500...1800000 (^=0,5s...0,5h)
Modus DAYUI:
1. Wert = Index, Einstellbereich: 1- 100000
2. Wert = Umpp in V, Einstellbereich: 0-Nennspg.
3. Wert = Impp in A, Einstellbereich: 0-Nennstrom
4. Wert = Verweilzeit des Indexes in ms,
Einstellbereich 500...1800000 (^=0,5s...0,5h)
FUNCtion:PHOTovoltaics:TECHnology˽{MAN | Vorwahl der zu simulierenden Paneel-Technologie, wodurch
CSI | THIN} bestimmte Parameter auf feste Werte gesetzt werden, bzw.
FUNCtion:PHOTovoltaics:TECHnology? Wahl des manuellen Modus
MAN = Manueller Modus
CSI = Paneel mit cSi-Technologie (Standardeinst.)
THIN = Paneel mit Dünnfilm-Technologie
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 80
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.17.3 Datenaufzeichnung
Das Gerät kann während der Laufzeit der PV-Simulation, egal welcher Modus, 576.000 Datensätze mit jeweils 6
Werten (Istwerte U, I, P und U, I, P im MPP) aufzeichnen. Die Datenaufzeichnung kann vor dem Start der Simu-
lation oder während des Ablaufs aktiviert werden. Ist der Speicher voll, wird er wieder überschrieben, ohne ihn
vorher zu löschen und die Anzahl der aufgezeichneten Datensätze (:REC:NUM?) auf 0 gesetzt. Es wird alle 100
ms ein Datensatz aufgezeichnet, das ergibt also max. 16 Stunden.
Die Aufzeichnung stoppt entweder beim Ende der Simulation oder Deaktivierung der Aufzeichnung. Danach können
die aufgezeichneten Daten schrittweise ausgelesen werden. Sofern sie benötigt werden, sollte das geschehen,
bevor das Gerät ausgeschaltet, denn die Daten werden nicht dauerhaft gespeichert.
Befehl Beschreibung
FUNCtion:PHOTovoltaics:RECord:ACTive˽{ENABle | Datenaufzeichnung
DISable} ENABle = eingeschaltet
FUNCtion:PHOTovoltaics:RECord:ACTive? DISable = ausgeschaltet (Standardeinstellung)
FUNCtion:PHOTovoltaics:RECord˽CLEar Aufgezeichnete Daten löschen
FUNCtion:PHOTovoltaics:RECord:NUMBer? Anzahl der bisher aufgezeichneten Datensätze
(1...576.000)
FUNCtion:PHOTovoltaics:RECord:INDex˽<NR1> Festlegen oder Auslesen der Indexnummer
FUNCtion:PHOTovoltaics:RECord:INDex? (1...576.000) des gewählten Datensatzes. Muß vor
dem Auslesen der Datensätze mit :DATa? stets neu
gesetzt werden.
FUNCtion:PHOTovoltaics:RECord:DATa? Datensatz X am zuvor gesetzten Index auslesen.
Das Gerät gibt dann folgende Werte kommagetrennt
zurück:
1. Wert = Indexnummer
2. Wert = Istwert Spannung
3. Wert = Istwert Strom
4. Wert = Istwert Leistung
5. Wert = Umpp (Spannung im MPP)
6. Wert = Impp (Strom im MPP)
7. Wert = Pmpp (Leistung im MPP)
Nachdem der gewählte Index mit FUNC:PHOT:REC:IND gesetzt wurde, um den Daten-
satz zu lesen, dauert es eine gewisse Zeit, bis die passenden Daten zu dem Index mit
FUNC:PHOT:REC:DATa? zurückgegeben werden. Anderenfalls schreibt das Gerät einen
Fehler in die Fehler-Queue. Ob die richtigen Daten gelesen wurden, kann durch Vergleich der
gesetzten mit der zurückgegebenen Indexnummer überprüft werden.
Nach dem Start der Simulation berechnet das Gerät die erste PV-Kurve. Das dauert ca. 500
ms. Bereits 100 ms nach Start wird der erste Datensatz der Aufzeichnung erfaßt. Somit sind
die ersten 3-4 Datensätze fehlerhaft. Das ist nicht so, wenn die Aufzeichnung mind. 500 ms
nach dem Start der Simulation gestartet wird.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 81
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.17.4 Statusbefehle
Statusbefehle und solche, die Ergebniswerte von der Simulation auslesen, können zwar jederzeit benutzt werden,
aber die richtige Reihenfolge und Wahl des richtigen Zeitpunkts ist vorteilhafter.
Befehl Beschreibung
FUNCtion:PHOTovoltaics:MPP:VOLTage? Spannung im MPP, in V. Der MPP ergibt sich aus der PV-
Simulationskurve, die sich wiederum aus den eingegebenen
Simulationsdaten ergibt. Die Spannung kann zwischen 0 und
Nennspannung liegen.
FUNCtion:PHOTovoltaics:MPP:CURRent? Strom im MPP, in A. Kann zwischen 0 und Nennstrom liegen.
FUNCtion:PHOTovoltaics:MPP:POWer? Leistung im MPP, in W. Kann zwischen 0 und Nennleistung liegen.
FUNCtion:PHOTovoltaics:STATe? Status der PV-Simulation
STOP = Simulation normal gestoppt (manuell oder Ablauf am
Ende)
RUN = Simulation läuft noch
ERROR MODE = Simulation nicht gestartet wegen Kurvenbe-
rechnungs-Fehler im Simulation-Modus ET oder UI
ERROR DAY = Simulation nicht gestartet wegen Fehler beim
Start im Simulation-Modus DAYET oder DAYUI
ERROR ALARM = Simulation gestoppt durch einen Gerätealarm
ERROR INTERPOLATION = Simulation nicht gestartet wegen
Fehler bei der Verweilzeit im Index 1
FUNCtion:PHOTovoltaics:DAY:NUMBer? Anzahl der gültigen Tagesverlauf-Indexe. Kann bei Übertragung
der Tagesdaten an das Gerät zur Überprüfung genutzt werden,
ob die Indexe in derselben Anzahl angenommen wurden wie
gesendet.
FUNCtion:PHOTovoltaics:OCVoltage? Durch Formel (siehe Norm) berechnete Leerlaufspannung U
OC
(open circuit voltage) des unbelasteten Solar-Paneels. Der
berechnete Wert ist abhängig vom Simulations-Modus, den
Standard-Paneel-Werten (siehe unten) und den Faktoren
FUNCtion:PHOTovoltaics:SCCurrent? Durch Formel (siehe Norm) berechneter Kurzschlußstrom I
SC
(short-circuit current) des Solar-Paneels. Der berechnete Wert ist
abhängig vom Simulations-Modus, den Standard-Paneel-Werten
(siehe unten) und den Faktoren
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 82
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.17.5 Parameterbefehle
Die hier aufgelisteten Befehle dienen zum Setzen oder Auslesen von zur PV-Simulation und Berechnung der PV-Kurve
benötigten Parametern. Dabei ist es wichtig zu beachten, welcher Simulations-Modus (ET, UI, DAYET, DAYUI), welche
Technologie und welcher Eingabemodus (MPP, ULIK) gewählt wurde. Davon ist abhängig, ob bestimmte Parameter
überhaupt setzbar sind bzw. ob sie gesperrt sind und dann vom Gerät automatisch mit Werten laut Norm gefüttert
werden. Die Tabelle gibt daher in einer Matrix an, welcher Parameter in welchem Simulation-Modus schreibbar ist.
Lesbar dagegen sind alle Parameter zu jeder Zeit, haben dann aber u. U. nicht plausible bzw. veraltete Daten.
Befehl Schreibbar in Modus:
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 83
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
PPM KILU NAM
ISC
NIHT
FUNCtion:PHOTovoltaics:FACTor:FFU˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:FFU?
   ─ ─
Füllfaktor Spannung (FF ). Nur im Technologie-Modus MAN veränderbar. Beeinflußt die
U
Berechnung der PV-Kurve nach Formel gemäß Norm. Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:FACTor:FFI˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:FFI?
   ─ ─
Füllfaktor Strom (FF). Nur im Technologie-Modus MAN veränderbar. Beeinflußt die Be-
I
rechnung der PV-Kurve nach Formel gemäß Norm. Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:FACTor:ALPHa˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:ALPHa?
Temperaturkoeffizient α (in 1/°C) für den Kurzschlußstrom. Nur im Technologie-Modus    ─ ─
MAN veränderbar. Beeinflußt die Berechnung der PV-Kurve nach Formel gemäß Norm.
Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:FACTor:BETA˽<NRf>
FUNCtion:PHOTovoltaics:FACTor:BETA?
Temperaturkoeffizient β (in 1/°C) für die Leerlaufspannung. Nur im Technologie-Modus    ─ ─
MAN veränderbar. Beeinflußt die Berechnung der PV-Kurve nach Formel gemäß Norm.
Einstellbereich: -1...<0
FUNCtion:PHOTovoltaics:FACTor:CU˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:CU?
   ─ ─
Korrekturfaktor C für die Leerlaufspannung. Nur im Technologie-Modus MAN veränderbar.
U
Beeinflußt die Berechnung der PV-Kurve nach Formel gemäß Norm. Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:FACTor:CR˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:CR?
Korrekturfaktor C in m²/W für die Leerlaufspannung. Nur im Technologie-Modus MAN    ─ ─
R
veränderbar. Beeinflußt die Berechnung der PV-Kurve nach Formel gemäß Norm.
Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:FACTor:CG˽<NR2>
FUNCtion:PHOTovoltaics:FACTor:CG?
Korrekturfaktor C in W/m² für die Leerlaufspannung. Nur im Technologie-Modus MAN    ─ ─
G
veränderbar. Beeinflußt die Berechnung der PV-Kurve nach Formel gemäß Norm.
Einstellbereich: >0...1
FUNCtion:PHOTovoltaics:STANdard:OCVoltage˽<NR2>
FUNCtion:PHOTovoltaics:STANdard:OCVoltage?
─    
Leerlaufspannung U (open circuit voltage) des zu simulierenden Paneels, in V.
OC
Einstellbereich: 0-Nennspannung
FUNCtion:PHOTovoltaics:STANdard:SCCurrent˽<NR2>
FUNCtion:PHOTovoltaics:STANdard:SCCurrent?
─    
Kurzschlußstrom I (short-circuit current) des zu simulierenden Paneels, in A.
SC
Einstellbereich: 0-Nennstrom
FUNCtion:PHOTovoltaics:STANdard:MPP:VOLTage˽<NR2>
FUNCtion:PHOTovoltaics:STANdard:MPP:VOLTage?  ─   
Spannung im MPP des zu simulierenden Paneels, in V. Einstellbereich: 0-Nennspannung
FUNCtion:PHOTovoltaics:STANdard:MPP:CURRent˽<NR2>
FUNCtion:PHOTovoltaics:STANdard:MPP:CURRent?  ─   
Strom im MPP des zu simulierenden Paneels in A. Einstellbereich: 0-Nennstrom

ModBus & SCPI
5.4.17.6 Steuerungsbefehle
Diese Befehle dienen zur Steuerung der PV-Simulation, üblicherweise nach erfolgter Konfiguration. In bestimm-
ten Modi sind während der Simulation ein oder mehrere Parameter veränderlich, die nach jeder Änderung eine
Neuberechnung der PV-Kurve erfordern, wodurch die vorherige überschrieben wird. Jenachdem ob die Parame-
teränderung den Punkt auf der Kurve betrifft, an dem sich die Simulation befindet, verschiebt er sich nach einer
gewissen Berechnungs- und Reaktionszeit.
Befehl Beschreibung
FUNCtion:PHOTovoltaics:STATe˽{RUN | STOP} Simulation starten oder stoppen
FUNCtion:PHOTovoltaics:STATe? RUN = PV-Kurve wird berechnet und Simulation wird
gestartet, sofern kein Fehler entsteht. Sofern Da-
tenaufzeichnung aktiviert wurde, startet diese auch.
STOP = Simulation und eventuelle Datenaufzeich-
nung werden gestoppt
FUNCtion:PHOTovoltaics:TEMPerature˽<NRf> Nur im Modus ET verfügbar:
FUNCtion:PHOTovoltaics:TEMPerature? Solarmodultemperatur in °C.
Einstellbereich: -40...+80
FUNCtion:PHOTovoltaics:IRRadiation˽<NR1> Nur im Modus ET verfügbar:
FUNCtion:PHOTovoltaics:IRRadiation? Einstrahlungsstärke in W/m².
Einstellbereich: 0-1500
5.4.17.7 Fehlersituationen
Eine Fehlersituation entsteht, wenn die konfigurierte Simulation nicht gestartet werden kann oder wenn
sie bereits gestartet wurde, eine Zeitlang lief und dann unerwartet stoppt. In beiden Fällen kann der Befehl
FUNCtion:PHOTovoltaics:STATe? (siehe Abschnitt 5.4.17.4) helfen, die Ursache zu ermitteln.
Folgendes gilt generell:
• Die Simulation kann nach einem unerwarteten Stopp nicht fortgeführt werden
• Daten der Datenaufzeichnung können während der Simulation oder nach einem unerwarteten Stopp ausgelesen
werden, außer es tritt ein Stromausfall auf
• Sämtliche Konfigurations-Parameter werden nicht gespeichert und sind nach dem Einschalten des Gerätes
auf Standardwerte zurückgesetzt
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 84
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.18 Befehle für die Batterietest-Funktion
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─ ─ ─ ─ (1 ─ ─   ─ ─ ─ ─ ─  ─ 
(1 Außer Serie PSI 9000 DT
Mit Stand 04/2019 ist die in diversen elektronischen Lasten sowie bidirektionalen Netzgeräten durch ein Firmware-
Update installierbare Batterietest-Funktion bei den meisten Serien auch fernsteuerbar. Es sind dabei nahezu
dieselben Möglichkeiten wie bei manueller Bedienung am Gerät vorhanden.
Zusätzlich zu den einzelnen Batterietestmodi für Laden und Entladen bieten Geräte der PSB-Serien einen
kombinierten Modus, genannt "Dynamischer Test". Dieser ist seit 03/2020 für ältere Geräte über eine Firmware-
Aktualisierung verfügbar.
5.4.18.1 Konfigurationsbefehle
Die Konfiguration kann in der Reihenfolge geschehen, wie mit den nachfolgenden Tabellen von oben nach un-
ten gezeigt. Als erstes muß stets der Testmodus gewählt werden. Einzelheiten zu den Batterietest-Modi sind im
Handbuch des Gerätes zu finden.
Befehl Beschreibung
[SOURce:]BATTery:MODe˽{IDLE | STATic | CHARge | Testmodus wählen bzw. den zuletzt gewählten
DYNamic | COMBined} abfragen:
[SOURce:]BATTery:MODe? IDLE = kein Modus gewählt, dient auch zum
Verlassen des Batterietestmodus'
STATic = Modus „Statisches Entladen“ wählen
DYNamic = Modus „Dynamisches Entladen“ wählen
Weitere Modi, nur bei PSB-Serien verfügbar:
CHARge = Modus "Statisches Laden" wählen
COMBined = Dynamischer Test, kombiniert stati-
sches Entladen und statisches Laden
Die nachfolgenden Befehle funktionieren zum Setzen oder Lesen von Werten, nachdem einer der Entlade-Modi
(DYNAMIC oder STATIC) gewählt wurde:
Befehl Beschreibung
[SOURce:]BATTery:CURRent˽<NR2> Nur für den statischen Entlade-Modus:
[SOURce:]BATTery:CURRent? Statischen Entladestrom (in A) setzen. Befehl funk-
tioniert nicht bei Wahl von Modus DYN.
Bereich: 0...I-max
[SOURce:]BATTery:POWer˽<NR3> Für statischen und dynamischen Entlade-Modus:
[SOURce:]BATTery:POWer? Maximale Leistung (in W) setzen. Leistungsbegren-
zung hat Vorrang vor dem Strom, also kann dieser
Werte nach I = P/U den Ladestrom auch unter des-
sen eingestellten Wert (BATT:CURR) begrenzen.
Bereich: 0...P-max
[SOURce:]BATTery:RESistance˽<NR2> Für statischen und dynamischen Entlade-Modus:
[SOURce:]BATTery:RESistance? Schaltet den Widerstandsmodus für den Test ein
oder aus bzw. setzt einen Widerstandswert (in Ω).
Die Widerstandsregelung kann, um den gesetzten
Wert zu erreichen, nach I = U/R auf den gesetzten
Stromsollwert einwirken und den Ladestrom auch
unter dessen eingestellten Wert begrenzen.
NR2 = 0 = Widerstandsmodus aus
NR2 = min. R ... max. R = Widerstand setzen
Die nachfolgenden Befehle sind für beide Entlade-Modi und definieren ein oder mehrere Stopp-Bedingungen, die
den Batterietest automatisch bei Erreichen der Bedingung stoppen können, wenn mindestens eine zutrifft:
Befehl Beschreibung
[SOURce:]BATTery:DISCharge:VOLTage˽<NR2> Entladeschlußspannung (U , in V) setzen. Erreicht
DV
[SOURce:]BATTery:DISCharge:VOLTage? die Batteriespannung diese Schwelle stoppt der
Batterietest.
Bereich: 0...U-max
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 85
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
[SOURce:]BATTery:DISCharge:CAPacity˽<NR2> Max. zu entnehmende Kapazität (in Ah) vorgeben,
[SOURce:]BATTery:DISCharge:CAPacity? bei Erreichen derer der Test stoppen kann bzw. das
Gerät veranlaßt wird, eine Meldung auszugeben.
Bereich: 0...99999.99 Ah
[SOURce:]BATTery:ACTion:CAPacity˽{ NONE | Legt fest, was bei Erreichen des Limit, wie mit
SIGNal | END} BATT:DIS:CAP festgelegt, geschehen soll.
[SOURce:]BATTery:ACTion:CAPacity? NONE = nichts (Limit wird ignoriert)
SIGNal = der Test wird fortgeführt, aber das Gerät
meldet das Erreichen des Limits auf seiner Anzeige
END = der Test wird gestoppt
[SOURce:]BATTery:DISCharge:TIME˽<Time2> Max. Testzeit vorgeben, bei deren Erreichen der Test
[SOURce:]BATTery:DISCharge:TIME? stoppen kann bzw. das Gerät veranlaßt wird, eine
Meldung auszugeben.
Bereich: 00:00:01 ... 10:00:00
[SOURce:]BATTery:ACTion:TIME˽{ NONE | SIGNal | END} Wie BATT:ACT:CAP, hier aber für die max. Testzeit,
[SOURce:]BATTery:ACTion:TIME? wie sie mit BATT:DIS:TIME vorgegeben werden kann
Beim dynamischen Entlade-Modus wird ein gepulster Strom erzeugt, der einem Rechteck mit einstellbarer Ampli-
tude und Tastverhältnis entspricht. Daher wird der Entladestrom für diesen Modus durch mehrere Befehle definiert.
Folgende Befehle funktionieren nur im Modus DYNAMIC:
Befehl Beschreibung
[SOURce:]BATTery:INDex˽<NR1> Wählt einen von 4 Parametern (Bereich: 0...3), aus
[SOURce:]BATTery:INDex? denen sich das Rechteck für den gepulsten Strom
zusammensetzt:
0 = Pegel 1 der Amplitude
Bereich: 0...I-max (Einstellgrenze)
1 = Pegel 2 der Amplitude
Bereich: 0...I-max (Einstellgrenze)
2 = Zeit von Pegel 1
Bereich: 0...36000 s
3 = Zeit von Pegel 2
Bereich: 0...36000 s
[SOURce:]BATTery:PULSe˽<NR2> Setzt oder liest den gesetzten Wert des zuvor mit
[SOURce:]BATTery:PULSe˽<Time3> BATTery:INDex gewählten Indexes. Ströme können
[SOURce:]BATTery:PULSe? im Format <NR2> vorgeben werden, Zeiten für Index
2 und 3 erfordern Format <Time3>
Bei den PSB-Serien, die im Quelle-Betrieb eine Batterie auch laden können, gibt es einen weiteren Testmodus,
den statischen Lade-Modus (CHARGE). Dieser funktioniert wie der statische Entlade-Modus, nur in umgekehrter
Richtung.
Befehl Beschreibung
[SOURce:]BATTery:CHARge:VOLTage˽<NR2> Ladespannung (in V) setzen. Der Wert hängt davon
[SOURce:]BATTery:CHARge:VOLTage? ab, ob eine Vorladung, Starkladung oder Erhaltungs-
ladung ausgeführt werden soll.
Bereich: 0...U-max
[SOURce:]BATTery:CHARge:CURRent˽<NR2> Statischen Ladestrom (in A) setzen. Der Ladestrom
[SOURce:]BATTery:CHARge:CURRent? ist anfangs auf diesen Wert begrenzt, wird ihn später
aber unterschreiten. Bereich: 0...I-max
[SOURce:]BATTery:CHARge:STOP:CURRent˽<NR2> Ladeschlußstrom (in A) setzen. Erreicht der Lade-
[SOURce:]BATTery:CHARge:CURRent? strom diese Grenze, wird der Test beendet.
Bereich: 0...I-max
[SOURce:]BATTery:CHARge:STOP:CAPacity˽<NR2> Max. zu ladende Kapazität (in Ah) vorgeben, bei Er-
[SOURce:]BATTery:CHARge:STOP:CAPacity? reichen derer der Test stoppen kann bzw. das Gerät
veranlaßt wird, eine Meldung auszugeben.
Bereich: 0...99999.99 Ah
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 86
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
[SOURce:]BATTery:CHARge:STOP:TIME˽<Time2> Max. Testzeit vorgeben, bei deren Erreichen der Test
[SOURce:]BATTery:CHARge:STOP:TIME? stoppen kann bzw. das Gerät veranlaßt wird, eine
Meldung auszugeben.
Bereich: 00:00:01 ... 10:00:00
[SOURce:]BATTery:ACTion:CAPacity˽{ NONE | Legt fest, was bei Erreichen des Limit, wie mit
SIGNal | END} BATT:CHAR:STOP:CAP festgelegt, geschehen soll.
[SOURce:]BATTery:ACTion:CAPacity? NONE = nichts (Limit wird ignoriert)
SIGNal = der Test wird fortgeführt, aber das Gerät
meldet das Erreichen des Limits auf seiner Anzeige
bzw. im Batterieteststatus
END = der Test wird gestoppt
[SOURce:]BATTery:ACTion:TIME˽{ NONE | SIGNal | Wie BATT:ACT:CAP, hier aber für die max. Testzeit,
END} wie sie mit BATT:CHAR:STOP:TIME vorgegeben
[SOURce:]BATTery:ACTion:TIME? werden kann
Der sogenannte Dynamische Test (COMBINED), welcher das Laden und Entladen einer mit Batterie kombiniert,
ist nur bei den PSB-Serien verfügbar, da diese Geräte zwischen Quelle- und Senke-Betrieb wechseln können.
Details zum dynamischen Test sind in den Handbüchern der PSB-Serien zu finden.
Da der Test die oben genannten Lade- und Entlade-Modi kombiniert, werden auch deren Befehle genutzt, um die
einzelnen Testabschnitte oder -phasen zu konfigurieren. Damit hier eine Übersicht entsteht, welche Parameter für
den dynamischen Test gesetzt werden müssen, werden in den folgenden Tabellen Befehle von oben teils wiederholt.
Befehle für die Konfiguration der Ladephase, davon ausgehend, es wurde BATTery:MODe˽COMBined gesetzt:
Befehl Beschreibung
[SOURce:]BATTery:CHARge:VOLTage˽<NR2> Ladespannung (in V) setzen. Der Wert hängt davon
[SOURce:]BATTery:CHARge:VOLTage? ab, ob eine Vorladung, Starkladung oder Erhaltungs-
ladung ausgeführt werden soll.
Bereich: 0...U-max
[SOURce:]BATTery:CHARge:CURRent˽<NR2> Statischen Ladestrom (in A) setzen. Der Ladestrom
[SOURce:]BATTery:CHARge:CURRent? ist anfangs auf diesen Wert begrenzt, wird ihn später
aber unterschreiten. Bereich: 0...I-max
[SOURce:]BATTery:CHARge:STOP:CURRent˽<NR2> Ladeschlußstrom (in A) setzen. Erreicht der Lade-
[SOURce:]BATTery:CHARge:CURRent? strom diese Grenze, wird der Test beendet.
Bereich: 0...I-max
[SOURce:]BATTery:CHARge:TIME<Time2> Dauer der Ladephase in Sekunden. Nach Erreichen
[SOURce:]BATTery:CHARge:TIME? der max. Dauer von 10 h wird die Phase beendet.
Bereich: 00:00:01...10:00:00
Befehle für die Konfiguration der Entladephase, davon ausgehend, es wurde BATTery:MODe˽COMBined gesetzt:
Befehl Beschreibung
[SOURce:]BATTery:COMBined:CURRent˽<NR2> Statischen Entladestrom (in A) setzen.
[SOURce:]BATTery:COMBined:CURRent? Bereich: 0...I-max
[SOURce:]BATTery:DISCharge:VOLTage˽<NR2> Entladeschlußspannung (U , in V) setzen. Erreicht
DV
[SOURce:]BATTery:DISCharge:VOLTage? die Batteriespannung diese Schwelle wird die Phase
beendet. Bereich: 0...U-max
[SOURce:]BATTery:DISCharge:TIME<Time2> Dauer der Entladephase in Sekunden. Nach Errei-
[SOURce:]BATTery:DISCharge:TIME? chen der gesetzten Dauer (max. 10 h) wird die Phase
beendet. Alternativ beendet der Ladeschlußstrom
die Phase.
Bereich: 00:00:01...10:00:00
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 87
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehle für die restliche Konfiguration, davon ausgehend, es wurde BATTery:MODe˽COMBined gesetzt:
Befehl Beschreibung
[SOURce:]BATTery:COMBined:STOP:CAPacity˽<NR2> Max. zu ladende und entladende Kapazität (in Ah)
[SOURce:]BATTery:COMBined:STOP:CAPacity? vorgeben, bei Erreichen derer der Test stoppen
kann bzw. das Gerät veranlaßt wird, eine Meldung
auszugeben. Der Wert ist global für beide Phasen.
Bereich: 0...99999.99 Ah
[SOURce:]BATTery:COMBined:STOP:TIME˽<Time2> Max. Testzeit vorgeben, bei deren Erreichen der
[SOURce:]BATTery:COMBined:STOP:TIME? Test stoppen kann bzw. das Gerät veranlaßt wird,
eine Meldung auszugeben. Der Wert ist global für
beide Phasen.
Bereich: 00:00:01 ... 10:00:00
[SOURce:]BATTery:ACTion:CAPacity˽{ NONE | Legt fest, was bei Erreichen des Limits, wie mit
SIGNal | END} BATT:COMB:STOP:CAP festgelegt, geschehen soll.
[SOURce:]BATTery:ACTion:CAPacity? NONE = nichts (Limit wird ignoriert)
SIGNal = der Test wird fortgeführt, aber das Gerät
meldet das Erreichen des Limits auf seiner Anzeige
bzw. im Batterieteststatus
END = der Test wird gestoppt
[SOURce:]BATTery:ACTion:TIME˽{ NONE | SIGNal | Wie BATT:ACT:CAP, hier aber für die max. Testzeit,
END} wie sie mit BATT:COMB:STOP:TIME vorgegeben
[SOURce:]BATTery:ACTion:TIME? werden kann
[SOURce:]BATTery:COMBined:TIME˽<Time3> Pausezeit zwischen den Phasen, in Sekunden.
[SOURce:]BATTery:COMBined:TIME? Bereich: 1...36000
[SOURce:]BATTery:COMBined:STARt˽{CHARge | Legt fest, mit welcher der beiden Phasen, Laden
DISCharge} (CHARge) oder Entladen (DISCharge), der Test be-
[SOURce:]BATTery:COMBined:STARt? gonnen wird. Nach Beendigung einer Phase wird in
die jeweils andere gewechselt. Somit werden beiden
Phasen immer mind. 1x durchlaufen.
[SOURce:]BATTery:COMBined:CYCLes˽<NR1> Legt fest, wie oft der Dynamische Test beide Phasen
[SOURce:]BATTery:COMBined:CYCLes? durchläuft. Der Test an sich stoppt nur bei Erreichen
der definierten Anzahl von Durchläufen oder Errei-
chen eines der beiden anderen Stoppkriterien.
Bereich: 0 (unendlich) oder 1...999
5.4.18.2 Steuerungs- und Zustandsbefehle
Nach der Moduswahl und Konfiguration der erforderlichen Parameter kann der Test gestartet werden. Solange
kein unerwartetes Ereignis wie z. B. ein Gerätealarm auftritt, wird der Test durchlaufen bis eine der definierten
Stopp-Bedingungen erreicht wurde.
Befehl Beschreibung
[SOURce:]BATTery:STATe˽{ RUN | STOP } Startet den Test bzw. stoppt ihn jederzeit vor Erreichen einer
[SOURce:]BATTery:STATe? Stopp-Bedingung.
RUN = Test starten
STOP = Test sofort stoppen
[SOURce:]BATTery:CONDition? Abfrage des Testzustandes. Dies ist jederzeit möglich, also vor,
während und nach dem Test. Mögliche Rückgaben:
IDLE = Test ist noch nicht gestartet bzw. wurde gestoppt (manuell
oder durch Alarm)
RUN = Test läuft momentan
FINISHED = Test normal beendet
ERROR = Test beendet durch Gerätealarm
Weitere Zustände:
SIGNAL AH = Eingestellte, max. zu entnehmende Anzahl Ah
erreicht, Test läuft weiter
SIGNAL TIME Eingestellte, max. Testzeit erreicht, Test läuft
weiter
END AH = Eingestellte, max. Anzahl Ah erreicht, Test beendet
END TIME = Eingestellte, max. Testzeit erreicht, Test beendet
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 88
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Befehl Beschreibung
Weitere Zustände (nur verfügbar bei bidirektionalen Geräten):
RUN, CHARGING = Test läuft momentan in der Ladephase
RUN, DISCHARGING = Test läuft momentan in der Entladephase
RUN, RESTING = Test pausiert momentan zwischen den La-
dephasen
5.4.18.3 Auswertungsbefehle
Nach dem Testende können noch ein paar Werte ausgelesen werden, die das Testergebnis repräsentieren.
Befehl Beschreibung
[SOURce:]BATTery:TEST? Fragt das Testergebnis ab. Das Gerät sollte einen String mit drei
Werten zurückliefern. Die Abfrage kann auch während des Tests
erfolgen:
1. Gesamte entladene und/oder geladene Batteriekapazität in Ah
2. Gesamte entnommene und/oder zugeführte Energie in Wh
3. Tatsächliche Batterietest-Zeit im Format <Time2>
[SOURce:]BATTery:TEST {RESet | Zurücksetzen aller oder einzelner Ergebniswerte. Kann genutzt
RESETAH | RESETWH | RESETTIME} werden, um zwischen mehreren Testläufen die Werte zu nullen.
Verlassen und Wiedereintritt in den Batterietestmodus hat den-
selben Effekt.
RESet = setzt alles auf Null zurück
RESETAH = setzt nur den Ah-Wert auf Null
RESETWH = setzt nur den Wh-Wert auf Null
RESETTIME = setzt nur den Zeitzähler auf Null
5.4.18.4 Tipps und Hinweise
• Entladene Batteriekapazität wird nicht von der geladenen abgezogen, ebenso bei der Energie.
• Um während eines langen Dynamischen Tests den Zwischenstand von Ah und Wh einer Phase oder eines
Durchlaufs zu ermitteln, könnten sie z. B. während der Ruhepause vor und nach einem Testabschnitt ausge-
lesen und die Differenz berechnet werden.
• Wenn die 10 h maximale Dauer einer Phase beim Dynamischen Test nicht ausreichen, kann der Dynamische
Test auch anders umgesetzt werden. Man müßte die Ablaufsteuerung dann in die eigene Software auslagern
und am Gerät nur "Statisches Laden" und "Statisches Entladen" separat konfigurieren und mit Wartezeiten
kombinieren. Die einzelnen Tests können theoretisch endlos lang laufen.
• Der sogenannte "dynamische Test", wie nur verfügbar bei bidirektionalen Geräten, kombiniert eine oder mehrere
Lade- und Entladephasen in einem Ablauf. Die dabei gezählten Ah- und Wh-Werte werden in beiden Phasen
hochgezählt. Es ist daher nicht möglich am Ende die tatsächlich an die Batterie abgegebene Kapazität bzw.
Energie zu erhalten.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 89
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.19 Spezifische Befehle und Syntax bei Serie PS 2000 B TFT
5.4.19.1 Sonderbefehle
Befehl Beschreibung
SYSTem:CONFig:TRACking˽{ ON | OFF } Aktiviert bzw. deaktiviert den sog. Tracking-Modus der
SYSTem:CONFig:TRACking? Triple-Modelle (siehe Gerätehandbuch PS 2000 B TFT
Triple). Es gelten dieselben Gegebenheiten wie bei der
manuellen Bedienung des Tracking-Modus, d. h. bei
aktiviertem Modus kann man den zweiten Ausgang nicht
separat steuern, sondern nur auf ihn bezogene Werte
auslesen.
5.4.19.2 Erweitertes Befehlsformat
Die Serie PS 2000 B TFT bietet Modelle mit zwei separaten Leistungsausgängen (Triple-Modelle), die man ge-
trennt ansteuern kann. Während das bei ModBus einfach durch die Verwendung unterschiedlicher Slave-Adressen
erfolgt, muß man bei SCPI andere Wege gehen. Der SCPI-Standard läßt die Verwendung eines Selektors zu, der
für bestimmte Befehle auswählt, für welchen Ausgang der Befehl gilt. Dieser Selektor ermöglicht es sogar, nicht
nur den einen oder anderen Ausgang anzusteuern, sondern auch beide gleichzeitig.
Dabei gilt:
• Wird kein Selektor verwendet, geht ein Befehl immer an Ausgang 1 (linke Anzeige)
• PS 2000 B TFT Single-Modelle benötigen keinen Selektor, unterstützten aber der Logik wegen Selektor (@1),
reagieren auf Befehle mit Selektor (@2) jedoch nicht bzw. mit einem Fehler
Übersicht der Selektoren und Kombinationen:
Selektor Beschreibung
(@1) Befehl geht nur an Ausgang 1 (gleichbedeutend mit einem Befehl ohne Selektor)
(@2) Befehl geht nur an Ausgang 2
(@1,2) oder (@1:2) Befehl geht an Ausgang 1 und 2 gleichzeitig
Befehle, die Selektion des Ausgangs bei Triple-Modellen erfordern:
Schreiben Abfragen
MEASURE[:SCALAR]:CURRENT[:DC]?
MEASURE[:SCALAR]:POWER[:DC]?
MEASURE[:SCALAR]:VOLTAGE[:DC]?
OUTPUT[:STATE] OUTPUT[:STATE]?
[SOURCE:]CURRENT [SOURCE:]CURRENT?
[SOURCE:]CURRENT:PROTECTION[:LEVEL] [SOURCE:]CURRENT:PROTECTION[:LEVEL]?
[SOURCE:]CURRENT:LIMIT:HIGH [SOURCE:]CURRENT:LIMIT:HIGH?
[SOURCE:]VOLTAGE [SOURCE:]VOLTAGE?
[SOURCE:]VOLTAGE:PROTECTION[:LEVEL] [SOURCE:]VOLTAGE:PROTECTION[:LEVEL]?
[SOURCE:]VOLTAGE:LIMIT:HIGH [SOURCE:]VOLTAGE:LIMIT:HIGH?
SYSTEM:LOCK SYSTEM:LOCK:OWN?
Der Selektor wird immer am Ende eines Befehls angehängt, wobei man unterscheidet zwischen Schreibbefehlen
und Anfragebefehlen. Schreibbefehle erfordern eine Trennung mit Komma.
Beispiele zur Syntax für die Selektion des Ausgangs:
Befehl Aktion
VOLT 29,(@1) Setzt 29 V für Ausgang 1, hat denselben Effekt wie VOLT 29
CURR?˽(@2) Fragt den Stromsollwert von Ausgang 2 ab -> Achtung, das Leerzeichen
muß verwendet werden, ansonsten kommt ein Syntaxfehler!
SYST:LOCK ON,(@1:2) Schaltet Ausgang 1 und 2 gleichzeitig auf Fernsteuerung um -> sollte die-
ser Befehl bei einem Single-Modell angewendet werden, hat der Fehler,
der dadurch erzeugt wird, Vorrang und es würde nicht in Fernsteuerung
wechseln
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 90
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.19.3 Ausgangsbezogene Rückgaben
Ebenso wie es erforderlich ist bei den Triple-Modellen bestimmte Befehle einem der beiden Ausgänge zuzuord-
nen, muß man bei Rückgaben wie z. B. einer Fehlermeldung unterscheiden können, von welchem Ausgang sie
kommen. Das betrifft jedoch nur Kommunikationsfehler, wie man sie mit SYST:ERR:ALL? abfragt. Diese sind
daher zwecks Verarbeitung gekennzeichnet. Beispiel: -221,"Settings conflict;@2" kam vom Gerät. Selektor @2
kennzeichnet den Fehler als dem Ausgang 2 zugehörig.
Bei anderen Rückgaben wird kein Selektor verwendet, es gilt aber eine gewisse Logik:
• VOLT?˽(@2) gibt z. B. 20.45V zurück, aber ohne Selektor, da die Antwort direkt auf die Anfrage erfolgt, die
explizit an Ausgang 2 ging
• MEAS:ARR?˽(@1:2) gibt sechs kommagetrennte Istwerte zurück, wovon die ersten drei zu Ausgang 1 gehören
und die zweiten drei zu Ausgang 2; auch hier gibt es keine extra Zuordnung durch einen Selektor
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 91
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.4.20 Spezifische Befehle bei Serie EL 3000 B
Die sog. 3000er Serien unterstützen auch SCPI, wobei die Standardbefehle identisch mit denen anderer Serien
sind. Ein spezielles Feature, das es so nur bei der Serie EL 3000 B gibt, ist der Rampengenerator. Man kann ihn
deshalb auch als Funktionsgenerator für Standardfunktionen wie Rechteck, Dreieck oder Trapez betrachten. Eine
Besonderheit bei dem Rampengenerator ist, daß dieser zur Laufzeit der Funktion im Hintergrund neu konfiguriert
und mit der geänderten Konfiguration durch einen Trigger-Befehl irgendwo innerhalb des momentan generierten
Verlaufs neu gestartet werden kann. Das grundlegende Konzept ist, daß der Generator konfiguriert wird und nach
dem Start im Gerät automatisch abläuft. Da die Daten nicht gespeichert werden, muß der Generator nach dem
Einschalten des Gerätes mindesten einmal neu konfiguriert werden muß, was auch bedeutet, das Gerät kann nicht
ohne eine Steuerung auskommen.
5.4.20.1 Konfigurationsbefehle für den Rampengenerator
Der Rampengenerator kann,wie beim Funktionsgenerator anderer Serien, entweder auf den Strom oder die
Spannung zugewiesen werden. Der jeweils andere Wert bleibt dann statisch, ebenso die Leistung. Er basiert
auf Rampen, die durch mehrere Zeiten für Anstieg/Abfall, sowie zwei Pegel definiert werden. Das bedeutet, man
benötigt nur wenige Befehle insgesamt für die Konfiguration. Verdeutlichung der Zuordnung:
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 92
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de
1
legeP
A
t
t1
2
legeP
Pegel 1: unterer Pegel
Pegel 2: oberer Pegel
t1 = Verweilzeit am unteren Pegel
t2 = Zeit für die ansteigende Rampe
t3 = Verweilzeit am oberen Pegel
t4 = Zeit für die abfallende Rampe
t4 t2 t3 t4
Befehl Beschreibung
[SOURce:]FUNCtion:RAMP:SELect˽{VOLTage | Wählt die Zuweisung der Rampengeneration zur Spannung
CURRent | NONE} (VOLTage) oder Strom (CURRent) oder keins von beidem
[SOURce:]FUNCtion:RAMP:SELect? (NONE) bzw. fragt die gesetzte Zuweisung ab. Dieser Befehl
muß immer als erstes gesendet werden, soll die Konfiguration
geschrieben werden, sowie auch zum Lesen.
[SOURce:]FUNCtion:RAMP:INDex˽{0...3} Wählt einen der 6 Parameter, die konfiguriert werden müssen.
[SOURce:]FUNCtion:RAMP:INDex? 0 = Unterer Pegel P1 und Zeit t1 (Anstieg P1->P2)
1 = Oberer Pegel P2 und Zeit t2 (Haltezeit von P2)
4 = Zeit t3 (abfallende Flanke, P2 -> P1)
3 = Zeit t4 (Haltezeit von P1)
Der obere Pegel ist für eine ansteigende Rampe der Endpunkt,
sowie für eine abfallende Rampe der Anfangspunkt. Umgekehrt
dann für den unteren Pegel. Der Pegel an sich wird mit dem
:OFFSet-Parameter definiert, daher muß der zu setzende Pegel
vorher gewählt werden. Die Zeiten verteilen sich pro Pegel auf
zwei Indexe und werden mit dem :TIMe-Befehl gesetzt.
[SOURce:]FUNCtion:RAMP:OFFSet˽<NR2> Funktioniert nur mit den Indexen 0 und 1, wie oben beschrieben.
[SOURce:]FUNCtion:RAMP:OFFSet? Legt den Pegel der Spannung oder des Stromes in Prozent vom
Nennwert fest, je nach Wahl der Zuweisung mit :SELect. Der
Wertebereich ist hier 0...100% von U bzw. 0...I
Nenn Nenn
[SOURce:]FUNCtion:RAMP:TIMe˽<NR1> Definiert die vorher mit :INDex gewählte Zeit. Der Wert wird in
[SOURce:]FUNCtion:RAMP:TIMe? Mikrosekunden angegeben, Bereich: 10 μs ... 6.000.000.000
μs (6 Milliarden), was 100 Minuten entspricht. Außerdem gibt
es eine technisch bedingte Schrittweite von 10, so daß
Zeitwerte die kein glattes Vielfaches von 10 sind auf- oder
abgerundet werden, wenn der Wert intern geschrieben
wird. Die Gesamtzeit aller Zeiten darf 100 Minuten nicht über-
schreiten. Eine der vier Zeiten kann auf genau 100 Minuten
gesetzt werden, wenn die anderen drei auf das Minimum von
10 μs gesetzt sind.

ModBus & SCPI
Hinweise zur Konfiguration:
• Die Reihenfolge der Wahl der 6 Indexe ist nicht vorgegeben
• Sollte P1 größer sein als P2 wird die generierte Kurve invertiert
5.4.20.2 Steuerung des Rampengenerators
Nach der Konfiguration kann direkt gestartet werden. Dabei steht dem Anwender zur Wahl zuerst den DC-Eingang
einzuschalten oder zuerst die Funktion zu starten (Direktstart), was den DC-Eingang automatisch mit einschaltet.
Der Unterschied zum Direktstart ist der, daß die Last vor dem Start der Funktion noch für eine gewisse Zeit statisch
arbeiten würde.
Befehl Beschreibung
[SOURce:]FUNCtion:RAMP:STATe˽{RUN | STOP} Startet die Funktion mit RUN bzw. stoppt sie mit STOP
[SOURce:]FUNCtion:RAMP:STATe? jederzeit während des Ablaufs.
[SOURce:]FUNCtion:RAMP:TRIGger˽{TRIGger} Löst die Übernahme einer im Hintergrund und zur Laufzeit
des Generators geladenen, neuen Konfiguration über-
gangslos aus, also ohne den Generator zu stoppen. Das
vermeidet Lücken im Ablauf. Falls die steuernde Software
eine Zeiterfassung des Ablaufs ab Start hat, kann das
Triggern auch zeitlich so günstig plaziert werden, daß es
genau am Ende eines Kurvenablaufs stattfindet.
Progammierbeispiele sind in „5.5.5. Programmierbeispiele zum Rampengenerator der Serie EL 3000 B“ zu finden.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 93
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.5 Beispielanwendungen
5.5.1 Master-Slave über SCPI konfigurieren und steuern
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─  ─ ─ ─ ─   ─ ─     
Die Geräte, die echtes Master-Slave (kurz: MS) mit Summenbildung über einen dedizierten Master-Slave-Bus
bieten, unterstützen auch die komplette, ferngesteuerte Konfiguration und Bedienung. Bei einem MS-System
steuert man üblicherweise nur den Master fern, die Slaves sind normalerweise nicht mit dem PC verbunden,
außer vielleicht bei der Konfiguration zum Slave an sich. Daher wird empfohlen, die komplette Konfiguration am
Bedienfeld der Geräte zu erledigen und nur die spätere Bedienung in die Fernsteuerungs-Software auszulagern.
Wenn man es am Gerät durchführt, können später trotzdem der Status der Initialisierung oder die Anzahl der
Geräte im MS-Verbund von der Software ausgelesen und überprüft werden. Die Initialisierung, die vom Master
nach dem Einschalten der Geräte automatisch mindestens einmal ausgeführt wird, läßt sich auch per Software
starten bzw. beliebig wiederholen.
Annahme: es sind fünf Netzgeräte PSI 9080-510 3U (80 V, 510 A, 15 kW) im MS parallelzuschalten. Der Master
muß sich nach Konfiguration und erfolgreicher Initialisierung als ein Gerät mit den Nennwerten 80 V, 2550 A und 75
kW, sowie 1 Ω (max. Widerstand) darstellen. Diese Werte sind gleichzeitig auch die neuen, temporären Nennwerte
des MS-Systems. Wie bei manueller Bedienung sind dann Sollwerte und Limit-Werte im Bereich 0...102%, sowie
Schutzwerte im Bereich 0...110% (die meisten Serien) bzw. 0...103% (bestimmte Lastserien) zulässig.
Die beispielhafte Schritt-für-Schritt-Anleitung unten besteht aus mehreren Teilen, weil manche davon optional sind.
Teil 1a: Den Master konfigurieren
1. Fernsteuerung aktivieren: SYST:LOCK˽ON
2. MS aktivieren: SYST:MS:ENABLE˽ON
3. Gerät als Master definieren: SYST:MS:LINK˽MASTER
4. (Falls Zwei-Quadranten-Betrieb gefahren wird und der Master eine elektronische Last ist)
Die Master-Last als Share-Bus-Slave definieren: SYST:SHAR:LINK˽SLAVE
Teil 1b: Den Slave bzw. die Slaves konfigurieren, falls mit Steuereinheit (PC, SPS usw.) verbunden
5. Fernsteuerung aktivieren: SYST:LOCK˽ON
6. MS aktivieren: SYST:MS:ENABLE˽ON
7. Gerät als Slave definieren: SYST:MS:LINK˽SLAVE
Schritte 5-7 für weitere Slaves wiederholen.
Teil 2: Das MS-System initialisieren
8. Fernsteuerung aktivieren, falls Schritte 1-7 nicht nötig waren, weil bereits konfiguriert: SYST:LOCK˽ON
9. Initialisierung starten, danach einige Sekunden warten: SYST:MS:INIT
Teil 3: Weitere, optionale Schritte
10. Den Status der Initialisierung abfragen, um ihn ggf. auszuwerten: SYST:MS:COND?
11. Die Anzahl der initialisierten Geräte abfragen (sollte in dem Beispiel 5 sein): SYST:MS:UNIT?
12. Nennwert des Stromes des MS-Systems abfragen: SYST:NOM:CURR?
13. Nennwert der Leistung des MS-Systems abfragen: SYST:NOM:POW?
14. Maximalen Widerstand des MS-System anfragen: SYST:NOM:RES:MAX?
15. Minimalen Widerstand des MS-System anfragen: SYST:NOM:RES:MIN?
16. Schutzwerte konfigurieren, hier beispielsweise OVP: VOLT:PROT˽70
17. Events konfigurieren
• z. B. OCD auf 2100 A setzen: SYST:CONF:OCD˽2100
• Alarmtyp für OCD festlegen (Typ Warnung): SYST:CONF:OCD:ACT˽WARNING
Die Einstellgrenzen (Limits) sind nach der Initialisierung auf Maximum, einige Sollwerte wie der Strom aber auch.
Man muß hier also bedenken, den zugehörigen Sollwert erst runterzusetzen, sonst kann man den zugehörigen
Limit-Wert nicht verändern.
18. Einstellgrenzen verkleinern, z. B. für den Ausgangsstrom die obere Grenze auf 2200 A, dazu:
• Stromsollwert auf 0 bzw. auf die untere Grenze setzen: CURR˽MIN
• Obere Grenze auf 2200 A setzen: CURR:LIM:HIGH˽2200
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 94
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Hier ist der Strom nun zunächst auf 0 gesetzt, bis 2200 A einstellbar, wird aber durch OCD auf 2100 A überwacht.
Sprich, würde man den Strom per Befehl auf über 2100 A setzen und dieser fließt irgendwann tatsächlich, würde
OCD ausgelöst. In dem Fall erfolgt keine Abschaltung des Ausgangs, weil der Aktionstyp „Warnung“ gesetzt wurde.
19. DC-Ausgang einschalten, um mit dem System zu arbeiten: OUTP˽ON
Ein so konfiguriertes System bleibt über das Ausschalten des Gerätes hinweg konfiguriert. Der Master muß nach
dem Einschalten aller Slaves das MS-System nur mindestens einmal neu initialisieren. Der Status der automa-
tischen Initialisierung nach dem Einschalten kann per Software ausgelesen und dementsprechend gehandelt
werden, indem die obigen Schritte ab zumindest 8, vielleicht auch ab 1 erneut ausgeführt werden, wenn nötig.
5.5.2 Programmier-Beispiele zum Funktionsgenerator
5.5.2.1 Allgemeine Befehlsabfolge für den Arbiträrgenerator
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─  ─  ─  ─ ─ ─ ─   ─ 
Angenommen, man möchte eine Sinuskurve mit Amplitude 30 A und Frequenz 10 Hz für 60 Sekunden auf den
Eingangsstrom einer elektronischen Last anwenden. Dazu reicht es, nur einen von den 99 Sequenzpunkten zu
beschreiben, beispielsweise Nummer 12. Da es hier um DC-Strom geht, benötigt die Amplitude auch einen Offset.
Allgemein ist bei einer Sinuskurve die Amplitude der Abstand zwischen Spitze und Mittellinie, welcher hier durch
Start(DC) und End(DC) definiert wird. Siehe dazu auch das Gerätehandbuch bzw. Abschnitt 5.4.12.5. Demzufolge
muß der Offset, welcher die Mittellinie ergibt, auch mindestens 30 A betragen. Für das Beispiel nehmen wir 50 A.
Es ergibt sich später also ein sinusförmiger, zwischen 20 A und 80 A wechselnder DC-Eingangsstrom.
Mit der Sinuskurve wird AC-Verhalten des DC-Eingangsstroms nachgebildet, daher wären nach der Tabelle in
5.4.12.5 mindestens die Indexe 0, 1, 2, 3, 5, 6 und 7 zu beschreiben. Sofern kein bestimmter Startwinkel benötigt
wird, kann Index 4 weggelassen werden, da standardmäßig auf 0° gesetzt.
Das Setzen der globalen Sollwerte auf ihr Maximum oder einen anderen sinnvollen Wert ist
auch bei Verwendung des Funktionsgenerators immer erforderlich. Das gilt besonders, wenn
mehrere Geräte im Master-Slave arbeiten. Dort begrenzen diese Sollwerte auch die Slaves.
Für das Schreiben von Sequenzpunktdaten in den Arbiträrgenerator gelten folgende Regeln:
• Soll der AC-Anteil eine Sequenzpunkts genutzt werden (Sinuskurvenerzeugung), dann müssen die DC-Werte
vor den AC-Werten geschickt werden
• Werden Rampen programmiert, d .h. DC-Start und DC-Ende sind nicht gleich, dann wird eine min. Steigung
(Verhältnis von Änderung des Wertes und Zeit) erwartet oder die Daten werden abgelehnt; bei 10000er Serien
ab einer bestimmten Firmwareversion ist diese Einschränkung nicht mehr vorhanden -> Hinweis: sollte beim
Laden der Sequenzpunktdaten ein Fehler zurückgegeben werden, so liegt dieser mit großer Wahrscheinlichkeit
an einer unzureichenden Steigung
• Die Zeit des Sequenzpunkt muß als letzer Wert geschrieben werden, weil er eine Überprüfung der min. Stei-
gung auslöst.
Befehlsabfolge (Annahme: Gerät ist bereits in Fernsteuerung):
Nr. Befehl Beschreibung Register
1 FUNC:GEN:SEL CURR Wählt Arbiträrgenerator für Strom. Ab hier befindet sich das Gerät 852
im Funktionsgenerator-Modus
2 FUNC:GEN:WAVE:LEV˽12 Wählt die 12. Sequenz zum Schreiben aus 1092
3 FUNC:GEN:WAVE:IND˽5 Index 5 wählen: Startwert DC-Anteil bzw. Offset AC-Anteil
4 FUNC:GEN:WAVE:DAT˽50 Offset auf 50 A setzen 1092
5 FUNC:GEN:WAVE:IND˽6 Index 6 wählen: Endwert DC-Anteil bzw. Offset AC-Anteil
6 FUNC:GEN:WAVE:DAT˽50 Offset auf 50 A setzen. Wenn sich der Offset über den Zeitraum 1092
des Ablaufs nicht ändern soll, so muß Endwert = Startwert ge-
setzt werden.
7 FUNC:GEN:WAVE:IND˽2 Index 2 wählen: Startfrequenz
8 FUNC:GEN:WAVE:DAT˽10 Startfrequenz auf 10 Hz setzen 1092
9 FUNC:GEN:WAVE:IND˽3 Index 3 wählen: Endfrequenz
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 95
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Nr. Befehl Beschreibung Register
10 FUNC:GEN:WAVE:DAT˽10 Endfrequenz auf 10 Hz setzen. Wenn sich die Frequenz über 1092
den Zeitraum des Ablaufs nicht ändern soll, so muß Endwert =
Startwert gesetzt werden.
11 FUNC:GEN:WAVE:IND˽0 Index 0 wählen: Startwert AC-Anteil (Amplitude)
12 FUNC:GEN:WAVE:DAT˽30 Amplitude auf 30 A setzen 1092
13 FUNC:GEN:WAVE:IND˽1 Index 1 wählen: Endwert AC-Anteil (Amplitude)
14 FUNC:GEN:WAVE:DAT˽30 Amplitude auf 30 A setzen. Wenn sich die Amplitude über den 1092
Zeitraum des Ablaufs nicht ändern soll, so muß Endwert = Start-
wert gesetzt werden.
15 FUNC:GEN:WAVE:IND˽7 Index 7 wählen: Dauer der Sequenz
16 FUNC:GEN:WAVE:DAT˽60 Ablaufdauer auf 60 s festlegen 1092
17 FUNC:GEN:WAVE:END˽12 Endsequenzpunkt auf 12 festlegen 860
18 FUNC:GEN:WAVE:STAR˽12 Startsequenzpunkt auf 12 festlegen 859
19 FUNC:GEN:WAVE:NUM˽1 Setze die Anzahl der Durchläufe auf 1, weil der eine Sequenz- 861
punkt allein schon 60 s läuft. Alternativ könnte man auch die
Dauer des Sequenzpunkts auf 1 s festlegen und 60 Durchläufe
wählen.
20 FUNC:GEN:WAVE:SUBM Lädt die zuvor gesetzten Werte in den Funktionsgenerator
Nun sollten noch die drei globalen Sollwerte gesetzt werden, bei manueller Bedienung „U/I/P Limits“ genannt,
damit nicht irgendwelche vorher mal eingestellten Werte die generierte Funktion durch unerwartete Begrenzung
verfälschen.
Wichtig für Master-Slave-Systeme: die Slaves selbst haben die programmierte Funktion nicht
laufen, denn sie werden durch den Master über den Share-Bus gesteuert. Damit diese wie
erwartet mitarbeiten, ist es zwingend nötig, diese globalen Sollwerte an den Master zu senden,
der sie an die Slaves weitergibt.
Für dieses Beispiel mit einer Stromsenke (el. Last) empfiehlt es sich, die Spannung auf 0 V, die Leistung auf Ma-
ximum und den Strom auf mindestens 105% des Spitzenwertes der Sinuskurve zu setzen:
Nr. Befehl Beschreibung Register
21 VOLT˽0 Spannung auf 0 V setzen, damit die auf den Strom angewendete 500
Sinuskurve sauber im Stromregelmodus zwischen Minimum und
Maximum pendeln kann
22 POW˽MAX Leistungssollwert mit MAX unabhängig vom Gerätemodell setzen 502
(498)
Der Funktionsgenerator ist nun konfiguriert und Sequenz 12 geladen. Jetzt kann er gestartet und ferngesteuert
bedient werden:
Nr. Befehl Beschreibung Register
23 INP˽ON Einschalten des DC-Eingangs bzw. des DC-Ausgangs, je nach 405
OUTP˽ON Gerätetyp
24 FUNC:GEN:WAVE:STAT˽RUN Starten des Funktionsablaufs mit RUN. Dieser stoppt nach 60 s 850
25 FUNC:GEN:WAVE:STAT˽STOP Optional: die Funktion kann jederzeit gestoppt werden. Der DC- 850
Eingang/-Ausgang bleibt danach zunächst eingeschaltet und
kann mit dem entsprechenden Befehl ausgeschaltet werden
26 FUNC:GEN:SEL˽NONE Optional: Funktionsgenerator mit NONE wieder verlassen. 852
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 96
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.5.2.2 Befehlsabfolge für den XY-Generator
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─ ─ ─  ─  ─ ─ ─ ─   ─ 
Die Konfiguration und das Laden von Tabellenwerten für den XY-Generator gestalten sich ähnlich wie beim Arbi-
trärgenerator. Angenommen, Sie möchten den Eingangsstrom einer elektronischen Last in Abhängigkeit von der
DC-Eingangsspannung bestimmen. Dafür eignet sich der XY-Generator mit der IU-Funktion sehr gut.
Über die zu ladende IU-Tabelle bestimmen Sie das Verhalten des Eingangsstromes über den gesamten Eingangs-
spannungsbereich hinweg und könnten somit festlegen, daß z. B. unter ein gewissen Spannung gar kein Strom
fließt (Tabellenwerte mit 0 A) oder daß der Strom ab einer gewissen Spannung linear und daher proportional zur
Eingangsspannung ansteigt. Die Stromkurve, die diesem Verhalten entspricht, kann man z. B. in Excel oder ähnlich
erstellen, grafisch darstellen lassen und auch als CSV-Datei speichern, für die Verwendung am HMI des Gerätes.
Der Meßbereich für die Führungsgröße ist auf 0...125% festgelegt, auch wenn manche elektronischen Lasten
bereits ab 103% Eingangsspannung wegen Überspannung abschalten würden. Bei Netzgeräten hingegen sind
niemals mehr als 100% Spannung machbar. Die abhängige Größe, I oder U, kann daher nur zwischen 0...100%
gesetzt werden, somit ist bei Tabelleneintrag 3276 (4096/1,25) bereits 100% für die abhängige Größe erreicht.
Somit können alle Tabellenwerte oberhalb Index 3276 auch auf dem Wert wie in 3276 bleiben.
Weiterhin gilt zu beachten, daß das Gerät aufgrund der globalen, einstellbaren Leistungsbegrenzung nicht 100%
Strom bei 100% Spannung machen kann. Wenn also Tabellen erzeugt werden, wäre es vielleicht sinnvoll, zwei
zusätzliche Spalten anzulegen, die später nicht in das CSV exportiert werden. Eine, in welcher der Meßbereich
0...125% der Führungsgröße mit Werten befüllt auf die 4096 Werte verteilt wird, und eine andere, wo für jeden
Tabelleneintrag die Leistung nach P = U * I berechnet und mit dem Nennwert des jeweiligen Modells verglichen
wird, um so Einträge zu erkennen, die vom Gerät nicht umsetzbar wären.
Es ist Vorsicht geboten bei großen Wertänderungen zwischen zwei oder mehreren aufeinander-
folgenden Tabelleneinträgen! Es empfiehlt sich, diese Einträge mit „sanft“ ansteigenden oder
abfallenden Werten zu versehen.
Nr. Befehl Beschreibung Register
1 FUNC:GEN:SEL˽IU Wähle XY-Generator als IU-Funktion, also I = f(U). Ab hier be- 855
Außerdem für PSB-Serien: findet sich das Gerät im Funktionsgenerator-Modus.
FUNC:GEN:SEL˽IUPS IU-Tabelle nur im Quelle-Betrieb 856
FUNC:GEN:SEL˽IUEL IU-Tabelle nur im Senke-Betrieb 856
2 FUNC:GEN:XY:LEV˽0 Wählt Tabelleneintrag 0 zum Schreiben aus 2600
3 FUNC:GEN:XY:DAT˽0 Stromwert für Tabelleneintrag 0 schreiben, hier: 0 A (Beispiel- 2600
wert)
...
8192 FUNC:GEN:XY:LEV˽3276 Wählt Tabelleneintrag 3276 zum Schreiben aus 5875
8193 FUNC:GEN:XY:DAT˽120 Stromwert für Tabelleneintrag 3276 schreiben, hier: 120 A 5875
(Beispielwert)
8194 FUNC:GEN:XY:SUBM Alles übernehmen
Nun sollten noch die Sollwerte gesetzt werden, die durch die Tabelle nicht beeinflußt werden, weil die Funktion
ansonsten wirkungslos ablaufen würde. Sprich, wenn eine UI-Tabelle geladen ist, wird die Spannung durch die
Tabelle beeinflußt, aber Strom und Leistung sind jedoch statisch und haben irgendwelche vormals gesetzten Werte.
Bei einer IU-Tabelle sind dann Spannung und Leistung statisch. Die Sollwerte, die man hier setzen kann, sind
beliebig, sollten aber die Funktion nicht stören, daher empfiehlt es sich, sie auf ihr Maximum zu setzen:
Nr. Befehl Beschreibung Register
8195 VOLT˽MAX bzw. CURR˽MAX Spannung bzw. Strom auf Maximum setzen. Man kann hier 500
auch beliebig andere Werte setzen, die aber empfohlenerweise 501
mindestens so hoch sein sollte wie der größte Wert aus der
XY-Tabelle.
8196 POW˽MAX Leistungssollwert auf Maximum setzen, unabhängig vom Ge- 502
rätemodell
Zusätzlich für PSB-Serien: Nur nötig in den Modi IU und IUEL, wo das Gerät im entweder 499
ausschließlich im Senke-Betrieb arbeitet oder in diesen wech- 498
SINK:CURR˽MAX
seln kann
SINK:POW˽MAX
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 97
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Der Funktionsgenerator ist nun konfiguriert und die IU-Tabelle geladen. Jetzt kann die Funktion gestartet und
ferngesteuert bedient werden:
Nr. Befehl Beschreibung Register
8197 INP˽ON Einschalten des DC-Eingangs bzw. des DC-Ausgangs, je nach 405
OUTP˽ON Gerätetyp
8198 INP˽OFF Später: Ausschalten des DC-Eingangs bzw. des DC-Ausgangs, 405
OUTP˽OFF je nach Gerätetyp, um die Funktion zu stoppen
8199 FUNC:GEN:SEL˽NONE Optional: Funktionsgenerator mit NONE wieder verlassen. 855
(856)
5.5.2.3 Befehlsfolge zur Realisierung einer ansteigenden Rampe (Arbiträrgenerator)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
 ─ ─  ─ ─  ─  ─  ─ ─ ─ ─   ─ 
Bevor Sie den Arbiträrgenerator mit Daten füttern können, sollte überlegt werden, wie man eine Rampe oder Recht-
eck oder Trapez usw. mit dem Arbiträrgenerator realisieren kann. Wichtig zu wissen ist, daß der Arbiträrgenerator
am Ende des Ablaufs automatisch stoppt. Dabei bleibt der DC-Ausgang des Gerätes jedoch an. Das Gerät geht
dann wieder in den statischen Modus und setzt die Sollwerte, die global für den Betrieb festgelegt wurden. Die
statischen Werte gelten aber auch für den Zeitraum vor dem Start, zumindest falls der DC-Ausgang vorher schon
eingeschaltet ist.
Das mit dem Stopp und Setzen des statischen Wertes ist für eine Rampe problematisch, weil ihr Endwert für eine
Zeit x konstant bleiben soll. Ein statischer Wert wäre auch konstant, soll hier aber u. U. gar nicht wirken. Warum?
Angenommen, bei einem Netzgerät soll die Rampe bei 0 V starten. Dann würde man den statischen Wert der
Spannung auf 0 V einstellen, den DC-Ausgang einschalten und danach die Funktion ablaufen lassen. Am Ende
der Funktion würde das Gerät aber wieder statisch 0 V setzen. Also muß die konstante Spannung am Ende der
Rampe zum Teil der Funktion werden.
Es ergibt sich daraus, daß die Rampe aus zwei Abschnitten besteht: der ansteigenden bzw. abfallenden Flanke
und dem konstanten Wert am Ende. Mittels des Arbiträrgenerators setzt man das mit zwei Sequenzpunkten um.
Annahme: die Rampe soll einen Spannungsanstieg von 0 V auf 50 V in einer Zeit von 6 s umsetzen. Die Endspan-
nung von 50 V soll für 3 Minuten konstant bleiben (die Zeit hier ist beliebig variabel). Die zwei Sequenzpunkte,
die man dazu benötigt, könnten Punkt 1 und 2 sein. Fernsteuerung ist bereits aktiv, es wird zunächst konfiguriert.
Da eine Rampe die Spannung linear ansteigen oder abfallen läßt, also nur den DC-Anteil des Sequenzpunktes
nutzt, sollten die zum hier nicht genutztem AC-Anteil gehörenden Parameter (Indexe 0, 1, 2, 3, 4) zur Sicherheit alle
auf 0 gesetzt werden, damit nicht irgendwelche vormals verwendeten Werte den späteren Ablauf stören können.
Die Befehle, die das umsetzen, sind im Beispiel unten nicht aufgeführt.
Sequenzpunkt 1, die ansteigende Flanke
Nr. Befehl Beschreibung Register
1 FUNC:GEN:SEL˽VOLT Wählt Arbiträrgenerator für Spannung. Ab hier befindet sich das 851
Gerät im Funktionsgenerator-Modus
2 FUNC:GEN:WAVE:LEV˽1 Wählt die 1. Sequenz zum Schreiben aus 900
3 FUNC:GEN:WAVE:IND˽5 Index 5 wählen: Startspannung der Rampe
4 FUNC:GEN:WAVE:DAT˽0 Auf 0 V setzen 900
5 FUNC:GEN:WAVE:IND˽6 Index 6 wählen: Endspannung der Rampe
6 FUNC:GEN:WAVE:DAT˽50 Auf 50 V setzen 900
7 FUNC:GEN:WAVE:IND˽7 Index 7 wählen: Dauer der Flanke
8 FUNC:GEN:WAVE:DAT˽6 Auf 6 Sekunden setzen 900
Sequenz 2, die konstante Spannung am Ende der Rampe
Nr. Befehl Beschreibung Register
9 FUNC:GEN:WAVE:LEV˽2 Wählt die 2. Sequenz zum Schreiben aus 915
10 FUNC:GEN:WAVE:IND˽5 Index 5 wählen: Startwert für die statische Spannung
11 FUNC:GEN:WAVE:DAT˽50 Auf 50 V setzen (muß gleich dem Endwert von Sequenzpunkt 915
1 sein)
12 FUNC:GEN:WAVE:IND˽6 Index 6 wählen: Endwert für die statische Spannung
13 FUNC:GEN:WAVE:DAT˽50 Auf 50 V setzen 915
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 98
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| Nr. Befehl               |     |     | Beschreibung          |     |     |     |     |     | Register |
| ------------------------ | --- | --- | --------------------- | --- | --- | --- | --- | --- | -------- |
| 14 FUNC:GEN:WAVE:IND˽7   |     |     | Index 7 wählen: Dauer |     |     |     |     |     |          |
| 15 FUNC:GEN:WAVE:DAT˽180 |     |     | Auf 3 Minuten setzen  |     |     |     |     |     | 915      |
Arbiträrgenerator konfigurieren
| Nr. Befehl |     |     | Beschreibung |     |     |     |     |     | Register |
| ---------- | --- | --- | ------------ | --- | --- | --- | --- | --- | -------- |
16 FUNC:GEN:WAVE:END˽2 Legt den 2. Sequenzpunkt als Endpunkt fest 860
17 FUNC:GEN:WAVE:STAR˽1 Legt den 1. Sequenzpunkt als Startpunkt fest 859
| 18 FUNC:GEN:WAVE:NUM˽1 |     |     | Anzahl der Durchläufe |     |     |     |     |     | 861 |
| ---------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| 19 FUNC:GEN:WAVE:SUBM  |     |     | Alle Daten übernehmen |     |     |     |     |     |     |
Danach	ist	die	Rampenfunktion	fertig	konfiguriert	und	kann	gestartet	werden.	Ist	der	DC-Eingang/Ausgang	noch
aus, wird er durch den Start des Funktionsgenerators automatisch eingeschaltet. Alternativ kann das auch vorher
mit	dem	entsprechenden	Befehl	geschehen,	was	hier	aber	nicht	nötig	ist,	weil	bei	0	V	gestartet	wird.	Soll	eine
Funktion bei einem Wert ungleich 0 starten, muß der DC-Ausgang vorher schon eingeschaltet sein.
Bei der Anzahl der Durchläufe reicht 1x. Das kann aber nach Belieben geändert werden. Dann würde die Funktion
nach 3 m 6 s mindestens einmal erneut ablaufen. Die Spannung würde jedoch nicht schlagartig von 50 V auf
0	V	absinken	können,	so	wie	für	die	steigende	Flanke	gefordert.	Die	zweite	und	weitere	Rampen	sähen	dann
etwas	unförmiger	aus.	Um	das	zu	verhindern,	könnte	ein	dritter	Sequenzpunkt	programmiert	werden,	welcher	der
Spannung einfach eine gewisse Zeit gibt, um wieder auf 0 zu sinken. Wie schnell die Spannung sinkt hängt in
erster Linie von der Belastung am DC-Ausgang ab.
| Nr. Befehl |     |     | Beschreibung |     |     |     |     |     | Register |
| ---------- | --- | --- | ------------ | --- | --- | --- | --- | --- | -------- |
20 FUNC:GEN:WAVE:STAT˽RUN Starten des Funktionsablaufs (RUN) 850
Ohne Wiederholung stoppt die Funktion bei 1-maligem Durchlauf und 2 genutzten Sequenzpunkten nach der sich
ergebenden Zeit von 3 m 6 s, die Spannung würde dann auf 0 sinken. Soll die Spannung danach nicht sinken
und	die	Zeit	am	Ende	der	Funktion	so	lang	wie	möglich	sein,	müßte	man	eventuell	die	restlichen	97	Sequenzen
bemühen. Pro Sequenzpunkt sind max. 10 h machbar, insgesamt also 98 x 10 h = 980 h statischer Wert.
5.5.3  Programmier-Beispiele zur PV-Simulation (DIN EN 50530)
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 ELR1
PSBE1
| ─ ─ | ─  | ─ ─ | ─ ─ | ─ ─ |  ─ | ─ ─ | ─  |  ─ | ─   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Näheres	zu	dieser	erweiterten	PV-Simulation	finden	Sie	in	den	Handbüchern	der	Geräte,	sowie	in	der	Normschrift
selbst. Die Gerätehandbücher erläutern auch den Zusammenhang zwischen Simulationsmodus, Eingabemodus
und Panel-Technologie.
Wichtig: nach dem Start der Simulation wird zunächst die erste PV-Kurve berechnet. Dafür
benötigt das Gerät ca. 500 ms. Das bedeutet, die eigentliche Simulation beginnt ca. 500 ms
nach dem Start.
Übersicht	(ein	"x"	markiert	eine	mögliche	Kombination):
|     |     | Optionen | Eingabemodus ULIK |     | Eingabemodus MPP |     |     |     |     |
| --- | --- | -------- | ----------------- | --- | ---------------- | --- | --- | --- | --- |
Simulations-Modus
|     |     |     | x   |     | x (Beispiel 1) |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
ET
| UI       |            |     |                |     | x (Beispiel 3) |     |     |     |     |
| -------- | ---------- | --- | -------------- | --- | -------------- | --- | --- | --- | --- |
| DAY ET   |            |     | x (Beispiel 2) |     | x              |     |     |     |     |
| DAY UI   |            |     |                |     | x (Beispiel 4) |     |     |     |     |
| 5.5.3.1  | Beispiel 1 |     |                |     |                |     |     |     |     |
• Technologie: cSi
• Eingabemodus: MPP-Werte
• Simulations-Modus: Kontinuierlich, mit einstellbarer Temperatur und Einstrahlungsstärke
• Datenaufzeichnung: aktiviert
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 99
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Konfiguration
| Nr. Befehl     | Beschreibung             |     | Register |
| -------------- | ------------------------ | --- | -------- |
| 1 SYST:LOCK˽ON | Fernsteuerung aktivieren |     | 402      |
2 FUNC:PHOT:MOD˽ET PV-Simulation aktivieren, Simulations-Modus ET 12001
| 3 FUNC:PHOT:TECH˽CSI         | Technologie wählen: cSi                 |     | 12016 |
| ---------------------------- | --------------------------------------- | --- | ----- |
| 4 FUNC:PHOT:IMOD˽MPP         | Eingabemodus wählen: MPP                |     | 12017 |
| 5 FUNC:PHOT:STAN:MPP:VOLT˽20 | MPP-Spannung setzen: 20 V               |     | 12050 |
| 6 FUNC:PHOT:STAN:MPP:CURR˽5  | MPP-Strom setzen: 5 A                   |     | 12051 |
| 7 FUNC:PHOT:REC:ACT˽ENAB     | Datenaufzeichnung: aktivieren           |     | 12018 |
| 8 POW˽MAX                    | Globale Leistung auf das Maximum setzen |     | 502   |
9 VOLT 30 Globale	Spannungsgrenze	setzen	(sollte	≥Uoc	sein) 500
•  Die Standard- oder Startwerte, wie in Schritt 5 und 6 gesetzt, dienen nur zur Berechnung der
ersten Kurve. Die Werte für den MPP (:STAN:MPP) sind dabei über die Faktoren FFi und
FFu mit den Grenzwerten Uoc (:STAN:OCV) und Isc (:STAN:SCC) verknüpft, so daß sie sich
gegenseitig überschreiben. Bedeutet, das Setzen von :STAN:MPP:VOLT überschreibt den
Wert in :STAN:OCV und umgekehrt. Beim Strom genauso.
•  Die erste Kurve nach dem Start der Funktion wird mit den Standardwerten T = 25°C und
E = 1000 W/m² berechnet
Steuerung (auch während der Simulation)
| Nr. Befehl            | Beschreibung                    |     | Register |
| --------------------- | ------------------------------- | --- | -------- |
| 10 FUNC:PHOT:STAT˽RUN | Simulation starten              |     | 12000    |
| 11 FUNC:PHOT:TEMP˽40  | Temperaturwert verändern: 40 °C |     | 12052    |
12 FUNC:PHOT:IRR˽800 Einstrahlungsstärke verändern: 800 W/m² 12053
13 FUNC:PHOT:STAT˽STOP Nach beliebiger Zeit Simulation stoppen 12000
Auswertung nach dem Ende der Simulation
| Nr. Befehl | Beschreibung |     | Register |
| ---------- | ------------ | --- | -------- |
14 FUNC:PHOT:REC:NUMB? Anzahl (n) der aufgezeichneten Datensätze ermitteln 12020
| 15 FUNC:PHOT:REC:IND˽1 | Index 1 anwählen zum Auslesen    |     | 12022 |
| ---------------------- | -------------------------------- | --- | ----- |
| 16 FUNC:PHOT:REC:DAT?  | Daten von Index 1 auslesen       |     | 12024 |
| ... ...                | Weitere n-1 Datensätze auslesen: |     | ...   |
| x FUNC:PHOT:REC:IND˽n  | Index n anwählen zum Auslesen    |     | 12022 |
|                        | Daten von Index n auslesen       |     | 12024 |
y FUNC:PHOT:REC:DAT?
5.5.3.2  Beispiel 2
•	 Technologie: Manuell
•	 Eingabemodus: Leerlaufspannung und Kurzschlußstrom
•	 Simulations-Modus: Tagestrend mit einstellbarer Temperatur und Einstrahlungsstärke
•	 Interpolation: deaktiviert
•	 Datenaufzeichnung: aktiviert
Konfiguration
| Nr. Befehl     | Beschreibung             |     | Register |
| -------------- | ------------------------ | --- | -------- |
| 1 SYST:LOCK˽ON | Fernsteuerung aktivieren |     | 402      |
2 FUNC:PHOT:MOD˽DAYET PV-Simulation aktivieren, Simulations-Modus DAYET 12001
3 FUNC:PHOT:TECH˽MAN Technologie wählen: Manuell (alle erforderlichen Para- 12016
meter müssen angegeben werden, hier Befehle 4-10)
|                          | Füllfaktor Spannung (FF | ): 0,8 | 12034 |
| ------------------------ | ----------------------- | ------ | ----- |
| 4 FUNC:PHOT:FACT:FFU˽0.8 |                         | U      |       |
5 FUNC:PHOT:FACT:FFI˽0.78 Füllfaktor Strom (FF): 0,78 I 12036
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 100
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
6 FUNC:PHOT:FACT:ALPH˽0.0003 Temperaturkoeffizient	α zu I SC : 0,0003 /°C 12038
7 FUNC:PHOT:FACT:BETA˽-0.003 Temperaturkoeffizient	β zu U OC : -0,003 /°C 12040
8 FUNC:PHOT:FACT:CU˽0.0725 Korrekturfaktor C  zu U : 0,0725 12042
U OC
9 FUNC:PHOT:FACT:CR˽0.00022 Korrekturfaktor C  zu U : 0,00022 m²/W 12044
R OC
10 FUNC:PHOT:FACT:CG˽0.00315 Korrekturfaktor C  zu U : 0,00315 W/m² 12046
G OC
| 11 FUNC:PHOT:IMOD˽ULIK    | Eingabemodus wählen: ULIK     | 12017 |
| ------------------------- | ----------------------------- | ----- |
| 12 FUNC:PHOT:STAN:OCV˽38  | Leerlaufspannung setzen: 38 V | 12048 |
| 13 FUNC:PHOT:STAN:SCC˽7   | Kurzschlußstrom setzen: 7 A   | 12049 |
| 14 FUNC:PHOT:REC:ACT˽ENAB | Datenaufzeichnung aktivieren  | 12018 |
15 FUNC:PHOT:DAY:INT˽OFF Interpolation der Tagesdaten deaktivieren 12005
| 16 POW˽MAX | Globale Leistung auf das Maximum setzen | 502 |
| ---------- | --------------------------------------- | --- |
17 VOLT 38 Globale	Spannungsgrenze	setzen	(sollte	≥Uoc	sein) 500
•  Die Standard- oder Startwerte, wie mit den beiden Befehlen in Schritt 12 und 13 gesetzt,
dienen nur zur Berechnung der ersten Kurve. Sobald ein Parameter verändert wird, der zur
Verschiebung des MPP führt, wird die Kurve neu berechnet.
•  Spannung und Strom im MPP sind über die Faktoren FFi und FFu mit der Leerlaufspannung
Uoc bzw. dem Kurzschlußstrom Isc verknüpft,  die in diesem Beispiel beide vorgegeben
werden, alternativ zu Beispiel 1. Diese Faktoren sind, je nach Technologie, veränderlich
oder unveränderlich.
Tagesdaten laden (nur möglich vor dem Start der Funktion)
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
18 FUNC:PHOT:DAY:MOD˽WRIT Zugriffsmodus	Schreiben	wählen 12006
19 FUNC:PHOT:DAY˽CLE Alte	Daten	löschen	(sollte	immer	vor	dem	Laden	neuer	12007
Daten ausgeführt werden)
20 FUNC:PHOT:DAY:DAT˽1,˽500,  Ersten Tages-Datensatz in Index 1 schreiben mit: 12010
| ˽20,˽1500 | Einstrahlungsstärke: 500 W/m² |     |
| --------- | ----------------------------- | --- |
Temperatur: 20°C
Verweildauer: 1500 ms
Die Verweildauer ist zwar generell auf minimal 500 ms definiert, der Wert für
den ersten Tagesdatensatz sollte aber auf 1000 ms oder höher gesetzt werden,
sonst könnte der Ablauf der Funktion fehlschlagen.
21 FUNC:PHOT:DAY:DAT˽2,˽800,  Zweiten Tages-Datensatz in Index 2 schreiben mit: 12010
| ˽28,˽1500 | Einstrahlungsstärke: 800 W/m² |     |
| --------- | ----------------------------- | --- |
Temperatur: 28°C
Verweildauer: 1500 ms
... ... Weitere Tages-Datensätze schreiben, insgesamt 500 ...
519 FUNC:PHOT:DAY:DAT˽500,˽  500. Tagesdaten-Satz in Index 1 schreiben mit: 12010
| 1200,˽35,˽20000 | Einstrahlungsstärke: 1200 W/m² |     |
| --------------- | ------------------------------ | --- |
Temperatur: 35°C
Verweildauer: 20000 ms
Steuerung
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
520 FUNC:PHOT:STAT˽RUN Simulation starten -> die Simulation läuft ab und stoppt 12000
automatisch nach der Gesamtzeit, die sich aus den Ver-
weildauern aller geladenen Tages-Datensätze ergibt
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 101
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Auswertung (nach dem Ende der Simulation)
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
521 FUNC:PHOT:REC:NUMB? Anzahl (n) der aufgezeichneten Datensätze ermitteln.  12020
Die Anzahl ist nicht gleichbedeutend mit der Anzahl der
Tages-Datensätze, weil die Aufzeichnung kontinuierlich
alle 100 ms aufzeichnet. Je nach Gesamtdauer der Si-
mulation	könnte	der	Aufzeichnungsspeicher	vollgelaufen
(max. 16 h Aufzeichnungsdauer) und Daten überschrieben
worden sein. Es kann daher notwendig werden, vor dem
Start die Gesamtdauer aus den Tages-Datensätzen zu
ermitteln und die aufgezeichneten Daten bereits während
der	Simulation	auszulesen,	den	Speicher	zu	löschen	und
später den Rest auszulesen.
| 522 FUNC:PHOT:REC:IND˽1 | Index 1 anwählen zum Auslesen    | 12022 |
| ----------------------- | -------------------------------- | ----- |
| 523 FUNC:PHOT:REC:DAT?  | Daten von Index 1 auslesen       | 12024 |
| ... ...                 | Weitere n-1 Datensätze auslesen: | ...   |
| x FUNC:PHOT:REC:IND˽n   | Index n anwählen zum Auslesen    | 12022 |
| y FUNC:PHOT:REC:DAT?    | Daten von Index n auslesen       | 12024 |
5.5.3.3  Beispiel 3
•	 Technologie: Dünnschicht
•	 Eingabemodus: MPP
•	 Simulationsmodus: UI
•	 Datenaufzeichnung: deaktiviert
Konfiguration
| Nr. Befehl     | Beschreibung             | Register |
| -------------- | ------------------------ | -------- |
| 1 SYST:LOCK˽ON | Fernsteuerung aktivieren | 402      |
2 FUNC:PHOT:MOD˽UI PV-Simulation aktivieren, Simulations-Modus UI 12001
| 3 FUNC:PHOT:TECH˽THIN        | Technologie wählen: Dünnfilm   | 12016 |
| ---------------------------- | ------------------------------ | ----- |
| 4 FUNC:PHOT:IMOD˽MPP         | Eingabemodus wählen: MPP       | 12017 |
| 5 FUNC:PHOT:STAN:MPP:VOLT˽45 | MPP-Spannung setzen: 45 V      | 12050 |
| 6 FUNC:PHOT:STAN:MPP:CURR˽10 | MPP-Strom setzen: 10 A         | 12051 |
|                              | Datenaufzeichnung deaktivieren | 12018 |
7 FUNC:PHOT:REC:ACT˽DIS
|     | Globale Leistung auf das Maximum setzen | 502 |
| --- | --------------------------------------- | --- |
8 POW˽MAX
9 VOLT 57 Globale	Spannungsgrenze	setzen	(sollte	≥Uoc	sein) 500
Steuerung (auch während der Simulation)
| Nr. Befehl            | Beschreibung       | Register |
| --------------------- | ------------------ | -------- |
| 10 FUNC:PHOT:STAT˽RUN | Simulation starten | 12000    |
11 FUNC:PHOT:STAN:MPP:VOLT˽40 MPP verschieben auf: 40 V 12050
| 12 FUNC:PHOT:STAN:MPP:CURR˽9 | MPP verschieben auf: 9 A | 12051 |
| ---------------------------- | ------------------------ | ----- |
13 FUNC:PHOT:STAT˽STOP Nach beliebiger Zeit Simulation stoppen 12000
5.5.3.4  Beispiel 4
•	 Technologie: cSi
•	 Eingabemodus: MPP-Werte
•	 Simulations-Modus: Tagestrend mit verschiebbarem MPP (Spannung und Strom)
•	 Interpolation: aktiviert (bei aktivierter Interpolation wird die Zeit des ersten Tages-Datensatzes für alle
übernommen, muß aber trotzdem in einem sinnvollen Bereich angegeben werden)
•	 Datenaufzeichnung: deaktiviert
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 102
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Konfiguration
| Nr. Befehl     | Beschreibung             | Register |
| -------------- | ------------------------ | -------- |
| 1 SYST:LOCK˽ON | Fernsteuerung aktivieren | 402      |
2 FUNC:PHOT:MOD˽DAYUI PV-Simulation aktivieren, Simulations-Modus DAYUI 12001
| 3 FUNC:PHOT:TECH˽CSI | Technologie wählen: cSi  | 12016 |
| -------------------- | ------------------------ | ----- |
| 4 FUNC:PHOT:IMOD˽MPP | Eingabemodus wählen: MPP | 12017 |
5 FUNC:PHOT:STAN:MPP:VOLT˽36 Leerlaufspannung setzen: 36 V 12050
6 FUNC:PHOT:STAN:MPP:CURR˽12 Kurzschlußstrom setzen: 12 A 12051
| 7 FUNC:PHOT:REC:ACT˽DIS | Datenaufzeichnung deaktivieren | 12018 |
| ----------------------- | ------------------------------ | ----- |
8 FUNC:PHOT:DAY:INT˽ON Interpolation der Tagesdaten aktivieren 12005
| 9 POW˽MAX | Globale Leistung auf das Maximum setzen | 502 |
| --------- | --------------------------------------- | --- |
10 VOLT 57 Globale	Spannungsgrenze	setzen	(sollte	≥Uoc	sein) 500
Tagesdaten laden (nur möglich vor dem Start der Funktion)
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
11 FUNC:PHOT:DAY:MOD˽WRIT Zugriffsmodus	Schreiben	wählen 12006
Alte	Daten	löschen	(sollte	immer	vor	dem	Laden	neuer	12007
12 FUNC:PHOT:DAY˽CLE
Daten ausgeführt werden)
13 FUNC:PHOT:DAY:DAT˽1,˽1,˽1,  Ersten Tages-Datensatz in Index 1 schreiben mit: 12010
| ˽300000 | MPP-Spannung: 1 V |     |
| ------- | ----------------- | --- |
MPP-Strom: 1 A
Verweildauer: 300.000 Millisekunden => 5 Minuten
14 FUNC:PHOT:DAY:DAT˽2,˽2,˽2,  Zweiten Tages-Datensatz in Index 2 schreiben mit: 12010
| ˽500 | MPP-Spannung: 2 V |     |
| ---- | ----------------- | --- |
MPP-Strom: 2 A
... ... Weitere Tages-Datensätze schreiben, insgesamt 1000 ...
1012 FUNC:PHOT:DAY:DAT˽1000,˽30,  1000. Tagesdaten-Satz in Index 1000 schreiben mit: 12010
MPP-Spannung: 30 V
˽9,˽500
MPP-Strom: 9 A
Durch die Vorgabe von 5 Minuten Verweildauer im ersten Tages-Datensatz und aktivierter Interpolation nutzen
alle 1000 Datensätze dieselbe Verweildauer. Es ergibt sich eine Gesamt-Simulationsdauer von 5000 Minuten.
Steuerung
| Nr. Befehl | Beschreibung | Register |
| ---------- | ------------ | -------- |
1013 FUNC:PHOT:STAT˽RUN Simulation starten -> die Simulation läuft ab und stoppt 12000
automatisch nach der Gesamtzeit, die sich aus den Ver-
weildauern aller geladenen Tages-Datensätze ergibt
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 103
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 5.5.4  | Programmier-Beispiele für MPP-Tracking |     |     |     |     |     |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ELR9 ELR5 PS9 PSI9 PSI5 PSE DT PST PSIT EL3 PSB PSBE PS3 PS2 PS1 PSI1 PSB1 PSBE1 ELR1
|   | ─ ─ | ─ ─ (1 | ─ ─ |   | ─ ─ | ─ ─ | ─  | ─  |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- |
(1  nicht PSI 9000 DT
| 5.5.4.1  | MPP2 |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Siehe	zu	diesem	Thema	auch	das	Handbuch	ihres	Gerätes,	welches	einige	Grundlagen	und	Begriffe	erläutert.	Für
die Modi MPP1 bis MPP3 müssen keine Daten geladen werden.
Die	in	der	Konfiguration	gesetzten	Parameter	sind	zur	Laufzeit	unveränderlich.
Konfiguration
| Nr. Befehl     |     |     | Beschreibung             |     |     |     |     | Register |
| -------------- | --- | --- | ------------------------ | --- | --- | --- | --- | -------- |
| 1 SYST:LOCK˽ON |     |     | Fernsteuerung aktivieren |     |     |     |     | 402      |
2 FUNC:GEN:MPP:IND˽0 Index 0 dient zur generellen Moduswahl 11000
3 FUNC:GEN:MPP:DAT˽MPP2 Modus MPP2 ("MPP verfolgen") wählen. Dieser Modus 11000
stoppt nicht automatisch.
4 FUNC:GEN:MPP:IND˽1 Leerlaufspannung U  des Solarpaneels setzen, an dem 11001
OC
die elektronische Last das Tracking ausführt. Dieser Wert
ist gleichzeitig die Spannungsgrenze des Gerätes.
| 5 FUNC:GEN:MPP:DAT˽50 |     |     | U  auf 50 V setzen |     |     |     |     | 11001 |
| --------------------- | --- | --- | ------------------ | --- | --- | --- | --- | ----- |
OC
6 FUNC:GEN:MPP:IND˽2 Kurzschlußstrom I  des Solarpaneels setzen, an dem die 11002
SC
elektronische Last das Tracking ausführt. Dieser Wert ist
gleichzeitig die Stromgrenze des Gerätes.
| 7 FUNC:GEN:MPP:DAT˽100 |     |     | I auf 100 A setzen |     |     |     |     | 11002 |
| ---------------------- | --- | --- | ------------------ | --- | --- | --- | --- | ----- |
SC
8 FUNC:GEN:MPP:IND˽10 Tracking-Intervall	Δt	in	Millisekunden,	der	zeitliche	Ab- 11013
stand zum nächsten Trackingversuch
| 9 FUNC:GEN:MPP:DAT˽3000 |     |     | Zeit = 3 s  |     |     |     |     | 11013 |
| ----------------------- | --- | --- | ----------- | --- | --- | --- | --- | ----- |
10 FUNC:GEN:MPP:IND˽6 ΔP,	ein	Differenzwert	zu	P  ab dessen Überschreitung 11006
MPP
das Gerät überhaupt erst wieder einen nächsten Trak-
kingversuch startet
11 FUNC:GEN:MPP:DAT˽30 ΔP	=	30	W	(bei	Serien	mit	geringer	Nennleistung	ist	der	11006
einstellbare Bereich 0-50 W [siehe Handbuch], bei anderen
|     |     |     | Serien ist er 0-P |     | )   |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
Nenn
Steuerung
| Nr. Befehl |     |     | Beschreibung |     |     |     |     | Register |
| ---------- | --- | --- | ------------ | --- | --- | --- | --- | -------- |
12 FUNC:GEN:MPP:STAT˽RUN Tracking	starten	->	das	Gerät	versucht,	den	MPP	zu	finden,	11010
um ihn dann zu verfolgen (engl.: to track). Dieser Modus
stoppt nicht automatisch. Der zeitliche Abstand zwischen
zwei	Trackingversuchen	wurde	über	Index	10	definiert,	die
zulässige Abweichung der Istleistung zum MPP mit Index
|     |     |     | 6. Der zuletzt ermittelte MPP wird als U |     |     |     | , I  und P |     |
| --- | --- | --- | ---------------------------------------- | --- | --- | --- | ---------- | --- |
|     |     |     |                                          |     |     | MPP | MPP        | MPP |
gespeichert und ist entweder zur Laufzeit des Tests oder
hinterher auslesbar.
|     |     |     | Tracking nach beliebiger Zeit stoppen |     |     |     |     | 11010 |
| --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ----- |
13 FUNC:GEN:MPP:STAT˽STOP
Auswertung
| Nr. Befehl |     |     | Beschreibung |     |     |     |     | Register |
| ---------- | --- | --- | ------------ | --- | --- | --- | --- | -------- |
14 FUNC:GEN:MPP:IND˽7 Index 7 dient zur Anwahl vor dem Auslesen der MPP-Werte 11007
11008
15 FUNC:GEN:MPP:DAT? Auslesen der drei Werte im MPP als U , I  und P
|     |     |     |     |     |     | MPP | MPP | MPP 11009 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 104
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.5.4.2 MPP4
Dieser Modus ist bei allen Serien über die Fernsteuerung verfügbar, aber nicht bei allen auch am Bedienteil (HMI).
Wenn Informationen über diesen Modus benötigt werden, dann siehe z. B. das Handbuch der Serie EL 9000 B 3U.
In diesem Modus, der auch "Benutzerkurve" genannt wird, ermittelt das Gerät anhand von Benutzerdaten (1-100
Spannungswerte) auf einer möglichen PV-Kurve eine Solarmoduls den sog. MPP anhand eines Spannungswertes.
Die ermittelten Werte (U, I, P im MPP) werden für alle angefahrenen Punkte gespeichert und sind später auslesbar.
Der eigentliche MPP, also der Punkt mit der höchsten Leistung, wird vom Gerät aus den Meßwerten ermittelt und
separat auslesbar abgelegt.
Das Beispiel zeigt Modus MPP4 Konfiguration und Ablauf mit 75 Benutzerpunkten.
Konfiguration
Nr. Befehl Beschreibung Register
1 SYST:LOCK˽ON Fernsteuerung aktivieren 402
2 FUNC:GEN:MPP:IND˽0 Index 0 dient zur generellen Moduswahl 11000
3 FUNC:GEN:MPP:DAT˽MPP4 Modus MPP4 ("Benutzerkurve") wählen. Dieser Modus 11000
stoppt nach Abarbeitung aller Punkte automatisch.
4 FUNC:GEN:MPP:IND˽8 Index 8 = Modus zur Benutzerdateneingabe 11100 -
11174
5 FUNC:GEN:MPP:LEV˽1 Level 1 entspricht dem 1. Punkt der Benutzerkurve.
6 FUNC:GEN:MPP:DAT˽100 1. Punkt der Benutzerkurve auf 100 V setzen
... Möglichst durchgängig weitere Punkt laden
153 FUNC:GEN:MPP:LEV˽75 Level 75 entspricht dem 75. Punkt der Benutzerkurve.
154 FUNC:GEN:MPP:DAT˽80 75. Punkt der Benutzerkurve auf 80 V setzen
155 FUNC:GEN:MPP:IND˽12 Endpunkt auf der Kurve wählen. Er muß nicht zwangs- 11015
weise mit dem letzten der zuvor geladenen Punkte über-
einstimmen. Da der Startpunkt nicht größer sein kann als
der Endpunkt, wird der Endpunkt zuerst gesetzt.
156 FUNC:GEN:MPP:DAT˽75 Endpunkt = 75 11015
157 FUNC:GEN:MPP:IND˽11 Startpunkt auf der Kurve wählen. Er muß nicht zwangs- 11014
weise mit dem ersten der zuvor geladenen Punkte über-
einstimmen. Der Wert darf nicht größer sein als der des
Endpunkts.
158 FUNC:GEN:MPP:DAT˽1 Startpunkt = 1 11014
159 FUNC:GEN:MPP:IND˽10 Tracking-Intervall Δt in Millisekunden, der zeitliche Ab- 11013
stand zum nächsten Trackingversuch
160 FUNC:GEN:MPP:DAT˽500 Zeit = 0,5 s 11013
161 FUNC:GEN:MPP:IND˽13 Anzahl der Wiederholungen (0-65535) des Durchlaufs. 11016
Es können hinterher nur die ermittelten Daten des letz-
ten Durchlaufs ausgelesen werden
162 FUNC:GEN:MPP:DAT˽0 Wiederholungen = 0, d. h. nur ein Durchlauf 11016
Wenn ein Punkt angefahren wird, der vorher nicht explizit mit einem Wert beschrieben wurde,
setzt das Gerät 0 V für diesen.
Steuerung
Nr. Befehl Beschreibung Register
163 FUNC:GEN:MPP:STAT˽RUN Tracking starten -> das Gerät nimmt den ersten Span- 11010
nungswert aus der Kurve, der als Startpunkt definiert
wurde und ermittelt dazu Strom und Leistung. Dann den
nächsten usw. Der zeitliche Abstand zwischen zwei Punk-
ten wurde über Index 10 definiert. Die Gesamtzeit des
Tests ergibt sich aus Δt * (Ende - Start +1). Es gibt keinen
auslesbaren Status, wann der Durchlauf zu Ende ist.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 105
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Auswertung
Nr. Befehl Beschreibung Register
164 FUNC:GEN:MPP:IND˽9 Index 9 = Modus zum Auslesen der MPP4-Meßwerte 11200 -
11274
165 FUNC:GEN:MPP:LEV˽1 1. Punkt der Ergebnisliste zum Lesen anwählen
166 FUNC:GEN:MPP:DAT? Meßwerte des 1. Punktes als U , I und P auslesen
MPP MPP MPP
... Kontinuierlich weiter auslesen
313 FUNC:GEN:MPP:LEV˽75 75. Punkt der Ergebnisliste zum Lesen anwählen
314 FUNC:GEN:MPP:DAT? Meßwerte des 75. Punktes als U , I und P auslesen
MPP MPP MPP
315 FUNC:GEN:MPP:IND˽7 Index 7 dient zur Anwahl vor dem Auslesen der MPP-Werte 11007
11008
316 FUNC:GEN:MPP:DAT? Auslesen der drei Werte des MPP als U , I und P
MPP MPP MPP
11009
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 106
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.5.5 Programmierbeispiele zum Rampengenerator der Serie EL 3000 B
5.5.5.1 Beispiel 1: Sägezahn
Angenommen, das Zielgerät ist eine EL 3200-25 B mit Nennwerten von 200 V und 25 A. Die gewünschte Funktion
soll ein Sägezahn mit Offset 1 A und Spitze 5 A generieren, mit einer Anstiegszeit von 100 ms (Puls) und Pause
von 200 ms.
Konfiguration
Nr. Befehl Erläuterung Register
1 SYST:LOCK˽ON Fernsteuerung aktivieren 402
2 FUNC:RAMP:SEL˽CURR Den Rampengenerator auf Modus "Strom" zuweisen 852
3 FUNC:RAMP:IND˽0 Index 0 ist nach dem Start des Gerätes zwar immer ge- 900
setzt, aber für eine spätere, erneute Konfiguration sollte er
trotzdem explizit gesetzt werden. Gemäß Abschnitt 5.4.20
ist Index 0 mit Pegel P1 verknüpft, der als unterer Pegel
betrachtet wird. Hier wäre das die Pause zwischen den
Zähnen, definiert mit 1 A bei 200 ms Dauer.
4 FUNC:RAMP:OFFS˽4 Setzt den Offset vom Nullpunkt. Bei dieser Art Funktions-
generator werden die Pegel P1 und P2 als Prozentwert
vom Nennwert angegeben. Die angepeilten 1 A sind beim
Beispielmodell dann 1/25 oder 4%, somit wird als Wert 4
angegeben.
5 FUNC:RAMP:TIM˽100000 Die an Index 0 gebundene Zeit ist t1. Gemäß Abschnitt 902
5.4.20 wäre das die Anstiegszeit des Sägezahns, also 100
ms. Da die Zeit in Mikrosekunden angegeben wird, ist der
Wert 100.000.
6 FUNC:RAMP:IND˽1 Index 1 wählt Pegel P2, hier der obere bei 5 A 901
7 FUNC:RAMP:OFFS˽20 5 A sind 20% des Nennwerts
8 FUNC:RAMP:TIM˽10 Weil die gewünschte Funktion einen Sägezahn ergeben soll, 904
ist die Verweildauer an der Spitze (hier: t2) idealerweise 0,
kann aber nur auf das minimal Machbare gesetzt werden,
was 10 μs sind.
9 FUNC:RAMP:IND˽2 Index 2 wählt nur einen Zeitwert, hier t3. 906
10 FUNC:RAMP:TIM˽10 Dies setzt die Abfallzeit, welche idealerweise auch 0 ist,
aber nur auf das minimal Machbare gesetzt werden kann
11 FUNC:RAMP:IND˽3 Wählt Zeit t4 908
12 FUNC:RAMP:TIM˽200000 t4 ist die Pausezeit nach dem Sägezahn. Könnte für einen
kontinuierlichen Sägezahn auch auf das Minimum gesetzt
werden, wenn keine Pause benötigt wird.
13 VOLT˽0 Globaler Spannungssollwert. Soll dieser nicht auf einem 500
bestimmten Minimum stehen, unterhalb dessen die Last
keinen Strom ziehen soll, wird er üblicherweise auf 0 gesetzt.
14 POW˽MAX Globaler Leistungssollwert. Wird üblicherweise auf das 502
Maximum gesetzt, damit CP den Ablauf nicht beeinflußt.
15 optional: VOLT:PROT˽MAX usw. Weitere globale Werte wie Schutzwerte, wenn benötigt. diverse
Steuerung
Nr. Befehl Erläuterung Register
16 FUNC:RAMP:STAT˽RUN Startet die Funktion. Sollte zu dem Zeitpunkt der DC-Eingang 850
noch ausgeschaltet sein, wird dieser automatisch mit ein-
geschaltet.
17 FUNC:RAMP:STAT˽STOP oder Stoppt die Funktion nach beliebiger Zeit, die der Anwender 850 or
selbst bestimmt. Beide Befehle bewirken dasselbe (Stopp 405
INP˽OFF
und Ausschalten des DC-Eingangs)
18 FUNC:RAMP:SEL˽NONE Funktionsgeneratormodus verlassen. 852
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 107
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
5.5.5.2 Beispiel: 1 kHz-Rechteck auf den Strom mit 60% Pulsdauer
Dieses Beispiel ist auch für den Strom, da Strom zu senken die natürliche Arbeitsweise einer elektronischen Last
ist. Trotzdem könnte es genauso im Spannungsmodus umgesetzt werden, was u. U. zu anderen Ergebnissen
führt als erwartet.
Der Strompegel ist beliebig. Nehmen wir mal 10 A für oben und 0 A für unten, beim Beispielmodell EL 3080-60 B.
Bei einem Rechteck mit 1 kHz hat es 1000 Wiederholungen pro Sekunde bzw. 1 ms Periodendauer. 60% Pulsdauer
davon ergeben also 0.6 ms für die 10 A und daher 0.4 ms für die 0 A. Dazu kommt, daß die Anstiegszeit technisch
bedingt nicht 0 sein kann (Minimum: 10 μs), wodurch die resultierende Kurve genau genommen ein Trapez wird.
Will man das berücksichtigen, verringern sich Puls- und Pausendauer um 10 μs.
Konfiguration
Nr. Befehl Erläuterung Register
1 SYST:LOCK˽ON Fernsteuerung aktivieren 402
2 FUNC:RAMP:SEL˽CURR Den Rampengenerator auf Modus "Strom" zuweisen 852
3 FUNC:RAMP:IND˽0 Index 0 ist nach dem Start des Gerätes zwar immer ge- 900
setzt, aber für eine spätere, erneute Konfiguration sollte er
trotzdem explizit gesetzt werden. Gemäß Abschnitt 5.4.20
ist Index 0 mit Pegel P1 verknüpft, der als unterer Pegel
betrachtet wird. Hier wäre das die Pause des Rechtecks
4 FUNC:RAMP:OFFS˽0 Setzt den Offset vom Nullpunkt. Bei dieser Art Funktionsge-
nerator werden die Pegel P1 und P2 als Prozentwert vom
Nennwert angegeben.
5 FUNC:RAMP:TIM˽390 Die an Index 0 gebundene Zeit ist t1. Gemäß Abschnitt 902
5.4.20 wäre das die Pausendauer des Rechtecks, hier 0.4
ms. Da in Mikrosekunden angegeben, ist der Wert hier 390.
6 FUNC:RAMP:IND˽1 Index 1 wählt Pegel P2, hier die oberen 10 A 901
7 FUNC:RAMP:OFFS˽16.66 Setzt P2 auf 10 A, also 1/6 oder 16,66% des Nennwerts
8 FUNC:RAMP:TIM˽10 t2 gehört zur Anstiegszeit auf den oberen Pegel und soll 904
idealerweise 0 sein, was technisch hier nicht machbar ist,
daher wird das Minimum gesetzt.
9 FUNC:RAMP:IND˽2 Index 2 wählt nur einen Zeitwert, hier t3. 906
10 FUNC:RAMP:TIM˽590 t3 ist die Verweildauer am oberen Pegel, der Puls. Oben als
0,6 ms gegeben, daher ist der Wert 590
11 FUNC:RAMP:IND˽3 Wählt Zeit t4 908
12 FUNC:RAMP:TIM˽10 Zeit t4 ist die Abfallzeit des Pulses. Diese soll so kurz wie
möglich sein, idealerweise 0, und wird daher auf das Mini-
mum gesetzt
13 VOLT˽0 Globaler Spannungssollwert. Soll dieser nicht auf einem 500
bestimmten Minimum stehen, unterhalb dessen die Last
keinen Strom ziehen soll, wird er üblicherweise auf 0 gesetzt.
14 POW˽MAX Globaler Leistungssollwert. Wird üblicherweise auf das 502
Maximum gesetzt, damit CP den Ablauf nicht beeinflußt.
15 optional: VOLT:PROT˽MAX usw. Weitere globale Werte wie Schutzwerte, wenn benötigt. diverse
Steuerung
Nr. Befehl Erläuterung Register
16 FUNC:RAMP:STAT˽RUN Startet die Funktion. Sollte zu dem Zeitpunkt der DC-Eingang 850
noch ausgeschaltet sein, wird dieser automatisch mit ein-
geschaltet.
17 FUNC:RAMP:STAT˽STOP oder Stoppt die Funktion nach beliebiger Zeit, die der Anwender 850 or
selbst bestimmt. Beide Befehle bewirken dasselbe (Stopp 405
INP˽OFF
und Ausschalten des DC-Eingangs)
18 FUNC:RAMP:SEL˽NONE Funktionsgeneratormodus verlassen. 852
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 108
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
6. Profibus & Profinet
6.1 Allgemeines
Die Anbindung an die Feldbusse Profibus oder Profinet ist nur über die Schnittstellenmodule IF-AB-PBUS (Pro-
fibus) oder IF-AB-PNET (Profinet, 1 oder 2 Ports) möglich und wird somit nur von bestimmten Serien unterstützt:
• EL 9000 B (HP, 2Q)
• ELR 9000 / ELR 9000 HP
• PSI 9000 2U - 24U
• PSE 9000 / PSB 9000
• alle 10000er Serien
Auf der Seite des Gerätes wird die Konfiguration so weit wie möglich vereinfacht. Bei Profibus ist es nur erforderlich,
die Slave-Adresse (0...125) festzulegen, während die Netzwerkparameter bei Profinet üblicherweise von außen
und am besten mit dem Siemens Primary Setup Tool (PST) konfiguriert werden. Andere, optionale Parameter wie
die benutzerdefinierbaren „Tags“ können am Gerät eingegeben oder per Befehl in Fernsteuerung definiert werden.
Dieser Abschnitt soll aufzeigen, wie die sogenannte ModBus-Register-Liste (PDF) als Referenz dient, das Gerät
über Profibus oder Profinet zu steuern. Die Schnittstellen-Module repräsentieren das Gerät dabei gegenüber dem
Netzwerk als DP-V1-Slave mit zyklischem und azyklischem Datenverkehr, wobei der azyklische im Vordergrund steht.
6.2 Vorbereitung
Für die Einbindung in ein Netzwerk und Anmeldung am Master (SPS o. ä.) wird ein bereits fertig konfiguriertes
und verkabeltes Gerät vorausgesetzt. Als nächstes wird eine Geräte-Stamm-Datei (GSD/GSDML) benötigt, die
entweder auf einem dem Gerät beiliegenden USB-Stick enthalten ist bzw. auf Anfrage beim Hersteller des Gerätes
und für alle oben gelisteten Geräte bzw. Geräteserien gilt, welche die Anybus-Schnittstellenmodule für Profibus
und Profinet unterstützen. Die GSD/GSDML wird in der Automatisierungssoftware eingebunden und ermöglicht
eine bestimmte Slot-Konfiguration für die zyklischen Prozessdaten und den azyklischen Verkehr. Mehr dazu unten.
Die Hardwarekonfiguration mit den Slots ist normalerweise für steckbare Hardwaremodule an
einer SPS oder Erweiterungen gedacht, daher der Name "Slot". Ein Netzgerät oder eine elek-
tronische Last werden als periphere Hardware mit mehreren Software-Slots betrachtet. Das
Slotmodell wird dazu genutzt, diverse Funktionen der Fernsteuerung auf die Slots aufzuteilen,
um bequemer damit arbeiten zu können. Die Adressierung erfolgt dabei genauso, als würde
man ein echtes Steckmodul, z. B. einen digitalen I/O-Port ansprechen.
6.3 Slot-Konfiguration für Profibus
Die Slotkonfiguration für Nutzer des Schnittstellenmoduls IF-AB-PBUS erfolgt über das Laden der GSD im Konfi-
gurationsdialog (bei Siemens STEP7: HWKONFIG) und Anordnung in einer vorgegebenen Reihenfolge, zumindest
die Slots 1-4. Eine Minimalkonfiguration mit 8 Slots deckt die meisten Serien ab, andere benötigen bis zu 12.
Übersicht der Slots und deren Zuordnung:
Slot Slot-Name Beschreibung
1 Device status Zyklischer Gerätezustand (für die Bitaufteilung siehe Register 505) + Azykl. Slot 1
2 Actual voltage Zyklischer Istwert Spannung (für Umrechnung siehe 4.4) + Azykl. Slot 2
3 Actual. current Zyklischer Istwert Strom (für Umrechnung siehe 4.4) + Azykl. Slot 3
4 Actual power Zyklischer Istwert Leistung (für Umrechnung siehe 4.4) + Azykl. Slot 4
5 Reserved slot 5 für azyklischen Verkehr (DP-V1, azyklischer Slot 5)
...
12 Reserved slot 12 für azyklischen Verkehr (DP-V1, azyklischer Slot 12)
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 109
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
6.4 Slot-Konfiguration für Profinet
Die auf USB-Stick mitgelieferte GSDML bietet keine automatische Konfiguration der Slots. Diese muß vom Anwender
selbst erledigt werden. Beim Laden muß die richtige GSDML für das Profinet-Modul, 1-Port oder 2-Port, gewählt
werden. Eine Slotkonfiguration ist für die zyklischen Objekte notwendig und sollte wie folgt umgesetzt werden:
Slot Slot-Name Beschreibung
1 Input 2 words Zyklischer Gerätezustand (für die Bitaufteilung siehe Register 505)
2 Input 1 word Zyklischer Istwert Spannung am DC-Eingang/Ausgang (für Umrechnung siehe 4.4)
3 Input 1 word Zyklischer Istwert Strom am DC-Eingang/Ausgang (für Umrechnung siehe 4.4)
4 Input 1 word Zyklischer Istwert Leistung am DC-Eingang/Ausgang (für Umrechnung siehe 4.4)
Für azyklische Kommunikation werden die Slots 5-12 nur indirekt verwendet, und zwar über einen aus der Slotnum-
mer und der sog. ID (wird bei Profibus verwendet) errechneten "Index". Der Index, zusammen mit Slot 0 und Subslot
1 reicht aus, um alle gemäß Registerliste adressierbaren Objekte zu verwenden. Die Registerlisten der 10000er
Serien enthalten ab der Ausgabe, die zur Firmware KE 3.02 paßt, bereits diesen Indexwert in einer separaten
Spalte, der ansonsten leicht berechnet werden kann, wie in „6.7.1. Fernsteuerung aktivieren/deaktivieren“ gezeigt.
6.5 Zyklische Kommunikation über Profibus/Profinet
Der Profibus/Profinet-Slave sendet zyklische Daten (Istwerte & Status) auf bestimmte Eingangsadressen (Slots
1-4), wenn durch den Anwender für Profibus (siehe „6.3. Slot-Konfiguration für Profibus“) oder Profinet (siehe „6.4.
Slot-Konfiguration für Profinet“) korrekt definiert. Diese Daten sind, sofern es sich um Istwerte handelt, gemäß
„4.4. Umrechnung der Soll- und Istwerte“ bzw. den dieser Anleitung zugehörigen sogenannten Registerlisten zu
interpretieren. Als Hilfe sind die Slots in der GSD teils so benamt wie die zugehörigen Register in der Registerliste
(in Anlehnung an das intern verwendete ModBus-Protokoll). Zum Beispiel ist der Istwert Strom in der Profibus-GSD
mit „Actual current“ einem der Slots zugeordnet, wiederzufinden in der Registerliste für alle Serien an Position 508
und an dieser Stelle auch für den Gebrauch mit Profibus/Profinet freigegeben, indem für dieses Register ein Slot
und ein Index angegeben sind. Das Prinzip gilt für alle Register, denen ein Slot/Index zugeordnet wurde.
Gemäß den Abschnitten 6.3 bzw. 6.4 gibt es bis zu 12 Slots für azyklischen Datenverkehr, denen eine variable
Anzahl von Indexen (siehe Registerliste) zugeordnet ist. Über entsprechende Bausteine (SFB52, SFB53) kann
azyklisch lesend und schreibend auf die sich ergebenden IDs zugegriffen werden. Die Slots für den azyklischen
Zugriff werden nur wegen der Reservierung der Slotadressen und des Speicherbereiches plaziert. Dabei ist irre-
levant, daß sie nur Eingangsadressen belegen.
Sollwerte, setzbarer Status und die meisten anderen Register werden aus verschiedenen Grün-
den nicht zyklisch übertragen. Einer der Gründe ist die hohe Anzahl an Registern, die nicht über
die verfügbaren 16 Slots und deren max. Datenbreite abgedeckt werden können.
6.6 Azyklische Kommunikation über Profibus/Profinet
Azyklische Kommunikation mit dem Gerät erfolgt über die Slotnummern 1-12, genauer gesagt über deren resultie-
rende ID, und den sog. Indexen, die man mittels der Systembausteine (STEP7 o. ä.) oder Funktionen (TIA Portal
o. ä.) anwählt und dann liest bzw. schreibt. Wird die Siemens Software STEP7 verwendet, werden hier üblicher-
weise SFB52 und SFB53 verwendet. IN TIA Portal, also aktuellen Versionen von STEP7, sind es die Funktionen
WRREC und RDREC. Andere SPS-Steuerungssoftwares bieten ähnliche Möglichkeiten.
Diese azyklischen SFBs/Funktionen benötigen eine „ID“, einen „Index“ und den Parameter selbst. Die Parameter
sind gemäß „4.4. Umrechnung der Soll- und Istwerte“ oder den Registerlisten anzugeben.
In der Registerliste sind zwei Spalten nur für Profinet/Profibus vorgesehen, die für einen bestimmten Befehl (hier
"Register", aus der ModBus-Terminologie) den Slot und den Index definieren. Dabei gilt:
• Register, für die kein Slot/Index eingetragen sind, werden über Profibus und Profinet nicht unterstützt
Die generelle Vorgehensweise für die Fernsteuerung eines Gerätes ist:
1. Fernsteuerung per Befehl aktivieren (falls von Seiten des Gerätes nicht blockiert, siehe auch „3.2. Bedienorte“)
2. Gerät fernsteuern bzw. überwachen, über zyklischen (DP-V0) und/oder azyklischen (DP-V1) Zugriff
3. Fernsteuerung beenden
Will man nur Daten vom Gerät lesen (Aufzeichnung, Logging) ist keine Fernsteuerung und auch keine Aktivierung
selbiger erforderlich. Man kann dann jederzeit Befehle an das Gerät zur Anfrage von Daten schicken und das
Gerät sollte, sofern die Situation des Gerätes es zuläßt, umgehend antworten.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 110
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Der Feldbus stellt sicher, daß der Befehl beim Gerät ankommt, anderenfalls wird ein Fehler generiert. Er kann
jedoch nicht feststellen, daß es den Befehl auch akzeptiert bzw. bereits umgesetzt hat. Die erfolgreiche Übernahme
eines Wertes oder Status‘ kann nur durch späteres Rücklesen überprüft werden. Ob ein Gerät einen Wert auch
tatsächlich am DC-Ausgang/DC-Eingang gesetzt hat, kann nicht eindeutig durch Rücklesen festgestellt werden.
6.7 Beispiele für azyklische Kommunikation
Die Beispiele unten beziehen sich auf die Verwendung der von Fa. Siemens hergestellten Steuerungssoftware
STEP7, welche in früheren Versionen Funktionsblöcke (SFB52, SFB53) für azyklischen Zugriff (DP-v1) bereit-
stellte, die in neueren Versionen (TIA Portal) nun als Funktionen namens RDREC (Datensatz lesen) und WRREC
(Datensatz schreiben) implementiert sind und dieselben Parameter ID, INDEX und MLEN als Eingang benötigen.
Diese drei müssen ermittelt werden, wobei die ID für ein bestimmtes Gerät immer gleich bleibt.
6.7.1 Fernsteuerung aktivieren/deaktivieren
Fernsteuerung ist nicht der Standardzustand des Gerätes und muß daher von der Steuerung beim Gerät explizit
angefragt werden. Je nach Einstellung und aktuellem Zustand des Gerätes kann es den Wechsel in Fernsteuerung
auch verweigern.
► So aktivieren bzw. deaktivieren Sie die Fernsteuerung des Gerätes über Profibus oder Profinet
1. Finden Sie in der Registerliste den passenden Befehl, hier: Register 402 - Fernsteuerungsmodus.
2. Ermitteln Sie die Werte von Slot und Index (dezimal) in den entsprechenden Spalten der Registerliste, hier
für das Beispiel sind das Slot 2 und Index 1. Für Profinet, zumindest falls die Registerliste eine separate
Spalte für den Profinet-Index enthält (diese Listen werden immer wieder mal aktualisiert), dort ablesen,
ansonsten berechnen (siehe Schritt 4).
3. Profibus: Für ältere CPUs wie die 300er Reihe lesen Sie aus der Slot-Konfiguration des Gerätes die E/A-Adresse für
Slot 2 ab, um den Parameter „ID“ zu erhalten. Dieser ist standardmäßig 260 bzw. anders dargestellt DW#16#104.
Profinet: Für neuere CPUs wie die 1200er, welche standardmäßig nur Profinet bieten, ist die ID gleich der
"Hw_Kennung" aus den Systemkonstanten des Slots 2.
4. Die aus der Registerliste entnommenen Werte für "Slot" und "Index" (Achtung, Kleinschreibung zwecks
Unterscheidung!) gehen in den Eingabe-Parameter INDEX für azyklische Bausteine über:
Profibus: INDEX = Index = 1
ID = wie abgelesen, z. B. 260 bzw. DW#16#104
MLEN = 2 (entspricht einem ModBus-Register)
Profinet: INDEX (berechnet) = Slot aus Registerliste * 255 + 1 + Index aus Registerliste = 512 (0x200)
ID = wie abgelesen, z. B. 260 bzw. DW#16#104, oder wie aus der "Hw_Kennung" abgelesen
MLEN = 2 (Länge in Bytes, entnommen aus der Registerliste für Register 402)
5. Nehmen Sie in Ihrer Automatisierungssoftware einen geeigneten Baustein, zum Beispiel SFB53 / DB53,
oder eine Funktion wie WRREC.
6. Lesen Sie aus den Spalten „Daten“ und „Beispiel“ den für diesen Befehl zu verwendenden Steuerwert aus:
0xFF00 = Fernsteuerung aktivieren
0x0000 = Fernsteuerung deaktivieren
7. Geben Sie den Steuerwert entsprechend der gewünschten Funktion am Eingang REQ ein, zusammen mit
den anderen drei und führen Sie den Baustein SFB53 bzw. die Funktion WRREC aus. Das Gerät sollte nun
in die Fernsteuerung wechseln bzw. diese verlassen.
6.7.2 Einen Sollwert setzen
Setzbefehle, also jene Befehle, die etwas am Gerät einstellen oder dessen Zustand verändern, setzen bereits
aktivierte Fernsteuerung voraus. Siehe dazu „6.7.1. Fernsteuerung aktivieren/deaktivieren“ und „3.2. Bedienorte“.
Bevor Sie einen Sollwert schicken, müssen Sie zunächst auswählen, welchen Sie setzen wollen und müssen
diesen ggf. vorher noch umrechnen, da Sollwerte als Prozentwert vom Nennwert übertragen werden. Siehe dazu
auch „4.3. Format der Sollwerte und Auflösung“ und „4.4. Umrechnung der Soll- und Istwerte“.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 111
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
► So setzen Sie einen Stromsollwert
1. Finden Sie in der Registerliste den passenden Befehl, hier: Register 501 - Sollwert Strom.
2. Ermitteln Sie die Werte von Slot und Index (dezimal) in den entsprechenden Spalten der Registerliste, hier
für das Beispiel sind das Slot 2 und Index 24. Für Profinet, zumindest falls die Registerliste eine separate
Spalte für den Profinet-Index enthält (diese Listen werden immer wieder mal aktualisiert), dort ablesen,
ansonsten berechnen (siehe Schritt 4).
3. Profibus: Für ältere CPUs wie die 300er Reihe lesen Sie aus der Slot-Konfiguration des Gerätes die E/A-Adresse für
Slot 2 ab, um den Parameter „ID“ zu erhalten. Dieser ist standardmäßig 260 bzw. anders dargestellt DW#16#104.
Profinet: Für neuere CPUs wie die 1200er, welche standardmäßig nur Profinet bieten, ist die ID gleich der
"Hw_Kennung" aus den Systemkonstanten des Slots 2.
4. Die aus der Registerliste entnommenen Werte für "Slot" und "Index" (Achtung, Kleinschreibung zwecks
Unterscheidung!) gehen in den Eingabe-Parameter INDEX für azyklische Bausteine über:
Profibus: INDEX = Index = 1
ID = wie abgelesen, z. B. 260 bzw. DW#16#104
MLEN = 2 (entspricht einem ModBus-Register)
Profinet: INDEX (berechnet) = Slot aus Registerliste * 255 + 24 + Index aus Registerliste = 535 (0x217)
ID = wie abgelesen, z. B. 260 bzw. DW#16#104, oder wie aus der "Hw_Kennung" abgelesen
MLEN = 2 (Länge in Bytes, entnommen aus der Registerliste für Register 501)
5. Nehmen Sie in Ihrer Automatisierungssoftware einen geeigneten Baustein, zum Beispiel SFB53 / DB53,
oder eine Funktion wie WRREC.
6. Lesen Sie aus den Spalten „Daten“ und „Beispiel“ die für diesen Befehl zu verwendenden Wertebereich aus:
0x0000...0xCCCC (dez. 52428) = Strom 0...100%. Errechnen Sie nun den Sollwert. Für ein Modell mit bei-
spielsweise 170 A Nennwert und gewünschten 10 A wäre das 52428÷17 = 3084 --> 0x0C0C.
7. Geben Sie den Steuerungswert am Eingang REQ des Bausteins SFB53 bzw. der Funktion WRREC ein,
zusammen mit ID und INDEX und führen Sie den Baustein aus. Das Gerät sollte nun 10 A Strom setzen. Dies
kann unter Anderem in der Anzeige des Gerätes nachgeschaut werden, wo der Stromsollwert angezeigt wird.
6.7.3 Etwas auslesen
Lesend kann jederzeit auf das Gerät zugegriffen werden, also auch ohne Fernsteuerung. Neben den zyklisch
übertragenen Werten können alle lesbaren Informationen auch azyklisch abgefragt werden.
► So lesen Sie die Istwerte von Spannung und Strom aus
1. Finden Sie in der Registerliste das passende Register, hier von Istwert Spannung. Das Register vom Istwert
Strom liegt direkt dahinter, daher wird gewählt: Register 507 - Istwert Spannung.
2. Ermitteln Sie die Werte für ID, INDEX und MLEN wie in den obigen Beispielen gezeigt und geben Sie diese
zusammen der Anzahl der zu lesenden Daten (4 Bytes oder 2 Words, abhängig davon, wie die Software
den Eingang definiert) am Eingang REQ des Bausteins SFB52 bzw. der Funktion RDREC an.
3. Führen Sie den Baustein aus. Im Datenpuffer des Bausteins sollten 4 Bytes erscheinen.
Die ausgelesenen 4 Bytes enthalten dann in den ersten 2 Bytes den Spannungsistwert als Prozentwert (Umrech-
nung siehe „4.4. Umrechnung der Soll- und Istwerte“) und in den letzten 2 Bytes den Stromistwert. Die Register
können durch Variieren der Datenlänge auf 6 auch den Leistungsistwert mit enthalten oder wahlweise einzeln
ausgelesen werden. Dann müßte der Parameter INDEX angepaßt werden und die Datenlänge wäre immer 2.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 112
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
6.8 Interpretation von Eingangsdaten
Die vom Gerät auf Anfrage oder ohne Anfrage zurückgegebenen Daten, allen voran die zyklischen, müssen für
die Weiterverwendung interpretiert werden. Hier wird das anhand eines Profibus Master-Simulator-Fensters bei-
spielhaft erläutert. Siehe auch „4.4. Umrechnung der Soll- und Istwerte“.
Das Beispiel links zeigt die Daten von einer Konfiguration mit 8 Slots. Da für zy-
klischen Transfer (DP-V0) nur die Slots 1-4 benutzt werden, bleibt der Rest leer.
Slot 1: „Device status“, gehört zu Register 505. Der Wert 0x000004C0 gibt an,
daß Bits 6, 7 und 10 gesetzt sind,was bedeutet, das Gerät ist als Master konfi-
guriert (für Master-Slave), der DC-Eingang/Ausgang ist an und Regelung ist CC.
Slot 2: „Actual voltage“ (Spannungsistwert), gehört zu Register 507. Bei z. B. einem
250 V-Modell berechnet sich der Wert 0x263A zu 250 V*0x263A/52428=46,7 V.
Slot 3: „Actual current“ (Stromistwert), gehört zu Register 508. Bei z. B. einem
510 A-Modell, berechnet sich der Wert 0x0C9B zu 510 A*0xC9B/52428=31,4 A.
Slot 4: „Actual power“ (Leistungsistwert), gehört zu Register 509. Bei z. B. einem
5 kW-Modell berechnet sich der Wert 0x0925 zu 5000 W*0x925/52428=223 W
Slot 5: nicht genutzt für zyklische Daten
Slot 6: nicht genutzt für zyklische Daten
Slot 7: nicht genutzt für zyklische Daten
Slot 8: nicht genutzt für zyklische Daten
Für Anwender eines PSB-Gerätes: die Istwerte von Strom und Leistung werden im Senke-Betrieb
auf der Anzeige des Gerätes mit negativem Vorzeichen dargestellt. Das gibt die Registerdefinition
der Istwerte bei Erfassung über analoge und digitale Schnittstellen nicht her. Die Betriebsart,
also Quelle- oder Senkebetrieb, wird über Bit 12 im "Device status"-Register 505 (zyklisch oder
azyklisch lesbar) signalisiert. Mit Hilfe des Bits können Istwerte nach dem Auslesen und für
spätere Weiterverarbeitung negiert werden.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 113
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
7. CANopen
Bei CANopen sind die für ein Gerät verfügbaren Kommunikationsobjekte üblicherweise in einer EDS/XDD-Datei
(Electronic Data Sheet) definiert. Sie wird mit dem Gerät auf USB-Stick mitgeliefert bzw. kann online von der Webseite
des Herstellers des Gerätes abgerufen werden. Das EDS kann in entsprechender Software eingebunden werden.
Die EDS-Indexe werden nicht gesondert erläutert, weil ihre Funktion identisch ist zu den ModBus-Registern in den
externen Registerlisten (siehe „4.7. Über die Register-Listen“). Beispiele aus der ModBus-Protokollbeschreibung
(siehe „4.8.7. Beispiele für ModBus RTU-Telegramme“) können für CANopen übernommen werden, jedoch redu-
ziert auf den eigentlichen Dateninhalt, weil der Anwender bei CANopen mit Checksummen und Funktionsnummern
nicht konfrontiert wird.
CANopen als Datenübertragungsprotokoll wird auch bei EtherCAT verwendet. Der Unterschied ist dort, daß
man kein EDS/XDD laden muß bzw. nicht laden kann und die sog. Objektliste aus dem Gerät herunterlädt, in die
Steuerungsumgebung. Dieser Abschnitt gilt gleichsam für EtherCAT-Anwender, da das Gerät hauptsächlich über
SDO-Zugriff steuerbar ist.
Das CANopen-Modul IF-AB-CANO bietet keinen Busabschlußwiderstand. Daher muß die Bu-
sterminierung hier am Kabel erfolgen.
7.1 Einschränkungen
Intern ist Kommunikation auf ModBus basiert, das einen Registersatz hat, der bei Adresse 0 anfängt. Da bei CA-
Nopen der Benutzerbereich von 0x2001 bis 0x5FFF positioniert ist, werden die ModBus-Adressen um den Betrag
0x2001 für die Addressierung in CANopen verschoben. Dabei wird der Registersatz und seine Adressaufteilung,
wie in den Registerlisten aufgeführt, beibehalten. Das bedeutet, daß man bei CANopen nicht alle Features des
Gerätes nutzen kann, denn man kann nur bis Register 16383 adressieren.
7.2 Vorbereitung (nicht EtherCAT)
Was wird für die Kommunikation mit einem Gerät über CANopen-Modul IF-AB-CANO benötigt?
1. CAN-Kabel mit gewünschter Länge und fest installiertem oder am Kabel schaltbarem Abschlußwiderstand,
der eingeschaltet werden muß, wenn sich das Gerät am Ende der CAN-Leitung befindet, wie es z. B. bei einer
Direktverbindung zwischen PC und einer elektronischen Last ELR 9000 o. ä. der Fall wäre.
2. EDS- oder XDD-Datei (wird mit dem Gerät auf USB-Stick geliefert).
3. CANopen-Software für den PC (nicht mitgeliefert, jede entsprechende sollte nutzbar sein)
4. Anleitung für die Verwendung der CANopen-Indexe. Siehe Abschnitte 1. - 4., 7.3 und 9., sowie die externen
Registerlisten-PDFs.
7.3 Anwendung der Benutzerobjekte (Indexe)
Das über CANopen verwendete Datenformat ist an ModBus angelehnt. Ein bestimmter Index ist dabei mit einem
bestimmtem ModBus-Register verbunden. Der CANopen-Standard gibt vor, Benutzerobjekte ab Index 2001 anzusie-
deln. Bei ModBus wird ab Adresse 0 gezählt. Somit sind alle ModBus-Register bei CANopen um den Wert 0x2001
verschoben und daher entspricht Index 2001 der Registeradresse 0 und z. B. Index 21F5 der Registeradresse 500
usw. Die mit dieser Anleitung mitgelieferten Registerlisten (je eine pro Geräteserie) dienen auch bei CANopen als
Ausgangsbasis. Dort ist Register 500 bei einem ELR 9000-Gerät dann als „Sollwert Spannung“ definiert und gibt
auch das Datenformat und den Wertebereich vor.
Das EDS/XDD enthält weniger Indexe als das Gerät ModBus-Register unterstützt, um eine gewisse Übersicht
beizubehalten. Die wichtigsten Funktionen des Gerätes sind jedoch abgedeckt. Der Anwender kann jedoch
Indexe einfach hinzufügen. Die an den Index zu sendenden Daten sind in der Registerliste definiert und in den
vorangehenden Abschnitten, die das ModBus-Protokoll erläutern, teils mit Beispielen veranschaulicht, die auch
für CANopen nutzbar sind. Weitere Beispiele finden Sie unten.
7.3.1 Umrechnung Index -> Register
Die Umrechnung des Index zu einer Registeradresse ist denkbar einfach durch den festen Offset 0x2001. In dem
EDS finden Sie z. B. Index „207A Nominal voltage“. Das berechnet sich zu Register 121:
Indexnummer - Offset = Register --> 207A - 2001 = 79 (hex) = 121 (dez). Laut Registerliste ist das der Spannungs-
nennwert des Gerätes als Floatwert (4 Bytes). Bei CANopen gibt es den Datentyp FLOAT nicht, daher ist der Index
hier als REAL32 definiert. Der Anwender muß dann lediglich nach IEEE 754 umrechnen.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 114
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
7.4 Konkrete Beispiele
7.4.1.1 Fernsteuerung übernehmen
Wie in „4.8.7.5. Fernsteuerung aktivieren oder beenden“ beschrieben, muß nach dem Einschalten des Gerätes
und bevor man es fernsteuern kann, zuerst die Fernsteuerung übernommen werden. Dazu muß man zunächst
das passende Register in der Registerliste oder den passenden Index im EDS finden. In dem Fall ist es Register
402 bzw. Index 2193. Der zu sendende Datenwert ist in der Registerliste definiert. Laut dieser ist der Wert 0xFF00
zu senden, um die Fernsteuerung zu übernehmen, und 0x0000, um sie wieder zu beenden.
7.4.1.2 Einen Sollwert setzen
Nachdem die Fernsteuerung übernommen wurde, können Sie Sollwerte an das Gerät schicken. Diese repräsentieren
einen Prozentwert des jeweiligen Nennwertes. Sollwerte können zyklisch oder azyklisch übertragen werden.Laut
Definition der Sollwertregister (siehe Registerliste) entsprechen 100% dem Hexwert 0xCCCC und 0% = 0x0000.
Es sind also 52429 Werte zwischen 0 und 100% verfügbar. An diesem Punkt sei darauf hingewiesen, daß das
nicht der tatsächlichen Auflösung des Gerätes entspricht, die ein Wert am DC-Eingang / DC-Ausgang hat. Die
tatsächliche Auflösung liegt bei der Hälfte, also 26214 Werten. Ein Berechnungsbeispiel für Sollwerte finden Sie
in „4.8.7.1. Einen Sollwert setzen“.
7.5 Besonderheiten gegenüber ModBus
Das bei CANopen verwendete Werteformat und Objektadressierung sind von ModBus abgeleitet und auf das
hierfür Nötigste reduziert.
7.5.1 Bei Verwendung des Arbiträrgenerators
Weil CANopen in einer Nachricht max. 4 Nutzdatenbytes übertragen kann, werden die 8 Parameter eines Se-
quenzpunktes des Arbiträrgenerators nicht alle auf einmal, sondern getrennt übertragen. Das Gerät prüft zwar
jeden einzelnen Wert bei Empfang auf Plausibilität, aber nachdem alle Sequenzdaten ohne Fehler empfangen
wurden, müssen sie mit einem zusätzlichen Befehl (Index 235F) übernommen werden.
Erst dieser Befehl lädt den Funktionsgenerator und gibt den Start frei. Wird der Befehl nicht gesendet, verwendet
der Funktionsgenerator alte Werte.
Die Schritte zur Konfiguration und zum Laden der Funktionsdaten sind über CANopen identisch mit der Vorge-
hensweise bei Verwendung einer anderen Schnittstelle und direkten ModBus-Nachrichten, wie in Abschnitt 4.11.8.1
beschrieben,
Schritt 1:
Auswahl, ob die Funktion auf die Spannung U (Index 2354) oder den Strom I (Index 2355) angewendet werden
soll. Bevor das nicht erfolgt ist, kann das Gerät keine Sequenzpunktdaten annehmen.
Schritt 2:
Endsequenzpunkt (Index 235D), Startsequenzpunkt (Index 235C), sowie Sequenzpunktzyklen (Index 235E)
festlegen.
Schritt 3:
Sequenzpunktdaten laden für alle benötigten Sequenzpunkte (Indexe 2385 - 29A5, pro Sequenzpunkt 8 Werte in
Subindexen).
Schritt 3.1:
Sequenzdaten übernehmen durch Schreiben von 0xFF00 auf Index 235F (Register 862).
Schritt 4:
Obergrenze für den Strom (Index 21F6) setzen, falls Funktion auf die Spannung angewendet. Ansonsten Ober-
grenze für die Spannung (Index 21F5) setzen, falls Funktion auf den Strom angewendet wird. Obergrenze für die
Leistung (Index 21F7) für beide Modi setzen.
Schritt 5:
Funktionsgenerator starten bzw. stoppen (Index 2353) bzw. falls nötig noch den DC-Eingang/Ausgang einschalten
(Index 2196).
Schritt 6:
Zum Verlassen des Funktionsgenerators die Auswahl U (Index 2354) bzw. I (Index 2355) von Schritt 1 wieder
rückgängig machen, durch Schreiben von 0x0000.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 115
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
7.6 CANopen-spezifische Fehlercodes
Das CANopen-Schnittstellenmodul unterstützt vom CANopen Standard übernommene bzw. an diesen angelehnte
Fehlercodes:
Codenummer Beschreibung
0x06020000 Objekt im Objektverzeichnis (ModBus-Registerliste) nicht vorhanden
0x06040043 Nicht unterstützter Befehl
0x06099911 Sub-Index existiert nicht
0x06010002 Es wurde versucht, ein „nur lesen“ Objekt zu schreiben
0x06010002 Es wurde versucht, ein „nur schreiben“ Objekt zu lesen
0x06070012 Falsche Datenlänge (zu viele Daten)
0x06070013 Falsche Datenlänge (zuwenig Daten)
0x06090030 Wert außerhalb des zulässigen Bereiches
0x08000022 Daten/Status konnte aufgrund des momentanes Zustandes des Gerätes nicht übertragen
oder gesetzt werden
0x05040005 Speicherfehler (kein Speicher mehr frei)
0x08000000 Allgemeiner Fehler
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 116
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
8. CAN
Dieser Abschnitt bezieht sich ausschließlich auf die CAN-Kommunikation über die CAN-Schnittstelle IF-AB-CAN.
Einstellungen zu dieser Schnittstelle werden am Gerät im Setup-Menü erledigt, sind aber über Fernsteuerung (z.
B. USB) konfigurierbar. Siehe dazu auch das Gerätehandbuch.
8.1 Vorbereitung
Was wird für die Kommunikation mit einem Gerät über CAN-Modul IF-AB-CAN benötigt?
1. Ein CAN-Kabel mit gewünschter Länge. Ein mechanisch schaltbarer Abschlußwiderstand am Kabel ist nicht
erforderlich, da das Schnittstellenmodul einen elektronisch geschalteten hat. Sollte das Kabel jedoch einen
haben, muß sichergestellt werden, daß nicht beide Abschlußwiderstände eingeschaltet sind, weil sonst Bus-
fehler auftreten könnten.
2. Bei Verwendung von Vector™ Softwares oder anderen, die mit sog. DBC-Dateien arbeiten: eine möglichst zum
Gerät passende Datenbasis (DBC). Diese wird üblicherweise vom Hersteller des Gerätes angeboten, kann
vom Anwender aber auch komplett selbst erstellt werden, z. B. durch Modifikation einer ähnlichen.
3. CAN-Software für den PC (nicht mitgeliefert, jede entsprechende sollte nutzbar sein).
4. Anleitung für die Verwendung der CAN-Objekte. Siehe unten und auch Abschnitte 1. - 4., sowie die mitgelie-
ferten Registerliste(n).
8.2 Einführung
Das verwendete Datenformat ist an das weiter vorn in diesem Dokument beschriebene ModBus RTU angelehnt.
Bezogen auf eine Datenbasis (DBC) stellt ein Mux-Wert ein bestimmtes ModBus-Register oder Objekt dar.
Befehle werden in der Datenbasis also über den Mux-Wert ausgewählt. Bei direkter Programmierung einer CAN-
Nachricht im Buffer (CAPL o. ä.) definieren die ersten beiden Daten-Bytes das Register (Objekt, Befehl), auf das
zugegriffen werden soll. Durch die Wahl der CAN-ID wird zwischen Lesen und Schreiben selektiert.
Das Gerät bietet aus diesem Grund immer drei CAN-IDs zur Verwendung, die mit der sog. Basis-ID am Gerät
definiert werden. Die Basis-ID (engl. base ID) wird zum Schreiben an das Gerät (Botschaft Send_Object) be-
nutzt, die Basis-ID + 1 zum Abfragen von Daten vom Gerät (Botschaft Query_Object) und Basis-ID + 2 wird vom
Gerät verwendet, Antworten (Botschaft Read_Object) zu senden. Antworten kommen auf Anfragen, aber auch
ungefragt bei Kommunikations- oder Zugriffsfehlern. Mit Einstellung der Basis-ID verschieben sich die anderen
beiden automatisch mit.
Es gibt weiterhin eine pro Gerät separat einstellbare Broadcast-ID welche dazu dienen kann, auf mehrere Geräte
mit gleicher Broadcast-ID gleichzeitig etwas zu schreiben (Send-Object). Anfragen an mehrere Geräte gleichzeitig
über einen (Broadcast-)Befehl sind nicht möglich.
Außer der Basis-ID und der Broadcast-ID für azyklischen Zugriff können bei einigen Serien weitere IDs für zyklische
Statusdaten eingestellt werden. Das Gerät sendet auf diesen IDs permanent Daten, sofern aktiviert und sobald
die CAN-Verbindung hergestellt wird. Für die Konfiguration der zyklischen Daten siehe Handbuch des Gerätes,
dort den Abschnitt zu den Kommunikations-Einstellungen im Setup-Menü.
8.3 Telegrammtypen
8.3.1 Normales Schreiben
Schreiben oder Setzen eines Wertes erfolgt immer über die Basis-ID oder die Broadcast-ID und erfordert in der
CAN-Nachricht die Angabe der Objektnummer, d. h. die Adresse eines ModBus-Registers bzw. -Startregisters,
sowie die Anzahl der zu schreibenden Register und eine bestimmte Anzahl von nachfolgenden Parameter-Bytes,
die verschiedene Datentypen repräsentieren können.
Zugehörige ModBus-Funktionen: Write Single Coil (WSC), Write Single Register (WSR)
Zugriff über: Basis-ID, Broadcast-ID
Bytes 0+1 Byte 2 Bytes 3+4
Register Anzahl Register Datenwort (16 Bit)
0...65534 Immer 1 Zu schreibender Wert
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 117
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Zugehörige ModBus-Funktion: Write Multiple Registers (WMR)
Zugriff über: Basis-ID, Broadcast-ID
Bytes 0+1 Byte 2 Byte 3 Bytes 4-7
Startreg. Anzahl Register Kennung Datenbytes
0...65534 2...123 0xFF, 0xFE... Vier Bytes oder zwei 16-Bit-Werte oder ein 32-Bit-Wert
Startregister: immer das in der Registerliste angegebene für den Befehl
Anzahl Register: siehe Registerliste. Wenn ein Objekt auf 40 Bytes Länge definiert ist, dann sind das 20 Register,
also würde hier eine 20 eingetragen.
Kennung: dient zur Erkennung der Reihenfolge mehrerer zusammenhängender Nachrichten. Ein String wie z. B.
der Benutzertext, der bis zu 40 Zeichen lang sein kann, muß zur Übertragung aufgeteilt werden. Jede Nachricht
kann bis zu 4 Zeichen eines Strings transportieren. Die Kennung ist absteigend zu zählen. Also erste Nachricht
0xFF, zweite Nachricht 0xFE usw. Nach diesem Schema wird der String im Gerät zusammengesetzt und gespei-
chert. Die Kennung ist erforderlich, da bei CAN nicht sichergestellt ist, daß Nachrichten in der Reihenfolge am Ziel
(PC, SPS) ankommen, wie sie vom Gerät abgeschickt wurden.
Datenbytes: Die Anzahl der Datenbytes in einer Nachricht ist immer 4, egal ob alle Bytes Nutzdaten enthalten oder
nicht. Beispiel: ein Benutzertext von 15 Zeichen Länge benötigt mindestens 4 Nachrichten zur Übertragung. Das
Objekt für den Benutzertext definiert 20 Register, also 10 Nachrichten. Da man bei 15 Zeichen weniger Register
beschreiben müßte, braucht man nur den Wert Anzahl Register entsprechend anpassen. Es ist nur wichtig, daß die
Anzahl der gesendeten Nachrichten zu Anzahl Register paßt. In dem Beispiel müßte man also Anzahl Register
mit 8 festlegen, so daß sich 4 Nachrichten und somit 16 Bytes ergeben (15 Zeichen String + Abschlußzeichen).
8.3.2 Zyklisches Schreiben
Das zyklische Schreiben ist eine zusätzliche Möglichkeit, häufig gebrauchte Sollwerte und Status zeitsparend in
einem Block zu übertragen. Dieser Block wird, je nach Geräteserie, an mehrere CAN IDs gesendet. Das Intervall,
in dem Sollwerte über die separaten ID für‘s zyklische Senden geschickt werden, definiert der Anwender mit seiner
CAN-Software zwar selbst, jedoch gelten auch hier die Timing-Empfehlungen im Abschnitt 3.3.3.
8.3.2.1 Blockteil "Steuerung"
Zugriff über: Basis-ID Zyklisches Senden
Bytes 0-1
Steuerwort
Aufteilung des Steuerwortes:
Zugehöriges
Bit Name Bedeutung
Register
8 Fernsteuerung 402 Aktiviert mit 1 bzw. deaktiviert mit 0 die Fernsteuerung des Gerätes
9 Eingang/Ausgang 405 Schaltet den DC-Eingang/-Ausgang des Gerätes mit 1 ein bzw. mit 0 aus
Schaltet mit 1 Widerstandsregelung (UIR-Modus, wo vorhanden) frei,
10 UIP / UIR 409
bei 0 ist dann UIP aktiv
Nur für el. Lasten der 9000er Serien (EL/ELR): Schaltet mit 1 den
Spannungsregler auf „schnell“ bzw. mit 0 auf „langsam“
11 Spannungsregler 422 Hinweis: hiermit kann nicht die Spannungsreglergeschwindigkeit bei den
10000er Serien umgeschaltet werden, da diese ein anderes Register
verwenden.
12 Alarme 411 Quittiert mit 1 alle löschbaren Alarme
Dieses Steuerwort ist mit Vorsicht zu behandeln, weil alle 5 Bits gleichzeitig Aktionen auslösen
können, die gegeneinander keine Prioritätsregelung haben. Das heißt, würde man versuchen,
gleichzeitig die Fernsteuerung zu aktivieren und den DC-Eingang/-Ausgang einzuschalten (Bit
0 und 1 beide logisch 1), kann es passieren, daß man einen Zugriffsfehler zurückgemeldet
bekommt, weil das Gerät zufällig Bit 9 vor Bit 8 verarbeitet hat.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 118
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 8.3.2.2  | Blockteil "Sollwerte 1" |     |     |     |
| -------- | ----------------------- | --- | --- | --- |
Zugriff über: Basis-ID Zyklisches Senden + 1
| Bytes 0-1    |     | Bytes 2-3    | Bytes 4-5    | Bytes 6-7    |
| ------------ | --- | ------------ | ------------ | ------------ |
| Register 500 |     | Register 501 | Register 502 | Register 503 |
Sollwert Spannung Sollwert Strom Sollwert Leistung Sollwert Widerstand
Bei den PSB Serien gehören diese 4 Sollwerte zum Quelle-Betrieb, im HMI unter "Basis-ID
Senden" angezeigt als "Sollwerte [PS]". Der Blockteil gehört auch für Serie PSBE zum Quelle-
betrieb, dort jedoch ohne den Sollwert Widerstand.
| 8.3.2.3  | Blockteil "Sollwerte 2" (nur PSB/PSBE Serien) |     |     |     |
| -------- | --------------------------------------------- | --- | --- | --- |
Zugriff über: Basis-ID Zyklisches Senden + 2
| Bytes 0-1    |     | Bytes 2-3    | Bytes 4-5    |     |
| ------------ | --- | ------------ | ------------ | --- |
| Register 499 |     | Register 498 | Register 504 |     |
Sollwert Strom (EL) Sollwert Leistung (EL) Sollwert Widerstand (EL)
Bei den PSB Serien gehören diese 3 Sollwerte zum Senke-Betrieb, im HMI unter "Basis-ID
Senden" angezeigt als "Sollwerte [EL]". Der Blockteil gehört auch für Serie PSBE zum Quelle-
betrieb, dort jedoch ohne den Sollwert Widerstand.
| 8.3.3  | Abfragen |     |     |     |
| ------ | -------- | --- | --- | --- |
Das	Abfragen	eines	Objekts	ist	der	erste	Teil	eines	Lese-Vorgangs.	Er	findet	immer	über	Basis-ID	+	1	statt.	Das
Gerät antwortet dann erwartungsgemäß auf der Basis-ID + 2, auf Read_Object. Damit ist der Lesevorgang abge-
schlossen. Zur Abfrage eines Objekts über die Abfrage-ID (Basis-ID + 1) reicht es aus, nur die Startregister-Nummer
anzugeben.	Das	Gerät	sollte	dann	die	zum	angefragten	Register	gehörige	Anzahl	Bytes	zurückliefern,	allerdings
in unterschiedlichen Antwortformaten. Siehe 8.3.4.
Zugehörige ModBus-Funktionen: Read Coils (RC), Read Holding Registers (RHR)
Zugriff über: Basis ID + 1
Bytes 0+1
Startreg.
0...65534
| 8.3.4  | Normales Lesen |     |     |     |
| ------ | -------------- | --- | --- | --- |
Die vom Gerät nach einer Anfrage oder in einer Fehlernachricht gesendeten Daten, die sich üblicherweise in einem
Puffer	befinden	bzw.	bei	Software	der	Fa.	Vector	durch	die	Datenbasis	automatisch	in	Signale	verteilt	werden,
bilden eine Antwort. Geteilte Antworten müssen nach dem Erhalt noch programmiertechnisch und anhand der
Kennung in der richtigen Reihenfolge zusammengesetzt werden. Es ist aber nur in wenigen Fällen erforderlich,
weil längere Objekte wie z. B. der Benutzertext nicht ständig gelesen werden.
Eingehend vom Gerät über: Basis ID + 2
Antwort in einer Nachricht (Anzahl angefragter Register 1-3):
| Bytes 0+1 | Bytes 2-7    |     |     |     |
| --------- | ------------ | --- | --- | --- |
| Register  | Daten        |     |     |     |
| 0...65534 | 1-3 Register |     |     |     |
Antwort in mehreren Nachrichten (Anzahl angefragter Register >3):
| Bytes 0+1 | Byte 2        | Bytes 3-7 |     |     |
| --------- | ------------- | --------- | --- | --- |
| Register  | Kennung       | Daten     |     |     |
| 0...65534 | 0xFF, 0xFE... | 5 Bytes   |     |     |
Der Wert in Byte 2 kann nicht für die Erkennung auf eine geteilte Antwort verwendet werden, auch dann nicht, wenn
die	nächste	Nachricht	0xFE	enthält.	Einzelne	Register	können	auch	den	Inhalt	0xFF	usw.	im	Byte	2	zurückgeben.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 119
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
Antwort als Fehlernachricht:
Bytes 0+1 Byte 2
65535 Fehlercode
Die	Fehlercodes	sind	zwar	teils	identisch	mit	denen	von	ModBus,	aber	teils	CAN-spezifisch.	Siehe	„8.3.6. Kom-
munikationsfehlercodes“.
8.3.5   Zyklisches Lesen
Das zyklische Lesen ist eine zusätzliche Funktion des Gerätes, durch die es bestimmte Objekte automatisch an
benutzerdefinierbare	IDs	und	in	einem	benutzerdefinierbaren	Intervall	senden	kann.	Das	eingehende	Nachrich-
tenformat ist hier abweichend vom Format beim normalen "azyklischen" Lesen.
Um zyklisches Lesen zu aktivieren und zu nutzen, muß der Anwender:
1.  die extra Basis-ID Zyklisches Lesen am Gerät einstellen (HMI, CAN-Einstellungen).
2.  von den 5 für zyklisches Lesen festgelegten Objekten auswählen, welche er zyklisch empfangen will und diese
aktivieren, indem die Zykluszeit ungleich 0 gesetzt wird.
die hierüber empfangenen Daten gesondert verarbeiten, da das Format etwas anders ist (siehe unten)
3.
Die Zykluszeiten der einzelnen Objekte sind dabei separat und beliebig einstellbar. Sollten sie sich decken, sendet
das Gerät die Nachrichten der einzelnen Objekte direkt aufeinander folgend.
Die kleinste einstellbare Intervallzeit ist 20 ms. Bei geringen CAN-Busgeschwindigkeiten wie z.
B. 10-50 kpbs können bei dieser Intervallzeit Busfehler wegen Überbelastung auftreten.
Ist zyklisches Lesen für mindestens eins der zyklischen Objekte aktiviert, sendet das Gerät sofort ab Herstellen
einer CAN-Verbindung automatisch und dauerhaft Nachrichten auf die entsprechenden IDs. Das zyklische Senden
kann jederzeit am Bedienfeld des Gerätes oder per azyklischem Befehl aus- bzw. eingeschaltet werden.
Dem zyklischen Lesen sind bis zu 6 CAN-IDs zu reservieren. Ab der einstellbaren „Basis-ID Lesen“ (siehe HMI
des	Gerätes)	sind	die	gesendeten	Daten	wie	folgt	definiert.
8.3.5.1  Nachricht "Status"
Eingehend vom Gerät über: Basis-ID Lesen
Bytes 0-3
Geräte-Status (32 Bit)
Aufteilung des Geräte-Statuswertes:
| Bit Name         | Bedeutung | Bit Name | Bedeutung |
| ---------------- | --------- | -------- | --------- |
| 31 Fernsteuerung | 1 = ein   | 15 -     |           |
30 Eingang/Ausgang 1 = ein (Soll, Register 405) 14 Alarm OVD 1 = Alarm aktiv
29 Geschw. Spgs.reg 1 = schnell (Register 422) 13 Alarm OVP 1 = Alarm aktiv
| 28 Betriebsart | 0 = UIP, 1 = UIR | 12  |     |
| -------------- | ---------------- | --- | --- |
27 Alarme 1 = mind. ein Alarm aktiv 11 Alarm PF 1 = Alarm aktiv
| 26 Alarm MSS | 1 = Alarm aktiv | 10  |     |
| ------------ | --------------- | --- | --- |
25 Alarm OCD 1 = Alarm aktiv 9 REM-SB 1 = ein (Register 505, Bit 30)
| 24 Alarm OCP | 1 = Alarm aktiv | 8 Alarm UCD   | 1 = Alarm aktiv        |
| ------------ | --------------- | ------------- | ---------------------- |
| 23           |                 | 7 Alarm UVD   | 1 = Alarm aktiv        |
| 22           |                 | 6 Fernfühlung | 1 = extern, 0 = intern |
Schnittstelle
| 21  | Register 505, Bits 4-0 | 5 Funktionsgen. | 1 = FG aktiv |
| --- | ---------------------- | --------------- | ------------ |
im	Eingriff
| 20           |                 | 4 MS-Typ          | 1 = Master, 0 = Slave         |
| ------------ | --------------- | ----------------- | ----------------------------- |
| 19           |                 | 3 Eingang/Ausgang | 1 = ein (Register 505, Bit 7) |
| 18 Alarm OPD | 1 = Alarm aktiv | 2                 |                               |
|              |                 | Reglerzustand     | Register 505, Bits 10-9       |
| 17 Alarm OPP | 1 = Alarm aktiv | 1                 |                               |
16 Alarm OT 1 = Alarm aktiv 0 PSB-Modus 0 = Quelle, 1 = Senke
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 120
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
8.3.5.2  Nachricht "Istwerte"
Eingehend vom Gerät über: Basis-ID Lesen + 1
| Bytes 0-1        | Bytes 2-3     | Bytes 4-5        |     |
| ---------------- | ------------- | ---------------- | --- |
| Register 507     | Register 508  | Register 509     |     |
| Istwert Spannung | Istwert Strom | Istwert Leistung |     |
Nur PSB/PSBE Serien: die hiermit gelesenen Istwerte enthalten kein Vorzeichen. Zwecks
Interpretation eines neg. Vorzeichens für Senke-Betrieb sollte das Bit 0 aus Block "Status"
ausgewertet werden.
8.3.5.3  Nachricht "Sollwerte 1"
Eingehend vom Gerät über: Basis-ID Lesen + 2
| Bytes 0-1    | Bytes 2-3    | Bytes 4-5    | Bytes 6-7    |
| ------------ | ------------ | ------------ | ------------ |
| Register 500 | Register 501 | Register 502 | Register 503 |
Sollwert Spannung Sollwert Strom Sollwert Leistung Sollwert Widerstand
Bei den PSB Serien gehören diese 4 Sollwerte zum Quelle-Betrieb, im HMI unter "Basis-ID Le-
sen" aufgelistet als "Sollwerte [PS]". Bei der PSBE-Serie dann ohne den "Sollwert Widerstand".
8.3.5.4  Nachricht "Limits 1"
Eingehend vom Gerät über: Basis-ID Lesen + 3
| Bytes 0-1     | Bytes 2-3     | Bytes 4-5     | Bytes 6-7     |
| ------------- | ------------- | ------------- | ------------- |
| Register 9002 | Register 9003 | Register 9000 | Register 9001 |
| I-max         | I-min         | U-max         | U-min         |
Bei den PSB/PSBE Serien gehören diese Einstellgrenzen nur zum Quelle-Betrieb, im HMI unter
"Basis-ID Lesen" aufgelistet als "Limits 1 [PS]".
8.3.5.5  Nachricht "Limits 2"
Eingehend vom Gerät über: Basis-ID Lesen + 4
| Bytes 0-1     | Bytes 2-3     |     |     |
| ------------- | ------------- | --- | --- |
| Register 9004 | Register 9006 |     |     |
| P-max         | R-max         |     |     |
Bei den PSB/PSBE Serien gehören diese Einstellgrenzen nur zum Quelle-Betrieb, im HMI unter
"Basis-ID Lesen" aufgelistet als "Limits 2 [PS]". Bei Serie PSBE dann ohne "R-max".
8.3.5.6  Nachricht "Sollwerte [EL]"
Nur	verfügbar	bei	bidirektionalen	Geräten	der	Serien	PSB	und	PSBE	(hier	ohne	"Sollwert	Widerstand").	Gehört
zum Senke-Betrieb.
Eingehend vom Gerät über: Basis-ID Lesen + 5
| Bytes 0-1    | Bytes 2-3    | Bytes 4-5    |     |
| ------------ | ------------ | ------------ | --- |
| Register 499 | Register 498 | Register 504 |     |
Sollwert Strom (EL) Sollwert Leistung (EL) Sollwert Widerstand (EL)
8.3.5.7  Nachricht "Limits [EL]"
Nur	verfügbar	bei	bidirektionalen	Geräten	der	Serien	PSB	und	PSBE	(hier	ohne	"R-max").	Gehört	zum	Senke-Betrieb.
Eingehend vom Gerät über: Basis-ID Lesen + 6
| Bytes 0-1     | Bytes 2-3     | Bytes 4-5     | Bytes 6-7     |
| ------------- | ------------- | ------------- | ------------- |
| Register 9008 | Register 9009 | Register 9005 | Register 9007 |
| I-max         | I-min         | P-max         | R-max         |
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 121
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
8.3.6 Kommunikationsfehlercodes
Die über CAN zurückgegebenen Fehlercode sind größtenteils an die ModBus-Kommunikation angelehnt. Das
CAN-Modul kann zudem eigene Fehlercodes erzeugen, weil es als Gateway eine eigene Firmware hat. Für das
Format einer Fehlermeldung siehe auch „8.3.4. Normales Lesen“.
Code Beschreibung
Ungültige Registeradresse. Bedeutet, daß das adressierte Register für das angesprochene Gerät nicht
0x02
definiert ist. Siehe Registerliste der jeweiligen Serie.
Falsche Länge der Nachricht bzw. der Nutzdaten. Je nach adressiertem Register werden zwei oder mehr
0x03 Nutzdaten-Bytes in der Nachricht erwartet, wodurch eine Mindestlänge entsteht. Dieser Fehler entsteht
z. B. wenn der DLC der CAN-Nachricht nur 5 ist, wenn er 6 oder mehr sein müßte.
Ausführungsfehler. Allgemeiner Fehler der entsteht, wenn ein korrekter Befehl nicht ausgeführt werden
0x04 kann, weil ein Konflikt mit dem Zustand des Gerätes besteht. Beispiel: man versucht den Modus des
Funktionsgenerator (wo vorhanden) zu ändern, während dieser momentan aktiv ist.
Zugriff verweigert. Es wurde versucht, auf ein Register zu schreiben, das als "nur lesen" definiert oder
0x07
umgekehrt.
Gerät ist in Lokal-Modus. Kann nur auftreten, wenn versucht wurde, mit einem korrekten Befehl das
0x17 Gerät in den Fernsteuerungsmodus zu versetzen, während die Fernsteuerungssperre "Lokal" am Gerät
aktiv war. Die Situation ist eigentlich eine wie bei Fehler 0x04, hier nur spezifischer zurückgemeldet.
Überlast. Kann auftreten, wenn zu viele Nachrichten beim Modul eintreffen und dessen Messageboxen
vollaufen. Überlast kann vermieden werden, indem entweder der Traffic auf dem CAN-Bus verringert
0x20
oder größere zeitliche Abstände zwischen zwei aufeinanderfolgenden Nachrichten an dieselbe CAN ID
gesetzt werden
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 122
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
| 8.3.7    | Beispiele                |     |
| -------- | ------------------------ | --- |
| 8.3.7.1  | Fernsteuerung übernehmen |     |
Wie in „4.8.7.5. Fernsteuerung aktivieren oder beenden“ beschrieben, muß nach dem Einschalten des Gerätes
und bevor man es fernsteuern kann, zuerst die Fernsteuerung übernommen werden. Dazu muß man zunächst
das	passende	Register	in	der	Registerliste	finden.	In	dem	Fall	ist	es	Register	402	(hex:	0x192).	Der	zu	sendende
Datenwert	ist	in	der	Registerliste	definiert.	Laut	Register	402	ist	der	Wert	0xFF00	zu	senden,	um	die	Fernsteuerung
zu übernehmen und 0x0000, um sie wieder zu beenden. Angenommen, das Gerät wäre auf Basis-ID 0x20 eingestellt,
würde man nach der Beschreibung in 8.3.1 die Daten
| 0x01 0x92 | 0x01 0xFF | 0x00 |
| --------- | --------- | ---- |
|        |          |    |
Anz.
| Register / | Reg. Bit (Coil) |     |
| ---------- | --------------- | --- |
Objekt
für TRUE
an die ID 0x20 schicken müssen. Das Gerät sollte daraufhin, sofern nicht irgendwie verhindert, in Fernsteuerung
umschalten. Dieser Status ist auf der Anzeige des Gerätes zusehen oder auch per Register 505 auslesbar.
| 8.3.7.2  | Einen Sollwert setzen und gegenlesen |     |
| -------- | ------------------------------------ | --- |
Nachdem	die	Fernsteuerung	übernommen	wurde,	können	Sie	Sollwerte	an	das	Gerät	schicken.	Diese	repräsentieren
einen	Prozentanteil	vom	Nennwert.	Laut	Definition	der	Register	sind	0xCCCC	=	100%	und	0x0000	=	0%.	Es	sind
also	52429	Werte	zwischen	0	und	100%	verfügbar.	An	diesem	Punkt	sei	darauf	hingewiesen,	daß	das	nicht	der
tatsächlichen	Auflösung	des	Gerätes	entspricht,	die	ein	Wert	am	DC-Eingang	/	DC-Ausgang	hat.	Die	tatsächliche
Auflösung	liegt	bei	etwa	26214	Werten.	Ein	Berechnungsbeispiel	für	Sollwerte	finden	Sie	in	„4.8.7.1. Einen Sollwert
setzen“.
Nachrichten-Beispiel: Ein Netzgerät PSI 9080-170 3U hat 170 A Nennstrom. Wollte man diesen auf 35 A setzen,
ergäbe sich laut der Berechnungsformel in 4.4	ein	Prozent-Sollwert	von	52428	/	170	A	*	35	A=	10794	=	0x2A2A.
Der Strom wird mit Register 501 gesetzt. Angenommen, das Gerät wäre auf Basis-ID 0x88 eingestellt, würde man
nach der Beschreibung in 8.3.1 die Daten
| 0x01 0xF5 | 0x01 0x2A | 0x2A |
| --------- | --------- | ---- |
|        |          |    |
Anz.
| Register / | Reg. Sollwert |       |
| ---------- | ------------- | ----- |
| Objekt     |               | Strom |
an	diese	ID	schicken	müssen.	Sofern	das	Gerät	den	Sollwert	annimmt,	setzt	es	diesen	und	man	könnte	ihn	von
der Anzeige ablesen bzw. über dasselbe Objekt zurücklesen. Die Anfrage
0x01 0xF5
  
Register /
Objekt
ginge raus an die ID 0x89 und das Gerät sollte kurze Zeit später auf der ID 0x8A mit folgenden Daten antworten:
| 0x01 0xF5  | 0x2A 0x2A |     |
| ---------- | --------- | --- |
|         |        |     |
| Register / | Sollwert  |     |
| Objekt     | Strom     |     |
Sollte "Sollwert Strom" nicht dem erwarteten Wert entsprechen, kann das z. B. daran liegen, daß die obere Ein-
stellgrenze für den Strom (I-max) auf 30 A gesetzt wurde. Dann würde von dem Gerät eine Fehlernachricht statt
der erwarteten Antwort kommen:
| 0xFF 0xFF | 0x03 |     |
| --------- | ---- | --- |
  
Fehler-
Fehler
code
Der ModBus Fehlercode 0x3 sagt aus „fehlerhafte Daten“, siehe 4.10. Das bedeutet, der Wert war falsch, weil
höher	als	die	Einstellgrenze.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 123
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
9. EtherCAT
9.1 Einleitung
Bestimmte Geräteserien (siehe „2.2. Anybus-Unterstützung“) unterstützen die Anybus-Schnittstellenmodule, dar-
unter 9000er Modelle mit älterenFirmwarestände ab August 2016 per Firmware-Update auch das EtherCAT-Modul
IF-AB-ECT. EtherCAT-Kommunikation basiert hier per Definition auf CANopen-Objekten, die über eine Netzwerk-
verbindung übertragen werden. Daher wird das „CANopen over Ethernet“ (CoE) genannt. Alle zu EtherCAT und
CANopen benötigte Dokumentation und Software wird vom Hersteller Fa. Beckhoff bzw. der CiA-Organisation zur
Verfügung gestellt.
9.2 Einschränkungen
• Der Scan nach Geräten kann ein bidirektionales Gerät nicht als solches aus dem ESI erkennen, außer das ESI
würde vorher modifiziert (siehe unten)
• Keine Hotplug-Unterstützung; das Gerät muß nach dem Start separat auf Run-Modus "OP" gestellt werden
• Keine Unterstützung für Portmapping in den PDOs
9.3 Einbindung des Gerätes in TwinCAT
Mit allen Geräteserien die EtherCAT unterstützen wird auf USB-Stick eine ESI-Datei mitgeliefert. Sie definiert
einen einfachen Slave und ist global für alle Serien. Alternativ ist die Datei auf Anfrage erhältlich. Die Datei wird
im Installationspfad von TwinCAT abgelegt, üblicherweise in c:\TwinCAT\<twincat_version>\Config\Io\EtherCAT\.
Nach Ablage der Datei und einem Neustart der TwinCAT-Umgebung können unsere EtherCAT-Slaves über den
Dialog „Insert EtherCAT Device“ durch Auswahl der Gerätebeschreibung "IF-AB-ECT (for standard)" oder "IF-AB-
ECT (for bidirectional)" eingebunden werden, falls das Gerät ein bidirektionales aus den Serien PSB oder PSBE
ist. Bidirektionale Geräte benötigen mehr Objekte im PDO, daher die beiden Untergruppen.
Hinweis: ein Scan nach Boxen kann nicht automatisch zwischen "standard" und "bidirectional" unterscheiden. Sollten
Sie ein bidirektionales Modell aus den Serien PSB oder PSBE haben, muß dieses manuell eingebunden werden.
9.4 Datenobjekte
Das im Gerät intern verwendete ModBus-Protokoll wird für die EtherCAT-Datenübertragung in beide Richtungen
in CANopen-Nachrichten umgesetzt. Als Referenz für alle zyklischen Objekte im PDO und die azyklischen Ob-
jekte (SDOs) dienen jene ModBus-Registerlisten, die auch auf dem mitgelieferten USB-Stick zu finden sind und
zusammen mit dieser Anleitung die Programmierdokumentation darstellen. Die azyklischen Datenobjekte werden
von TwinCAT automatisch aus dem Gerät geladen (Objektnamen nur auf Englisch verfügbar), sobald es online ist
bzw. sobald der Tab „CoE“ in TwinCAT ausgewählt wird. Offline-Objekte in Form eines CANopen EDS sind nicht
verfügbar. Danach können die Indexe verwendet werden, um direkt oder programmatisch das Gerät zu steuern.
Es besteht eine direkte Verbindung zwischen den Nummern der ModBus-Register und den bei CANopen verwen-
deten Indexen. Daher können Indexe in ModBus-Register bzw. umgekehrt umgerechnet werden, um die Referenz
zu finden.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 124
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
•
Umrechnung ModBus-Register ► CANopen-Index
ModBus-Registernummer in dezimal + 8193 ► Umwandeln in Hexadezimal = Index
Beispiel:	Sie	möchten	das	Gerät	in	Fernsteuerungsmodus	versetzen	und	suchen	den	Index	dazu.	Laut	Registerliste
läßt sich dazu Register 402 verwenden. Berechnung: 402 + 8193 = 8595 --> in Hex dann 0x2193, also Index 2193.
•	 Umrechnung CANopen-Index ► ModBus-Register
CANopen-Index in hexadezimal - 0x2001 ► Umwandeln in Dezimal = Register
Beispiel:	Sie	benötigen	die	Bitaufteilung	des	PDOs-Objekts	„Status“.	Suchen	Sie	dazu	den	Index	aus	der	Objekt-
liste heraus, hier 21FA. Berechnung des ModBus-Registers: 0x21FA - 0x2001 = 0x1F9 --> in Dezimal dann 505.
In	der	Registerliste	bei	Register	505	finden	Sie	die	Aufteilung	dieses	32-Bit-Wertes.
9.4.1  Unterobjekte im RxPDO
Das	ESI	definiert	für	alle	unsere	EtherCAT-Slaves	die	gleichen	Unterobjekte	im	RxPDO:
| Name            | EtherCAT- | Länge ModBus-     | Kurzbeschreibung                |
| --------------- | --------- | ----------------- | ------------------------------- |
|                 | Datentyp  | in Bytes Register |                                 |
| Status          | UDINT     | 4 505             | Gerätestatus                    |
| Voltage Monitor | UINT      | 2 507             | Istwert Spannung (Prozentwert)  |
| Current Monitor | UINT      | 2 508             | Istwert Strom (Prozentwert)     |
| Control         | UDINT     | 4 -               | Nicht dokumentiert              |
| Voltage select  | UINT      | 2 500             | Sollwert Spannung (Prozentwert) |
| Current select  | UINT      | 2 501             | Sollwert Strom (Prozentwert)    |
| Power select    | UINT      | 2 502             | Sollwert Leistung (Prozentwert) |
Resistance select (1
|     | UINT | 2 503 | Sollwert Widerstand (Prozentwert) |
| --- | ---- | ----- | --------------------------------- |
Bidirektionale	Geräte	aus	den	Serien	PSB	und	PSBE	haben	mehr	Sollwerte,	daher	sollte	die	Boxdefinition	"IF-AB-
ECT	(for	bidirectional)"	für	diese	Serien	verwendet	werden,	um	Zugriff	auf	diese	zusätzlichen	Objekte	zu	erhalten:
| Name | EtherCAT- | Länge ModBus-     | Kurzbeschreibung |
| ---- | --------- | ----------------- | ---------------- |
|      | Datentyp  | in Bytes Register |                  |
Current select (EL) UINT 2 499 Sollwert Strom (Prozentwert) für Senke-Betrieb
Power select (EL) UINT 2 498 Sollwert Leistung (Prozentwert) für Senke-Betrieb
Resistance select (EL) (1  UINT 2 504 Sollwert Widerstand (Prozentwert) für Senke-Betrieb
9.4.2  Unterobjekte im TxPDO
Objekte in diesem PDO dienen zur Steuerung des Gerätes. Mit Stand sind nur Sollwerte auf diese Weise über-
tragbar,	alles	andere	erfolgt	über	SDO-Zugriff.
| Name           | EtherCAT- | Länge ModBus-     | Kurzbeschreibung                |
| -------------- | --------- | ----------------- | ------------------------------- |
|                | Datentyp  | in Bytes Register |                                 |
| Voltage select | UINT      | 2 500             | Sollwert Spannung (Prozentwert) |
| Current select | UINT      | 2 501             | Sollwert Strom (Prozentwert)    |
| Power select   | UINT      | 2 502             | Sollwert Leistung (Prozentwert) |
Resistance select (1 UINT 2 503 Sollwert Widerstand (Prozentwert)
Bidirektionale	Geräte	aus	den	Serien	PSB	und	PSBE	haben	mehr	Sollwerte,	daher	sollte	die	Boxdefinition	"IF-AB-
ECT	(for	bidirectional)"	für	diese	Serien	verwendet	werden,	um	Zugriff	auf	diese	zusätzlichen	Objekte	zu	erhalten:
| Name | EtherCAT- | Länge ModBus-     | Kurzbeschreibung |
| ---- | --------- | ----------------- | ---------------- |
|      | Datentyp  | in Bytes Register |                  |
Current select (EL) UINT 2 499 Sollwert Strom (Prozentwert) für Senke-Betrieb
Power select (EL) UINT 2 498 Sollwert Leistung (Prozentwert) für Senke-Betrieb
Resistance select (EL) (1 UINT 2 504 Sollwert Widerstand (Prozentwert) für Senke-Betrieb
1	 Dieser	Wert	gehört	zu	einem	Feature	namens	"Widerstandsmodus"	(kurz:UIR),	das	nicht	bei	jeder	Serie	verfügbar	ist
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 125
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
9.4.3 SDOs
Die über EtherCAT unterstützten azyklischen Datenobjekte sind als Indexliste im Gerät gespeichert und können
daraus heruntergeladen werden. Dazu muß das Gerät online sein. Es gibt keine separate Dokumentation für diese
Objekte. Wie bei CANopen (siehe „7. CANopen“) sind die diversen Registerlisten für die einzelnen Geräteserien die
Referenz zur Erläuterung der Funktion und des Inhalt eines Datenobjekts, sowie die auf ModBus und zugehörige
Beispiele bezogenen Abschnitte in diesem Dokument.
9.5 Steuerung
Grundsätzlich gilt: die Objekte im TxPDO steuern nur die Sollwerte U, I, P und R zyklisch. Alle anderen Zustände
und Funktionen des Gerätes sind nur über azyklischen Zugriff über SDOs, in dem Fall CANopen-Indexe zu steuern.
Das betrifft auch grundlegende Funktionen wie "Fernsteuerung ein/aus" und "DC ein/aus". Diese Objekte können
auch nicht in das TxPDO gemappt werden, weil die Geräte Portmapping nicht unterstützen.
Informationen über den Objektzugriff über SDOs bei CANopen/EtherCAT sind in der Dokumentation der jeweiligen
Software zu finden.
9.5.1 Verwendung der CANopen-Datenobjekte
Siehe „7.3. Anwendung der Benutzerobjekte (Indexe)“.
Die grundlegende Vorgehensweise zur Steuerung und Überwachung der Geräte unterscheidet sich bei EtherCAT
nicht von anderen Schnittstellen. Daher gelten bei Verwendung des Gerätes als EtherCAT-Slave die in den Ab-
schnitten „3.2. Bedienorte“, „3.5. Besonderheiten der Fernsteuerung“, „4.3. Format der Sollwerte und Auflösung“,
„4.4. Umrechnung der Soll- und Istwerte“ und „4.7. Über die Register-Listen“ aufgeführten Informationen ebenso.
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 126
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

ModBus & SCPI
A. Anhang
A1. Geräteklassen
Zwecks Unterscheidung von Serien untereinander und auch Varianten innerhalb einer Serie gibt es die Geräteklasse
als Nummer. Sie kann aus dem Gerät ausgelesen werden (Register 0 oder SYSTEM:DEVICE:CLASS?) und u. A.
zur Erkennung von bestimmten Geräten unter mehreren dienen, die z. B. bei einer Netzwerksuche auffindbar wären.
Klasse Zugehörige Serie(n) Klasse Zugehörige Serie(n)
16 PS 2000 B TFT Single 62 PSB 9000 Slave (nur Front-USB)
20 ELR 9000 63 PSB 9000 3U 3W
21 PSI 9000 2U/3U (Modelle ab 2014) 64 PSBE 9000
23 PS 5000 65 ELR 9000 HP Slave
24 PS 2000 B TFT Triple 66 PSB 10000
28 PS 9000 2U/3U (Modelle ab 2014) 67 ELR 10000
29 PSI 5000 68 PSI 10000
30 PS 9000 1U 69 PSBE 10000
32 ELR 9000 TFT 3W 70 PSB 10000 Slave (nur Front-USB)
33 PSI 9000 2U/3U TFT 81 ELR 10000 (ab 01/2022)
34 ELR 9000 TFT 3W 82 PSI 10000 (ab 01/2022)
35 PSI 9000 2U/3U TFT 3W 83 PSB 10000 (ab 01/2022)
38 PS 9000 2U/3U 3W 84 PSBE 10000 (ab 01/2022)
39 EL 9000 B 85 PS 10000
41 ELR 5000 86 PU 10000
42 PSI 9000 DT 87 PUB 10000
43 PSE 9000 3U 88 PUL 10000
44 EL 9000 DT
45 PSI 9000 Slave
46 EL 9000 B Slave
47 / 50 PSI 9000 T
48 / 51 EL 9000 T
49 / 56 PS 9000 T
52 USB-B-Port am reduzierten HMI von PSI
9000 3U/WR, EL 9000 B 2Q, ELR 9000 B
Slave und EL 9000 B Slave
53 EL 9000 B 2Q
54 EL 9000 B 3W
55 EL 3000 B
57 PS 3000 C
58 PS 9000
59 ELR 9000 HP
60 ELR 9000 HP 3W
61 PSB 9000 Slave
Erläuterungen:
TFT = Modell/Serie mit TFT-Touchpanel (ältere Serien hatten LCD-Touchpanel)
3W = Modell/Serie mit Option 3W installiert
1U / 2U usw. = Bauform ist 19“ und Gehäusehöhe in x Höheneinheiten
T = Bauform: Tower
DT = Bauform: Desktop
R = Bauform: Wandgehäuse
2Q = Slave-Einheit für Zwei-Quadranten-Betrieb
EA Elektro-Automatik GmbH Telefon: 02162 / 3785-0 www.elektroautomatik.de
Seite 127
Helmholtzstr. 31-37 • 41747 Viersen Telefax: 02162 / 16230 ea1974@elektroautomatik.de

EA Elektro-Automatik GmbH & Co. KG
Entwicklung - Produktion - Vertrieb
Helmholtzstraße 31-37
41747 Viersen
Telefon: 02162 / 37 85-0
Telefax: 02162 / 16 230
E-Mail: ea1974@elektroautomatik.de
Internet: www.elektroautomatik.de