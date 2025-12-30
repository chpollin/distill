# Zwölf Stile zur Visualisierung von Wissen

Ein Template-Set für die visuelle Kommunikation epistemischer Strukturen. Dieses Dokument dient als Wissensbasis für Large Language Models und menschliche Anwender gleichermaßen: Es systematisiert, welche Visualisierungsform für welche Art von Wissen geeignet ist, und liefert einsatzbereite Prompts für generative Bildmodelle.

## Einleitung

Dieses Handbuch bietet ein systematisches Vokabular für die Übersetzung abstrakter Wissensstrukturen in visuelle Darstellungen. Es richtet sich an Forschende, Lehrende und Kommunikatoren, die mit Text-zu-Bild-Modellen arbeiten und dabei über rein dekorative Illustration hinausgehen wollen.

Die zentrale Frage lautet nicht „Wie soll es aussehen?", sondern „Was soll gezeigt werden?". Die zwölf Stile bilden ein geschlossenes Repertoire, das Entscheidungen strukturiert und nachvollziehbar macht.

### Frontier-Bildmodelle als Reasoning-Werkzeuge

Die aktuellen Frontier-Modelle für Bildgenerierung – etwa OpenAI Image Gen (GPT-4o, DALL-E 3) und Gemini Imagen – sind weit mehr als ästhetische Illustratoren. Sie verfügen über ausgeprägte Reasoning-Fähigkeiten, die es ermöglichen, komplexe konzeptuelle Strukturen in visuelle Form zu übersetzen. Diese Modelle verstehen Prompts nicht nur als Bildbeschreibungen, sondern als semantische Anweisungen, die räumliche Relationen, kategoriale Unterscheidungen und epistemische Strukturen codieren.

Das eröffnet einen neuen Möglichkeitsraum: Kontextinformationen aus Texten und Forschungskontexten können systematisch visualisiert werden. Die Modelle explorieren dabei eigenständig Varianten innerhalb des spezifizierten Stilrahmens. Statt einer einzigen „richtigen" Darstellung entstehen Visualisierungsfamilien, die verschiedene Aspekte eines Konzepts betonen können.

Dieses Handbuch nutzt diese Fähigkeiten, indem es die Reasoning-Kompetenz der Modelle mit strukturierten Prompt-Templates verbindet. Die zwölf Stile sind so konzipiert, dass sie den Modellen klare semantische Rahmenbedingungen vorgeben, innerhalb derer sie ihre visuelle Interpretation entwickeln können. Das Ergebnis ist eine produktive Zusammenarbeit zwischen menschlicher Konzeption und maschineller Visualisierung.

## Theoretische Grundlagen

### Grafische Semiotik

Die grafische Semiotik nach Jacques Bertin (*Sémiologie graphique*, 1967) systematisiert die Codierung von Information durch visuelle Mittel. Die zwei Dimensionen der Bildebene bilden das primäre Ordnungssystem. Sechs retinale Variablen ergänzen dieses System, nämlich Form, Orientierung, Farbe, Textur, Tonwert und Größe. Jede Variable eignet sich für bestimmte Datentypen. Position codiert quantitative Relationen, Farbe kategoriale Unterscheidungen, Größe Mengenvergleiche. Die Stile in diesem Handbuch nutzen diese Systematik, um epistemische Strukturen visuell zu codieren.

### Gestalt-Prinzipien

Die Gestalt-Prinzipien beschreiben, wie das menschliche Wahrnehmungssystem visuelle Elemente zu Einheiten organisiert. Das übergeordnete Prägnanzgesetz besagt, dass Wahrnehmung zur einfachsten und stabilsten Struktur tendiert. Die einzelnen Prinzipien spezifizieren die Bedingungen dieser Organisation. Nähe bewirkt Gruppierung räumlich benachbarter Elemente. Ähnlichkeit bewirkt Gruppierung visuell gleichartiger Elemente. Geschlossenheit ergänzt unvollständige Formen. Kontinuität verbindet Elemente entlang von Linien oder Kurven. Figur-Grund-Trennung scheidet Vordergrund von Hintergrund.

Die Prinzipien Symmetrie und gemeinsames Schicksal sind für statische Visualisierungen weniger relevant. Symmetrie wirkt primär bei der Wahrnehmung von Einzelformen. Gemeinsames Schicksal setzt Bewegung voraus und greift daher bei unbewegten Bildern nicht.

### Kognitive Verarbeitung

Die *Cognitive Load Theory* (Sweller, 1988) erklärt, wie Lernende Information verarbeiten und wann Überlastung eintritt. Das Arbeitsgedächtnis hat eine begrenzte Kapazität. Die Theorie unterscheidet drei Arten kognitiver Last. Intrinsische Last entsteht durch die Komplexität des Inhalts selbst. Extrinsische Last wird durch ungünstige Darstellung verursacht. Lernförderliche Last dient dem Aufbau von Wissensstrukturen. Effektive Visualisierungen minimieren extrinsische Last durch klare Gestaltung und ermöglichen so die Verarbeitung komplexer Inhalte.

Die *Dual Coding Theory* (Paivio, 1971) ergänzt diesen Ansatz. Das menschliche kognitive System verarbeitet Information über zwei unterschiedliche Kanäle, einen verbalen und einen nonverbalen. Die Kombination von Bild und Text verbessert Verstehen und Behalten, weil Information in beiden Systemen gespeichert wird.

### Designprinzipien

Edward Tuftes Arbeiten zur Datenvisualisierung (*The Visual Display of Quantitative Information*, 1983) formulieren Gütekriterien für informationsreiche Darstellungen. Das *data-ink ratio* bezeichnet den Anteil der Tinte, die tatsächlich Daten repräsentiert, im Verhältnis zur gesamten verwendeten Tinte. Gute Visualisierungen maximieren diesen Anteil. *Chartjunk* bezeichnet unnötige oder ablenkende Elemente in einer Datenvisualisierung, die nicht zum Verständnis der dargestellten Information beitragen. Tufte plädiert für Einfachheit und Direktheit und warnt vor Verzerrungen, die durch inkonsistente Skalen oder irreführende Achsen entstehen.

### Wissensvisualisierung

Die Theorie der *Knowledge Visualization* (Burkhard, Eppler, 2004) unterscheidet zwischen Informationsvisualisierung und Wissensvisualisierung. Informationsvisualisierung macht Daten sichtbar. Wissensvisualisierung zielt auf den Transfer von Einsichten, Erfahrungen, Einstellungen, Werten, Erwartungen, Perspektiven, Meinungen und Prognosen zwischen Personen. Diese Unterscheidung ist relevant, weil die Stile dieses Handbuchs nicht nur Daten abbilden, sondern epistemische Strukturen vermitteln sollen.

### Visuelle Rhetorik

Visuelle Rhetorik untersucht, wie Visualisierungen argumentieren und überzeugen. Sie analysiert die persuasiven Effekte visueller Gestaltung und die Bedeutungsproduktion durch Bilder, Typografie und Komposition (vgl. Kostelnick & Hassett, 2003). Visualisierungen sind nicht neutral, sondern rahmen Information durch Auswahl, Anordnung und Gestaltung. Designentscheidungen repräsentieren Hinzufügungen oder Auslassungen von Information auf verschiedenen Ebenen, nämlich bei den Daten, der visuellen Repräsentation, textuellen Annotationen und der Interaktivität. Diese Perspektive sensibilisiert für die rhetorische Dimension der Stilentscheidungen.

### Visuelle Genres und Traditionen

Die Stile greifen auf etablierte Bildtraditionen der Wissenschaftskommunikation zurück. Die ISOTYPE-Methode (Otto Neurath, Gerd Arntz, Marie Reidemeister) liefert das Vorbild für piktografische Quantifizierung. Die botanische und naturhistorische Illustration informiert Konventionen der Detailgenauigkeit und taxonomischen Darstellung. Kartografische Darstellungen strukturieren territoriale und relationale Logiken. Stratigrafische Schnitte aus Geologie und Archäologie prägen Schichtungsdarstellungen. Die Datenjournalismus-Tradition, etwa bei David McCandless, liefert Strategien für das Fassbar-Machen großer Zahlen und komplexer Zusammenhänge. Die Zuordnung der einzelnen Stile zu diesen Traditionen erfolgt in den jeweiligen Stilbeschreibungen.

### Aufgabentaxonomien

Die Strukturtypen orientieren sich an etablierten Kategorien der Informationsvisualisierung, wie sie Brehmer und Munzner in ihrer *Multi-Level Typology of Abstract Visualization Tasks* (2013) systematisiert haben. Diese Taxonomie unterscheidet zwischen dem Warum (dem Zweck einer Visualisierung), dem Wie (den Interaktions- und Darstellungsmethoden) und dem Was (den Datentypen). Die zwölf Stile dieses Handbuchs adressieren primär das Warum, indem sie typische epistemische Operationen mit visuellen Formen verbinden.

## Übersicht der Stile

|Nr.|Stil|Zeigt|Strukturtyp|Theoretischer Bezug|
|---|---|---|---|---|
|1|Lineare Phasenfolge|Phasen, Schritte, Abfolgen|Lineare Sequenz|Bertin (geordnete Komponenten)|
|2|Piktografischer Mengenvergleich|Mengenverhältnisse, Proportionen|Quantitativer Vergleich|ISOTYPE-Methode|
|3|Hub-Struktur|Zentrum mit abhängigen Bereichen|Netzwerk (zentralisiert)|Netzwerktheorie|
|4|Schematische Komponenten-Dekomposition|Aufbau, Komponenten, Teile|Hierarchie (Teil-Ganzes)|Flat-Design-Diagrammatik|
|5|Metamorphose|Wandlung, Zustandsänderung|Transformation|Naturhistorische Illustration|
|6|Gestalt-Gruppierung|Zugehörigkeit, Cluster, Ähnlichkeit|Kategorisierung|Gestalt-Psychologie|
|7|Anti-Sublim|Große Mengen, Masse fassbar gemacht|Skalierung|Datenjournalismus, visuelle Rhetorik|
|8|Rhetorischer Kontrast|Kern vs. Peripherie, Wichtigkeit|Fokussierung|Gestalt (Figur-Grund), visuelle Rhetorik|
|9|Stratigraphische Zeitschichtung|Geschichte als Ablagerung, Epochen|Temporale Tiefe|Geologische und archäologische Illustration|
|10|Zyklus-Spirale|Rückkopplung, Iteration, Wiederholung|Zyklus|Diagrammatik|
|11|Netzwerk-Konstellation|Verbindungen ohne Zentrum|Netzwerk (dezentral)|Netzwerktheorie, Graphenvisualisierung|
|12|Epistemische Unschärfe|Hypothesen, Unsicherheit, Ambiguität|Unsicherheit|Visuelle Rhetorik|

## Die Stile im Detail

### Stil 1: Lineare Phasenfolge

**Strukturtyp:** Lineare Sequenz

**Zeigt:** Phasen, Schritte, Abfolgen mit gleichwertigen Elementen

**Theoretischer Bezug:** Bertins Konzept der geordneten Komponenten. Die horizontale Achse codiert Zeit oder Reihenfolge durch Position. Die formale Identität der Container signalisiert strukturelle Gleichwertigkeit der Schritte.

**Geeignet für:** Prozesse mit aufeinanderfolgenden, gleichwertigen Schritten. Workflows, Anleitungen, Phasenmodelle, Verfahrensabläufe.

**Nicht geeignet für:** Iterative Prozesse, Rückkopplungen, parallele Abläufe, qualitative Transformation, Prozesse mit Steigerungslogik.

**Abgrenzung zu Stil 5:** Stil 1 zeigt *gleichwertige* Schritte (A, dann B, dann C). Stil 5 zeigt *qualitative Veränderung* (A wird zu B, wobei B wesensmäßig anders ist als A). Entscheidungskriterium: Wenn das Ergebnis einer Phase sich strukturell vom Input unterscheidet, ist Stil 5 angemessen. Wenn jede Phase eine abgeschlossene Handlung darstellt, die zur nächsten führt, ist Stil 1 richtig.

**Abgrenzung zu Stil 10:** Stil 1 zeigt *einmalige* Durchläufe. Stil 10 zeigt *wiederkehrende* Phasen, bei denen der Prozess nach Abschluss erneut beginnt und auf dem Vorherigen aufbaut.

#### Prinzip

Die lineare Phasenfolge codiert Abfolge durch horizontale Position. Alle Elemente sind formal gleichwertig, das heißt sie haben identische Form und Größe. Die Progression wird ausschließlich durch Farbverlauf innerhalb einer Farbfamilie angezeigt, nicht durch Formveränderung. Dies unterscheidet den Stil fundamental von Stil 5, wo die Formen selbst sich wandeln.

Das visuelle Schema folgt diesen Regeln:

- **Container:** Identische geometrische Formen (Rechtecke, Kreise, Hexagone) in horizontaler Anordnung
- **Konnektoren:** Schlichte graue Pfeile zwischen den Elementen
- **Farblogik:** Alle Formen verwenden denselben Farbton, unterschieden nur durch Sättigung. Links am hellsten, rechts am dunkelsten.
- **Icons:** Weiße Umriss-Symbole innerhalb der Container, austauschbare Platzhalter für phasenspezifische Inhalte

Die Farbprogression signalisiert Fortschritt ohne qualitative Wertung. Dunklere Sättigung bedeutet nicht "besser" oder "wichtiger", sondern lediglich "später in der Sequenz".

#### Template-Prompt

```
A minimalist horizontal process diagram on pure white background. Exactly [ANZAHL] [FORM] of identical size arranged in a perfectly centered horizontal row with equal spacing. Connected by thin gray arrows between each shape. Color scheme: [FARBFAMILIE] – all shapes use the same hue, differing only in saturation, with the leftmost shape palest and the rightmost shape most saturated. Each shape contains one white outline icon, from left to right: [ICON-LISTE]. Style: flat design, solid colors only, absolutely no gradients, no shadows, no 3D effects, no glow. The shapes should fill approximately 60% of the image width. No text, no labels, no numbers. 16:9 aspect ratio.
```

Die Variablen sind:

- ANZAHL: Typischerweise 3 bis 6 Phasen
- FORM: rounded rectangles, circles, hexagons, squares
- FARBFAMILIE: Eine Farbbezeichnung mit dem Zusatz "family", etwa teal blue family, terracotta family, sage green family
- ICON-LISTE: Domänenspezifische Symbole, durch Kommas getrennt

#### Beispiel 1: Forschungsprozess (4 Phasen)

Geeignet für wissenschaftliche Arbeitsabläufe, Methodendarstellungen, Projektphasen in Forschungskontexten.

```
A minimalist horizontal process diagram on pure white background. Exactly 4 rounded rectangles of identical size arranged in a perfectly centered horizontal row with equal spacing. Connected by thin gray arrows between each shape. Color scheme: teal blue family – all shapes use the same hue, differing only in saturation, with the leftmost shape very pale teal and the rightmost shape deep saturated teal. Each shape contains one white outline icon, from left to right: open book, magnifying glass with graph, two interlocking gears, document with checkmark. Style: flat design, solid colors only, absolutely no gradients, no shadows, no 3D effects, no glow. The shapes should fill approximately 60% of the image width. No text, no labels, no numbers. 16:9 aspect ratio.
```

Die vier Phasen repräsentieren einen generalisierten Forschungsablauf: Literaturarbeit, Analyse, Verarbeitung, Dokumentation. Die Icons sind abstrakt genug, um auf verschiedene Disziplinen übertragbar zu sein.

<div class="image-grid">
<div>
<img src="images/stil-01-phasenfolge/stil-01-forschung-openai.png" alt="Forschungsprozess – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-01-phasenfolge/stil-01-forschung-gemini.png" alt="Forschungsprozess – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 2: Entscheidungsprozess (3 Phasen)

Geeignet für Governance-Abläufe, Genehmigungsverfahren, dreistufige Workflows in administrativen Kontexten.

```
A minimalist horizontal process diagram on pure white background. Exactly 3 circles of identical size arranged in a perfectly centered horizontal row with equal spacing. Connected by thin gray arrows between each shape. Color scheme: terracotta family – all shapes use the same warm reddish-brown hue, differing only in saturation, with the leftmost circle pale terracotta and the rightmost circle deep saturated terracotta. Each circle contains one white outline icon, from left to right: inbox tray with downward arrow, balance scale, hand giving thumbs up. Style: flat design, solid colors only, absolutely no gradients, no shadows, no 3D effects, no glow. The shapes should fill approximately 60% of the image width. No text, no labels, no numbers. 16:9 aspect ratio.
```

Die drei Phasen repräsentieren einen Entscheidungsablauf: Eingang, Abwägung, Freigabe. Die reduzierte Phasenzahl eignet sich für Prozesse mit klarer Dreiteilung.

<div class="image-grid">
<div>
<img src="images/stil-01-phasenfolge/stil-01-entscheidung-openai.png" alt="Entscheidungsprozess – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-01-phasenfolge/stil-01-entscheidung-gemini.png" alt="Entscheidungsprozess – Gemini">
<em>Gemini</em>
</div>
</div>

#### Anpassungshinweise

**Phasenanzahl:** Drei Phasen für einfache Abläufe, vier für Standardprozesse, fünf oder sechs für differenziertere Darstellungen. Mehr als sechs Phasen überfordern die horizontale Lesbarkeit.

**Formwahl:** Rechtecke wirken technischer und eignen sich für Arbeitsabläufe. Kreise wirken weicher und eignen sich für kommunikative oder soziale Prozesse. Hexagone können Vernetzungspotenzial andeuten, sollten aber sparsam verwendet werden.

**Farbfamilien:** Kühle Töne (Teal, Blau, Grün) für analytische oder technische Prozesse. Warme Töne (Terracotta, Orange, Amber) für organisatorische oder menschenbezogene Prozesse. Die Wahl ist konventionell, nicht zwingend.

**Icons:** Die Icons sollten als Umrisszeichnungen (outline) spezifiziert werden, um Konsistenz zu gewährleisten. Gefüllte Icons können die Farbwirkung stören. Domänenspezifische Anpassungen sind möglich, etwa juristische Symbole (Paragraphenzeichen, Hammer, Vertrag) oder medizinische Symbole (Stethoskop, Spritze, Herz).

**Bekannte Probleme:** Generative Modelle tendieren bei Sequenzdiagrammen zu einer "typischen" Anzahl von fünf Phasen. Die explizite Angabe "exactly [N]" wird nicht immer befolgt. Bei Abweichungen hilft Neugenerierung oder die Verstärkung durch "exactly [N], no more, no fewer".

---

### Stil 2: Piktografischer Mengenvergleich

**Strukturtyp:** Quantitativer Vergleich (proportional)

**Zeigt:** Mengenverhältnisse, Proportionen, Verteilungen über Kategorien hinweg

**Theoretischer Bezug:** Das Prinzip der Mengencodierung durch Symbolwiederholung wurde in den 1930er Jahren durch die ISOTYPE-Methode systematisiert. Das Grundprinzip, nämlich identische Symbole zu wiederholen, um Quantitätsverhältnisse intuitiv erfassbar zu machen, ist unabhängig von der historischen Ästhetik anwendbar und nutzt das präattentive Erfassen von Gruppengrößen.

**Geeignet für:** Illustrative Darstellungen von Proportionen in Kommunikationskontexten. Größenordnungsvergleiche, bei denen die ungefähre Relation wichtiger ist als exakte Werte. Lehrmaterialien, Präsentationen, Öffentlichkeitsarbeit.

**Nicht geeignet für:** Datengetreue Visualisierung mit Anspruch auf numerische Präzision. Wissenschaftliche Publikationen, bei denen exakte Werte zählen. Kontexte, in denen Betrachter die Symbole abzählen und als Fakten interpretieren würden.

**Abgrenzung zu Stil 7:** Stil 2 ermöglicht die Wahrnehmung von Proportionen zwischen Kategorien (Reihe A ist etwa doppelt so lang wie Reihe B). Stil 7 vermittelt einen qualitativen Eindruck von Masse ohne kategoriale Differenzierung.

**Abgrenzung zu Stil 6:** Stil 2 vergleicht *Mengen* (wie viel im Verhältnis zu wie viel). Stil 6 zeigt *Gruppenzugehörigkeit* (was gehört zusammen).

#### Prinzip

Der piktografische Mengenvergleich codiert Quantitätsverhältnisse durch die Wiederholung identischer Symbole in horizontalen Reihen. Jede Reihe repräsentiert eine Kategorie. Die relative Länge der Reihen macht Proportionen auf einen Blick erfassbar.

Das visuelle Schema folgt diesen Regeln:

- **Piktogramme:** Einfache geometrische Silhouetten oder Icons. Reduktion auf das Wesentliche, keine naturalistischen Details. Jedes Symbol in einer Reihe muss identisch sein.
- **Anordnung:** Horizontale Reihen, linksbündig ausgerichtet. Die unterschiedliche Reihenlänge codiert die Mengenverhältnisse.
- **Farblogik:** Jede Kategorie erhält eine distinkte Farbe. Die Farben dienen der Unterscheidung, nicht der Wertung.
- **Hintergrund:** Neutral, typischerweise weiß oder hellgrau, optional mit subtiler Rasterstruktur.

#### Epistemische Einschränkung

Generative Bildmodelle haben kein Konzept von Kardinalität. Sie produzieren visuell plausible Muster, aber sie zählen nicht. Die im Prompt spezifizierten Mengen werden als ungefähre Orientierung interpretiert, nicht als exakte Vorgabe. **Die erzeugten Grafiken sind daher für illustrative Zwecke geeignet, nicht für datengetreue Visualisierung.**

Für Anwendungen, bei denen numerische Präzision erforderlich ist, empfiehlt sich einer der folgenden Wege:

- Nachbearbeitung der generierten Grafik in Vektorsoftware, um die Symbolanzahl zu korrigieren
- Verwendung klassischer Diagrammwerkzeuge statt generativer Modelle
- Verzicht auf konkrete Zahlenwerte und Beschränkung auf qualitative Aussagen (deutlich mehr, etwa halb so viel, ein kleiner Anteil)

#### Template-Prompt

```
A clean infographic comparing proportions across [ANZAHL] categories using repeated pictograms. [ANZAHL] horizontal rows of identical symbols, left-aligned, each row representing a different category. [KATEGORIE-BESCHREIBUNG]. The rows have visibly different lengths to show proportional differences: [PROPORTIONSBESCHREIBUNG]. The pictograms are simple, bold silhouettes, flat design, each symbol in a row identical to the others in that row. [HINTERGRUND]. Muted color palette with distinct colors for each category. Style: modern minimalist infographic, flat colors, no gradients, no shadows, no 3D effects. Absolutely no text, no numbers, no legends, no labels. 16:9 aspect ratio.
```

Die Variablen sind:

- ANZAHL: Typischerweise 3 bis 5 Kategorien
- KATEGORIE-BESCHREIBUNG: Benennung der Piktogrammtypen und Farben pro Reihe
- PROPORTIONSBESCHREIBUNG: Qualitative Verhältnisangaben (longest row, medium row, shortest row) statt exakter Zahlen
- HINTERGRUND: Je nach Kontext weiß, hellgrau oder mit subtiler Rasterstruktur

#### Beispiel 1: Ressourcenverteilung (4 Kategorien)

Geeignet für illustrative Darstellungen von Verteilungen über Bereiche hinweg, etwa Arbeitskräfte, Budgets oder Kapazitäten.

```
A clean infographic comparing proportions across 4 categories using repeated human figure pictograms. Four horizontal rows of identical symbols, left-aligned, each row representing a different category. Top row: navy blue figures holding a tool, this is the longest row. Second row: burnt orange figures holding a book, medium-long row. Third row: forest green figures holding a briefcase, short row. Bottom row: warm brown figures holding a plant, shortest row with only a few figures. The pictograms are simple, bold silhouettes, flat design, each symbol in a row identical to the others in that row. Clean white background with subtle light gray grid lines. Muted color palette. Style: modern minimalist infographic, flat colors, no gradients, no shadows, no 3D effects. Absolutely no text, no numbers, no legends, no labels. 16:9 aspect ratio.
```

Die vier Reihen visualisieren eine absteigende Verteilung. Die Attribute (Werkzeug, Buch, Aktentasche, Pflanze) differenzieren die Kategorien semantisch. Die konkreten Zahlenwerte bleiben offen und können bei Bedarf in einer Bildunterschrift ergänzt werden.

<div class="image-grid">
<div>
<img src="images/stil-02-mengenvergleich/stil-02-ressourcen-openai.png" alt="Ressourcenverteilung – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-02-mengenvergleich/stil-02-ressourcen-gemini.png" alt="Ressourcenverteilung – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 2: Drei-Sektoren-Vergleich (3 Kategorien)

Geeignet für einfache Proportionsdarstellungen mit klarer Abstufung.

```
A clean infographic comparing proportions across 3 categories using repeated circular pictograms. Three horizontal rows of identical circles, left-aligned. Top row: slate blue circles, this is the longest row. Middle row: terracotta circles, medium-length row about half as long as the top row. Bottom row: sage green circles, short row about one third the length of the top row. The pictograms are simple flat circles, each symbol in a row identical to the others. Pure white background. Muted color palette. Style: modern minimalist infographic, flat colors, no gradients, no shadows, no 3D effects, strictly frontal view. Absolutely no text, no numbers, no legends, no labels. 16:9 aspect ratio.
```

Dieses Beispiel verwendet abstrakte Formen statt menschlicher Figuren. Es eignet sich für Kontexte, in denen die Kategorien keine Personengruppen darstellen.

<div class="image-grid">
<div>
<img src="images/stil-02-mengenvergleich/stil-02-sektoren-openai.png" alt="Drei-Sektoren-Vergleich – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-02-mengenvergleich/stil-02-sektoren-gemini.png" alt="Drei-Sektoren-Vergleich – Gemini">
<em>Gemini</em>
</div>
</div>

#### Anpassungshinweise

**Piktogrammwahl:** Menschliche Figuren sind am intuitivsten für Darstellungen von Bevölkerungen oder Arbeitskräften. Abstrakte Formen (Kreise, Quadrate) eignen sich für nicht-personenbezogene Daten. Die Symbole sollten einfach genug sein, um bei Wiederholung konsistent zu bleiben.

**Proportionsangaben:** Qualitative Beschreibungen (longest, medium, shortest, about half, about one third) liefern konsistentere Ergebnisse als exakte Zahlen. Die Modelle interpretieren relative Längenangaben zuverlässiger als absolute Mengen.

**Kategorienanzahl:** Drei bis vier Kategorien funktionieren am besten. Bei fünf oder mehr Kategorien tendieren die Modelle zu Eigeninterpretationen und fügen zusätzliche Reihen oder abweichende Symbole hinzu.

**Anordnungsvariante:** Manche Modelle interpretieren den Prompt als Flächenanordnung statt als einzelne Reihen. Die Symbole werden dann in rechteckigen Blöcken gruppiert. Dies kann für bestimmte Darstellungen nützlich sein, weicht aber vom klassischen Reihenvergleich ab.

**Nachbearbeitung:** Für Anwendungen mit Präzisionsanspruch sollte die generierte Grafik als Ausgangspunkt dienen. Die Symbolanzahl kann in Vektorsoftware korrigiert werden, ohne die stilistische Qualität zu beeinträchtigen.

**Kontextempfehlung:** Der Stil eignet sich für Wissenschaftskommunikation, Lehrmaterialien und illustrative Zwecke. Für wissenschaftliche Publikationen mit Datenanspruch sind klassische Diagrammformen (Balkendiagramme, Punktdiagramme) vorzuziehen.

---

### Stil 3: Hub-Struktur

**Strukturtyp:** Netzwerk (zentralisiert)

**Zeigt:** Beziehungen zwischen einem dominanten Zentrum und abhängigen oder assoziierten Bereichen

**Theoretischer Bezug:** In der Netzwerktheorie bezeichnet die Hub-and-Spoke-Topologie Strukturen, bei denen ein zentraler Knoten mit mehreren peripheren Knoten verbunden ist, die untereinander weniger oder keine Verbindungen haben. Die visuelle Codierung nutzt Größe und Position zur Darstellung von Zentralität.

**Geeignet für:** Strukturen mit einem Kernbereich und peripheren Elementen. Disziplinen mit Hilfswissenschaften, Organisationen mit Abteilungen, Theorien mit Anwendungsfeldern, Produkte mit Features.

**Nicht geeignet für:** Symmetrische Netzwerke ohne klares Zentrum, Strukturen mit mehreren gleichwertigen Zentren, rein hierarchische Über-/Unterordnungen.

**Abgrenzung zu Stil 11:** Stil 3 für Strukturen mit *einem* dominanten Zentrum. Stil 11 für Strukturen mit *keinem* oder *mehreren* gleichwertigen Zentren. Entscheidungskriterium: Wenn ein Element deutlich mehr Verbindungen oder Bedeutung hat als alle anderen, ist Stil 3 angemessen.

**Abgrenzung zu Stil 4:** Stil 3 zeigt Beziehungen zwischen eigenständigen Bereichen. Stil 4 zeigt Teil-Ganzes-Beziehungen, bei denen die Teile ohne das Ganze nicht sinnvoll existieren.

#### Prinzip

Die Hub-Struktur codiert Zentralität durch Größe und Position. Das dominante Element steht im Zentrum und ist deutlich größer als die peripheren Elemente. Die Verbindungslinien zum Zentrum sind die primäre Beziehungsebene. Sekundärverbindungen zwischen peripheren Elementen sind optional und sollten sparsam eingesetzt werden, um die Hub-Logik nicht zu verwässern.

Das visuelle Schema folgt diesen Regeln:

- **Zentrum:** Ein dominantes Element, mindestens dreimal so groß wie die peripheren Elemente
- **Peripherie:** Kleinere Elemente, die das Zentrum umgeben, idealerweise in asymmetrischer Anordnung
- **Primärverbindungen:** Durchgezogene Linien vom Zentrum zu jedem peripheren Element
- **Farblogik:** Das Zentrum in einer kontrastierenden Farbe, die Peripherie in einer kohärenten Farbfamilie
- **Sekundärverbindungen:** Optional, gestrichelt und nur zwischen ausgewählten peripheren Elementen

Die asymmetrische Anordnung verhindert einen mechanischen Eindruck und suggeriert organische Beziehungen statt starrer Hierarchie.

#### Template-Prompt

```
A conceptual diagram showing a hub-and-spoke relationship structure. One central [ZENTRALFORM] in [ZENTRALFARBE], clearly dominant, approximately three times larger than the surrounding elements. Exactly [ANZAHL] smaller [PERIPHERFORM] arranged around the center with uneven spacing, not touching each other. Each peripheral element connected to the center by a solid gray line. The peripheral elements all use [PERIPHERFARBEN], creating a cohesive color family that contrasts with the central element. [SEKUNDÄRVERBINDUNGEN]. Clean modern style, flat colors, no gradients, no shadows, no decorative elements. Pure white background. Absolutely no text, no labels. 16:9 aspect ratio.
```

Die Variablen sind:

- ZENTRALFORM: circle, hexagon, rounded square
- ZENTRALFARBE: Eine kühle oder neutrale Farbe (deep teal, muted navy blue, slate gray)
- ANZAHL: Typischerweise 4 bis 6 periphere Elemente
- PERIPHERFORM: circles, hexagons, squares (kann identisch mit oder unterschiedlich von der Zentralform sein)
- PERIPHERFARBEN: Eine kohärente Farbfamilie (muted warm tones, variations of sage green, soft blue-gray tones)
- SEKUNDÄRVERBINDUNGEN: "No connections between the peripheral elements" oder "Only two adjacent peripheral elements connected by a thin dotted gray line"

#### Beispiel 1: Abstrakte Hub-Struktur (5 periphere Elemente)

Geeignet für Darstellungen von Kernbereichen mit assoziierten Feldern, ohne Beziehungen zwischen den peripheren Elementen zu betonen.

```
A conceptual diagram showing a hub-and-spoke relationship structure. One central circle in deep teal, clearly dominant, approximately three times larger than the surrounding elements. Exactly 5 smaller circles arranged around the center with uneven spacing, not touching each other. Each peripheral element connected to the center by a solid gray line. The peripheral elements all use muted warm tones: sand, terracotta, dusty rose, soft ochre, and warm gray, creating a cohesive color family that contrasts with the teal center. No connections between the peripheral elements. Clean modern style, flat colors, no gradients, no shadows, no decorative elements. Pure white background. Absolutely no text, no labels. 16:9 aspect ratio.
```

Der Kontrast zwischen dem kühlen Zentrum und der warmen Peripherie macht die Hierarchie sofort erkennbar. Die Abwesenheit von Sekundärverbindungen betont die zentrale Rolle des Hubs.

<div class="image-grid">
<div>
<img src="images/stil-03-hub/stil-03-abstrakt-openai.png" alt="Abstrakte Hub-Struktur – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-03-hub/stil-03-abstrakt-gemini.png" alt="Abstrakte Hub-Struktur – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 2: Hub-Struktur mit Formdifferenzierung (4 periphere Elemente)

Geeignet für Darstellungen, bei denen die Unterscheidung zwischen Zentrum und Peripherie zusätzlich betont werden soll, oder wenn ausgewählte Querverbindungen relevant sind.

```
A conceptual diagram showing a hub-and-spoke relationship structure. One central large circle in muted navy blue, clearly dominant, approximately three times larger than the surrounding elements. Exactly 4 smaller hexagons arranged around the center at different distances, not forming a perfect circle. Each hexagon connected to the center by a solid thin dark gray line. The hexagons use variations of sage green and gray-green tones, creating a cohesive muted palette. Only two of the hexagons are connected to each other by a thin dotted light gray line. Clean modern style, flat colors, no gradients, no shadows. Off-white background. Absolutely no text, no labels. 16:9 aspect ratio.
```

Die Formdifferenzierung (Kreis vs. Hexagone) verstärkt die visuelle Hierarchie. Die einzelne gestrichelte Sekundärverbindung zeigt, dass solche Querbeziehungen möglich sind, ohne die Hub-Struktur zu dominieren.

<div class="image-grid">
<div>
<img src="images/stil-03-hub/stil-03-formdiff-openai.png" alt="Hub-Struktur mit Formdifferenzierung – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-03-hub/stil-03-formdiff-gemini.png" alt="Hub-Struktur mit Formdifferenzierung – Gemini">
<em>Gemini</em>
</div>
</div>

#### Anpassungshinweise

**Elementanzahl:** Vier bis sechs periphere Elemente funktionieren am besten. Bei mehr Elementen tendieren die Modelle zu symmetrischer Kreisanordnung, was mechanisch wirkt. Bei weniger als vier Elementen kann die Struktur dünn erscheinen.

**Formdifferenzierung:** Die Verwendung unterschiedlicher Formen für Zentrum und Peripherie (etwa Kreis vs. Hexagone) verstärkt die Hierarchie. Sie ist optional, aber hilfreich wenn die Größendifferenz allein nicht ausreicht.

**Farbstrategie:** Der Kontrast zwischen Zentrum und Peripherie ist entscheidend. Bewährte Kombinationen sind kühles Zentrum mit warmer Peripherie (Teal vs. Terracotta-Töne) oder dunkles Zentrum mit heller Peripherie (Navy vs. Grüntöne). Die peripheren Elemente sollten untereinander farblich verwandt sein, um ihre Zusammengehörigkeit zu signalisieren.

**Sekundärverbindungen:** Je mehr Querverbindungen zwischen peripheren Elementen, desto mehr verwischt die Hub-Logik. Für klare Zentralstrukturen sollten Sekundärverbindungen weggelassen werden. Für Strukturen mit ausgewählten Querbeziehungen reichen ein bis zwei gestrichelte Verbindungen.

**Anordnung:** Die Anweisung "uneven spacing" oder "at different distances" verhindert perfekt kreisförmige Anordnungen. Eine leicht asymmetrische Verteilung wirkt organischer und weniger diagrammatisch.

**Bekannte Probleme:** Die Modelle tendieren dazu, mehr periphere Elemente zu erzeugen als spezifiziert, besonders wenn die Zahl nicht explizit genannt wird. ChatGPT ignoriert Farbfamilien-Anweisungen häufiger als Gemini und erzeugt bunte Regenbogen-Paletten. Bei solchen Ergebnissen hilft Neugenerierung.

---

### Stil 4: Schematische Komponenten-Dekomposition

**Strukturtyp:** Hierarchie (Teil-Ganzes)

**Zeigt:** Aufbau, Komponenten, Dekomposition – wie ein Ganzes aus Teilen besteht

**Theoretischer Bezug:** Die räumliche Anordnung codiert Teil-Ganzes-Beziehungen. Das zentrale Element repräsentiert das Ganze, die umgebenden Elemente die Teile. Die Verbindungslinien zeigen Zugehörigkeit. Der Stil nutzt die Konventionen moderner technischer Dokumentation und Flat-Design-Ästhetik.

**Geeignet für:** Strukturen, bei denen ein Ganzes in seine Bestandteile zerlegt werden soll. Systemarchitekturen, Begriffsanalysen, Anatomien, Produktstrukturen.

**Nicht geeignet für:** Über-/Unterordnung im Sinne von Rangfolgen, Entscheidungsbäume, zeitliche Entwicklungen, Beziehungen zwischen gleichwertigen Elementen.

**Abgrenzung zu Stil 3:** Stil 4 zeigt *Teil-Ganzes-Beziehungen* (die Komponenten sind Bestandteile des Ganzen). Stil 3 zeigt *assoziierte Bereiche* (die peripheren Elemente sind eigenständig, aber mit dem Zentrum verbunden).

**Abgrenzung zu Stil 6:** Stil 4 wählen, wenn die Teile ohne das Ganze nicht sinnvoll existieren. Stil 6 wählen, wenn die gruppierten Elemente auch unabhängig voneinander vorkommen können.

#### Prinzip

Die Komponenten-Dekomposition zeigt ein zentrales Objekt, umgeben von seinen Bestandteilen. Jede Komponente ist in einem eigenen Container dargestellt und durch eine Linie mit dem Zentrum verbunden. Die visuelle Sprache ist bewusst schematisch und verwendet Flat-Design-Ästhetik.

Das visuelle Schema folgt diesen Regeln:

- **Zentrum:** Das Ganze, dargestellt als erkennbares Objekt oder Symbol, mindestens doppelt so groß wie die Komponenten
- **Komponenten:** In rechteckigen Containern mit abgerundeten Ecken, gleichmäßig um das Zentrum verteilt
- **Verbindungen:** Einfache graue Linien vom Zentrum zu jeder Komponente
- **Icons:** Jede Komponente enthält ein flaches, stilisiertes Icon, das den Teil repräsentiert
- **Farblogik:** Container haben einheitlichen hellen Hintergrund, Icons verwenden eine begrenzte Farbpalette

#### Template-Prompt

```
A flat design component diagram showing [ZENTRALOBJEKT] in the center with [ANZAHL] component cards arranged around it. The central element is a simplified, flat icon of [ZENTRALOBJEKT-BESCHREIBUNG], clearly larger than the surrounding elements. Each component is shown in a rounded rectangle card with a flat colored icon inside and an empty label area below. The cards are connected to the center by thin gray lines. Components shown: [KOMPONENTEN-LISTE]. Style: modern flat design, solid colors, no gradients, no shadows, no 3D effects. Clean white background. Muted professional color palette. No text, no labels. 16:9 aspect ratio.
```

Die Variablen sind:

- ZENTRALOBJEKT: Das Ganze, das zerlegt wird
- ANZAHL: Typischerweise 6 bis 10 Komponenten
- ZENTRALOBJEKT-BESCHREIBUNG: Kurze visuelle Beschreibung des zentralen Elements
- KOMPONENTEN-LISTE: Aufzählung der Teile mit ihren Icon-Beschreibungen

#### Beispiel 1: Technisches System (Computer)

Geeignet für technische Dokumentation, Systemarchitekturen, Hardware-Übersichten.

```
A flat design component diagram showing a desktop computer in the center with 8 component cards arranged around it. The central element is a simplified, flat icon of a desktop PC tower case, clearly larger than the surrounding elements. Each component is shown in a rounded rectangle card with a flat colored icon inside and an empty label area below. The cards are connected to the center by thin gray lines. Components shown: CPU chip, RAM memory stick, hard drive, cooling fan, power supply unit, graphics card, motherboard circuit, USB cable. Style: modern flat design, solid colors, no gradients, no shadows, no 3D effects. Clean white background. Muted professional color palette with blues, grays, and occasional orange accents. No text, no labels. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-04-dekomposition/stil-04-technisch-openai.png" alt="Technisches System – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-04-dekomposition/stil-04-technisch-gemini.png" alt="Technisches System – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 2: Abstraktes Konzept

Geeignet für konzeptuelle Zerlegungen, bei denen das Ganze und seine Teile durch geometrische Formen repräsentiert werden.

```
A flat design component diagram showing an abstract central form (overlapping geometric shapes: circles, squares, triangles in teal and gold) with 6 component cards arranged around it. Each component card contains a single simple geometric shape (circle, square, triangle, hexagon, arrow, star) in the same teal and gold color scheme. The cards are rounded rectangles with a clean white interior and thin gray border, connected to the center by thin gray lines. Style: modern flat design, solid colors, no gradients, no shadows, no 3D effects. Clean white background. No text, no labels. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-04-dekomposition/stil-04-abstrakt-openai.png" alt="Abstraktes Konzept – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-04-dekomposition/stil-04-abstrakt-gemini.png" alt="Abstraktes Konzept – Gemini">
<em>Gemini</em>
</div>
</div>

#### Anpassungshinweise

**Zentralobjekt:** Kann konkret (Computer, Gebäude, Organismus) oder abstrakt (geometrische Komposition, Symbolgruppe) sein. Die Beschreibung sollte spezifisch genug sein, um ein erkennbares Objekt zu erzeugen.

**Komponentenanzahl:** Sechs bis zehn Komponenten funktionieren am besten. Weniger wirkt dünn, mehr überfrachtet das Diagramm.

**Anordnung:** Die Modelle verteilen die Komponenten typischerweise gleichmäßig um das Zentrum. Für asymmetrische Anordnungen kann "arranged asymmetrically" oder "with varying distances" ergänzt werden.

**Farbpalette:** Die Anweisung "muted professional color palette" liefert konsistente Ergebnisse. Für spezifische Farbschemata können konkrete Farben genannt werden.

#### Epistemische Einschränkung

Generative Bildmodelle interpretieren Teil-Ganzes-Beziehungen visuell, nicht semantisch. Sie können nicht prüfen, ob die genannten Komponenten tatsächlich Teile des Ganzen sind. Die Verantwortung für die inhaltliche Korrektheit liegt beim Promptschreiber. Für fachspezifische Anwendungen sollten die Komponentenlisten aus verlässlichen Quellen stammen.

---
### Stil 5: Transformation

**Strukturtyp:** Transformation

**Zeigt:** Wandlung, Zustandsänderung, qualitative Veränderung

**Theoretischer Bezug:** Die horizontale Anordnung codiert Zeit, die visuelle Veränderung codiert qualitative Transformation. Der Stil verwendet abstrakte Metaphern statt biologischer Referenzen, um domänenunabhängige Anwendbarkeit zu gewährleisten.

**Geeignet für:** Prozesse, bei denen das Ergebnis wesensmäßig anders ist als der Ausgangszustand. Lernprozesse, Entwicklungsstufen, Reifungsprozesse, paradigmatische Wechsel.

**Nicht geeignet für:** Rein technische Abläufe ohne qualitative Steigerung, reversible Prozesse, gleichwertige Schritte.

**Abgrenzung zu Stil 1:** Stil 5 zeigt *qualitative Veränderung* mit Richtung. Stil 1 zeigt *gleichwertige Schritte* ohne Steigerung.

#### Prinzip

Die Transformation wird durch eine horizontale Abfolge von Stadien dargestellt, jeweils in einer kreisförmigen Vignette, verbunden durch Pfeile. Das visuelle Prinzip:

- **Anfangszustand:** Dichter, dunkler, ungeordneter oder verschlossener
- **Zwischenstadien:** Gradueller Übergang, erste Anzeichen der Veränderung
- **Endzustand:** Klarer, heller, strukturierter oder entfaltet

Die Farbprogression unterstützt die Richtung, typischerweise von dunklen, kühlen Tönen zu hellen, warmen Tönen. Die Metapher (Kristallisation, Klärung, Entfaltung oder andere) muss im Prompt explizit beschrieben werden, sonst fallen Modelle auf biologische Metamorphose zurück.

#### Template-Prompt

```
A transformation diagram showing [ANZAHL] stages of qualitative change, arranged horizontally from left to right. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows. [STADIEN-BESCHREIBUNG]. Scientific illustration style with clean rendering, no decorative effects. Solid white background. No text, no labels. 16:9 aspect ratio.
```

Die Stadien-Beschreibung muss konkret genug sein, um visuelle Unterschiede zu erzeugen, aber abstrakt genug, um nicht auf ein spezifisches reales Objekt festzulegen.

<div class="image-grid">
<div>
<img src="images/stil-05-transformation/stil-05-template-openai.png" alt="Template-Struktur – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-05-transformation/stil-05-template-gemini.png" alt="Template-Struktur – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 1: Kristallisation (4 Stadien)

Geeignet für Ordnungsgewinn, Strukturierung, Reifung, Systematisierung.

```
A transformation diagram showing four stages of qualitative change, arranged horizontally from left to right. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows. Stage one: a dense cluster of rough, irregular dark gray rock fragments. Stage two: fragments begin to show angular facets, hints of crystalline structure emerge, medium gray-brown tones. Stage three: a more organized crystalline formation, distinct facets visible, warm amber-brown coloration. Stage four: a refined, upward-pointing crystal cluster with clear geometric facets, luminous golden-amber color. Scientific illustration style with clean rendering, no decorative sparkles or glow effects. Solid white background. No text, no labels. 16:9 aspect ratio.
```


<div class="image-grid">
<div>
<img src="images/stil-05-transformation/stil-05-kristallisation-openai.png" alt="Kristallisation – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-05-transformation/stil-05-kristallisation-gemini.png" alt="Kristallisation – Gemini">
<em>Gemini</em>
</div>
</div>

#### Beispiel 2: Klärung (3 Stadien)

Geeignet für Erkenntnisprozesse, Verständnis, Durchdringung, Abstraktion.

```
A transformation diagram showing 3 stages of qualitative change, arranged horizontally from left to right. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows. Stage one: a dense, cloudy, opaque spherical form in dark gray tones. Stage two: the form becomes partially translucent, lighter areas emerge, medium gray-blue tones. Stage three: a clear, transparent, luminous sphere with subtle inner structure visible, pale blue-white coloration. Scientific illustration style with clean rendering, no decorative effects. Solid white background. No text, no labels. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-05-transformation/stil-05-klaerung-openai.png" alt="Klärung – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-05-transformation/stil-05-klaerung-gemini.png" alt="Klärung – Gemini">
<em>Gemini</em>
</div>
</div>

#### Anpassungshinweise

Die Richtung kann umgekehrt werden (von komplex zu einfach, von hell zu dunkel) für Reduktions- oder Fokussierungsprozesse. Die Stadienanzahl ist variabel, 3 für einfache, 4 für differenzierte, 5 für feingliedrige Transformationen.

--- 
### Stil 6: Gestalt-Gruppierung

**Strukturtyp:** Kategorisierung

**Zeigt:** Zugehörigkeit, Cluster, Ähnlichkeitsgruppen, kategoriale Unterscheidungen

**Theoretischer Bezug:** Direkte Anwendung der Gestalt-Prinzipien der visuellen Wahrnehmung. Das Prinzip der Nähe bewirkt, dass räumlich benachbarte Elemente als zusammengehörig wahrgenommen werden. Das Prinzip der Ähnlichkeit gruppiert visuell gleichartige Elemente. Das Prinzip der Geschlossenheit fasst umschlossene Elemente zu Einheiten zusammen. Die Kombination dieser Prinzipien ermöglicht die Kommunikation von Gruppenzugehörigkeit ohne explizite Beschriftung.

**Geeignet für:** Typologien, Klassifikationen, Segmentierungen, Cluster-Analysen, kategoriale Unterscheidungen. Situationen, in denen gezeigt werden soll, welche Elemente zusammengehören.

**Nicht geeignet für:** Hierarchien mit Rangordnung, sequenzielle Abfolgen, Teil-Ganzes-Beziehungen, Mengenvergleiche mit Präzisionsanspruch.

**Abgrenzung zu Stil 2:** Stil 6 zeigt *Gruppenzugehörigkeit*, also was zusammengehört. Stil 2 zeigt *Mengen*, also wie viel im Verhältnis zu wie viel. Entscheidungskriterium: Geht es um die kategoriale Zuordnung oder um quantitative Proportionen?

**Abgrenzung zu Stil 4:** Stil 6 zeigt Gruppierungen *unabhängiger* Elemente nach Ähnlichkeit. Stil 4 zeigt Teile *eines* Ganzen, die konstitutiv zusammengehören. Entscheidungskriterium: Können die gruppierten Elemente auch unabhängig voneinander existieren, oder sind sie Bestandteile eines übergeordneten Ganzen?

**Abgrenzung zu Stil 11:** Stil 6 zeigt kategoriale Zugehörigkeit ohne Beziehungen zwischen den Elementen. Stil 11 zeigt Verbindungen zwischen Elementen in einem Netzwerk. Entscheidungskriterium: Geht es um Gruppenmitgliedschaft oder um Relationen?

#### Prinzip

Die Gestalt-Gruppierung codiert Kategoriezugehörigkeit durch visuelle Mittel. Elemente, die zusammengehören, werden räumlich nah beieinander positioniert und teilen visuelle Eigenschaften wie Farbe oder Form. Elemente unterschiedlicher Kategorien werden durch negative Räume getrennt und visuell differenziert.

Das visuelle Schema folgt diesen Regeln:

- **Cluster-Formation:** Elemente innerhalb eines Clusters überlappen sich teilweise und bilden eine visuelle Einheit, wie ein Stapel oder Haufen
- **Separation:** Großzügiger negativer Raum zwischen den Clustern macht die Gruppengrenzen unmittelbar wahrnehmbar
- **Farbcodierung:** Jeder Cluster verwendet eine distinkte Farbe aus einer harmonischen, gedeckten Palette
- **Formkonsistenz:** Innerhalb eines Clusters sind alle Elemente identisch, um maximale Gestalt-Wirkung zu erzielen
- **Beschriftungsflächen:** Leere Rechtecke mit farbigem Rahmen unterhalb jedes Clusters ermöglichen externe Beschriftung

Die überlappende Anordnung ist entscheidend. Einzelne Elemente nebeneinander wirken wie eine Aufzählung. Überlappende Elemente verschmelzen zu einer visuellen Gestalt, die präattentiv als Einheit wahrgenommen wird.

#### Template-Prompt

```
A diagram demonstrating visual grouping through Gestalt principles. [ANZAHL] distinct clusters arranged [ANORDNUNG] on [HINTERGRUND]. Each cluster contains [CLUSTER-GRÖSSE] identical [ELEMENTFORM] of the same type, partially overlapping to form a cohesive visual pile. [CLUSTER-BESCHREIBUNG]. Grouping is achieved through proximity, color similarity, and overlapping arrangement: elements within each cluster overlap slightly like stacked documents, while clusters are separated by generous negative space. Each cluster uses a distinct muted color: [FARBPALETTE]. Below each cluster, include an empty rectangular placeholder area with a thin border in the same color as the cluster above it. Style: clean minimalist design, flat simplified forms, no gradients, no shadows, no 3D effects. Absolutely no text, no labels, no annotations, no letters, no numbers anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- ANZAHL: Typischerweise 3 bis 5 Cluster
- ANORDNUNG: in a 2x2 grid, in a horizontal row, asymmetrically distributed
- HINTERGRUND: neutral light gray background, pure white background, soft off-white background
- CLUSTER-GRÖSSE: Angabe pro Cluster, etwa 5 to 7 elements each oder varying from 4 to 8 elements
- ELEMENTFORM: simple circles, small rounded squares, simplified icons, geometric shapes
- CLUSTER-BESCHREIBUNG: Spezifikation der Elemente pro Cluster
- FARBPALETTE: Begrenzte Palette mit einer Farbe pro Cluster, etwa dusty blue, warm terracotta, sage green, and soft amber

#### Beispiel 1: Proportionale Cluster (4 Cluster, quantitativ)

Geeignet für Darstellungen, bei denen die relative Größe oder Bedeutung der Kategorien kommuniziert werden soll. Marktanteile, Ressourcenverteilung, gewichtete Segmente.

```
A diagram demonstrating visual grouping with proportional sizing to indicate quantity or importance. 4 distinct clusters of overlapping circles arranged on a light gray background. Each cluster contains identical circles, but the clusters vary significantly in size. Cluster one in dusty blue: large cluster with 10-12 overlapping circles, taking substantial visual space. Cluster two in warm terracotta: medium cluster with 6-7 overlapping circles. Cluster three in sage green: small cluster with 3-4 overlapping circles. Cluster four in soft amber: very small cluster with just 2 overlapping circles. The varying sizes communicate relative magnitude. Below each cluster, include an empty rectangular placeholder area with width proportional to the cluster size above, thin border in matching color. Style: clean minimalist design, flat colors, no gradients, no shadows. Absolutely no text, no labels, no numbers. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-06-gruppierung/stil-06-proportional-openai.png" alt="Proportionale Cluster – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-06-gruppierung/stil-06-proportional-gemini.png" alt="Proportionale Cluster – Gemini">
<em>Gemini</em>
</div>
</div>

Die proportionale Variante erweitert die reine Kategorisierung um eine quantitative Dimension. Die Clustergröße codiert relative Bedeutung oder Menge, ohne exakte Zahlen zu beanspruchen. Die proportionalen Beschriftungsfelder verstärken diesen Effekt.

#### Beispiel 2: Textur-Differenzierung

Für barrierefreie Darstellungen oder monochromatische Kontexte. Die Cluster werden ausschließlich durch Textur unterschieden, nicht durch Farbe. Diese Variante funktioniert auch für farbenblinde Nutzende.

```
A diagram demonstrating visual grouping through texture and pattern rather than color. 4 distinct clusters of overlapping squares arranged on a pure white background. All clusters use the same muted gray-blue color, but each cluster has a different internal pattern. Cluster one: squares filled with thin horizontal lines. Cluster two: squares filled with small dots in a regular grid. Cluster three: squares filled with diagonal lines. Cluster four: squares filled solid without pattern. Each cluster contains 5-6 overlapping squares. The texture difference creates clear group distinction without relying on color. Generous negative space separates the clusters. Below each cluster, include an empty rectangular placeholder area with a thin gray border and a small sample of the cluster's pattern inside the left edge of the placeholder. Style: clean minimalist design, subtle patterns, monochromatic palette. Absolutely no text, no labels. 16:9 aspect ratio.
```

![Textur-Differenzierung – OpenAI](images/stil-06-gruppierung/stil-06-textur-openai.png)
*Textur-Differenzierung – OpenAI*

#### Beispiel 3: Organische Schwarmformation

Für Darstellungen mit impliziter Dynamik oder Richtung. Die Cluster werden als Schwärme dargestellt, deren Elemente sich in eine gemeinsame Richtung bewegen oder ein organisches Muster bilden.

```
A diagram demonstrating visual grouping through organic swarm-like formations inspired by natural patterns. 4 distinct clusters of small teardrop or seed-shaped elements arranged on a soft off-white background. Each cluster forms an organic, flowing shape rather than a geometric arrangement, as if the elements are moving together like a flock of birds or school of fish. Cluster one in dusty blue: elements flowing toward the upper right. Cluster two in warm terracotta: elements flowing toward the left. Cluster three in sage green: elements in a circular swirl pattern. Cluster four in soft amber: elements dispersing outward from a center point. Each cluster contains 8-12 small identical elements. The organic arrangements suggest dynamic grouping and shared direction. Below each cluster, include an empty rectangular placeholder area with a thin border in matching color. Style: clean minimalist design, flat colors, organic natural feeling, no gradients, no shadows. Absolutely no text, no labels. 16:9 aspect ratio.
```

![Schwarmformation – OpenAI](images/stil-06-gruppierung/stil-06-schwarm-openai.png)
*Schwarmformation – OpenAI*

#### Beispiel 4: Territoriale Zonen

Für räumliche oder institutionelle Verteilungen. Die Cluster werden als organische Flächen dargestellt, die an thematische Karten erinnern. Die Zonen berühren sich fast, aber nicht ganz, wie Staaten auf einer Landkarte.

```
A diagram demonstrating visual grouping through territorial zones, inspired by thematic cartography. 4 distinct irregular blob shapes arranged on a cream-colored background, resembling regions on a map. Each blob has soft, organic edges rather than geometric boundaries. Blob one in pale dusty blue. Blob two in pale warm terracotta. Blob three in pale sage green. Blob four in pale soft amber. Within each blob, 4 to 6 small circular markers in a darker shade of the same color are scattered naturally. The blobs do not touch but are separated by narrow channels of background color, like borders between territories. Below the entire composition, include 4 empty rectangular placeholder areas arranged horizontally, each with a thin border matching one blob color. Style: soft organic shapes, muted watercolor-like flat fills, no gradients, no shadows. Absolutely no text, no labels. 16:9 aspect ratio.
```

![Territoriale Zonen – Gemini](images/stil-06-gruppierung/stil-06-territorial-gemini.png)
*Territoriale Zonen – Gemini*

#### Beispiel 5: Kontinuität durch Verbindungslinien

Für Darstellungen, bei denen die interne Verbundenheit der Gruppenelemente betont werden soll. Die Elemente werden durch geschwungene Linien verbunden, die das Gestalt-Prinzip der Kontinuität nutzen.

```
A diagram demonstrating visual grouping through the Gestalt principle of continuity. 4 distinct clusters of small circles arranged on a pure white background. Within each cluster, the circles are connected by thin curved lines that flow smoothly from element to element, creating a sense of continuous path. The connecting lines within each cluster share the same color as the circles. Cluster one in dusty blue with 6 connected circles. Cluster two in warm terracotta with 5 connected circles. Cluster three in sage green with 7 connected circles. Cluster four in soft amber with 4 connected circles. No lines connect different clusters. Generous negative space separates the clusters. Below each cluster, include an empty rectangular placeholder area with a thin border in the same color. Style: clean minimalist design, thin elegant lines, no gradients, no shadows. Absolutely no text, no labels. 16:9 aspect ratio.
```

![Kontinuität – Gemini](images/stil-06-gruppierung/stil-06-kontinuitaet-gemini.png)
*Kontinuität – Gemini*

#### Anpassungshinweise

**Elementwahl:** Identische Elemente pro Cluster erzeugen stärkere Gestalt-Wirkung als gemischte. Ein Cluster aus fünf Briefumschlägen wirkt kohärenter als ein Cluster aus Briefumschlag, Buch und Telefon. Für heterogene Kategorien kann die abstrakte Variante mit geometrischen Formen vorgezogen werden.

**Überlappungsgrad:** Die Formulierung "partially overlapping to form a cohesive visual pile" ist entscheidend. Zu wenig Überlappung erzeugt keine Gestalt, zu viel Überlappung macht die Einzelelemente unkenntlich. Ein Überlappungsgrad von etwa 20 bis 30 Prozent funktioniert gut.

**Farbstrategie:** Die Farben sollten kategorial distinkt, aber harmonisch sein. Gedeckte Paletten wie dusty blue, warm terracotta, sage green, soft amber funktionieren besser als gesättigte Primärfarben. Die farbigen Beschriftungsrahmen verstärken die Zuordnung.

**Clusteranzahl:** Drei bis fünf Cluster sind optimal. Bei zwei Clustern wirkt die Darstellung wie ein Vergleich statt wie eine Klassifikation. Bei mehr als sechs Clustern wird die Unterscheidung schwierig.

**Räumliche Anordnung:** Das 2x2-Raster nutzt den Bildraum gut und suggeriert keine Rangfolge. Horizontale Reihen können eine implizite Ordnung von links nach rechts suggerieren. Asymmetrische Anordnung wirkt organischer, erfordert aber mehr Anpassung.

#### Varianten-Auswahl

Die Wahl der Variante hängt vom Kommunikationsziel ab:

| Wenn du zeigen willst... | Verwende Variante... |
|---|---|
| Kategoriale Zugehörigkeit (Basisfall) | Überlappende Icons oder Formen |
| Relative Größe oder Bedeutung | Proportionale Cluster |
| Räumliche oder institutionelle Verteilung | Territoriale Zonen |
| Barrierefreie Darstellung ohne Farbabhängigkeit | Textur-Differenzierung |
| Interne Verbundenheit der Elemente | Kontinuität durch Linien |
| Dynamik oder Richtung | Organische Schwarmformation |

#### Bekannte Probleme

**Icon-Konsistenz:** Bei figurativen Varianten erzeugen Modelle gelegentlich unterschiedliche Icons innerhalb eines Clusters. Die Formulierung "identical icons of the same type" reduziert dieses Problem, garantiert aber keine Konsistenz. Bei inkonsistenten Ergebnissen hilft Neugenerierung.

**Überlappung:** Manche Modelle interpretieren "overlapping" als Transparenz-Überlagerung statt als Stapel-Anordnung. Beide Interpretationen funktionieren visuell, aber der Stapel-Effekt ist intuitiver.

**Beschriftungsrahmen:** Die farbigen Rahmen werden zuverlässig erzeugt. Die Anweisung für proportionale Rahmenbreiten bei der proportionalen Variante wird nicht immer befolgt und kann in der Nachbearbeitung korrigiert werden.

**Territoriale Variante:** Die organischen Blob-Formen variieren stark zwischen Generierungen. Für konsistente Ergebnisse kann die Anweisung "soft, organic edges like amoeba shapes" hinzugefügt werden.

---

### Stil 7: Skalierung und Überwältigung

**Strukturtyp:** Skalierung (qualitativ)

**Zeigt:** Verhältnis zwischen dem Erfassbaren und dem Unerfassbaren, große Mengen kognitiv zugänglich gemacht, das Einzelne im Verhältnis zur Masse

**Theoretischer Bezug:** Der Stil nutzt die kognitive Grenze der *Subitizing*-Fähigkeit. Menschen können bis etwa vier bis fünf Elemente instantan erfassen, darüber hinaus beginnt das Zählen. Der Übergang vom Zählbaren zum Unzählbaren macht Größenordnungen erfahrbar, die sonst abstrakt bleiben. Die Tradition des Datenjournalismus, insbesondere die Arbeiten von David McCandless, hat diese Technik für die Kommunikation von Statistiken etabliert. Der Begriff *Anti-Sublim* verweist auf die rhetorische Strategie, das Erhabene nicht durch Größe zu erzeugen, sondern durch die Konfrontation mit der eigenen Wahrnehmungsgrenze.

**Geeignet für:** Korpusgrößen, Archivbestände, historische Zeitspannen, Bevölkerungszahlen, Datenmengen, Stichprobengrößen. Situationen, in denen die schiere Menge selbst die Botschaft ist.

**Nicht geeignet für:** Präzise Mengenvergleiche, Proportionen zwischen Kategorien, Strukturen innerhalb der Menge.

**Abgrenzung zu Stil 2:** Stil 2 zeigt *Verhältnisse zwischen Mengen*, wobei beide Mengen zählbar oder zumindest vergleichbar bleiben. Stil 7 zeigt das *Verhältnis zwischen dem Zählbaren und dem Unzählbaren*. Entscheidungskriterium: Geht es um den Vergleich zweier Größen oder um die Erfahrung von Überwältigung?

**Abgrenzung zu Stil 6:** Stil 6 gruppiert Elemente nach Kategorien, wobei die Elemente distinkt bleiben. Stil 7 lässt Elemente in Textur übergehen, wobei die Unterscheidbarkeit verloren geht. Entscheidungskriterium: Sollen die Elemente als Individuen wahrnehmbar bleiben?

#### Prinzip

Die Skalierungsvisualisierung arbeitet mit dem Kontrast zwischen zwei Zonen. Eine kleine, klar abgegrenzte Zone zeigt wenige Elemente, die einzeln wahrnehmbar und zählbar sind. Der Rest des Bildes füllt sich mit denselben Elementen, aber in einer Dichte, die sie zur Textur werden lässt. Der Übergang von der einen zur anderen Zone kann abrupt oder graduell sein, beide Varianten funktionieren.

Das visuelle Schema folgt diesen Regeln:

- **Zählbare Zone:** Wenige Elemente, typischerweise 5 bis 10, in einer Akzentfarbe, großzügig verteilt, klar voneinander unterscheidbar
- **Masse:** Dieselben Elemente in einer neutralen Farbe, so dicht gepackt, dass sie zur Textur werden
- **Farbkontrast:** Die Akzentfarbe hebt die zählbare Zone hervor, die Masse bleibt in gedämpftem Grau
- **Positionierung:** Die zählbare Zone befindet sich typischerweise in einer Ecke oder am Rand, um den Größenunterschied zu betonen
- **Keine Beschriftungsflächen:** Anders als bei anderen Stilen braucht dieser Stil keine externen Labels, weil das Bild für sich selbst spricht

Der epistemische Effekt entsteht durch die körperliche Erfahrung der eigenen Wahrnehmungsgrenze. Die Betrachtenden *erleben*, dass sie die Masse nicht erfassen können, während sie die wenigen hervorgehobenen Elemente mühelos zählen.

#### Template-Prompt

```
A flat 2D visualization representing overwhelming scale made comprehensible. [MENGENBESCHREIBUNG] filling [BILDFÜLLUNG]. In [POSITION], [ZÄHLBARE-ANZAHL] [ELEMENTFORM] in [AKZENTFARBE] are clearly countable and individually distinct, [SAMPLE-DETAIL]. The rest of the image fills with the same elements in [MASSENFARBE], [DICHTEBESCHREIBUNG]. The stark contrast between the small countable sample and the incomprehensible mass is the core message. Style: strictly flat 2D design, no perspective, no shadows, no depth, no 3D effects, no gradients, clean vector-like rendering. Background: [HINTERGRUND]. Absolutely no text, no numbers, no labels anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- MENGENBESCHREIBUNG: Thousands of tiny identical document icons, Hundreds of thin vertical lines, Thousands of small circles
- BILDFÜLLUNG: most of the image in a dense grid, the image horizontally as a single band, the entire image
- POSITION: the lower left corner, the left side, a small rectangular area
- ZÄHLBARE-ANZAHL: exactly 5, exactly 10, exactly 6
- ELEMENTFORM: document icons with a folded corner, vertical lines, circles, squares
- AKZENTFARBE: warm orange, vivid coral, bright amber
- SAMPLE-DETAIL: separated from the mass by white space, evenly spaced, generously spaced within a bordered area
- MASSENFARBE: muted gray, cool gray, faded blue-gray
- DICHTEBESCHREIBUNG: packed so densely they become texture rather than countable units, progressively compressing until they merge into solid gray, increasing in density until individual elements are indistinguishable
- HINTERGRUND: pure white, soft off-white, neutral light gray

#### Beispiel 1: Dokumentenkorpus (Forschungsdaten)

Geeignet für die Visualisierung von Korpusgrößen, Archivbeständen, Editionsprojekten oder Datensammlungen. Die figurative Darstellung mit Dokumenten-Icons macht die Anwendung für Forschende unmittelbar nachvollziehbar.

```
A flat 2D visualization representing overwhelming scale made comprehensible. Thousands of tiny identical document icons with a folded corner filling most of the image in a dense grid. In the lower left corner, exactly 5 document icons in warm orange are clearly countable and individually distinct, separated from the mass by a small margin of white space. The rest of the image fills with the same document icons in muted gray, packed so densely they become texture rather than countable units. The stark contrast between the small countable sample and the incomprehensible archive mass is the core message. Style: strictly flat 2D design, no perspective, no shadows, no depth, no 3D effects, simplified icon shapes, clean vector-like rendering. Background: pure white. Absolutely no text, no numbers, no labels anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-07-skalierung/stil-07-dokumente-openai.png" alt="Dokumentenkorpus – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-07-skalierung/stil-07-dokumente-gemini.png" alt="Dokumentenkorpus – Gemini">
<em>Gemini</em>
</div>
</div>

Die Dokumenten-Variante eignet sich besonders für die Kommunikation von Archivgrößen oder Korpusumfängen. Fünf hervorgehobene Dokumente stehen für das, was ein Mensch tatsächlich lesen kann. Die graue Masse repräsentiert das, was ungelesen bleibt.

#### Beispiel 2: Zeitspanne (historische Dimension)

Geeignet für die Visualisierung von Zeiträumen, Epochen oder Generationen. Die horizontale Anordnung suggeriert eine Zeitleiste, der Übergang von Zählbar zu Textur macht historische Tiefe erfahrbar.

```
A flat 2D visualization representing overwhelming scale made comprehensible. Hundreds of thin vertical lines representing years arranged horizontally across the image in a single band. On the left side, exactly 10 vertical lines in vivid coral are evenly spaced and clearly countable, representing a decade. Moving rightward, the lines transition to cool gray and progressively compress, becoming denser and denser until they merge into a solid gray block on the right side where individual lines are no longer distinguishable. The transition from countable to uncountable moves smoothly from left to right. The composition makes deep time viscerally comprehensible by showing how small a decade is within centuries. Style: strictly flat 2D design, no perspective, no shadows, no depth, no 3D effects, precise straight lines, clean vector-like rendering. Background: soft off-white. Absolutely no text, no numbers, no labels anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-07-skalierung/stil-07-zeitspanne-openai.png" alt="Zeitspanne – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-07-skalierung/stil-07-zeitspanne-gemini.png" alt="Zeitspanne – Gemini">
<em>Gemini</em>
</div>
</div>

Die Zeitspannen-Variante macht historische Tiefe körperlich erfahrbar. Zehn Jahre lassen sich überblicken. Vierhundert Jahre werden zur undifferenzierten Masse. Diese Visualisierung eignet sich für Einleitungen zu Langzeitstudien oder für die Kontextualisierung historischer Forschung.

#### Anpassungshinweise

**Elementwahl:** Abstrakte Formen wie Kreise oder Quadrate funktionieren für domänenunabhängige Darstellungen. Figurative Icons wie Dokumente, Personen oder Bücher erhöhen die Konkretheit und Anschlussfähigkeit für spezifische Kontexte.

**Dichtegradient:** Der Übergang von Zählbar zu Unzählbar kann abrupt oder graduell sein. Die Dokumenten-Variante arbeitet mit abruptem Kontrast, die Zeitspannen-Variante mit graduellem Übergang. Beide funktionieren, erzeugen aber unterschiedliche rhetorische Effekte. Der abrupte Kontrast betont den Unterschied, der graduelle Übergang betont die Kontinuität.

**Anzahl der hervorgehobenen Elemente:** Fünf bis zehn Elemente sind optimal. Weniger als fünf wirkt nicht repräsentativ, mehr als zehn überfordert die Subitizing-Fähigkeit und schwächt den Kontrast.

**Positionierung:** Die hervorgehobene Zone sollte in einer Ecke oder am Rand liegen, nicht im Zentrum. Die periphere Position verstärkt den Eindruck der Marginalität gegenüber der Masse.

**Farbwahl:** Warme Akzentfarben wie Orange, Coral oder Amber kontrastieren gut mit der neutralen grauen Masse. Die Akzentfarbe sollte auffällig, aber nicht aggressiv sein.

**Alternative Varianten:** Für Datenpunkte in quantitativer Forschung kann die Dokumenten-Variante durch Kreise ersetzt werden. Für Textmengen in Editionsprojekten können horizontale Rechtecke verwendet werden, die Textzeilen suggerieren. Die Struktur des Prompts bleibt dabei gleich.

#### Bekannte Probleme

**3D-Interpretation:** Trotz expliziter Flat-Design-Anweisungen erzeugen manche Modelle gelegentlich perspektivische Darstellungen. Die Formulierung "strictly flat 2D design, no perspective, no shadows, no depth, no 3D effects" reduziert dieses Problem, garantiert aber keine Konsistenz. Bei 3D-Ergebnissen hilft Neugenerierung.

**Dichtekontrolle:** Die exakte Dichte der Masse ist schwer zu steuern. Manche Ergebnisse zeigen zu lockere Anordnungen, die den Textur-Effekt nicht erreichen. Die Formulierung "packed so densely they become texture" verbessert die Ergebnisse, aber Variation bleibt.

**Sample-Positionierung:** Die Position der hervorgehobenen Zone wird nicht immer exakt befolgt. "Lower left corner" führt zuverlässiger zu konsistenten Ergebnissen als "bottom left" oder andere Formulierungen.

**Elementanzahl:** Die exakte Anzahl der hervorgehobenen Elemente wird häufig ignoriert. "Exactly 5" kann zu 4, 6 oder 7 Elementen führen. Für präzise Kontrolle ist Nachbearbeitung erforderlich.

---

### Stil 8: Rhetorischer Kontrast

**Strukturtyp:** Gegenüberstellung

**Zeigt:** Gegensätze, Spannungen, Dualismen, Vorher/Nachher, Dichotomien

**Theoretischer Bezug:** Die rhetorische Figur der *Antithese* visualisiert. Der Kontrast erzeugt Bedeutung durch Differenz, nicht durch isolierte Betrachtung. Die Gestalt-Psychologie beschreibt dies als *Figur-Grund-Relation*, wobei hier beide Seiten abwechselnd als Figur und Grund fungieren können. Die Zweiteilung des Bildraums ist eine der ältesten visuellen Argumentationsformen und findet sich von mittelalterlichen Diptychen bis zu modernen Infografiken.

**Geeignet für:** Vergleiche, Vorher/Nachher-Darstellungen, Dichotomien, Spannungsverhältnisse, konkurrierende Paradigmen, qualitative Unterschiede.

**Nicht geeignet für:** Graduelle Übergänge, Spektren, Kontinua, mehr als zwei Zustände.

**Abgrenzung zu Stil 2:** Stil 2 zeigt *quantitative* Verhältnisse zwischen Mengen. Stil 8 zeigt *qualitative* Gegensätze zwischen Zuständen. Entscheidungskriterium: Geht es um wie viel oder um was für ein?

**Abgrenzung zu Stil 5:** Stil 5 zeigt *Transformation* als Prozess von A nach B. Stil 8 zeigt *Kontrast* als gleichzeitige Gegenüberstellung. Entscheidungskriterium: Soll eine Entwicklung oder ein Unterschied kommuniziert werden?

#### Prinzip

Der rhetorische Kontrast arbeitet mit der Zweiteilung des Bildraums. Zwei Zonen werden nebeneinander gestellt, typischerweise durch eine vertikale Trennlinie separiert. Die Bedeutung entsteht durch den Vergleich. Was auf der einen Seite gezeigt wird, gewinnt Bedeutung durch das, was auf der anderen Seite fehlt oder anders ist.

Das visuelle Schema folgt diesen Regeln:

- **Zweiteilung:** Das Bild wird vertikal in zwei gleich große Zonen geteilt
- **Kontrastierende Eigenschaften:** Dieselben Grundelemente erscheinen in beiden Zonen, aber mit unterschiedlichen Eigenschaften wie Anordnung, Dichte, Farbe oder Ausrichtung
- **Trennlinie:** Eine dünne vertikale Linie markiert die Grenze zwischen den Zonen
- **Farbcodierung:** Jede Zone verwendet eine distinkte Farbe, die den Kontrast verstärkt
- **Beschriftungsflächen:** Leere Rechtecke unterhalb jeder Zone ermöglichen externe Beschriftung

Der Kontrast kann auf verschiedenen Dimensionen operieren: Ordnung versus Chaos, Dichte versus Leere, Statik versus Dynamik, Homogenität versus Heterogenität. Die gewählte Dimension sollte zur inhaltlichen Aussage passen.

#### Template-Prompt

```
A flat 2D visualization demonstrating rhetorical contrast through visual opposition. The image is divided into two distinct zones by a thin vertical line in the center. Left zone: [LINKE-BESCHREIBUNG]. Right zone: [RECHTE-BESCHREIBUNG]. The contrast between the two sides creates meaning through difference. [VERBINDENDES-ELEMENT]. Below each zone, include an empty rectangular placeholder area with a thin border in [RAHMENFARBE]. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean vector-like rendering. Background: [HINTERGRUND]. Absolutely no text, no labels, no annotations anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- LINKE-BESCHREIBUNG: Vollständige Beschreibung der linken Zone mit Elementen, Anordnung und Farbe
- RECHTE-BESCHREIBUNG: Vollständige Beschreibung der rechten Zone mit kontrastierenden Eigenschaften
- VERBINDENDES-ELEMENT: Erklärung, was beide Zonen gemeinsam haben (z.B. dieselben Grundelemente)
- RAHMENFARBE: Typischerweise matching the zone color above
- HINTERGRUND: pure white, soft warm gray, neutral light gray

#### Beispiel 1: Ordnung versus Chaos (Methodologie)

Geeignet für die Visualisierung von Strukturierung versus Unstrukturiertheit, systematischen versus ad-hoc Ansätzen, formalisierten versus informellen Prozessen.

```
A flat 2D visualization demonstrating rhetorical contrast through visual opposition. The image is divided into two distinct zones by a thin vertical line in the center. Left zone: geometric shapes arranged in a perfect grid pattern, all shapes are identical squares in muted blue, evenly spaced, aligned precisely, suggesting order and system. Right zone: the same squares in warm coral scattered randomly, rotated at various angles, overlapping chaotically, clustered unevenly, suggesting disorder and entropy. The contrast between the two sides creates meaning through difference. Both zones use the same square elements, only the arrangement differs. Below each zone, include an empty rectangular placeholder area with a thin border matching the zone color above. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean vector-like rendering. Background: pure white. Absolutely no text, no labels, no annotations anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-08-kontrast/stil-08-ordnung-chaos-openai.png" alt="Ordnung vs. Chaos – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-08-kontrast/stil-08-ordnung-chaos-gemini.png" alt="Ordnung vs. Chaos – Gemini">
<em>Gemini</em>
</div>
</div>

Die Ordnung-Chaos-Variante eignet sich für methodologische Kontexte. Sie kann die Differenz zwischen strukturierten und unstrukturierten Daten, zwischen formalisierten und informellen Prozessen oder zwischen systematischen und explorativen Ansätzen visualisieren.

#### Beispiel 2: Dichte versus Leere (Ressourcenverteilung)

Geeignet für die Visualisierung von Ungleichverteilungen, Konzentration versus Streuung, Überfluss versus Mangel.

```
A flat 2D visualization demonstrating rhetorical contrast through visual opposition. The image is divided into two distinct zones by a thin vertical line in the center. Left zone: densely packed small circles in deep teal filling the entire left half, so many circles they almost merge into texture, suggesting abundance and saturation. Right zone: only 3 small circles in the same deep teal scattered sparsely across a vast empty space, suggesting scarcity and absence. The contrast between the two sides creates meaning through difference. Both zones use the same element type and color, only the density differs dramatically. Below each zone, include an empty rectangular placeholder area with a thin teal border. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean vector-like rendering. Background: soft warm gray. Absolutely no text, no labels, no annotations anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-08-kontrast/stil-08-dichte-leere-openai.png" alt="Dichte vs. Leere – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-08-kontrast/stil-08-dichte-leere-gemini.png" alt="Dichte vs. Leere – Gemini">
<em>Gemini</em>
</div>
</div>

Die Dichte-Leere-Variante kommuniziert Ungleichverteilung ohne Zahlen. Sie eignet sich für die Darstellung von Ressourcenkonzentration, Aufmerksamkeitsverteilung oder Forschungsintensität in verschiedenen Bereichen.

#### Anpassungshinweise

**Kontrastdimension:** Die Wahl der Kontrastdimension sollte zur inhaltlichen Aussage passen. Ordnung versus Chaos für methodologische Fragen, Dichte versus Leere für Verteilungsfragen, Alt versus Neu für historische Vergleiche, Organisch versus Mechanisch für Paradigmenkontraste.

**Elementkonsistenz:** Beide Zonen sollten dieselben Grundelemente verwenden. Der Kontrast entsteht durch unterschiedliche Eigenschaften derselben Elemente, nicht durch unterschiedliche Elementtypen. Diese Konsistenz macht den Vergleich valide.

**Farbwahl:** Kontrastierende, aber harmonische Farben verstärken die Lesbarkeit. Blau versus Coral, Teal versus Amber, Grau versus Orange funktionieren gut. Zu ähnliche Farben schwächen den Kontrast.

**Trennlinie:** Die vertikale Trennlinie sollte dünn und neutral sein. Sie markiert die Grenze, ohne selbst Aufmerksamkeit zu binden. In manchen Fällen kann die Trennlinie auch weggelassen werden, wenn der Kontrast stark genug ist.

**Symmetrie:** Die beiden Zonen sollten gleich groß sein, um keine implizite Wertung zu suggerieren. Asymmetrische Aufteilungen kommunizieren Dominanz einer Seite.

#### Bekannte Probleme

**Elementanzahl:** Die genaue Anzahl der Elemente in jeder Zone wird selten exakt umgesetzt. Für die rhetorische Wirkung ist das unproblematisch, solange der qualitative Kontrast erhalten bleibt.

**Überlappung:** Bei der Chaos-Variante können Elemente über die Trennlinie hinausragen. Dies kann durch explizite Anweisungen wie "elements stay within the zone boundaries" adressiert werden.

**Beschriftungsflächen:** Die farbigen Rahmen werden zuverlässig erzeugt. Die Position unterhalb der Zonen wird konsistent eingehalten.

---

### Stil 9: Stratigraphische Zeitschichtung

**Strukturtyp:** Zeitliche Ablagerung

**Zeigt:** Historische Schichten, Epochen, sedimentierte Zeit, Entwicklungsphasen, akkumulierte Geschichte

**Theoretischer Bezug:** Die geologische Metapher der *Stratigraphie* visualisiert Zeit als vertikale Ablagerung. Ältere Schichten liegen unten, jüngere oben. Diese Darstellungskonvention entstammt der Archäologie und Geologie, wo sie buchstäblich der physischen Realität entspricht. Foucault adaptierte die Metapher für seine Wissensarchäologie, um historische Diskursformationen als Sedimentschichten zu konzeptualisieren. Die Visualisierung macht diese Metapher konkret.

**Geeignet für:** Historische Epochen, Entwicklungsphasen, Projektgeschichte, akkumulierte Wissensschichten, Quellenüberlieferung.

**Nicht geeignet für:** Zyklische Prozesse, gleichzeitige Ereignisse, nicht-chronologische Strukturen.

**Abgrenzung zu Stil 1:** Stil 1 zeigt Phasen als *horizontale Sequenz* von links nach rechts. Stil 9 zeigt Epochen als *vertikale Schichtung* von unten nach oben. Entscheidungskriterium: Soll die Abfolge oder die Akkumulation betont werden?

**Abgrenzung zu Stil 10:** Stil 9 zeigt *lineare* Akkumulation ohne Wiederkehr. Stil 10 zeigt *zyklische* Wiederkehr mit Variation. Entscheidungskriterium: Kehren die Phasen wieder oder sind sie einmalig?

#### Prinzip

Die stratigraphische Visualisierung stapelt horizontale Bänder übereinander. Jedes Band repräsentiert eine Zeitschicht, Epoche oder Phase. Die unterste Schicht ist die älteste, die oberste die jüngste. Die relative Höhe der Schichten kann die relative Dauer codieren.

Das visuelle Schema folgt diesen Regeln:

- **Horizontale Bänder:** Jede Zeitschicht wird als horizontales Band dargestellt, das die gesamte Bildbreite einnimmt
- **Vertikale Stapelung:** Die Bänder liegen direkt übereinander, von unten nach oben chronologisch geordnet
- **Trennlinien:** Dünne weiße Linien separieren die Schichten, wie Sedimentgrenzen
- **Farbcodierung:** Jede Schicht verwendet eine distinkte Farbe aus einer harmonischen Palette
- **Höhenvariation:** Die Schichthöhe kann die relative Dauer oder Bedeutung codieren
- **Beschriftungsflächen:** Rechteckige Placeholders am rechten Rand jeder Schicht ermöglichen externe Beschriftung

Optional können kleine Icons in die Schichten eingebettet werden, wie Fossilien in Gestein. Diese Icons repräsentieren epochentypische Elemente oder Quellen.

#### Template-Prompt

```
A flat 2D visualization demonstrating temporal stratification like geological layers. [ANZAHL] horizontal bands stacked vertically, representing [ZEITKONZEPT]. The bottom layer is the oldest, the top layer is the most recent. [SCHICHTBESCHREIBUNG]. Each layer has a distinct color from a harmonious palette: [FARBPALETTE]. The layers touch but do not blend, with thin white lines separating them. On the right side of each layer, include an empty rectangular placeholder area with a thin border matching the layer color, positioned within the layer. Style: strictly flat 2D design, no perspective, no shadows, no texture, no gradients, no 3D effects, clean horizontal bands with sharp edges. Background: visible only at the edges as [HINTERGRUND]. Absolutely no text, no labels, no dates anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- ANZAHL: Typischerweise 3 bis 6 Schichten
- ZEITKONZEPT: historical epochs, research phases, development stages
- SCHICHTBESCHREIBUNG: Details zu Höhenvariation und optionalen eingebetteten Icons
- FARBPALETTE: Typischerweise von warmen Erdtönen unten zu kühleren Tönen oben
- HINTERGRUND: soft off-white, neutral gray

#### Beispiel 1: Historische Epochen (4 Schichten)

Geeignet für die Visualisierung von Epochengliederungen, Periodisierungen oder historischen Überblicken.

```
A flat 2D visualization demonstrating temporal stratification like geological layers. 4 horizontal bands stacked vertically, representing historical epochs from ancient to modern. The bottom layer is the thickest and represents the longest period, each subsequent layer becomes slightly thinner, with the top layer being the thinnest. The bottom layer in muted terracotta. The second layer in dusty gold. The third layer in sage green. The top layer in cool blue. The layers touch but do not blend, with thin white lines separating them. On the right side of each layer, include an empty rectangular placeholder area with a thin border matching the layer color, positioned within the layer. Style: strictly flat 2D design, no perspective, no shadows, no texture, no gradients, no 3D effects, clean horizontal bands with sharp edges. Background: visible only at the edges as soft off-white. Absolutely no text, no labels, no dates anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-09-schichtung/stil-09-epochen-openai.png" alt="Historische Epochen – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-09-schichtung/stil-09-epochen-gemini.png" alt="Historische Epochen – Gemini">
<em>Gemini</em>
</div>
</div>

Die variierende Schichthöhe kommuniziert unterschiedliche Zeitspannen. Die dickste Schicht unten suggeriert die längste Epoche, die dünnste Schicht oben die kürzeste. Diese Proportionen können in der Nachbearbeitung präzisiert werden.

#### Beispiel 2: Forschungsphasen mit Artefakten (5 Schichten)

Geeignet für die Visualisierung von Projektgeschichte, Quellenüberlieferung oder Technologieentwicklung.

```
A flat 2D visualization demonstrating temporal stratification like geological layers. 5 horizontal bands stacked vertically, representing phases of a research project from inception to completion. Each layer contains 2-3 small simplified icons embedded within it like fossils in rock: bottom layer in pale coral contains tiny scroll icons, second layer in pale amber contains tiny book icons, third layer in pale sage contains tiny document icons, fourth layer in pale teal contains tiny computer icons, top layer in pale blue contains tiny cloud icons. The icons are subtle and small, integrated into each layer rather than floating on top. The layers touch but do not blend, with thin white lines separating them. On the right side of each layer, include an empty rectangular placeholder area with a thin border matching the layer color. Style: strictly flat 2D design, no perspective, no shadows, no texture, no gradients, no 3D effects, simplified geometric icons. Background: visible only at the edges as neutral gray. Absolutely no text, no labels, no dates anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-09-schichtung/stil-09-forschungsphasen-openai.png" alt="Forschungsphasen – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-09-schichtung/stil-09-forschungsphasen-gemini.png" alt="Forschungsphasen – Gemini">
<em>Gemini</em>
</div>
</div>

Die eingebetteten Icons zeigen epochentypische Medien und Technologien. Von Schriftrollen über Bücher und Dokumente zu Computern und Cloud-Symbolen wird die Entwicklung der Forschungsinfrastruktur lesbar.

#### Anpassungshinweise

**Schichtanzahl:** Drei bis sechs Schichten sind optimal. Weniger als drei wirkt nicht wie eine Schichtung, mehr als sechs wird unübersichtlich.

**Farbprogression:** Eine Progression von warmen Erdtönen unten zu kühleren Tönen oben verstärkt die Metapher der geologischen Tiefe. Alternative Paletten sind möglich, sollten aber eine erkennbare Progression aufweisen.

**Höhenvariation:** Gleich hohe Schichten suggerieren gleich lange Perioden. Unterschiedliche Höhen kommunizieren unterschiedliche Dauern. Die Proportionen sollten zur historischen Realität passen oder explizit als schematisch gekennzeichnet werden.

**Eingebettete Icons:** Die Fossilien-Metapher funktioniert gut für Quellentypen, Medien oder Technologien. Die Icons sollten klein und subtil sein, um die Schichtstruktur nicht zu dominieren.

**Leserichtung:** Die Konvention liest von unten nach oben als von alt nach neu. Diese Konvention sollte nicht umgekehrt werden, da sie in Geologie und Archäologie etabliert ist.

#### Bekannte Probleme

**Schichthöhen:** Die exakten Proportionen der Schichthöhen werden selten präzise umgesetzt. Für schematische Darstellungen ist das akzeptabel, für maßstabsgetreue Darstellungen ist Nachbearbeitung erforderlich.

**Icon-Platzierung:** Die Position der eingebetteten Icons variiert. Manche Ergebnisse zeigen die Icons am Rand statt in der Schicht. Die Formulierung "embedded within" hilft, garantiert aber keine konsistente Platzierung.

**Trennlinien:** Die weißen Trennlinien werden zuverlässig erzeugt. In manchen Fällen sind sie sehr dünn und kaum sichtbar, was die Schichttrennung schwächt.

---

### Stil 10: Zyklus-Spirale

**Strukturtyp:** Iteration und Wiederkehr

**Zeigt:** Wiederkehrende Prozesse, zyklische Entwicklung, iterative Verfeinerung, Phasen die sich wiederholen aber weiterentwickeln

**Theoretischer Bezug:** Die Spirale verbindet zyklische Wiederkehr mit linearem Fortschritt. Im Gegensatz zum geschlossenen Kreis kehrt die Spirale nicht zum identischen Ausgangspunkt zurück, sondern zu einer veränderten Version desselben Punktes. Diese Form visualisiert dialektische Entwicklung im Sinne Hegels, iterative Forschungsprozesse und agile Methodologien. Die Spirale ist das visuelle Äquivalent der Formulierung: Wir durchlaufen dieselben Phasen, aber auf höherem Niveau.

**Geeignet für:** Iterative Forschungsprozesse, agile Methodologien, zyklische Entwicklung, wiederkehrende Evaluationsschleifen, Lernzyklen.

**Nicht geeignet für:** Einmalige Sequenzen, lineare Entwicklungen ohne Wiederkehr, Prozesse ohne erkennbare Phasenstruktur.

**Abgrenzung zu Stil 1:** Stil 1 zeigt Phasen als *einmalige* Sequenz. Stil 10 zeigt Phasen als *wiederkehrende* Zyklen. Entscheidungskriterium: Werden die Phasen einmal oder mehrfach durchlaufen?

**Abgrenzung zu Stil 9:** Stil 9 zeigt *akkumulierte* Geschichte ohne Wiederkehr. Stil 10 zeigt *iterierte* Phasen mit Variation. Entscheidungskriterium: Schichten sich die Phasen oder wiederholen sie sich?

#### Prinzip

Die Zyklus-Spirale zeigt einen Pfad, der sich vom Zentrum nach außen windet und dabei wiederkehrende Segmente durchläuft. Jedes Segment repräsentiert eine Phase, die sich mit jeder Windung wiederholt. Die Expansion der Spirale zeigt Wachstum oder Fortschritt.

Das visuelle Schema folgt diesen Regeln:

- **Spiralpfad:** Eine kontinuierliche Linie windet sich vom Zentrum nach außen
- **Farbsegmente:** Der Pfad ist in wiederkehrende Farbsegmente unterteilt, wobei jede Farbe eine Phase repräsentiert
- **Phasenwiederholung:** Dieselbe Farbsequenz wiederholt sich mit jeder Windung
- **Wachstum:** Jede Windung ist größer als die vorherige, was Entwicklung suggeriert
- **Übergangsknoten:** Kleine Kreise oder Punkte markieren die Übergänge zwischen Phasen
- **Beschriftungsflächen:** Rechteckige Placeholders am Bildrand, farblich den Phasen zugeordnet

#### Template-Prompt

```
A flat 2D visualization demonstrating cyclical progression through a spiral form. A spiral expanding outward from the center of the image, making [WINDUNGEN] complete rotations. The spiral path is divided into [SEGMENTANZAHL] distinct segments per rotation, each segment in a different color: [FARBPALETTE]. The segments repeat in the same color sequence with each rotation, showing the cyclical nature. Each rotation is larger than the previous, suggesting growth and development. At the transition points between colors, include small circular nodes in the same color as the segment ending. [PLACEHOLDER-POSITION] include [ANZAHL] empty rectangular placeholder areas, each with a thin border matching one segment color. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean curved lines of medium thickness, clearly visible spiral path. Background: [HINTERGRUND]. Absolutely no text, no labels, no numbers anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- WINDUNGEN: Typischerweise 2 bis 4 Windungen
- SEGMENTANZAHL: Typischerweise 3 bis 5 Phasen pro Zyklus
- FARBPALETTE: Distinkte Farben für jede Phase, z.B. dusty blue, warm coral, sage green, soft amber
- PLACEHOLDER-POSITION: At the bottom of the image, Near the outer edge of the spiral
- HINTERGRUND: pure white, soft off-white

#### Beispiel 1: Forschungszyklus (4 Phasen)

Geeignet für die Visualisierung von iterativen Forschungsprozessen mit Planung, Durchführung, Analyse und Reflexion.

```
A flat 2D visualization demonstrating cyclical progression through a spiral form. A spiral expanding outward from the center of the image, making 3 complete rotations. The spiral path is divided into 4 distinct segments per rotation, each segment in a different color: dusty blue for planning, warm coral for execution, sage green for analysis, soft amber for reflection. The segments repeat in the same color sequence with each rotation, showing the cyclical nature of research. Each rotation is slightly larger than the previous, suggesting growth and development. At the end of each segment where colors change, include a small circular node in the same color. At the bottom of the image, include 4 empty rectangular placeholder areas arranged in a horizontal row, each with a thin border matching one segment color. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean curved lines of medium thickness, clearly visible spiral path. Background: pure white. Absolutely no text, no labels, no numbers anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-10-spirale/stil-10-forschungszyklus-openai.png" alt="Forschungszyklus – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-10-spirale/stil-10-forschungszyklus-gemini.png" alt="Forschungszyklus – Gemini">
<em>Gemini</em>
</div>
</div>

Die Vier-Phasen-Spirale zeigt einen klassischen Forschungszyklus. Die Wiederholung der Farbsequenz mit jeder Windung macht die Iterationen sichtbar. Die Expansion nach außen suggeriert Fortschritt und Vertiefung.

#### Beispiel 2: Iterativer Prozess (3 Phasen)

Geeignet für die Visualisierung von agilen Methodologien, Design-Thinking-Schleifen oder anderen Drei-Phasen-Iterationen.

```
A flat 2D visualization demonstrating cyclical progression through a spiral form. A tight spiral expanding outward from the center, making 4 complete rotations. The spiral path is divided into 3 distinct segments per rotation: deep teal, warm terracotta, and muted gold. The segments repeat in the same color sequence with each rotation. The innermost rotation is small and compact, each subsequent rotation expands significantly, showing iterative growth. The line thickness is consistent throughout. At the transition points between colors, include small diamond-shaped nodes. At the bottom of the image, include 3 empty rectangular placeholder areas arranged horizontally, each with a thin border matching one segment color. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean smooth curves. Background: soft off-white. Absolutely no text, no labels, no numbers anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-10-spirale/stil-10-iteration-openai.png" alt="Iterativer Prozess – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-10-spirale/stil-10-iteration-gemini.png" alt="Iterativer Prozess – Gemini">
<em>Gemini</em>
</div>
</div>

Die Drei-Phasen-Spirale eignet sich für schlankere Iterationsmodelle. Die kompaktere Segmentierung und die vier Windungen zeigen mehr Durchläufe bei weniger Komplexität pro Zyklus.

#### Anpassungshinweise

**Phasenanzahl:** Drei bis fünf Phasen pro Zyklus sind optimal. Weniger als drei wirkt nicht wie ein Zyklus, mehr als fünf macht die Wiederholung schwer erkennbar.

**Windungsanzahl:** Zwei bis vier Windungen zeigen die Wiederholung deutlich. Eine Windung ist kein Zyklus, mehr als vier wird visuell unübersichtlich.

**Farbkonsistenz:** Die Farbsequenz muss in jeder Windung identisch sein. Dies ist das zentrale visuelle Argument für die Zyklizität. Abweichungen zerstören die Lesbarkeit.

**Wachstumsrate:** Die Expansion der Spirale kann gleichmäßig oder beschleunigt sein. Gleichmäßiges Wachstum suggeriert stetigen Fortschritt, beschleunigtes Wachstum suggeriert kumulative Entwicklung.

**Leserichtung:** Die Spirale wird typischerweise vom Zentrum nach außen gelesen, also von der ersten Iteration zur letzten. Diese Leserichtung entspricht der zeitlichen Abfolge.

#### Bekannte Probleme

**Segmentkonsistenz:** Die exakte Wiederholung der Farbsequenz wird nicht immer perfekt umgesetzt. Manche Ergebnisse zeigen Variationen in der Segmentlänge oder Farbzuordnung.

**Knotenplatzierung:** Die Übergangsknoten werden manchmal weggelassen oder inkonsistent platziert. Die Formulierung "at the transition points" hilft, garantiert aber keine perfekte Umsetzung.

**Placeholder-Position:** Die Position der Beschriftungsflächen variiert. "At the bottom" führt zu konsistenteren Ergebnissen als andere Positionsangaben.

**Spiralform:** Manche Modelle erzeugen konzentrische Kreise statt einer echten Spirale. Die Formulierung "continuous spiral path" und "expanding outward" adressiert dieses Problem.

---

### Stil 11: Netzwerk-Konstellation

**Strukturtyp:** Relationen

**Zeigt:** Verbindungen, Beziehungen, Abhängigkeiten, Verflechtungen, Akteurskonstellationen

**Theoretischer Bezug:** Die Netzwerkvisualisierung entstammt der *Graphentheorie* und wurde durch die Akteur-Netzwerk-Theorie und die Soziale Netzwerkanalyse für die Geistes- und Sozialwissenschaften erschlossen. Knoten repräsentieren Entitäten, Kanten repräsentieren Relationen. Die räumliche Anordnung suggeriert Nähe oder Distanz, auch wenn diese Positionierung in den meisten Fällen algorithmisch erzeugt wird und keine inhärente Bedeutung trägt. Die Visualisierung macht Strukturen sichtbar, die in tabellarischen Daten verborgen bleiben.

**Geeignet für:** Akteurskonstellationen, Korrespondenznetze, Zitationsnetzwerke, Kooperationsstrukturen, Abhängigkeiten, Verflechtungen.

**Nicht geeignet für:** Hierarchien mit klarer Rangordnung, zeitliche Abfolgen, Teil-Ganzes-Beziehungen.

**Abgrenzung zu Stil 3:** Stil 3 zeigt eine *Hub-Struktur* als konzeptuelles Schema. Stil 11 zeigt *empirische Netzwerke* mit multiplen Verbindungen und komplexer Topologie. Entscheidungskriterium: Geht es um ein idealtypisches Zentrum-Peripherie-Modell oder um die Darstellung tatsächlicher Relationen?

**Abgrenzung zu Stil 6:** Stil 6 zeigt *Gruppenzugehörigkeit* ohne Verbindungen zwischen Elementen. Stil 11 zeigt *Relationen* zwischen Elementen. Entscheidungskriterium: Soll Kategoriezugehörigkeit oder Verbundenheit kommuniziert werden?

#### Prinzip

Die Netzwerk-Konstellation zeigt Entitäten als Knoten und ihre Beziehungen als Verbindungslinien. Die visuelle Struktur kommuniziert Zentralität, Cluster, Isolation und Verbindungsdichte.

Das visuelle Schema folgt diesen Regeln:

- **Knoten:** Kreise repräsentieren Entitäten. Größe kann Bedeutung oder Zentralität codieren
- **Kanten:** Linien zwischen Knoten repräsentieren Relationen. Alle Linien sind gleich gewichtet, keine Pfeile
- **Cluster:** Räumliche Nähe und Farbähnlichkeit suggerieren Gruppenzugehörigkeit
- **Zentrum-Peripherie:** Zentral positionierte Knoten wirken wichtiger als periphere
- **Beschriftungsflächen:** Rechteckige Placeholders am unteren Bildrand, farblich den Knotentypen zugeordnet

Die Anordnung sollte organisch wirken, nicht zu geometrisch. Perfekte Symmetrie suggeriert ein idealtypisches Modell, nicht ein empirisches Netzwerk.

#### Template-Prompt

```
A flat 2D visualization demonstrating network relationships through nodes and connections. [KNOTENANZAHL] circular nodes of [KNOTENGRÖSSE] arranged [ANORDNUNG] on [HINTERGRUND]. The nodes are connected by thin straight lines representing relationships. [VERBINDUNGSBESCHREIBUNG]. [KNOTENDIFFERENZIERUNG]. The network should feel [NETZWERKCHARAKTER]. Below the network, include [PLACEHOLDER-ANZAHL] empty rectangular placeholder areas with thin borders in colors matching the node types above. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean circles and thin lines, no arrows on connections. Background: [HINTERGRUND]. Absolutely no text, no labels, no names anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- KNOTENANZAHL: Typischerweise 10 bis 20 Knoten
- KNOTENGRÖSSE: varying sizes, uniform medium size
- ANORDNUNG: in a loose constellation, in visible clusters, with clear center-periphery structure
- VERBINDUNGSBESCHREIBUNG: Details zu Verbindungsmustern innerhalb und zwischen Gruppen
- KNOTENDIFFERENZIERUNG: Farbcodierung und Größenvariation der Knotentypen
- NETZWERKCHARAKTER: organic and balanced, hierarchical with clear structure, decentralized and distributed
- PLACEHOLDER-ANZAHL: Entspricht der Anzahl der Knotentypen
- HINTERGRUND: pure white, soft off-white, neutral light gray

#### Beispiel 1: Akteurskonstellationen (3 Gruppen)

Geeignet für die Visualisierung von Stakeholder-Netzwerken, institutionellen Verflechtungen oder Kooperationsstrukturen mit erkennbaren Gruppen.

```
A flat 2D visualization demonstrating network relationships through nodes and connections. 12 circular nodes of varying sizes arranged in a loose constellation across the image. The nodes form 3 visible clusters: 4 nodes in dusty blue grouped in the upper left area, 4 nodes in warm coral grouped in the lower right area, and 4 nodes in sage green scattered in between. Nodes within each cluster are connected to each other by thin lines in their cluster color. A few thin gray lines connect nodes from different clusters, showing inter-group relationships. Node sizes vary: each cluster has one larger central node and 3 smaller peripheral nodes. The network should feel organic and balanced, not rigidly geometric. Below the network, include 3 empty rectangular placeholder areas with thin borders matching the three cluster colors. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean circles and thin lines, no arrows. Background: pure white. Absolutely no text, no labels, no names anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-11-netzwerk/stil-11-akteure-openai.png" alt="Akteurskonstellationen – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-11-netzwerk/stil-11-akteure-gemini.png" alt="Akteurskonstellationen – Gemini">
<em>Gemini</em>
</div>
</div>

Die Drei-Cluster-Variante zeigt Gruppen mit internen Verbindungen und selteneren Brücken zwischen Gruppen. Die Größenvariation innerhalb der Cluster suggeriert unterschiedliche Zentralität der Akteure.

#### Beispiel 2: Zentralisiertes Netzwerk (Hub-Struktur)

Geeignet für die Visualisierung von Netzwerken mit klarem Zentrum, etwa Korrespondenznetze um eine zentrale Figur oder Organisationsstrukturen mit dominantem Akteur.

```
A flat 2D visualization demonstrating network relationships through nodes and connections. One large central node in warm amber surrounded by 8 medium-sized nodes in muted blue arranged in a rough circle around it. Each peripheral node connects to the central hub with a thin line. The peripheral nodes also have 1-2 connections to their immediate neighbors, forming a secondary ring structure. Beyond the inner ring, 6 small nodes in soft gray are scattered at the edges, each connected to only one inner-ring node. The network should feel hierarchical with clear center-periphery structure. Below the network, include 3 empty rectangular placeholder areas with thin borders: amber for the hub, blue for the inner ring, gray for the periphery. Style: strictly flat 2D design, no perspective, no shadows, no gradients, no 3D effects, clean circles and thin straight lines, uniform line thickness. Background: soft off-white. Absolutely no text, no labels, no names anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-11-netzwerk/stil-11-hub-openai.png" alt="Zentralisiertes Netzwerk – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-11-netzwerk/stil-11-hub-gemini.png" alt="Zentralisiertes Netzwerk – Gemini">
<em>Gemini</em>
</div>
</div>

Die Hub-Variante zeigt ein Netzwerk mit klarer Hierarchie. Das zentrale Element dominiert, der innere Ring bildet die primäre Peripherie, die äußeren Knoten sind nur indirekt verbunden. Diese Struktur findet sich in Korrespondenznetzen um prominente Figuren oder in zentralisierten Organisationen.

#### Anpassungshinweise

**Knotenanzahl:** Zehn bis zwanzig Knoten sind optimal für statische Visualisierungen. Weniger wirkt trivial, mehr wird unübersichtlich. Für größere Netzwerke sind interaktive Visualisierungen oder Aggregationen erforderlich.

**Verbindungsdichte:** Zu wenige Verbindungen lassen das Netzwerk fragmentiert wirken, zu viele erzeugen visuelle Überlastung. Als Faustregel sollte jeder Knoten zwei bis vier Verbindungen haben.

**Farbcodierung:** Farben sollten Knotentypen oder Cluster markieren, nicht individuelle Knoten. Zu viele Farben zerstören die Lesbarkeit.

**Größenvariation:** Knotengröße kann Zentralität, Bedeutung oder eine quantitative Variable codieren. Die Variation sollte deutlich genug sein, um wahrnehmbar zu sein, aber nicht so extrem, dass kleine Knoten verschwinden.

**Räumliche Anordnung:** Die Position der Knoten suggeriert Nähe oder Distanz, auch wenn diese Positionierung oft willkürlich ist. Cluster sollten räumlich gruppiert sein, Brückenknoten zwischen Clustern positioniert.

**Kantengewichtung:** Für einfache Visualisierungen sollten alle Kanten gleich gewichtet sein. Unterschiedliche Linienstärken für Beziehungsintensität sind möglich, aber erhöhen die Komplexität.

#### Bekannte Probleme

**Knotenüberlappung:** Bei dichteren Netzwerken überlappen Knoten manchmal. Die Formulierung "nodes should not overlap" hilft, wird aber nicht immer befolgt.

**Verbindungslinien:** Die Linien kreuzen sich häufig. Dies ist bei komplexeren Netzwerken unvermeidlich, kann aber durch manuelle Nachbearbeitung reduziert werden.

**Clusterbildung:** Die gewünschte Clusterstruktur wird nicht immer erkennbar umgesetzt. Explizite Positionsangaben wie "in the upper left area" verbessern die Ergebnisse.

**Placeholder-Position:** Die Beschriftungsflächen werden zuverlässig am unteren Bildrand erzeugt. Die Farbzuordnung zu den Knotentypen funktioniert meist korrekt.

---

### Stil 12: Epistemische Unschärfe

**Strukturtyp:** Unsicherheit und Vagheit

**Zeigt:** Grenzen des Wissens, Hypothetisches, Umstrittenes, Ungewisses, Grade der Sicherheit, unscharfe Kategorien

**Theoretischer Bezug:** Die visuelle Kommunikation von Unsicherheit ist ein offenes Problem der Informationsvisualisierung. Konventionelle Diagramme suggerieren durch scharfe Grenzen eine Gewissheit, die oft nicht gegeben ist. Der Stil adaptiert Techniken aus der *Fuzzy-Set*-Theorie, der Visualisierung von Konfidenzintervallen und der kartografischen Darstellung umstrittener Grenzen. Die bewusste Verwendung von Unschärfe kommuniziert epistemische Bescheidenheit und macht Wissensgrenzen sichtbar.

**Geeignet für:** Hypothetische Zusammenhänge, umstrittene Kategorisierungen, Grade der Gewissheit, unscharfe Begriffe, Wissenslücken.

**Nicht geeignet für:** Präzise Daten, eindeutige Kategorien, Fakten ohne Unsicherheit.

**Abgrenzung zu Stil 6:** Stil 6 zeigt *scharfe* Kategorien mit klaren Grenzen. Stil 12 zeigt *unscharfe* Kategorien mit graduellen Übergängen. Entscheidungskriterium: Sind die Kategoriengrenzen eindeutig oder umstritten?

**Abgrenzung zu allen anderen Stilen:** Stil 12 ist der einzige Stil, der bewusst auf visuelle Präzision verzichtet. Diese Unschärfe ist nicht Mangel, sondern Botschaft.

#### Prinzip

Die epistemische Unschärfe verwendet weiche Kanten, Transparenz und graduelle Übergänge, um Unsicherheit zu visualisieren. Scharfe Elemente markieren Gewissheit, unscharfe Elemente markieren Ungewissheit.

Das visuelle Schema folgt diesen Regeln:

- **Weiche Kanten:** Unsichere Grenzen werden mit Farbverläufen oder verschwommenen Rändern dargestellt
- **Transparenz:** Überlappende transparente Flächen zeigen unscharfe Kategorien, die ineinander übergehen
- **Kontrast scharf/unscharf:** Der Unterschied zwischen gewissem und ungewissem Wissen wird durch den Unterschied zwischen scharfen und unscharfen Formen kommuniziert
- **Farbintensität:** Gesättigtere Farben im Zentrum, ausbleichende Farben zur Peripherie codieren abnehmende Gewissheit
- **Beschriftungsflächen:** Die Placeholders können selbst unscharf sein, etwa durch gestrichelte Rahmen, die die Unsicherheit spiegeln

#### Template-Prompt

```
A flat 2D visualization demonstrating epistemic uncertainty through visual ambiguity. [GRUNDSTRUKTUR]. [UNSCHÄRFEBESCHREIBUNG]. The visualization communicates that boundaries are uncertain and categories overlap. [KONTRASTDETAIL]. Style: flat 2D design with intentional soft edges where uncertainty is shown, sharp edges only where certainty exists, no perspective, no shadows, no 3D effects. Use [TECHNIK] to indicate uncertainty. Background: [HINTERGRUND]. Include [PLACEHOLDER-ANZAHL] empty rectangular placeholder areas below, with borders that [RAHMENBESCHREIBUNG]. Absolutely no text, no labels, no question marks anywhere in the image. 16:9 aspect ratio.
```

Die Variablen sind:

- GRUNDSTRUKTUR: Beschreibung der Grundelemente, z.B. overlapping circles, concentric zones
- UNSCHÄRFEBESCHREIBUNG: Details zur Darstellung der Unsicherheit
- KONTRASTDETAIL: Optionaler Kontrast zwischen scharfen und unscharfen Elementen
- TECHNIK: transparency and soft edges, feathered boundaries, opacity gradients
- HINTERGRUND: pure white, soft off-white, neutral light gray
- PLACEHOLDER-ANZAHL: Entspricht der Anzahl der Kategorien oder Zonen
- RAHMENBESCHREIBUNG: are rendered as dashed lines, progress from solid to dashed

#### Beispiel 1: Überlappende Kategorien (Fuzzy Boundaries)

Geeignet für die Visualisierung von Kategorien, deren Grenzen umstritten oder graduell sind. Zeigt, dass Elemente mehreren Kategorien gleichzeitig angehören können.

```
A flat 2D visualization demonstrating epistemic uncertainty through visual ambiguity. 3 large circular zones arranged horizontally with significant overlap between adjacent zones. The left zone in dusty blue, the center zone in sage green, the right zone in warm coral. Where zones overlap, the colors blend creating intermediate tones: blue-green between left and center, green-coral between center and right. The edges of all zones are soft and feathered rather than sharp, fading gradually into the background. The center of each zone is more saturated, becoming increasingly transparent toward the edges. The visualization communicates that boundaries are uncertain and categories overlap. Style: flat 2D design with intentional soft feathered edges, colors at 60% opacity to allow blending, no perspective, no shadows, no 3D effects. Use transparency and soft edges to indicate uncertainty. Background: pure white. Include 3 empty rectangular placeholder areas below, with borders in matching colors but rendered as dashed lines to echo the uncertain boundaries above. Absolutely no text, no labels, no question marks anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-12-unschaerfe/stil-12-kategorien-openai.svg" alt="Überlappende Kategorien – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-12-unschaerfe/stil-12-kategorien-gemini.png" alt="Überlappende Kategorien – Gemini">
<em>Gemini</em>
</div>
</div>

Die überlappenden Kreise zeigen drei Kategorien, die nicht scharf voneinander abgrenzbar sind. Die Mischfarben in den Überlappungszonen machen die Zwischenbereiche sichtbar. Die gestrichelten Beschriftungsrahmen spiegeln die Unsicherheit der dargestellten Grenzen.

#### Beispiel 2: Konfidenzgrade (Kern und Peripherie)

Geeignet für die Visualisierung von Wissenskernen und spekulativen Rändern. Zeigt Grade der Gewissheit als konzentrische Zonen.

```
A flat 2D visualization demonstrating epistemic uncertainty through visual ambiguity. A central element surrounded by zones of decreasing certainty. In the center, a solid dark teal circle with sharp edges represents confirmed knowledge. Around it, a larger ring in medium teal with slightly soft edges represents probable knowledge. Around that, an even larger ring in light teal with very soft, feathered edges represents possible knowledge. The outermost zone fades almost completely into the background, representing speculation. The visualization communicates degrees of certainty radiating outward from a solid core to uncertain periphery. Each concentric zone is clearly distinguishable but transitions are gradual rather than sharp. Style: flat 2D design with progressively softer edges moving outward, sharp center fading to uncertain edges, no perspective, no shadows, no 3D effects. Use opacity gradients and edge softness to indicate uncertainty levels. Background: soft off-white. Include 4 empty rectangular placeholder areas below arranged horizontally, with borders progressing from solid dark teal on the left to dashed light teal on the right, mirroring the certainty gradient above. Absolutely no text, no labels, no question marks anywhere in the image. 16:9 aspect ratio.
```

<div class="image-grid">
<div>
<img src="images/stil-12-unschaerfe/stil-12-konfidenz-openai.svg" alt="Konfidenzgrade – OpenAI">
<em>OpenAI</em>
</div>
<div>
<img src="images/stil-12-unschaerfe/stil-12-konfidenz-gemini.png" alt="Konfidenzgrade – Gemini">
<em>Gemini</em>
</div>
</div>

Die konzentrischen Zonen zeigen abnehmende Gewissheit vom Kern zur Peripherie. Der scharfe Kern repräsentiert gesichertes Wissen, die weichen Ränder repräsentieren Spekulation. Die Beschriftungsflächen spiegeln diesen Gradienten durch den Übergang von durchgezogenen zu gestrichelten Linien.

#### Anpassungshinweise

**Unschärfegrad:** Die Intensität der Unschärfe sollte zur inhaltlichen Aussage passen. Leichte Unschärfe für geringe Unsicherheit, starke Unschärfe für fundamentale Wissensgrenzen.

**Kontrastelemente:** Scharfe Elemente in der Nähe unscharfer verstärken den Effekt. Das Nebeneinander von Gewissem und Ungewissem macht die Unsicherheit erst lesbar.

**Farbwahl:** Gedeckte Farben funktionieren besser als gesättigte, weil sie die sanften Übergänge unterstützen. Starke Farbkontraste in Überlappungszonen können die Unschärfe untergraben.

**Placeholder-Gestaltung:** Die gestrichelten Beschriftungsrahmen sind ein starkes visuelles Element, das die Unsicherheit auch in den Labels kommuniziert. Diese Konsistenz verstärkt die Botschaft.

**Kombination mit anderen Stilen:** Epistemische Unschärfe kann als Modifikation anderer Stile verwendet werden. Ein Netzwerk mit unscharfen Kanten, eine Zeitleiste mit verschwommenen Phasengrenzen, eine Gruppierung mit überlappenden Kategorien.

#### Bekannte Probleme

**Unschärfe-Konsistenz:** Die Intensität der Unschärfe variiert zwischen Generierungen. Manche Ergebnisse sind zu scharf, andere zu diffus. Die Formulierung "soft feathered edges" und "gradually fading" hilft, aber Nachbearbeitung kann erforderlich sein.

**Farbmischung:** Die Mischfarben in Überlappungszonen werden nicht immer plausibel erzeugt. Manche Modelle zeigen Additiv-Mischung, andere Subtraktiv-Mischung, wieder andere keine erkennbare Mischung.

**Lesbarkeit:** Zu viel Unschärfe kann die Lesbarkeit zerstören. Die Balance zwischen epistemischer Botschaft und visueller Klarheit erfordert Erfahrung und gegebenenfalls Iteration.

**Gestrichelte Linien:** Die gestrichelten Placeholder-Rahmen werden meist korrekt umgesetzt, aber die Strichlänge und Abstände variieren.

---

## Schnellreferenz: Welcher Stil wofür?

|Wenn du zeigen willst...|Verwende Stil...|
|---|---|
|Abfolge gleichwertiger Schritte|1 (Sequenz)|
|Mengen und Proportionen (präzise)|2 (Isotype)|
|Bereiche mit einem Zentrum|3 (Wissens-Territorium)|
|Aufbau und Komponenten|4 (Komponenten-Dekomposition)|
|Qualitative Wandlung|5 (Metamorphose)|
|Kategorien und Cluster|6 (Gestalt-Gruppierung)|
|Große Mengen, Masse (qualitativ)|7 (Anti-Sublim)|
|Kern vs. Peripherie|8 (Rhetorischer Kontrast)|
|Zeitliche Schichten|9 (Stratigraphie)|
|Zyklen und Iteration|10 (Spirale)|
|Netzwerke ohne Zentrum|11 (Konstellation)|
|Unsicherheit und Hypothesen|12 (Epistemische Unschärfe)|

## Abgrenzungshilfen

|Verwechslungsgefahr|Unterscheidungskriterium|Theoretischer Bezug|
|---|---|---|
|Stil 1 vs. Stil 5|Gleichwertige Schritte vs. qualitative Veränderung|Bertin: geordnete vs. ungeordnete Komponenten|
|Stil 1 vs. Stil 10|Einmalige Sequenz vs. wiederkehrende Phasen|Prozesstheorie: linear vs. zyklisch|
|Stil 2 vs. Stil 6|Mengenvergleich vs. Gruppenzugehörigkeit|Bertin: quantitativ vs. kategorial|
|Stil 2 vs. Stil 7|Präzise Quantifizierung vs. qualitativer Eindruck|ISOTYPE: Zählbarkeit als Prinzip|
|Stil 3 vs. Stil 11|Ein Zentrum vs. kein/mehrere Zentren|Netzwerktheorie: Hub-and-Spoke vs. dezentral|
|Stil 4 vs. Stil 6|Teil-Ganzes-Beziehung vs. Ähnlichkeitsgruppierung|Mereologie vs. Klassifikation|

## Grenzen und Erweiterungen

### Nicht abgedeckte Aufgabentypen

Die zwölf Stile decken häufige epistemische Operationen ab, aber nicht alle. Folgende Aufgaben erfordern möglicherweise Anpassungen oder Kombinationen.

**Korrelationsdarstellung:** Das Zeigen von Zusammenhängen zwischen zwei oder mehr Variablen ist nicht durch einen eigenen Stil abgedeckt. Für diese Aufgabe können Stil 11 (Netzwerk) oder Stil 6 (Gestalt-Gruppierung) adaptiert werden, oder klassische Streudiagramme außerhalb dieses Systems verwendet werden.

**Kausalitätsdarstellung:** Keiner der zwölf Stile ist explizit für die Darstellung von Ursache-Wirkungs-Beziehungen konzipiert. Stil 1 (Sequenz) zeigt Abfolge, nicht Verursachung. Stil 11 (Netzwerk) zeigt Verbindungen, nicht deren Richtung oder kausale Natur. Für kausale Zusammenhänge können gerichtete Graphen oder Flussdiagramme außerhalb dieses Systems verwendet werden, oder Stil 1 mit explizit asymmetrischen Pfeilen adaptiert werden.

**Anomalie-Erkennung:** Das Hervorheben von Ausreißern oder Abweichungen vom Erwarteten kann durch Stil 8 (Rhetorischer Kontrast) angenähert werden, erfordert aber typischerweise quantitative Referenzwerte.

**Räumliche Verteilung:** Geografische Verteilungsmuster sind durch Stil 3 (Wissens-Territorium) nur metaphorisch abgedeckt. Für tatsächliche kartografische Darstellungen sind spezialisierte Werkzeuge erforderlich.

### Kombinationsmöglichkeiten

Komplexe Sachverhalte können mehrere Visualisierungen erfordern. Einige produktive Kombinationen sind:

- Stil 1 + Stil 5 für Prozesse mit sowohl gleichwertigen als auch transformativen Phasen
- Stil 3 + Stil 11 für Strukturen mit einem Zentrum und dezentralen Substrukturen
- Stil 9 + Stil 12 für historische Entwicklungen mit unsicherer Quellenlage

## Domänenanpassung

Die Stile sind domänenunabhängig konzipiert, aber die verwendeten Icons und Symbole entstammen einem allgemeinen Repertoire. Für spezifische Fachbereiche können die Prompts durch domänenspezifische Elemente ergänzt werden, ohne die strukturellen Eigenschaften zu verändern.

## Hinweise zur Anwendung

### Farblogik

Die Prompts verwenden eine konsistente Farbsemantik. Warme Farben (Orange, Terracotta, Gold) codieren typischerweise Wichtigkeit, Nähe oder Gegenwart. Kühle Farben (Blau, Grau, Grün) codieren Peripherie, Distanz oder Vergangenheit. Sättigung korreliert mit Gewissheit oder Relevanz. Diese Konventionen sind kulturell geprägt und können für spezifische Kontexte angepasst werden.

### Prompt-Anpassung

Die Icons und Farben in den Prompts sind Platzhalter. Sie können durch kontextspezifische Elemente ersetzt werden, ohne den Stil zu verändern. Die strukturellen Elemente (Anordnung, Verbindungstypen, Farblogik) sollten beibehalten werden.

### Iteration

Generative Bildmodelle liefern nicht immer beim ersten Versuch optimale Ergebnisse. Mehrfaches Generieren mit demselben Prompt ist normal. Bei systematischen Abweichungen kann der Prompt durch zusätzliche Constraints angepasst werden.

### Text-Constraints

Die Anweisung „no text" wird nicht immer befolgt. Bei Stilen mit starker Genre-Konvention (Botanische Taxonomie, Isotype) kann Text erscheinen, der nachträglich entfernt werden muss. Alternativ können Phrasen wie „absolutely no text, no labels, no letters, no words, no numbers anywhere in the image" verstärkt werden.

### Modellspezifische Variation

Die Prompts wurden primär mit Nano Banana Pro (Gemini 3 Imagen) getestet. Bei anderen Modellen können Anpassungen erforderlich sein. DALL-E tendiert zu stärkerer Stilisierung, Midjourney zu höherem Detailgrad. Die strukturellen Anweisungen sollten modellübergreifend funktionieren.

## Literatur

Bertin, J. (1967). *Sémiologie graphique: Les diagrammes, les réseaux, les cartes*. Paris/La Haye: Mouton & Gauthier-Villars. Englische Übersetzung: *Semiology of Graphics: Diagrams, Networks, Maps*. Madison: University of Wisconsin Press, 1983.

Brehmer, M. & Munzner, T. (2013). A Multi-Level Typology of Abstract Visualization Tasks. *IEEE Transactions on Visualization and Computer Graphics*, 19(12), 2376–2385. [https://doi.org/10.1109/TVCG.2013.124](https://doi.org/10.1109/TVCG.2013.124)

Burkhard, R. A. & Eppler, M. J. (2004). Knowledge Visualization: Towards a New Discipline and its Fields of Application. In: Tochtermann, K. & Maurer, H. (Hrsg.), *Proceedings of I-KNOW '04*. Graz: Know-Center Austria. [https://www.researchgate.net/publication/33682085](https://www.researchgate.net/publication/33682085)

Burke, C. (2009). Isotype: Representing Social Facts Pictorially. *Information Design Journal*, 17(3), 211–223. [https://doi.org/10.1075/idj.17.3.06bur](https://doi.org/10.1075/idj.17.3.06bur)

Kostelnick, C. & Hassett, M. (2003). *Shaping Information: The Rhetoric of Visual Conventions*. Carbondale: Southern Illinois University Press. [https://siupress.siu.edu/books/978-0-8093-8905-6](https://siupress.siu.edu/books/978-0-8093-8905-6)

Munzner, T. (2014). *Visualization Analysis and Design*. Boca Raton: A K Peters/CRC Press. [https://www.cs.ubc.ca/~tmm/vadbook/](https://www.cs.ubc.ca/~tmm/vadbook/)

Neurath, O. (1936). *International Picture Language: The First Rules of Isotype*. London: Kegan Paul, Trench, Trubner & Co. [https://archive.org/details/internationalpic00neur](https://archive.org/details/internationalpic00neur)

Paivio, A. (1971). *Imagery and Verbal Processes*. New York: Holt, Rinehart and Winston. [https://archive.org/details/imageryverbalpro0000paiv](https://archive.org/details/imageryverbalpro0000paiv)

Sweller, J. (1988). Cognitive Load During Problem Solving: Effects on Learning. *Cognitive Science*, 12(2), 257–285. [https://doi.org/10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)

Tufte, E. R. (1983). *The Visual Display of Quantitative Information*. Cheshire: Graphics Press. 2. Auflage 2001. [https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/)

Ware, C. (2012). *Information Visualization: Perception for Design*. 3. Auflage. Burlington: Morgan Kaufmann.

Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4(1), 301–350. [https://doi.org/10.1007/BF00410640](https://doi.org/10.1007/BF00410640)