from transformers import pipeline
import matplotlib.pyplot as plt

# Counter Setup
# https://huggingface.co/blog/sentiment-analysis-python
sentiment_pipeline = pipeline(model="bhadresh-savani/distilbert-base-uncased-emotion")
emotions = {'Sadness':0, 'Anger':0, 'Fear':0, 'Joy':0, 'Love':0, 'Surprise':0}

def aggregatesenti(senti):
    try:
        emotions[senti.title()] += 1
    except:
        return


def showpie(sorted_emo):
    expl = [0.1,0,0,0,0,0]
    plt.pie(list(sorted_emo.values()),
            labels = list(sorted_emo.keys()),
            autopct='%1.1f%%',
            explode=expl)
    plt.show()
    


