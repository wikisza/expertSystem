from flask import Flask, render_template, request
from durable.lang import *

Dane="ss"


app = Flask(__name__)

with ruleset('FilmCzySerial'):
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Przed'))
    def Series24(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': '24 (2001-2010)', 'opis': 'Walka z czasem w stylu thrillera, każdy odcinek to jedna godzina akcji.', 'zdj': 'zdj24.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Po') & (m.opisAkcjaS == 'Zemsta, brutalna przemoc, moralne dylematy antybohatera'))
    def ThePunisher(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Punisher (2017-2019)', 'opis': 'Brutalna opowieść o zemście i sprawiedliwości.', 'zdj': 'punisher.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Po') & (m.opisAkcjaS == 'Superbohater bez nadprzyrodzonych mocy, lucznictwo, tajemnicze watki'))
    def Arrow(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Arrow (2012-2020)', 'opis': 'Bohater walczący z przestępczością w zielonym kapturze.', 'zdj':'arrow.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'SciFi') & (m.premiera2015 == 'Przed'))
    def BlackMirror(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Black Mirror (2011-obecnie)', 'opis': 'Dystopijne historie o wpływie technologii na życie.' , 'zdj':'blackmirror.jpg'})

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'SciFi') & (m.premiera2015 == 'Po') & (m.opisSciFiS == 'Lata 80, dzieci kontra nadprzyrodzone sily, nostalgia za dawnymi czasami'))
    def StrangerThings(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Stranger Things (2016-obecnie)', 'opis': 'Tajemnice, potwory i dzieci w latach 80.', 'zdj':'strangerthings.jpg'})

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'SciFi') & (m.premiera2015 == 'Po') & (m.opisSciFiS == 'Przestrzen kosmiczna, polityczne intrygi, wojny miedzy planetami'))
    def TheExpanse(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Expanse (2015-2021)', 'opis': 'Konflikty polityczne w kosmosie.' , 'zdj':'expanse.jpg'})

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Fantasy') & (m.premiera2015 == 'Przed'))
    def GameOfThrones(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Game of Thrones (2011-2019)', 'opis': 'Walka o tron pełna zdrad i intryg.', 'zdj':'gameof.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Fantasy') & (m.premiera2015 == 'Po') & (m.opisFantasyS == 'Opowiesci o wiedzminie, potwory, magia, moralne wybory bohaterow'))
    def TheWitcher(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Witcher (2019-obecnie)', 'opis': 'Wiedźmin Geralt poluje na potwory w fantastycznym świecie.', 'zdj':'witcher.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Fantasy') & (m.premiera2015 == 'Po') & (m.opisFantasyS == 'Rownolegle swiaty, mloda dziewczyna na misji, zwierzece daemony'))
    def HisDarkMaterials(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'His Dark Materials (2019-2022)', 'opis': 'Magia, nauka i równoległe światy.', 'zdj': 'hisdarkmaterials.jpg'})

    #horror
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Horror') & (m.premiera2015 == 'Przed') & (m.opisHorrorS == 'Antologia horroru, rozne sezony z roznymi historiami, mroczne tematy.'))
    def AmericanHorrorStory(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'American Horror Story (2011-obecnie)', 'opis': 'Antologia horroru z różnymi historiami.' , 'zdj': 'american.jpg'})

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Horror') & (m.premiera2015 == 'Przed') & (m.opisHorrorS == 'Swiat opanowany przez zombie, walka o przetrwanie, rozpad spoleczenstwa.'))
    def TheWalkingDead(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Walking Dead (2010-2022)', 'opis': 'Przetrwanie w świecie opanowanym przez zombie.' , 'zdj': 'walking.jpg'})
    
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Horror') & (m.premiera2015 == 'Po'))
    def TheHauntingofHillHouse(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Haunting of Hill House (2018)', 'opis': 'Rodzinne traumy i nawiedzony dom.' , 'zdj': 'haunting.jpg'})

    #komedia
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Przed') & (m.opisKomediaS == 'Humor w miejscu pracy, mockument, codzienne problemy w biurze.'))
    def TheOffice(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Office (US) (2005-2013)', 'opis': 'Komedia o codziennym życiu w biurze.', 'zdj': 'theoffice.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Przed') & (m.opisKomediaS == 'Zycie urzednikow lokalnych, absurdalny humor, pozytywna energia.'))
    def ParksAndRecreation(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Parks and Recreation (2009-2015)', 'opis': 'Życie urzędników miejskich z humorem.', 'zdj':'parks.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Po'))
    def Brooklyn99(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Brooklyn Nine-Nine (2013-2021)', 'opis': 'Zabawy w policyjnym komisariacie.', 'zdj': 'brooklyn.jpg' })

    #dramat
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Dramat') & (m.premiera2010 == 'Po') & (m.opisDramatS == 'Historia brytyjskiej monarchii, polityka i prywatne Zycie krolowej Elzbiety II'))
    def TheCrown(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Crown (2016 - obecnie)', 'opis': 'Historia życia królowej Elżbiety II.', 'zdj':'crown.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Dramat') & (m.premiera2010 == 'Po') & (m.opisDramatS == 'Rodzinne konflikty w wielkim imperium medialnym, walka o wladze, psychologiczne napiecia.'))
    def Succession(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Succession (2018 - 2023)', 'opis': 'Rodzinne konflikty o przejęcie medialnego imperium.', 'zdj':'succession.jpg'  })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Dramat') & (m.premiera2010 == 'Przed'))
    def BreakingBad(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Breaking Bad (2008 - 2013)', 'opis': 'Nauczyciel chemii staje się dilerem narkotyków.', 'zdj':'breaking.jpg' })

    #thiller
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Thiller') & (m.premiera2015 == 'Po') & (m.opisThillerS == 'Profilowanie seryjnych mordercow, poczatki badan nad psychika przestepcow, oparty na prawdziwych wydarzeniach.'))
    def Mindhunter(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Mindhunter (2017 - 2019)', 'opis': 'Profilowanie seryjnych morderców przez FBI.', 'zdj':'mindhunter.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Thiller') & (m.premiera2015 == 'Po') & (m.opisThillerS == 'Manipulacja, obsesyjna milosc, niepokojacy portret psychologiczny.'))
    def You(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'You (2018 - obecnie)', 'opis': 'Obsesyjna miłość prowadzi do niebezpiecznych działań.', 'zdj':'you.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Thiller') & (m.premiera2015 == 'Przed'))
    def TrueDetective(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'True Detective (2014 - obecnie)', 'opis': 'Mroczne kryminały w antologicznej formie.', 'zdj':'detective.jpg' })

    #animacja
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Animacja') & (m.premiera2010 == 'Po') & (m.opisAnimacjaS == 'Podroze miedzy wymiarami, czarny humor, filozoficzne zagadnienia.'))
    def RickAndMorty(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Rick and Morty (2013-obecnie)', 'opis': 'Szalone przygody dziadka naukowca i wnuka. ', 'zdj':'rick.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Animacja') & (m.premiera2010 == 'Po') & (m.opisAnimacjaS == 'Animowany Swiat zwierzat, depresja, satyra na Hollywood.'))
    def BoJackHorseman(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'BoJack Horseman (2014 - 2020)', 'opis': 'Animowany dramat o upadłej gwieździe.', 'zdj':'bojack.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Animacja') & (m.premiera2010 == 'Przed'))
    def Avatar(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Avatar: The Last Airbender (2005-2008)', 'opis': 'Epicka podróż młodego Avatara.', 'zdj':'avatar.jpg' })

    #romans
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Romans') & (m.premiera2015 == 'Po') & (m.opisRomansS == 'XIX-wieczny Londyn, romans, intrygi w wyzszych sferach, wizualne bogactwo.'))
    def Bridgerton(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Bridgerton (2020-obecnie)', 'opis': 'Romansy i intrygi w XIX-wiecznym Londynie.', 'zdj':'bridgerton.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Romans') & (m.premiera2015 == 'Po') & (m.opisRomansS == 'Intymna historia milosci i dojrzewania, relacje mlodych ludzi, emocjonalna glebia.'))
    def NormalPeople(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Normal People (2020)', 'opis': 'Miłosna relacja pełna emocji i komplikacji.', 'zdj':'normal.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Romans') & (m.premiera2015 == 'Przed'))
    def Outlander(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Outlander (2014-obecnie)', 'opis': 'Miłość i przygody w podróżach przez czas.', 'zdj':'outlander.jpg' })

    #kryminał
    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Kryminal') & (m.premiera2015 == 'Po') & (m.opisKryminalS == 'Historia Pabla Escobara i karteli narkotykowych w Kolumbii, brutalna rzeczywistosc przestepcza.'))
    def Narcos(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Narcos (2015-2017)', 'opis': 'Historia Pabla Escobara i walki z narkobiznesem.', 'zdj':'narcos.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Kryminal') & (m.premiera2015 == 'Po') & (m.opisKryminalS == 'Historia prawnika w swiecie przestepczym, prequel Breaking Bad, moralne dylematy.'))
    def BetterCallSaul(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Better Call Saul (2015-2022)', 'opis': 'Prequel o prawniczych początkach Saula Goodmana.', 'zdj':'better.jpg' })

    @when_all((m.preferowanyTyp == 'Serial') & (m.gatunek == 'Kryminal') & (m.premiera2015 == 'Przed'))
    def Sherlock(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Sherlock (2010-2017)', 'opis': 'Współczesna interpretacja genialnego detektywa.', 'zdj':'sherlock.jpg' })

    ##   filmy

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Przed'))
    def DieHard(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Die hard (1998)', 'opis': 'Klasyczny film akcji z pojedynkiem w wieżowcu.', 'zdj':'diehard.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Po') & (m.opisAkcjaF == 'Postapokaliptyczny Swiat, szybkie poscigi samochodowe, minimalistyczny dialog.'))
    def MadMax(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Mad Max: Fury Road(2015)', 'opis': 'Postapokaliptyczna pogoń przez pustynię.', 'zdj':'madmax.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Akcja') & (m.premiera2010 == 'Po') & (m.opisAkcjaF == 'Wysoce stylizowana przemoc, mistrzowskie sekwencje walki, zemsta za smierc psa.'))
    def JohnWick(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'John Wick (2014)', 'opis': 'Zemsta i brawurowe sceny walki.', 'zdj':'john.jpg' })

    # SciFi
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'SciFi') & (m.premiera2011 == 'Przed'))
    def Inception(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Inception (2010)', 'opis': 'Sny w snach i kradzież tajemnic.', 'zdj':'inception.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'SciFi') & (m.premiera2011 == 'Po') & (m.opisSciFiF == 'Cyberpunkowy Swiat, pytania o nature czlowieczenstwa, wciagajaca wizualnie scenografia.'))
    def BladeRunner(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Blade Runner 2049 (2017)', 'opis': 'Filozoficzna opowieść o androidach.', 'zdj':'blade.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'SciFi') & (m.premiera2011 == 'Po') & (m.opisSciFiF == 'Podroze kosmiczne, paradoksy czasowe, emocjonalna historia ojca i corki.'))
    def Interstellar(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Interstellar (2014)', 'opis': 'Podróż w kosmosie w poszukiwaniu nadziei.', 'zdj':'interstellar.jpg' })

    # fantasy
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Fantasy') & (m.premiera2005 == 'Po'))
    def PansLabyrinth(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Pans Labyrinth (2006)', 'opis': 'Mroczna baśń w Hiszpanii czasów wojny.', 'zdj':'pan.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Fantasy') & (m.premiera2005 == 'Przed') & (m.opisFantasyF == 'Epicka podroz, magia, przyjazn i lojalnosc.'))
    def TheLordOfTheRings(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Lord of the Rings (2001)', 'opis': 'Walka o zniszczenie pierścienia w Śródziemiu.', 'zdj':'lord.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Fantasy') & (m.premiera2005 == 'Przed') & (m.opisFantasyF == 'Swiat magii, mlodziez w szkole czarodziejow, walka dobra ze zlem.'))
    def HarryPotter(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Harry Potter and the Sorcerers Stone (2001)', 'opis': 'Początek przygody w świecie magii.', 'zdj':'harry.jpg' })

    # horror
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Horror') & (m.premiera2010 == 'Po') & (m.opisHorrorF == 'Powolne budowanie napiecia, trauma rodzinna, nadnaturalne elementy.'))
    def Hereditary(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Hereditary (2018)', 'opis': 'Rodzinna tragedia w atmosferze grozy.', 'zdj':'hereditary.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Horror') & (m.premiera2010 == 'Po') & (m.opisHorrorF == 'Cisza jako element przetrwania, rodzinne wiezi, groza zwiazana z nieznanym zagrozeniem.'))
    def AQuietPlace(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'A Quiet Place (2018)', 'opis': 'Przetrwanie w świecie ciszy.', 'zdj':'place.jpg' })
    
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Horror') & (m.premiera2010 == 'Przed'))
    def TheExorcist(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Exorcist (1973)', 'opis': 'Kultowy horror o opętaniu.', 'zdj':'exorcist.jpg' })

    # komedia
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Przed') & (m.opisKomediaF == 'Petla czasowa, humor egzystencjalny, rozwoj bohatera.'))
    def GroundhogDay(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Groundhog Day (1993)', 'opis': 'Powtarzający się dzień zmienia życie.', 'zdj':'day.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Przed') & (m.opisKomediaF == 'Przygody nastolatkow, humor niepoprawny, przyjazn i dojrzewanie.'))
    def Superbad(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Superbad (2007)', 'opis': 'Szalona komedia o nastoletnich przygodach.', 'zdj':'superbad.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Komedia') & (m.premiera2010 == 'Po'))
    def TheGrandBudapestHotel(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Grand Budapest Hotel (2014)', 'opis': 'Barwna komedia o ekscentrycznym hotelu.', 'zdj':'hotel.jpg' })

    #dramat
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Dramat') & (m.premiera1960 == 'Po') & (m.opisDramatF == 'Rodzinne intrygi, mafia, klasyczne dialogi.'))
    def TheGodfather(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Godfather (1972)', 'opis': 'Klasyka o mafijnym imperium.', 'zdj':'godfather.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Dramat') & (m.premiera1960 == 'Po') & (m.opisDramatF == 'Holocaust, moralna przemiana bohatera, czarno-biala stylistyka.'))
    def ShindlersList(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Shindlers List (1993)', 'opis': 'Poruszająca opowieść o Holokauście.', 'zdj':'list.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Dramat') & (m.premiera1960 == 'Przed'))
    def Movie12AngryMan(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': '12 Angry Man (1957)', 'opis': 'Dramat sądowy w pokoju narad.', 'zdj':'angry.jpg' })

    #thiller
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Thiller') & (m.premiera2000 == 'Przed') & (m.opisThillerF == 'Seryjny morderca, atmosfera mroku i zagadki, analiza grzechow glownych.'))
    def Se7en(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Se7en (1995)', 'opis': 'Mroczny thriller o seryjnym mordercy.', 'zdj':'seven.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Thiller') & (m.premiera2000 == 'Przed') & (m.opisThillerF == 'Relacja miedzy sledcza a morderca, psychologia zla, niezapomniane dialogi.'))
    def TheSilenceOfTheLambs(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Silence of the Lambs (1991)', 'opis': 'Psychologiczna gra z Hannibalem Lecterem.', 'zdj':'silence.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Thiller') & (m.premiera2000 == 'Po'))
    def GoneGirl(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Gone Girl (2014)', 'opis': 'Zniknięcie, które kryje mroczne sekrety.', 'zdj':'gone.jpg' })

    #animacja
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Animacja') & (m.premiera2001 == 'Po') & (m.opisAnimacjaF == 'Swiat duchow, symbolika, magiczna przygoda.'))
    def SpiritedAway(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Spirited Away (2001)', 'opis': 'Magiczna podróż dziewczynki w świat duchów.', 'zdj':'spirited.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Animacja') & (m.premiera2001 == 'Po') & (m.opisAnimacjaF == 'Przelamywanie stereotypow bajkowych, humor dla dzieci i doroslych, oryginalne postacie'))
    def Shrek(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Shrek (2001)', 'opis': 'Baśń na opak z zabawnym ogram.', 'zdj':'shrek.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Animacja') & (m.premiera2001 == 'Przed'))
    def ToyStory(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Toy Story (1995)', 'opis': 'Ożywione zabawki w wielkiej przygodzie.', 'zdj':'toy.jpg' })

    #romans
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Romans') & (m.premiera2010 == 'Przed') & (m.opisRomansF == 'Relacje spoleczne, milosc powolnie budowana, napiecie romantyczne.'))
    def PridePrejudice(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Pride & Prejudice (2005)', 'opis': 'Klasyczna historia miłości i uprzedzeń.', 'zdj':'pride.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Romans') & (m.premiera2010 == 'Przed') & (m.opisRomansF == 'Milosc na przestrzeni lat, emocjonalna narracja, klasyczne sceny romantyczne.'))
    def TheNotebook(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Notebook (2004)', 'opis': 'Wzruszająca opowieść o wielkiej miłości.', 'zdj':'notebook.jpg'  })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Romans') & (m.premiera2010 == 'Po'))
    def LaLaLand(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'La La Land (2016)', 'opis': 'Miłość i przygody w podróżach przez czas.', 'zdj':'land.jpg' })

    #kryminał
    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Kryminal') & (m.premiera2000 == 'Przed') & (m.opisKryminalF == 'Nielinowa narracja, stylizowane dialogi, czarny humor.'))
    def PulpFiction(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Pulp Fiction (1994)', 'opis': 'Kultowy, niekonwencjonalny film gangsterski.', 'zdj':'pulp.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Kryminal') & (m.premiera2000 == 'Przed') & (m.opisKryminalF == 'Zmagania policjantow i zlodziei, poscigi, moralne dylematy.'))
    def Heat(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'Heat (1995)', 'opis': 'Pojedynek policjanta z geniuszem zbrodni.', 'zdj':'heat.jpg' })

    @when_all((m.preferowanyTyp == 'Film') & (m.gatunek == 'Kryminal') & (m.premiera2000 == 'Po'))
    def TheDeparted(c):
        c.assert_fact({ 'rekomendacja': c.m.rekomendacja, 'wynik': 'The Departed (2006)', 'opis': 'Intrygi i zdrady w policji i mafii.', 'zdj':'departed.jpg' })

    @when_all(+m.rekomendacja)
    def output(c):
        #print('Propozycja: {0}.{1} Opis filmu: {2}'.format(c.m.rekomendacja, c.m.wynik, c.m.opis, c.m.zdj))
        global Dane
        #Dane=""+('Propozycja: {0}.{1} Opis filmu: {2}'.format(c.m.rekomendacja, c.m.wynik, c.m.opis))
        Dane = [
        "Propozycja: " + c.m.rekomendacja,
        c.m.wynik,
        c.m.opis,
        c.m.zdj
        ]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        preferowany_typ = request.form.get('preferowanyTyp')
        gatunek = request.form.get('gatunek')
        premiera = request.form.get('premiera')
        opis = request.form.get('opis')
        
        post('FilmCzySerial',{'rekomendacja': '1', 'preferowanyTyp': preferowany_typ, 'gatunek': gatunek, 'premiera2010': premiera, 'premiera2015': premiera, 'premiera2011':premiera,'premiera2005':premiera,'premiera1960':premiera,'premiera2000':premiera,'premiera2001':premiera,'opisAkcjaS':opis,'opisSciFiS':opis,'opisFantasyS':opis,'opisHorrorS':opis,'opisKomediaS':opis,'opisDramatS':opis,'opisThillerS':opis,'opisAnimacjaS':opis,'opisRomansS':opis,'opisKryminalS':opis,'opisAkcjaF':opis,'opisSciFiF':opis,'opisFantasyF':opis,'opisHorrorF':opis,'opisKomediaF':opis,'opisDramatF':opis,'opisThillerF':opis,'opisAnimacjaF':opis,'opisRomansF':opis,'opisKryminalF':opis});
        return render_template('results.html', wynik=Dane)
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
