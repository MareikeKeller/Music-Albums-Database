from http import client
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)



albums = {
     "1":{
        "id": "1",

        "album": "What's Going On",

        "artist": "Marvin Gaye",

        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-001-Marvin-Gaye-WHATS-GOING-ON.jpg?w=1000",

        "year": "1971",

        "summary": "Marvin Gaye’s masterpiece began as a reaction to police brutality. In May 1969, Renaldo ‘Obie’ Benson, the Four Tops’ bass singer, watched TV coverage of hundreds of club-wielding cops breaking up the People’s Park, a protest hub in Berkeley. Aghast at the violence, Benson began to write a song with Motown lyricist Al Cleveland, trying to capture the confusion and pain of the times. He knew he had something big in his nascent version of ‘What’s Going On,’ but the rest of the Four Tops weren’t interested, and Benson’s efforts to get Joan Baez to record it didn’t work out, either. But one of Motown’s biggest stars and greatest voices turned out to be more receptive. Gaye was in a dark and contemplative place, wounded by the death of his frequent duet partner Tammi Terrell, yearning to sing subtler and more substantive material, and mulling over his brother Frankie’s horrifying tales of his recent stint fighting in Vietnam. Gaye had been keeping busy writing for and producing a group called the Originals, and trying to figure out what was next. ‘I’d been stumbling around for an idea,’ he told biographer David Ritz. ‘I knew there was more inside me. And that was something no record executive or producer could see. But I saw it. I knew I had to get out there.’ After some hesitation, Gaye embraced ‘What’s Going On,’ and with the help of arranger David Van De Pitte, crafted a version of the song that was jazzier and more sophisticated than any Motown recording to date, layering cinematic strings over James Jamerson’s supernaturally sinuous bass line and a polyrhythmic groove. Gaye unleashed one of his most spectacular vocal performances in a career full of them, scatting and improvising around the main melody. Motown Records founder Berry Gordy initially resisted releasing ‘What’s Going On,’ telling Gaye that he thought scatting was out of date and protest lyrics were too commercially risky. But when the song became an instant hit, Gordy gave Gaye a single month to craft an album to accompany ‘What’s Going On.’ Gaye more than rose to the challenge. ‘I work best under pressure and when I’m depressed,’ he told the Detroit Free Press at the time. ‘The world’s never been as depressing as it is right now. We’re killing the planet, killing our young men in the streets, and going to war around the world. Human rights … that’s the theme.’ What emerged was soul music’s first concept album, and one of the most important and influential LPs ever made. John Legend recently described it as ‘the voice of black America speaking out that we couldn’t always smile on cue for you.’ Building it all around one finished song lent What’s Going On a musical and thematic through line. ‘What’s Happening Brother’ assumes the voice of a Vietnam vet like Gaye’s brother, puzzled by a changing America and looking for work; ‘Mercy Mercy Me (The Ecology)’ is a taut ode to the environment; ‘Flyin’ High (In the Friendly Sky)’ takes on drug addiction. After What’s Going On, black musicians at Motown and elsewhere felt a new freedom to push the musical and political boundaries of their art. ‘When I was struggling for the right of the Motown artist to express himself,’ Gaye said, ‘Stevie [Wonder] knew I was also struggling for him.’ At the end of the final song on What’s Going On, the lament ‘Inner City Blues (Make Me Wanna Holler),’ the music shifts back into a jazzier reprise of the title track. As the album fades out, the groove continues on. Five decades later, it still hasn’t stopped.",

        "records_sold": "30M",

        "streams": "22.2M",
        
        "awards_won": ["NAACP Image Awards", "Grammy Hall of Fame", "Grammy Awards"],

        "genres": ["RnB", "Soul"],
        },
        
    "2": {
        "id": "2",
        
        "album": "Pet Sounds",
        "artist": "The Beach Boys",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-002-Beach-Boys-PET-SOUNDS-update.jpg?w=1000",
        "year": "1966",
        "summary": "‘Who’s gonna hear this shit?’ Beach Boys singer Mike Love asked the band’s resident genius, Brian Wilson, in 1966, as Wilson played him the new songs he was working on. ‘The ears of a dog?’ Confronted with his bandmate’s contempt, Wilson made lemonade of lemons. ‘Ironically,’ he observed, ‘Mike’s barb inspired the album’s title. ‘Barking dogs – Wilson’s dog Banana among them, in fact – are prominent among the found sounds on the album. The Beatles made a point of echoing them on Sgt. Pepper’s Lonely Hearts Club Band – an acknowledgment that Pet Sounds was the inspiration for the Beatles’ masterpiece. That gesture actually completed a circle of inﬂuence: Wilson initially conceived of Pet Sounds as an effort to top the Beatles’ Rubber Soul. With its vivid orchestration, lyrical ambition, elegant pacing, and thematic coherence, Pet Sounds invented — and in several senses, perfected — the notion that an album could be more than the sum of its parts. When Wilson sang, ‘Wouldn’t it be nice if we were older,’ on the album’s magnificent opening song, he wasn’t just imagining a love that could evolve past high school, he was suggesting a new grown-up identity for rock & roll music itself. Wilson made Pet Sounds without the rest of the band, using them only to ﬂesh out the vocal arrangements. He even considered putting the album out as a solo project, and the ﬁrst single, ‘Caroline, No,’ was released under his own name. The personal nature of the songs, which Wilson co-wrote primarily with lyricist Tony Asher, further distinguished the album from the Beach Boys’ previous hits. Its luxurious sound conveys a heartbreaking wistfulness, as songs such as ‘I Just Wasn’t Made for These Times’ and ‘I’m Waiting for the Day’ bid farewell to the innocent world of the early Sixties. The album’s centerpiece is ‘God Only Knows,’ arranged with harpsichord, horns, sleigh bells, and strings to create a spiritual feeling Wilson later compared to ‘being blind, but in being blind, you can see more. You close your eyes; you’re able to see a place or something that’s happening.’ In the years to come, countless artists would live in his vision.",
        "records_sold": "100M",
        "streams": "10M",
        "awards_won": ["Grammy Awards", "American Music Awards", "Kid's Choice Awards"],
        "genres": ["RnB", "Rock", "Pop"],
        }, 
     "3": {
        "id": "3",
        "album": "Blue",
        "artist": "Joni Mitchell",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-003-JoniMitchell-BLUE-HR.jpg?w=1000",
        "year": "1971",
        "summary": "In 1971, Joni Mitchell represented the West Coast feminine ideal — celebrated by Robert Plant as ‘a girl out there with love in her eyes and flowers in her hair’ on Led Zeppelin’s ‘Goin’ to California.’ It was a status that Mitchell hadn’t asked for and did not want: ‘I went, ‘Oh, my God, a lot of people are listening to me,’’ she recalled in 2013. ‘’They better find out who they’re worshiping. Let’s see if they can take it. Let’s get real.’ So I wrote Blue.’From its smoky, introspective cover to its wholly unguarded approach to songwriting, Blue is the first time any major rock or pop artist had opened up so fully, producing what might be the ultimate breakup album and setting a still-unmatched standard for confessional poetry in pop music. Using acoustic instruments and her octave-leaping voice, Mitchell portrayed herself as a lonely painter, aching to make sense of all her heartbreak. She reflects on past relationships and encounters, including a chef from Crete (‘Carey’) and rock luminaries like Graham Nash (‘My Old Man’), Leonard Cohen (‘A Case of You’), and James Taylor (‘This Flight Tonight’), who lent a hand on a few tracks. Along with its romantic melancholy, Blue was the sound of a woman availing herself of the romantic and sexual freedom that was, until then, an exclusively male province in rock.The songs had such stark, emotional intensity that it shocked the men around her: ‘Kris Kristofferson said to me, ‘Oh, Joni. Save something for yourself.’ The vulnerability freaked them out.’ On ‘Little Green,’ she opens up about a baby she had given up for adoption, and on the staggering piano dirge ‘River,’ she takes responsibility for a romance gone wrong, changing the scope of love songs forever: ‘I’m so hard to handle/I’m selfish, and I’m sad,’ she laments. ‘Now I’ve gone and lost the best baby/That I ever had.’Mitchell continued to release excellent records throughout the Seventies, but Blue remains her masterpiece. ‘The Blue album, there’s hardly a dishonest note in the vocals,’ she told Rolling Stone in 1979. ‘At that period of my life, I had no personal defenses. I felt like a cellophane wrapper on a pack of cigarettes. I felt like I had absolutely no secrets from the world, and I couldn’t pretend in my life to be strong. Or to be happy. But the advantage of it in the music was that there were no defenses there either.’",
        "records_sold": "7M",
        "streams": "1M",
        "awards_won": ["Grammy Hall of Fame", "Grammy Awards", "Billboard Music Awards"],
        "genres": ["Folk", "Rock"],
        }, 

    "4": {
        "id": "4",
        "album": "Songs in the Key of Life",
        "artist": "Stevie Wonder",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-004-Stevie-Wonder-SONGS-IN-THE-KEY-OF-LIFE.jpg?w=1000",
        "year": "1976",
        "summary": "Months before the recording sessions for Songs in the Key of Life ended, the musicians in Stevie Wonder’s band had T-shirts made up that proclaimed, ‘We’re almost finished.’ It was the stock answer to casual fans and Motown executives and everybody who’d fallen in love with Wonder’s early-Seventies gems – 1972’s Talking Book, 1973’s Innervisions, and 1974’s Fulfillingness’ First Finale – and who had been waiting two years for the next chapter. ‘I believed there was a lot that needed to be said,’ Wonder said. More, in fact, than he could fit onto a double album – also included was a bonus EP, a seven-inch single with four more songs from the sessions. Songs, released in 1976, encompasses an incredible range of life experiences – from the giddy joy of a baby in the bathtub (‘Isn’t She Lovely,’ featuring the cries and giggles of Wonder’s infant daughter Aisha Morris) through tributes to his musical heroes (‘Sir Duke’) to dismay about the indifference of the wealthy (‘Village Ghetto Land’). Wonder pulled from every imaginable musical source — the ecstatic ‘Sir Duke’ references Duke Elington and Ella Fitzgerald, while ‘As’ featured Herbie Hancock on Fender Rhodes. Though Wonder’s blindness meant he could record faster by memorizing lyrics, some songs had four or five intricate verses, so somebody had to prompt him. Often it was engineer John Fischbach, reading lines into the headphone mix just seconds before Wonder sang them. ‘He never got thrown off,’ engineer John Fischbach told Rolling Stone years later. ‘His vocals had so much power.’ The album’s mastery of many styles remains astonishing, but the feat might not have meant so much had Wonder not delivered some of his most impassioned political art as well, like the autobiographical ‘I Wish,’ the takedown of wealthy complacency ‘Village Ghetto Land,’ and, perhaps most movingly, ‘Black Man,’ in which he runs down a funky list of global Afro-diasporic aspirations and heroes. Songs in the Key of Life linked all this together, in Wonder’s all-encompassing innervision.",
        "records_sold": "20M",
        "streams": "15.6M",
        "awards_won": ["Grammy Awards", "American Music Awards", "Grammy Hall of Fame"],
        "genres": ["RnB", "Pop", "Soul", "Jazz", "Funk"],
        }, 

    "5": {
        "id": "5",
        "album": "Abbey Road",
        "artist": "The Beatles",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-005-Beatles-ABBEY-ROAD.jpg?w=1000",
        "year": "1969",
        "summary": "‘It was a very happy record,’ said producer George Martin, describing this album in The Beatles Anthology. ‘I guess it was happy because everybody thought it was going to be the last.’ Indeed, Abbey Road — recorded in two months during the summer of 1969 — almost never got made at all. That January, the Beatles were on the verge of a breakup, exhausted and angry with one another after the disastrous sessions for the aborted Get Back LP, later salvaged as Let It Be [see No. 342]. Yet determined to go out with the same glory with which they had ﬁrst entranced the world at the start of the decade, the group reconvened at EMI’s Abbey Road Studios to make their most polished album: a collection of superb songs cut with an attention to reﬁned detail, then segued together (especially on Side Two) with conceptual force. There was no thematic link, other than the Beatles’ unique genius. John Lennon veered from the stormy metal of ‘I Want You (She’s So Heavy)’ to the exquisite vocal sunrise of ‘Because.’ Paul McCartney was saucy (‘Oh! Darling’), silly (‘Maxwell’s Silver Hammer’), and deliciously bitter (‘You Never Give Me Your Money’). George Harrison proved his long-secret worth as a composer with ‘Something’ (later covered by Frank Sinatra) and the folk-pop diamond ‘Here Comes the Sun,’ written in his friend Eric Clapton’s garden after a grim round of business meetings. Lennon, McCartney, and Harrison reputedly sang more three-part harmonies here than on any other Beatles album. That warm feeling — a sense of an increasingly divided band warmly coming together as friends — may be one reason Abbey Road has become the most beloved Beatles album of all time.",
        "records_sold": "30M",
        "streams": "25M",
        "awards_won": ["Grammy Awards", "Billboard Music Awards", "Brit Awards"],
        "genres": ["Skiffle", "Rock", "Blues"],
        }, 

    "6": {
        "id": "6",
        "album": "Nevermind",
        "artist": "Nirvana",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-006-Nirvana-NEVERMIND-HR.jpg?w=1000",
        "year": "1991",
        "summary": "An overnight-success story of the 1990s, Nirvana’s second album and its totemic ﬁrst single, ‘Smells Like Teen Spirit,’ shot up from the Northwest underground — the nascent grunge scene in Seattle — to kick Michael Jackson’s Dangerous off the top of the Billboard charts and blow hair metal off the map. Few albums have had such an overpowering impact on a generation — a nation of teens suddenly turned punk — and such a catastrophic effect on its main creator. The weight of success led already-troubled singer-guitarist Kurt Cobain to take his own life in 1994. But his slashing riffs, corrosive singing, and deviously oblique writing — rammed home by the Zeppelin-via-Pixies might of bassist Krist Novoselic and drummer Dave Grohl — put warrior purity back in rock & roll. Lyrically, Cobain raged in code — shorthand grenades of inner tumult and self-loathing. His genius, though, in songs like ‘Lithium,’ ’Breed,’ and ‘Teen Spirit’ was the soft-loud tension he created between verse and chorus, restraint and assault. Cobain was a pop lover at heart — and a Beatlemaniac: Nevermind co-producer Butch Vig remembered hearing Cobain play John Lennon’s ‘Julia’ at sessions. Cobain also fought to maintain his underground honor with songs like the scabrous punk purge ‘Territorial Pissings.’ Ultimately, it was a losing battle, but it is part of this album’s enduring power. Vig recalled when Cobain was forced to overdub the guitar intro to ‘Teen Spirit’ because he couldn’t nail it live with the band: ’That pissed him off. He wanted to play [the song] live all the way through.’",
        "records_sold": "30M",
        "streams": "22.2M",
        "awards_won": ["MVA Awards", "Grammy Awards", "American Music Awards"],
        "genres": ["Grunge", "Folk", "Rock"],
        }, 

    "7": {
        "id": "7",
        "album": "Rumours",
        "artist": "Fleetwood Mac",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-007-Fleetwood-Mac-RUMOURS.jpg?w=1000",
        "year": "1977",
        "summary": "With Rumours, Fleetwood Mac turned private turmoil into gleaming, melodic public art. The band’s two couples — bassist John McVie and singer-keyboard player Christine McVie, who were married; guitarist Lindsey Buckingham and vocalist Stevie Nicks, who were not — broke up during the protracted sessions for the album. As John later told Rolling Stone of the atmosphere during the making of Rumours, ‘Parties going on all over the house. Amazing. Terrifying. Huge amounts of illicit materials, yards and yards of this wretched stuff. Days and nights would just go on and on.’This frenzied, decadent vibe lent a highly charged, confessional aura to such songs as Buckingham’s ‘Go Your Own Way,’ Nicks’ ‘Dreams,’ Christine’s ‘Don’t Stop,’ and the group-composed anthem to betrayal, ‘The Chain.’ The band’s soap opera fueled its own intricate creative conversation; on ‘You Make Loving Fun,’ Christine sang about her new boyfriend, the band’s lighting designer, as her ex John dutifully drives home the song with a sunny, funky bass line. To write ‘Dreams,’ Nicks sat on a black velvet bed in a tiny room hidden deep in the Record Plant, where the band was recording, creating one of her most haunting songs in 10 minutes. ‘[In ‘Go Your Own Way’] Lindsey is saying go ahead and date other men and go live your crappy life, and [I’m] singing about the rain washing you clean,’ Nicks said. ‘We were coming at it from opposite angles, but we were really saying the same exact thing.’ The Mac’s catchy exposés, produced with California-sunshine polish, touched a nerve: Rumours became the sixth-best-selling album of all time.",
        "records_sold": "40M",
        "streams": "21.9M",
        "awards_won": ["Grammy Awards", "American Music Awards", "Brit Awards"], 
        "genres": ["Folk", "Metal", "Rock"],
        }, 

    "8": {
        "id": "8",
        "album": "Purple Rain",
        "artist": "Prince",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-008-Prince-PURPLE-RAIN.jpg?w=1000",
        "year": "1984",
        "summary": "‘I think Purple Rain is the most avant-garde, ‘purple’ thing I’ve ever done,’ Prince told Ebony in 1986. He was still a rising star with only a couple of hits when he got the audacious idea to make a movie based on his life, and make his next LP the movie’s soundtrack. When it was released in 1984, he became the first artist to have the Number One song, album, and movie in North America. But Purple Rain was so much more than a huge movie soundtrack: It was a testament to Prince’s dream of creating a utopian Top 40, a place where funk, psychedelia, heavy-metal shredding, huge ballads, and daring experimentalism could coexist. ‘Listening to Purple Rain now, it’s kind of like a Beatles album,’ keyboardist Matt Fink of the Revolution told Rolling Stone shortly after Prince’s death in 2016. ‘Every song is just so brilliant in its own way — all so unique and different.’It’s an incredible balance of contradicting impulses — from the pornographic ‘Darling Nikki’ to the sparkling innocence of ‘Take Me With You.’ When Purple Rain director Albert Magnoli asked for a good song to back a montage sequence, Prince came in the next day with ‘When Doves Cry,’ a stark, eccentric-sounding brokenhearted song that became his first Number One single.The title track was one of several songs recorded live at his hometown club, First Avenue, in Minneapolis (strings and overdubs were added later in the studio). It was inspired by Bob Seger, of all people — when Prince was touring behind 1999 [see No. 130] in 1983, Seger was playing many of the same markets. Prince didn’t understand the Midwestern rocker’s appeal, but decided to try a ballad in the Seger mode — the result may be the greatest rock ballad of all time.",
        "records_sold": "25M",
        "streams": "9.5M",
        "awards_won": ["Academy Awards", "Brit Awards", "Golden Globes"],
        "genres": ["rnb", "Soul", "Afrobeats"],
        }, 

    "9": {
        "id": "9",
        "album": "Blood on the Tracks",
        "artist": "Bob Dylan",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-009-Bob-Dylan-BLOOD-ON-THE-TRACKS.jpg?w=1000",
        "year": "1975",
        "summary": "Bob Dylan once introduced this album’s opening song, ‘Tangled Up in Blue,’ onstage as taking him 10 years to live and two years to write. It was, for him, a pointed reference to the personal crisis — the collapse of his marriage to Sara Lowndes — that at least partly inspired this album, Dylan’s best of the 1970s.In fact, he wrote all of these lyrically piercing, gingerly majestic folk-pop songs in two months, in mid-1974. He was so proud of them that he privately auditioned almost all of the album, from start to ﬁnish, for pals and peers, including Mike Bloomﬁeld, David Crosby, and Graham Nash, before cutting them in September — in just a week, with members of the bluegrass band Deliverance.But in December, Dylan played the record for his brother, David, in Minneapolis, who suggested recutting some songs with local musicians. The ﬁnal Blood was a mix of New York and Minneapolis tapes; the New York versions are slower, more pensive, while the Minneapolis versions are faster and wilder. Together, they frame the gritty anguish in Dylan’s vocals, as he rages through some of his most passionate, confessional songs — from adult breakup ballads like ‘You’re a Big Girl Now’ and ‘If You See Her, Say Hello’ to the sharp-tongued opprobrium of ‘Idiot Wind,’ his greatest put-down song since ‘Like a Rolling Stone.’‘A lot of people tell me they enjoyed that album,’ Dylan said soon after it became an instant commercial and critical success. ‘It’s hard for me to relate to that — I mean, people enjoying that type of pain.’ Yet Dylan had never turned so much pain into so much musical splendor.",
        "records_sold": "2.5M",
        "streams": "8.9M",
        "awards_won": ["Grammy Awards", "Golden Globe Awards", "Academy Awards"],
        "genres": ["Country", "Blues", "Folk"],
        }, 

    "10": {
        "id": "10",
        "album": "The Miseducation of Lauryn Hill",
        "artist": "Lauryn Hill",
        "cover": "https://www.rollingstone.com/wp-content/uploads/2020/09/R1344-010-Lauryn-Hill-MISEDUCATION.jpg?w=1000",
        "year": "1998",
        "summary": "‘This is a very sexist industry,’ Lauryn Hill told Essence magazine in 1998. ‘They’ll never throw the ‘genius’ title to a sister.’ Though already a star as co-leader of the Fugees, with Wyclef Jean, she was hungry to express her own vision. ‘[I wanted to] write songs that lyrically move me and have the integrity of reggae and the knock of hip-hop and the instrumentation of classic soul,’ the singer said of her debut album.She took control of the recording process, writing, producing, arranging, and helming sessions that included collaborators like pianist John Legend, still in college when he got the call to go out to New Jersey, where Hill was recording, and the pathfinding R&B artist D’Angelo. They shaped a sound that went from the money-hating banger ‘Lost Ones’ to subtle, glorious, heartbreaking monuments such as ‘Ex-Factor’ (reportedly about Wyclef Jean) and the swinging sermon ‘Doo Wop (That Thing).’ For ‘I Used to Love Him,’ Hill duetted with her hip-hop-soul forebear Mary J. Blige. Each song was driven by a clarity of vision and personal honesty that felt revelatory; in ‘To Zion,’ she detailed her struggles as an ambitious professional and a new mom. Miseducation’s musical legacy is just as deep; at a time when pop was becoming increasingly slick and digitized in the go-go Nineties, here was an album that showed the commercial appeal of a rawer sound; ‘I wanna hear that thickness of sound,’ Hill said. ‘You can’t get that from a computer, because a computer’s too perfect. But that human element, that’s what makes the hair on the back of my neck stand up. I love that.’",
        "records_sold": "20M",
        "streams": "9.3M",
        "awards_won": ["Soul Train Awards", "VMA", "Image Awards", "Grammy Awards"],
        "genres": ["rnb", "Soul", "Rap"],
        }, 

     }


# ROUTES


@app.route('/')
def welcome():
    return render_template('welcome.html', albums=albums)   

@app.route('/search/')
def search():
    return render_template('welcome.html', albums=albums)   

#get specific info according to id
@app.route('/results/<id>')
def show_results(id=None):

    data_id = albums[id]

    return render_template('results.html', data_id=data_id, albums=albums) 



@app.route('/edit/<id>')
def edit(id=None):

    global data_id
    data_id = albums[id]

    return render_template('edit.html', data_id=data_id, albums=albums) 


@app.route('/edit_route', methods=['GET', 'POST'])
def edit_route():
    global albums 

    album_json_data = request.get_json(force=True)
    data_id = album_json_data["id"]
    

    id_to_edit = data_id


    albums[id_to_edit]['album'] = album_json_data["album"]
    albums[id_to_edit]['artist'] = album_json_data["artist"]
    albums[id_to_edit]['cover'] = album_json_data["cover"]
    albums[id_to_edit]['year'] = album_json_data["year"]
    albums[id_to_edit]['summary'] = album_json_data["summary"]
    albums[id_to_edit]['records_sold'] = album_json_data["records_sold"]
    albums[id_to_edit]['streams'] = album_json_data["streams"]
    albums[id_to_edit]['awards_won'] = album_json_data["awards_won"]
    albums[id_to_edit]['genres'] = album_json_data["genres"]


    return jsonify(albums=albums) 


@app.route('/results')
def results():
    return render_template('results.html')  


@app.route('/add_route', methods=['GET', 'POST'])
def add_route():
    global albums 

    album_json_data = request.get_json()  




    album_length = len(albums)

    #updating album length to use as ID for new entries
    album_length = album_length + 1
    album_length = "" + str(album_length) + ""


    #create new dictionary enrty
    albums[album_length] = {}

    albums[album_length]['id'] = album_length
    albums[album_length]['album'] = album_json_data["album"]
    albums[album_length]['artist'] = album_json_data["artist"]
    albums[album_length]['cover'] = album_json_data["cover"]
    albums[album_length]['year'] = album_json_data["year"]
    albums[album_length]['summary'] = album_json_data["summary"]
    albums[album_length]['records_sold'] = album_json_data["records_sold"]
    albums[album_length]['streams'] = album_json_data["streams"]
    albums[album_length]['awards_won'] = album_json_data["awards_won"]
    albums[album_length]['genres'] = album_json_data["genres"]

    return jsonify(albums=albums) 


@app.route('/add')
def add():
    return render_template('add.html', albums=albums) 


#search route returning an array of matching search results
@app.route('/search/<search_term>', methods=['GET', 'POST'])
def search_term(search_term):
    global albums
    print(search_term)
    save_search_term = search_term #what is in /<search_term>
    
    found_matches = []
   #for loop to create route that inputs search term into url
    for album_id in albums:
        album = albums[album_id]

        substring = search_term.lower()

        if substring in album["artist"].lower():
                found_matches.append(album)


    #search for genres

        for values in album["genres"]:

            lower_value = values.lower()

            print(substring)

            #making sure album is not already found based on artist
            if album not in found_matches:
                if substring in lower_value:
                    found_matches.append(album)

        for values in album["awards_won"]:

            lower_value = values.lower()

            print(substring)

            #making sure album is not already found based on artist
            if album not in found_matches:
                if substring in lower_value:
                    found_matches.append(album)
                    
  
    print(found_matches)

    return render_template('search_results.html', search_term=substring, found_matches=found_matches)







if __name__ == '__main__':
   app.run(debug = True)




