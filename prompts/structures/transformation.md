# Strukturtyp 5: Transformation / Metamorphose

## Metadaten

- **Typ-ID:** transformation
- **Nummer:** 5
- **Theoretischer Bezug:** Die horizontale Anordnung codiert Zeit, die visuelle Veränderung codiert qualitative Transformation. Abstrakte Metaphern statt biologischer Referenzen gewährleisten domänenunabhängige Anwendbarkeit.

## Wann verwenden

**Geeignet für:**
- Prozesse, bei denen das Ergebnis wesensmäßig anders ist als der Ausgangszustand
- Lernprozesse
- Entwicklungsstufen
- Reifungsprozesse
- Paradigmatische Wechsel
- Erkenntnisprozesse

**Nicht geeignet für:**
- Rein technische Abläufe ohne qualitative Steigerung
- Reversible Prozesse
- Gleichwertige Schritte (→ verwende "sequence")

## Abgrenzung

| Verwechslung mit | Unterscheidungskriterium |
|------------------|--------------------------|
| Sequenz (Stil 1) | Sequenz zeigt gleichwertige Schritte, Transformation zeigt qualitative Veränderung mit Richtung |

**Entscheidungshilfe:** Wenn das Ergebnis einer Phase sich strukturell vom Input unterscheidet, ist Transformation angemessen. Wenn jede Phase eine abgeschlossene Handlung darstellt, die zur nächsten führt, ist Sequenz richtig.

---

## Visuelle Prinzipien

### Grundstruktur
Die Transformation wird durch eine horizontale Abfolge von Stadien dargestellt, jeweils in einer kreisförmigen Vignette, verbunden durch Pfeile.

### Richtungsprinzip
- **Anfangszustand:** Dichter, dunkler, ungeordneter oder verschlossener
- **Zwischenstadien:** Gradueller Übergang, erste Anzeichen der Veränderung
- **Endzustand:** Klarer, heller, strukturierter oder entfaltet

### Farbprogression
Typischerweise von dunklen, kühlen Tönen zu hellen, warmen Tönen. Unterstützt die Richtung der Transformation.

### Wichtig
Die Metapher (Kristallisation, Klärung, Entfaltung) **muss** im Prompt explizit beschrieben werden, sonst fallen Modelle auf biologische Metamorphose (Raupe→Schmetterling) zurück.

---

## Template-Prompt

```
A transformation diagram showing {ANZAHL} stages of qualitative change, arranged horizontally from left to right. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows. {STADIEN_BESCHREIBUNG}. Scientific illustration style with clean rendering, no decorative effects. Solid white background. No text, no labels. 16:9 aspect ratio.
```

### Variablen

| Variable | Beschreibung | Beispielwerte |
|----------|--------------|---------------|
| `ANZAHL` | Anzahl der Stadien | 3, 4, 5 |
| `STADIEN_BESCHREIBUNG` | Detaillierte Beschreibung der visuellen Veränderung | Siehe Metaphern unten |

---

## Visuelle Metaphern

### 1. Kristallisation
**Zeigt:** Ordnungsgewinn, Strukturierung, Systematisierung, Reifung

```
Stage one: a dense cluster of rough, irregular dark gray rock fragments. Stage two: fragments begin to show angular facets, hints of crystalline structure emerge, medium gray-brown tones. Stage three: a more organized crystalline formation, distinct facets visible, warm amber-brown coloration. Stage four: a refined, upward-pointing crystal cluster with clear geometric facets, luminous golden-amber color.
```

**Anwendung:** Theorieentwicklung, Konzeptpräzisierung, Methodenreifung

### 2. Klärung
**Zeigt:** Erkenntnisprozesse, Verständnis, Durchdringung, Abstraktion

```
Stage one: a dense, cloudy, opaque spherical form in dark gray tones. Stage two: the form becomes partially translucent, lighter areas emerge, medium gray-blue tones. Stage three: a clear, transparent, luminous sphere with subtle inner structure visible, pale blue-white coloration.
```

**Anwendung:** Problemlösung, Analyse, Erkenntnisgewinn

### 3. Entfaltung
**Zeigt:** Entwicklung, Wachstum, Ausdifferenzierung

```
Stage one: a compact, tightly folded geometric form in dark teal. Stage two: the form begins to open, revealing inner layers, medium teal. Stage three: partially unfolded with visible internal structure, light teal. Stage four: fully expanded form with complex, differentiated structure, luminous pale teal.
```

**Anwendung:** Projektentwicklung, Ideenreifung, Organisationswachstum

### 4. Verdichtung (umgekehrte Richtung)
**Zeigt:** Fokussierung, Essenz, Reduktion auf das Wesentliche

```
Stage one: scattered, diffuse particles in light gray spread across the vignette. Stage two: particles begin to coalesce, forming loose clusters, medium gray. Stage three: denser aggregation with visible structure emerging, dark gray. Stage four: a compact, solid crystalline core with intense dark color.
```

**Anwendung:** Zusammenfassung, Kernaussagen-Extraktion, Abstraktion

---

## Negative Constraints

Füge diese Einschränkungen zum Prompt hinzu, um unerwünschte Interpretationen zu vermeiden:

```
NEGATIVE CONSTRAINTS:
- No biological metamorphosis (no caterpillars, butterflies, cocoons)
- No human figures or faces
- No literal depictions of objects (books, computers, etc.)
- No arrows within the vignettes (only between them)
- No decorative sparkles, glow effects, or lens flares
- No text, numbers, or labels
```

---

## Anpassungshinweise

### Stadienanzahl
- **3 Stadien:** Einfache Transformationen (Anfang → Mitte → Ende)
- **4 Stadien:** Differenzierte Darstellung mit zwei Zwischenstufen
- **5 Stadien:** Feingliedrige Prozesse mit erkennbaren Zwischenschritten

### Richtungsumkehr
Die Richtung kann umgekehrt werden (von komplex zu einfach, von hell zu dunkel) für:
- Reduktionsprozesse
- Fokussierung
- Abstraktion

### Farbpaletten nach Kontext

| Kontext | Empfohlene Palette |
|---------|-------------------|
| Wissenschaftlich | Grau → Teal → Blau-Weiß |
| Kreativ | Dunkelviolett → Magenta → Gold |
| Technisch | Dunkelblau → Cyan → Weiß |
| Organisch | Braun → Grün → Gold |

---

## Bekannte Probleme

| Problem | Workaround |
|---------|------------|
| Biologische Metamorphose | Explizite Metapher im Prompt benennen (Kristallisation, Klärung) |
| Ungleiche Vignettengrößen | "of equal size" explizit betonen |
| Fehlende Pfeile | "connected by thin gray arrows" verstärken |
| Zu viele Stadien | "Exactly [N] stages, no more, no fewer" verwenden |
| Dekorative Effekte (Gemini) | "no decorative sparkles or glow effects" hinzufügen |

---

## Beispiel-Prompts

### Minimal (3 Stadien, Klärung)
```
A transformation diagram showing 3 stages of qualitative change, arranged horizontally from left to right. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows. Stage one: a dense, cloudy, opaque spherical form in dark gray tones. Stage two: the form becomes partially translucent, lighter areas emerge, medium gray-blue tones. Stage three: a clear, transparent, luminous sphere with subtle inner structure visible, pale blue-white coloration. Scientific illustration style with clean rendering, no decorative effects. Solid white background. No text, no labels. 16:9 aspect ratio.
```

### Erweitert (4 Stadien, Kristallisation, mit Constraints)
```
A transformation diagram showing exactly 4 stages of qualitative change, arranged horizontally from left to right, no more, no fewer. Each stage contained in a subtle circular vignette of equal size, connected by thin gray arrows between each vignette. Stage one: a dense cluster of rough, irregular dark gray rock fragments. Stage two: fragments begin to show angular facets, hints of crystalline structure emerge, medium gray-brown tones. Stage three: a more organized crystalline formation, distinct facets visible, warm amber-brown coloration. Stage four: a refined, upward-pointing crystal cluster with clear geometric facets, luminous golden-amber color. Scientific illustration style with clean rendering. No biological metamorphosis, no butterflies, no decorative sparkles or glow effects, no text, no labels, no numbers. Solid white background. 16:9 aspect ratio.
```

---

## Referenzbilder

Siehe: `assets/style-references/stil-05-transformation/`

- `stil-05-template-gemini.png` - Template-Struktur (Gemini)
- `stil-05-template-openai.png` - Template-Struktur (OpenAI)
- `stil-05-kristallisation-gemini.png` - Kristallisations-Metapher (Gemini)
- `stil-05-kristallisation-openai.png` - Kristallisations-Metapher (OpenAI)
- `stil-05-klaerung-gemini.png` - Klärungs-Metapher (Gemini)
- `stil-05-klaerung-openai.png` - Klärungs-Metapher (OpenAI)
