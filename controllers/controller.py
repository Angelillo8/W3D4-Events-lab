from flask import render_template, request, redirect
from app import app
from models.events import events, add_new_event, delete_event
from models.event import *
import datetime

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods = ['POST'])
def add_task():
    event_date = request.form['date']
    split_date = event_date.split('-')
    event_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form['name']
    event_guests = request.form['guests']
    event_recurring = True if 'recurring' in request.form else False
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_recurring, event_room_location, event_description)
    add_new_event(new_event)
    return index()

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
  delete_event(name)
  return redirect('/events')