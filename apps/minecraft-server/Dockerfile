FROM openjdk:17-slim-bullseye

LABEL "maintainer" "Roman Czerwinski"

RUN apt-get update && \
    apt-get install wget git -y

RUN mkdir -p /home/minecraft/plugins && \
    groupadd minecraft && \
    useradd -g minecraft minecraft && \
    chown -R minecraft:minecraft /home/minecraft

USER minecraft

WORKDIR /home/minecraft

# This is the vanilla server
# RUN wget https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar \

# This is the high performance spigot server
RUN wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastStableBuild/artifact/target/BuildTools.jar \
    -O /home/minecraft/buildserver.jar && \
    chown minecraft:minecraft /home/minecraft/buildserver.jar && \
    echo '#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).' > /home/minecraft/eula.txt && \
    echo "#$(date)" >> /home/minecraft/eula.txt && \
    echo 'eula=true' >> /home/minecraft/eula.txt

# Feel free to override these
ENV MIN_MEM "3072"
ENV MAX_MEM "3072"
ENV SERVER_VERSION "1.18.2"

# You actually have to build the server before you can run it, this takes a
# very long time so change the SERVER_VERSION variable above with caution
RUN java -jar /home/minecraft/buildserver.jar --rev ${SERVER_VERSION} && \
    mv /home/minecraft/spigot-${SERVER_VERSION}.jar /home/minecraft/server.jar && \
    chown minecraft:minecraft /home/minecraft/server.jar

# This is the Geyser plugin, allowing bedrock server clients to join the java server
RUN wget https://ci.opencollab.dev/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar \
    -O /home/minecraft/plugins/Geyser-Spigot.jar && \
    chown minecraft:minecraft /home/minecraft/plugins/Geyser-Spigot.jar

# This is the Floodgate plugin, allowing bedrock server clients to join the java server
# from Xbox, Playstation, and iOS without complicated login processes
RUN wget https://ci.opencollab.dev/job/GeyserMC/job/Floodgate/job/master/lastSuccessfulBuild/artifact/spigot/target/floodgate-spigot.jar \
    -O /home/minecraft/plugins/floodgate-spigot.jar && \
    chown minecraft:minecraft /home/minecraft/plugins/floodgate-spigot.jar

# Adds the plugin configuration files to the plugin folders
COPY ./plugins/Geyser-Spigot/config.yml /home/minecraft/plugins/Geyser-Spigot/config.yml

ENTRYPOINT [ "sh", "-c", "java -Xmx${MAX_MEM}M -Xms${MIN_MEM}M -XX:+UseG1GC -jar ./server.jar nogui" ]
