# Diskussion zu App-Prototyp

## Ziele

- Erproben aller (!) Technologien
- Erkennen möglicher Problemzonen
- Ausmerzen möglicher Risiken
- Grundlage für (grobe) Aufwandsschätzung


## Bestandteile

- Quasar Frontend für Trainee
- Quasar Frontend für Coach
- Datenbank
- Anbindung Rezept/Nährstoff API Spoonacular
- Flask Backend
- Integration Backend/Frontend/DB
- Automatisierte Tests Backend
- Automatisierte Tests Frontend
- Automatisiertes Deployment (für alle Komponenten)

### Prio 2
- Secret-Handling (für Vercel/DB/Spoonacular) über Environment-Variablen
- "Dockerisierung"
- (Datenbank-Schema-Migration/Evolution )


## Dokumentation

"minimale" Doku, insbesondere derjenigen Dinge, die gut/schlecht waren
(evtl. in Form von ADRs)


## Time-Tracking

- ALLE Arbeiten aufschreiben
- trenne (evtl. erst später) _setup_ und _entwicklung_


## Funktion, die im Prototyp umgesetzt werden soll

***Automatisches Erstellen einer Mahlzeit für angegebene Nährwerte.***

- Coach: 
  - Gibt Nährwerte ein
  - erhält Vorschlag für Mahlzeit
  - Kann neu generieren (lassen) oder akzeptieren

- Trainee:
  - Sieht Mahlzeit
 
- Benötigt:
  - Quasar für Coach & Trainee Frontend
  - Spoonacular, um automatischen Mahlzeit-Vorschlag zu erhalten
  - Flask, um Spoonacular Request zu senden und zu verarbeiten (und für schreiben/lesen aus der DB?)
  - Datenbank, um Mahlzeit zwischen Coach und Trainee auszutauschen
  - Automatische Tests
  - Automatisches Deployment
 
- Einschränkungen / Einfachheiten:
  - Keine Benuzer anlegbar, sondern erstmal nur ein Standard-Coach und ein Standard-User, ohne Login und Account

### Mockup
Ich hab mal ein grobes Mockup dazu erstellt. Erstmal nur für mobile view, das ganze responsiv gestalten kann ich mit Quasar dann relativ easy, dafür wollte ich für den Prototypen jetzt kein weiteres Mockup erstellen.

[**Mockup bei Canva**](https://www.canva.com/design/DAF8z56g02o/fc0dFiLb2XgaiEcKLf_dPA/edit)

#### Bilder

**Coach-View**  
![mockup-coach-view](https://github.com/perstarke-webdev/starke-nutrition-app-prototype/assets/7078370/dd6dbbee-ea9e-4260-b1b5-f95a710f8942)

**Trainee-View**   
![mockup-trainee-view](https://github.com/perstarke-webdev/starke-nutrition-app-prototype/assets/7078370/5aca44da-428c-4bfd-8acf-80de58277618)





