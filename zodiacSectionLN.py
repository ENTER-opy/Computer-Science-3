import time

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)

def CheckCHZodiac():
    try:
        Birthyear = int(input("Please input your birthyear (Must not be earlier than 1900): "))
    except ValueError:
        print("Invalid input. Please enter a valid numerical year.")
        exit()
    CHzodsigns = [
        ["Rat (鼠 / Shǔ)",0],
        ["Ox (牛 / Niú)",1],
        ["Tiger (虎 / Hǔ)",2],
        ["Rabbit (兔 / Tù)",3],
        ["Dragon (龙 / Lóng)",4],
        ["Snake (蛇 / Shé)",5],
        ["Horse (马 / Mǎ)",6],
        ["Goat (羊 / Yáng)",7],
        ["Monkey (猴 / Hóu)",8],
        ["Rooster (鸡 / Jī)",9],
        ["Dog (狗 / Gǒu)",10],
        ["Pig (猪 / Zhū)",11]
    ]
    if Birthyear>=1900:
        index = int((Birthyear - 1900) % 12)
        print(index)
        zodsign = CHzodsigns[index][0]
        print(f"You were born in the Year of The: {zodsign}")
        XtraInf(CHzodsigns[index][1])

    else:
        print("INVALID! YEAR MUST NOT BE EARLIER THAN 1900")
        exit()

def XtraInf(n):
    yn= input('Would you like to learn more about your Chinese Zodiac Sign? (y/n):')
    if yn == 'y':
        print(n)
        typing_effect('YOUR CHINESE ZODIAC IS...\n'
              f'\n{ZodGlos[n]}')

ZodGlos= ['THE RAT\n'
          '•\n'
          '•\n'
          'the Rat, or 鼠 (shǔ), which cleverly raced its way to first place, becoming the lead animal in the Chinese zodiac!\n'
'The Rat is much more than just a furry creature to the Chinese. It symbolizes cleverness and is believed to bring good luck in solving problems. And even though it’s small, it stands for big concepts like wealth and new beginnings.\n'
'People born under this sign are often seen as intelligent problem-solvers.\n'
'In countless stories, the Rat smoothly navigates through tricky situations. This teaches us a lesson or two about the value of smart thinking and being adaptable in our own lives.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the RAT:\n'
          '•King Charles,\n'
          '•Cameron Diaz,\n'
          '•Wolfgang Amadeus Mozart,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 2,3'
'\nLUCKY COLORS: BLUE, GOLD, GREEN\n'
'\nUNLUCKY NUMBERS:5, 9'
'\nUNLUCKY COLORS: YELLOW, BROWN'
          ,
        'THE OX \n'
        '•\n'
        '•\n'
'The Ox, or 牛 (niú), earned second place in the zodiac race.'
'\nIn China, the Ox is seen as a very special animal. Believe it or not, many people in China choose not to eat beef. That’s because, especially for families who farm, the ox is often treated like a part of the family.'
'\nOxen mean a lot in Chinese culture. They stand for things like wealth, good luck, being hard-working and never giving up. They’re super strong and can work in the fields all day, which shows us a picture of what it looks like to keep going and never quit.'
'\nPeople born in the Year of the Ox are thought to be hard-working and honest, just like the oxen in the fields. They do their work without making a fuss or needing to be in the spotlight.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the OX:\n'
          '•Adolf Hitler!,\n'
          '•Barrack Obama,\n'
          '•Bruno Mars,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 1,4'
'\nLUCKY COLORS: WHITE, YELLOW, GREEN\n'
'\nUNLUCKY NUMBERS:5, 6'
'\nUNLUCKY COLORS: BLUE'
          ,
        'THE TIGER \n'
        '•\n'
        '•\n'
'the Tiger, or 虎 (hǔ), which claimed the third spot in the zodiac race with its striking presence! Can you feel the energy and power just thinking about it?\n'
'In China, Tigers are seen as symbols packed with vitality, courage, and majestic power. But here’s a little curveball – being a Tiger in the zodiac isn’t always seen as good due to its sometimes wild temperament.\n'
'However, let’s pounce on a fun fact that might just surprise you: did you know that when tiger babies grow up, they often find themselves at the top? Yes, they frequently perch atop the Forbes 300 list of the wealthiest people in the world!\n'
'Even with their sometimes feisty nature, it seems like Tigers know a thing or two about climbing to the top and securing success.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the TIGER:\n'
          '•Queen Elizabeth,\n'
          '•Fidel Castro,\n'
          '•Tom Cruise,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 1 , 3 , 4'
'\nLUCKY COLORS: BLUE , GRAY , ORANGE\n'
'\nUNLUCKY NUMBERS:6 , 7, 8'
'\nUNLUCKY COLORS: BROWN'
          ,
        'THE RABBIT \n'
        '•\n'
        '•\n'
'Fourth place in the zodiac race, we find the gentle Rabbit, or 兔 (tù).\n'
'In Chinese culture, the Rabbit isn’t just a cute, furry friend. It stands for graciousness, kindness, and a warm heart, spreading vibes of compassion, tenderness, and sheer elegance wherever it goes.\n'
'Here’s a little moonlit mystery for you: while folks in the Western world talk about seeing a man on the moon, Chinese lore spots a Jade Rabbit (玉兔) up there! This celestial bunny is so prominent in Chinese culture that China named its first lunar rover “Jade Rabbit”!\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the RABBIT:\n'
          '•Bugs Moran,\n'
          '•Albert Einstein,\n'
          '•Marie Curie,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 3 , 4 , 6'
'\nLUCKY COLORS: RED , PINK , PURPLE , BLUE\n'
'\nUNLUCKY NUMBERS:1 , 7 , 8'
'\nUNLUCKY COLORS: DARK BROWN, DARK YELLOW, WHITE'
          ,
        'THE DRAGON \n'
        '•\n'
        '•\n'
        'the Dragon, known as 龍 (lóng) in traditional Chinese and 龙 (lóng) in simplified Chinese.\n'
'Even though the Dragon ended the famous zodiac race in fifth place, it is very special in Chinese culture.\b'
'It’s a big symbol of power and good luck and is often connected with rulers and emperors.\n'
'There’s a saying — 龍的傳人/龙的传人 (lóng de chuánrén) — which means “descendants of the dragon.” It shows how Chinese people feel a strong link to this mighty and magical creature.\n'
'A lot of families in China dream about having a dragon baby boy. They think it will bring good luck and that he will have a bright future and successful career.\n'
'But there’s a tricky part! When lots of dragon babies are born in the same year, it means they might have to compete harder with each other for chances later on, like getting into a good school or finding a job.\n'
'The story of the Dragon mixes old traditions with modern-day life, weaving a rich tale of the past meeting the present.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the DRAGON:\n'
          '•Vladimir Putin,\n'
          '•Bruce Lee,\n'
          '•Keanu Reeves,\n'
          '•Martin Luther King Jr.,\n'
          '•Jack Ma,\n'
          '•Sigmund Freud,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 1 , 6 , 7'
'\nLUCKY COLORS: GOLD, SILVER, GRAYISH WHITE\n'
'\nUNLUCKY NUMBERS: 3 , 8'
'\nUNLUCKY COLORS: BLUE , GREEN'
          ,
        'THE SNAKE \n'
        '•\n'
        '•\n'
        'In the sixth spot, we have the Snake or 蛇 (shé), a creature steeped in mystique and awe in Chinese culture.\n'
'Often referred to as the “little dragon” or 小龍/小龙 (xiǎo lóng), the Snake isn’t just a reptile in Chinese tradition but a symbol thought to foretell the future. Calm yet mysteriously enchanting, Snakes are believed to have the power to extend life.\n'
'Here’s a curious tidbit: if a Snake makes its way into a house, think twice before shooing it away! Killing a snake, especially one that enters a dwelling, is considered unlucky.\n'
'Why? Because that slithery visitor might just be bringing some good fortune your way!\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the SNAKE:\n'
          '•J.K Rowling,\n'
          '•Bob Dylan,\n'
          '•John F Kennedy,\n' 
          '•You!\n'
        '•Audrey Hepburn (not you)\n'
'\nLUCKY NUMBERS: 2 , 8 , 9'
'\nLUCKY COLORS: RED , BLACK , YELLOW\n'
'\nUNLUCKY NUMBERS:1 , 7 , 6'
'\nUNLUCKY COLORS: BROWN, GOLD, WHITE'
          ,
        'THE HORSE \n'
        '•\n'
        '•\n'
        'the Horse, or 馬/马 (mǎ), secured the seventh place in the Great Zodiac Race.\n'
'Horses aren’t just valued for their physical strength in Chinese culture; they symbolize much more – think faithfulness, nobility, and an indomitable spirit that simply can’t be beaten!\n'
'Let’s ride into an intriguing fact: the outstanding horses in Chinese history are hailed as 千里馬/千里马 (qiān lǐ mǎ), translating to “thousand-kilometer horses.” This is a nod to their incredible ability to cover a staggering 1,000 kilometers in just one day.\n'
'Did you know that praising someone as a “千里馬/千里马” is one of the highest compliments, likening their talents to the remarkable abilities of these legendary horses?\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the HORSE:\n'
          '•Arethra Franklin,\n'
          '•Jimi Hendrix,\n'
          '•Frederic Chopin,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 2 , 3 , 7'
'\nLUCKY COLORS: YELLOW , GREEN\n'
'\nUNLUCKY NUMBERS:1 , 5 , 6'
'\nUNLUCKY COLORS: BLUE , WHITE'
          ,
        'THE GOAT \n'
        '•\n'
        '•\n'
        'Bounding into the eighth position in the renowned zodiac race; the Goat, or 羊 (yáng). In the rich tapestry of Chinese culture, the Goat is often seen as a beacon of good luck, peace, and auspicious vibes.\n'
'The Goat is not just about star-studded facts. This gentle creature, despite its traditional symbolism of prosperity and positivity, has faced some modern-day dilemmas in China.\n'
'In recent times, some folks associate the Goat with being “meek and destined for slaughter,” which has surprisingly led to a dip in birth rates during the Goat years.\n'
'There’s no denying that many “Goats” have climbed to remarkable heights, proving that every zodiac sign has its own unique and incredible story to tell.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the GOAT:\n'
          '•Steve Jobs,\n'
          '•Thomas Edison,\n'
          '•Julia Roberts,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 2 , 7'
'\nLUCKY COLORS: RED , BROWN , PURPLE\n'
'\nUNLUCKY NUMBERS:4 , 9'
'\nUNLUCKY COLORS: BLUE , BLACK'
          ,
        'THE MONKEY \n'
        '•\n'
        '•\n'
         'the ninth spot in the Zodiac race is reserved for the clever Monkey, or 猴 (hóu). These curious and playful creatures have a special place in Chinese tales and traditions.\n'
'One monkey in particular leaps out from the rest: The Monkey King, Sun Wukong, or 孫悟空. This rebellious yet heroic figure doesn’t just settle with causing a ruckus in heaven; he also becomes a key character in the famous journey to the West alongside the monk Xuan-Zang (玄奘). This legendary monkey doesn’t just stop at old folktales but continues to frolic and create mischief in modern times too!\n'
'The tales of the Monkey King have transcended time, sparking TV shows, movies, and various entertainment products. Sun Wukong has leapt out of ancient stories to become a global cultural icon, spreading the whimsical and bold spirit of the Monkey across generations and borders.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the MONKEY:\n'
          '•Will Smith,\n'
          '•Tom Hanks,\n'
          '•Ryan Gosling,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 3 , 4 , 6'
'\nLUCKY COLORS: WHITE , BLUE , GOLD\n'
'\nUNLUCKY NUMBERS:2 , 7'
'\nUNLUCKY COLORS: RED , PINK'
          ,
        'THE ROOSTER \n'
        '•\n'
        '•\n'
        'Tenth place in the zodiac race, the Rooster, or 雞/鸡 (jī). With a hearty crow to announce the dawn, the Rooster doesn’t just wake us up from our slumbers but also plays a vital role in Chinese symbolism and culture.\n'
'Roosters aren’t just your average barnyard birds in the vast expanse of Chinese traditions. They stand as beacons of honesty, lighting the way with their moral and physical strength.\n'
'Their unabashed confidence and somewhat pompous demeanor are easily spotted, yet beneath those flamboyant feathers lie motivation and unyielding spirit.\n'
'Yes, they may love to flaunt their vibrant plumes and capture attention with their loud crows, but Roosters also teach us the value of standing tall and embracing our own colors.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the ROOSTER:\n'
          '•Jack Black,\n'
          '•Matthew Mc Conaughey,\n'
          '•Jeniffer Aniston,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 4 , 9'
'\nLUCKY COLORS: WHITE , BLUE , GOLD\n'
'\nUNLUCKY NUMBERS:1 , 3 , 9'
'\nUNLUCKY COLORS: RED'
          ,
        'THE DOG \n'
        '•\n'
        '•\n'
        'the 11th position in our zodiac adventure is the Dog, or 狗 (gǒu).\n'
'Beloved in both the East and West, dogs have always wagged their tails firmly in our cultural histories and personal stories.\n'
'Known for their steadfast loyalty, dogs in the Chinese zodiac are not just furry companions but also symbols of sincere friendship and unwavering support. They’re seen as creatures who care deeply and bring joy with their playful antics.\n'
'Not only our everyday companions, but dogs also find themselves in the company of well-known figures. Winston Churchill and Justin Bieber are just a few names from the long list of those born in the Year of the Dog.'
'\nNOTABLE PEOPLE BORN UNDER the Year of the DOG:\n'
          '•Elvis Presley,\n'
          '•Micheal Jackson,\n'
          '•Donald Trump,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 3 , 4 , 9'
'\nLUCKY COLORS: RED , GREEN , PURPLE\n'
'\nUNLUCKY NUMBERS:1 , 7 , 6'
'\nUNLUCKY COLORS: BLUE , GOLD , WHITE'
          ,
        'THE PIG \n'
        '•\n'
        '•\n'
        'Lastly, but certainly not least, let’s give a warm welcome to the Pig, or 豬/猪 (zhū), who leisurely strolled into the 12th place in the zodiac race.\n'
'Unlike its often negative portrayal in the West as greedy and lazy, the Pig in Chinese culture is admired and loved for its joyful, carefree spirit and its ability to enjoy life’s pleasures without a rush.\n'
'The Pig didn’t sprint to the finish line in the legendary race. Instead, it took its sweet time, savoring the journey and soaking in all the sights along the way. And who can blame it?\n'
'Pigs symbolize wealth, prosperity, and good fortune in Chinese culture. They’re seen as creatures who know how to have fun and find happiness in life’s simple and easy things.\n'
'Pigs remind us to take a break, look around, and cherish the moments that bring us joy and relaxation.\n'
'And so, as we wrap up our journey through the Chinese zodiac, let’s embrace the Pig’s spirit, reminding us to take a breather, enjoy the journey, and cherish every moment along the way.\n'
'\nNOTABLE PEOPLE BORN UNDER the Year of the PIG:\n'
          '•Tenzin Gyatso,\n'
          '•Arnold Schwarzeneggar,\n'
          '•Rondal Reagan,\n' 
          '•You!\n'
'\nLUCKY NUMBERS: 2 , 5 , 8'
'\nLUCKY COLORS: YELLOW , GRAY , BROWN , GOLD\n'
'\nUNLUCKY NUMBERS:1 , 7'
'\nUNLUCKY COLORS: RED , BLUE , GREEN'
         ]


CheckCHZodiac()