# Trending Twitter Tunes

The soundtrack to your social media life.

http://twitter-tunes.herokuapp.com/

https://twitter.com/trending__tunes

### About
A Python application that takes a US Twitter trending topic and finds a YouTube music video related to that topic name.
For example, the trending topic #USMNT will be returned with this music-related clip: https://www.youtube.com/watch?v=u0kn_t7hwC4

The Trending Twitter Tunes website displays the top 10 Twitter topics and their associated music video.
Additionally we have a Twitterbot that tweets the top Twitter trend and it's associated video once per hour:

![Image of USMNT TWEET]
(twitter_tunes/static/trending_tunes_soccer.png)
https://twitter.com/trending__tunes/status/714966217606303744


Technologies Used:

* AJAX
* apscheduler
* Heroku
* Pyramid
* pytest & tox
* Python
* Redis
* Regex
* tweepy
* Twitter API
* YouTube API


Technical Overview:

So, how does all of this actually work!?  The tweepy python module is used to make Twitter API calls and return the current top trends.  Redis is used in Heroku to store these trends as to avoid unnecessary Twitter API calls.  Regex is utilized to parse the returned trends into searchable terms, i.e. '#ThenItAllWentHorriblyWrong' becomes 'Then it all went horribly wrong'. This enables us to make YouTube API calls with a string YouTube will more easily understand.  The word 'music' is added to the end of the search term, the query is sent to youtube, and the analysis of our YouTube results begins.  The returned results are then checked for any videos that contain specific key words in the channel name/title i.e. 'VEVO' in the channel or 'remix' in the title.  Video URLs that have these words are considered 'validated' and we pass that information along to whatever is utilizing it, i.e. the bot or the website.  Our bot only tweets terms that have been flagged as validated after the YouTube query, as we don't want our bot to tweet non-music related material at any point in time.  On the other hand, our site allows these results to be shown on the page however, we mark the 'validated' results once the AJAX call to our server has been made.
Our scheduler updates the redis every few minutes and our bot attempts to tweet once an hour.  When the bot attempts to tweet it looks for the top trends validated YouTube video, verifies it has not been tweeted recently, and lets the world know what it should be listening to!  The best part about this application is that it has been built in a modular fashion and could be easily modified to target other specific YouTube videos!

### Authors:
Iris Carrera https://github.com/icarrera/

Kyle Richardson https://github.com/kylerichva

A.J. Wolhfert https://github.com/wohlfea

Joe McClenahan https://github.com/jmcclena94

Ben Garnaat https://github.com/bgarnaat




### How To Contribute
See CONTRIBUTING.md
