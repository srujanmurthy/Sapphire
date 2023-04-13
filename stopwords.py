import spacy
from nltk.corpus import stopwords

#Custom stopwords
custom_stopwords = [
"this","makes","talk","actually","eventually","i've","[music data]","musicdata","dont","-","--","laughter","laugh","maybe","like","just"
"know",
"equal",
"look",
"pause",
"we've",'so',
"_",
"+","-","^","%","$","*",
"by",
"use",
"using",
"=",
"gonna",
"he",
"hi",
"going",
"like",
"hello",
"we're",
"that's",
"there's",
"i'm",
"she",
"it",
"they",
"them",
"his",
"her",
"its",
"their",
"theirs",
"him",
"hers",
"themself",
"right",
"left",
"right?",
"left?",
"themselves",
"want",
"okay",
"need",
"wait",
"waiting",
"sitting","","let's",'question',"questions","are","kind","now","probably","outside","inside","here","face","wanna","thing"]
#Generate pronouns
pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves", "mine", "yours", "his", "hers", "its", "ours", "theirs"]
#Generate nouns(common)
nouns = ["dog", "cat", "house", "car", "book", "pen", "tree", "flower", "river", "mountain", "ocean", "sun", "moon", "star", "computer", "phone", "chair", "table", "door", "window", "shirt", "shoe", "hat", "food", "water", "air", "money", "love", "friend", "family", "teacher", "student", "doctor", "nurse", "engineer", "scientist", "writer", "artist", "musician", "actor", "athlete", "city", "country", "planet", "universe", "idea", "emotion", "memory", "dream", "thought", "experience", "feeling", "color", "sound", "taste", "smell", "texture", "temperature", "shape", "size", "weight", "speed", "distance", "time", "moment", "hour", "day", "week", "month", "year", "decade", "century", "history", "culture", "language", "art", "science", "technology", "nature", "environment"]
#Generate numbers in string format
numbers_str = []
for char in range(0,10000,1):
  numbers_str.append(str(char))
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
sw_spacy = list(en.Defaults.stop_words)
stop_words = set(stopwords.words('english'))

sw = []