import requests
from uagents import Agent, Context, Protocol, Model
from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType

# Define the protocol for temperature queries
temperature_protocol = Protocol(name="temperature_protocol")

# Define the model for querying user requests
class QueryUserRequest(Model):
    location: str = Field(description="Location for weather query")
    max_temperature: float = Field(description="Maximum acceptable temperature")
    min_temperature: float = Field(description="Minimum acceptable temperature")


# Function to fetch data from the weather API
def fetch_data(location):
    try:
        WEATHER_API_KEY = "bb105451e60b48b483880333240102"
        api_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=yes"
        response = requests.get(api_url)
        data = response.json()

        status = True
        time_data = data['location']['localtime']
        temp_data = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_mph = data['current']['wind_mph']
        cloud = data['current']['cloud']
        aqi = data['current']['air_quality']['pm2_5']

        return status, time_data, temp_data, condition, humidity, cloud, wind_mph, aqi

    except Exception as e:
        print(f"Error fetching temperature data: {str(e)}")
        status = False
        return status, None, None

# Handler for processing temperature query requests
@temperature_protocol.on_message(model=QueryUserRequest, replies={UAgentResponse})
async def handle_query_request(ctx: Context, sender: str, msg: QueryUserRequest):
    api_status, api_time, api_temp, condition, humidity, cloud, wind, aqi = fetch_data(msg.location)

    if api_status:
        if api_temp < msg.min_temperature:
            status = "Temperature Alert: It's Colder than the given range"
        elif api_temp > msg.max_temperature:
            status = "Temperature Alert: It's Hotter than the given range"
        else:
            status = "Temperature is within the range"


        final_message_str = f'Location : {msg.location}\nMaximum acceptable temperature: {msg.max_temperature}°C\nMinimum acceptable temperature: {msg.min_temperature}°C\nStatus: {status}\nTime: {api_time}\nTemperature: {api_temp}°C\nWeather Conditions: {condition}\nHumidity Levels: {humidity}\nCloud Levels: {cloud}\nWind Speed in mph: {wind}mph\nAQI in terms of PM 2.5: {aqi}'
        await ctx.send(sender, UAgentResponse(message=final_message_str, type=UAgentResponseType.FINAL))
    else:
        error_message = "Failed to retrieve temperature data."
        await ctx.send(sender, UAgentResponse(message=error_message, type=UAgentResponseType.FINAL))
# Create an instance of the Agent class
agent = Agent()
agent.include(temperature_protocol, publish_manifest=True)

if __name__ == "__main__":
    agent.run()