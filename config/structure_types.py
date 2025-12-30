"""
Strukturtyp-Taxonomie für epistemische Visualisierung.

Diese Taxonomie basiert auf dem Dokument "Zwölf Stile zur Visualisierung von Wissen"
und systematisiert, welche Visualisierungsform für welche Art von Wissen geeignet ist.

Jeder Strukturtyp enthält:
- id: Eindeutige Nummer (1-12)
- name: Deutscher Name
- name_en: Englischer Name für Prompts
- shows: Was der Stil zeigt
- suitable_for: Geeignete Anwendungsfälle
- not_for: Ungeeignete Anwendungsfälle (wichtig für Abgrenzung)
- distinguish_from: Abgrenzungskriterien zu ähnlichen Stilen
- template: Pfad zum Prompt-Template
- reference_images: Pfad zu Beispielbildern
"""

STRUCTURE_TYPES = {
    "sequence": {
        "id": 1,
        "name": "Lineare Phasenfolge",
        "name_en": "Linear Phase Sequence",
        "shows": "Phasen, Schritte, Abfolgen mit gleichwertigen Elementen",
        "suitable_for": [
            "Prozesse mit aufeinanderfolgenden, gleichwertigen Schritten",
            "Workflows",
            "Anleitungen",
            "Phasenmodelle",
            "Verfahrensabläufe"
        ],
        "not_for": [
            "Iterative Prozesse",
            "Rückkopplungen",
            "Parallele Abläufe",
            "Qualitative Transformation",
            "Prozesse mit Steigerungslogik"
        ],
        "distinguish_from": {
            "transformation": "Sequenz zeigt gleichwertige Schritte, Transformation zeigt qualitative Veränderung",
            "spiral": "Sequenz ist einmalig, Spirale zeigt wiederkehrende Phasen"
        },
        "template": "prompts/structures/sequence.md",
        "reference_images": "assets/style-references/stil-01-phasenfolge/"
    },

    "quantity": {
        "id": 2,
        "name": "Piktografischer Mengenvergleich",
        "name_en": "Pictographic Quantity Comparison",
        "shows": "Mengenverhältnisse, Proportionen, Verteilungen",
        "suitable_for": [
            "Illustrative Darstellungen von Proportionen",
            "Größenordnungsvergleiche",
            "Lehrmaterialien",
            "Präsentationen"
        ],
        "not_for": [
            "Präzise numerische Daten",
            "Wissenschaftliche Publikationen mit Datenanspruch"
        ],
        "distinguish_from": {
            "grouping": "Quantity vergleicht Mengen, Grouping zeigt Kategoriezugehörigkeit",
            "scale": "Quantity zeigt Verhältnisse zwischen zählbaren Mengen, Scale zeigt Unzählbares"
        },
        "template": "prompts/structures/quantity.md",
        "reference_images": "assets/style-references/stil-02-mengenvergleich/"
    },

    "hub": {
        "id": 3,
        "name": "Hub-Struktur",
        "name_en": "Hub Structure",
        "shows": "Beziehungen zwischen einem dominanten Zentrum und abhängigen Bereichen",
        "suitable_for": [
            "Strukturen mit Kernbereich und peripheren Elementen",
            "Disziplinen mit Hilfswissenschaften",
            "Organisationen mit Abteilungen",
            "Theorien mit Anwendungsfeldern"
        ],
        "not_for": [
            "Symmetrische Netzwerke ohne klares Zentrum",
            "Strukturen mit mehreren gleichwertigen Zentren",
            "Rein hierarchische Über-/Unterordnungen"
        ],
        "distinguish_from": {
            "network": "Hub hat ein dominantes Zentrum, Network hat kein oder mehrere Zentren",
            "decomposition": "Hub zeigt Beziehungen zwischen eigenständigen Bereichen, Decomposition zeigt Teil-Ganzes"
        },
        "template": "prompts/structures/hub.md",
        "reference_images": "assets/style-references/stil-03-hub/"
    },

    "decomposition": {
        "id": 4,
        "name": "Schematische Komponenten-Dekomposition",
        "name_en": "Component Decomposition",
        "shows": "Aufbau, Komponenten, Teile eines Ganzen",
        "suitable_for": [
            "Systemarchitekturen",
            "Begriffsanalysen",
            "Anatomien",
            "Produktstrukturen"
        ],
        "not_for": [
            "Rangfolgen",
            "Entscheidungsbäume",
            "Zeitliche Entwicklungen",
            "Beziehungen zwischen gleichwertigen Elementen"
        ],
        "distinguish_from": {
            "hub": "Decomposition zeigt Teil-Ganzes-Beziehungen, Hub zeigt assoziierte Bereiche",
            "grouping": "Decomposition: Teile existieren nicht ohne das Ganze, Grouping: Elemente sind unabhängig"
        },
        "template": "prompts/structures/decomposition.md",
        "reference_images": "assets/style-references/stil-04-dekomposition/"
    },

    "transformation": {
        "id": 5,
        "name": "Transformation / Metamorphose",
        "name_en": "Transformation",
        "shows": "Wandlung, Zustandsänderung, qualitative Veränderung",
        "suitable_for": [
            "Prozesse mit wesensmäßiger Veränderung",
            "Lernprozesse",
            "Entwicklungsstufen",
            "Reifungsprozesse",
            "Paradigmatische Wechsel"
        ],
        "not_for": [
            "Rein technische Abläufe ohne qualitative Steigerung",
            "Reversible Prozesse",
            "Gleichwertige Schritte"
        ],
        "distinguish_from": {
            "sequence": "Transformation zeigt qualitative Veränderung mit Richtung, Sequenz zeigt gleichwertige Schritte"
        },
        "visual_metaphors": [
            "Kristallisation (Ordnungsgewinn, Strukturierung)",
            "Klärung (Erkenntnisprozesse, Durchdringung)",
            "Entfaltung (Entwicklung, Wachstum)"
        ],
        "template": "prompts/structures/transformation.md",
        "reference_images": "assets/style-references/stil-05-transformation/"
    },

    "grouping": {
        "id": 6,
        "name": "Gestalt-Gruppierung",
        "name_en": "Gestalt Grouping",
        "shows": "Zugehörigkeit, Cluster, Ähnlichkeitsgruppen, kategoriale Unterscheidungen",
        "suitable_for": [
            "Typologien",
            "Klassifikationen",
            "Segmentierungen",
            "Cluster-Analysen"
        ],
        "not_for": [
            "Hierarchien mit Rangordnung",
            "Sequenzielle Abfolgen",
            "Teil-Ganzes-Beziehungen",
            "Mengenvergleiche mit Präzisionsanspruch"
        ],
        "distinguish_from": {
            "quantity": "Grouping zeigt was zusammengehört, Quantity zeigt wie viel",
            "decomposition": "Grouping: unabhängige Elemente, Decomposition: Teile eines Ganzen",
            "network": "Grouping zeigt Kategoriezugehörigkeit, Network zeigt Relationen"
        },
        "variants": ["proportional", "texture", "swarm", "territorial", "continuity"],
        "template": "prompts/structures/grouping.md",
        "reference_images": "assets/style-references/stil-06-gruppierung/"
    },

    "scale": {
        "id": 7,
        "name": "Skalierung / Anti-Sublim",
        "name_en": "Scale Visualization",
        "shows": "Große Mengen, Masse fassbar gemacht, das Einzelne im Verhältnis zur Masse",
        "suitable_for": [
            "Korpusgrößen",
            "Archivbestände",
            "Historische Zeitspannen",
            "Bevölkerungszahlen",
            "Datenmengen"
        ],
        "not_for": [
            "Präzise Mengenvergleiche",
            "Proportionen zwischen Kategorien",
            "Strukturen innerhalb der Menge"
        ],
        "distinguish_from": {
            "quantity": "Quantity zeigt zählbare Verhältnisse, Scale zeigt das Unzählbare",
            "grouping": "Grouping: Elemente bleiben distinkt, Scale: Elemente werden zur Textur"
        },
        "template": "prompts/structures/scale.md",
        "reference_images": "assets/style-references/stil-07-skalierung/"
    },

    "contrast": {
        "id": 8,
        "name": "Rhetorischer Kontrast",
        "name_en": "Rhetorical Contrast",
        "shows": "Gegensätze, Spannungen, Dualismen, Vorher/Nachher, Dichotomien",
        "suitable_for": [
            "Vergleiche",
            "Vorher/Nachher-Darstellungen",
            "Dichotomien",
            "Spannungsverhältnisse",
            "Konkurrierende Paradigmen"
        ],
        "not_for": [
            "Graduelle Übergänge",
            "Spektren",
            "Kontinua",
            "Mehr als zwei Zustände"
        ],
        "distinguish_from": {
            "quantity": "Contrast zeigt qualitative Gegensätze, Quantity zeigt quantitative Verhältnisse",
            "transformation": "Contrast zeigt gleichzeitige Gegenüberstellung, Transformation zeigt Entwicklung"
        },
        "contrast_dimensions": ["order_chaos", "density_emptiness", "static_dynamic", "homogeneity_heterogeneity"],
        "template": "prompts/structures/contrast.md",
        "reference_images": "assets/style-references/stil-08-kontrast/"
    },

    "stratigraphy": {
        "id": 9,
        "name": "Stratigraphische Zeitschichtung",
        "name_en": "Stratigraphic Layering",
        "shows": "Historische Schichten, Epochen, sedimentierte Zeit, akkumulierte Geschichte",
        "suitable_for": [
            "Historische Epochen",
            "Entwicklungsphasen",
            "Projektgeschichte",
            "Akkumulierte Wissensschichten",
            "Quellenüberlieferung"
        ],
        "not_for": [
            "Zyklische Prozesse",
            "Gleichzeitige Ereignisse",
            "Nicht-chronologische Strukturen"
        ],
        "distinguish_from": {
            "sequence": "Stratigraphy zeigt vertikale Akkumulation, Sequence zeigt horizontale Abfolge",
            "spiral": "Stratigraphy zeigt lineare Akkumulation, Spiral zeigt zyklische Wiederkehr"
        },
        "template": "prompts/structures/stratigraphy.md",
        "reference_images": "assets/style-references/stil-09-schichtung/"
    },

    "spiral": {
        "id": 10,
        "name": "Zyklus-Spirale",
        "name_en": "Spiral Cycle",
        "shows": "Wiederkehrende Prozesse, zyklische Entwicklung, iterative Verfeinerung",
        "suitable_for": [
            "Iterative Forschungsprozesse",
            "Agile Methodologien",
            "Zyklische Entwicklung",
            "Wiederkehrende Evaluationsschleifen",
            "Lernzyklen"
        ],
        "not_for": [
            "Einmalige Sequenzen",
            "Lineare Entwicklungen ohne Wiederkehr",
            "Prozesse ohne erkennbare Phasenstruktur"
        ],
        "distinguish_from": {
            "sequence": "Spiral zeigt wiederkehrende Phasen, Sequence zeigt einmalige Abfolge",
            "stratigraphy": "Spiral zeigt iterierte Phasen, Stratigraphy zeigt akkumulierte Geschichte"
        },
        "template": "prompts/structures/spiral.md",
        "reference_images": "assets/style-references/stil-10-spirale/"
    },

    "network": {
        "id": 11,
        "name": "Netzwerk-Konstellation",
        "name_en": "Network Constellation",
        "shows": "Verbindungen, Beziehungen, Abhängigkeiten, Verflechtungen",
        "suitable_for": [
            "Akteurskonstellationen",
            "Korrespondenznetze",
            "Zitationsnetzwerke",
            "Kooperationsstrukturen",
            "Abhängigkeiten"
        ],
        "not_for": [
            "Hierarchien mit klarer Rangordnung",
            "Zeitliche Abfolgen",
            "Teil-Ganzes-Beziehungen"
        ],
        "distinguish_from": {
            "hub": "Network hat kein oder mehrere Zentren, Hub hat ein dominantes Zentrum",
            "grouping": "Network zeigt Relationen, Grouping zeigt Kategoriezugehörigkeit"
        },
        "template": "prompts/structures/network.md",
        "reference_images": "assets/style-references/stil-11-netzwerk/"
    },

    "uncertainty": {
        "id": 12,
        "name": "Epistemische Unschärfe",
        "name_en": "Epistemic Uncertainty",
        "shows": "Grenzen des Wissens, Hypothetisches, Umstrittenes, Ungewisses",
        "suitable_for": [
            "Hypothetische Zusammenhänge",
            "Umstrittene Kategorisierungen",
            "Grade der Gewissheit",
            "Unscharfe Begriffe",
            "Wissenslücken"
        ],
        "not_for": [
            "Präzise Daten",
            "Eindeutige Kategorien",
            "Fakten ohne Unsicherheit"
        ],
        "distinguish_from": {
            "grouping": "Uncertainty zeigt unscharfe Kategorien mit graduellen Übergängen, Grouping zeigt scharfe Grenzen"
        },
        "visual_techniques": ["soft_edges", "transparency", "opacity_gradients", "dashed_borders"],
        "template": "prompts/structures/uncertainty.md",
        "reference_images": "assets/style-references/stil-12-unschaerfe/"
    }
}


def get_structure_type(type_id: str) -> dict:
    """Gibt einen Strukturtyp anhand seiner ID zurück."""
    return STRUCTURE_TYPES.get(type_id)


def get_all_types() -> list:
    """Gibt alle Strukturtypen als Liste zurück, sortiert nach ID."""
    return sorted(STRUCTURE_TYPES.values(), key=lambda x: x["id"])


def get_type_by_number(number: int) -> dict:
    """Gibt einen Strukturtyp anhand seiner Nummer (1-12) zurück."""
    for type_id, data in STRUCTURE_TYPES.items():
        if data["id"] == number:
            return {"id": type_id, **data}
    return None


def get_distinction_criteria(type_a: str, type_b: str) -> str:
    """Gibt das Abgrenzungskriterium zwischen zwei Typen zurück."""
    type_data = STRUCTURE_TYPES.get(type_a)
    if type_data and "distinguish_from" in type_data:
        return type_data["distinguish_from"].get(type_b, "")
    return ""


def suggest_negative_constraints(type_id: str) -> list:
    """Generiert Negative Constraints basierend auf dem Strukturtyp."""
    type_data = STRUCTURE_TYPES.get(type_id)
    if not type_data:
        return []

    constraints = []

    # Aus "not_for" ableiten
    for item in type_data.get("not_for", []):
        constraints.append(f"NOT: {item}")

    # Aus Abgrenzungskriterien ableiten
    for other_type, criterion in type_data.get("distinguish_from", {}).items():
        # Extrahiere was der andere Typ zeigt
        if "zeigt" in criterion.lower():
            parts = criterion.split(",")
            for part in parts:
                if other_type in part.lower():
                    constraints.append(f"AVOID: {part.strip()}")

    return constraints
