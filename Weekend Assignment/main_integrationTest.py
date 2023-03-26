# Requirement 1: Online Ticket Booking System
# To make it easier for audiences to book tickets for events, we need an online ticket booking system.


class Event:
    def __init__(self, name, date, time, price):
      self.name = name
      self.date = date
      self.time = time
      self.price = price

class TicketBooking:
  def __init__(self):
    self.events = []
    self.booked_events = []

  def add_event(self, event):
    self.events.append(event)

  def book_ticket(self, event_index):
    event = self.events[event_index]
    self.booked_events.append(event)
    self.events.pop(event_index)
    print(f"Ticket booked for {event.name} on {event.date} at {event.time}. Price: {event.price}")

booking = TicketBooking()

# Adding events
event1 = Event("Theatre Play", "2023-04-15", "19:00", 500)
booking.add_event(event1)

event2 = Event("Music Concert", "2023-05-10", "18:30", 1000)
booking.add_event(event2)

# Booking a ticket
booking.book_ticket(0)

# Integration Testing:

def test_ticket_booking():
  booking = TicketBooking()

  event1 = Event("Theatre Play", "2023-04-15", "19:00", 500)
  booking.add_event(event1)

  event2 = Event("Music Concert", "2023-05-10", "18:30", 1000)
  booking.add_event(event2)

  booking.book_ticket(0)

  assert len(booking.events) == 1
  assert len(booking.booked_events) == 1

test_ticket_booking()


# Requirement 2: Artist Registration System
# To provide a platform for emerging talent, we need an artist registration system.

class Artist:
  def __init__(self, name, category):
    self.name = name
    self.category = category

class ArtistRegistration:
  def __init__(self):
    self.artists = []

  def register_artist(self, artist):
    self.artists.append(artist)
    print(f"{artist.name} registered as an artist in the {artist.category} category.")

registration = ArtistRegistration()

# Registering an artist
artist1 = Artist("Sudha Raghunathan", "Music")
registration.register_artist(artist1)


# Integration Testing:
def test_artist_registration():
  registration = ArtistRegistration()

  artist1 = Artist("Sudha Raghunathan", "Music")
  registration.register_artist(artist1)

  assert len(registration.artists) == 1

test_artist_registration()


# Write APIs to access the data from the public domain and
# test the program for regression testing the same program

from flask import Flask, jsonify, request
app = Flask(__name__)
# Example API endpoint to retrieve artist information
@app.route('/artists')
def get_artists():
    # TODO: Query the public domain data source and retrieve artist information
    artists = [
        {'name': 'John', 'genre': 'Music'},
        {'name': 'Jane', 'genre': 'Dance'},
        
    ]
    return jsonify(artists)

if __name__ == '__main__':
    app.run(debug=True)


import requests
def test_get_artists():
    response = requests.get('http://localhost:5000/artists')
    assert response.status_code == 200
    artists = response.json()
    assert len(artists) > 0

