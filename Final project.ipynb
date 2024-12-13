{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "eb34b4a2-0530-4c6b-bafd-170d726798fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HTTP Status Code: 200\n",
      "City: London\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "'values'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[19], line 25\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m weather_data:\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCity: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mCITY\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 25\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTemperature: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mweather_data[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalues\u001b[39m\u001b[38;5;124m'\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtemperature\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m°C\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     26\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPrecipitation Type: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mweather_data[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalues\u001b[39m\u001b[38;5;124m'\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mprecipitationType\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHumidity: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mweather_data[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalues\u001b[39m\u001b[38;5;124m'\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhumidity\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mKeyError\u001b[0m: 'values'"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Your API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "CITY = 'London'  # You can change this to any city you want\n",
    "LAT = 51.5074    # Latitude for London (or any location)\n",
    "LON = -0.1278    # Longitude for London (or any location)\n",
    "\n",
    "# Base URL for the Tomorrow.io weather API\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP status code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    # Print out some of the key weather data\n",
    "    weather_data = data.get('data', {}).get('timelines', [])[0]\n",
    "    if weather_data:\n",
    "        print(f\"City: {CITY}\")\n",
    "        print(f\"Temperature: {weather_data['values']['temperature']}°C\")\n",
    "        print(f\"Precipitation Type: {weather_data['values']['precipitationType']}\")\n",
    "        print(f\"Humidity: {weather_data['values']['humidity']}%\")\n",
    "    else:\n",
    "        print(\"No weather data available.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "27a6f6fd-9d5a-432e-8cdf-1d7e56eab717",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python executable: C:\\Users\\shock\\anaconda3\\python.exe\n",
      "Python version: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)]\n",
      "Script started\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(\"Python executable:\", sys.executable)\n",
    "print(\"Python version:\", sys.version)\n",
    "print(\"Script started\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f59c81a6-f421-4b13-9068-9da327ecf810",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'data': {'timelines': [{'timestep': 'current', 'endTime': '2024-12-12T10:24:00Z', 'startTime': '2024-12-12T10:24:00Z', 'intervals': [{'startTime': '2024-12-12T10:24:00Z', 'values': {'humidity': 94, 'precipitationType': 0, 'temperature': 6.63}}]}]}}\n"
     ]
    }
   ],
   "source": [
    "print(response.json())  # Prints the full JSON response to inspect the structure\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "19e3bbf2-cb57-4190-9aba-8ed7dd6e0044",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HTTP Status Code: 200\n",
      "City: London\n",
      "Temperature: 6.63°C\n",
      "Humidity: 94%\n",
      "Precipitation Type: 0\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Your new API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "LAT = 51.5074    # Latitude for London (or your preferred location)\n",
    "LON = -0.1278    # Longitude for London (or your preferred location)\n",
    "\n",
    "# API request URL\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP Status Code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    # Access the weather data\n",
    "    timeline_data = data.get('data', {}).get('timelines', [])[0].get('intervals', [])[0].get('values', {})\n",
    "    \n",
    "    if timeline_data:\n",
    "        temperature = timeline_data.get('temperature', 'N/A')\n",
    "        humidity = timeline_data.get('humidity', 'N/A')\n",
    "        precipitation = timeline_data.get('precipitationType', 'N/A')\n",
    "        \n",
    "        print(f\"City: London\")\n",
    "        print(f\"Temperature: {temperature}°C\")\n",
    "        print(f\"Humidity: {humidity}%\")\n",
    "        print(f\"Precipitation Type: {precipitation}\")\n",
    "    else:\n",
    "        print(\"No weather data available.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "23bb9dde-c275-4cf4-bec8-0cef6ac5d273",
   "metadata": {},
   "outputs": [],
   "source": [
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity,windSpeed,pressure&timesteps=current&apikey={API_KEY}'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ce248d2c-7c1e-4364-a0c1-a018c8dc164c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HTTP Status Code: 200\n",
      "City: London\n",
      "Temperature: 6.63°C\n",
      "Humidity: 94%\n",
      "Precipitation Type: 0\n",
      "Wind Speed: 1.31 m/s\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Your API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "LAT = 51.5074    # Latitude for London (or your preferred location)\n",
    "LON = -0.1278    # Longitude for London (or your preferred location)\n",
    "\n",
    "# API request URL (removed 'pressure' field as it's invalid)\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity,windSpeed&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP Status Code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    # Access the weather data\n",
    "    timeline_data = data.get('data', {}).get('timelines', [])[0].get('intervals', [])[0].get('values', {})\n",
    "    \n",
    "    if timeline_data:\n",
    "        temperature = timeline_data.get('temperature', 'N/A')\n",
    "        humidity = timeline_data.get('humidity', 'N/A')\n",
    "        precipitation = timeline_data.get('precipitationType', 'N/A')\n",
    "        wind_speed = timeline_data.get('windSpeed', 'N/A')\n",
    "        \n",
    "        print(f\"City: London\")\n",
    "        print(f\"Temperature: {temperature}°C\")\n",
    "        print(f\"Humidity: {humidity}%\")\n",
    "        print(f\"Precipitation Type: {precipitation}\")\n",
    "        print(f\"Wind Speed: {wind_speed} m/s\")\n",
    "    else:\n",
    "        print(\"No weather data available.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8c66a444-284c-495a-9f18-ba5ae5bffe8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: matplotlib in c:\\users\\shock\\anaconda3\\lib\\site-packages (3.9.2)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (1.4.4)\n",
      "Requirement already satisfied: numpy>=1.23 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (24.1)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (10.4.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (3.1.2)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\shock\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install matplotlib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d69a0f16-ea87-440c-b999-f8e53728b65d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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gfLG3UxACSQnJ2vs2LFasmSJlixZoi5dunjWFQaXL774wnNhcGHQqV69ulwul5YuXVrs3T+FbRs2bND69es1ZcoU9e7d27P++++/L5fXU716dV100UUaOXJksesLP7QKuVyuMtmumWn+/PkKDQ1V69atJUnTp09XQECAPvzwQwUFBXn6zpkzp8TjvvPOO0pMTNSMGTO8as3NzT3vWgs/oPfs2aPY2Fivdbt371b16tW92spqH52+7dPt3r1blSpVUpUqVUo9Zl5envbv3+8VPrKysrz6ValSRZUqVTrjtiUVee2Ar3FkBiiBK6+8Un5+fvrggw+0ceNGdejQwbMuMjJSzZs319SpU5WRkeF1S3a3bt1kZvrxxx/VunXrIo9mzZpJ+t8H4emB58033yxSS1n8q7dbt27asGGD6tSpU2xdp4eZsjJixAht2rRJAwcO9AQXl8slf39/+fn5efodO3ZM//rXv4o8//QjTIVcLpcCAwO9AkVWVlaJ7mY6k8JTRu+8845Xe3p6ujZv3qyOHTue99jn0qBBA11wwQWaNm2a12m5I0eOaObMmZ47nEqjcF6+++67Xu3Tpk3zWg4NDVWbNm00a9Ysr31dUFCgd955R7Gxsapfv35pXxJQrjgyA5RA4e3Cc+bMUaVKlTzXyxRKSkrSuHHjJHl/v0z79u1111136Y477tB//vMfXXnllQoNDdWePXu0bNkyNWvWTPfcc48aNmyoOnXqaOjQoTIzVa1aVfPnz1dqamqRWgoD0EsvvaTevXsrICBADRo0UHh4eIlfz1NPPaXU1FS1a9dODzzwgBo0aKDjx48rIyNDH3/8sd54440iRyNK4+DBg55TZEeOHNGWLVs0ffp0LV26VN27d9eIESM8fbt27aqxY8eqZ8+euuuuu7R//349//zzxR7JatasmaZPn64ZM2aodu3aCgoKUrNmzdStWzfNmjVLAwYM0E033aTMzEw9/fTTqlWrlr777rvzeg0NGjTQXXfdpVdeeUWVKlXSn/70J2VkZOiJJ55QXFycHnzwwfPbOaeYP39+sX+3m266SWPGjNGtt96qbt26qX///srNzdVzzz2ngwcP6plnnin1tjp37qwrr7xSQ4YM0ZEjR9S6dWstX7682NA4evRoderUScnJyXr44YcVGBio119/XRs2bNB7771XpkehgDLhw4uPAUcZ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AwAAHI0wAwAAHK3UYSYzM1O7du3yLH/11VcaNGiQJkyYUKaFAQAAlESpw0zPnj21ePFiSVJWVpY6deqkr776So8++qieeuqpMi8QAADgbEodZjZs2KBLL71UkvTvf/9bTZs21YoVKzRt2jRNmTKlrOsDAAA4q1KHmZMnT8rtdkuSPv30U1133XWSpIYNG2rPnj1lWx0AAMA5lDrMNGnSRG+88YaWLl2q1NRUXXvttZKk3bt3q1q1amVeIAAAwNmUOsw8++yzevPNN9WhQwf16NFDF198sSRp3rx5ntNPAAAAvxX/0j6hQ4cO2rdvnw4dOqQqVap42u+66y6FhISUaXEAAADncl7fM2NmWr16td58803l5ORIkgIDAwkzAADgN1fqIzM7duzQtddeq507dyo3N1edOnVSeHi4xowZo+PHj+uNN94ojzoBAACKVeojMwMHDlTr1q114MABBQcHe9r/8pe/6LPPPivT4gAAAM6l1Edmli1bpuXLlyswMNCrPT4+Xj/++GOZFQYAAFASpT4yU1BQoPz8/CLtu3btUnh4eJkUBQAAUFKlDjOdOnXSuHHjPMsul0uHDx/W8OHD1aVLl7KsDQAA4JxKfZrpxRdfVHJysho3bqzjx4+rZ8+e+u6771S9enW999575VEjAADAGZU6zMTExGjdunV67733tGbNGhUUFKhfv3669dZbvS4IBgAA+C2UOsxIUnBwsPr27au+ffuWdT0AAAClUuow8/bbb591fa9evc67GAAAgNIqdZgZOHCg1/LJkyd19OhRzzcAE2YAAMBvqdR3Mx04cMDrcfjwYW3ZskWXX345FwADAIDf3Hn9NtPp6tWrp2eeeabIURsAAIDyViZhRpL8/Py0e/fushoOAACgREp9zcy8efO8ls1Me/bs0auvvqr27duXWWEAAAAlUeowc8MNN3gtu1wu1ahRQ1dddZVeeOGFsqoLAACgREodZgoKCsqjDgAAgPNSZtfMAAAA+EKJjswMHjy4xAOOHTv2vIsBAAAorRKFmbVr15ZoMJfL9auKAQAAKK0ShZnFixeXdx0AAADnhWtmAACAo53Xr2anp6fr/fff186dO3XixAmvdbNmzSqTwgAAAEqi1Edmpk+frvbt22vTpk2aPXu2Tp48qU2bNunzzz9XZGRkedQIAABwRqUOM6NGjdKLL76oDz/8UIGBgXrppZe0efNmde/eXRdeeGF51AgAAHBGpQ4z27ZtU9euXSVJbrdbR44ckcvl0oMPPqgJEyaUeYEAAABnU+owU7VqVeXk5EiSLrjgAm3YsEGSdPDgQR09erRsqwMAADiHEoeZdevWSZKuuOIKpaamSpK6d++ugQMH6s4771SPHj3UsWPHcikSAADgTEp8N1PLli3VokUL3XDDDerRo4ckadiwYQoICNCyZct044036oknnii3QgEAAIpT4iMzy5cvV8uWLfX888+rTp06uu2225SWlqYhQ4Zo3rx5Gjt2rKpUqVKetQIAABRR4jDTtm1bvfXWW8rKytL48eO1a9cuXX311apTp45GjhypXbt2lWedAAAAxSr1BcDBwcHq3bu3lixZoq1bt6pHjx568803lZiYqC5dupRHjQAAAGf0q37OoE6dOho6dKgee+wxRUREaOHChWVVFwAAQImc188ZSFJaWpomTZqkmTNnys/PT927d1e/fv3KsjYAAIBzKlWYyczM1JQpUzRlyhRt375d7dq10yuvvKLu3bsrNDS0vGoEAAA4oxKHmU6dOmnx4sWqUaOGevXqpb59+6pBgwblWRsAAMA5lTjMBAcHa+bMmerWrZv8/PzKsyYAAIASK3GYmTdvXnnWAQAAcF5+1d1MAAAAvkaYAQAAjkaYAQAAjkaYAQAAjkaYAQAAjkaYAQAAjlZhwszo0aPlcrk0aNAgT5uZKSUlRTExMQoODlaHDh20ceNG3xUJAAAqnAoRZtLT0zVhwgRddNFFXu1jxozR2LFj9eqrryo9PV3R0dHq1KmTcnJyfFQpAACoaHweZg4fPqxbb71Vb731lqpUqeJpNzONGzdOjz32mG688UY1bdpUU6dO1dGjRzVt2rQzjpebm6tDhw55PQAAwO+Xz8PMvffeq65du+rqq6/2at++fbuysrLUuXNnT5vb7VZSUpJWrFhxxvFGjx6tyMhIzyMuLq7cagcAAL7n0zAzffp0rVmzRqNHjy6yLisrS5IUFRXl1R4VFeVZV5xhw4YpOzvb88jMzCzbogEAQIVS4t9mKmuZmZkaOHCgFi1apKCgoDP2c7lcXstmVqTtVG63W263u8zqBAAAFZvPjsysXr1ae/fuVatWreTv7y9/f3+lpaXp5Zdflr+/v+eIzOlHYfbu3VvkaA0AAPjj8lmY6dixo7755hutW7fO82jdurVuvfVWrVu3TrVr11Z0dLRSU1M9zzlx4oTS0tLUrl07X5UNAAAqGJ+dZgoPD1fTpk292kJDQ1WtWjVP+6BBgzRq1CjVq1dP9erV06hRoxQSEqKePXv6omQAAFAB+SzMlMSQIUN07NgxDRgwQAcOHFCbNm20aNEihYeH+7o0AABQQbjMzHxdRHk6dOiQIiMjlZ2drYiICF+XA5S5hKEf+boE+FDGM119XQJQLkrz+e3z75kBAAD4NQgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0QgzAADA0XwaZkaPHq1LLrlE4eHhqlmzpm644QZt2bLFq4+ZKSUlRTExMQoODlaHDh20ceNGH1UMAAAqGp+GmbS0NN17771atWqVUlNTlZeXp86dO+vIkSOePmPGjNHYsWP16quvKj09XdHR0erUqZNycnJ8WDkAAKgo/H258QULFngtT548WTVr1tTq1at15ZVXysw0btw4PfbYY7rxxhslSVOnTlVUVJSmTZum/v37FxkzNzdXubm5nuVDhw6V74sAAAA+VaGumcnOzpYkVa1aVZK0fft2ZWVlqXPnzp4+brdbSUlJWrFiRbFjjB49WpGRkZ5HXFxc+RcOAAB8psKEGTPT4MGDdfnll6tp06aSpKysLElSVFSUV9+oqCjPutMNGzZM2dnZnkdmZmb5Fg4AAHzKp6eZTnXffffp66+/1rJly4qsc7lcXstmVqStkNvt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fbfeeOMN+fn5eY1z0UUXKSEhQe+++2651FlRJCcn6/Dhw/rPf/7jaVu6dKmio6OVnp6uo0f/9+vaS5YsUUxMjOrXr6/AwEBFR0eX++/nTZw4UYMHD9YDDzyg9evXa/ny5RoyZIgOHz5crtstSy+//LLuuOMOVapUNh/f8+bN0/XXX3/OfhV9DhNmylh0dLTnERkZKZfL5dX2xRdfqFWrVgoKClLt2rU1YsQI5eXleZ7vcrn05ptvqlu3bgoJCVGjRo20cuVKff/99+rQoYNCQ0PVtm1bbdu2zfOclJQUNW/eXG+++abi4uIUEhKim2++ucgh28mTJ6tRo0YKCgpSw4YN9frrr3vWFR7e//e//60OHTooKChI77zzjvbv368ePXooNjZWISEhatasmd577z3P8/r06aO0tDS99NJLcrlccrlcysjIKPbQ/5w5c7zerArrnjRpkmrXri232y0zU3Z2tu666y7VrFlTERERuuqqq7R+/fqz7vfp06fruuuu82o7ePCg4uPj1bRpUzVr1swTUCTp0UcfVUZGhr788kv17t1bjRs3Vv369XXnnXdq3bp1CgsLk/TLh2uXLl28XjP+97c71bhx45SQkOBZLjzkP2rUKEVFRaly5cqe+f7II4+oatWqio2N1aRJkzzPKe4008cff6z69esrODhYycnJysjI8NruqXNtypQpGjFihNavX++Zj1OmTFHfvn3VrVs3r+fl5eUpOjraa/unKigo0Pvvv+81rzZv3qyLLrpIV111lTp27KiLLrpImzdvliQ999xzuvLKK3XJJZcUO9511133u59HDRo0UExMjJYsWeJpW7Jkia6//nrVqVNHK1as8GpPTk72/Hdxpw4XLlyoRo0aKSwsTNdee6327NnjeX5+fr4GDx6sypUrq1q1ahoyZIjsHF+bNn/+fHXv3l39+vVT3bp11aRJE/Xo0UNPP/20p0/hvB0xYoTnPah///46ceKEp4+ZacyYMapdu7aCg4N18cUX64MPPvDa1qZNm9SlSxeFhYUpKipKt99+u/bt2+dZf+TIEfXq1UthYWGqVauWXnjhhXPu33379unTTz8t8l53Pp8bknT8+HEtWrTIM97rr7+uevXqKSgoSFFRUbrpppu8+lfoOezjI0O/a5MnT7bIyEjP8oIFCywiIsKmTJli27Zts0WLFllCQoKlpKR4+kiyCy64wGbMmGFbtmyxG264wRISEuyqq66yBQsW2KZNm+yyyy6za6+91vOc4cOHW2hoqF111VW2du1aS0tLs7p161rPnj09fSZMmGC1atWymTNn2g8//GAzZ860qlWr2pQpU8zMbPv27SbJEhISPH1+/PFH27Vrlz333HO2du1a27Ztm7388svm5+dnq1atMjOzgwcPWtu2be3OO++0PXv22J49eywvL6/Iazczmz17tp065Qrrvuaaa2zNmjW2fv16KygosPbt29uf//xnS09Pt61bt9pDDz1k1apVs/37959xX1euXNmmT5/u1Xbw4EFr2bKl+fv72wUXXGBff/21mZnl5+dblSpV7K677irR3/H111+3hISEEvV1upKeZiruVM6LL75o8fHxXmOFh4fbvffea99++61NnDjRJNk111xjI0eOtK1bt9rTTz9tAQEBtnPnTjP73zxcu3atmZnt3LnT3G63DRw40L799lt75513LCoqyquWU+fa0aNH7aGHHrImTZp45uPRo0dt+fLl5ufnZ7t37/bUN3fuXAsNDbWcnJxi98XatWtNkmVlZXnaNm3aZFWqVLEdO3ZYRkaGVa5c2TZt2mTfffed1atXz+t01Ok+/vhjc7vddvz48TP2+T3o2bOnde7c2bN8ySWX2Pvvv2/33HOPPfroo2Zmlpuba8HBwfbPf/7TzIrOr8mTJ1tAQIBdffXVlp6ebqtXr7ZGjRp5vac9++yzFhkZaR988IFt2rTJ+vXrZ+Hh4Wc9zdS/f39r2LChZWRknLFP7969LSwszG655RbbsGGDffjhh1ajRg1P7WZmjz76qDVs2NAWLFhg27Zts8mTJ5vb7bYlS5aYmdnu3butevXqNmzYMNu8ebOtWbPGOnXqZMnJyZ4x7rnnHouNjbVFixbZ119/bd26dbOwsLCznmaaPXu2hYaGFjnFdD6fG2ZmH374odWpU8fMzNLT083Pz8+mTZtmGRkZtmbNGnvppZe8+lfkOUyYKUenf6BfccUVNmrUKK8+//rXv6xWrVqeZUn2+OOPe5ZXrlxpkmzixImetvfee8+CgoI8y8OHDzc/Pz/LzMz0tH3yySdWqVIlz3UicXFxNm3aNK9tP/3009a2bVsz+9+HyLhx4875urp06WIPPfSQZ7m487wlDTMBAQG2d+9eT9tnn31mERERRf5nqVOnjr355pvF1nPgwAGT5HW9zKkKA1ahn376ySQVud7hTObOnWuVKlX6Q1w307t3b/Pz87PQ0FCvR1BQ0HmFmfj4eK/91qBBA7viiis8y3l5eRYaGmrvvfeemRUNM8OGDbNGjRp5XUvxj3/844xh5ky1mZk1btzYnn32Wc/yDTfcYH369Dnjvpg9e7b5+fkVuY5j/PjxVr9+fatfv76NHz/ezMw6duxos2fPtvfff9+aNGlizZs3t7S0NK/nrV+/3iSd9YP092DChAkWGhpqJ0+etEOHDpm/v7/99NNPNn36dGvXrp2ZmaWlpZkk27Ztm5kVH2Yk2ffff+8Z97XXXrOoqCjPcq1atbyudTl58qTFxsaeNczs3r3bLrvsMpNk9evXt969e9uMGTO85mjv3r2tatWqduTIEU9b4bVA+fn5dvjwYQsKCrIVK1Z4jd2vXz/r0aOHmZk98cQTXoHOzCwzM9NzjVBOTo4FBgZ6/QNs//79FhwcfNYw8+KLL1rt2rWLtJ/P54aZ2Z133mmDBw82M7OZM2daRETEWQN5RZ7DFf63mX5PVq9erfT0dI0cOdLTlp+fr+PHj+vo0aMKCQmR9Mu5yUJRUVGSpGbNmnm1HT9+XIcOHfL85PyFF16o2NhYT5+2bduqoKBAW7ZskZ+fnzIzM9WvXz/deeednj55eXlFfl69devWXsv5+fl65plnNGPGDP3444/Kzc1Vbm6uQkNDf+3ukCTFx8erRo0anuXVq1fr8OHDqlatmle/Y8eOFTlEeuo6SQoKCip2fXR0tNey/f9D0SU9Px8cHKyCggLl5uYqODi4RM9xsuTkZI0fP96r7csvv9Rtt91W6rGaNGnidW4/KipKTZs29Sz7+fmpWrVq2rt3b7HP37x5sy677DKvv1Xbtm1LXYck/f3vf9eECRM0ZMgQ7d27Vx999JE+++yzM/Y/duyY3G53kXly9913e/3Q7ZQpUxQeHq62bduqQYMGSk9P165du/S3v/1N27dv9/xmT+HcOfW6kd+j5ORkHTlyROnp6Tpw4IDq16+vmjVrKikpSbfffruOHDmiJUuW6MILL1Tt2rXPOE5ISIjq1KnjWa5Vq5ZnnmRnZ2vPnj1ec8Hf31+tW7c+66mmWrVqaeXKldqwYYPS0tK0YsUK9e7dW//85z+1YMECz1y9+OKLPe/H0i9z7vDhw8rMzNTevXt1/PhxderUyWvsEydOqEWLFpJ+eR9bvHix53T1qbZt26Zjx47pxIkTXvVXrVpVDRo0OGPt0i9z8kzvc6X93DAzzZ8/X9OnT5ckderUSfHx8apdu7auvfZaXXvttfrLX/7itR8q8hwmzPyGCgoKNGLECN14441F1p06QQMCAjz/XfhGWlxbQUHBGbdV2Mflcnn6vfXWW2rTpo1Xv9MvVDw9pLzwwgt68cUXNW7cODVr1kyhoaEaNGiQ1/nj4lSqVKnIm0pxF/ievr2CggLVqlXL65x7oTPdflutWjW5XC4dOHDgrDUVqlGjhqpUqeK51uFcfv75Z4WEhPwhgoz0y9+kbt26Xm27du3yWi7p3/fUeSv9Mh+LazvTXD7bB1Np9erVS0OHDtXKlSu1cuVKJSQkeF0wfrrq1avr6NGjOnHihAIDA4vts2/fPj311FP64osv9OWXX6p+/fqqV6+e6tWrp5MnT2rr1q2eD5Sff/5ZkrzC++9R3bp1FRsbq8WLF+vAgQNKSkqS9Ms/KhITE7V8+XItXrxYV1111VnHKW6elNV8aNq0qZo2bap7771Xy5Yt0xVXXKG0tDTPNTxncupc/eijj3TBBRd4rS8MrgUFBfrzn/+sZ599tsgYtWrV0nfffXdedVevXv2M73Ol/dz46quvdOLECV1++eWSpPDwcK1Zs0ZLlizRokWL9OSTTyolJUXp6eme996KPIe5APg31LJlS23ZskV169Yt8vi1V6bv3LlTu3fv9iyvXLlSlSpVUv369RUVFaULLrhAP/zwQ5HtJiYmnnXcpUuX6vrrr9dtt92miy++WLVr1y7yP2JgYKDy8/O92mrUqKGcnBwdOXLE03a27w4p1LJlS2VlZcnf379IrdWrVy/2OYGBgWrcuLE2bdp0zvGlXz6Ib7nlFr377rte+6zQkSNHvC7K3rBhg1q2bFmisf8oatSooaysLK8Pl5L8fUurcePGWrVqlVfb6cunK24+Sr+E3htuuEGTJ0/W5MmTdccdd5x1nMILnM82rwYNGqQHH3xQsbGxys/P9wp0eXl5XnVs2LBBsbGxZ5zHvyfJyclasmSJlixZog4dOnjak5KStHDhQq1ateqcweFsIiMjVatWLa+5kJeXp9WrV5d6rMaNG0uS13vV+vXrPUd8pV/mXFhYmGJjY9W4cWO53W7t3LmzyHtUXFycpF/exzZu3KiEhIQifQr/sRAQEOBV/4EDB7R169az1tqiRQtlZWWV+B9uZzN37lx17drV6x+0/v7+uvrqqzVmzBh9/fXXysjI0Oeff+5ZX5HnMGHmN/Tkk0/q7bffVkpKijZu3KjNmzdrxowZevzxx3/12EFBQerdu7fWr1+vpUuX6oEHHlD37t09p1hSUlI0evRovfTSS9q6dau++eYbTZ48+ZxfglS3bl2lpqZqxYoV2rx5s/r376+srCyvPgkJCfryyy+VkZGhffv2qaCgQG3atFFISIgeffRRff/995o2bZqmTJlyztdx9dVXq23btrrhhhu0cOFCZWRkaMWKFXr88ce9bvc83TXXXKNly5ade0f9f6NGjVJcXJzatGmjt99+W5s2bdJ3332nSZMmqXnz5l63ai5durTMv4zP6Tp06KD//ve/GjNmjLZt26bXXntNn3zySZlv5+6779a2bds0ePBgbdmypUTzKCEhQdu3b9e6deu0b98+5ebmetb9/e9/19SpU7V582b17t37rOPUqFFDLVu2POO8Sk1N1Xfffad7771XknTppZfq22+/1SeffKIJEybIz8/P67TBH2keJScna9myZVq3bp3nyIz0S5h56623dPz48V8VZiRp4MCBeuaZZzR79mx9++23GjBgwDm/dO+ee+7R008/reXLl2vHjh1atWqVevXqpRo1anid8jlx4oT69eunTZs26ZNPPtHw4cN13333qVKlSgoPD9fDDz+sBx98UFOnTtW2bdu0du1avfbaa5o6daok6d5779XPP/+sHj166KuvvtIPP/ygRYsWqW/fvsrPz1dYWJj69eunRx55RJ999pk2bNigPn36nPMftS1atFCNGjW0fPnyX7XvpKK3ZH/44Yd6+eWXtW7dOu3YsUNvv/22CgoKnDOHfXe5zu9fcRfBLliwwNq1a2fBwcEWERFhl156qU2YMMGzXpLNnj3bs3z6BZFmZ76z5PXXX7eYmBgLCgqyG2+80X7++Wevbb/77rvWvHlzCwwMtCpVqtiVV15ps2bNOuN2zH65KO3666+3sLAwq1mzpj3++OPWq1cvr4vstmzZYpdddpkFBwebJNu+fbuZ/XIBZd26dS0oKMi6detmEyZMKHIBcHEXah46dMjuv/9+i4mJsYCAAIuLi7Nbb73Vc8dLcTZv3mzBwcF28ODBM/Y53cGDB23o0KFWr149CwwMtKioKLv66qtt9uzZnos+d+3aZQEBAV4XV/+eleZL88aPH29xcXEWGhpqvXr1spEjRxa5APj0sYq7WDw+Pt5efPFFMyt+Hs6fP9/q1q1rbrfbrrjiCps0adJZLwA+fvy4/fWvf7XKlSubJJs8ebJnXUFBgcXHx1uXLl1KtD/eeOMNu+yyy4q0Hz161OrXr1/k/5e33nrLoqKi7MILL7QPP/zQ037s2DGLiIiwlStXlmi7Tlf4d2zYsKFXe+FFsIV30BQq7gLgc91AcPLkSRs4cKBFRERY5cqVbfDgwUXem073wQcfWJcuXaxWrVoWGBhoMTEx9te//tVzp6PZ/+btk08+adWqVbOwsDD7+9//7nVTQkFBgb300kvWoEEDCwgIsBo1atg111zjddH31q1b7S9/+YtVrlzZgoODrWHDhjZo0CDPe0tOTo7ddtttFhISYlFRUTZmzJgSfWne0KFD7W9/+5tXW2k/N77//ntzu91ed/ItXbrUkpKSrEqVKhYcHGwXXXSRzZgxw7O+os9hl1kZnpSGT6SkpGjOnDnlcpjfSbp3764WLVpo2LBhZTbmI488ouzsbE2YMKHMxoTvHD16VDExMZo0aVKx166d7vjx42rQoIGmT59+3hceS9Jrr72muXPnatGiRec9Bn4bffr00cGDBzVnzhxfl1Ksn376SU2aNNHq1asVHx9/XmOMHTtWn376qT7++OMSP6eiz2FOM+F347nnniv27oFfo2bNml5fqAVnKigo0O7du/XEE08oMjKyyJeOnUlQUJDefvttry87Ox8BAQF65ZVXftUYgPTLXUkTJ07Uzp07z3uM2NjYUv+jr6LPYY7M/A5wZAY4u4yMDCUmJio2NlZTpkxRx44dfV0SKqiKfmQGxSPMAAAAR+M0EwAAcDTCDAAAcDTCDAAAcDTCDAAAcDTCDAAAcDTCDAAAcDTCDAAAcDTCDAAAcLT/B0Vafi9r+IqAAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Example weather data (replace these with actual fetched data)\n",
    "temperature = 6.63  # Replace with actual temperature data\n",
    "humidity = 94       # Replace with actual humidity data\n",
    "wind_speed = 5.2    # Replace with actual wind speed data\n",
    "\n",
    "# Labels and values for the bar chart\n",
    "labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']\n",
    "values = [temperature, humidity, wind_speed]\n",
    "\n",
    "# Create the bar chart\n",
    "plt.bar(labels, values)\n",
    "plt.title('Weather Data for London')\n",
    "plt.ylabel('Values')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f0564612-5706-469e-886d-0678381a9326",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HTTP Status Code: 200\n"
     ]
    }
   ],
   "source": [
    "print(f\"HTTP Status Code: {response.status_code}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "b3f54999-e2ee-494e-a27d-83f3d754afdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "API data fetched successfully\n",
      "{'data': {'timelines': [{'timestep': 'current', 'endTime': '2024-12-12T10:28:00Z', 'startTime': '2024-12-12T10:28:00Z', 'intervals': [{'startTime': '2024-12-12T10:28:00Z', 'values': {'humidity': 94, 'precipitationType': 0, 'temperature': 6.63, 'windSpeed': 1.31}}]}]}}\n"
     ]
    }
   ],
   "source": [
    "if response.status_code == 200:\n",
    "    data = response.json()\n",
    "    if not data:\n",
    "        print(\"No data returned from the API.\")\n",
    "    else:\n",
    "        print(\"API data fetched successfully\")\n",
    "        print(data)\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "af47753e-cff9-41e8-936a-8e40ab823023",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HTTP Status Code: 200\n",
      "API data fetched successfully\n",
      "City: London\n",
      "Temperature: 6.81°C\n",
      "Humidity: 94%\n",
      "Precipitation Type: 0\n",
      "Wind Speed: 1.13 m/s\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Your API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "LAT = 51.5074    # Latitude for London (or your preferred location)\n",
    "LON = -0.1278    # Longitude for London (or your preferred location)\n",
    "\n",
    "# API request URL\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity,windSpeed&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP Status Code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    print(\"API data fetched successfully\")\n",
    "    \n",
    "    # Access the values from the API response\n",
    "    timeline_data = data.get('data', {}).get('timelines', [])[0].get('intervals', [])[0].get('values', {})\n",
    "    \n",
    "    if timeline_data:\n",
    "        temperature = timeline_data.get('temperature', 'N/A')\n",
    "        humidity = timeline_data.get('humidity', 'N/A')\n",
    "        precipitation = timeline_data.get('precipitationType', 'N/A')\n",
    "        wind_speed = timeline_data.get('windSpeed', 'N/A')\n",
    "        \n",
    "        print(f\"City: London\")\n",
    "        print(f\"Temperature: {temperature}°C\")\n",
    "        print(f\"Humidity: {humidity}%\")\n",
    "        print(f\"Precipitation Type: {precipitation}\")\n",
    "        print(f\"Wind Speed: {wind_speed} m/s\")\n",
    "    else:\n",
    "        print(\"No weather data available.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2b9579a2-cbc2-4fbd-ba35-45b19dcc5f27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Script started\n",
      "HTTP Status Code: 200\n",
      "API data fetched successfully\n",
      "City: London\n",
      "Temperature: 6.81°C\n",
      "Humidity: 94%\n",
      "Precipitation Type: 0\n",
      "Wind Speed: 1.13 m/s\n",
      "Script completed\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Print at the start of the script to confirm it's running\n",
    "print(\"Script started\")\n",
    "\n",
    "# Your API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "LAT = 51.5074    # Latitude for London (or your preferred location)\n",
    "LON = -0.1278    # Longitude for London (or your preferred location)\n",
    "\n",
    "# API request URL\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity,windSpeed&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP Status Code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check for the content of the response\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    print(\"API data fetched successfully\")\n",
    "    \n",
    "    # Access the values from the API response\n",
    "    timeline_data = data.get('data', {}).get('timelines', [])[0].get('intervals', [])[0].get('values', {})\n",
    "    \n",
    "    if timeline_data:\n",
    "        temperature = timeline_data.get('temperature', 'N/A')\n",
    "        humidity = timeline_data.get('humidity', 'N/A')\n",
    "        precipitation = timeline_data.get('precipitationType', 'N/A')\n",
    "        wind_speed = timeline_data.get('windSpeed', 'N/A')\n",
    "        \n",
    "        print(f\"City: London\")\n",
    "        print(f\"Temperature: {temperature}°C\")\n",
    "        print(f\"Humidity: {humidity}%\")\n",
    "        print(f\"Precipitation Type: {precipitation}\")\n",
    "        print(f\"Wind Speed: {wind_speed} m/s\")\n",
    "    else:\n",
    "        print(\"No weather data available.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n",
    "\n",
    "# Print at the end of the script to confirm completion\n",
    "print(\"Script completed\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "1d0ef7cb-a382-4da7-85cd-b2e47435644d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Script started\n",
      "Making API request to: https://api.tomorrow.io/v4/timelines?location=51.5074,-0.1278&fields=temperature,precipitationType,humidity,windSpeed&timesteps=current&apikey=72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b\n",
      "HTTP Status Code: 200\n",
      "Full API Response:\n",
      "{\"data\":{\"timelines\":[{\"timestep\":\"current\",\"endTime\":\"2024-12-12T11:15:00Z\",\"startTime\":\"2024-12-12T11:15:00Z\",\"intervals\":[{\"startTime\":\"2024-12-12T11:15:00Z\",\"values\":{\"humidity\":94,\"precipitationType\":0,\"temperature\":6.81,\"windSpeed\":1.13}}]}]}}\n",
      "API data fetched successfully\n",
      "API Response Data:\n",
      "{'data': {'timelines': [{'timestep': 'current', 'endTime': '2024-12-12T11:15:00Z', 'startTime': '2024-12-12T11:15:00Z', 'intervals': [{'startTime': '2024-12-12T11:15:00Z', 'values': {'humidity': 94, 'precipitationType': 0, 'temperature': 6.81, 'windSpeed': 1.13}}]}]}}\n",
      "Timeline Data Found:\n",
      "{'humidity': 94, 'precipitationType': 0, 'temperature': 6.81, 'windSpeed': 1.13}\n",
      "City: London\n",
      "Temperature: 6.81°C\n",
      "Humidity: 94%\n",
      "Precipitation Type: 0\n",
      "Wind Speed: 1.13 m/s\n",
      "Script completed\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Print at the start of the script to confirm it's running\n",
    "print(\"Script started\")\n",
    "\n",
    "# Your API key from Tomorrow.io\n",
    "API_KEY = '72Jrf3ZVRv9fXiRSKw7OQSVU4PN7MH5b'\n",
    "LAT = 51.5074    # Latitude for London (or your preferred location)\n",
    "LON = -0.1278    # Longitude for London (or your preferred location)\n",
    "\n",
    "# API request URL\n",
    "URL = f'https://api.tomorrow.io/v4/timelines?location={LAT},{LON}&fields=temperature,precipitationType,humidity,windSpeed&timesteps=current&apikey={API_KEY}'\n",
    "\n",
    "# Send GET request to Tomorrow.io API\n",
    "print(f\"Making API request to: {URL}\")\n",
    "response = requests.get(URL)\n",
    "\n",
    "# Print the HTTP Status Code for debugging\n",
    "print(f\"HTTP Status Code: {response.status_code}\")\n",
    "\n",
    "# Check the full response content\n",
    "print(\"Full API Response:\")\n",
    "print(response.text)  # This will show the raw response from the API\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    data = response.json()  # Parse the JSON response\n",
    "    print(\"API data fetched successfully\")\n",
    "\n",
    "    # Access and print the structure of the response\n",
    "    print(\"API Response Data:\")\n",
    "    print(data)\n",
    "\n",
    "    # Proceed with extracting data if the structure is correct\n",
    "    if 'data' in data and 'timelines' in data['data']:\n",
    "        timelines = data['data']['timelines']\n",
    "        if len(timelines) > 0 and 'intervals' in timelines[0]:\n",
    "            intervals = timelines[0]['intervals']\n",
    "            if len(intervals) > 0 and 'values' in intervals[0]:\n",
    "                timeline_data = intervals[0]['values']\n",
    "                print(\"Timeline Data Found:\")\n",
    "                print(timeline_data)  # Print out the values dictionary\n",
    "                \n",
    "                # Access weather data safely, using None if not available\n",
    "                temperature = timeline_data.get('temperature', 'N/A')\n",
    "                humidity = timeline_data.get('humidity', 'N/A')\n",
    "                precipitation = timeline_data.get('precipitationType', 'N/A')\n",
    "                wind_speed = timeline_data.get('windSpeed', 'N/A')\n",
    "                \n",
    "                # Print the weather data\n",
    "                print(f\"City: London\")\n",
    "                print(f\"Temperature: {temperature}°C\")\n",
    "                print(f\"Humidity: {humidity}%\")\n",
    "                print(f\"Precipitation Type: {precipitation}\")\n",
    "                print(f\"Wind Speed: {wind_speed} m/s\")\n",
    "            else:\n",
    "                print(\"No 'values' data in the response.\")\n",
    "        else:\n",
    "            print(\"No 'intervals' data in the response.\")\n",
    "    else:\n",
    "        print(\"No 'timelines' or 'data' in the response.\")\n",
    "else:\n",
    "    print(\"Failed to retrieve data.\")\n",
    "    print(\"Response:\", response.text)\n",
    "\n",
    "# Print at the end of the script to confirm completion\n",
    "print(\"Script completed\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4501addc-5429-4172-a10f-125cd9f2a8fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Example time (hourly intervals)\n",
    "time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00']\n",
    "\n",
    "# Example temperatures for these times\n",
    "temperatures = [6.5, 6.3, 6.1, 5.9, 5.8, 5.7]\n",
    "\n",
    "# Create a line plot for temperature over time\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.plot(time, temperatures, marker='o', color='b')\n",
    "\n",
    "# Adding title and labels\n",
    "plt.title('Temperature Forecast Over Time')\n",
    "plt.xlabel('Time')\n",
    "plt.ylabel('Temperature (°C)')\n",
    "\n",
    "# Show the plot\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3173071f-80e2-49be-ac69-4fa5498b0f20",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "735137c6-9047-48bb-8582-a4f0d8e16a22",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
