# AirportSearch -- HackUTD VI 2019
Find out airports all over the world using keywords

Used the amadeus api to search up International airports in major cities using keywords.
Backend - Flask
Frontend - HTML, CSS, Bootstrap

Before running:
-- Update Access token in app.py line 20 (After Bearer)
-- Instructions given in pdf

POST request details for access token request:
    URL -- https://test.api.amadeus.com/v1/security/oauth2/token
    Header -- "Content-Type" : "application/x-www-form-urlencoded"
    Body -- grant_type=client_credentials&client_id=qAsgL1xmTETsBpHvYxs78BWFfKzWiuXu&client_secret=l28a49Ie3CBcRpUP 

Run:
python app.py
