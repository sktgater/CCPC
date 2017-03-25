import os, datetime
import re
import json
from flask import Flask, request, render_template, redirect, abort
from flask import jsonify
from unidecode import unidecode


# mongoengine database module
from flask.ext.mongoengine import MongoEngine
# connect('models')

app = Flask(__name__)   # create our flask app
app.config['CSRF_ENABLED'] = False

# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
#app.config['MONGODB_SETTINGS'] = {'HOST':os.environ.get('MONGOLAB_URI'),'DB': 'CCPC2014'}
#app.logger.debug("Connecting to MongoLabs")
#db = MongoEngine(app) # connect MongoEngine with Flask App







# import data models
#import models

#all_members ={}
##try to import data base into a dictionary
#for x in models.TeamMember.objects:
#	all_members['%s' % x.name] = {
#	'photo':'%s' % x.photo,
#	'bio':'%s' % x.bio,
#	'department':'%s' % x.department
#	}
#
#all_speakers ={}
#
#for x in models.Speaker.objects:
#	all_speakers



# home page
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
#	return render_template('about.html',all_members = all_members)
	return render_template('about.html')

@app.route("/directions")
def direction():
	return render_template('direction.html')

# add speakers or team membaers
#@app.route("/add", methods=['GET'])
#def add():
#	return render_template("add.html")

#@app.route("/addSpeaker", methods=['POST'])
#def addSpeaker():
#	# get form data - create new idea
#	speaker = models.Speaker()
#	speaker.name = request.form.get('name')
#	speaker.photo = request.form.get('photo')
#	speaker.bio = request.form.get('bio')
#	speaker.panel = request.form.get('panel')
#	speaker.save() # save it
#
#	return redirect('/add')
#
#
#@app.route("/addMember", methods=['POST'])
#def addMember():
#	# get form data - create new idea
#	member = models.TeamMember()
#	member.name = request.form.get('name')
#	member.department = request.form.get('department')
#	member.photo = request.form.get('photo')
#	member.bio = request.form.get('bio')
#	member.save() # save it
#
#	return redirect('/add')
#

# query the speaker and return the object
#@app.route('/speakers/<name>')
#def getSpeakerAtr(name):
#    theSpeaker = models.Speaker.objects.get(name=name)
#    return '''%s''' % theSpeaker.panel
#
#
## query the speaker and return the object
#@app.route('/teammember/<name>')
#def getTeamMemberAtr(name):
#    theMember = models.TeamMember.objects.get(name=name)
#    return '''%s''' % theMember.department
#
#@app.route('/panels/<name>')
#def getPanelDes(name):
#	thePanel = models.Panel.objects.get(name=name)
#	return ''''''

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)