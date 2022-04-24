# Minecraft Server

Because you "can" doesn't always mean you should, but fuck it I'm gonna do it anyways. I am adding my minecraft server to my kubernetes cluster and you cannot stop me. This directory will contain the Dockerfile and any other necessary pieces for building the image itself.

This server runs for both Java and Bedrock servers, but it is primarily a Java Spigot server. It uses the Geyser plugin to allow bedrock connections.

## Running This

If you want to just run it, you will want to have somewhere on disk to store the server's data if you wish to have your server's worlds persist across restarts. If you have decided that already then we will assume you have it stored as an env var and have named it `$MINECRAFT_SERVER_DATA`. Replace the instance of that with your local server data location below if you want, or just set the env var to that value and copy-paste your heart out. I don't care either way.

```bash
# Starts a minecraft server in the background, saving the world to your local
# directory at whatever $MINECRAFT_SERVER_DATA is set to. This server has min
# and max memory set to 1024 MB or 1 GB, you can adjust it up and down if you
# like. If you leave out those env vars it defaults to 3072 MB or 3 GB. Use
# whatever is appropriate for your host machine type.
docker run \
    --rm \
    -d \
    -e MIN_MEM=1024 \
    -e MAX_MEM=1024 \
    -p 25565:25565 \
    -p 19132:19132/udp \
    -v $MINECRAFT_SERVER_DATA/world:/home/minecraft/world \
    -v $MINECRAFT_SERVER_DATA/world_nether:/home/minecraft/world_nether \
    -v $MINECRAFT_SERVER_DATA/world_the_end:/home/minecraft/world_the_end \
    romanmc72/minecraft-server:latest
```

and that ought to just work. "OUGHT TO" lol. Your mileage may vary it works for me though, if you don't like this then make your own image :fu:.
