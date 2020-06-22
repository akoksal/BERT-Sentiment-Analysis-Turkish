# BERT Sentiment Analysis Turkish

Sentiment Analysis in Turkish tweets is implemented with 3 different feature extraction techniques and simple multilayer perceptron(MLP). These feature extraction techniques are:
 - Handcrafted Feature Extraction with [SentiTurkNet](http://myweb.sabanciuniv.edu/rdehkharghani/sentiturknet-3/)
 - [Turkish Word2Vec](https://github.com/akoksal/Turkish-Word2Vec)
 - [BERTurk](https://github.com/stefan-it/turkish-bert)
 
 For more NLP content like this, please subscribe to my blog: https://akoksal.com/
 
 And check out this post for detailed explanation and better models with Keras: https://akoksal.com/articles/understand-tweets-better-with-BERT-sentiment-analysis
  
 ## Dataset
 **Due to license problems in Twitter datasets, I had to remove BOUN Twitter Data and collected tweets with TweetScraper. Maybe, I can share the tweets with their corresponding IDs in the future.**
 
 ## Notebooks
 Notebooks are self-explanatory. You can check out PyIstanbul Notebooks folder for 3 different feature extraction techniques.
 
 BERT Features with Keras notebook has custom loss, Dropout, and more controllable features with Keras which result better scores with 68% macro accuracy.
 
 ## Results
 Models  | Positive Accuracy | Neutral Accuracy | Negative Accuracy | Average Accuracy(Macro)
------------- | ------------- | ------------- | ------------- | -------------
SentiTurkNet  | 0.04 | 0.94 | 0.09 | 0.36
Word2Vec  |  0.37 | 0.69 | 0.47 | 0.51 
**BERT**  | 0.53 | 0.76 | 0.67 | **0.65**

## Analysis
Also, 3 different topics with big incidents are analyzed and the correlation between incidents and Twitter sentiments is seen by BERT model.
### 1. Netflix

Protests in Twitter after new Turkish series in Netflix with LGBT content.

![](https://live.staticflickr.com/65535/49770815696_93f5fdd09a_n.jpg)

> Tweet


![](https://live.staticflickr.com/65535/49770815741_01cebfba13_z.jpg)

> Scores


### 2. Cappy

Two different incidents in Twitter about Cappy for unidentified objects in juice.

![](https://live.staticflickr.com/65535/49770817666_a79d38c4bd_n.jpg)

> Tweet 1

![](https://live.staticflickr.com/65535/49770285753_1c848b4d33_n.jpg)

> Tweet 2

![](https://live.staticflickr.com/65535/49770286768_504f0dbbd8_z.jpg)
> Scores

### 3. Berkcan Guven

Some major critics about Berkcan Guven in Twitter after he released a video with underage celebrity. He removed the video after 7 hours which already had more than 700k views.

![](https://live.staticflickr.com/65535/49770287643_e18a1426e8_n.jpg)

> Video

![](https://live.staticflickr.com/65535/49771145192_346f0a916f_z.jpg)

> Scores
