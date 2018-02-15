from flask import Flask, request, jsonify
import argparse
import sys

#Web app
app = Flask(__name__)

@app.route('/ping',methods=['GET'])
def pingServer():
    '''
    Ping request to make sure server is alive, return 'pong'
    '''
    # TODO
    pass

@app.route('/people',methods=['GET'])
def getPeople():
    '''
    Return a standard JSON block of people in any order of format. Must be valid JSON
    '''
    # TODO
    pass

@app.route('/people/age',methods=['GET'])
def sortPeopleByAge():
    '''
    Returns Json block containing a list of people sorted by age youngest to oldest
    '''
    # TODO
    pass

@app.route('/ids/lastname/<lastname>',methods=['GET'])
def getIdsByLastName(lastname):
    '''
    Returns Json block of ids found for the given last name
    Using path params
    '''
    # TODO
    pass


# TODO Create an endpoint POST that accepts a 'person' and appends it to our people. Returns the newley update JSON block of all people.
# New endpoint goes here.


# Optional Challenge: Persist the data somehow


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--debug", help="Optional Debug Mode for stack traces", action="store_true")

    # TODO: pass in a port from the command line and run on that port i.e. 'python3 server.py 9000 test.csv'

    parser.add_argument("file", help="File to import data from")
    args = parser.parse_args()

    # TODO: Initialize any pre-application start code here if needed
    # TODO: Read in people from people.csv into an appropraite data structure so that the endpoints can return data based
    #       on the data in the csv.

    app.debug=args.debug
    app.run(host='0.0.0.0')

