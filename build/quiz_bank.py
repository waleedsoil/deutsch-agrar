# -*- coding: utf-8 -*-
"""
Grammar item bank. One item per line:
week | question | option;option;option;option | index_of_correct | explanation
Weekly quizzes pull the items tagged with that week.
Checkpoints pull cumulatively from every week up to that point.
"""

BANK = r"""
1 | Welche Form ist richtig? "Ich ___ Student." | bin;bist;ist;sind | 0 | sein: ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind.
1 | "Woher kommen Sie?" fragt nach … | dem Herkunftsort;dem Alter;dem Beruf;der Adresse | 0 | woher = from where. Wo = where, wohin = to where.
1 | Wie wird "Boden" ausgesprochen? | mit langem o;mit kurzem o;mit ö;mit au | 0 | Vowel + single consonant + vowel = long vowel. Bo-den has a long o.
1 | Welches Wort hat einen langen Vokal? | Saat;Satt;Mann;Kamm | 0 | A doubled vowel is always long: Saat, Aal, Beet, Boot.
2 | "Du ___ im Labor." (arbeiten) | arbeitest;arbeitst;arbeitet;arbeite | 0 | Stems ending in -t or -d insert an -e- before the ending: du arbeitest, er arbeitet.
2 | Wo steht das konjugierte Verb im Aussagesatz? | an zweiter Position;am Anfang;am Ende;an dritter Position | 0 | The conjugated verb is always the second element in a German statement.
2 | "Morgen ___ ich ins Labor." | gehe;ich gehe;gehen;geht | 0 | If a time expression takes position 1, the verb stays in position 2 and the subject follows.
2 | Wie sagt man 342? | dreihundertzweiundvierzig;dreihundertvierzigzwei;dreihundertzwei und vierzig;dreihundertvierundzwanzig | 0 | German says the unit before the ten: zwei-und-vierzig.
3 | Welcher Artikel? "___ Bodenprobe" | die;der;das;den | 0 | Compound nouns take the gender of the last part: die Probe → die Bodenprobe.
3 | Welcher Artikel? "___ Düngung" | die;der;das;dem | 0 | Nouns ending in -ung are always feminine.
3 | Akkusativ: "Ich nehme ___ Bohrstock." | den;der;dem;des | 0 | Only the masculine changes in the accusative: der → den.
3 | Welcher Artikel? "___ Ergebnis" | das;der;die;dem | 0 | Nouns ending in -nis are usually neuter: das Ergebnis, das Zeugnis.
4 | "Es gibt" verlangt … | den Akkusativ;den Dativ;den Nominativ;den Genitiv | 0 | es gibt is always followed by the accusative: Es gibt einen Fehler.
4 | "Ich habe ___ Zeit." | keine;kein;keinen;nicht | 0 | Zeit is feminine, so kein takes -e in the accusative: keine Zeit.
4 | 14:30 Uhr heißt umgangssprachlich … | halb drei;halb zwei;zwei Uhr dreißig vor drei;drei Uhr halb | 0 | German "halb X" means half an hour BEFORE X: halb drei = 2:30.
4 | Wo steht "nicht" bei "Ich arbeite heute nicht"? | am Satzende;vor dem Verb;nach dem Subjekt;am Satzanfang | 0 | nicht negating the whole sentence goes at the end, before any final verb part.
5 | "Die Vorlesung ___ um acht ___." (anfangen) | fängt … an;anfängt;fängt an …;an … fängt | 0 | Separable prefixes move to the end of the main clause.
5 | "Ich ___ die Probe trocknen." (müssen) | muss;musst;müsse;müssen | 0 | Modal verbs have no ending in ich and er/sie/es: ich muss, er muss.
5 | Wo steht der Infinitiv bei einem Modalverb? | am Satzende;direkt nach dem Modalverb;an Position 2;am Satzanfang | 0 | Modal in position 2, infinitive at the very end: Ich kann heute nicht kommen.
5 | Welches Verb ist NICHT trennbar? | verstehen;aufstehen;mitkommen;einkaufen | 0 | ver-, be-, er-, ent-, ge-, zer- are inseparable and never take ge- in the participle.
6 | Imperativ (Sie): "___ Sie die Probe!" | Nehmen;Nimm;Nehmt;Nehme | 0 | The Sie-imperative keeps the infinitive form plus Sie: Nehmen Sie!
6 | Imperativ (du) von "nehmen": | Nimm!;Nehm!;Nimmst!;Nehme! | 0 | Verbs with e→i stem change keep the change in the du-imperative and drop the -st.
6 | "___ vorsichtig!" (sein, du) | Sei;Bist;Sein;Seie | 0 | sein is irregular in the imperative: Sei! / Seid! / Seien Sie!
6 | "möchten" drückt aus: | einen höflichen Wunsch;eine Erlaubnis;eine Verpflichtung;eine Fähigkeit | 0 | möchten is the polite wish form; wollen is more direct, dürfen is permission.
7 | "Ich fahre ___ dem Fahrrad." | mit;für;durch;ohne | 0 | mit always takes the dative and is one of the eight dative prepositions.
7 | "Ich arbeite ___ Professorin Weber." | bei;an;auf;für | 0 | bei + person means working at their group or under them.
7 | Dativ Plural: "Ich helfe den ___." (Studenten) | Studenten;Student;Studente;Studentes | 0 | Dative plural adds -n to the noun unless it already ends in -n or -s.
7 | Welches Verb verlangt den Dativ? | helfen;sehen;nehmen;fragen | 0 | helfen, danken, gehören, gefallen, schmecken and passen take the dative.
8 | Perfekt von "arbeiten": | hat gearbeitet;ist gearbeitet;hat arbeitet;hat gearbeitet worden | 0 | Regular verbs: ge- + stem + -t, with haben.
8 | Perfekt von "studieren": | hat studiert;hat gestudiert;ist studiert;hat studieren | 0 | Verbs ending in -ieren never take ge-.
8 | "___ Probe ist trocken." (mein, feminin) | Meine;Mein;Meinen;Meinem | 0 | Possessive articles follow the ein-pattern: meine Probe (f), mein Feld (n), mein Boden (m).
8 | Wo steht das Partizip II? | am Satzende;an Position 2;vor dem Objekt;am Satzanfang | 0 | haben/sein in position 2, participle at the very end. This is the Satzklammer.
9 | "Ich ___ nach Deutschland gekommen." | bin;habe;war;wurde | 0 | Verbs of movement and change of state take sein in the Perfekt.
9 | Partizip II von "lesen": | gelesen;gelest;geliest;gelesen worden | 0 | Strong verb: ge- + changed stem + -en.
9 | Perfekt von "anfangen": | hat angefangen;hat gefangan;ist angefangen;hat anfangen | 0 | The ge- goes between the prefix and the stem: an-ge-fangen.
9 | Welches Verb bildet das Perfekt mit "sein"? | bleiben;lesen;messen;kaufen | 0 | bleiben, sein and werden take sein even though nothing moves.
10 | "Ich gehe ___ das Labor." (Richtung) | in;im;an;bei | 0 | Wohin? takes the accusative: in das Labor / ins Labor.
10 | "Die Probe ist ___ Labor." (Ort) | im;ins;in das;an das | 0 | Wo? takes the dative: in dem Labor = im Labor.
10 | Wie sagt man den 3. Mai? | am dritten Mai;am drei Mai;an dem drittem Mai;im dritten Mai | 0 | Dates use am + ordinal with the dative ending -en.
10 | Wohin fährt man? "Ich fahre ___ Göttingen." | nach;in;zu;an | 0 | nach is used with cities and countries without an article.
11 | "Ich stelle die Kiste ___ den Tisch." | auf;auf dem;an dem;im | 0 | Movement (wohin?) with a two-way preposition takes the accusative.
11 | "Die Kiste steht ___ dem Tisch." | auf;auf den;an den;in den | 0 | Position (wo?) with a two-way preposition takes the dative.
11 | Welches Verb bedeutet "to lay something down"? | legen;liegen;lagen;gelegen | 0 | legen (legte, gelegt) is transitive and takes the accusative; liegen is the position verb.
11 | "Häng das Schild ___ die Wand." | an;an der;auf der;in der | 0 | Movement → accusative. Position would be: Das Schild hängt an der Wand.
12 | Komparativ von "hoch": | höher;hocher;hoher;höcher | 0 | hoch is irregular: hoch – höher – am höchsten.
12 | "Weizen braucht mehr Stickstoff ___ Hafer." | als;wie;wie als;denn | 0 | als is used for comparison of difference; wie only for equality (so … wie).
12 | Superlativ: "Dieser Boden ist ___ fruchtbarsten." | am;der;das;zum | 0 | The adverbial superlative is am + -sten.
12 | "immer größer" bedeutet: | zunehmend größer;sehr groß;am größten;nicht groß | 0 | immer + comparative expresses a continuing increase.
13 | Präteritum von "können" (ich): | konnte;kannte;könnte;gekonnt | 0 | konnte = simple past; könnte = Konjunktiv II; kannte comes from kennen.
13 | Nach "denn" ändert sich die Wortstellung … | gar nicht;Verb ans Ende;Verb an Position 1;Subjekt ans Ende | 0 | und, aber, oder, denn, sondern are position-0 and do not change word order.
13 | "Es ___ 2024 eine lange Trockenphase." | gab;gibt;hatte;war | 0 | Präteritum of es gibt is es gab.
13 | "Nicht Weizen, ___ Gerste." | sondern;aber;oder;denn | 0 | sondern corrects a preceding negation; aber contrasts without negation.
14 | "Ich bleibe zu Hause, weil es ___." | regnet;regnet es;es regnet;regnen | 0 | weil sends the conjugated verb to the end of the clause.
14 | "Weil es regnet, ___ ich zu Hause." | bleibe;ich bleibe;bleiben;bleibt | 0 | If the subordinate clause comes first, it fills position 1, so the main verb comes next.
14 | Welche Konjunktion verlangt Verb-Endstellung? | dass;denn;und;aber | 0 | dass, weil, wenn, obwohl, damit and ob are subordinating: verb goes last.
14 | "___ es zu nass ist, kann man nicht fahren." | Wenn;Als;Wann;Ob | 0 | wenn = if / whenever; als = a single past event; wann = question word.
15 | "Ich interessiere mich ___ Bodenkunde." | für;an;auf;über | 0 | sich interessieren für + Akkusativ is a fixed pair. Learn verb and preposition together.
15 | "Ich bewerbe mich ___ die Stelle." | um;für;auf;an | 0 | sich bewerben um + Akkusativ (or auf eine Stelle). bei + employer.
15 | "Ich nehme ___ der Exkursion teil." | an;auf;in;zu | 0 | teilnehmen an + Dativ.
15 | Wo steht "mich" im Nebensatz? "…, weil ich ___ angemeldet habe." | mich;sich;mir;mich mich | 0 | The reflexive pronoun matches the subject: ich → mich.
16 | "der ___ Boden" (trocken) | trockene;trockner;trockenen;trocken | 0 | After a definite article in the nominative singular the adjective takes -e.
16 | "Ich untersuche den ___ Boden." (schwer) | schweren;schwere;schwerer;schwers | 0 | Masculine accusative after der-word: -en.
16 | "Der Boden ist ___." (trocken) | trocken;trockene;trockener;trockenen | 0 | Predicative adjectives after sein, werden and bleiben take no ending at all.
16 | "in dem ___ Sommer" (heiß) | heißen;heiße;heißer;heißes | 0 | After a definite article in the dative, the ending is always -en.
17 | "ein ___ Ergebnis" (interessant) | interessantes;interessante;interessanter;interessanten | 0 | After ein with a neuter noun the adjective must carry the -es signal itself.
17 | "ein ___ Boden" (schwer, Nominativ) | schwerer;schwere;schweres;schweren | 0 | ein shows no gender, so the adjective takes the strong ending -er.
17 | "___ Boden, ___ Niederschläge" (schwer / gering, ohne Artikel) | Schwerer … geringe;Schwere … geringer;Schweren … gering;Schwerer … geringer | 0 | With no article: masculine nominative -er, plural nominative -e.
17 | "mit ___ Humusgehalt" (hoch, ohne Artikel) | hohem;hoher;hohes;hohen | 0 | Dative masculine with no article takes -em. Note hoch loses the c: hohem.
18 | Genitiv: "der Einfluss ___ Stickstoffs" | des;der;dem;den | 0 | Masculine and neuter genitive: des + noun with -s or -es.
18 | "die Ergebnisse ___ Untersuchung" | der;des;dem;den | 0 | Feminine genitive is der; the noun itself does not change.
18 | Was bedeutet "Bodenfruchtbarkeit"? | soil fertility;soil moisture;soil sample;soil profile | 0 | Read compounds right to left: Fruchtbarkeit (fertility) of the Boden (soil).
18 | Gesprochene Alternative zum Genitiv: | von + Dativ;mit + Dativ;für + Akkusativ;zu + Dativ | 0 | Spoken German prefers "das Feld von Herrn Müller" to "Herrn Müllers Feld".
19 | Höfliche Bitte: "___ Sie mir bitte helfen?" | Könnten;Konnten;Können Sie;Kannten | 0 | Konjunktiv II könnten is the standard polite request form.
19 | "Ich ___ gern an Ihrem Versuch mitarbeiten." | würde;werde;wurde;wäre | 0 | würde + infinitive expresses a polite wish; werde is future, wurde is past.
19 | Formelle Anrede in einer E-Mail: | Sehr geehrte Frau Weber,;Hallo Frau Weber,;Liebe Frau Weber,;Guten Tag Weber, | 0 | Sehr geehrte/r + title + surname is the standard formal opening.
19 | Formeller Schluss: | Mit freundlichen Grüßen;Liebe Grüße;Bis dann;Tschüss | 0 | Mit freundlichen Grüßen is neutral and always correct in formal writing.
20 | Futur I: "Ich ___ die Arbeit schreiben." | werde;würde;wurde;bin | 0 | Futur I = werden + infinitive. würde is conditional.
20 | Wann benutzt man im Deutschen meist das Präsens statt Futur? | wenn eine Zeitangabe dabei ist;nie;nur in Fragen;nur schriftlich | 0 | With a time marker, present tense is normal: Nächste Woche fange ich an.
20 | "Ich ___ Agrarwissenschaftler." (werden, Vollverb) | werde;bin;habe;würde | 0 | werden as a full verb means "to become" and needs no infinitive.
21 | Passiv Präsens: "Der Weizen ___ im Oktober ___." | wird … gesät;ist … gesät;hat … gesät;wird … säen | 0 | Passiv = werden (conjugated) + Partizip II at the end.
21 | Wer handelt? "Das Feld wird vom Landwirt gedüngt." | der Landwirt;das Feld;der Dünger;niemand | 0 | von + dative marks the agent, the one who actually does it.
21 | Aktiv → Passiv: "Wir messen die Proben." | Die Proben werden gemessen.;Die Proben sind gemessen.;Wir werden die Proben gemessen.;Die Proben messen. | 0 | The accusative object becomes the subject; the verb becomes werden + Partizip II.
21 | "durch" im Passiv markiert … | das Mittel oder die Ursache;die Person;den Ort;die Zeit | 0 | von = person, durch = means or cause: durch Regen zerstört.
22 | Passiv Präteritum: "Die Versuche ___ angelegt." | wurden;werden;sind;waren | 0 | Passiv Präteritum uses wurde/wurden + Partizip II.
22 | Passiv Perfekt: "Das Feld ist gedüngt ___." | worden;geworden;gewesen;werden | 0 | In the passive perfect, werden becomes worden, not geworden.
22 | "Das Feld ist gedüngt." beschreibt … | einen Zustand;einen Vorgang;die Zukunft;eine Bitte | 0 | sein + Partizip II is the Zustandspassiv: the result, not the action.
22 | "Hier wird gearbeitet." ist … | unpersönliches Passiv;Aktiv;Zustandspassiv;Futur | 0 | Impersonal passive has no subject and is common on signs and notices.
23 | "___ der Versuch klein war, sind die Ergebnisse klar." | Obwohl;Weil;Damit;Trotzdem | 0 | obwohl introduces a concession and sends the verb to the end.
23 | "Wir säen Zwischenfrüchte, ___ den Boden zu schützen." | um;damit;dass;für | 0 | um … zu is used when both clauses share the same subject.
23 | Wann muss man "damit" statt "um … zu" nehmen? | bei verschiedenen Subjekten;immer;nie;nur im Passiv | 0 | Different subjects require damit: Ich erkläre es, damit du es verstehst.
23 | "___ ich in Indien gearbeitet habe, habe ich viel gelernt." (einmaliges Ereignis) | Als;Wenn;Wann;Ob | 0 | als = one specific event in the past; wenn = repeated or future.
24 | Indirekte Frage: "Können Sie mir sagen, wann der Zug ___?" | abfährt;fährt ab;abfahren;fährt | 0 | Indirect questions are subordinate clauses: the separable verb stays together at the end.
24 | Indirekte Ja/Nein-Frage benutzt … | ob;dass;wenn;was | 0 | ob is the indirect form of a yes/no question: Ich weiß nicht, ob er kommt.
24 | "Ich wollte fragen, ___ ich die Frist verlängern kann." | ob;dass;wann;wenn | 0 | The direct question would be "Kann ich …?", a yes/no question → ob.
25 | "Humus ist der Teil des Bodens, ___ organisch ist." | der;den;dem;das | 0 | Gender from Teil (masculine), case from its role as subject → der.
25 | "Der Versuch, ___ wir gestern besprochen haben, läuft weiter." | den;der;dem;dessen | 0 | Masculine head noun, but the pronoun is the direct object in its own clause → den.
25 | Wo steht das Verb im Relativsatz? | am Ende;an Position 2;vor dem Pronomen;am Anfang | 0 | Relative clauses are subordinate clauses: conjugated verb last.
25 | "Zwischenfrüchte sind Pflanzen, ___ man zwischen zwei Kulturen anbaut." | die;der;denen;deren | 0 | Plural head noun, accusative object in the relative clause → die.
26 | "Der Kollege, ___ ich geholfen habe, ist Agronom." | dem;den;der;dessen | 0 | helfen takes the dative, so the relative pronoun is dative masculine: dem.
26 | "Der Versuch, ___ Ergebnisse wir kennen, …" | dessen;deren;dem;den | 0 | Genitive relative pronoun: dessen for masculine/neuter, deren for feminine/plural.
26 | "Das Feld, ___ wir arbeiten, ist nass." | auf dem;auf das;auf dem das;das auf | 0 | The preposition comes before the relative pronoun and sets its case: auf + Ort → Dativ.
26 | "Alles, ___ er gesagt hat, war richtig." | was;das;dass;welches | 0 | After alles, nichts, etwas and das the relative pronoun is was.
27 | "Ich freue mich ___ das Gespräch." | auf;über;für;an | 0 | sich freuen auf = look forward to (future); sich freuen über = be glad about (past).
27 | "Der Ertrag hängt ___ dem Niederschlag ab." | von;an;auf;über | 0 | abhängen von + Dativ.
27 | Bezug auf eine Sache: "Ich denke oft ___." | daran;an ihn;an es;darauf | 0 | denken an + da-compound for things: daran. For people: an ihn / an sie.
27 | Frage nach einer Sache: "___ beschäftigen Sie sich?" | Womit;Mit was;Mit wem;Wovon | 0 | wo(r)- + preposition asks about things; mit wem asks about people.
28 | "die Erhöhung ___ Düngung" | der;des;dem;den | 0 | Feminine genitive: der Düngung.
28 | n-Deklination: "Ich habe mit dem ___ gesprochen." (Student) | Studenten;Student;Studentes;Studenten's | 0 | Masculine n-nouns (Student, Kollege, Praktikant, Experte) add -n/-en in every case except nominative singular.
28 | Nominalstil von "Wir haben die Daten ausgewertet": | die Auswertung der Daten;wir werteten aus;die Daten auswerten;auswertend die Daten | 0 | Verb → noun, object → genitive. This is the register of German textbooks.
29 | "Es hat geregnet, ___ konnten wir nicht säen." | deshalb;weil;obwohl;damit | 0 | deshalb is an adverb in position 1, so the verb inverts: deshalb konnten wir …
29 | Was folgt nach "trotzdem" am Satzanfang? | das konjugierte Verb;das Subjekt;ein Komma;der Infinitiv | 0 | trotzdem occupies position 1, so the verb must come in position 2.
29 | "Ich habe ___ wenig Erfahrung, ___ ich lerne schnell." | zwar … aber;sowohl … als auch;weder … noch;je … desto | 0 | zwar … aber concedes a point and then counters it.
30 | "___ höher die Düngung, ___ größer das Auswaschungsrisiko." | Je … desto;So … wie;Zwar … aber;Weder … noch | 0 | je + comparative (verb last) , desto + comparative + verb + subject.
30 | "Ich habe ___ Laborerfahrung ___ Felderfahrung." | sowohl … als auch;entweder … oder;weder … noch;zwar … aber | 0 | sowohl … als auch = both … and.
30 | "Er hat ___ Zeit ___ Geld." (er hat nichts) | weder … noch;sowohl … als auch;entweder … oder;nicht nur … sondern | 0 | weder … noch is already negative; do not add nicht.
30 | Wortstellung nach "je …": | Verb am Ende;Verb an Position 2;Verb am Anfang;kein Verb | 0 | The je-clause is subordinate: Je mehr Regen fällt, desto besser wächst der Bestand.
31 | Konjunktiv II von "haben": | hätte;hatte;habe;hätt | 0 | hätte (with umlaut) is Konjunktiv II; hatte is the simple past.
31 | Irrealis der Vergangenheit: "Wenn es geregnet ___, ___ der Ertrag höher gewesen." | hätte … wäre;hatte … war;würde … würde;hätte … hätte | 0 | Past unreal = hätte/wäre + Partizip II, with the auxiliary chosen by the main verb.
31 | "An deiner Stelle ___ ich mich bewerben." | würde;werde;wurde;wäre | 0 | würde + infinitive is the standard way to give advice.
31 | Welche Form ist Konjunktiv II von "kommen"? | käme;kam;komme;kommte | 0 | Strong verbs form Konjunktiv II from the Präteritum stem plus umlaut: kam → käme.
32 | "Das Feld ___ gedüngt werden." (müssen) | muss;wird;ist;hat | 0 | Modal + Partizip II + werden: Das Feld muss gedüngt werden.
32 | "Die Vorschrift ist zu beachten." bedeutet: | Sie muss beachtet werden.;Sie kann beachtet werden.;Sie wurde beachtet.;Sie darf beachtet werden. | 0 | sein + zu + Infinitiv expresses obligation in the passive sense.
32 | "Das lässt sich messen." bedeutet: | Das kann gemessen werden.;Das wird gemessen.;Das wurde gemessen.;Das muss gemessen werden. | 0 | sich lassen + Infinitiv is a common passive substitute meaning "can be".
32 | Was bedeutet "messbar"? | kann gemessen werden;muss gemessen werden;wurde gemessen;wird gemessen | 0 | The suffix -bar means "able to be …": messbar, anwendbar, lesbar.
33 | "die ___ Nachfrage" (steigen, Partizip I) | steigende;gestiegene;steigen;steigend | 0 | Partizip I = infinitive + d, then normal adjective endings: die steigende Nachfrage.
33 | "das ___ Getreide" (ernten, Partizip II) | geerntete;erntende;geerntet;ernten | 0 | Partizip II as an attribute has passive meaning and takes adjective endings.
33 | Partizip I hat welche Bedeutung? | aktiv und gleichzeitig;passiv;abgeschlossen;zukünftig | 0 | Partizip I is active and simultaneous; Partizip II is passive and completed.
34 | "___ der Trockenheit blieb der Ertrag stabil." | Trotz;Wegen;Während;Aufgrund | 0 | trotz + Genitiv expresses concession: despite the drought.
34 | "___ der geringen Stichprobe sind die Ergebnisse unsicher." | Aufgrund;Trotz;Obwohl;Während | 0 | aufgrund + Genitiv gives the cause. obwohl would need a full clause.
34 | Welches Wort schwächt eine Aussage ab? | vermutlich;eindeutig;sicher;definitiv | 0 | Hedging words like vermutlich, tendenziell and weitgehend are standard in academic German.
34 | Korrekte Quellenangabe: | Nach Müller (2023) …;Müller sagt 2023 …;Bei Müller 2023 sagt …;Müller (2023) sagte mir … | 0 | Nach + author + year, or Laut der Studie von …, is the neutral academic form.
35 | "Nachdem wir gesiebt ___, haben wir gewogen." | hatten;haben;hatte;sind | 0 | nachdem requires a tense one step earlier: Plusquamperfekt before Perfekt.
35 | Plusquamperfekt wird gebildet mit … | hatte/war + Partizip II;habe/bin + Partizip II;werde + Infinitiv;würde + Infinitiv | 0 | Plusquamperfekt = Präteritum of haben/sein + Partizip II.
35 | "___ der Boden abgetrocknet ist, fangen wir an." | Sobald;Nachdem;Während;Bevor | 0 | sobald = as soon as, and takes the present for a near-future condition.
35 | Welche Reihenfolge? "bevor" markiert … | das spätere Ereignis im Nebensatz;das frühere Ereignis;Gleichzeitigkeit;eine Ursache | 0 | Bevor wir säen, bearbeiten wir den Boden: the bevor-clause happens second.
36 | "Es ist wichtig, die Proben sofort ___ kühlen." | zu;um zu;dass;für | 0 | An infinitive clause after es ist wichtig uses plain zu + Infinitiv.
36 | Trennbares Verb im Infinitivsatz: "Ich habe vor, morgen ___." | anzufangen;zu anfangen;anfangen zu;zufangen an | 0 | zu goes between the prefix and the stem: an-zu-fangen.
36 | "Ich habe das Praktikum gemacht, ___ Erfahrung zu sammeln." | um;damit;ohne;statt | 0 | um … zu expresses purpose with the same subject.
36 | "Er ging, ___ etwas zu sagen." | ohne;um;statt;damit | 0 | ohne … zu = without doing something.
37 | Konjunktiv I von "sein" (er): | sei;ist;wäre;war | 0 | sei is the Konjunktiv I form used in reported speech in written German.
37 | "Er sagte, er ___ krank." (indirekte Rede) | sei;ist;war;wäre gewesen | 0 | Reported speech in news and academic writing uses Konjunktiv I where it is distinct.
37 | Wann ersetzt Konjunktiv II den Konjunktiv I? | wenn die Form wie der Indikativ aussieht;immer;nie;nur bei sein | 0 | If Konjunktiv I is identical to the indicative (sie haben), Konjunktiv II (sie hätten) is used.
38 | Welche Zeitform benutzt eine Zusammenfassung? | Präsens;Präteritum;Perfekt;Futur | 0 | Summaries of texts are written in the present tense.
38 | Welche Zeitform benutzt ein Versuchsbericht? | Präteritum oder Perfekt;Präsens;Futur;Konjunktiv | 0 | Reports of completed work use the past, usually with the passive.
38 | Was gehört NICHT in eine Zusammenfassung? | die eigene Meinung;die Kernaussage;die Struktur;das Thema | 0 | A Zusammenfassung stays neutral; opinion belongs in a Stellungnahme.
39 | "Der Ertrag ist ___ 20 Prozent gestiegen." (Zunahme von 20 %) | um;auf;bei;über | 0 | um = by that amount; auf = to that level. The difference matters in exams.
39 | "Die Grafik ___ die Entwicklung der Preise." | zeigt;sieht;schaut;liest | 0 | Standard opener: Die Grafik zeigt / stellt … dar / gibt … wieder.
39 | Wie beschreibt man eine kleine Zunahme? | leicht gestiegen;sprunghaft gestiegen;stark gefallen;stagniert | 0 | leicht / geringfügig = small; deutlich / stark / sprunghaft = large.
40 | Der deutsche Lebenslauf ist … | tabellarisch und rückwärts chronologisch;ein Fließtext;eine Liste von Hobbys;ein Motivationsschreiben | 0 | German CVs are tabular, reverse chronological, one to two pages.
40 | Was gehört in den Betreff einer Bewerbung? | die Stelle und die Referenznummer;eine Begrüßung;der eigene Name;das Datum | 0 | Betreff: Bewerbung als … , Referenznummer … — precise and searchable.
40 | Nominalstil im Lebenslauf: | Durchführung von Feldversuchen;Ich habe Feldversuche gemacht;Feldversuche machen;Ich mache Feldversuche | 0 | CV bullets use nouns, not full sentences.
41 | Gute Antwort auf "Erzählen Sie etwas über sich": | Studium, Erfahrung, Bezug zur Stelle;die ganze Lebensgeschichte;nur der Name;nur die Hobbys | 0 | Structure: who I am, what I can do, why this position. Two minutes maximum.
41 | STAR auf Deutsch heißt: | Situation, Aufgabe, Handlung, Ergebnis;Studium, Text, Arbeit, Referenz;Struktur, Thema, Antwort, Rede;Situation, Team, Aufgabe, Regel | 0 | Use it to answer every "Erzählen Sie von einer Situation, in der …" question.
41 | Beste Schwäche-Antwort: | eine echte Schwäche plus konkrete Gegenmaßnahme;"Ich bin Perfektionist";"Ich habe keine";"Ich arbeite zu viel" | 0 | Name something real, small and relevant, then say what you do about it.
42 | "Meine Gehaltsvorstellung ___ bei 45.000 Euro brutto." | liegt;ist;hat;steht | 0 | liegen bei is the standard, slightly softer collocation for a salary figure.
42 | Was ist die Probezeit? | eine Anfangszeit mit kurzer Kündigungsfrist;die Einarbeitung;ein Praktikum;die Urlaubszeit | 0 | Usually up to six months, with a two-week notice period on both sides.
42 | Zeit gewinnen im Gespräch: | "Darf ich kurz überlegen?";"Ich weiß nicht.";"Nächste Frage.";Schweigen | 0 | Buying time politely is better than guessing or freezing.
42 | Was ist eine Befristung? | eine zeitliche Begrenzung des Vertrags;eine Gehaltserhöhung;eine Kündigung;eine Beförderung | 0 | befristet = fixed-term; unbefristet = permanent.
43 | "Wie verhalten Sie sich?" fragt nach … | Ihrer Handlung in der Situation;Ihrem Namen;der Regel;dem Schild | 0 | This stem asks what you actually do. Answer options describe actions.
43 | Was bedeutet "rechts vor links"? | Wer von rechts kommt, hat Vorfahrt.;Rechts abbiegen ist erlaubt.;Links hat Vorfahrt.;Man fährt rechts. | 0 | Default rule at unsigned junctions.
43 | Der Anhalteweg besteht aus … | Reaktionsweg und Bremsweg;nur Bremsweg;nur Reaktionsweg;Bremsweg und Abstand | 0 | Anhalteweg = Reaktionsweg + Bremsweg. A standard exam calculation.
43 | Der Schulterblick prüft … | den toten Winkel;den Bremsweg;den Reifendruck;das Blinklicht | 0 | The mirror does not cover the blind spot, so the shoulder check is mandatory.
44 | Am Telefon bitten, langsamer zu sprechen: | "Könnten Sie bitte etwas langsamer sprechen?";"Sprechen Sie langsam!";"Ich verstehe nicht.";"Was?" | 0 | Polite and confident. Never apologise for your German on the phone.
44 | Was ist ein Bescheid? | eine offizielle Entscheidung;eine Rechnung;eine Frage;eine Bestätigung des Empfangs | 0 | A Bescheid is a formal decision you can object to (Widerspruch) within a Frist.
44 | Reklamation: "Das Gerät hat einen ___." | Mangel;Fehlen;Schuld;Problem | 0 | Mangel is the legal term for a defect and triggers Gewährleistung rights.
45 | Häufigster Fehler von Lernenden im Nebensatz: | Verb nicht am Ende;falsches Genus;falsche Zeitform;fehlendes Komma | 0 | Verb-final placement is the single highest-value thing to automate.
45 | Wie prüft man ein Adjektivende schnell? | Zeigt der Artikel das Genus? Wenn nein, muss das Adjektiv es zeigen.;Immer -en;Immer -e;Nach Gefühl | 0 | This one rule collapses all three adjective tables.
46 | Wie lange dauert das Modul Lesen in der B1-Prüfung? | 65 Minuten;30 Minuten;90 Minuten;45 Minuten | 0 | Goethe-Zertifikat B1: Lesen 65 min, Hören 40 min, Schreiben 60 min, Sprechen 15 min.
46 | Beste Strategie beim Hörverstehen: | Aufgaben vorher lesen;nur zuhören;alles mitschreiben;raten | 0 | Read the questions in the pause first; you then listen for specific information.
46 | Was tun, wenn Sie ein Wort im Lesetext nicht kennen? | weiterlesen und aus dem Kontext erschließen;sofort nachschlagen;die Aufgabe überspringen;raten und weitergehen | 0 | You are tested on understanding the text, not every word. Read on; the answer is usually in the next sentence.
47 | "Nährstoffversorgung" besteht aus … | Nährstoff + Versorgung;Nähr + Stoffversorgung;Nährstoffver + Sorgung;Näh + Rstoffversorgung | 0 | Split compounds at the real word boundaries and read right to left: the supply of nutrients.
47 | Beste Strategie bei einem Text über Ihrem Niveau: | Kernaussage pro Absatz suchen;jedes Wort übersetzen;nur die Überschrift lesen;aufgeben | 0 | One core sentence per paragraph gives you the argument. Detail can come on a second pass.
47 | Was bedeutet "Beschreibende Sortenliste"? | eine amtliche Liste mit Sorteneigenschaften;eine Preisliste;eine Anbauanleitung;ein Gesetzestext | 0 | Published by the Bundessortenamt; standard reading for anyone working with varieties in Germany.
48 | Welches Zertifikat ist für den Arbeitsmarkt am gängigsten? | Goethe-Zertifikat oder telc;nur ein Universitätskurs;ein Sprachtandem;ein Onlinekurs ohne Prüfung | 0 | Employers recognise Goethe, telc and ÖSD. A certificate makes your level checkable.
48 | Was ändert sich typischerweise auf B2? | aktiver Konjunktiv I und komplexer Nominalstil;das Alphabet;die Wortstellung;die Artikel | 0 | B2 adds register control: reported speech, Funktionsverbgefüge and dense nominal style.
48 | Wie hält man ein erreichtes Niveau? | tägliche kurze Nutzung;einmal im Monat lernen;nur Prüfungen wiederholen;gar nichts tun | 0 | Thirty minutes of real use a day beats three hours once a week. Maintenance is a habit, not a course.
"""
