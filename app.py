import discord , random , requests , datetime , math , json , asyncio
from discord.ext import commands
from bs4 import BeautifulSoup

#CHANGE TOKEN
#N2YO_API_KEY
#CITY_NAME
#API_KEY

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

TOKEN = "YOUR_TOKEN_IN_DISCORD_BOT"

class Iss_App:
    N2YO_API_KEY = 'YOUR_API_IN_N2YO'
    THRESHOLD_DISTANCE = 900  # Threshold distance in km for ISS passing over location
    MY_LATITUDE = #YOUR_LAT
    MY_LONGITUDE = #YOUR_LONG
      
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        # Convert degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        # Apply haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        km = 6371 * c
        return km

    async def send_iss_alert(self, message):
        channel = bot.get_channel(UR_CHANNEL_ID)  # Replace with your desired channel ID
        await channel.send(message)
      
    async def get_iss_location(self):  
        print("ISS monitoring is now started..")
        while True:        
            try:
                response = requests.get('https://api.n2yo.com/rest/v1/satellite/positions/25544/0/0/0/1/&apiKey={}'.format(self.N2YO_API_KEY))
                data = json.loads(response.text)
                iss_latitude = float(data['positions'][0]['satlatitude'])
                iss_longitude = float(data['positions'][0]['satlongitude'])
                distance = self.calculate_distance(self.MY_LATITUDE, self.MY_LONGITUDE, iss_latitude, iss_longitude)
                if distance <= self.THRESHOLD_DISTANCE:
                    messages = ["🌸 Alert: Calling all space babes! The ISS is about to grace your skies, within 900 km of where you are! Get starry-eyed! 🛰️❗️",
           "🌸 Attention, space goddesses! The ISS is about to dance across your skies, coming within 900 km of where you are! Get ready to be captivated! 🛰️❗️",
           "🌸 Space babes, get ready! The ISS is about to grace your skies within 900 km of where you are! 🛰️❗️",
           "🌸 Listen up, starry-eyed beauties! Prepare for a celestial treat as the ISS graces your skies within 900 km of your whereabouts! lol 🛰️❗️"]
                    message = random.choice(messages)    
                    print(message)
                    await self.send_iss_alert(message)
                    await asyncio.sleep(360)
                else:
                    # else for an iss not visible
                    await asyncio.sleep(40)
            except Exception as e:
                print(f"Error occurred in Iss tracker function: {e}")
                await asyncio.sleep(3600)
                
       

    async def run(self):
        await self.get_iss_location()

def iss_monitoring():
    app = Iss_App()
    asyncio.create_task(app.run())

async def start_iss_monitoring():
    await bot.wait_until_ready()
    iss_monitoring()


@bot.event
async def on_ready():
    print(f"{bot.user} is now started..")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    # Start the ISS tracking background task
    bot.loop.create_task(start_iss_monitoring())
    
def weather():   
    CITY_NAME= 'YOUR_CITY'
    API_KEY = 'YOUR_API_IN_OPENWEATHERMAP'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&units=imperial&APPID={API_KEY}")
    if weather_data.json()['cod'] == '404':
        t_weather = "Hey there! 🌸 I apologize, but it seems that there's a temporary issue with the weather site I usually rely on."
        return t_weather       
    else:
        temp_f = weather_data.json()['main']['temp']
        feels_like_f = weather_data.json()['main']['feels_like']
        feels_like_c = round((feels_like_f - 32) * 5/9)
        temp_min_f = weather_data.json()['main']['temp_min']
        temp_min_c = round((temp_min_f - 32) * 5/9)
        humidity = weather_data.json()['main']['humidity']  # Retrieve humidity data
        dew_point_f = temp_f - ((100 - humidity)/5)  # Retrieve dew_point data
        dew_point_c = round((dew_point_f - 32) * 5/9)
        visibility_meters = weather_data.json()['visibility']  # Retrieve visibility data
        visibility_km = visibility_meters / 1000
        wind_speed_mph = weather_data.json()['wind']['speed']  # Retrieve wind_speed data
        wind_speed_ms = wind_speed_mph * 0.44704
        wind_speed_rounded = round(wind_speed_ms, 1)
        wind_direction = weather_data.json()['wind']['deg']  # Retrieve wind_direction data
        # Convert the wind direction angle to a cardinal direction
        if 348.75 <= wind_direction < 11.25:
            direction = "N"
        elif 11.25 <= wind_direction < 33.75:
            direction = "NNE"
        elif 33.75 <= wind_direction < 56.25:
            direction = "NE"
        elif 56.25 <= wind_direction < 78.75:
            direction = "ENE"
        elif 78.75 <= wind_direction < 101.25:
            direction = "E"
        elif 101.25 <= wind_direction < 123.75:
            direction = "ESE"
        elif 123.75 <= wind_direction < 146.25:
            direction = "SE"
        elif 146.25 <= wind_direction < 168.75:
            direction = "SSE"
        elif 168.75 <= wind_direction < 191.25:
            direction = "S"
        elif 191.25 <= wind_direction < 213.75:
            direction = "SSW"
        elif 213.75 <= wind_direction < 236.25:
            direction = "SW"
        elif 236.25 <= wind_direction < 258.75:
            direction = "WSW"
        elif 258.75 <= wind_direction < 281.25:
            direction = "W"
        elif 281.25 <= wind_direction < 303.75:
            direction = "WNW"
        elif 303.75 <= wind_direction < 326.25:
            direction = "NW"
        elif 326.25 <= wind_direction < 348.75:
            direction = "NNW"
        else:
            direction = "Unknown"
        greetings = ["🌸 Hey!","🌸 Hey hey!"]
        greeting = random.choice(greetings)
        t_weather = f"{greeting} the weather in our city is {temp_min_c}°C but feels like {feels_like_c}°C , wind from {direction} ({wind_speed_rounded}m/s), humidity {humidity}% ,dew point {dew_point_c}°C and {visibility_km} km visibility :>"      
        return t_weather
    
def astronomy():  
    from datetime import date
    events = [
        ("Delta Aquariids Meteor Shower", date(2023, 7, 30), "Moon phase: 95.6%."),
        ("Full Moon (Supermoon)", date(2023, 8, 1), ""),
        ("Mercury at Greatest Eastern Elongation", date(2023, 8, 9), "The best time to photograph Mercury is shortly after Sunset."),
        ("Perseids Meteor Shower", date(2023, 8, 12), "Moon phase: 10.0%."),
        ("New Moon", date(2023, 8, 16), ""),
        ("Saturn at opposition", date(2023, 8, 27), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Saturn and its rings."),
        ("Full Moon (Supermoon)", date(2023, 8, 31), ""),
        ("New Moon", date(2023, 9, 15), ""),
        ("Neptune at opposition", date(2023, 9, 19), "It's brighter than at any other time of the year and is visible throughout the night."),
        ("Mercury at Greatest Western Elongation", date(2023, 9, 22), "The best time to photograph Mercury is shortly before Sunrise."),
        ("Fall or spring equinox", date(2023, 9, 23), "This is the best time to photograph the zodiacal light."),
        ("Full Moon", date(2023, 9, 29), ""),
        ("Milky Way season ends (Northern Hemisphere)", date(2023, 10, 14), ""),
        ("Annular solar eclipse", date(2023, 10, 14), "The eclipse path will begin in the Pacific Ocean off the coast of southern Canada and move across the southwestern United States and Central America, Columbia, and Brazil. A partial eclipse will be visible throughout much of North and South America."),
        ("Orionids Meteor Shower", date(2023, 10, 21), "Moon phase: 51.2%."),
        ("Venus at Greatest Western Elongation", date(2023, 10, 23), "This is the best time to view Venus since it's so bright that it becomes the third brightest object in the sky after the Sun and the Moon."),
        ("Partial lunar eclipse", date(2023, 10, 28), "Visible in Africa, Oceania, the Americas, Asia, and Europe."),
        ("Full Moon", date(2023, 10, 28), ""),
        ("Jupiter at opposition", date(2023, 11, 3), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Jupiter and its moons."),
        ("New Moon", date(2023, 11, 13), ""),
        ("Uranus at opposition", date(2023, 11, 13), "It's brighter than at any other time of the year. You need a telescope."),
        ("Leonids Meteor Shower", date(2023, 11, 17), "Moon phase: 26.5%."),
        ("Full Moon", date(2023, 11, 27), ""),
        ("Manhattanhenge (Sunrise)", date(2023, 11, 30), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("Mercury at Greatest Eastern Elongation", date(2023, 12, 4), "The best time to photograph Mercury is shortly after Sunset."),
        ("New Moon", date(2023, 12, 13), ""),
        ("Geminids Meteor Shower", date(2023, 12, 14), "Moon phase: 5.6%."),
        ("Winter or summer solstice", date(2023, 12, 22), "It marks the shortest or longest day of the year."),
        ("Ursids Meteor Shower", date(2023, 12, 22), "Moon phase: 85.3%."),
        ("Full Moon", date(2023, 12, 27), "")]
    today = datetime.date.today()
    next_event = None  
    for event in events:
        if event[1] >= today:
            next_event = event
            break
    if next_event is not None:
        name, date, info = next_event
        emojis = ["✨🌠","✨🌙","🌠🌙","🌙💫"]
        emoji = random.choice(emojis)
        astronomy = f"The {name} will happen on {date}!!. {info}{emoji}"
        return astronomy
    else:
        astronomy = ["Oopsie! No upcoming events at the moment, but our stargazing journey continues! 🌌✨ I'll keep you updated!",
                     "Aww, no upcoming events for now, but don't worry! More celestial magic is on its way! 🌟💖I keep an eye out for future updates! 🌠🌙",
                     "Right now, there are no upcoming events, but that's just a little break before the next stellar spectacle! 🌠✨ Stay patient and i'll keep u updated!"]
        return astronomy


@bot.tree.command(name="help")
async def help_command(interaction: discord.Interaction):
    """
    Displays the list of available commands and their descriptions.
    """
    help_text = """
    Hey! check out these cool commands you can use:
    `🌦️ /weather`: i'll send the weather information.
    `🌌 /event`: i'll send information about upcoming astronomy events.
    `🌸 /news`: i'll send the latest news in our city.
    """
    await interaction.response.send_message(help_text)
    
    
    

@bot.tree.command(name="weather")
async def get_weather(interaction: discord.Interaction):
    """
    Get the weather information in our city
    """
    weather_info = weather()
    await interaction.response.send_message(weather_info)


@bot.tree.command(name="event")
async def get_upcoming_astronomy_event(interaction: discord.Interaction):
    """
    Get information about upcoming astronomy events.
    """  
    event_info = astronomy()
    await interaction.response.send_message(event_info)
    
    
    
@bot.tree.command(name="sendamessage")
async def send_message_to_channel(interaction: discord.Interaction, channel_name: str, *, message: str):
    """
    Sends a message to a specified channel in the server.
    Usage: !sendm {channel name} {message}
    """
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)
    if channel is not None:
        await channel.send(message)
        await interaction.response.send_message(f"Message sent to {channel.mention}")
    else:
        await interaction.response.send_message(f"Channel `{channel_name}` not found in the server.")

bot.run(TOKEN)
