from discord import Intents
import discord
import requests

# Configura tu token de bot de Discord
TOKEN = 'TOKEN'

# Configura tu ID de usuario de Discord para que solo tú puedas ejecutar el comando
tu_id_de_usuario = 'ID'

# Comando para obtener la dirección IP pública
COMANDO = '!ip'

# URL del servicio para obtener la dirección IP pública
IP_SERVICE_URL = 'https://api4.ipify.org?format=json'


# Función para obtener la dirección IP pública
def obtener_direccion_ip():
    try:
        response = requests.get(IP_SERVICE_URL)
        if response.status_code == 200:
            ip = response.json()['ip']
            return ip
        else:
            return 'No se pudo obtener la dirección IP pública'
    except Exception as e:
        return f'Error: {str(e)}'


# Inicialización del cliente de Discord
intents = Intents.default()
client = discord.Client(intents=intents)


# Evento para la conexión del bot a Discord
@client.event
async def on_ready():
    print(f'Conectado como {client.user}')


# Evento para manejar los mensajes
@client.event
async def on_message(message):
    # Verificar si el mensaje proviene del usuario correcto y comienza con el comando
    if str(message.author.id) == tu_id_de_usuario and message.content.startswith(COMANDO):
        # Obtener la dirección IP pública
        ip = obtener_direccion_ip()
        
        # Enviar la dirección IP pública al canal donde se solicitó el comando
        await message.channel.send(ip)


# Iniciar el bot
client.run(TOKEN)
