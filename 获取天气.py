import requests

API_KEY = 'YOUR_API_KEY' # 获取的OpenWeather密钥
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric&lang=zh-CN"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # 返回的数据格式为JSON
            main = data['main']
            wind = data['wind']
            weather = data['weather'][0]
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            wind_speed = wind['speed']
            description = weather['description']

            # 输出天气信息
            print(f"城市: {city_name}")
            print(f"天气描述: {description}")
            print(f"温度: {temperature}°C")
            print(f"气压: {pressure} hPa")
            print(f"湿度: {humidity}%")
            print(f"风速: {wind_speed} m/s")
        else:
            print("无法获取天气数据，请检查城市名称或API配置")
    except Exception as e:
        print(f"发生错误: {e}")

# 运行程序，获取用户输入的城市天气
def main():
    city_name = input("请输入城市名称: ")
    get_weather(city_name)

    while 1:
        print('\n')
        second = input("继续查询请输入1，退出请输入其他: ")
        if second == "1":
            city_name = input("请输入城市名称: ")
            get_weather(city_name)
        else:
            break

    print("已经成功退出")

if __name__ == '__main__':
    main()
