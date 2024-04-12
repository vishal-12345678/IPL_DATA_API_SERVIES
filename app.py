#pipe line which connect two softwares is called API,s .
# api and uri both are url but when you hit url it will return web page but api will return jason
# get method is passing arguments through url . post method only work in forms to transfer data . so get is more useful command


from flask import Flask , jsonify,request
import ipl     # importing the python file we have created separately for data aANALYSIS
import JUGAAD
app=Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/api/teams')   # we will create a function in ipl file and access it with this url on web page teamsAPI() will be the function name but this url is nt online yet everyone cant acees it.
def teams():
    teams = ipl.teamsAPI()  #we will call functions from ipl file and unction will be teamsAPI . API,s are nothing but function
    return jsonify(teams)   # apis always fetch data or return data in jason so list->dictionary->jason for dit to jason use jsonify


@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1,team2)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')  # THIS TEAM ARGUMENT WILL BE PASSED THROUGH API
    response = JUGAAD.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = JUGAAD.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = JUGAAD.bowlerAPI(bowler_name)
    return response


app.run(debug=True,port=5001)
