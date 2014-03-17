# User Interest Classification (Twitter)

User interest classification based on their social media content (Twitter)



## Edit values in `gettweets.py`

    access_token_key = ""
    access_token_secret = ""
    consumer_key = ""
    consumer_secret = ""


## Directories

* All the training data you download using below command is saved in `data/`
      
    ```python gettweets.py pinchofyum food```
    
* All the user interest classification using below command is saved in `test/`
      
    ```python classify.py wsj```

* Stored Models `model/`


## Download training data using below commands

    python gettweets.py pinchofyum food
    python gettweets.py FoodNetwork food
    python gettweets.py nytimesfood food
    python gettweets.py seriouseats food
    python gettweets.py latimesfood food
    python gettweets.py FoodNetwork cooking
    python gettweets.py jamieoliver cooking
	python gettweets.py bflay cooking
	python gettweets.py CookingChannel cooking
	python gettweets.py Paula_Deen cooking
	python gettweets.py hetaltrivedibl health
	python gettweets.py MensHealthMag health
	python gettweets.py WomensHealthMag health
	python gettweets.py goodhealth health
	python gettweets.py WSJ news
	python gettweets.py HuffPostPol politics
	python gettweets.py loomnie politics
	python gettweets.py politico politics
	python gettweets.py nprpolitics politics
	python gettweets.py HuffPostPol politics
	python gettweets.py _munter_ webdev
	python gettweets.py mkuehnel webdev
	python gettweets.py smashingmag webdev
	python gettweets.py drublic webdev
	python gettweets.py IMDb movies
	python gettweets.py RottenTomatoes movies
	python gettweets.py wbpictures movies
	python gettweets.py lionsgatemovies movies
	python gettweets.py YahooMovies movies
	python gettweets.py michaelsantoli finance
	python gettweets.py YahooFinance finance
	python gettweets.py howardlindzon finance
	python gettweets.py ftfinancenews finance
	python gettweets.py igrigorik tech
	python gettweets.py BBCClick tech
	python gettweets.py nytimestech tech
	python gettweets.py BBCTech tech
	python gettweets.py mattcutts tech
	python gettweets.py a_greenberg tech
	python gettweets.py bitcoinpoet bitcoin
	python gettweets.py bitcoininfo bitcoin
	python gettweets.py bit8coin bitcoin
	python gettweets.py BTCFoundation bitcoin
	python gettweets.py BitCoinReporter bitcoin
	python gettweets.py AirlineReporter aviation
	python gettweets.py Flightglobal aviation
	python gettweets.py nycaviation aviation
	python gettweets.py aviation_quest aviation
	python gettweets.py aspireaviation aviation 
	python gettweets.py Inc business
	python gettweets.py Forbes business
	python gettweets.py businessinsider business
	python gettweets.py LakshmanaG bigdata
	python gettweets.py BigDataBlogs bigdata
	python gettweets.py IBMbigdata bigdata
	python gettweets.py FaceOfBigData bigdata
	python gettweets.py BigDataDiary bigdata
	python gettweets.py TedOBrien93 datascience
	python gettweets.py ds_ldn datascience
	python gettweets.py hmason datascience
	python gettweets.py BerkeleyData datascience
	python gettweets.py DataScienceCtrl datascience
	python gettweets.py cultofmac mac
	python gettweets.py MacRumors mac
	python gettweets.py macworld mac
	python gettweets.py pcworld PC
	python gettweets.py PCMag PC
	python gettweets.py pcpro PC
	python gettweets.py RockstarGames gaming
	python gettweets.py PC_Gamer gaming
	python gettweets.py gameinformer gaming
	python gettweets.py EA gaming
	python gettweets.py Xbox gaming
	python gettweets.py SEGA gaming
	python gettweets.py Warcraft gaming
	python gettweets.py amazongames gaming
	python gettweets.py sheenalashay blogging
	python gettweets.py Raishimi blogging
	python gettweets.py problogger blogging
	python gettweets.py DayneShuda blogging
	python gettweets.py Yoga_Journal yoga
	python gettweets.py YogaWorks yoga
	python gettweets.py yogadork yoga
	python gettweets.py MyYogaOnline yoga	
    python gettweets.py pitchforkmedia music
    python gettweets.py RollingStone music
    python gettweets.py stereogum music
    python gettweets.py nprmusic music

