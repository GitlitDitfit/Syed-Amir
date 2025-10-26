import requests

def get_temperature(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(base_url)
    weather_data = response.json()
    try:
        temperature = weather_data['main']['temp']
        return temperature
    except KeyError:
        return "City not found. Please check the city name."

def main():
    api_key = "5c6cc07485c79e7764731a9563164bde" 
    
    city = input("Enter the city name: ")
    temperature = get_temperature(city, api_key)
    
    if isinstance(temperature, str):
        print(temperature)
    else:
        print(f"The temperature in {city} is {temperature}°C")

if __name__ == "__main__":
    main()