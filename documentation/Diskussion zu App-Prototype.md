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

**Automatisches Erstellen einer Mahlzeit für angegebene Nährwerte.**

- Coach: 
  - Gibt Nährwerte ein
  - erhält Vorschlag für Mahlzeit
  - Kann neu generieren oder aktzeptieren

- Trainee:
  - Sieht Mahlzeit
 
- Benötigt:
  - Quasar für Coach & Trainee Frontend
  - Spoonacular, um automatischen Mahlzeit-Vorschlag zu erhalten
  - Flask, um Spoonacular Request zu senden und zu verarbeiten (und für schreiben/lesen aus der DB?)
  - Datenbank, um Mahlzeit zwischen Coach und Trainee auszutauschen
  - Automatische Tests
  - Automatisches Deployment
 


    
