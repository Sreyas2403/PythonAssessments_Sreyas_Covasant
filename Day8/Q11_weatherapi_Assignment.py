from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    response_format = request.args.get('format', 'json').lower()
    
    temperature = round(random.uniform(-10, 40), 1)
    
    weather_data = {
        'city': city,
        'temperature': temperature,
        'unit': 'C',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }

    if response_format == 'xml':
        xml = f'''<weather>
    <city>{weather_data['city']}</city>
    <temperature>{weather_data['temperature']}</temperature>
    <unit>{weather_data['unit']}</unit>
    <timestamp>{weather_data['timestamp']}</timestamp>
</weather>'''
        return xml, 200, {'Content-Type': 'application/xml'}
    
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run()