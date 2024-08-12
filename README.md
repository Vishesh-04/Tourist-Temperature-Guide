# Tourist temperature Guide

## Project Description

The Tourist Temperature Guide is a Temperature Alert Agent built using Fetch.AI's uAgent library. It provides a user-friendly interface where users can input their desired location and preferred temperature range. The agent then fetches real-time weather data, including temperature, humidity, cloud conditions, wind speed, and air quality index (AQI), and alerts the user if the current temperature of the location falls outside their specified range.

## Features
### 1.Location-Based Weather Query:
    . Users can input any location to retrieve the latest weather data.
    
    . The agent automatically fetches and displays the current weather conditions of the specified location.

### 2.Temperature Alert System:
    . Users can set a minimum and maximum acceptable temperature range.
    . The agent compares the current temperature of the location against the user-defined range and provides alerts if the temperature is outside the specified range.
    . Alerts are categorized into:
        .  Too Cold: If the current temperature is below the minimum acceptable range.
        . Too Hot: If the current temperature is above the maximum acceptable range.
        . Within Range: If the current temperature is within the acceptable range.
### 3.Real-Time Weather Data:
    . Temperature: Displays the current temperature in degrees Celsius.
    . Humidity: Provides the current humidity levels.
    . Cloud Conditions: Shows the current cloud coverage at the location.
    . Wind Speed: Displays wind speed in miles per hour (mph).
    . Air Quality Index (AQI): Gives the AQI level in terms of PM 2.5.
    . Local Time: Shows the local time of the queried location.
    . Weather Condition: Describes the current weather conditions (e.g., sunny, rainy).
### 4. Error Handling:
    . The agent handles exceptions and notifies users if there is a failure in fetching weather data.


## Use Case 
### 1.Travel Planning:
    . Scenario: A user is planning a vacation and wants to ensure the weather at their destination is within a comfortable temperature range.
    . Solution: The user inputs the destination and preferred temperature range. The agent provides real-time weather information and alerts the user if the weather is too hot or too cold, helping them make informed travel decisions.

### 2.Outdoor Event Planning:
    . Scenario: An event organizer needs to ensure that the weather conditions will be suitable for an outdoor event.
    . Solution: The organizer inputs the event location and acceptable temperature range. The agent monitors the weather and alerts the organizer if the temperature falls outside the acceptable range, allowing for contingency planning.

### 3.Health and Safety Monitoring:
    . Scenario: A user with health conditions that are sensitive to extreme temperatures needs to monitor the weather before going outside.
    . Solution: The user inputs their location and safe temperature range. The agent provides real-time updates, helping the user avoid exposure to potentially harmful weather conditions.

### 4.Tourism and Hospitality:
    . Scenario: A hotel provides a service to its guests to help them plan their daily activities based on the weather.
    . Solution: The hotel integrates the agent into its website, allowing guests to check the weather and receive alerts directly from the hotel’s platform.

## Technical Details 
    . Backend: The agent is built using Fetch.AI's uAgent library.
    . Weather Data Source: The agent fetches weather data from the WeatherAPI, using the API key and query parameters to retrieve relevant weather information.
    . Protocol: The temperature_protocol handles user queries and manages responses.
    . Data Handling: The agent processes weather data to provide status alerts and detailed weather information, ensuring users receive timely and accurate updates.

## Future Enhancements 
    . Historical Weather Data: Provide users with historical weather trends to help in better decision-making.
    . Forecasting: Integrate weather forecasting to alert users about future weather conditions.
    . Localization: Support multiple languages to cater to a global audience.
    . Enhanced Web Interface: Develop a more interactive web interface with maps and visual alerts.
    . Web Interface Integration: The agent's outputs can be displayed on a webpage, providing users with a visual and interactive experience.

## Project Implementation Video
[Project Demo Video Link](https://drive.google.com/file/d/1bwg709i3P1wnkFI3iR57dBnICtbp27BR/view?usp=sharing)

## How to Run the Project

### Step 1: Create a Acoount on DeltaV

### Step 2: Search for Tourist Temperature Guide

### Step 3: Follow the Demo Video 
