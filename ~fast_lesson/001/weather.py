import pyowm

owm = pyowm.OWM('42901314474499fbf7a3f3e5c49b6ad9')
obs = owm.weather_at_place('San Francisco, US')
print(obs)

