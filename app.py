# importing Flask and other modules
from flask import Flask, request, render_template
import praw
import sys
from sentihelper import *
import senticonsts

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST":
		# getting input with name = fname in HTML form
		user = request.form.get("fname")
		# Initialize a Reddit object
		reddit = praw.Reddit(
			user_agent    = senticonsts.RED_USER_AGENT,
			client_id     = senticonsts.RED_CLIENT_ID,
			client_secret = senticonsts.RED_CLIENT_SECRET,
			username      = senticonsts.RED_USERNAME,
			password      = senticonsts.RED_PASSWORD
		)
		l = 500
		# Iterate through users comments.
		# If you want to limit the number of comments returned, specify the number in the limit argument.
		for comment in reddit.redditor(user).comments.new(limit=l):
			# Print the text (body) of each comment
			aggregatesenti(sentiment_pipeline(comment.body)[0]['label'])
			# Print the title of the comment's parent post
			# print(comment.submission.title)

		# Show Results
		sorted_emo = dict(sorted(emotions.items(), key=lambda item: item[1], reverse=True))
		emo, pct = zip(*sorted_emo.items())

		return render_template('sentiments.html', username=user, limit=l,
			 e0=emo[0], p0=pct[0],
			 e1=emo[1], p1=pct[1],
			 e2=emo[2], p2=pct[2],
			 e3=emo[3], p3=pct[3],
			 e4=emo[4], p4=pct[4],
			 e5=emo[5], p5=pct[5])

	return render_template("form.html")

if __name__=='__main__':
	app.run()
