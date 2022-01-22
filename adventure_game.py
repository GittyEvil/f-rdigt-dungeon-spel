# Imports
from math import e
import random
from re import L
from sre_constants import RANGE_UNI_IGNORE
import sys
import time
from time import sleep
from turtle import right
from typing import MutableMapping
from unittest import case

# Definierar globala variabler som jag sedan använder genom hela koden
guldmynt = 0
enemy = ""
aDamage = 0
uDamage = 0
health = 0
mana = 0
damage = 0 
char = ""
ryggsäck=[]
    
# Skapar funktionen start
def start(): #backstory
    # Använder globala variabler och uppdaterar deras värde genom return
    global health
    global aDamage
    global uDamage
    global mana
    global damage
    print("Du slogs mot en stor drake men började förlora..")
    sleep(1)
    print("Du försöker fly så fort som möjligt och hittar en grotta..")
    sleep(1)
    print("Du tar dig in i grottan där du är säker men kan inte ta dig ut för där vaktar draken..")
    sleep(1)
    print("vilken klass vill du välja.. Det finns 4 klasser att välja på:tank, krigare, magiker och jägare.")
    
    # Ställer en fråga till användaren (input)
    character=input(">")
    character=character.lower()
    # Beroende på vilken klass användaren väljer kommer de globala variablerna att uppdateras till olika värden
    if character == "tank":
        print("du har valt klassen tank.")
        sleep(1)
        statistics = """         
                  TANK
        ************************
         HP: 200
         AD: 20 
         MANA: 100
         ABILITY: AXETHROW 
         ULTIMATE: AXEFURY
         WEAPON: GAMMAL ROSTIG YXA
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 50
        uDamage = 100
        health = 500
        mana = 100
        damageC = 20
        damage = damage + damageC
        return mana, health, aDamage, damage, uDamage

    if character == "krigare":
        print("du har valt klassen krigare.")
        sleep(1)
        statistics = """         
                 KRIGARE
        ************************
         HP: 150
         AD: 35
         MANA: 100
         ABILITY: SWORDSPIN
         ULTIMATE: FATE SEALED
         WEAPON: GAMMAL ROSTIG SVÄRD
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 50
        uDamage = 100
        health = 300
        mana = 100
        damageC = 40
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage

    if character == "magiker":
        print("du har valt klassen magiker.")
        sleep(1)
        statistics = """         
                MAGIKER
        ************************
         HP: 100
         AD: 20 
         MANA: 200
         ABILITY: FIREBALL
         ULTIMATE: PRIMORDIAL BUSRT
         WEAPON: TRÄPINNE
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 80
        uDamage = 700
        health = 250
        mana = 200
        damageC = 30
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage

    if character == "jägare":
        print("du har valt klassen jägare.")
        sleep(1)
        statistics = """         
                 JÄGARE
        ************************
         HP: 100
         AD: 50
         MANA: 200
         ABILITY: QUICKSHOT
         ULTIMATE: CROSSBOW
         WEAPON: GAMMAL PILBÅGE
        ************************          
        """
        print(statistics)
        sleep(2)
        aDamage = 60
        uDamage = 120
        health = 250
        mana = 200
        damageC = 45
        damage = damage + damageC
        return mana, health, damage, aDamage, uDamage
    else:
        # Ifall användaren skriver in ett värde som inte tas emot ställs frågan igen 
        print("Du måste välja en utav klasserna!")
        character=input(">")
        character=character.lower()

# Funktionen guldrum
def guldrum(): #själva guldrummet
    global guldmynt
    global ryggsäck
    global damage
    print("du är nu i guldrummet..")
    sleep(1)
    print("rummet är upplyst och du ser en guldkista mitt i rummet..")
    sleep(1)
    print("du känner dig säker när du går in..")
    sleep(1)
    print("rummet är mycket dammigt och det ser ut som om rummet har varit övergivet väldigt länge..")
    sleep(1)
    print("vill du gå fram till guldkistan?('ja' eller 'nej')")
    guldkista=input(">")
    guldkista=guldkista.lower()
    print(guldkista)
    if guldkista == "ja":
        print("du står nu framför guldkistan.") 
        sleep(1)
        print("vill du öppna guldkistan?")
        öppnakista=input(">")
        öppnakista=öppnakista.lower()
        print(öppnakista)
        if öppnakista == "ja":
            print("i kistan så ligger det några guldmynt och en bok med konstiga symboler på")
            sleep(1)
            print("vill du ta upp boken och guldmynten?")
            kistaitems=input(">")
            kistaitems=kistaitems.lower()
            print(kistaitems)
            if kistaitems == "ja":
                print("du tar upp den konstiga boken och 200 guldmynt..")
                sleep(1)
                print("Du bläddrar igenom boken fort..")
                sleep(1)
                print("Plötsligt börjar symbolerna på boken att glänsa och du känner dig starkare...")
                sleep(1)
                print("*Boken du hittat är en rune-bok som gör dig starkare!*")
                sleep(1)
                print("*Genom att ta upp rune-böcker under speletsgång kommer du att göra mer skada med dina vanliga attack*")
                guldmynt = guldmynt + 200
                print("vill du gå ut ur rummet?")
                gåut=input(">")
                gåut=gåut.lower()
                if gåut == "ja":
                    print("Du befinner dig i första rummet, du kan antingen gå åt höger(gå höger) eller framåt för fight tutorial (gå framåt)")
                    question=input(">")
                    question=question.lower()
                    if question == "gå framåt":
                        sleep(2)
                        lootrum()
                        return guldmynt
                    elif question == "gå höger":
                        sleep(2)
                        bosskoridor()
                        return guldmynt
                    else:
                        print("Det verkar inte finnas något sånt att göra i rummet..")
                        sleep(2)
                        print("höger(gå höger) eller framåt(gå framåt)")
                        question=input(">")
                        question=question.lower()
                if gåut == "nej":
                    print("du står kvar och stirrar på en stängd guldkista..")
                    sleep(1)
                    print("Plötsligt ser du kistan röra på sig...")
                    sleep(1)
                    print("Det är en levande kista!")
                    sleep(1)
                    print("Du genast springer ut ur guldrummet och hör att kistan springer efter dig!")
                    sleep(1)
                    print("Du flyr tillbaks där du började och kan inte längre gå in i guldkorridoren..")
                    sleep(1)
                    print("Nu kan du antingen gå genom trädörren('gå framåt för fight tutorial') eller genom dörren med dödsskallen ovan('gå höger')")
                    dörr = input(">")
                    dörr=dörr.lower()
                    print(dörr)
                    if dörr == "gå framåt":
                        lootrum()
                        return guldmynt
                    elif dörr == "gå höger":
                        bosskoridor()
                        return guldmynt
                    else:
                        print("Det finns inga andra vägar..")
                        print(dörr)
                        return guldmynt
                damage=damage + 10
                return damage
            elif kistaitems == "nej":
                print("du låter föremålen ligga kvar.")
                sleep(1)
                print("Det verkar inte finnas något annat intressant i rummet, du borde gå ut och testa en annan dörr")
                ut=input(">")
                ut=ut.lower()
                print(ut)
                if ut == "gå ut":
                    förstarummet()
                else:
                    print("Du kan gå ut genom att skriva in 'gå ut'")
                    print(ut)
        if öppnakista == "nej":
            print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")
            sleep(1)
            print("Det verkar inte finnas något mer intressant i rummet, du borde gå ut och testa en annan dörr")
            goOut=input(">")
            goOut=goOut.lower()
            print(goOut)
            if goOut == "gå ut":
                förstarummet()
            else:
                print("Du kan gå ut genom att skriva in 'gå ut'")
                print(goOut)
    if guldkista == "nej":
        print("du känner att guldkistan kan vara farlig men du känner dig fortfarande säker i rummet..")
        print("vill du gå ut ur rummet?")
        gåut=input(">")
        gåut=gåut.lower()
        print(gåut)
        if gåut == "ja":
            guldkorridor()
        if gåut == "nej":
            print("du står kvar och stirrar på en stängd guldkista..")
            sleep(1)
            print("Plötsligt ser du kistan röra på sig...")
            sleep(1)
            print("Det är en levande kista!")
            sleep(1)
            print("Du genast springer ut ur guldrummet och hör att kistan springer efter dig!")
            sleep(1)
            print("Du flyr tillbaks där du började och kan inte längre gå in i guldkorridoren..")
            sleep(1)
            print("Nu kan du antingen gå genom trädörren('gå framåt') eller genom dörren med dödsskallen ovan('gå vänster')")
            dörr = input(">")
            dörr=dörr.lower()
            print(dörr)
            if dörr == "gå framåt":
                lootrum()
            elif dörr == "gå vänster":
                bosskoridor()
            else:
                print("Det finns inga andra vägar..")
                print(dörr)

#Skapar funktionen bossrum
def bossrum():   #bossrummet
    global guldmynt
    global damage
    print("du har nu öppnat den stora tunga porten..")
    sleep(1)
    print("du ser dig omkring, det är en stor sal med bord och stolar lite överallt, dammigt och en stor tron längst in i rummet..")
    sleep(1)
    print("Du ser inte om någon sitter på tronen eftersom att det är så mörkt längre in. det lyser knappt där du står redan..")
    sleep(1)
    print("du ser återigen skelett delar som ligger lite överallt. Men skelett delarna är ovanligt stora..")
    sleep(1)
    print("kan det vara en magiker som gjort detta?")
    sleep(1)
    print("Du går längre in i rummet...")
    sleep(1)
    print("Plötsligt börjar facklor att ljusa en efter en...")
    sleep(1)
    print("Du börjar känna dig osäker men du fortsätter att gå framåt..")
    sleep(1)
    print("Du står nu framför tronen och då märker du att de stora skelett delarna darrar och börjar att röra på sig..")
    sleep(1)
    print("Du hör väldigt högt oväsen och skelett delar som hoppar mot varandra...")
    sleep(5)
    print("Efter några sekunder är skeletten helformad och liknar vanligt mänsklig skelett men ovanligt stort...")
    sleep(1)
    print("Skeletten vänder sig mot tronen och tar upp en krona och lägger den på huvudet.. medan han skriker..")
    sleep(2)
    print("I..AM...THE KING!!!")
    sleep(2)
    print("""
              .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '    """)
    sleep(2)
    print("Du knuffas bakåt då han stompar kraftigt med en av sina ben...")
    sleep(2)
    print("Du måste döda *SKELETT KUNGEN!*")

    # Skapar en local funktion(funktion inuti en funktion)
    def fightBossSK():
        # berättar att funktionen använder globala variabler
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        global ryggsäck
        global guldmynt
        #Skapar ett lokalt variabel eHealth för (enemyHealth) och tilldelar det värde
        eHealth = 1000
        sleep(4)
        # skapar en while loop för fighten som gäller så länge enemyHealth är större än noll
        while eHealth > 0:
            # Skapar en if sats inuti while loopen som aktiveras då man har dött alltså då health är mindre än noll, då startas om fighten och man startar med 300 hp
            if health <= 0:
                print("Du har dött...")
                sleep(2)
                print("Men ge inte upp än!")
                sleep(2)
                print("STARTAR OM BOSS FIGHTEN")
                sleep(1)
                health=300
                fightBossSK()
            # Skapar en if sats för vad som ska hända så länge spelaren lever
            if health > 0:
                # Skapar en fråga(uppmaning för användaren)
                action = input("Du står framför SKELETT-KUNGEN \n \n döda den!! >")
                action=action.lower()
                # Ifall svaret på uppmaningen är attack kommer följande att hända:
                if action == "attack":
                    # Ifall enemyHealth är lika eller mindre än noll kommer endast följande att skrivas ut:
                    if eHealth <= 0:
                        # EnemyHealth är lika med gamla enemyhealth - damge(skada man gör beroende på vilken klass man har valt)
                        eHealth=eHealth-damage
                        print("SKELETT-KUNGEN överlevde inte din autoattack!")
                    # Annars ifall enemyHP fortfarande är större än noll kommer följande att hända:
                    else:
                        eHealth=eHealth-damage
                        # skapar en variabel som innehåller en random.choice funktion alltså den väljer ut slumpmässig element i listan
                        eAttTxt = random.choice(["Dess ben delar flyger omkring i rummet!\n \n", "SKELETT-KUNGEN skriker vilt!\n \n", "SKELETT-KUNGEN: DU  KAN INTE DÖDA MIG!\n \n"])
                        # Skriver ut den slumpmässiga elementen
                        health = health - random.randint(15,20)
                        print(eAttTxt)
                        print(f"Du attackerade SKELETT-KUNGEN!\n")
                        sleep(2)
                        print(f"SKELETT-KUNGEN blev träffad med din auto-attack, den har {eHealth}hp kvar!")
                        # Ditt Health är lika med health du hade innan - funktion som väljer ut ett slumpmässigt tal mellan 15 och 20
                        print(f"SKELETT-KUNGEN slår kraftigt tillbaks! Du har \n \n {health}hp kvar")
                # Ifall svaret på uppmaningen är a(ability) kommer följande att ske:
                elif action == "a":
                    #kontrollerar att spelaren har tillräckligt mana för att använda ability, ifall hen inte har tillräckligt mana kommer ability inte att användas
                    if mana < 50:
                        print("Du har inte tillräckligt med mana")
                    else:
                        # Därefter att mana har blivit kontrollerad kollar den efter enemieshp efter den använda ability, Ifall enemiesHP är mindre eller lika med noll kommer den endast skriva ut följande:
                        if eHealth <= 0:
                            mana = mana-50
                            eHealth = eHealth - aDamage
                            print("SKELETT-KUNGEN överlevde inte din kraftfulla ability!")
                        else:
                            # Annars kommer följande att ske: 
                            # Det tar bort 50 mana och enemieshp är lika med enemieshp innan subtraherat med aDamage(abilityDamage) som tilldelas vid klassVal
                            mana = mana - 50
                            eHealth = eHealth - aDamage
                            health=health - random.randint(15,20)
                            eAbTxt = random.choice(["\n \nSkeletten flyger bort mot väggen efter att den har tagit emot din kraftfulla ability!", "Skeletten skriker av ondska då du träffar den med din ability!"])
                            print(eAbTxt)
                            print(f"Du attackerade skeletten med din kraftfulla ability! \n \n den har {eHealth}hp kvar!\n")
                            print(f"Skeletten tar sig upp och attackerar tillbaka! Du har {health}hp kvar!\n")
                            print(f"Du har {mana} mana kvar")
                # Ifall svaret på uppmaningen är u(ultimate)
                elif action == "u":
                    if mana < 100:
                        print("Du har inte tillräckligt med mana")
                    else:
                        if eHealth <= 0:
                            mana = mana - 100
                            eHealth = eHealth - uDamage
                            print("SKELETT-KUNGEN överlevde inte din kraftfulla ultimate!!")
                        else:
                            mana = mana - 100
                            eHealth = eHealth - uDamage
                            health=health - random.randint(15,20)
                            eUTxt = random.choice(["SKELETT-KUNGEN förlorar kontrollen och faller på knäna!", "SKELETT-KUNGEN blir träffad med din ultimate och tar emot stor skada!"])
                            print(eUTxt)
                            print("Du träffade SKELETT-KUNGEN med din kraftfulla Ultimate!")
                            sleep(1)
                            print(f"SKELETT-KUNGEN blev träffad med din ultimate-ability, den har {eHealth}hp kvar!")
                            print(f"SKELETT-KUNGEN lyckades inte att ta sig upp efter att den blev träffad med din ultimate, du tar ingen skada!\n")
                            print(f"Du har {mana} mana kvar")
                # Skapar en användbar item som återupptar hp 
                elif action == "hp":
                    #Först skapar jag en for sats som kollar ifall spelaren har någon livselixir i sin ryggsäck
                    for healthPotion in ryggsäck:
                        # Alltså ifall Det finns någon livselixir i ryggsäcken kommer följande att hända
                        if healthPotion == "Livselixir":
                            #Ditt hp kommer att adderas med 100
                            health=health+100
                            # Därefter skriver den ut hur mycket hp man har för att man ska veta vad man ligger på
                            print(f"Du har {health}hp kvar")
                            # Skapar även ett limit, alltså man kan inte ha mer än 500 hp, ifall hp är lika eller större än 500 kommer hp att vara lika med 500
                            if health >= 500:
                                health=500
                            else:
                                # Annars ifall du har mindre hp än 500 kommer det att ta bort en livselixir ifrån din ryggsäck
                                print(health)
                                ryggsäck.remove("Livselixir")
                                print(ryggsäck)
                # Här skapar jag en liknande item fast med en annan funktion, en manaelixir
                elif action == "mana":
                    # Kollar igenom ryggsäcken
                    for manaPotion in ryggsäck:
                        # För "Manaelixir" i ryggsäcken kommer den att addera mana med 100
                        if manaPotion == "Manaelixir":
                            # Den adderar mana med 100 och skriver ut hur mycket mana man ligger på
                            mana=mana+100
                            print(f"Du har {mana} mana kvar")
                            # Skapar en ytterligare if sats för att kontrollera att spelaren inte ska ha mer mana än 200
                            # Alltså ifall mana är lika eller större än 200 kommer mana att vara lika med 200
                            if mana >= 200:
                                mana=200
                            else:
                                # Ifall mana inte är redan lika med två hundra eller mer, kommer den att addera på mana och ta bort en "Manaelixir" från ryggsäcken
                                print(health)
                                ryggsäck.remove("Manaelixir")
                                #Samt skriva ut ryggsäcken för att veta ifall man har några fler elixir
                                print(ryggsäck)
                else:
                    print("Du kan använda en av följande inputs: attack, u(ultimate), a(ability), hp(Livselixir) eller mana(manaelixir)")
                    sleep(5)
    
    fightBossSK()
    # Efter att bossen har blivit besegrad kommer följande att skrivas ut:
    print("""
                                              ___-----------___
                                        __--~~                 ~~--__
                                    _-~~                             ~~-_
                                 _-~                                     ~-_
                                |                                           |
                               |                                             |
                              |                                               |
                              |                                               |
                             |                                                 |
    .-------| |--------------|                                                 |-------------------.__
    |WMWMWMW| |>>>>>>>>>>>>> |                                                 |>>>>>>>>>>>>>>>>>>>>>>:>
    `-------| |-------------- |                                               |-------------------'^^
                              |  |    _-------_               _-------_    |  |
                              |  |  /~         ~\           /~         ~\  |  |
                               ||  |             |         |             |  ||
                               || |               |       |               | ||
                               || |              |         |              | ||
                               |   \_           /           \           _/   |
                              |      ~~--_____-~    /~V~\    ~-_____--~~      |
                              |                    |     |                    |
                             |                    |       |                    |
                             |                    |  /^\  |                    |
                              |                    ~~   ~~                    |
                               \_         _                       _         _/
                                 ~--____-~ ~\                   /~ ~-____--~
                                      \     /\                 /\     /
                                       \    | ( ,           , ) |    /
                                        |   | (~(__(  |  )__)~) |   |
                                         |   \/ (  (~~|~~)  ) \/   |
                                          |   |  [ [  |  ] ]  /   |
                                           |                     |
                                            \                   /
                                             ~-_             _-~
                                                ~--___-___--~    
 
                         """)
    sleep(5)
    print("Du har dödat SKELETT-KUNGEN!")
    sleep(1)
    print("Det tar en stund för dig att fånga andan efter boss-fighten..")
    sleep(6)
    print("Du ser dig omkring i rummet och nu när flackorna lyser märker du hur gigantiskt rummet är...")
    sleep(1)
    print("Du märker en lucka i goilvet bakom SKELETT-KUNGENS tron, som verkar leda till någon annan rum..")
    sleep(1)
    print("Det verkar vara säkert i rummet nu när SKELETT-KUNGEN är död")
    sleep(1)
    print("Vad vill du göra? ('gå ner') för att gå genom luckan i golvet")
    q_1=input(">")
    q_1=q_1.lower()
    if q_1 == "gå ner":
        dungeonentry()
    elif q_1 == "search":
        sleep(2)
        print("Du letar nu igenom den gigantiska rummen, det kommer att ta en stund..")
        sleep(10)
        print("Du har letat igenom de trasiga möblerna och kungens tron")
        sleep(2)
        print("Du hittade 2 stycken Livselixir, 1000 guldmynt, 3 Manaelixir och du hittade en gigantisk kista i rum hörnet..")
        # Lägger till följande element i ryggsäcken(listan)
        ryggsäck.append("Livselixir")
        ryggsäck.append("Livselixir")
        ryggsäck.append("Manaelixir")
        ryggsäck.append("Manaelixir")
        ryggsäck.append("Manaelixir")
        sleep(3)
        print(ryggsäck)
        # Adderar globala integer(guldmynt) med 1000
        guldmynt = guldmynt + 1000
        sleep(2)
        print("Vill du gå fram till kistan?")
        kistaQ_1=input(">")
        kistaQ_1=kistaQ_1.lower()
        if kistaQ_1 == "ja":
            print("Du står framför den gigantiska kistan som är helt dammig och full av spindelnät..")
            sleep(2)
            print("Vill du öppna kistan?")
            kistaQ_2=input(">")
            kistaQ_2=kistaQ_2.lower()
            if kistaQ_2 == "ja":
                print("Du öppnar kistan och märker massor av olika föremål..")
                sleep(2)
                print("Det kommer att ta en stund innan du hittar något värdefullt...")
                sleep(10)
                print("Efter att du har letat igenom kistan har du hittat följande saker:")
                sleep(2)
                print("""
                     1x Livselixir
                     1x Manaelixir
                     300x Guldmynt
                     """)
                guldmynt = guldmynt + 300
                ryggsäck.append("Livselixir")
                ryggsäck.append("Manaelixir")
                print(ryggsäck)
                sleep(2)
                print("Du hittar även en Rune-bok som du bläddrar igenom genast..")
                sleep(2)
                print("Det känns väldigt bra då du bläddrar igenom boken, du känner dig starkare...")
                sleep(2)
                print("*Från och med nu kommer dina autoattacks att göra 20 mer skada*")
                damage = damage + 20
                sleep(2)
                print("Det verkar inte finnas något mer att göra i rummet")
                sleep(2)
                print("Du bestämmer dig att gå ner genom luckan..")
                dungeonentry()
                #Eftersom vi kommer att använda damage i andra funktioner måste vi returnera den uppdaterade värden för att annars skulle det inte förändras globalt
                return damage
            elif kistaQ_2 == "nej":
                sleep(2)
                print("Du känner att kistan kan vara farlig..")
                sleep(2)
                print("Du vågar inte öppna kistan, du går igenom luckan på en gång...")
                dungeonentry()
            else: 
                print("Du kan inte göra det i det här rummet")
                sleep(2)
                kistaQ_2=input(">")
                kistaQ_2=kistaQ_2.lower()
        elif kistaQ_1 == "nej":
            print("Du kommer ihåg vad som hände med förra kistan, du håller dig borta")
            sleep(2)
            print("Istället går du genom luckan på en gång..")
            dungeonentry()
        else:
            print("Du kan inte göra det i det här rummet")
            sleep(2)
            kistaQ_1=input(">")
            kistaQ_1=kistaQ_1.lower()
    elif q_1 == "gå bakåt":
        print("Du försöker vända men då märker du att dörren du kom ifrån är fortfarande låsta..")
        sleep(2)
        print("Du märker att skelett delarna börjar darra igen...")
        sleep(2)
        print("Du är tvungen att genast fly genom luckan...")
        dungeonentry()
    else:
        print("Du kan inte göra det i den här rummen")
        sleep(2)
        print("Du har endast en väg du kan välja ('gå ner') genom luckan...")
        q_2=input(">")
        q_2=q_2.lower()
        print(q_2)
        if q_2 == "gå ner":
            sleep(2)
            dungeonentry()
        else:
            print("Du vet att det är väldigt farligt..")
            sleep(2)
            print("Men du vet också att utan mat och vatten kommer du inte överleva länge i grottan...")
            sleep(2)
            print("Du måste gå genom luckan..")
            dungeonentry()

def guldkorridor(): #rum innan guldrumS
    global ryggsäck
    print("du står nu i vad som ser ut och vara en guldig korridor..")
    sleep(1)
    print("när du ser dig omkring så ser du massa bokhyllor fullt med böcker och rummet är även dammigt..")
    sleep(1)
    print("rummet är även någorlunda upplyst..")
    sleep(1)
    print("längre in i rummet ser du en till guldig dörr..")
    sleep(1)
    print("bakom dig har du dörren du kom ifrån..")
    sleep(1)
    print("vill du gå igenom dörren framför dig?")

    gåiniguldrum=input(">")
    gåiniguldrum=gåiniguldrum.lower()

    if gåiniguldrum =="ja":
        sleep(2)
        guldrum()
    elif gåiniguldrum == "nej":
        print("Du väljer att inte fortsätta genom den guldiga rummen\n")
        sleep(1)
        print("Du bestämmer dig att gå tillbaka till grottöppningen")
        sleep(2)
        förstarummet()
    elif gåiniguldrum == "search":
        print("Du letar igenom den guldiga korridoren...\n")
        sleep(1)
        print("Du hittar en mana elixir!\n")
        ryggsäck.append("Manaelixir")
        print(f"Ryggsäck: {ryggsäck}\n")
        sleep(1)
        print("**Mana elixir kan du använda som livselixir, under fightens gång**\n")
        sleep(1)
        print("**Till skillnad från livselixiren, du använder manaelixir genom 'mana' och den återger dig 50 mana\n")
        sleep(1)
        print("Det verkar inte finnas något mer att göra i korridoren..\n")
        sleep(1)
        print("Vad vill du göra? 'gå framåt'(genom guldiga dörren) och 'gå bakåt'(tillbaks till gråttöppningen)\n")
        sleep(1)
        gåiniguldrum = input(">")
        gåiniguldrum=gåiniguldrum.lower()
        if gåiniguldrum == "gå framåt":
            guldrum()
        elif gåiniguldrum == "gå bakåt":
            förstarummet()
        else:
            print("Du måste ju välja en av alternativen\n \n'gå framåt' \neller\n'gå bakåt'")
            gåiniguldrum = input(">")
            gåiniguldrum=gåiniguldrum.lower()
    else:
        print("Du kan inte göra det i det här rummet!")
        gåiniguldrum = input(">")
        gåiniguldrum=gåiniguldrum.lower()


def bosskoridor(): 
    global ryggsäck
    print("du har nu gått igenom dörren med en dödskalle över sig..")
    sleep(1)
    print("du ser massor av skelett delar överallt som verkar vara mänskliga ben..")
    sleep(1)
    print("du blir genast försiktig och kollar runt för att se om det finns någon fiende i rummet..")
    sleep(1)
    print("du ser bara massa bokhyllor med blod på från de döda och en stor port längre in i rummet..")
    sleep(1)
    print("bakom en död kropp vid en bokhylla så ser det ut att ligga en karta av något slag..")
    sleep(1)
    print("när du kollar närmare på den stora svarta porten så ser du tydliga mönster av drakar och andra monster och andra saker som du inte kan identifiera..")
    sleep(1)
    print("du misstänker att bakom den dörren finns något riktigt farligt..")
    sleep(1)
    print("vad vill du göra? för att gå genom porten > ('gå framåt')")

    bossdörr=input(">")
    bossdörr=bossdörr.lower()

    if bossdörr == "gå framåt":
        bossrum()
    elif bossdörr == "search":
        ryggsäck.append("Livselixir")
        ryggsäck.append("Manaelixir")
        print("Du söker igenom de blodiga hyllorna..")
        sleep(1)
        print("Du hittar en livselixir och manaelixir!")
        print(ryggsäck)
        sleep(1)
        print("Du har letat igenom rummet, vad vill du göra nu?")
        q_1=input(">")
        q_1=q_1.lower()
        if q_1 == "gå bakåt":
            print("Du går fram till dörren där du kom från..")
            sleep(2)
            print("Men då du försöker öppna dörren märker du att den är låst...")
            sleep(2)
            print("Det finns bara en väg...")
            q_2=input(">")
            q_2=q_2.lower()
            if q_2 == "gå framåt":
                bossrum()
            elif q_2 == "ta upp mappen":
                print("""
                    *****II*****
                        LEFT
                        LEFT
                        RIGHT""")
                sleep(2)
                print("Du tog upp den dammiga mappen")
                print(f"Ryggsäck: {ryggsäck}")
                sleep(4)
                print("Men plötsligt hör du väldigt tunga fotsteg bakom dörren där du kom ifrån(grottöppningen)")
                sleep(2)
                print("Du hör varelsen slå i dörren, du blir tvungen att fly genom den mystiska porten...")
                bossrum()
            else:
                print("Du har endast en dörr kvar...('gå framåt')")
                sleep(2)
                print("Du går igenom den mystiska porten..")
                bossrum()
        elif q_1 == "gå framåt":
            print("Du bestämmer dig att gå igenom den mystiska porten...")
            bossrum()
        else:
            print("Du är fortfarande rädd för den mystiska porten..")
            sleep(2)
            print("Men plötsligt hör du en mänsklig röst som kommer just från rummet dit den mystiska porten leder till...")
            sleep(2)
            print("*DET ÄR LUNGT, VAR INTE RÄDD, VI HAR OCKSÅ FASTNAT PÅ GRUND AV DRAKEN*")
            sleep(2)
            print("Du igenkänner rösten, dessutom befinner de sig i samma situation, du bestämmer dig att gå in..")
            sleep(2)
            bossrum()
    elif bossdörr == "ta upp mappen":
        print("Du har nu tagit upp den dammiga mappen och du lyckades att läsa igenom den \n \n     Det står:")
        sleep(2)
        print("""
            *****II*****
                LEFT
                LEFT
                RIGHT""")
        print(f"Ryggsäck: {ryggsäck}")
        print("Du ser dig omkring i rummet igen, vad vill du göra? ('gå framåt') för att gå genom mystiska porten")
        mappq_1=input(">")
        mappq_1=mappq_1.lower()
        if mappq_1 == "gå framåt":
            bossrum()
        elif mappq_1 == "search":
            ryggsäck.append("Livselixir", "Manaelixir")
            print("Du söker igenom de blodiga hyllorna..")
            sleep(1)
            print("Du hittar en livselixir och manaelixir!")
            print(ryggsäck)
            sleep(1)
            print("Du har letat igenom rummet, vad vill du göra nu?")
            mappq_2=input(">")
            mappq_2=mappq_2.lower()
            if mappq_2 == "gå bakåt":
                print("Du märker att dörren bakom dig(där du kom från) är låst..")
                sleep(2)
                print("Du inser att den enda vägen är genom den mystiska porten..")
                mappq_4=input(">")
                mappq_4=mappq_4.lower()
                if mappq_4 == "gå framåt":
                    bossrum()
                else:
                    print("Du finns ingen annan väg än framåt genom den mystiska porten...")
                    bossrum()
            elif mappq_2 == "gå framåt":
                bossrum()
            else:
                print("Det finns inget sånt du kan göra i det här rummet")
                mappq_5=input(">")
                mappq_5=mappq_5
                if mappq_5 == "gå bakåt":
                    print("Du märker att dörren bakom dig(där du kom från) är låst..")
                    sleep(2)
                    print("Du inser att den enda vägen är genom den mystiska porten..")
                    mappq_4=input(">")
                    mappq_4=mappq_4.lower()
                    if mappq_4 == "gå framåt":
                        bossrum()
                    else:
                        print("Det finns ingen annan väg än framåt genom den mystiska porten...")
                        bossrum()
                else:
                    print("Du finns ingen annan väg än framåt genom den mystiska porten...")
                    bossrum()
        else:
            print("Du märker att dörren bakom dig(där du kom från) är låst..")
            sleep(2)
            print("Du inser att den enda vägen är genom den mystiska porten..")
            mappq_1=input(">")
            mappq_1=mappq_1.lower()
    elif bossdörr == "gå bakåt":
        print("Du går fram till dörren där du kom ifrån..")
        sleep(2)
        print("Men då du försöker öppna dörren märker du att den är låst...")
        sleep(2)
        print("Det finns bara en väg...")
        q_2=input(">")
        q_2=q_2.lower()
        print(q_2)
        if q_2 == "gå framåt":
            bossrum()
        elif q_2 == "ta upp mappen":
            ryggsäck.append("""
                    *****II*****
                        LEFT
                        LEFT
                        RIGHT""")
            print("""
                    *****II*****
                        LEFT
                        LEFT
                        RIGHT""")
            sleep(2)
            print("Du tog upp den dammiga mappen")
            print(f"Ryggsäck: {ryggsäck}")
            sleep(4)
            print("Men plötsligt hör du väldigt tunga fotsteg bakom dörren där du kom ifrån(grottöppningen)")
            sleep(2)
            print("Du hör varelsen slå i dörren, du blir tvungen att fly genom den mystiska porten...")
            bossrum()
        else:
            print("Du har endast en dörr kvar...('gå framåt')")
            sleep(2)
            print("Du går igenom den mystiska porten..")
            bossrum()
    else:
        print("Du kan inte göra det i rummet")
        q_3=input(">")
        q_3=q_3.lower()
        print(q_3)
        if q_3 == "gå framåt":
            print("Du bestämmer dig att gå igenom den mystiska porten...")
            bossrum()
        elif q_3 == "gå bakåt":
            print("Du märker att dörren bakom dig(där du kom från) är låst..")
            sleep(2)
            print("Du inser att den enda vägen är genom den mystiska porten..")
            mappq_4=input(">")
            mappq_4=mappq_4.lower()
            print(mappq_4)
            if mappq_4 == "gå framåt":
                bossrum()
            else:
                print("Det finns ingen annan väg än framåt genom den mystiska porten...")
                bossrum()

    gåtillgrottöppning=input(">")
    gåtillgrottöppning=gåtillgrottöppning.lower()
    
    if gåtillgrottöppning == "ja":
        grottöppning()
    if gåtillgrottöppning == "nej":
        bosskoridor()
    

# själva starten av spelet:
def grottöppning(): 
    print("du står nu i grottöppningen, det är kvavt och du ser inte så mycket..")
    sleep(1)
    print("du går lite längre in och ser ljus, när du kollar närmare ser du 3 dörrar..")
    sleep(1)
    print("en dörr rakt framför dig, en träddörr(*fight-tutorial*), till vänster har ser du en gulddörr och till höger om dig har du en dörr med en dödskalle hängandes över..")
    sleep(1)
    print("du blir väldigt försiktig med tanke på att det kan bo fler monster här eller något annat mystiskt, men du behöver ta dig ut..")
    sleep(1)
    print("hur gör du? vilken dörr väljer du?")
    sleep(1)
    print("vänster höger eller rakt fram.")
    sleep(1)
    print("(För att gå vänster skriv \"gå vänster\")")
    
    förstadörr=input(">")
    förstadörr=förstadörr.lower()
    if förstadörr == "gå vänster":
        print("du står nu och kikar in i gulddörren, du ser ett tomt rum och en till gulddörr framför dig..")
        sleep(1)
        print("du går in och kikar in i nästa rum..")
        sleep(1)
        guldkorridor()
    elif förstadörr == "gå höger":
        sleep(2)
        bosskoridor()
    elif förstadörr == "gå framåt":
        sleep(2)
        lootrum()
    else:
        print("Det verkar inte finnas någon sådan alternativ, 'gå vänster'(genom guldiga dörren) eller 'gå höger'(genom dörren med skallen ovan)")
        förstadörr=input(">")
        förstadörr=förstadörr.lower()

def förstarummet():
    print("Du befinner dig nu i första rummet, 'gråttöppningen'")
    sleep(1)
    print("Du kan antingen gå åt höger, genom dörren med dödsskallen ovan \n \n eller till vänster genom gulddörren")
    choice = input(">")
    choice = choice.lower()
    if choice == "gå vänster":
        guldkorridor()
    elif choice == "gå höger":
        bosskoridor()
    else:
        choice = input(">")
        choice = choice.lower()

def dungeonentry():
    sleep(2)
    print("Det verkar som att du har gått in i en fängelsehåla..\n")
    sleep(2)
    print("Rummet du befinner dig i ser mycket läskigare ut än de rummen du varit innan i..\n")
    sleep(2)
    print("Rummet liknar grottöppningen, det finns en dörr åt höger, vänster och framåt\n")
    sleep(2)
    print("Medan nu ser du inga tecken som exempelvis dödsskallen eller guldiga dörren...\n")
    sleep(2)
    print("Du måste hitta din egen väg framåt\n")
    sleep(3)
    print("...\n")
    sleep(2)
    dorrChoice=input(">")
    dorrChoice=dorrChoice.lower()

    if dorrChoice == "gå framåt":
        sleep(2)
        frontDoorLvl2()
    elif dorrChoice == "gå vänster":
        sleep(2)
        leftDoorLvl2()
    elif dorrChoice == "gå höger":
        rightDoorLvl2()

def firstDoorLvl2():
    print("Du är tillbaka i fängelsehålans entré")
    sleep(2)
    print("Tre dörrar, vänster, höger och framför dig")
    sleep(2)
    print("Vad vill du göra?")
    choice=input(">")
    choice=choice.lower()
    if choice == "gå vänster":
        sleep(2)
        leftDoorLvl2()
    elif choice == "gå framåt":
        sleep(2)
        frontDoorLvl2()
    elif choice == "gå höger":
        sleep(2) 
        rightDoorLvl2()

def frontDoorLvl2():
    print("Du befinner dig nu i ett väldigt litet rum, med många facklor på väggarna..\n")
    sleep(2)
    print("Du ser flera trasiga hyllor och gammla trälådor..\n")
    sleep(2)
    print("Framför dig ser du en konstig dörr som du inte har sett innan...\n")
    sleep(2)
    print("Det ser ut som en krogdörr, trädörr med olika metall detaljer..\n")
    sleep(2)
    print("Genom den lilla fönstret i dörren ser du glänsande ljus\n")
    sleep(2)
    print("Höger om dig finns ännu en till dörr, den verkar igenkännerbar, den liknar trädörren som du har sett innan..\n")
    sleep(2)
    print("Vad vill du göra?\n")
    dorrChoice=input(">\n")
    dorrChoice=dorrChoice.lower()
    if dorrChoice == "gå framåt":
        sleep(2)
        tavernDoorLvl2()
    elif dorrChoice == "gå höger":
        sleep(2)
        lootRoomLvl2()


def lootRoomLvl2():
    print("Du går in i ett rum med många trälådor..")
    sleep(2)
    print("När du tittar dig omkring i rummet märker du att i hörnet ligger någon varelse...")
    sleep(2)
    print("Du går fram till varelsen...")
    sleep(2)
    print("Plötsligt hoppar varelsen på dig...")
    sleep(2)
    print("Ni knuffar på varandra, du lyckas knuffa bort den...")
    sleep(2)
    print("*JAG KOMMER ATT DÖDA DIG*")
    sleep(2)
    print("Du blir tvungen att döda varelsen...")
    def fight():
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        global ryggsäck
        eHealth = 500
        sleep(2)
        while eHealth > 0:
            print(f"Du har {mana} mana kvar")
            if health <= 0:
                print("Du har dött, men ge inte upp än!")
                sleep(2)
                print("*STARTA OM FIGHTEN*")
                sleep(2)
                health = 300
                fight()
            if health > 0:
                action = input(">\n")
                action = action.lower()
                if action == "attack":
                    if eHealth <= 0:
                        eHealth=eHealth-damage
                        print("Varelsen överlevde inte din autoattack!")
                    else:
                        eHealth=eHealth-damage
                        eAttTxt = random.choice(["Varelsen faller omkull på grund av din mäkriga attack!\n", "Varelsen skriker vilt efter att hen har blivit träffad med din attack...\n", "Varelsen blir kraftigt träffad med din autoattack!\n"])
                        print(eAttTxt)
                        health=health-random.randint(5,15)
                        print(f"Du attackerade Varelsen med din auto-attack, den har {eHealth}hp kvar!\n")
                        print(f"Varelsen attackerar tillbaks med sina klor.. du har {health}hp kvar..\n")
                elif action == "a" and mana >= 50:
                    if mana < 50:
                        print("Du har inte tillräckligt med mana..")
                    else:
                        if eHealth <= 0:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            print("Den mystiska varelsen överlevde inte din kraftfulla ability!")
                        else:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            eAbTxt = random.choice(["Varelsen skriker av ondska då den blir träffad med din kraftfulla ability!", "Varelsen faller omkull men lyckas ta sig upp efter din ability..."])
                            print(eAbTxt)
                            health=health-random.randint(5,15)
                            print(f"Du attackerade Varelsen med din kraftfulla ability, den har {eHealth}hp kvar!\n")
                            print(f"Varelsen tar sig upp igen och slår tillbaks med sin konstiga lila näve.. du har {health}hp kvar...")
                elif action == "u" and mana >= 100:
                    if mana < 100:
                        print("Du har inte tillräckligt med mana..")
                    else:
                        if eHealth <= 0:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            print("Den konstiga varelsen överlevde inte din kraftfulla ultimate!")
                        else:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            eUTxt = random.choice(["Varelsen blir mycket kraftigt träffad med din ultimate!", "Varelsen flyger in i väggen efter att den har blivit träffad med din kraftfulla ultimate!"])
                            print(eUTxt)
                            print(f"Varelsen blir träffad med din ultimate-ability och tar enorm skada, den har {eHealth}hp kvar!")
                            print("Varelsen lyckas inte ta sig upp efter att hen har blivit träffad med din ultimate, du tar ingen skada!")
                elif action == "hp":
                    for healthPotion in ryggsäck:
                        if healthPotion == "Livselixir":
                            health=health+100
                            if health >= 500:
                                health=500
                            else:
                                ryggsäck.remove("Livselixir")
                                print(ryggsäck)
                elif action == "mana":
                    for manaPotion in ryggsäck:
                        if manaPotion == "Manaelixir":
                            mana=mana+100
                            if mana >= 200:
                                mana=200
                            else:
                                ryggsäck.remove("Manaelixir")
                                print(ryggsäck)
                elif action == "berserker":
                    for berserkerPotion in ryggsäck:
                        if berserkerPotion == "Berserker":
                            damage = damage + 50
                else:
                    action = input(">\n")
                    action = action.lower()

    fight()
    print("Du har dödat Varelsen, du känner att den var verkligen konstig..")
    sleep(2)
    print("Den var både liten men även väldigt stark...")
    sleep(2)
    print("Nu när varelsen är död öppnas ett nytt dörr...")
    sleep(2)
    print("Konstig krog-dörr med litet fönster ruta som ljus kommer ifrån...")
    sleep(2)
    print("Du kan gå tillbaka till fängelsehålans entré(gå bakåt) eller gå genom den konstiga krog-dörren(gå framåt)")
    sleep(2)
    print("Vad vill du göra?")
    fightChoice=input(">")
    fightChoice=fightChoice.lower()
    if fightChoice == "gå bakåt":
        sleep(2)
        print("Du är nu tillbaka i fängelsehålans entré")
        sleep(2)
        print("Vilken dörr väljer du höger eller vänster?")
        dorrChoice=input(">")
        dorrChoice=dorrChoice.lower()
        if dorrChoice == "gå vänster":
            sleep(2)
            leftDoorLvl2()
        elif dorrChoice == "gå höger":
            sleep(2)
            rightDoorLvl2()
        else:
            print("Det finns bara två vägar, höger (gå höger) och vänster(gå vänster)")
            dorrChoice=input(">")
            dorrChoice=dorrChoice.lower()
    elif fightChoice == "gå framåt":
        sleep(2)
        tavernDoorLvl2()
    elif fightChoice == "search":
        print("Du letar igenom rummen...")
        sleep(5)
        print("Du hittar 2x Manaelixir och 2x Livselixir")
        ryggsäck.append("Livselixir")
        ryggsäck.append("Livselixir")
        ryggsäck.append("Manaelixir")
        ryggsäck.append("Manaelixir")
        print(ryggsäck)
        sleep(3)
        print("Vilken dörr väljer du?")
        fightChoice=input(">")
        fightChoice=fightChoice.lower()
    else:
        print("Det verkar inte finnas något sånt att göra i rummet...")
        sleep(3)
        fightChoice=input(">")
        fightChoice=fightChoice.lower()


def tavernDoorLvl2():
    global guldmynt
    global ryggsäck
    sleep(3)
    print("Du går in genom krog-dörren...")
    sleep(2)
    print("Det ser väldigt vänligt ut i rummet...")
    sleep(2)
    print("Det finns en mängd bord och sittande främmlingar...")
    sleep(2)
    print("Framför dig finns en bar, vill du gå fram och prata med baristan?..")
    sleep(2)
    choice=input(">")
    choice=choice.lower()
    if choice == "ja":
        print("Barista - Dig känner jag inte igen, vad får dig att komma hit?")
        sleep(2)
        print("Du - Jag vet faktiskt inte, det enda jag vet är att jag var tvungen att fly hit på grund av draken...")
        sleep(4)
        print("Barista - Jaha, men då har jag något som du verkligen kommer att behöva för att döda draken")
        sleep(4)
        print("Barista - Här kan du köpa alla typer av elixirer, för 50 guldmynt!")
        sleep(4)
        print("Barista - Manaelixir, Livselixir men även för endast 1000 guldmynt kan du köpa en speciell-elixir")
        sleep(6)
        print("Barista - Berserker-potion som kommer att göra dig starkare inför kommande fighter(för att använda berserkerpotion under fightens gång, skriv 'berserker')...")
        sleep(2)
        print("Vad vill du göra?(för att köpa t.ex. livselixir(>livselixir)) för att gå tillbaka till fängelsehålans entré('gå bakåt')")
        shopQ=input(">")
        shopQ=shopQ.lower()
        if shopQ == "livselixir":
            if guldmynt >= 50:
                guldmynt = guldmynt - 50
                print("Du har köpt en livselixir!")
                ryggsäck.append("Livselixir")
                print(ryggsäck)
                shopQ=input(">")
                shopQ=shopQ.lower()
                return guldmynt
            else:
                print("Du har inte tillräckligt med guldmynt..")
                shopQ=input(">")
                shopQ=shopQ.lower()
        elif shopQ == "manaelixir":
            if guldmynt >= 50:
                guldmynt = guldmynt - 50
                print("Du har köpt en Manaelixir!")
                ryggsäck.append("Manaelixir")
                print(ryggsäck)
                shopQ=input(">")
                shopQ=shopQ.lower()
                return guldmynt
            else:
                print("Du har inte tillräckligt med guldmynt..")
                shopQ=input(">")
                shopQ=shopQ.lower()
        elif shopQ == "berserker":
            if guldmynt >= 1000:
                guldmynt = guldmynt - 1000
                print("Du har köpt en speciell-elixir, Berserker-potion!")
                ryggsäck.append("Berserker")
                print(ryggsäck)
                shopQ=input(">")
                shopQ=shopQ.lower()
                return guldmynt
            else:
                print("Du har inte tillräckligt med guldmynt..")
                shopQ=input(">")
                shopQ=shopQ.lower()
        elif shopQ == "gå bakåt":
            sleep(2)
            print("Du befinner dig nu i första rummet, fängelsehålans entré")
            sleep(3)
            print("Vilken dörr väljer du? Vänster eller höger?")
            sleep(2)
            dorrChoice=input(">")
            dorrChoice=dorrChoice.lower()
            if dorrChoice == "gå vänster":
                sleep(2)
                leftDoorLvl2()
            elif dorrChoice == "gå höger":
                sleep(2)
                rightDoorLvl2()
            else:
                print("Det finns endast två vägar, höger(gå höger) och vänster(gå vänster)")
                dorrChoice=input(">")
                dorrChoice=dorrChoice.lower()
        else:
            print("Det verkar inte finnas något sånt du kan göra...")
            sleep(3)
            print("Du kan köpa en livselixir genom 'livselixir' en manaelixir genom 'manaelixir', berserker potion genom 'berserker' eller gå till fängelsehålans entré genom 'gå bakåt'")        
            shopQ=input(">")
            shopQ=shopQ.lower()

def leftDoorLvl2():
    # LEFT LEFT RIGHT (Treasure-room(mappen))
    global guldmynt
    global damage
    print("Rummet du befinner dig i nu är väldigt mörkt..\n")
    sleep(2)
    print("Du varken ser någonting..\n")
    sleep(2)
    print("Det enda du ser är en liten ljuskälla långt borta i rummet..\n")
    sleep(2)
    print("Du går mot ljuskällan, eftersom du ser inget annat märkligt i rummet..\n")
    sleep(2)
    print("Då du är nästan framme vid ljuskällan, plötsligen börjar vägg-flackor att tändas en efter en...\n")
    sleep(2)
    print("Genast märker du hur stort rummet är jämfört med förra rummet..\n")
    sleep(2)
    print("Du hör konstigt ljud, viskande och någon trassel..\n") 
    sleep(2)
    print("Plötsligt märker du en konstig varelse...\n")
    sleep(2)
    print("Hen är väldigt kort, bär på en gigantisk påse på ryggen och är grönhyad..")
    sleep(5)
    print("...")
    sleep(2)
    print("*VÄLKOMMEN TILL GOBLIN KÄLLAREN - Goblin*")
    sleep(2)
    print("Goblin - 'Hos mig kan du känna dig trygg så länge du förblir vänlig...'")
    sleep(2)
    print("Goblin - Jag kan uppgradera dina vapen för ett pris..")
    sleep(2)
    print("Goblin - Jag tar emot endast glänsande guldiga mynt...")
    sleep(2)
    print("Goblin - Ifall du kan betala 2000 guld mynt kommer jag att uppgradera ditt vapen")
    sleep(2)
    print("Goblin - Tro mig, det är värt det..")
    sleep(3)
    print(f"Just nu har du {guldmynt} guldmynt")
    sleep(2)
    print("Du märker ett glänsande guldigt dörr till vänster..")
    sleep(2)
    print("Höger om dig märker du även ett dörr du inte har sett innan..")
    sleep(2)
    print("Konstig krog-dörr med detaljerad med metall och ett litet fönster som du ser ljus igenom...")
    sleep(2)
    print("Vad vill du göra?")
    choice=input(">")
    choice=choice.lower()
    if choice == "search":
        print("Du söker igenom det mörka rummet...")
        sleep(5)
        print("Tyvär är det verkligen för mörkt i rummet...")
        sleep(2)
        print("Du hittar ingenting...")
        sleep(2)
        choice=input(">")
        choice=choice.lower()
        if choice == "gå vänster":
            print("Du bestämmer dig att gå igenom den guld-glänsande dörren...")
            sleep(5)
            goldKorridorLvl2()
        elif choice == "gå höger":
            print("Du är nyfiken och bestämmer dig att gå igenom den konstiga krog-dörren...")
            sleep(5)
            tavernDoorLvl2()
        else:
            print("Det verkar inte finnas något sånt att göra i rummet...")
            sleep(2)
            print("för att gå höger ('gå höger'), åt vänster ('gå vänster')")
            choice=input(">")
            choice=choice.lower()
    elif choice == "gå vänster":
        print("Du bestämmer dig att gå igenom den guld-glänsande dörren...")
        sleep(5)
        goldKorridorLvl2()
    elif choice == "gå höger":
        print("Du är nyfiken och bestämmer dig att gå igenom den konstiga krog-dörren...")
        sleep(5)
        tavernDoorLvl2()
    elif choice == "upgrade":
        sleep(2)
        if guldmynt >= 2000:
            damage = damage + 50
            guldmynt = guldmynt - 2000
            print("Du visar guldet till herr goblin, han tar genast emot det")
            sleep(2)
            print("Han tar fram ett konstigt skrolla och tar ditt vapen...")
            sleep(2)
            print("Du blir lite nervös..")
            sleep(2)
            print("Han börjar att prata med ett konstigt språk...")
            sleep(2)
            print("Efter några sekunder är han redo")
            sleep(2)
            print("Goblin - Ditt vapen är nu uppgraderat med gamla nordiska runer")
            sleep(2)
            print("Goblin - Det kommer att göra 50 mer skada från och med nu!")
            sleep(2)
            print("Vad vill du göra nu?(gå bakåt) eller (gå höger)")
            goblinQ=input(">")
            goblinQ=goblinQ.lower()
            return damage, guldmynt
        else:
            print("Du har inte tillräckligt guldmynt...")
            goblinQ=input(">")
            goblinQ=goblinQ.lower()
    else:
        print("Det verkar inte finnas något sånt att göra i rummet...")
        sleep(2)
        print("för att gå höger ('gå höger'), åt vänster ('gå vänster')")
        choice=input(">")
        choice=choice.lower()

def goldKorridorLvl2():
    global damage
    global guldmynt
    sleep(2)
    print("Du kommer in genom den guldiga dörren..")
    sleep(2)
    print("För första gången ser du verkliga möbler som inte är alls dammiga eller förstörda...")
    sleep(2)
    print("Det finns flera bokhyllor, bordar, stolar och en fin röd matta som leder till nästa dörr till höger om dig...")
    sleep(2)
    print("Dörren har ännu fler guld detaljer än dörren innan...")
    sleep(2)
    print("Vad vill du göra?")
    choice=input(">")
    choice=choice.lower()
    if choice == "search":
        print("Du letar igenom den guldiga korridoren...")
        sleep(10)
        print("Rummet verkar vara fylld med värdefulla saker men du hittar faktiskt ingenting som skulle kunna vara värdefullt för dig...")
        sleep(2)
        dorrQ=input("Vad vill du göra? \n \n>")
        dorrQ=dorrQ.lower()
        if dorrQ == "gå höger":
            sleep(2)
            print("Du följer den fina röda mattan, genom den guldiga dörren...")
            sleep(3)
            goldRoomLvl2()
        elif dorrQ == "gå bakåt":
            print("Du väljer att vända, du känner att guldiga rummet kan vara farligt...")
            sleep(2)
            print("Du är tillbaks i goblin-källaren...")
            sleep(2)
            print("Du kan uppgradera ditt vapen genom 'upgrade'")
            sleep(2)
            print("Vad vill du göra?")
            goblinQ=input(">")
            goblinQ=goblinQ.lower()
            if goblinQ == "gå höger":
                sleep(2)
                tavernDoorLvl2()
            elif goblinQ == "gå bakåt":
                sleep(2)
                firstDoorLvl2()
            elif goblinQ == "upgrade":
                if guldmynt >= 2000:
                    guldmynt = guldmynt - 2000
                    damage = damage + 50
                    print("Du visar guldet till herr goblin, han tar genast emot det")
                    sleep(2)
                    print("Han tar fram ett konstigt skrolla och tar ditt vapen...")
                    sleep(2)
                    print("Du blir lite nervös..")
                    sleep(2)
                    print("Han börjar att prata med ett konstigt språk...")
                    sleep(2)
                    print("Efter några sekunder är han redo")
                    sleep(2)
                    print("Goblin - Ditt vapen är nu uppgraderat med gamla nordiska runer")
                    sleep(2)
                    print("Goblin - Det kommer att göra 50 mer skada från och med nu!")
                    sleep(2)
                    print("Vad vill du göra nu?(gå bakåt) eller (gå höger)")
                    goblinQ=input(">")
                    goblinQ=goblinQ.lower()
                    return damage, guldmynt
                else:
                    print("Du har inte tillräckligt guldmynt...")
                    goblinQ=input(">")
                    goblinQ=goblinQ.lower()
            else:
                print("Det verkar inte finnas något sånt att göra i rummet...")
                sleep(2)
                print("Du kan gå igenom krog-dörren ('höger'), gå tillbaka till fängelsehålans entré('gå bakåt') eller uppgradera ditt vapen genom 'upgrade'")
                goblinQ=input(">")
                goblinQ=goblinQ.lower()

def goldRoomLvl2():
    global uDamage
    global guldmynt
    global damage
    print("Du går in i ett rum med tre stycken pedestaler...")
    sleep(2)
    print("På den ena finns en kista...('höger')")
    sleep(2)
    print("På den andra finns ett hög med guldmynt...('framåt')")
    sleep(2)
    print("På den tredje finns en rune-bok...('vänster')")   
    sleep(2)
    print("Vilken väljer du?")
    choice=input(">")
    choice=choice.lower()
    if choice == "vänster":
        uDamage = uDamage + 200
        sleep(2)
        print("Du går fram till den vänstra pedestalen och försiktigt tar upp rune-boken...")
        sleep(2)
        print("Du börjar bläddra igenom boken genast, men det känns annorlunda denna gången...")
        sleep(2)
        print("Du känner dig mycketstarkare, jämfört med förra rune-böcker...")
        sleep(2)
        print("*Från och med nu kommer din ultimate-ability att göra 200 mera skada!*")
        sleep(2)
        print("Efter att du har tagit upp boken stängs genast de två andra pedestalerna.. och du blir magiskt knuffad bort från guldiga rummet...")
        sleep(2)
        print("Du är knuffad till goblin-källaren och ingången till guldkorridoren stängs genast med en kratta...")
        sleep(2)
        print("Det verkar som att du inge längre kan gå in i guldiga rummet...")
        sleep(2)
        print("Du har ett dörr bakom dig('gå bakåt') till fängelsehålans entré, krog-dörren till höger ('gå höger') och uppgradera ditt vapen hos goblin (endast en gång) med 2000 guldmynt 'upgrade'")
        dorrQ=input(">")
        dorrQ=dorrQ.lower()
        if dorrQ == "gå höger":
            sleep(2)
            tavernDoorLvl2()
            return uDamage
        elif dorrQ == "gå bakåt":
            sleep(2)
            firstDoorLvl2()
            return uDamage
        elif dorrQ == "upgrade":
            if guldmynt >= 2000:
                guldmynt = guldmynt - 2000
                damage = damage + 50
                print("Du visar guldet till herr goblin, han tar genast emot det")
                sleep(2)
                print("Han tar fram ett konstigt skrolla och tar ditt vapen...")
                sleep(2)
                print("Du blir lite nervös..")
                sleep(2)
                print("Han börjar att prata med ett konstigt språk...")
                sleep(2)
                print("Efter några sekunder är han redo")
                sleep(2)
                print("Goblin - Ditt vapen är nu uppgraderat med gamla nordiska runer")
                sleep(2)
                print("Goblin - Det kommer att göra 50 mer skada från och med nu!")
                sleep(2)
                print("Vad vill du göra nu?(gå bakåt) eller (gå höger)")
                goblinQ=input(">")
                goblinQ=goblinQ.lower()
                if goblinQ == "gå bakåt":
                    sleep(2)
                    firstDoorLvl2()
                    return damage, guldmynt, uDamage
                elif goblinQ == "gå höger":
                    sleep(2)
                    tavernDoorLvl2()
                    return damage, guldmynt, uDamage
                else:
                    print("Det verkar inte finnas något sånt du kan göra...")
                    goblinQ=input(">")
                    goblinQ=goblinQ.lower()
            else:
                print("Du har inte tillräckligt guldmynt...")
                dorrQ=input(">")
                dorrQ=dorrQ.lower()
        else:
            print("Det verkar inte finnas något sånt att göra i rummet...")
            sleep(2)
            dorrQ=input(">")
            dorrQ=dorrQ.lower()
    elif choice == "framåt":
        sleep(2)
        print("Du går fram till den mittersta pedestalen och tar upp guldhögen...")
        sleep(3)
        print("Du får sammanlagt 1000 guldmynt")
        guldmynt = guldmynt + 1000
        print(f"Du har sammanlagt {guldmynt} guldmynt")
        sleep(2)
        print("Efter att du har tagit upp varje mynt från högen, stängs båda ytterliggande pedestaler...")
        sleep(2)
        print("Du blir magiskt knuffad tillbaks till goblin-källaren...")
        sleep(2)
        print("Den guldiga-dörren stängs genast och du kan inte längre ta den vägen...")
        sleep(3)
        print("Vilken dörr väljer du? Fängelsehålans entré(gå bakåt), Krog-dörren(gå höger) eller uppgradera ditt vapen(endast en gång) för 2000 guldmynt")
        dorrQ2=input(">")
        dorrQ2=dorrQ2.lower()
        if dorrQ2 == "gå höger":
            sleep(2)
            tavernDoorLvl2()
        elif dorrQ2 == "gå bakåt":
            sleep(2)
            firstDoorLvl2()
        elif dorrQ2 == "upgrade":
            if guldmynt >= 2000:
                guldmynt = guldmynt - 2000
                damage = damage + 50
                print("Du visar guldet till herr goblin, han tar genast emot det")
                sleep(2)
                print("Han tar fram ett konstigt skrolla och tar ditt vapen...")
                sleep(2)
                print("Du blir lite nervös..")
                sleep(2)
                print("Han börjar att prata med ett konstigt språk...")
                sleep(2)
                print("Efter några sekunder är han redo")
                sleep(2)
                print("Goblin - Ditt vapen är nu uppgraderat med gamla nordiska runer")
                sleep(2)
                print("Goblin - Det kommer att göra 50 mer skada från och med nu!")
                sleep(2)
                print("Vad vill du göra nu?(gå bakåt) eller (gå höger)")
                goblinQ2=input(">")
                goblinQ2=goblinQ2.lower()
                if goblinQ2 == "gå bakåt":
                    sleep(2)
                    firstDoorLvl2()
                    return damage, guldmynt
                elif goblinQ2 == "gå höger":
                    sleep(2)
                    tavernDoorLvl2()
                    return damage, guldmynt
                else:
                    print("Det verkar inte finnas något sånt att göra...")
                    sleep(2)
                    goblinQ2=input(">")
                    goblinQ2=goblinQ2.lower()
            else:
                print("Du har inte tillräckligt guldmynt...")
                dorrQ2=input(">")
                dorrQ2=dorrQ2.lower()
        else:
            print("Det verkar inte finnas något sånt att göra i rummet...")
            sleep(2)
            dorrQ2=input(">")
            dorrQ2=dorrQ2.lower()
    elif choice == "höger":
        sleep(2)
        print("Du bestämmer dig att öppna kistan...")
        sleep(5)
        print("Inuti kistan hittar du ingenting...")
        sleep(2)
        print("De andra två pedestaler stängs genast... och du blir knuffad tillbaks till goblin källaren...")
        sleep(2)
        print("Den guldiga-dörren stängs direkt och det verkar inte som att du kan ta den vägen längre...")
        sleep(2)
        print("Vilken dörr väljer du? Fängelsehålans entré(gå bakåt), Krog-dörren(gå höger) eller du kan uppgradera ditt vapen(endast en gång) för 2000 guldmynt")
        dorrQ3=input(">")
        dorrQ3=dorrQ3.lower()
        if dorrQ3 == "upgrade":
            if guldmynt >= 2000:
                guldmynt = guldmynt - 2000
                damage = damage + 50
                print("Du visar guldet till herr goblin, han tar genast emot det")
                sleep(2)
                print("Han tar fram ett konstigt skrolla och tar ditt vapen...")
                sleep(2)
                print("Du blir lite nervös..")
                sleep(2)
                print("Han börjar att prata med ett konstigt språk...")
                sleep(2)
                print("Efter några sekunder är han redo")
                sleep(2)
                print("Goblin - Ditt vapen är nu uppgraderat med gamla nordiska runer")
                sleep(2)
                print("Goblin - Det kommer att göra 50 mer skada från och med nu!")
                sleep(2)
                print("Vad vill du göra nu?(gå bakåt) eller (gå höger)")
                goblinQ3=input(">")
                goblinQ3=goblinQ3.lower()
                if goblinQ3 == "gå bakåt":
                    sleep(2)
                    firstDoorLvl2()
                    return guldmynt, damage
                elif goblinQ3 == "gå höger":
                    sleep(2)
                    tavernDoorLvl2()
                    return guldmynt, damage
                else:
                    print("Det verkar inte finnas något sånt att göra...")
                    sleep(2)
                    goblinQ3=input(">")
                    goblinQ3=goblinQ3.lower()
            else:
                print("Du har inte tillräckligt guldmynt...")
                dorrQ3=input(">")
                dorrQ3=dorrQ3.lower()
        elif dorrQ3 == "gå bakåt":
            sleep(2)
            firstDoorLvl2()
        elif dorrQ3 == "gå höger":
            sleep(2)
            tavernDoorLvl2()
        else:
            print("Det verkar inte finnas något sånt att göra i rummet..")
            sleep(2)
            dorrQ3=input(">")
            dorrQ3=dorrQ3.lower()

def rightDoorLvl2():
    sleep(2)
    print("Nu befinner du dig i ett ganska smalt rum, verkligen liknar ett korridor..")
    sleep(2)
    print("Men du känner dig inte säker i rummet...")
    sleep(2)
    print("Du fortsätter gå genom korridoren, på väggarna finns det facklor som leder vägen fram till slutet av korridoren...")
    sleep(2)
    print("I slutet av korridoren ser du ett stort dörr som verkar vara bränt?")
    sleep(2)
    print("Du går ännu närmare den brända dörren då du märker att du har gått på en tryckplatta...")
    sleep(2)
    print("Plötsligt faller krattor över dörrarna...")
    sleep(2)
    print("Och den vänstra väggen öppnas...")
    sleep(2)
    print("Du märker att något finns bakom krattan men du har inte tid att ta ett bättre titt på det..")
    sleep(2)
    print("Genom dörren som öppnades i väggen kommer ut en gigantisk troll...")
    sleep(2)
    print("...")
    sleep(2)
    print("*VEM ÄR DET SOM VÅGAR KOMMA IN I MITT FÄNGELSEHÅLA?!...*")
    sleep(2)
    print("Trollen ser sig omkring, då han ser dig tar han upp sin gigantiska träklubba..")
    sleep(2)
    print("Du inser att det är dags att döda trollen...")
    sleep(3)
    print("DÖDA TROLLEN!")
    def fight():
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        global ryggsäck
        eHealth = 800
        sleep(2)
        while health > 0 and eHealth > 0:
            print(f"Du har {mana} mana kvar")
            if health <= 0:
                print("Du har dött, men ge inte upp än!")
                sleep(2)
                print("*STARTA OM FIGHTEN*")
                sleep(2)
                health = 300
                fight()
            if health > 0:
                action = input(">\n")
                action = action.lower()
                if action == "attack":
                    if eHealth <= 0:
                        eHealth=eHealth-damage
                        print("Trollen överlevde inte din autoattack!")
                    else:
                        eHealth=eHealth-damage
                        eAttTxt = random.choice(["Trollen faller omkull på grund av din mäkriga attack!\n", "Trollen skriker vilt efter att hen har blivit träffad med din attack...\n", "Trollen blir kraftigt träffad med din autoattack!\n"])
                        print(eAttTxt)
                        health=health-random.randint(10,15)
                        print(f"Du attackerade trollen med din auto-attack, den har {eHealth}hp kvar!\n")
                        print(f"Trollen attackerar tillbaks med sin gigantisk träklubba, du har {health}hp kvar..\n")
                elif action == "a" and mana >= 50:
                    if mana < 50:
                        print("Du har inte tillräckligt med mana..")
                    else:
                        if eHealth <= 0:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            print("Den gigantiska trollen överlevde inte din kraftfulla ability!")
                        else:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            eAbTxt = random.choice(["Trollen skriker av ondska då den blir träffad med din kraftfulla ability!", "Trollen faller omkull men lyckas ta sig upp efter din ability..."])
                            print(eAbTxt)
                            health=health-random.randint(10,15)
                            print(f"Du attackerade TROLLEN med din kraftfulla ability, den har {eHealth}hp kvar!\n")
                            print(f"TROLLEN tar sig upp igen och slår tillbaks med sin gigantiska klubba, du har {health}hp kvar...")
                elif action == "u" and mana >= 100:
                    if mana < 100:
                        print("Du har inte tillräckligt med mana..")
                    else: 
                        if eHealth <= 0:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            print("Den stora TROLLEN överlevde inte din kraftfulla ultimate!")
                        else:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            eUTxt = random.choice(["Trollen blir mycket kraftigt träffad med din ultimate!", "Trollen slår i väggen efter att den har blivit träffad med din kraftfulla ultimate!"])
                            print(eUTxt)
                            print(f"TROLLEN blir träffad med din ultimate-ability och tar enorm skada, den har {eHealth}hp kvar!")
                            print("TROLLEN lyckas inte ta sig upp efter att hen har blivit träffad med din ultimate, du tar ingen skada!")
                elif action == "hp":
                    for healthPotion in ryggsäck:
                        if healthPotion == "Livselixir":
                            health=health+100
                            print(f"Du har {health}hp kvar")
                            if health >= 500:
                                health=500
                            else:
                                ryggsäck.remove("Livselixir")
                                print(ryggsäck)
                elif action == "mana":
                    for manaPotion in ryggsäck:
                        if manaPotion == "Manaelixir":
                            mana=mana+100
                            print(f"Du har {mana} mana kvar")
                            if mana >= 200:
                                mana=200
                            else:
                                ryggsäck.remove("Manaelixir")
                                print(ryggsäck)
                elif action == "berserker":
                    for berserkerPotion in ryggsäck:
                        if berserkerPotion == "Berserker":
                            damage = damage + 50
                else:
                    print("Du kan använda följande inputs: mana(manaelixir), hp(livselixir), attack(auto-attack), a(ability), u(ultimate)")
                    sleep(2)
                    action = input(">\n")
                    action = action.lower()

    fight()
    sleep(5)
    print("Du har dödat TROLLEN!")
    sleep(2)
    print("Krattorna lyfter sig och du har nu tillgång till två nya vägar!")
    sleep(3)
    print("Du kan gå igenom den öppna väggen (där trollen kom ifån('gå vänster')) eller gå vidare genom dörren i slutet av korridoren('gå framåt')")
    dorrChoice=input(">\n")
    dorrChoice=dorrChoice.lower()
    if dorrChoice == "gå framåt":
        print("Du bestämmer dig att gå vidare genom dörren i slutet av korridoren...")
        sleep(2)
        bossKorridorLvl2()
    elif dorrChoice == "gå vänster":
        print("Du väljer att kika in i rummet där TROLLEN kom ifrån..")
        sleep(2)
        trollChamber()
    else:
        print("Det verkar inte finnas något sånt att göra i rummet..")
        dorrChoice=input(">\n")
        dorrChoice=dorrChoice.lower()

def bossKorridorLvl2():
    print("Du går in igenom den mystiska dörren...")
    sleep(5)
    print("Rummet ser väldigt legendariskt ut..")
    sleep(2)
    print("Framför dig finns en gigantisk dörr med en stor dödsskalle ovan...")
    sleep(2)
    print("På väggarna ser du flera brinnande eld flammor, det verkar farligt...")
    sleep(2)
    print("Vad vill du göra?")
    choice=input(">")
    choice=choice.lower()
    if choice == "gå framåt":
        sleep(2)
        bossRoomLvl2()
    elif choice == "gå bakåt":
        print("Du är fortfarande rädd att gå genom dörren med dödsskallen...")
        sleep(2)
        print("Du går tillbaks till fängelsehålans entré..")
        firstDoorLvl2()
    else:
        print("Det verkar inte finnas något sånt att göra i rummet...")
        sleep(2)
        print("Du kan gå framåt(genom den gigantiska dörren) eller bakåt (tillbaks till fängelsehålans entré)")
        choice=input(">")
        choice=choice.lower()

def bossRoomLvl2():
    print("Du går genom den gigantiska dörren...")
    sleep(2)
    print("Du börjar undra när du kommer äntligen kunna lämna grottan och leva fritt igen...")
    sleep(2)
    print("Hela grottan verkar vara en stor fälla som draken använder för sin fånge...")
    sleep(2)
    print("Du ser dig omkring i rummet...")
    sleep(6)
    print("Hela rummet ser ut som en arena, du ser lava rinnande från taket...")
    sleep(2)
    print("Du känner att marken skakar på sig...")
    sleep(2)
    print("Du hör en främmande röst...")
    sleep(2)
    print("...")
    sleep(2)
    print("*** DU HAR KOMMIT GANSKA LÅNGT... ***")
    sleep(3)
    print("*** JAG GISSADE PÅ ATT DU ALDRIG SKULLE KOMMA FRAM TILL MITT HEM... ***")
    sleep(2)
    print("*** MEN NU NÄR DU ÄR HÄR... ***")
    sleep(3)
    print("*** KOMMER DU ATT ***")
    sleep(10)
    print("*** DÖ!!!... ***")
    sleep(3)
    print("Plötsligt ser du DRAKEN klättra ner från taket...")
    sleep(2)
    print("Det är ditt enda chans att ta dig ur detta stället...")
    sleep(2)
    print("DU MÅSTE DÖDA DRAKEN!")
    sleep(2)
    print("""
                                                         /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ |
                   {\__--_/}    / \\_>- )<__\      |
                   /'   (_/  _-~  | |__>--<__|      |
                  |0  0 _/) )-~     | |__>--<__|     |
                  / /~ ,_/       / /__>---<__/      |
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~
         `-)) )) (           |__>--<__|    |               /'  /     ~\`
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `   """)
    def fightBossDRAGON():
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        global ryggsäck
        global guldmynt
        eHealth = 2000
        sleep(4)
        while eHealth > 0:
            if health <= 0:
                print("Du har dött...")
                sleep(2)
                print("Men ge inte upp än!")
                sleep(2)
                print("STARTAR OM BOSS FIGHTEN")
                sleep(1)
                health = 300
                fightBossDRAGON()
            if health > 0:
                action = input("Du står framför DRAKEN \n \n DÖDA DEN!! >")
                action=action.lower()
                if action == "attack":
                    if eHealth <= 0:
                        eHealth=eHealth-damage
                        print("DRAKEN överlevde inte din autoattack!")
                    else:
                        eHealth=eHealth-damage
                        eAttTxt = random.choice(["DRAKEN förlorar en av sina mäktiga tänder!\n \n", "DRAKEN skriker vilt!\n \n", "DRAKEN - Hur vågar du attackera mig!?...\n \n"])
                        print(eAttTxt)
                        print(f"Du attackerade DRAKEN!\n")
                        sleep(1)
                        print(f"DRAKEN blir träffad med din auto-attack, den har {eHealth}hp kvar!")
                        sleep(1)
                        health = health - random.randint(10,15)
                        print(f"DRAKEN attackerar dig med sin långa svans... Du har \n \n {health}hp kvar...")
                elif action == "a":
                    if mana < 50:
                        print("Du har inte tillräckligt med mana...")
                    else:
                        if eHealth <= 0:
                            mana = mana-50
                            eHealth = eHealth - aDamage
                            print("DRAKEN överlevde inte din kraftfulla ability!")
                        else:
                            mana = mana - 50
                            eHealth = eHealth - aDamage
                            health=health - random.randint(10,15)
                            eAbTxt = random.choice(["\n \nDRAKEN skriker vilt efter att den blir träffad med din kraftfulla ability!", "DRAKEN skakar av sig efter din kraftfulla ability!"])
                            print(eAbTxt)
                            print(f"DRAKEN blev träffad med din ability, den har {eHealth}hp kvar!")
                            print(f"DRAKEN attackerar tillbaks... Du har {health}hp kvar...\n")
                            print(f"Du har {mana} mana kvar")
                elif action == "u":
                    if mana < 100:
                        print("Du har inte tillräckligt med mana")
                    else:
                        if eHealth <= 0:
                            mana = mana - 100
                            eHealth = eHealth - uDamage
                            print("DRAKEN överlevde inte din kraftfulla ultimate!!")
                        else:
                            mana = mana - 100
                            eHealth = eHealth - uDamage
                            health=health - random.randint(15,25)
                            eUTxt = random.choice(["SKELETT-KUNGEN förlorar kontrollen och faller på knäna!", "SKELETT-KUNGEN blir träffad med din ultimate och tar emot stor skada!"])
                            print(eUTxt)
                            print("Du träffade SKELETT-KUNGEN med din kraftfulla Ultimate!")
                            sleep(1)
                            print(f"DRAKEN blir träffad med din ultimate-ability, den tar emot enorm skada, den har {eHealth}hp kvar!") 
                            print(f"DRAKEN förlorar kontrollen och faller ner till marken, den lyckas inte att attackera tillbaks!\n")
                            print(f"Du har {mana} manakvar")
                elif action == "hp":
                    for healthPotion in ryggsäck:
                        if healthPotion == "Livselixir":
                            health=health+100
                            if health >= 500:
                                health=500
                                print(health)
                            else:
                                print(health)
                                ryggsäck.remove("Livselixir")
                                print(ryggsäck)
                elif action == "mana":
                    for manaPotion in ryggsäck:
                        if manaPotion == "Manaelixir":
                            mana=mana+100
                            if mana >= 200:
                                mana=200
                                print(mana)
                            else:
                                print(health)
                                ryggsäck.remove("Manaelixir")
                                print(ryggsäck)
                elif action == "berserker":
                    for berserkerPotion in ryggsäck:
                        if berserkerPotion == "Berserker":
                            damage=damage+50
                else:
                    print("Du kan använda en av följande inputs: attack, u(ultimate), a(ability), hp(Livselixir) eller mana(manaelixir)")
                    sleep(5)

    fightBossDRAGON()
    sleep(5)
    print("""
                                                                                                
                                                                                        
                                            ██                                          
                                            ██                                          
                                            ██                                          
                                      ██████████████                                    
                                            ██                                          
                                            ██                                          
                              ██████████    ██    ██████████                            
                            ██████  ██████████████████  ██████                          
                            ████        ██████████        ████                          
                      ██████████                          ██████████                    
                    ██████  ████                          ████  ██████                  
                    ████                ██████████                ████                  
                    ████      ████        ██████        ████      ████                  
                    ██████    ████        ██████        ████    ██████                  
                    ████████    ██        ██████        ██    ████████                  
                      ████████    ██      ██████      ██    ████████                    
                        ██████      ██    ██████    ██      ██████                      
                          ██████    ████  ██████  ████    ██████                        
                          ██████████████  ██████  ██████████████                        
                            ██████████████████████████████████                          
                            ████  ████  ████  ████  ████  ████                          
                          ██████████████████████████████████████                        
                          ██████████████████████████████████████                        
                          ██████████████████████████████████████                        
                                                                                        
                                                                                        
                                                                                        """)
    sleep(2)
    print("Du besegrade draken!!!")
    sleep(2)
    print("Plötsligt märker du en bro som faller ned och på andra sidan ser du en stege...")
    sleep(2)
    print("Du ser solen för första gången efter så länge...")
    sleep(2)
    print("Du går uppför stegen, längst uppe ser du en by långt borta och ett brinnande träd...")
    sleep(2)
    print("DU HAR KOMMIT UT!")
    sleep(2)
    print("*** THE END ***")
    sleep(2)
    print("PRODUCTION: \n \n Artur Kaminski \n \n Adrian Stude")

def trollChamber():
    global ryggsäck
    global damage
    global guldmynt
    print("Du befinner dig nu i ett väldigt konstigt rum..") 
    sleep(2)
    print("Det verkar som att TROLLEN levde i fängelsehålan..")
    sleep(2)
    print("Du ser en gigantisk säng, gigantisk kök, det liknar ett vanligt hem men allt är jättestort..")
    sleep(2)
    print("Du ser inga fler dörrar, enda öppningen är den du kom ifrån('gå bakåt')")
    sleep(2)
    print("Vad vill du göra?")
    choice=input(">")
    choice=choice.lower()
    if choice == "gå bakåt":
        sleep(2)
        print("Du är nu tillbaka i den mystiska korridoren, vad vill du göra?")
        korridorChoice = input(">")
        korridorChoice=korridorChoice.lower()
        if korridorChoice == "gå bakåt":
            sleep(2)
            firstDoorLvl2()
        elif korridorChoice == "gå framåt":
            sleep(2)
            bossKorridorLvl2()
        else:
            print("Det verkar inte finnas något sånt att göra i korridoren..")
            korridorChoice = input(">")
            korridorChoice=korridorChoice.lower()
    elif choice == "search":
        print("Du söker igenom Troll-bon..")
        sleep(10)
        print("Du hittar 2 Livselixir, 2 Manaelixir och 500 guldmynt!")
        guldmynt = guldmynt + 500
        ryggsäck.append("Livselixir")
        ryggsäck.append("Livselixir")
        ryggsäck.append("Manaelixir")
        ryggsäck.append("Manaelixir")
        print(ryggsäck)
        sleep(2)
        print("Du letade igenom det gigantiska rummet och hittade ett kista under sängen..")
        sleep(2)
        print("Vill du öppna kistan?")
        caseQ=input(">")
        caseQ=caseQ.lower()
        if caseQ == "ja":
            damage = damage + 30
            print("Du öppnar den stora kistan..")
            sleep(5)
            print("Inuti kistan hittar du en rune-bok...")
            sleep(2)
            print("Du bläddrar igenom boken fort och känner dig starkare!")
            sleep(2)
            print("Från och med nu kommer din ultimate att göra 200 mer skada!")
            sleep(2)
            print("Du hittar inget mer som du skulle kunna göra i rummet, du bestämmer dig att gå ut från grottan..")
            sleep(10)
            print("Du befinner dig i den mystiska korridoren")
            sleep(2)
            print("Vad vill du göra?")
            korridorChoice = input(">")
            korridorChoice=korridorChoice.lower()
            if korridorChoice == "gå bakåt":
                sleep(2)
                firstDoorLvl2()
                return damage, guldmynt
            elif korridorChoice == "gå framåt":
                sleep(2)
                bossKorridorLvl2()
                return damage, guldmynt
            else:
                print("Det verkar inte finnas något sånt att göra i korridoren..")
                korridorChoice = input(">")
                korridorChoice=korridorChoice.lower()
        elif caseQ == "nej":
            print("Du lämnar kistan och hittar inget annat i rummet att göra..")
            sleep(3)
            print("Du går tillbaka till den mystiska korridoren..")
            sleep(2)
            print("Nu befinner du dig i den mystiska korridoren")
            sleep(2)
            print("Vad vill du göra?")
            korridorChoice = input(">")
            korridorChoice=korridorChoice.lower()
            if korridorChoice == "gå bakåt":
                sleep(2)
                firstDoorLvl2()
            elif korridorChoice == "gå framåt":
                sleep(2)
                bossKorridorLvl2()
            else:
                print("Det verkar inte finnas något sånt att göra i korridoren..")
                korridorChoice = input(">")
                korridorChoice=korridorChoice.lower()
        else:
            print("Du kan antingen svara 'ja' eller 'nej'")
            caseQ=input(">")
            caseQ=caseQ.lower()
    else:
        print("Det verkar inte finnas något sånt att göra i rummet...")
        sleep(3)
        print("Du kan gå tillbaka till korridoren genom att skriva in 'gå bakåt'")
        caseQ=input(">")
        caseQ=caseQ.lower()

#trädörren
def lootrum(): 
    global ryggsäck
    print("Du går in genom den öppna trä dörren")
    sleep(1)
    print("Plötsligt stängs dörren bakom dig och du ser en levande skelett springa mot dig \n")
    sleep(1)
    def fightS():
        global health
        global damage
        global uDamage
        global aDamage
        global mana
        global ryggsäck
        eHealth = 200
        tutorial()
        sleep(2)
        while eHealth > 0:
            print(f"Du har {mana} mana kvar\n")
            if health <= 0:
                print("Du har dött, men ge inte upp!")
                sleep(1)
                print("*STARTAR OM FIGHTEN*")
                health=300
                fightS()
            if health > 0:
                action = input(f"Du står framför skeletten, döda den!\n \n >")
                action=action.lower()
                if action == "attack":
                    if eHealth <= 0:
                        eHealth=eHealth - damage
                        print("skeletten överlevde inte din autoattack!")
                    else:
                        eHealth=eHealth - damage
                        eAttTxt = random.choice(["Dess ben delar flyger omkring i rummet!\n", "Skeletten skriker vilt!\n", "Skeletten kunde inte försvara sig!\n"])
                        print(eAttTxt)
                        print(f"Du attackerade skeletten, den har {eHealth}hp kvar!\n")
                        print(f"Skeletten slår tillbaks! Du har {health}hp kvar!\n")
                        health=health - random.randint(3,6)
                elif action == "a" and mana >= 50:
                    if mana < 50:
                        print("Du har inte tillräckligt med mana")
                    else:
                        if eHealth <= 0:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            print("skeletten överlevde inte din kraftfulla ability!")
                        else:
                            eHealth = eHealth - aDamage
                            mana = mana - 50
                            eAbTxt = random.choice(["\n \nSkeletten flyger bort mot väggen efter att den har tagit emot din kraftfulla ability!", "Skeletten skriker av ondska då du träffar den med din ability!"])
                            health=health - random.randint(3,6)
                            print(eAbTxt)
                            print(f"Du attackerade skeletten med din kraftfulla ability! \n \n den har {eHealth}hp kvar!\n")
                            print(f"Skeletten tar sig upp och attackerar tillbaka! Du har {health}hp kvar!\n")
                elif action == "u" and mana >= 100:
                    if mana < 100:
                        print("Du ha inte tillräckligt mana!")
                    else:
                        if eHealth <= 0:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            print("Skeletten överlevde inte ditt kraftfulla ultimate!")
                        else:
                            eHealth = eHealth - uDamage
                            mana = mana - 100
                            eUTxt = random.choice(["\n \nSkeletten flyger bort mot väggen efter att den har tagit emot din kraftfulla ultimate-ability!", "Skeletten skriker av ondska då du träffar den med din ability!"])
                            print(eUTxt)
                            print(f"\nSkeletten blir träffad med din ultimate ability! Den tar enorm skada, den har {eHealth}hp kvar!")
                            sleep(1)
                            print("\n \n Skeletten kunde inte ta sig upp i tid för att attackera dig tillbaka, du förlorar ingen hp!")
                elif action == "hp":
                    for healthPotion in ryggsäck:
                        if healthPotion == "Livselixir":
                            health=health+100
                            if health >= 500:
                                health=500
                            else:
                                ryggsäck.remove("Livselixir")
                                print(ryggsäck)
                elif action == "mana":
                    for manaPotion in ryggsäck:            
                        if manaPotion == "Manaelixir":
                            mana=mana+50
                            if mana >= 200:
                                mana=200
                            else:
                                ryggsäck.remove("Manaelixir")
                                print(ryggsäck)
                else:
                    action = input("Du kan använda följande inputs: hp(Livselixir), mana(Manaelixir), attack(auto-attack), a(ability), u(ultimate)")
                    action=action.lower()

    fightS()
    print("**Du har nu dödat din första fiende!** \n")
    sleep(1)
    print("**Du kommer genom spelets gång behöva döda många fler för att gå vidare...**")
    sleep(1)
    print(f"Du har {mana} mana kvar efter fighten")
    sleep(1)
    print("**Kom ihåg att använda dina abilities och kontrollera din health, lycka till!**\n")
    sleep(1)
    print("Efter att du har dödat skeletten, har dörrarna öppnats")
    sleep(1)
    print("Du ser dig omkring i rummet efter att ha lugnat ned sig..")
    sleep(1)
    print("Du ser inget märkligt förutom några gamla dammiga hyllor, kanske vore det smart att leta igenom dem?..")
    sleep(1)
    leta = input("Vad vill du göra \n \n du kan gå tillbaka till första rummen och testa ett annat dörr genom att skriva 'gå bakåt' \n \n eller leta igenom rummet genom att skriva 'search'")
    leta = leta.lower()
    if leta == "gå bakåt":
        sleep(2)
        förstarummet()
    elif leta == "search":
        sleep(2)
        ryggsäck.append("Livselixir")
        print(f"Ryggsäck: {ryggsäck}\n")
        print("Du söker igenom alla dammiga hyllor och du hittar en livselixir!\n")
        sleep(2)
        print("*Livs elixir kan du använda under fightens gång genom att skriva 'hp' då du märker att ditt hp är lågt*")
        sleep(2)
        print("Nu har du letat igenom rummet och det verkar inte finnas något mer du kan göra, gå tillbaka till grottöppningen och välj ett annat dörr!('gå bakåt')")
        val=input(">")
        val=val.lower()
        if val == "gå bakåt":
            förstarummet()
        else:
            print("Det finns inget kvar att göra i rummet")
            val=input(">")
            val=val.lower()
    else:
        print("Det verkar inte finnas något annat du kan göra i rummet, välj en av alternativen!")
        leta = input("Vad vill du göra \n \n du kan gå tillbaka till första rummen och testa ett annat dörr genom att skriva 'gå bakåt' \n \n eller leta igenom rummet genom att skriva 'search'")
        leta = leta.lower()


def tutorial():
    print("                                               *****Fight tutorial*****\n")
    sleep(2)
    print("                                  Kom ihåg att använda dina abilities under spelets gång! \n")
    sleep(2)
    print("               Fienden kommer alltid att attackera efter dig, alltså är det möjligt att gå ut ur fighten utan skada \n")
    sleep(2)
    print("                    Du måste även kontrollera ditt hp, det kommer att skrivas ut efter varje fiendes attack \n") 
    sleep(2)
    print("Du kan använda dina elixir under fightens gång, istället för att skriva exempelvis 'attack' kan du skriva hp(livselixir) eller mana(manaelixir) \n")
    sleep(2)
    print("            Du måste tänka strategiskt, dina abilities är värdefulla och väldigt dyra, du måste tänka efter dina steg \n")
    sleep(2)
    print("                 Du kan använda dina abilities genom att under fightens gång skriva a och ultimate genom 'u' \n")

start()
grottöppning()