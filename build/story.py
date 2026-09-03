# -*- coding: utf-8 -*-
"""
कथा — a serialised story that unlocks one episode every three weeks.
Each episode is written at the level reached in that week: episode 1 uses only
present tense and the accusative; episode 16 uses everything up to B1.
Glossary entries: [German, English, मराठी].
"""

EPISODES = [
{"w":1,"n":1,"title":"Ankunft","mr_title":"आगमन","level":"A1",
 "text":"""Nikhil kommt aus Solapur. Solapur ist eine Stadt in Indien. Jetzt wohnt er in Göttingen.

Sein Zimmer ist klein. Es hat ein Bett, einen Tisch und ein Fenster. Das Fenster ist groß. Draußen steht ein Baum. Der Baum hat keine Blätter mehr.

Es ist Oktober. Es ist kalt und grau. In Solapur ist es jetzt warm.

Nikhil hat Hunger. Er geht in die Küche. Dort steht eine Frau und trinkt Tee.

„Hallo, ich bin Fatma“, sagt sie. „Ich wohne auch hier. Und du?“

„Ich heiße Nikhil. Ich bin neu. Ich komme aus Indien.“

„Willkommen. Sprichst du Deutsch?“

Nikhil ist ehrlich. „Ein bisschen. Sehr wenig.“

Fatma lacht. „Ein bisschen ist genug für heute.“

Nikhil geht in sein Zimmer zurück. Er hat ein Buch. Das Buch ist neu und dünn. Auf dem Buch steht ein Wort: Deutsch.

Er öffnet die erste Seite.""",
 "gloss":[["die Ankunft","arrival","आगमन"],["das Zimmer","room","खोली"],["das Blatt","leaf","पान"],
          ["ehrlich","honest","प्रामाणिक"],["ein bisschen","a little","थोडंसं"],
          ["genug","enough","पुरेसं"],["die Seite","page","पान (पुस्तकाचं)"]],
 "mr":"पहिल्या भागात फक्त वर्तमानकाळ आहे — तुम्ही आठवडा ३ मध्ये जे शिकलात तेवढंच. 'Er hat ein Buch' मध्ये 'ein' कर्म आहे म्हणून द्वितीया, पण नपुंसकलिंगात रूप बदलत नाही. 'Er hat einen Tisch' मध्ये मात्र einen — पुल्लिंगातच बदल होतो. मराठीत 'ला' सगळ्या लिंगांना लागतो; जर्मनमध्ये फक्त पुल्लिंग बदलतं. एवढाच फरक लक्षात ठेवा.",
 "q":[["Woher kommt Nikhil?",["Aus Indien","Aus der Türkei","Aus Göttingen","Aus Solapur in Deutschland"],0,"Solapur ist eine Stadt in Indien — der zweite Satz sagt es direkt."],
      ["Wie viel Deutsch spricht Nikhil?",["Ein bisschen","Sehr gut","Gar nichts","Nur Englisch"],0,"„Ein bisschen. Sehr wenig.“ — und Fatma sagt, das ist genug für heute."]]},

{"w":6,"n":2,"title":"Der erste Tag im Labor","mr_title":"प्रयोगशाळेतला पहिला दिवस","level":"A1",
 "text":"""Frau Dr. Bergmann ist klein und spricht schnell. Sehr schnell.

„Guten Morgen. Sie sind der neue Student aus Indien?“

„Ja. Ich heiße Nikhil Deshmukh.“

„Gut. Kommen Sie mit.“

Im Labor stehen zwanzig Kisten. In den Kisten ist Erde.

„Hören Sie zu“, sagt Frau Bergmann. „Nehmen Sie eine Probe. Wiegen Sie die Probe. Notieren Sie das Gewicht. Dann trocknen Sie die Probe bei hundertfünf Grad. Verstehen Sie?“

Nikhil versteht vier Wörter: Probe, wiegen, trocknen, Grad. Das ist genug. Er nickt.

„Können Sie das machen?“

„Ja, ich kann das machen.“

„Gut. Sie dürfen die Waage benutzen. Aber Sie müssen vorsichtig sein. Sie ist alt.“

Frau Bergmann geht. Nikhil steht allein im Labor. Er nimmt eine Probe. Er wiegt sie. Er notiert das Gewicht.

Um zwölf Uhr kommt ein Student herein. Er ist groß und trägt eine Warnweste.

„Du bist der Neue, oder? Ich bin Jonas. Sag mal — verstehst du Bergmann?“

„Nein.“

Jonas lacht laut. „Ich auch nicht. Und ich bin Deutscher.“""",
 "gloss":[["zuhören","to listen","लक्ष देऊन ऐकणे"],["das Gewicht","weight","वजन"],
          ["nicken","to nod","मान डोलावणे"],["die Waage","scale","तराजू"],
          ["benutzen","to use","वापरणे"],["vorsichtig","careful","काळजीपूर्वक"],
          ["allein","alone","एकटा"],["laut","loud(ly)","मोठ्याने"]],
 "mr":"आज्ञार्थ बघा: 'Nehmen Sie', 'Wiegen Sie', 'Trocknen Sie' — क्रियापद पहिल्या जागी आणि Sie लगेच मागे. मराठीत 'घ्या', 'वजन करा' — तेच काम, पण जर्मनला Sie लिहावंच लागतं. आणि 'Hören Sie zu' मध्ये zu शेवटी गेला — विभक्त क्रियापद, अगदी मराठीतल्या 'लक्ष देऊन ऐका' सारखं दोन तुकड्यांत. Modal वाक्यंही बघा: 'Sie müssen vorsichtig sein' — मूळ क्रियापद शेवटी, मराठीसारखं.",
 "q":[["Was soll Nikhil mit der Probe machen?",["Wiegen, notieren, trocknen","Nur trocknen","Nur wiegen","Zu Frau Bergmann bringen"],0,"Die Anweisung kommt in drei Imperativen nacheinander."],
      ["Warum lacht Jonas?",["Er versteht Frau Bergmann auch nicht","Nikhil hat einen Fehler gemacht","Die Waage ist kaputt","Er kennt Solapur"],0,"Er ist Deutscher und versteht sie trotzdem nicht — das ist die Pointe."]]},

{"w":9,"n":3,"title":"Das Bürgeramt","mr_title":"नगरपालिका कार्यालय","level":"A1",
 "text":"""Am Montag ist Nikhil um sieben Uhr aufgestanden. Er hat gefrühstückt und ist zum Bürgeramt gefahren.

Er hat eine Nummer genommen: 247. Auf dem Bildschirm stand 189.

Er hat zwei Stunden gewartet. Er hat sein Buch gelesen. Er hat drei Kapitel gelernt. Dann hat er nichts mehr gelesen und nur gewartet.

Um halb elf ist seine Nummer gekommen.

Die Frau am Schalter hat nicht gelächelt. „Unterlagen, bitte.“

Nikhil hat den Pass, den Mietvertrag und die Wohnungsgeberbestätigung gegeben.

Die Frau hat alles genommen. Sie hat etwas getippt. Sie hat einen Stempel genommen und auf ein Papier gedrückt.

„Fertig. Das ist Ihre Meldebescheinigung.“

Nikhil hat das Papier genommen. „Danke. Das war alles?“

Zum ersten Mal hat die Frau gelächelt. „Das war alles. Willkommen in Göttingen.“

Draußen hat es geregnet. Nikhil ist trotzdem langsam gegangen. Er hat das Papier fest in der Hand gehalten. Er ist jetzt offiziell hier.""",
 "gloss":[["aufstehen","to get up","उठणे"],["der Bildschirm","screen","पडदा, स्क्रीन"],
          ["warten","to wait","वाट पाहणे"],["der Schalter","service counter","खिडकी, काउंटर"],
          ["lächeln","to smile","हसणे"],["die Unterlagen","documents","कागदपत्रं"],
          ["der Stempel","stamp","शिक्का"],["fertig","done","झालं, पूर्ण"]],
 "mr":"हा भाग पूर्ण भूतकाळात आहे. sein आणि haben ची निवड बघा: 'ist aufgestanden', 'ist gefahren', 'ist gekommen', 'ist gegangen' — सगळी गतीची क्रियापदं. 'hat gewartet', 'hat gelesen', 'hat genommen' — सकर्मक. हे नेमकं मराठीच्या 'ने'-प्रयोगासारखं आहे: 'मी गेलो' (गती, sein) विरुद्ध 'मी वाचलं' (सकर्मक, haben). इंग्रजी भाषकांना ही यादी पाठ करावी लागते — तुमच्या डोक्यात ती आधीच आहे.",
 "q":[["Wie lange hat Nikhil gewartet?",["Etwa zwei Stunden","Zehn Minuten","Den ganzen Tag","Er hat nicht gewartet"],0,"Von kurz nach sieben bis halb elf, und der Text sagt: zwei Stunden."],
      ["Warum steht „ist gegangen\“ und nicht „hat gegangen\“?",["gehen ist ein Bewegungsverb","gehen ist unregelmäßig","Es ist ein Fehler","Weil es regnet"],0,"Bewegung und Zustandswechsel nehmen sein — genau wie मराठी 'मी गेलो' ohne ने."]]},

{"w":12,"n":4,"title":"Herr Krämer","mr_title":"क्रेमर साहेब","level":"A2",
 "text":"""Das Versuchsfeld liegt zwanzig Minuten außerhalb der Stadt. Herr Krämer ist der Landwirt. Er ist sechzig Jahre alt, spricht wenig und geht schnell.

„Sie sind aus Indien? Was baut man da an?“

„Zuckerrohr. Hirse. Baumwolle. Bei uns ist es viel wärmer als hier.“

„Wie viel Regen?“

„Weniger. Viel weniger. Aber der Regen kommt schneller und stärker.“

Herr Krämer hat genickt. Das war offenbar eine gute Antwort.

„Und die Felder? Größer oder kleiner?“

„Viel kleiner. Mein Onkel hat zwei Hektar. Das ist bei uns normal.“

Herr Krämer hat gelacht — kurz, nur einmal. „Zwei Hektar. Ich habe hundertvierzig. Und ich habe trotzdem weniger Zeit als Sie.“

Sie sind über das Feld gegangen. Der Boden war schwer und nass. Nikhils Schuhe waren nach zehn Metern doppelt so schwer.

„Sehen Sie das?“, hat Herr Krämer gesagt und auf eine Spur gezeigt. „Das ist der Traktor von letzter Woche. Der Boden war zu nass. Das war mein Fehler. Der teuerste Fehler in diesem Jahr.“

Nikhil hat die Spur angeschaut. Bodenverdichtung. Das Wort kannte er aus dem Buch. Zum ersten Mal hat er es im Feld gesehen.""",
 "gloss":[["außerhalb","outside of","बाहेर, वेशीबाहेर"],["anbauen","to grow, cultivate","लागवड करणे"],
          ["offenbar","apparently","बहुधा, स्पष्टपणे"],["die Spur","track, mark","खूण, चाकाचा माग"],
          ["der Fehler","mistake","चूक"],["teuer","expensive","महाग"],
          ["schwer","heavy; difficult","जड; कठीण"]],
 "mr":"तुलनेची रूपं मोजा: wärmer, weniger, schneller, stärker, größer, kleiner, teuerste. आणि 'als' — मराठीतलं 'पेक्षा'. 'Es ist wärmer als hier' = 'इथल्यापेक्षा जास्त उबदार आहे.' एक सापळा: 'so schwer wie' (इतकं… जितकं) मध्ये wie येतं, als नाही. मराठीत 'पेक्षा' आणि 'इतकं' वेगळे आहेत — तसंच als आणि wie वेगळे ठेवा.",
 "q":[["Wie groß ist der Betrieb von Herrn Krämer?",["140 Hektar","2 Hektar","20 Hektar","Das steht nicht im Text"],0,"„Ich habe hundertvierzig\“ — direkt nach den zwei Hektar des Onkels."],
      ["Was war Herrn Krämers Fehler?",["Er ist bei zu nassem Boden gefahren","Er hat zu spät gesät","Er hat zu viel gedüngt","Er hat den Traktor verkauft"],0,"Zu nasser Boden plus Traktor ergibt Bodenverdichtung — und die ist teuer und langsam zu reparieren."]]},

{"w":15,"n":5,"title":"Vierzig Proben","mr_title":"चाळीस नमुने","level":"A2",
 "text":"""Am Donnerstag ist es passiert.

Nikhil hat sich beeilt. Er wollte um sechs fertig sein, weil er sich mit Jonas verabredet hatte. Er hat vierzig Proben aus dem Feld geholt und die Etiketten geschrieben.

Am Freitagmorgen hat Frau Bergmann die Kisten angeschaut. Dann hat sie sehr lange nichts gesagt.

„Herr Deshmukh. Die Parzellen drei und dreizehn haben dasselbe Etikett.“

Nikhil hat sich sofort erinnert. Der Regen. Der Stift. Die Eile.

„Es tut mir sehr leid. Ich habe mich beeilt.“

„Können wir wissen, welche Probe welche ist?“

„Nein.“

„Dann sind es nicht zwei Proben. Es sind achtunddreißig Proben und zwei Fragezeichen.“

Nikhil hat sich sehr geschämt. Er hat sich auf einen Fehler mit der Sprache vorbereitet. Auf diesen Fehler hat er sich nicht vorbereitet.

„Ich hole sie noch einmal. Heute.“

Frau Bergmann hat ihn angesehen. „Ja. Das machen Sie. Und Herr Deshmukh — Sie haben mir das sofort gesagt, ohne Ausrede. Das ist wichtiger als vierzig Proben.“

Am Nachmittag ist er wieder auf das Feld gefahren. Es hat wieder geregnet. Diesmal hat er sich Zeit genommen.""",
 "gloss":[["sich beeilen","to hurry","घाई करणे"],["sich verabreden","to arrange to meet","भेटायचं ठरवणे"],
          ["das Etikett","label","चिठ्ठी, लेबल"],["die Eile","hurry","घाई"],
          ["sich erinnern","to remember","आठवणे"],["sich schämen","to be ashamed","लाज वाटणे"],
          ["die Ausrede","excuse","सबब"],["sich vorbereiten auf","to prepare for","तयारी करणे"]],
 "mr":"या भागात परावर्तनी क्रियापदं आहेत: sich beeilen, sich erinnern, sich schämen, sich vorbereiten. मराठीत 'घाई करणे' मध्ये 'स्वतःला' लागत नाही — जर्मनला mich/sich लागतं. ही जर्मनची स्वतःची सवय आहे, मराठीतून येत नाही, म्हणून क्रियापद आणि परावर्तनी सर्वनाम एकत्रच पाठ करा. आणि 'sich vorbereiten auf' मधलं auf कधीच बदलत नाही — जोडीने लक्षात ठेवा, वेगळं नाही.",
 "q":[["Was war das Problem?",["Zwei Proben hatten dasselbe Etikett","Er hat die Proben verloren","Er kam zu spät","Die Waage war kaputt"],0,"Parzellen drei und dreizehn — im Regen, in Eile geschrieben."],
      ["Was findet Frau Bergmann wichtiger als vierzig Proben?",["Dass er den Fehler sofort zugegeben hat","Dass er schnell arbeitet","Dass er gut Deutsch spricht","Dass er das Feld kennt"],0,"„ohne Ausrede\“ — im deutschen Arbeitsleben zählt das oft mehr als der Fehler selbst."]]},

{"w":18,"n":6,"title":"Die Sprache der Bücher","mr_title":"पुस्तकांची भाषा","level":"A2",
 "text":"""Jonas hat Nikhil ein Buch geliehen. Der Titel war kurz: Grundlagen der Bodenkunde.

Der erste Satz war nicht kurz.

„Die Bestimmung der Nährstoffversorgung des Oberbodens erfolgt in der Regel durch die Entnahme einer Mischprobe innerhalb der Bearbeitungstiefe.“

Nikhil hat den Satz dreimal gelesen. Dann hat er einen Stift genommen und die langen Wörter geteilt.

Nährstoff + versorgung. Bearbeitung + s + tiefe. Misch + probe.

Plötzlich war der Satz nicht mehr schwer. Er war nur lang.

Am Abend hat er es Fatma erklärt. Sie hat in der Küche Brot geschnitten.

„Es ist wie im Marathi“, hat er gesagt. „राजपुत्र — das ist der Sohn des Königs, in einem Wort. Deutsch macht dasselbe. Man liest von rechts nach links.“

„Und im Türkischen hängen wir alles hinten an“, hat Fatma gesagt. „Jede Sprache ist faul. Nur auf eine andere Art.“

Nikhil hat gelacht und den Satz noch einmal gelesen. Die Bestimmung der Nährstoffversorgung des Oberbodens.

Drei Genitive hintereinander. In seinem Kopf: तीन षष्ठी, एका ओळीत.

Er hat verstanden.""",
 "gloss":[["leihen","to lend","उसनं देणे"],["die Grundlage","fundamentals","मूलतत्त्वं"],
          ["die Bestimmung","determination","निर्धारण"],["erfolgen","to take place","होणे, घडणे"],
          ["die Entnahme","taking, extraction","काढणे, घेणे"],["teilen","to divide","विभागणे"],
          ["plötzlich","suddenly","अचानक"],["faul","lazy","आळशी"]],
 "mr":"षष्ठी: der Nährstoffversorgung **des** Oberbodens = वरच्या मातीच्या अन्नद्रव्य पुरवठ्याचं. मराठी चा/ची/चे इथे des/der होतं. आणि समास: लांब जर्मन शब्द नेहमी उजवीकडून डावीकडे फोडा, कारण मुख्य शब्द शेवटी असतो — अगदी मराठी तत्पुरुष समासासारखं. Bearbeitungstiefe = मशागतीची खोली. एकदा फोडायची सवय लागली की Fachtext अर्धा सोपा होतो.",
 "q":[["Wie liest man ein langes deutsches Kompositum?",["Von rechts nach links, das Hauptwort steht hinten","Von links nach rechts","Man muss es nachschlagen","Man teilt es in Silben"],0,"Bodenfruchtbarkeit = Fruchtbarkeit des Bodens. Das letzte Element trägt Bedeutung und Genus."],
      ["Was macht „des Oberbodens\“ im Satz?",["Es ist ein Genitiv","Es ist ein Dativ","Es ist das Subjekt","Es ist ein Akkusativ"],0,"des + -s am Nomen: Genitiv, मराठीतलं चा/ची/चे."]]},

{"w":21,"n":7,"title":"Im Labor wird gearbeitet","mr_title":"प्रयोगशाळेत काम चालू आहे","level":"A2",
 "text":"""An der Tür des Labors hängt ein Schild. Nikhil hat es hundertmal gesehen und nie gelesen.

Hier wird mit Chemikalien gearbeitet. Schutzbrille und Kittel werden getragen. Es wird nicht gegessen und nicht getrunken.

Kein „Sie müssen“. Kein „bitte“. Nur: es wird gemacht.

Frau Bergmann hat ihm die Methode erklärt.

„Die Proben werden zuerst luftgetrocknet. Dann werden sie gesiebt — zwei Millimeter. Der Stickstoff wird nach Kjeldahl bestimmt. Die Werte werden in die Tabelle eingetragen, und zwar am selben Tag.“

Nikhil hat mitgeschrieben. Kein einziges Mal „ich“ oder „wir“. Nur die Proben, der Stickstoff, die Werte — und werden.

„Warum sagt man nie, wer es macht?“, hat er gefragt.

Frau Bergmann hat ihn kurz angesehen, wie sie es tut, wenn eine Frage besser ist als erwartet.

„Weil es egal ist, wer es macht. Die Methode muss funktionieren, auch wenn Sie nächstes Jahr nicht mehr hier sind. Das ist keine Höflichkeit, Herr Deshmukh. Das ist Wissenschaft.“

Am Abend hat Nikhil in sein Heft geschrieben, in zwei Sprachen, untereinander:

Der Weizen wird im Oktober gesät.
गहू ऑक्टोबरमध्ये पेरला जातो.

Dieselbe Form. Zwei Sprachen. Und Englisch war bei keiner davon nötig.""",
 "gloss":[["das Schild","sign","फलक"],["der Kittel","lab coat","अंगरखा, लॅब कोट"],
          ["sieben","to sieve","चाळणे"],["bestimmen","to determine","निश्चित करणे"],
          ["eintragen","to enter (data)","नोंदवणे"],["und zwar","and specifically","आणि तेही"],
          ["egal","irrelevant","फरक पडत नाही"],["nötig","necessary","आवश्यक"]],
 "mr":"हा भाग मुद्दाम कर्मणी प्रयोगात लिहिला आहे. werden + Partizip II = मराठी सहायक 'जाणे'. 'Die Proben werden gesiebt' = 'नमुने चाळले जातात.' रचना जुळते, फक्त सहायक क्रियापद वेगळं. जर्मन शास्त्रीय लेखनात कर्ता जवळपास कधीच येत नाही — 'मी केलं' नाही, 'केलं जातं'. तुमच्या प्रबंधाची भाषा हीच असेल, म्हणून हा आठवडा अभ्यासासाठी सर्वात मोलाचा आहे.",
 "q":[["Was heißt „Die Proben werden gesiebt\“?",["नमुने चाळले जातात","आम्ही नमुने चाळतो","नमुने चाळले","नमुने चाळायचे आहेत"],0,"werden + Partizip II ist Vorgangspassiv — क्रिया चालू आहे, कर्ता सांगितलेला नाही."],
      ["Warum benutzt wissenschaftliches Deutsch das Passiv?",["Weil die Methode wichtiger ist als die Person","Aus Höflichkeit","Weil es kürzer ist","Weil es leichter ist"],0,"Frau Bergmanns Antwort: die Methode muss auch ohne dich funktionieren."]]},

{"w":24,"n":8,"title":"Der zweite Winter kommt früh","mr_title":"दुसरा हिवाळा लवकर आला","level":"A2",
 "text":"""Im November wird es um halb fünf dunkel. Im Dezember um vier.

Nikhil hat gemerkt, dass er weniger spricht. Nicht weil er die Wörter nicht hat — er hat jetzt viele Wörter. Sondern weil es anstrengend ist.

Am Telefon hat seine Mutter gefragt, ob er genug isst. Er hat gesagt, dass alles gut ist. Beide haben gewusst, dass das nur halb stimmt.

In der Küche hat Fatma Teig geknetet. Sie hat nicht gefragt, wie es ihm geht. Sie hat gefragt: „Weißt du, was mir im ersten Winter geholfen hat?“

„Nein.“

„Ich habe aufgehört, alles zu verstehen. Im Bus, im Radio, im Supermarkt. Ich habe nur noch einen Satz pro Tag richtig verstanden. Einen. Und den habe ich aufgeschrieben.“

„Und das hat geholfen?“

„Nach vier Monaten hatte ich hundertzwanzig Sätze. Und keine Angst mehr.“

Nikhil hat gefragt, ob sie die Sätze noch hat.

„Natürlich nicht. Das war nicht der Sinn.“

Er ist in sein Zimmer gegangen und hat eine neue Seite aufgeschlagen. Oben hat er geschrieben: Ein Satz pro Tag.

Der erste war von Herrn Krämer, vom Feld, im Oktober:
Der Boden vergisst nichts.""",
 "gloss":[["merken","to notice","लक्षात येणे"],["anstrengend","exhausting","दमवणारं"],
          ["stimmen","to be true","खरं असणे"],["der Teig","dough","कणीक"],
          ["kneten","to knead","मळणे"],["aufhören","to stop","थांबवणे"],
          ["die Angst","fear","भीती"],["der Sinn","point, purpose","हेतू, मुद्दा"]],
 "mr":"अप्रत्यक्ष प्रश्न बघा: 'Sie hat gefragt, ob er genug isst' — 'का' साठी ob, आणि क्रियापद शेवटी. 'Weißt du, was mir geholfen hat?' — प्रश्नशब्द तसाच राहतो पण क्रियापद शेवटी जातं. मराठीत 'तो नीट जेवतो का ते तिने विचारलं' — तिथेही क्रियापद शेवटी. कार्यालयात आणि मुलाखतीत हेच विनम्र रूप वापरायचं आहे: 'Können Sie mir sagen, ob…'",
 "q":[["Was hat Fatma im ersten Winter gemacht?",["Sie hat einen Satz pro Tag aufgeschrieben","Sie hat einen Kurs besucht","Sie ist nach Hause gefahren","Sie hat nur Türkisch gesprochen"],0,"Sie hat aufgehört, alles verstehen zu wollen — und einen Satz pro Tag festgehalten."],
      ["Warum hat sie die Sätze nicht mehr?",["Das Aufschreiben war der Zweck, nicht die Liste","Sie hat sie verloren","Sie waren falsch","Sie hat sie weitergegeben"],0,"„Das war nicht der Sinn\“ — die Gewohnheit war das Ziel."]]},

{"w":27,"n":9,"title":"Die Bewerbung","mr_title":"अर्ज","level":"B1",
 "text":"""Die Ausschreibung hing am schwarzen Brett: Wissenschaftliche Hilfskraft, Fachgebiet Pflanzenernährung, zehn Stunden pro Woche.

Jonas hat darauf gezeigt. „Bewirb dich.“

„Mein Deutsch ist nicht gut genug.“

„Darum geht es nicht. Es geht darum, ob du Proben nehmen kannst, ohne sie zu verwechseln.“

Nikhil hat ihn angesehen. Jonas hat gegrinst.

„Zu früh?“

„Ein bisschen.“

Er hat sich trotzdem beworben. Drei Abende hat er an dem Anschreiben gearbeitet. Er hat sich zuerst über den Lehrstuhl informiert, dann hat er den Text zweimal weggeworfen.

Die erste Version bestand aus Adjektiven: motiviert, zuverlässig, teamfähig. Fatma hat sie gelesen und gefragt, woran man das erkennen soll.

Die dritte Version bestand aus Sätzen wie diesem:

Im Rahmen meiner Bachelorarbeit habe ich 120 Bodenproben selbstständig entnommen, aufbereitet und ausgewertet. Zurzeit betreue ich einen Feldversuch mit vier Varianten und drei Wiederholungen.

Kein einziges Adjektiv. Nur Zahlen und Verben.

Fatma hat genickt. „Jetzt glaube ich es.“

Nikhil hat lange auf den Absenden-Knopf geschaut. Dann hat er darauf gedrückt und ist sofort spazieren gegangen, damit er nicht auf die Antwort warten musste.""",
 "gloss":[["die Ausschreibung","job posting","जाहिरात"],["das schwarze Brett","notice board","सूचना फलक"],
          ["sich bewerben","to apply","अर्ज करणे"],["verwechseln","to mix up","गोंधळ करणे"],
          ["sich informieren über","to find out about","माहिती घेणे"],
          ["im Rahmen","within the scope of","अंतर्गत, चौकटीत"],
          ["entnehmen","to take (a sample)","नमुना घेणे"],["betreuen","to supervise, look after","सांभाळणे"]],
 "mr":"क्रियापद + शब्दयोगी जोड्या: sich bewerben um, sich informieren über, warten auf, zeigen auf. आणि da-रूपं: 'darauf', 'darum geht es' — मराठीतलं 'त्यावर', 'त्याबद्दलच आहे'. वस्तूसाठी da-, माणसासाठी नाही (auf ihn). पण खरा धडा भाषेचा नाही: विशेषणं काढून टाका, आकडे आणि क्रियापदं ठेवा. 'मेहनती आहे' पेक्षा '१२० नमुने स्वतः घेतले' हे जर्मन अर्जात दहापट जास्त वजनदार आहे.",
 "q":[["Warum hat Nikhil die erste Version weggeworfen?",["Sie bestand nur aus Adjektiven ohne Belege","Sie war zu lang","Sie hatte Grammatikfehler","Sie war auf Englisch"],0,"Fatmas Frage — woran erkennt man das? — ist genau der Test für jedes Anschreiben."],
      ["Was heißt „Darum geht es nicht\“?",["That is not the point","That is not allowed","That is not enough","That is not here"],0,"es geht um = it is about. darum = about that, मराठी 'त्याबद्दल'."]]},

{"w":30,"n":10,"title":"Weder Anfänger noch Experte","mr_title":"ना नवशिका, ना तज्ज्ञ","level":"B1",
 "text":"""Die Zusage kam nach elf Tagen. Zwei Zeilen. Nikhil hat sie viermal gelesen.

In der ersten Woche hat Frau Bergmann ihn in ihr Büro gebeten.

„Sie sind jetzt nicht mehr Gast, sondern Mitarbeiter. Das heißt zweierlei. Erstens: Sie dürfen Fragen stellen, so viele Sie wollen. Zweitens: Sie müssen sagen, wenn etwas nicht stimmt — auch wenn ich es gesagt habe.“

„Auch wenn Sie es gesagt haben?“

„Besonders dann. Ich habe zweiundzwanzig Jahre Erfahrung, aber ich war seit April nicht mehr auf dem Feld. Sie waren gestern dort.“

Nikhil hat einen Moment gebraucht.

„Dann sage ich etwas. Die Parzellen am Rand sind anders. Der Boden ist dort trockener, weil das Feld leicht abfällt. Je weiter unten, desto feuchter.“

Frau Bergmann hat sich zurückgelehnt.

„Seit wann wissen Sie das?“

„Seit sechs Wochen. Ich war nicht sicher, ob ich das sagen darf.“

„Sechs Wochen.“ Sie hat es nicht freundlich gesagt, aber auch nicht unfreundlich. „Herr Deshmukh, Ihr Deutsch ist weder perfekt noch ist es Ihr Problem. Ihr Problem ist, dass Sie sechs Wochen gewartet haben. Nicht nur die Grammatik zählt hier, sondern auch der Mut.“

Auf dem Rückweg hat Nikhil gemerkt, dass er den ganzen Satz verstanden hatte — sofort, ohne Umweg über das Englische.""",
 "gloss":[["die Zusage","acceptance","होकार"],["der Gast","guest","पाहुणा"],
          ["zweierlei","two things","दोन गोष्टी"],["abfallen","to slope down","उतार असणे"],
          ["sich zurücklehnen","to lean back","मागे टेकणे"],["der Mut","courage","धाडस"],
          ["der Umweg","detour","वळसा"],["zählen","to count, matter","महत्त्वाचं असणे"]],
 "mr":"जोडगोळी जोडशब्द: 'nicht… sondern', 'weder… noch', 'nicht nur… sondern auch', 'je weiter… desto feuchter'. मराठी: 'ना… ना', 'फक्त… नाही तर… सुद्धा', 'जितकं… तितकं'. हे शब्द B1 चं खरं लक्षण आहेत आणि मराठीतून ते नैसर्गिक वाटतात. 'Je weiter unten, desto feuchter' — पहिल्या भागात क्रियापद शेवटी, दुसऱ्या भागात लगेच. एकदा पाठ केलं की आयुष्यभर पुरतं.",
 "q":[["Was war laut Frau Bergmann Nikhils eigentliches Problem?",["Dass er sechs Wochen geschwiegen hat","Sein Deutsch","Seine Messungen","Seine Arbeitszeiten"],0,"„Nicht nur die Grammatik zählt hier, sondern auch der Mut.\“"],
      ["Was bedeutet „Je weiter unten, desto feuchter\“?",["The further down, the wetter","Sometimes below it is wet","Below it is never wet","It is wet everywhere"],0,"je … desto: मराठी 'जितकं… तितकं'. Der je-Teil ist ein Nebensatz."]]},

{"w":33,"n":11,"title":"Die Aussaat","mr_title":"पेरणी","level":"B1",
 "text":"""Ende März wurde der Boden befahrbar. Herr Krämer hat um halb sechs angerufen.

„Heute. In zwei Stunden. Bringen Sie Gummistiefel mit, die richtigen.“

Der abgetrocknete Boden roch anders als der nasse. Nikhil hat es nicht beschreiben können, nicht auf Deutsch und auch nicht auf Marathi.

Die gereinigte Sämaschine stand schon am Feldrand. Herr Krämer hat sie eingestellt: dreihundertfünfzig keimfähige Körner pro Quadratmeter.

„Und die markierten Parzellen?“

„Die werden per Hand gesät. Deshalb sind Sie hier.“

Vier Stunden. Gebückt, in Reihen, mit einer Schnur als Linie. Die vorbereiteten Tüten waren nummeriert, jede mit einer anderen Variante. Nikhils Rücken hat nach der zweiten Stunde angefangen zu schmerzen und nach der dritten aufgehört, weil er es nicht mehr gemerkt hat.

Um zwei Uhr waren sie fertig. Das gesäte Feld sah aus wie vorher: braun, leer, still.

„Das ist das Komische an dem Beruf“, hat Herr Krämer gesagt und sich eine Zigarette gedreht, die er nicht angezündet hat. „Der wichtigste Tag im Jahr sieht aus wie gar nichts.“

Drei Wochen später ist Nikhil allein zum Feld gefahren. Die auflaufenden Reihen waren dünn, grün und schnurgerade.

Er hat ein Foto gemacht und es seiner Mutter geschickt, ohne Text. Sie hat geantwortet: तू पेरलंस?

Er hat geschrieben: हो. आणि ते उगवलं.""",
 "gloss":[["befahrbar","driveable","गाडी जाण्यायोग्य"],["der Gummistiefel","rubber boot","रबरी बूट"],
          ["riechen","to smell","वास येणे"],["gebückt","bent over","वाकून"],
          ["die Schnur","string, line","दोरी"],["schmerzen","to hurt","दुखणे"],
          ["anzünden","to light","पेटवणे"],["schnurgerade","dead straight","अगदी सरळ"]],
 "mr":"धातुसाधित विशेषणं मोजा: abgetrocknet, gereinigt, markiert, vorbereitet, gesät, auflaufend. मराठीत हे रोजचंच आहे — 'वाळलेली माती', 'साफ केलेलं यंत्र', 'पेरलेलं शेत', 'उगवणाऱ्या ओळी'. Partizip II निष्क्रिय आणि पूर्ण (पेरलेलं), Partizip I सक्रिय आणि चालू (उगवणारं). इंग्रजीत हे कमी लवचिक आहे; मराठीतून तुम्हाला ते आपोआप जमेल.",
 "q":[["Was bedeutet „die auflaufenden Reihen\“?",["The rows that are coming up","The rows that were sown","The rows that ran away","The rows that were harvested"],0,"Partizip I: aktiv und gleichzeitig — मराठी 'उगवणाऱ्या ओळी'."],
      ["Warum sagt Herr Krämer, der wichtigste Tag sehe aus wie nichts?",["Nach der Aussaat sieht das Feld unverändert aus","Weil niemand zusieht","Weil es geregnet hat","Weil die Maschine kaputt war"],0,"„braun, leer, still\“ — die Arbeit ist im Boden, nicht sichtbar."]]},

{"w":36,"n":12,"title":"Zwölf Minuten","mr_title":"बारा मिनिटं","level":"B1",
 "text":"""Das Seminar war auf Deutsch. Zwölf Minuten Vortrag, fünf Minuten Fragen, vierzehn Zuhörer.

Nikhil hat drei Wochen gebraucht, um sich vorzubereiten, und drei Tage, um aufzuhören, den Text auswendig zu lernen. Jonas hatte ihm geraten, das nicht zu tun.

„Wenn du auswendig lernst und ein Wort verlierst, verlierst du alles. Lerne stattdessen die Struktur.“

Also hat Nikhil sechs Sätze auf eine Karte geschrieben, um sich daran festzuhalten, ohne abzulesen.

Er hat um Punkt zehn angefangen.

„Ich möchte Ihnen heute die ersten Ergebnisse aus dem Feldversuch vorstellen. Mein Vortrag gliedert sich in drei Teile.“

Bei Minute vier hat er ein Wort verloren. Statt zu erstarren, hat er den Satz einfach anders gebaut — langsamer, kürzer, mit einem Wort, das er sicher kannte. Niemand hat etwas gemerkt. Er selbst hat es zwei Sekunden lang gemerkt, und dann war es vorbei.

Bei Minute zwölf hat er aufgehört, ohne sich zu entschuldigen.

Die erste Frage kam von Frau Bergmann, und sie war schwierig — natürlich war sie schwierig.

„Darf ich kurz überlegen?“

Zwei Sekunden Stille. Kein Mensch fand das seltsam. In Solapur hätte er es nie gewagt.

Dann hat er geantwortet. Nicht perfekt. Aber es war seine Antwort, in seinen Worten, ohne Umweg.

Beim Hinausgehen hat Jonas ihm auf die Schulter geklopft. „Zwölf Minuten. Ohne Englisch. Weißt du noch, Oktober?“""",
 "gloss":[["der Vortrag","talk, presentation","व्याख्यान"],["raten","to advise","सल्ला देणे"],
          ["auswendig","by heart","पाठ"],["sich festhalten an","to hold on to","आधार घेणे"],
          ["ablesen","to read out","वाचून दाखवणे"],["erstarren","to freeze up","गोठून जाणे"],
          ["seltsam","strange","विचित्र"],["wagen","to dare","धाडस करणे"]],
 "mr":"zu + क्रियापद रचना: 'um sich vorzubereiten', 'ohne abzulesen', 'statt zu erstarren', 'ohne sich zu entschuldigen'. मराठी: 'तयारी करण्यासाठी', 'न वाचता', 'गोठून जाण्याऐवजी'. विभक्त क्रियापदात zu मध्ये घुसतं — vorzubereiten, abzulesen. आणि एक व्यावहारिक धडा: पाठ करू नका, रचना शिका. शब्द हरवला तर वाक्य नव्याने बांधा — हेच खरं B1.",
 "q":[["Warum hat Nikhil aufgehört, den Text auswendig zu lernen?",["Wer auswendig lernt, verliert bei einem Wort alles","Es war zu lang","Jonas hat es verboten","Er hatte keine Zeit"],0,"Jonas' Rat: lerne die Struktur, nicht den Wortlaut."],
      ["Was heißt „ohne sich zu entschuldigen\“?",["without apologising","without asking","without stopping","without preparing"],0,"ohne … zu + Infinitiv, mit dem Reflexivpronomen davor."]]},

{"w":39,"n":13,"title":"Die Kurve","mr_title":"आलेखातली रेषा","level":"B1",
 "text":"""Die Auswertung hat drei Wochen gedauert und am Ende auf eine einzige Abbildung gepasst.

Auf der x-Achse: die vier Düngungsvarianten. Auf der y-Achse: der Kornertrag in Dezitonnen pro Hektar.

Der Ertrag ist von Variante eins bis Variante drei deutlich gestiegen, und zwar um etwa achtzehn Prozent. Zwischen Variante drei und vier ist er dagegen nicht weiter gestiegen, sondern leicht zurückgegangen.

„Erklären Sie mir die Stelle“, hat Frau Bergmann gesagt und auf den Knick gezeigt.

„Mehr Stickstoff bringt bis zu einem Punkt mehr Ertrag. Danach nicht mehr. Die Pflanze kann ihn nicht mehr nutzen, also bleibt er im Boden.“

„Und dann?“

„Dann wird er ausgewaschen. Der Landwirt bezahlt zweimal: einmal für den Dünger und einmal über die Düngeverordnung.“

Frau Bergmann hat nichts gesagt, was für sie viel war.

Später hat Nikhil die Abbildung angeschaut und gemerkt, dass ihn nicht die Zahlen überrascht hatten — die kannte er aus jedem Lehrbuch. Überrascht hat ihn, dass er sie auf Deutsch erklärt hatte, ohne einen einzigen Satz vorher im Kopf zu übersetzen.

Zu Hause hat er den Ordner geöffnet, in dem seine ersten Texte lagen. Oktober, Woche drei: Mein Zimmer ist klein. Es hat ein Bett.

Er hat den Ordner wieder zugemacht. Nicht aus Scham. Aus etwas anderem, für das er in keiner seiner drei Sprachen ein Wort hatte.""",
 "gloss":[["die Abbildung","figure","आकृती"],["die Achse","axis","अक्ष"],
          ["deutlich","clearly, markedly","स्पष्टपणे"],["zurückgehen","to decline","घटणे"],
          ["der Knick","kink, bend","वळण, मोड"],["nutzen","to use","वापरणे"],
          ["auswaschen","to leach out","निचरा होऊन वाहून जाणे"],["die Scham","shame","लाज"]],
 "mr":"आलेख वर्णनाची भाषा: 'ist gestiegen', 'ist zurückgegangen', 'um achtzehn Prozent', 'deutlich', 'leicht', 'dagegen'. एक सापळा लक्षात ठेवा — 'um 18 %' म्हणजे १८ टक्क्यांनी वाढ, 'auf 18 %' म्हणजे १८ टक्क्यांपर्यंत. मराठीतला 'ने' आणि 'पर्यंत' हाच फरक. मुलाखतीत, सेमिनारमध्ये आणि प्रबंधात हीच आठ वाक्यं पुन्हा पुन्हा लागतील.",
 "q":[["Was beschreibt „um 18 % gestiegen\“?",["Ein Anstieg von 18 Prozentpunkten","Ein Anstieg bis auf 18 %","Ein Rückgang","Keine Veränderung"],0,"um = by. auf = to. Der Unterschied wird in Prüfungen gezielt geprüft."],
      ["Warum sinkt der Ertrag nach Variante 3?",["Die Pflanze kann den zusätzlichen Stickstoff nicht mehr nutzen","Es hat zu wenig geregnet","Die Sorte war falsch","Der Boden war verdichtet"],0,"Über dem Optimum bleibt der Stickstoff im Boden und wird ausgewaschen."]]},

{"w":42,"n":14,"title":"Vierzig Minuten, drei Personen","mr_title":"चाळीस मिनिटं, तीन माणसं","level":"B1",
 "text":"""Das Unternehmen züchtet Getreidesorten und sitzt vierzig Bahnminuten entfernt. Die Stelle: Versuchstechniker, befristet auf zwei Jahre, mit Option auf Verlängerung.

Drei Personen im Raum. Frau Ohlsen von der Personalabteilung, ein Züchter, eine Versuchsleiterin.

„Erzählen Sie uns kurz etwas über sich.“

Nikhil hat zwei Minuten gesprochen. Studium, Feldversuch, HiWi-Stelle, warum diese Firma. Er hatte es zwanzigmal geübt, aber nicht auswendig gelernt.

Dann kamen die fachlichen Fragen, und sie waren nicht freundlich gemeint — sie waren einfach Fragen.

„Wie würden Sie einen Sortenversuch anlegen, wenn Ihnen nur ein halber Hektar zur Verfügung steht?“

Er hat über Randeffekte gesprochen, über Wiederholungen, über die Frage, ob vier Sorten mit vier Wiederholungen besser sind als acht Sorten mit zwei.

Die Versuchsleiterin hat zum ersten Mal etwas notiert.

Dann Frau Ohlsen: „Ihre Gehaltsvorstellung?“

In Solapur hätte er gesagt: Was Sie für angemessen halten. Er wusste inzwischen, dass das hier nicht bescheiden klingt, sondern unvorbereitet.

„Meine Gehaltsvorstellung liegt bei zweiundvierzigtausend Euro brutto im Jahr. Falls die Stelle nach Tarif eingruppiert ist, würde ich mich gern daran orientieren.“

Frau Ohlsen hat genickt und etwas geschrieben.

Am Ende die letzte Frage: „Haben Sie noch Fragen an uns?“

Er hatte drei. Er hat alle drei gestellt.

Auf dem Bahnsteig hat er gemerkt, dass er vierzig Minuten lang nicht ein einziges Mal an Grammatik gedacht hatte.""",
 "gloss":[["züchten","to breed","पैदास करणे"],["befristet","fixed-term","मुदतबंद"],
          ["zur Verfügung stehen","to be available","उपलब्ध असणे"],["der Randeffekt","edge effect","कडेचा परिणाम"],
          ["angemessen","appropriate","योग्य"],["bescheiden","modest","विनम्र"],
          ["eingruppiert","classified (pay scale)","वेतनश्रेणीत बसवलेलं"],["sich orientieren an","to go by","आधार घेणे"]],
 "mr":"इथला धडा भाषेपेक्षा संस्कृतीचा आहे. 'तुम्ही ठरवा' हे मराठीत विनम्र वाटतं; जर्मन मुलाखतीत ते तयारीचा अभाव वाटतं. आकडा सांगा, कारण द्या, आणि Tarif चा उल्लेख करा. आणि शेवटच्या प्रश्नाला नेहमी 'हो' — तीन प्रश्न तयार ठेवा. Konjunktiv II ('würde ich mich gern orientieren') इथे विनम्रता देतो, दुर्बलता नाही.",
 "q":[["Warum ist „Was Sie für angemessen halten\“ eine schlechte Antwort?",["Es wirkt unvorbereitet, nicht bescheiden","Es ist unhöflich","Es ist grammatisch falsch","Es ist zu direkt"],0,"In Deutschland erwartet man eine konkrete Zahl mit Begründung."],
      ["Was sollte man auf „Haben Sie noch Fragen?\“ antworten?",["Immer ja, mit vorbereiteten Fragen","Nein, danke","Nur eine Frage zum Urlaub","Das kommt darauf an"],0,"Keine Fragen zu haben liest sich als kein Interesse."]]},

{"w":45,"n":15,"title":"Rechts vor links","mr_title":"उजवीकडचा आधी","level":"B1",
 "text":"""Die Theorieprüfung hat er auf Deutsch gemacht, obwohl sie auf Englisch möglich gewesen wäre.

Jonas hielt das für Angeberei. Nikhil hat es anders begründet: „Der Fahrlehrer spricht Deutsch. Die Schilder sind auf Deutsch. Wenn ich die Prüfung auf Englisch mache, verschiebe ich das Problem nur um drei Monate.“

Er hat sie im ersten Versuch bestanden, mit vier Fehlerpunkten.

Die praktische Prüfung war schlimmer.

„Nächste Kreuzung rechts“, hat der Prüfer gesagt, ohne den Kopf zu heben.

Kein Schild. Rechts vor links.

Von rechts kam nichts. Er ist gefahren.

Zwanzig Minuten später, ein Kreisverkehr, ein Radfahrer im toten Winkel. Nikhil hat den Schulterblick gemacht, den er sechzig Mal geübt hatte, und ist stehen geblieben.

Der Prüfer hat zum ersten Mal den Kopf gehoben.

Nach vierzig Minuten, zurück vor der Fahrschule: „Bestanden.“

Nikhil hat gefragt, ob er etwas falsch gemacht habe.

„Sie haben zweimal zu vorsichtig angefahren. Das legt sich.“

Am Abend hat er den Führerschein fotografiert und nach Hause geschickt. Klasse B.

Sein Vater hat angerufen, was er selten tut. Er hat nur gefragt, ob Nikhil jetzt einen Traktor fahren dürfe.

„Nur bis dreieinhalb Tonnen. Für die großen brauche ich Klasse T.“

Sein Vater hat gelacht. „Also hast du noch etwas zu tun.“

Über die Hälfte der Stellenanzeigen, die Nikhil bis dahin gelesen hatte, verlangte den Führerschein. Ab jetzt fiel keine mehr aus diesem Grund weg.""",
 "gloss":[["die Angeberei","showing off","फुशारकी"],["begründen","to justify","कारण देणे"],
          ["verschieben","to postpone","पुढे ढकलणे"],["der Prüfer","examiner","परीक्षक"],
          ["der tote Winkel","blind spot","अंधळा कोपरा"],["sich legen","to settle down","निवळणे"],
          ["verlangen","to require","मागणी करणे"],["wegfallen","to drop out","गळून पडणे"]],
 "mr":"'obwohl sie auf Englisch möglich gewesen wäre' — obwohl + Konjunktiv II भूतकाळ, एका वाक्यात दोन कठीण गोष्टी. आणि निर्णय बघा: सोपा मार्ग तात्पुरता असतो. परीक्षा इंग्रजीत दिली असती तर प्रशिक्षकाची जर्मन सूचना तशीच अडचण राहिली असती. जिथे जिथे भाषा टाळता येते, तिथे ती टाळल्याने समस्या फक्त पुढे सरकते.",
 "q":[["Warum hat er die Theorieprüfung auf Deutsch gemacht?",["Weil der Fahrlehrer und die Schilder Deutsch sind","Weil Englisch nicht möglich war","Weil es billiger war","Weil Jonas es wollte"],0,"Die englische Prüfung hätte das Problem nur um drei Monate verschoben."],
      ["Was heißt „Das legt sich\“?",["That will settle down with time","That is dangerous","That is forbidden","That was the reason"],0,"sich legen = nachlassen, weggehen. मराठी 'ते निवळेल'."]]},

{"w":48,"n":16,"title":"Der Ordner","mr_title":"ती फाईल","level":"B1",
 "text":"""Das Angebot kam an einem Dienstag: unbefristet nach der Probezeit, Beginn im Oktober.

Nikhil hat es zweimal gelesen und dann etwas getan, das er sich seit Wochen vorgenommen hatte. Er hat den alten Ordner geöffnet.

Ganz unten lag ein Blatt vom Oktober des Vorjahres. Sechs Sätze, in großer Handschrift, mit einem Fehler in jedem zweiten:

Ich heiße Nikhil. Ich komme aus Indien. Ich studiere Landwirtschaft. Mein Zimmer ist klein. Das Wetter ist kalt. Ich lerne Deutsch.

Er hat lange darauf geschaut.

Nachdem er ein Jahr lang jeden Tag etwas auf Deutsch gemacht hatte, waren nicht die Wörter das Auffälligste. Es war, dass er inzwischen auf Deutsch dachte, ohne es zu bemerken — und dass er, wenn er nachdachte, immer noch auf Marathi dachte, aber nicht mehr über den Umweg des Englischen ging.

Fatma hat in die Küche gerufen, ob er mitesse.

Herr Krämer hat eine SMS geschickt: Wann fangen Sie an? Vorher noch eine Ernte, oder?

Frau Bergmann hat drei Zeilen geschrieben, die letzte davon: Melden Sie sich, wenn Sie promovieren wollen.

Nikhil hat das alte Blatt aus dem Ordner genommen und über den Schreibtisch gehängt, dorthin, wo man es beim Arbeiten sieht.

Dann hat er eine neue Seite aufgeschlagen und oben geschrieben, so wie vor einem Jahr, nur ein Wort größer:

B2.""",
 "gloss":[["das Angebot","offer","देऊ केलेलं, प्रस्ताव"],["unbefristet","permanent","कायमस्वरूपी"],
          ["sich etwas vornehmen","to resolve to do something","ठरवणे"],
          ["die Handschrift","handwriting","हस्ताक्षर"],["auffällig","striking","लक्षवेधी"],
          ["bemerken","to notice","लक्षात येणे"],["sich melden","to get in touch","संपर्क करणे"],
          ["promovieren","to do a doctorate","पीएच.डी. करणे"]],
 "mr":"शेवटच्या भागात वर्षभराचं व्याकरण एकत्र आहे: nachdem + Plusquamperfekt, ob-वाक्य, संबंधवाचक वाक्यं, ohne… zu. पण खरा मुद्दा शेवटच्या परिच्छेदात आहे — मराठीतून विचार करणं सोडायचं नाही. फक्त इंग्रजीचा वळसा काढून टाकायचा. वर्ष दोनचं ध्येय: जर्मन वाक्य थेट सुचणं, आणि मराठी विचारांसाठी राखून ठेवणं.",
 "q":[["Was hat sich nach einem Jahr am meisten verändert?",["Er denkt Marathi, aber ohne Umweg über das Englische","Er hat Marathi vergessen","Er denkt nur noch auf Deutsch","Er spricht kein Englisch mehr"],0,"Der vorletzte Absatz sagt es genau so — der Umweg fällt weg, die Muttersprache bleibt."],
      ["Warum steht „Nachdem er … gemacht hatte\“ im Plusquamperfekt?",["nachdem verlangt die frühere Zeitstufe","Es ist ein Passiv","Es ist Konjunktiv","Es ist ein Fehler"],0,"nachdem + Plusquamperfekt im Nebensatz, Perfekt oder Präteritum im Hauptsatz."]]},
]


# ---------------------------------------------------------------------------
# Model texts. Read one, then write your own on the same skeleton.
# ---------------------------------------------------------------------------
ESSAYS = [
{"w":29,"id":"stellungnahme","title":"Stellungnahme: Zwischenfrüchte",
 "mr_title":"मत मांडणी — आंतरपिकं","kind":"Stellungnahme (230 Wörter)",
 "text":"""In den letzten Jahren wird in der deutschen Landwirtschaft viel über Zwischenfrüchte diskutiert. Für die einen sind sie ein zusätzlicher Kostenfaktor, für die anderen ein zentrales Instrument des Bodenschutzes.

Meiner Meinung nach überwiegen die Vorteile deutlich.

Erstens schützen Zwischenfrüchte den Boden im Winter. Eine bedeckte Fläche verliert bei Starkregen erheblich weniger Bodenmaterial als eine offene. Gerade auf Hanglagen ist das ein messbarer Effekt.

Zweitens binden sie Stickstoff, der sonst ausgewaschen würde. Der Nährstoff bleibt damit im System und steht der Folgekultur zur Verfügung. Für den Betrieb ist das nicht nur ökologisch, sondern auch wirtschaftlich sinnvoll.

Zwar entstehen zusätzliche Kosten für Saatgut und eine weitere Überfahrt, und in trockenen Jahren kann eine Zwischenfrucht der Hauptkultur Wasser entziehen. Diese Einwände sind berechtigt. Sie sprechen jedoch nicht gegen Zwischenfrüchte an sich, sondern für eine sorgfältige Wahl der Art und des Aussaattermins.

Aus diesen Gründen bin ich der Ansicht, dass Zwischenfrüchte in den meisten Fruchtfolgen sinnvoll sind. Entscheidend ist nicht die Frage, ob man sie anbaut, sondern welche Art man unter welchen Standortbedingungen wählt.""",
 "mr":"रचना बघा, मजकूर नंतर. सहा भाग: विषय → माझं मत → पहिला मुद्दा + पुरावा → दुसरा मुद्दा + पुरावा → विरोधी मुद्दा मान्य करून त्याचं उत्तर → निष्कर्ष. मराठी निबंधात विरोधी मुद्दा अनेकदा वगळला जातो; जर्मन Stellungnahme मध्ये तो वगळला तर गुण कापले जातात. 'Zwar…, jedoch…' हा त्यासाठीचा साचा आहे.",
 "steal":["In den letzten Jahren wird viel über … diskutiert.",
          "Meiner Meinung nach überwiegen die Vorteile deutlich.",
          "Erstens … Zweitens …",
          "Zwar …, und …. Diese Einwände sind berechtigt. Sie sprechen jedoch nicht gegen …, sondern für …",
          "Aus diesen Gründen bin ich der Ansicht, dass …",
          "Entscheidend ist nicht die Frage, ob …, sondern welche …"]},

{"w":34,"id":"abstract","title":"Abstract: ein eigener Versuch",
 "mr_title":"शोधसारांश","kind":"Wissenschaftliches Abstract (170 Wörter)",
 "text":"""Die vorliegende Untersuchung befasst sich mit dem Einfluss unterschiedlicher Stickstoffgaben auf den Kornertrag von Winterweizen auf einem schluffigen Lehmboden.

Der Feldversuch wurde im Versuchsjahr 2026/27 an einem Standort in Südniedersachsen als randomisierte Blockanlage mit vier Varianten und drei Wiederholungen angelegt. Die Stickstoffgaben betrugen 0, 80, 160 und 240 kg N/ha. Erfasst wurden Bestandesdichte, Kornertrag und Proteingehalt. Die statistische Auswertung erfolgte mittels einfaktorieller Varianzanalyse.

Der Kornertrag stieg bis zu einer Gabe von 160 kg N/ha signifikant an (p < 0,05). Zwischen 160 und 240 kg N/ha wurde dagegen kein weiterer Ertragszuwachs festgestellt, während der Proteingehalt weiter zunahm.

Die Ergebnisse deuten darauf hin, dass unter den vorliegenden Standortbedingungen eine Gabe von etwa 160 kg N/ha ertraglich ausreichend ist. Aufgrund der geringen Zahl an Wiederholungen sind die Ergebnisse jedoch vorsichtig zu interpretieren. Eine mehrjährige Wiederholung des Versuchs erscheint sinnvoll.""",
 "mr":"चार भाग, कडक क्रम: विषय → पद्धत → निकाल → अर्थ आणि मर्यादा. संपूर्ण मजकूर कर्मणीत आहे — 'wurde angelegt', 'erfolgte', 'wurde festgestellt'. 'मी केलं' कुठेच नाही. आणि शेवटचं वाक्य महत्त्वाचं: मर्यादा स्वतः सांगणं जर्मन शास्त्रीय लेखनात दुर्बलता नाही, प्रामाणिकपणा आहे. 'vorsichtig zu interpretieren' हे रूप पाठ करा.",
 "steal":["Die vorliegende Untersuchung befasst sich mit …",
          "Der Feldversuch wurde als randomisierte Blockanlage mit … Varianten und … Wiederholungen angelegt.",
          "Erfasst wurden …",
          "Die statistische Auswertung erfolgte mittels …",
          "Die Ergebnisse deuten darauf hin, dass …",
          "Aufgrund … sind die Ergebnisse jedoch vorsichtig zu interpretieren."]},

{"w":38,"id":"bericht","title":"Feldbericht","mr_title":"क्षेत्र अहवाल","kind":"Bericht (150 Wörter)",
 "text":"""Am 14. Mai 2027 wurde auf dem Versuchsfeld Reinshof eine Bonitur des Winterweizenversuchs durchgeführt. Beteiligt waren zwei Mitarbeitende des Instituts sowie eine studentische Hilfskraft.

Erfasst wurden Bestandesdichte, Wuchshöhe und Krankheitsbefall in allen zwölf Parzellen. Die Bonitur erfolgte nach dem institutseigenen Schema in drei Wiederholungen je Parzelle.

Der Bestand war insgesamt gleichmäßig entwickelt. In den Parzellen 3 und 7 wurde ein beginnender Befall mit Gelbrost festgestellt. Der Befallsgrad lag in beiden Fällen unter fünf Prozent und damit unterhalb der Schadschwelle.

Am Feldrand wurden auf einer Länge von etwa zwanzig Metern Fahrspuren aus der Vorjahresernte sichtbar. Der Bestand ist dort deutlich schwächer entwickelt.

Eine Behandlung war zum Zeitpunkt der Bonitur nicht erforderlich. Eine erneute Kontrolle wird für den 28. Mai vorgeschlagen. Die betroffenen Randparzellen sollten bei der Auswertung gesondert betrachtet werden.""",
 "mr":"अहवालाचा साचा: काय-कुठे-कधी → कोण → पद्धत → निरीक्षण → विशेष नोंद → शिफारस. काळ भूतकाळ, आवाज कर्मणी, मत शून्य. मराठी अहवालातही हेच अपेक्षित असतं, पण जर्मनमध्ये 'मला वाटतं' असं एक वाक्यही आलं तर तो अहवाल राहत नाही. शिफारस मात्र शेवटी स्पष्ट लिहायची — 'wird vorgeschlagen', 'sollten … betrachtet werden'.",
 "steal":["Am … wurde auf … eine … durchgeführt. Beteiligt waren …",
          "Erfasst wurden …",
          "Die … erfolgte nach … in drei Wiederholungen.",
          "In den Parzellen … wurde … festgestellt.",
          "Eine Behandlung war zum Zeitpunkt der Bonitur nicht erforderlich.",
          "Eine erneute Kontrolle wird für den … vorgeschlagen."]},

{"w":40,"id":"anschreiben","title":"Anschreiben: Versuchstechniker",
 "mr_title":"अर्जपत्र","kind":"Anschreiben (250 Wörter)",
 "text":"""Betreff: Bewerbung als Versuchstechniker im Bereich Getreidezüchtung, Referenznummer 2027-114

Sehr geehrte Frau Ohlsen,

in Ihrer Ausschreibung suchen Sie eine Person, die Feldversuche eigenständig betreut, Bonituren durchführt und Daten aufbereitet. Genau das ist die Arbeit, die ich seit zwei Jahren mache.

Als wissenschaftliche Hilfskraft am Lehrstuhl für Pflanzenernährung betreue ich einen Stickstoffversuch mit vier Varianten und drei Wiederholungen. Ich habe die Parzellen mit angelegt, über eine Vegetationsperiode boniturt und rund 160 Bodenproben entnommen, aufbereitet und ausgewertet. Die statistische Auswertung habe ich in R durchgeführt und die Ergebnisse im Institutsseminar auf Deutsch vorgestellt.

Zusätzlich arbeite ich seit anderthalb Jahren regelmäßig auf einem landwirtschaftlichen Betrieb in der Region mit. Dort habe ich gelernt, wie unterschiedlich sich Termine im Versuchsplan und Termine auf dem Acker anfühlen — und wie man beides zusammenbringt.

Mein Bachelorstudium habe ich in Indien im Fach Bodenkunde abgeschlossen; derzeit studiere ich Nachhaltige Internationale Landwirtschaft im Master. Diese Kombination bringt einen Blick mit, der in einem Züchtungsunternehmen nützlich sein kann: Ich kenne Anbausysteme unter sehr unterschiedlichen Wasser- und Temperaturbedingungen.

Ich besitze den Führerschein der Klasse B und kann ab dem 1. Oktober beginnen.

Über die Gelegenheit, mich persönlich vorzustellen, würde ich mich sehr freuen.

Mit freundlichen Grüßen
Nikhil Deshmukh

Anlagen: Lebenslauf, Zeugnisse, Arbeitsproben""",
 "mr":"पहिलं वाक्य सर्वात महत्त्वाचं: 'तुम्हाला हे हवं आहे — मी नेमकं तेच करतो.' स्वतःपासून सुरुवात करू नका, त्यांच्या गरजेपासून करा. विशेषणं जवळपास शून्य आहेत; आकडे भरपूर — १६० नमुने, चार varianten, तीन wiederholungen. मराठी/भारतीय अर्जांत नम्रतेसाठी अस्पष्ट भाषा वापरली जाते; जर्मनीत ती दुर्लक्षित होते. आणि भारतातलं शिक्षण कमीपणा म्हणून नाही, वेगळा दृष्टिकोन म्हणून मांडा — इथे तेच केलं आहे.",
 "steal":["In Ihrer Ausschreibung suchen Sie eine Person, die … Genau das ist die Arbeit, die ich seit … mache.",
          "Als … betreue ich …",
          "Ich habe … entnommen, aufbereitet und ausgewertet.",
          "Diese Kombination bringt einen Blick mit, der … nützlich sein kann.",
          "Ich besitze den Führerschein der Klasse B und kann ab dem … beginnen.",
          "Über die Gelegenheit, mich persönlich vorzustellen, würde ich mich sehr freuen."]},

{"w":46,"id":"zusammenfassung","title":"Zusammenfassung eines Fachartikels",
 "mr_title":"लेखाचा सारांश","kind":"Zusammenfassung (160 Wörter)",
 "text":"""Der Artikel „Zwischenfrüchte in trockenen Jahren“ von Hoffmann, erschienen 2026 in einer landwirtschaftlichen Fachzeitschrift, behandelt die Frage, ob der Zwischenfruchtanbau bei zunehmender Frühjahrstrockenheit weiterhin sinnvoll ist.

Der Autor stellt zunächst dar, dass Zwischenfrüchte Bodenerosion verringern und Nährstoffe binden. Anschließend weist er darauf hin, dass sie dem Boden gleichzeitig Wasser entziehen, das der Hauptkultur im Frühjahr fehlen kann.

Als Lösung schlägt er einen früheren Termin für die Beseitigung des Bestandes vor. Nach seinen Angaben lässt sich der Wasserverbrauch dadurch deutlich senken, ohne dass die Schutzwirkung verloren geht.

Abschließend kommt der Autor zu dem Schluss, dass nicht der Zwischenfruchtanbau selbst, sondern dessen Management über den Erfolg entscheidet. Er empfiehlt, die Artenwahl stärker an den Standort anzupassen.""",
 "mr":"सारांशाचे नियम: वर्तमानकाळ, स्वतःचे शब्द, अवतरण नाही, स्वतःचं मत नाही. पहिल्या वाक्यात शीर्षक + लेखक + वर्ष + विषय, चारही. मग 'zunächst… anschließend… abschließend' या तीन शब्दांवर पूर्ण रचना उभी राहते. आणि 'Nach seinen Angaben' — म्हणजे हे लेखकाचं म्हणणं आहे, माझं नाही. हे अंतर ठेवणं जर्मन शैक्षणिक लेखनात अनिवार्य आहे.",
 "steal":["Der Artikel „…\“ von …, erschienen … in …, behandelt die Frage, ob …",
          "Der Autor stellt zunächst dar, dass …",
          "Anschließend weist er darauf hin, dass …",
          "Als Lösung schlägt er … vor.",
          "Nach seinen Angaben lässt sich … senken, ohne dass …",
          "Abschließend kommt der Autor zu dem Schluss, dass …"]},
]
