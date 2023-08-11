# Monero Mining in Docker!

This folder contains everything you need to start up and launch a [Monero](https://www.getmonero.org/) cryptocurrency mining rig. Why do this? Monero is designed so that it does not require special hardware in order to actually mine the coin, so instead of investing in a GPU heavy workhorse of a mining rig, you can connect a fleet of computers together in docker or kubernetes to run a swarm of miners in parallel (at least that is the plan right now).

## Running the setup

There are 2 parts to the mining process here, the [miner](https://github.com/Romanmc72/My_Dockerfiles/tree/main/mining/monero/miner) and the [daemon](https://github.com/Romanmc72/My_Dockerfiles/tree/main/mining/monero/daemon). The daemon container will download the entire blockchain to volume mounted storage and expose its p2p and rpc ports. The miner will connect to the daemon on those ports and begin mining once the entire blockchain has been downloaded to the daemon. You can spin up as many miners as you want for the daemon.

### Initial Run

Downloading the entire blockchain can take upwards of 10 hours as of writing this. You can speed it up by pruning the blockchain (just getting a portion of it), but this decreases the exposure you will have to obtain rewards from mining. You can also speed it up by downloading the `blockchain.raw` file and running the import command. The daemon is set up to attempt to import the `blockchain.raw` and if it cannot for whatever reason (doesn't exist or is corrupt/in the wrong place) then it will just sync the blockchain the usual way. Find how to do all of this in the [monero documentation online](https://www.getmonero.org/get-started/mining/).

### Getting paid

You should note that my monero address is in the miner's `config.json`, so if you just run this setup as is, waiting 10 hours to download the blockchain and start mining, you will be paying me if you do not change the wallet address in the config file (or override the usage of the config by passing in the CLI args). To be fair, I am totally fine with you paying me. No issue with it at all, however I anticipate that you will want to reap your own rewards for your own efforts. Totally get it. Just, if this does make you some money please donate something to cover my costs for developing this stuff.

My monero address is:

`43KfaYWpJTGWJLxsyv7gT2ASuP7JSbpYwM3bLhBADRGjJpb6iKSpdmBQdqEsGbUzjEAFuFBeu2L8qVCLVnJ5fpWtUxUwKTg`

Thank you if you decide to donate!

## Did you write the mining software?

LOL no. I downloaded and built it from source. You can find the source code here:

- [monerod (daemon)](https://github.com/monero-project/monero)
    - [Dockerfile](https://github.com/Romanmc72/My_Dockerfiles/tree/main/mining/monero/daemon)
- [xmrig (miner)](https://github.com/xmrig/xmrig)
    - [Dockerfile](https://github.com/Romanmc72/My_Dockerfiles/tree/main/mining/monero/miner)

## Disclaimer

This software "works" for me. If it does not work for you you *can* let me know, but I have no guarantee that I will get back to you or fix your issue. If it doesn't work for you, feel free to write your own solution. I take no responsibility for how you use this software or any damages or repercussions it may cause, intended or otherwise. Do what you want, live your life, leave me alone.
