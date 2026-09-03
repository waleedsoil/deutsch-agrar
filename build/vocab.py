# -*- coding: utf-8 -*-
"""
Vocabulary decks. Format per line:  german | english | example sentence (may be empty)
Nouns carry their article and plural. Verbs carry the pattern where it is irregular.
"""

DECKS = {}

DECK_META = {
 "alltag":        ("Everyday life", "Shops, food, weather, transport, time, small talk", "A1"),
 "uni":           ("University", "Courses, exams, admin, supervisors, HiWi work", "A1"),
 "wohnen":        ("Housing", "Room hunting, contracts, bills, bins, flatmates", "A2"),
 "behoerden":     ("Offices & paperwork", "Bürgeramt, insurance, bank, tax, contracts", "A2"),
 "feld":          ("Fieldwork & safety", "Tools, instructions, shifts, protective gear", "A1"),
 "agrar_boden":   ("Soil science", "Horizons, texture, nutrients, sampling, fertility", "A2"),
 "agrar_pflanze": ("Crops & plant production", "Species, growth stages, protection, yield", "A2"),
 "agrar_tier":    ("Livestock", "Species, housing, feed, welfare, performance", "A2"),
 "agrar_technik": ("Machinery & technology", "Tractors, implements, precision farming", "A2"),
 "agrar_oekonomie": ("Farm economics & policy", "Costs, subsidies, regulation, markets", "B1"),
 "wissenschaft":  ("Academic & scientific", "Method, data, statistics, argument, citation", "B1"),
 "bewerbung":     ("Applications & interviews", "CV, cover letter, interview, contract, salary", "B1"),
 "fuehrerschein": ("Driving licence", "Theory exam, road signs, instructor commands", "B1"),
 "verben":        ("Irregular verbs", "The 80 strong verbs that carry everyday German", "A1"),
}

DECKS["alltag"] = """
guten Morgen | good morning | Guten Morgen, haben Sie kurz Zeit?
guten Tag | hello (daytime) | Guten Tag, ich hätte eine Frage.
guten Abend | good evening |
tschüss | bye (informal) |
auf Wiedersehen | goodbye (formal) |
bis morgen | see you tomorrow |
danke schön | thank you |
bitte schön | you're welcome / here you are |
Entschuldigung | excuse me / sorry | Entschuldigung, wo ist der Bahnhof?
Es tut mir leid. | I'm sorry. |
Wie geht es Ihnen? | How are you? (formal) |
der Name (-n) | name | Wie ist Ihr Name, bitte?
der Vorname (-n) | first name |
der Nachname (-n) | surname |
die Adresse (-n) | address |
die Telefonnummer (-n) | phone number |
die E-Mail-Adresse (-n) | email address |
buchstabieren | to spell | Können Sie das bitte buchstabieren?
wiederholen | to repeat | Können Sie das bitte wiederholen?
langsam | slow(ly) | Können Sie bitte langsamer sprechen?
verstehen | to understand | Das habe ich nicht verstanden.
die Sprache (-n) | language |
das Land (Länder) | country |
die Stadt (Städte) | city |
das Dorf (Dörfer) | village |
der Montag | Monday |
der Dienstag | Tuesday |
der Mittwoch | Wednesday |
der Donnerstag | Thursday |
der Freitag | Friday |
der Samstag | Saturday |
der Sonntag | Sunday |
die Woche (-n) | week |
der Monat (-e) | month |
das Jahr (-e) | year |
heute | today |
gestern | yesterday |
morgen | tomorrow |
übermorgen | the day after tomorrow |
vorgestern | the day before yesterday |
jetzt | now |
später | later |
früh | early |
spät | late |
immer | always |
oft | often |
manchmal | sometimes |
selten | rarely |
nie | never |
die Uhr (-en) | clock, o'clock | Es ist zehn Uhr.
die Uhrzeit (-en) | time of day |
die Stunde (-n) | hour |
die Minute (-n) | minute |
halb | half | Es ist halb drei. (= 14:30)
Viertel nach | quarter past |
Viertel vor | quarter to |
das Frühstück | breakfast |
das Mittagessen | lunch |
das Abendessen | dinner |
das Brot (-e) | bread |
das Brötchen (-) | bread roll |
die Milch | milk |
der Käse | cheese |
das Ei (-er) | egg |
das Fleisch | meat |
das Gemüse | vegetables |
das Obst | fruit |
der Apfel (Äpfel) | apple |
die Kartoffel (-n) | potato |
die Zwiebel (-n) | onion |
der Reis | rice |
das Mehl | flour |
der Zucker | sugar |
das Salz | salt |
der Pfeffer | pepper |
das Öl (-e) | oil |
das Wasser | water |
der Tee | tea |
der Kaffee | coffee |
einkaufen | to shop | Ich gehe am Samstag einkaufen.
kosten | to cost | Was kostet ein Kilo Äpfel?
bezahlen | to pay | Kann ich mit Karte bezahlen?
die Kasse (-n) | checkout, till |
das Kleingeld | small change |
die Quittung (-en) | receipt |
das Angebot (-e) | special offer |
das Kilo (-) | kilogram |
das Gramm (-) | gram |
der Liter (-) | litre |
die Packung (-en) | packet |
das Stück (-e) | piece |
das Wetter | weather | Wie ist das Wetter heute?
die Sonne | sun |
der Regen | rain |
der Schnee | snow |
der Wind (-e) | wind |
der Nebel | fog |
die Wolke (-n) | cloud |
warm | warm |
kalt | cold |
heiß | hot |
kühl | cool |
trocken | dry |
nass | wet |
feucht | moist, humid |
der Grad (-) | degree | Heute sind es zwölf Grad.
der Bahnhof (Bahnhöfe) | train station |
die Haltestelle (-n) | bus/tram stop |
der Zug (Züge) | train |
der Bus (-se) | bus |
das Fahrrad (Fahrräder) | bicycle |
die Fahrkarte (-n) | ticket |
die Verspätung (-en) | delay | Der Zug hat 20 Minuten Verspätung.
umsteigen | to change (trains) | In Kassel müssen Sie umsteigen.
abfahren | to depart |
ankommen | to arrive |
der Arzt (Ärzte) | doctor |
der Termin (-e) | appointment | Ich möchte einen Termin vereinbaren.
die Apotheke (-n) | pharmacy |
das Rezept (-e) | prescription; recipe |
krank | ill |
müde | tired |
der Kopf (Köpfe) | head |
der Rücken (-) | back |
die Hand (Hände) | hand |
der Fuß (Füße) | foot |
weh tun | to hurt | Mein Rücken tut weh.
die Freizeit | free time |
das Wochenende (-n) | weekend |
der Urlaub (-e) | holiday, leave |
der Freund (-e) | friend (m) |
die Freundin (-nen) | friend (f) |
zusammen | together |
allein | alone |
gern | gladly, to like doing | Ich koche gern.
lieber | preferably | Ich trinke lieber Tee.
vielleicht | maybe |
natürlich | of course |
klar | sure, clear |
genau | exactly |
schon | already |
noch | still, yet |
erst | only, not until |
schon mal | ever, before |
"""

DECKS["uni"] = """
die Universität (-en) | university |
die Hochschule (-n) | higher-education institution |
der Studiengang (Studiengänge) | degree programme | Mein Studiengang heißt Nachhaltige Internationale Landwirtschaft.
das Semester (-) | semester | Ich bin im dritten Semester.
das Wintersemester (-) | winter semester |
das Sommersemester (-) | summer semester |
die Vorlesung (-en) | lecture | Die Vorlesung fängt um acht Uhr an.
das Seminar (-e) | seminar |
die Übung (-en) | tutorial, exercise class |
das Praktikum (Praktika) | lab course; internship |
die Exkursion (-en) | field trip | Am Freitag machen wir eine Exkursion zum Versuchsgut.
der Hörsaal (Hörsäle) | lecture hall |
das Labor (-e/-s) | laboratory |
die Bibliothek (-en) | library |
die Mensa (Mensen) | canteen |
das Modul (-e) | module |
das Modulhandbuch (Modulhandbücher) | module handbook |
die Prüfungsordnung (-en) | examination regulations |
der Leistungspunkt (-e) | credit point |
die Prüfung (-en) | exam |
die Klausur (-en) | written exam |
die mündliche Prüfung | oral exam |
die Hausarbeit (-en) | term paper |
das Referat (-e) | oral presentation |
die Abgabefrist (-en) | submission deadline | Die Abgabefrist ist der 15. März.
die Note (-n) | grade | Ich habe eine gute Note bekommen.
bestehen | to pass | Ich habe die Klausur bestanden.
durchfallen | to fail |
die Anmeldung (-en) | registration |
sich anmelden | to register | Ich habe mich für die Prüfung angemeldet.
sich abmelden | to deregister |
die Immatrikulation (-en) | enrolment |
die Rückmeldung (-en) | semester re-registration |
der Semesterbeitrag (Semesterbeiträge) | semester fee |
das Prüfungsamt (Prüfungsämter) | examination office |
die Sprechstunde (-n) | office hour | Ich gehe in die Sprechstunde von Frau Professor Weber.
der Betreuer (-) | supervisor (m) |
die Betreuerin (-nen) | supervisor (f) |
der Professor (-en) | professor (m) |
die Professorin (-nen) | professor (f) |
die wissenschaftliche Hilfskraft | student research assistant (HiWi) | Ich arbeite als wissenschaftliche Hilfskraft am Institut.
der Lehrstuhl (Lehrstühle) | chair, professorship |
das Institut (-e) | institute |
die Fakultät (-en) | faculty |
die Masterarbeit (-en) | master's thesis |
die Bachelorarbeit (-en) | bachelor's thesis |
das Thema (Themen) | topic |
die Gliederung (-en) | outline, structure |
das Zeugnis (-se) | certificate, transcript |
die Anerkennung (-en) | recognition of credits |
das Stipendium (Stipendien) | scholarship |
die Studienbescheinigung (-en) | enrolment certificate |
der Studienausweis (-e) | student ID |
der Stundenplan (Stundenpläne) | timetable |
das Vorlesungsverzeichnis (-se) | course catalogue |
die Anwesenheitspflicht | compulsory attendance |
die Gruppenarbeit (-en) | group work |
die Literaturliste (-n) | reading list |
das Skript (-e) | lecture notes |
die Folie (-n) | slide |
die Frist (-en) | deadline |
verlängern | to extend | Kann ich die Frist verlängern?
"""

DECKS["wohnen"] = """
die Wohnung (-en) | flat, apartment |
das Zimmer (-) | room |
die Wohngemeinschaft (-en) | shared flat (WG) | Ich suche ein Zimmer in einer WG.
der Mitbewohner (-) | flatmate (m) |
die Mitbewohnerin (-nen) | flatmate (f) |
das Wohnheim (-e) | hall of residence |
die Küche (-n) | kitchen |
das Bad (Bäder) | bathroom |
der Flur (-e) | hallway |
der Keller (-) | cellar |
der Balkon (-e/-s) | balcony |
möbliert | furnished |
die Besichtigung (-en) | viewing | Wann ist die Besichtigung?
der Mietvertrag (Mietverträge) | tenancy agreement |
die Miete (-n) | rent |
die Kaltmiete | rent excluding bills |
die Warmmiete | rent including bills |
die Nebenkosten (Pl.) | utility costs |
die Kaution (-en) | deposit |
der Vermieter (-) | landlord |
der Mieter (-) | tenant |
kündigen | to terminate (a contract) | Ich muss den Vertrag drei Monate vorher kündigen.
die Heizung (-en) | heating |
der Strom | electricity |
der Stromzähler (-) | electricity meter |
das Internet | internet |
die Waschmaschine (-n) | washing machine |
der Müll | waste |
die Mülltrennung | waste separation |
der Restmüll | residual waste |
das Altpapier | waste paper |
der Biomüll | organic waste |
der Gelbe Sack | yellow recycling bag |
das Pfand | deposit on bottles |
der Hausmeister (-) | caretaker |
die Hausordnung (-en) | house rules |
die Ruhezeit (-en) | quiet hours |
die Wohnungsgeberbestätigung (-en) | landlord confirmation for registration |
"""

DECKS["behoerden"] = """
das Bürgeramt (Bürgerämter) | citizens' registration office |
die Anmeldung (-en) | registration of residence | Ich muss mich innerhalb von zwei Wochen anmelden.
die Ummeldung (-en) | change-of-address registration |
die Meldebescheinigung (-en) | registration certificate |
die Ausländerbehörde (-n) | foreigners' authority |
der Aufenthaltstitel (-) | residence permit |
die Verlängerung (-en) | extension |
der Antrag (Anträge) | application, formal request | Ich habe den Antrag online gestellt.
einen Antrag stellen | to submit an application |
der Bescheid (-e) | official decision, notice |
die Frist (-en) | deadline |
der Nachweis (-e) | proof, evidence |
die Bescheinigung (-en) | certificate, confirmation |
das Formular (-e) | form |
ausfüllen | to fill in | Bitte füllen Sie das Formular vollständig aus.
die Unterschrift (-en) | signature |
unterschreiben | to sign |
der Personalausweis (-e) | ID card |
der Reisepass (Reisepässe) | passport |
die Krankenkasse (-n) | health insurance fund |
die Versicherung (-en) | insurance |
der Beitrag (Beiträge) | contribution, fee |
die Haftpflichtversicherung (-en) | liability insurance |
die Selbstbeteiligung (-en) | excess, deductible |
die Steuer (-n) | tax |
die Steuererklärung (-en) | tax return |
die Steueridentifikationsnummer (-n) | tax ID number |
das Finanzamt (Finanzämter) | tax office |
das Konto (Konten) | bank account |
die Überweisung (-en) | bank transfer |
der Dauerauftrag (Daueraufträge) | standing order |
die Lastschrift (-en) | direct debit |
der Kontoauszug (Kontoauszüge) | bank statement |
die Rechnung (-en) | invoice |
die Mahnung (-en) | payment reminder |
der Beleg (-e) | receipt, voucher |
der Rundfunkbeitrag | broadcasting fee |
der Widerspruch (Widersprüche) | formal objection |
die Kündigung (-en) | termination, notice |
die Vollmacht (-en) | power of attorney |
beglaubigt | certified (copy) |
zuständig | responsible, in charge | Wer ist dafür zuständig?
die Öffnungszeit (-en) | opening hours |
die Wartenummer (-n) | queue number |
der Schalter (-) | counter, service desk |
"""

DECKS["feld"] = """
das Feld (-er) | field |
der Acker (Äcker) | arable field |
die Parzelle (-n) | plot | Jede Parzelle ist zehn Quadratmeter groß.
die Schaufel (-n) | shovel |
der Spaten (-) | spade |
die Hacke (-n) | hoe |
der Rechen (-) | rake |
die Schubkarre (-n) | wheelbarrow |
der Eimer (-) | bucket |
die Kiste (-n) | crate, box |
die Palette (-n) | pallet |
der Sack (Säcke) | sack, bag |
die Tüte (-n) | bag |
das Etikett (-en) | label |
der Handschuh (-e) | glove |
die Schutzbrille (-n) | safety goggles |
der Gehörschutz | hearing protection |
die Warnweste (-n) | high-visibility vest |
der Sicherheitsschuh (-e) | safety boot |
der Helm (-e) | helmet |
der Arbeitsschutz | occupational safety |
die Unterweisung (-en) | safety briefing | Vor dem ersten Arbeitstag gibt es eine Unterweisung.
die Betriebsanweisung (-en) | operating instruction |
die Gefahr (-en) | danger |
gefährlich | dangerous |
Vorsicht! | Careful! |
Achtung! | Attention! |
der Unfall (Unfälle) | accident |
die Erste Hilfe | first aid |
der Verbandkasten (Verbandkästen) | first-aid kit |
der Feuerlöscher (-) | fire extinguisher |
der Notausgang (Notausgänge) | emergency exit |
die Schicht (-en) | shift | Ich habe morgen Frühschicht.
die Frühschicht (-en) | early shift |
die Spätschicht (-en) | late shift |
die Pause (-n) | break |
der Feierabend | end of the working day |
die Überstunde (-n) | overtime hour |
die Arbeitszeit (-en) | working hours |
der Stundenlohn (Stundenlöhne) | hourly wage |
der Vorarbeiter (-) | foreman |
heben | to lift | Heben Sie schwere Kisten immer aus den Beinen.
tragen | to carry |
ziehen | to pull |
schieben | to push |
stapeln | to stack |
sortieren | to sort |
wiegen | to weigh | Wiegen Sie die Probe bitte auf zwei Stellen genau.
messen | to measure |
markieren | to mark |
notieren | to note down |
aufräumen | to tidy up |
reinigen | to clean |
befüllen | to fill |
entleeren | to empty |
abstellen | to put down, park |
anfassen | to touch |
"""

DECKS["agrar_boden"] = """
der Boden (Böden) | soil |
die Bodenkunde | soil science |
die Bodenprobe (-n) | soil sample | Wir haben 120 Bodenproben genommen.
die Probenahme (-n) | sampling |
der Bohrstock (Bohrstöcke) | soil auger, probe |
das Bodenprofil (-e) | soil profile |
der Bodenhorizont (-e) | soil horizon |
der Oberboden | topsoil |
der Unterboden | subsoil |
die Krume (-n) | plough layer, topsoil |
die Bodenart (-en) | soil texture class |
der Ton | clay |
der Schluff | silt |
der Sand | sand |
der Lehm | loam |
der Humus | humus |
die organische Substanz | organic matter |
der Kohlenstoff | carbon |
der Humusgehalt | humus content |
die Bodenstruktur (-en) | soil structure |
das Aggregat (-e) | soil aggregate |
die Lagerungsdichte (-n) | bulk density |
die Porosität | porosity |
die Bodenverdichtung (-en) | soil compaction | Bei nassem Boden droht Bodenverdichtung.
die Verschlämmung | surface sealing, capping |
die Erosion | erosion |
die Bodenfruchtbarkeit | soil fertility |
der pH-Wert (-e) | pH value |
die Kalkung (-en) | liming |
die Kationenaustauschkapazität | cation exchange capacity |
der Nährstoff (-e) | nutrient |
der Stickstoff | nitrogen |
der Phosphor | phosphorus |
das Kalium | potassium |
das Magnesium | magnesium |
der Schwefel | sulphur |
das Spurenelement (-e) | trace element |
die Nährstoffversorgung | nutrient supply |
die Düngung (-en) | fertilisation |
der Dünger (-) | fertiliser |
der Mineraldünger (-) | mineral fertiliser |
der Wirtschaftsdünger (-) | farmyard/organic fertiliser |
die Gülle | liquid manure, slurry |
der Stallmist | farmyard manure |
der Kompost (-e) | compost |
die Düngebedarfsermittlung (-en) | fertiliser requirement calculation |
die Nährstoffbilanz (-en) | nutrient balance |
die Auswaschung (-en) | leaching |
die Nitratauswaschung | nitrate leaching |
die Mineralisierung | mineralisation |
die Wasserhaltefähigkeit | water-holding capacity |
die Feldkapazität | field capacity |
der Welkepunkt (-e) | wilting point |
die Infiltration | infiltration |
der Wassergehalt (-e) | water content |
die Trockenmasse | dry matter |
das Sieb (-e) | sieve |
sieben | to sieve |
trocknen | to dry | Die Proben werden bei 105 °C getrocknet.
das Bodenleben | soil biota |
der Regenwurm (Regenwürmer) | earthworm |
die Mykorrhiza | mycorrhiza |
die Bodenprobenmischung (-en) | composite sample |
"""

DECKS["agrar_pflanze"] = """
die Pflanze (-n) | plant |
der Pflanzenbau | crop production |
der Ackerbau | arable farming |
der Anbau | cultivation |
anbauen | to grow, cultivate | In Indien baut man viel Hirse an.
die Kultur (-en) | crop |
das Getreide | cereals |
der Weizen | wheat |
der Winterweizen | winter wheat | Winterweizen wird im Oktober gesät.
die Gerste | barley |
der Roggen | rye |
der Hafer | oats |
der Mais | maize |
der Raps | oilseed rape |
die Kartoffel (-n) | potato |
die Zuckerrübe (-n) | sugar beet |
die Sonnenblume (-n) | sunflower |
die Sojabohne (-n) | soybean |
die Ackerbohne (-n) | faba bean |
die Erbse (-n) | pea |
die Hülsenfrucht (Hülsenfrüchte) | legume |
der Klee | clover |
die Luzerne | alfalfa |
das Grünland | grassland |
die Hirse | millet |
der Reis | rice |
die Baumwolle | cotton |
das Zuckerrohr | sugarcane |
die Sorte (-n) | variety, cultivar |
die Sortenprüfung (-en) | variety trial |
die Züchtung (-en) | breeding |
das Saatgut | seed |
die Aussaat (-en) | sowing |
säen | to sow |
die Saatstärke (-n) | seed rate |
die Keimung | germination |
die Keimfähigkeit | germination capacity |
der Keimling (-e) | seedling |
auflaufen | to emerge | Der Bestand ist gleichmäßig aufgelaufen.
der Bestand (Bestände) | crop stand |
die Bestandesdichte (-n) | plant density |
die Bestockung | tillering |
das Schossen | stem elongation |
die Blüte (-n) | flowering; blossom |
die Ähre (-n) | ear (of cereal) |
das Korn (Körner) | grain, kernel |
die Reife | ripeness, maturity |
die Ernte (-n) | harvest |
ernten | to harvest |
der Ertrag (Erträge) | yield | Der Ertrag lag bei 8 Tonnen pro Hektar.
der Kornertrag | grain yield |
die Qualität (-en) | quality |
der Proteingehalt | protein content |
die Fruchtfolge (-n) | crop rotation |
die Zwischenfrucht (Zwischenfrüchte) | catch crop, cover crop |
die Hauptfrucht (Hauptfrüchte) | main crop |
die Untersaat (-en) | undersowing |
die Gründüngung | green manuring |
die Brache (-n) | fallow |
die Wurzel (-n) | root |
das Blatt (Blätter) | leaf |
der Halm (-e) | stalk, culm |
der Trieb (-e) | shoot |
die Knolle (-n) | tuber |
die Photosynthese | photosynthesis |
die Bewässerung | irrigation |
bewässern | to irrigate |
der Wasserbedarf | water requirement |
die Trockenheit | drought, dryness |
die Dürre (-n) | severe drought |
der Niederschlag (Niederschläge) | precipitation |
der Frost (Fröste) | frost |
der Hagel | hail |
die Vegetationsperiode (-n) | growing season |
das Unkraut (Unkräuter) | weed |
der Schädling (-e) | pest |
die Krankheit (-en) | disease |
der Pilz (-e) | fungus |
der Mehltau | mildew |
der Rost | rust (disease) |
die Blattlaus (Blattläuse) | aphid |
der Befall | infestation |
die Schadschwelle (-n) | economic threshold |
der Pflanzenschutz | crop protection |
das Pflanzenschutzmittel (-) | plant protection product |
das Herbizid (-e) | herbicide |
das Fungizid (-e) | fungicide |
das Insektizid (-e) | insecticide |
die Zulassung (-en) | approval, authorisation |
die Wartezeit (-en) | pre-harvest interval |
die Resistenz (-en) | resistance |
die Beizung | seed dressing |
ausbringen | to apply, spread | Das Mittel darf nicht bei Wind ausgebracht werden.
"""

DECKS["agrar_tier"] = """
das Rind (-er) | cattle |
die Kuh (Kühe) | cow |
die Milchkuh (Milchkühe) | dairy cow |
das Kalb (Kälber) | calf |
das Schwein (-e) | pig |
die Sau (Säue) | sow |
das Schaf (-e) | sheep |
die Ziege (-n) | goat |
das Huhn (Hühner) | chicken |
das Geflügel | poultry |
die Legehenne (-n) | laying hen |
das Vieh | livestock |
die Herde (-n) | herd |
die Tierhaltung | animal husbandry |
der Stall (Ställe) | barn, stable |
die Bucht (-en) | pen |
die Einstreu | bedding |
die Weide (-n) | pasture |
die Beweidung | grazing |
weiden | to graze |
das Futter | feed |
das Futtermittel (-) | feedstuff |
das Grundfutter | roughage |
das Kraftfutter | concentrate feed |
die Silage (-n) | silage |
das Heu | hay |
das Stroh | straw |
die Ration (-en) | ration |
die Fütterung | feeding |
die Tränke (-n) | drinker, water trough |
die Milchleistung (-en) | milk yield |
die Mast | fattening |
die Zunahme (-n) | weight gain |
die Zucht (-en) | breeding |
die Besamung (-en) | insemination |
der Tierarzt (Tierärzte) | veterinarian |
die Tiergesundheit | animal health |
der Tierschutz | animal welfare |
die Besatzdichte (-n) | stocking density |
der Melkstand (Melkstände) | milking parlour |
der Melkroboter (-) | milking robot |
die Klaue (-n) | hoof, claw |
die Impfung (-en) | vaccination |
"""

DECKS["agrar_technik"] = """
der Traktor (-en) | tractor |
der Schlepper (-) | tractor (colloquial) |
der Mähdrescher (-) | combine harvester |
die Sämaschine (-n) | seed drill |
die Drillmaschine (-n) | seed drill |
der Pflug (Pflüge) | plough |
pflügen | to plough |
der Grubber (-) | cultivator |
die Egge (-n) | harrow |
die Kreiselegge (-n) | power harrow |
die Bodenbearbeitung | soil tillage |
die Feldspritze (-n) | field sprayer |
der Düngerstreuer (-) | fertiliser spreader |
der Anhänger (-) | trailer |
die Zapfwelle (-n) | power take-off (PTO) |
der Frontlader (-) | front loader |
die Ballenpresse (-n) | baler |
der Ballen (-) | bale |
das Mähwerk (-e) | mower |
der Häcksler (-) | forage harvester |
die Arbeitsbreite (-n) | working width |
die Fahrgasse (-n) | tramline |
der Reifendruck | tyre pressure |
der Kraftstoff (-e) | fuel |
der Diesel | diesel |
die Wartung (-en) | maintenance |
die Reparatur (-en) | repair |
das Ersatzteil (-e) | spare part |
die Betriebsstunde (-n) | operating hour |
die Präzisionslandwirtschaft | precision agriculture |
das Lenksystem (-e) | guidance system |
die Drohne (-n) | drone |
der Sensor (-en) | sensor |
die Fernerkundung | remote sensing |
die Satellitenaufnahme (-n) | satellite image |
die Applikationskarte (-n) | application map |
die Ertragskartierung | yield mapping |
die Schlagkartei (-en) | field record book |
das Gewächshaus (Gewächshäuser) | greenhouse |
die Klimakammer (-n) | climate chamber |
die Waage (-n) | scale, balance |
das Messgerät (-e) | measuring device |
kalibrieren | to calibrate |
einstellen | to adjust, set | Stellen Sie die Sämaschine auf 350 Körner pro Quadratmeter ein.
"""

DECKS["agrar_oekonomie"] = """
der Betrieb (-e) | farm, business |
der Landwirt (-e) | farmer (m) |
die Landwirtin (-nen) | farmer (f) |
der Betriebsleiter (-) | farm manager |
die Fläche (-n) | area, land |
der Hektar (-) | hectare |
die Pacht (-en) | lease, tenancy |
pachten | to lease (land) |
der Pachtpreis (-e) | rental price for land |
der Schlag (Schläge) | field parcel |
die Direktzahlung (-en) | direct payment |
die Gemeinsame Agrarpolitik | Common Agricultural Policy |
die Förderung (-en) | subsidy, funding |
der Antrag (Anträge) | application |
die Auflage (-n) | condition, requirement |
die Düngeverordnung | fertiliser ordinance |
das rote Gebiet (-e) | nitrate-vulnerable zone |
die Verordnung (-en) | regulation, ordinance |
das Gesetz (-e) | law |
die Vorschrift (-en) | rule, regulation |
die Nachhaltigkeit | sustainability |
nachhaltig | sustainable |
der Ökolandbau | organic farming |
die Umstellung (-en) | conversion (to organic) |
die Zertifizierung (-en) | certification |
die Wertschöpfungskette (-n) | value chain |
die Vermarktung | marketing |
der Markt (Märkte) | market |
das Angebot (-e) | supply, offer |
die Nachfrage | demand |
der Preis (-e) | price |
die Kosten (Pl.) | costs |
der Erlös (-e) | revenue |
der Umsatz (Umsätze) | turnover |
der Gewinn (-e) | profit |
der Verlust (-e) | loss |
der Deckungsbeitrag (Deckungsbeiträge) | gross margin |
die Rentabilität | profitability |
die Investition (-en) | investment |
der Kredit (-e) | loan |
die Genossenschaft (-en) | cooperative |
die Bilanz (-en) | balance sheet |
die Wirtschaftlichkeit | economic efficiency |
der Klimawandel | climate change |
die Anpassung (-en) | adaptation |
die Emission (-en) | emission |
die Biodiversität | biodiversity |
die Ernährungssicherheit | food security |
der Verbraucher (-) | consumer |
"""

DECKS["wissenschaft"] = """
die Forschung (-en) | research |
die Untersuchung (-en) | investigation, study |
der Versuch (-e) | experiment, trial |
das Experiment (-e) | experiment |
der Feldversuch (-e) | field trial |
der Gefäßversuch (-e) | pot experiment |
die Hypothese (-n) | hypothesis |
die Fragestellung (-en) | research question |
das Ziel (-e) | objective |
die Methode (-n) | method |
das Versuchsdesign (-s) | experimental design |
die Wiederholung (-en) | replicate |
die Variante (-n) | treatment |
die Kontrolle (-n) | control |
die Stichprobe (-n) | sample |
der Standort (-e) | site, location |
die Erhebung (-en) | data collection |
erheben | to collect (data) |
die Messung (-en) | measurement |
der Messwert (-e) | measured value |
die Daten (Pl.) | data |
die Auswertung (-en) | analysis, evaluation |
auswerten | to analyse | Die Daten wurden mit R ausgewertet.
die Statistik (-en) | statistics |
der Mittelwert (-e) | mean |
der Median (-e) | median |
die Standardabweichung (-en) | standard deviation |
die Streuung (-en) | dispersion, variance |
die Signifikanz | significance |
signifikant | significant |
der Zusammenhang (Zusammenhänge) | relationship, connection |
die Korrelation (-en) | correlation |
die Ursache (-n) | cause |
die Wirkung (-en) | effect |
der Einfluss (Einflüsse) | influence |
das Ergebnis (-se) | result |
die Schlussfolgerung (-en) | conclusion |
die Diskussion (-en) | discussion |
die Zusammenfassung (-en) | summary |
die Literatur | literature |
die Quelle (-n) | source |
zitieren | to cite | Nach Müller (2023) steigt der Ertrag deutlich.
die Abbildung (-en) | figure |
die Tabelle (-n) | table |
die Grafik (-en) | chart, graph |
die Achse (-n) | axis |
der Anteil (-e) | share, proportion |
der Durchschnitt (-e) | average |
die Zunahme (-n) | increase |
die Abnahme (-n) | decrease |
die Schwankung (-en) | fluctuation |
der Trend (-s) | trend |
steigen | to rise | Der Ertrag ist um 15 Prozent gestiegen.
sinken | to fall |
zunehmen | to increase |
abnehmen | to decrease |
schwanken | to fluctuate |
untersuchen | to investigate |
ermitteln | to determine |
erfassen | to record, capture |
darstellen | to present, depict |
feststellen | to ascertain |
vergleichen | to compare |
überprüfen | to verify |
zurückführen auf | to attribute to | Der Rückgang ist auf die Trockenheit zurückzuführen.
hervorgehen aus | to emerge from |
annehmen | to assume |
vermuten | to presume |
vermutlich | presumably |
offenbar | apparently |
tendenziell | tending to |
weitgehend | largely |
in der Regel | as a rule |
"""

DECKS["bewerbung"] = """
die Bewerbung (-en) | application |
sich bewerben um | to apply for | Ich bewerbe mich um die Stelle als Versuchstechniker.
die Stellenanzeige (-n) | job advert |
die Stelle (-n) | position, job |
die Position (-en) | position |
das Anschreiben (-) | cover letter |
der Lebenslauf (Lebensläufe) | CV |
der Werdegang (Werdegänge) | career path |
das Zeugnis (-se) | reference, certificate |
das Arbeitszeugnis (-se) | employment reference |
die Urkunde (-n) | diploma, certificate |
die Anlage (-n) | attachment, enclosure |
der Arbeitgeber (-) | employer |
der Arbeitnehmer (-) | employee |
die Personalabteilung (-en) | HR department |
das Vorstellungsgespräch (-e) | job interview | Ich wurde zu einem Vorstellungsgespräch eingeladen.
die Einladung (-en) | invitation |
die Zusage (-n) | acceptance, offer |
die Absage (-n) | rejection |
die Berufserfahrung (-en) | professional experience |
die Qualifikation (-en) | qualification |
die Kenntnisse (Pl.) | knowledge, skills |
die Fähigkeit (-en) | ability |
die Stärke (-n) | strength |
die Schwäche (-n) | weakness |
die Teamfähigkeit | ability to work in a team |
die Belastbarkeit | resilience under pressure |
die Eigeninitiative | initiative |
die Zuverlässigkeit | reliability |
die Sorgfalt | thoroughness, care |
die Motivation | motivation |
die Herausforderung (-en) | challenge |
die Verantwortung (-en) | responsibility |
zuständig sein für | to be responsible for |
die Aufgabe (-n) | task |
das Aufgabengebiet (-e) | area of responsibility |
die Einarbeitung | onboarding, training-in |
die Weiterbildung (-en) | further training |
das Gehalt (Gehälter) | salary |
die Gehaltsvorstellung (-en) | salary expectation | Meine Gehaltsvorstellung liegt bei 45.000 Euro brutto im Jahr.
das Bruttojahresgehalt | gross annual salary |
brutto | gross |
netto | net |
der Arbeitsvertrag (Arbeitsverträge) | employment contract |
die Probezeit (-en) | probation period |
die Kündigungsfrist (-en) | notice period |
die Befristung (-en) | fixed-term limitation |
unbefristet | permanent |
der Urlaubsanspruch (Urlaubsansprüche) | holiday entitlement |
die Vollzeit | full-time |
die Teilzeit | part-time |
der Tarifvertrag (Tarifverträge) | collective agreement |
die Betriebszugehörigkeit | length of service |
die Rückfrage (-n) | follow-up question |
sich vorstellen | to introduce oneself |
die Selbstpräsentation (-en) | self-presentation |
der Schwerpunkt (-e) | focus, specialisation |
"""

DECKS["fuehrerschein"] = """
der Führerschein (-e) | driving licence |
die Fahrschule (-n) | driving school |
der Fahrlehrer (-) | driving instructor |
die Fahrstunde (-n) | driving lesson |
die Theorieprüfung (-en) | theory test |
die praktische Prüfung (-en) | practical test |
der Sehtest (-s) | eyesight test |
der Erste-Hilfe-Kurs (-e) | first-aid course |
die Führerscheinstelle (-n) | driving licence authority |
die Klasse B | category B (car) |
die Klasse T | category T (agricultural tractor) |
das Fahrzeug (-e) | vehicle |
der Fahrzeugschein (-e) | vehicle registration document |
die Hauptuntersuchung (-en) | roadworthiness inspection (TÜV) |
die Zulassung (-en) | vehicle registration |
die Anhängelast (-en) | permitted trailer load |
die Vorfahrt | right of way | An dieser Kreuzung gilt rechts vor links.
die Vorfahrtsstraße (-n) | priority road |
das Verkehrszeichen (-) | road sign |
das Gefahrzeichen (-) | warning sign |
das Vorschriftzeichen (-) | regulatory sign |
das Richtzeichen (-) | informative sign |
die Ampel (-n) | traffic light |
die Kreuzung (-en) | junction, crossroads |
der Kreisverkehr (-e) | roundabout |
die Einbahnstraße (-n) | one-way street |
die Autobahn (-en) | motorway |
die Landstraße (-n) | country road |
die Ortschaft (-en) | built-up area |
die Geschwindigkeitsbegrenzung (-en) | speed limit |
die Höchstgeschwindigkeit (-en) | maximum speed |
der Sicherheitsabstand (Sicherheitsabstände) | safe following distance |
der Bremsweg (-e) | braking distance |
der Anhalteweg (-e) | total stopping distance |
die Reaktionszeit (-en) | reaction time |
überholen | to overtake |
abbiegen | to turn (off) |
blinken | to indicate |
der Schulterblick (-e) | shoulder check |
der tote Winkel | blind spot |
sich einordnen | to get into lane |
anfahren | to pull away |
einparken | to park |
der Rückwärtsgang | reverse gear |
die Kupplung (-en) | clutch |
die Bremse (-n) | brake |
das Gaspedal (-e) | accelerator |
der Sicherheitsgurt (-e) | seat belt |
der Airbag (-s) | airbag |
die Warnblinkanlage (-n) | hazard lights |
das Warndreieck (-e) | warning triangle |
die Promillegrenze (-n) | blood alcohol limit |
der Bußgeldkatalog | schedule of fines |
das Reißverschlussverfahren | zip merge |
die Haltelinie (-n) | stop line |
das Halteverbot | no-stopping zone |
der Fußgängerüberweg (-e) | pedestrian crossing |
die Rettungsgasse (-n) | emergency corridor |
das Rettungsfahrzeug (-e) | emergency vehicle |
Wie verhalten Sie sich? | How do you behave (in this situation)? |
Womit müssen Sie rechnen? | What must you expect? |
Was ist zu beachten? | What must be observed? |
"""

DECKS["verben"] = """
sein – war – ist gewesen | to be |
haben – hatte – hat gehabt | to have |
werden – wurde – ist geworden | to become |
gehen – ging – ist gegangen | to go |
kommen – kam – ist gekommen | to come |
fahren – fuhr – ist gefahren | to drive, travel |
laufen – lief – ist gelaufen | to run, walk |
fliegen – flog – ist geflogen | to fly |
bleiben – blieb – ist geblieben | to stay |
stehen – stand – hat gestanden | to stand |
liegen – lag – hat gelegen | to lie |
sitzen – saß – hat gesessen | to sit |
sehen – sah – hat gesehen | to see |
lesen – las – hat gelesen | to read |
schreiben – schrieb – hat geschrieben | to write |
sprechen – sprach – hat gesprochen | to speak |
nehmen – nahm – hat genommen | to take |
geben – gab – hat gegeben | to give |
finden – fand – hat gefunden | to find |
bringen – brachte – hat gebracht | to bring |
denken – dachte – hat gedacht | to think |
wissen – wusste – hat gewusst | to know (a fact) |
kennen – kannte – hat gekannt | to know (be familiar with) |
essen – aß – hat gegessen | to eat |
trinken – trank – hat getrunken | to drink |
schlafen – schlief – hat geschlafen | to sleep |
helfen – half – hat geholfen | to help |
treffen – traf – hat getroffen | to meet |
halten – hielt – hat gehalten | to hold, stop |
tragen – trug – hat getragen | to carry, wear |
wachsen – wuchs – ist gewachsen | to grow |
ziehen – zog – hat gezogen | to pull |
schneiden – schnitt – hat geschnitten | to cut |
messen – maß – hat gemessen | to measure |
wiegen – wog – hat gewogen | to weigh |
gießen – goss – hat gegossen | to pour, water |
graben – grub – hat gegraben | to dig |
werfen – warf – hat geworfen | to throw |
verlieren – verlor – hat verloren | to lose |
gewinnen – gewann – hat gewonnen | to win, extract |
beginnen – begann – hat begonnen | to begin |
verstehen – verstand – hat verstanden | to understand |
bestehen – bestand – hat bestanden | to pass; to consist |
entscheiden – entschied – hat entschieden | to decide |
vergleichen – verglich – hat verglichen | to compare |
beschreiben – beschrieb – hat beschrieben | to describe |
erhalten – erhielt – hat erhalten | to receive |
bekommen – bekam – hat bekommen | to get |
vergessen – vergaß – hat vergessen | to forget |
verbinden – verband – hat verbunden | to connect |
unterscheiden – unterschied – hat unterschieden | to distinguish |
enthalten – enthielt – hat enthalten | to contain |
anfangen – fing an – hat angefangen | to begin |
teilnehmen – nahm teil – hat teilgenommen | to take part |
vorschlagen – schlug vor – hat vorgeschlagen | to suggest |
einladen – lud ein – hat eingeladen | to invite |
aufstehen – stand auf – ist aufgestanden | to get up |
ausfallen – fiel aus – ist ausgefallen | to be cancelled |
zunehmen – nahm zu – hat zugenommen | to increase |
abnehmen – nahm ab – hat abgenommen | to decrease |
"""
