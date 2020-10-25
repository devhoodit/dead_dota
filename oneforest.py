import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
import re



client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
      print("on")

@client.command()
async def ping(ctx):
      await ctx.send('Pong!\n:ping_pong: {}ms'.format(round(client.latency * 1000)))

@client.command()
async def dota(ctx):
      schedule = requests.get('https://oneforest.net/schedule')
      schedule_html = schedule.text
      
      soup = BeautifulSoup(schedule_html, 'html.parser')
      scr = soup.select('tr > td > a')
      #body > main > div > div.absc.list.rs > table > tbody > tr:nth-child(5) > td.title > a
      print('start')
      
      date = []
      date_url = []
      
      for html in scr:
            regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
            match_obj = regex.search(str(html))
            if match_obj != None:
                  date.append(match_obj.group())
                  date_url.append(html.get('href'))
                  
#booldy > main > div > div.absc.article > div.article-content > article > div > p:nth-child(1)
      data = requests.get('https://oneforest.net' + date_url[0])
      data_html = data.text
      soup = BeautifulSoup(data_html, 'html.parser')
      scr = soup.select('div.article-content > article > div > p')
      
      body = []
      
      for html in scr:
            regex = re.compile(r'>.*?<')
            match_obj = regex.findall(str(html))
            if match_obj != None:
                  if match_obj[0] != '>\xa0<':
                        body.append(match_obj)
      string = []
      for index in body:
            for detail in index:
                  if detail != '><':
                        string.append(detail.strip('><'))

      final = ''
      for index in string:
            final = final + index + '\n'

      embed = discord.Embed(
                        titile = 'SCHEDULE',
                        description = date[0],
                        colour = discord.Colour.blue()
                        )
      embed.add_field(name='schedule', value=final, inline=True)
      await ctx.send(embed=embed)
      


client.run('YOUR TOEKN')
