# Youtube API

I wanted to explore using the YouTube API, so I created a small app that will do so. It runs on Docker and you will need to get an API key from Google in order to use the API itself. My API key is not baked into the image, so fro real, get your own key. This app exclusively grabs the current subscriber count from whichever youtuber that you pass into the `CMD` argument. You can pass them in via their Channel ID or the Username like so:

```bash
# For the channel username
docker run \
    --rm \
    -e GOOGLE_API_KEY=$GOOGLE_API_KEY \
    romanmc72/youtube-subscriber-count:0.0.1 \
    --username MrBeast6000
;
# For the channel id
docker run \
    --rm \
    -e GOOGLE_API_KEY=$GOOGLE_API_KEY \
    romanmc72/youtube-subscriber-count:0.0.1 \
    --id UCY1kMZp36IQSyNx_9h4mpCg
;
```

This will simply grab the subscriber count to as many digits as youtube tracks, spit out the result, and exit successfully. If you want to do something more fancy be my guest but that is really all I cared about doing here.

## Cool, but why?

Some youtubers (cough cough... Mr Beast) allegedly give out large prizes to their N'th subscriber when that N is a multiple of 20 million or so. With this I now have a way to check what the subscriber count is on a daily basis and see how close they are to the threshold, then potentially subscribe at that next big landmark ot win a prize.
