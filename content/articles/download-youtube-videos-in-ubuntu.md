Title: Download Youtube Videos in Ubuntu for FREE!
Date: 2017-2-22 22:21
Modified: 2017-2-22 22:21
Category: tutorial
Tags: tutorial
Cover: images/ubuntu_youtube.png
Slug: download-youtube-videos-in-ubuntu
Summary: There are some free as well as paid online tool for downloading Youtube videos but youtube-dl is free, opensource, geeky and awesome command line tool to download videos from Youtube. 

[youtube-dl] is a command-line program to download videos from YouTube.com and a few more sites like vimeo, 9gag, Dailymotion, [etc](https://rg3.github.io/youtube-dl/supportedsites.html). 

It is purely build in Python and requires the Python interpreter (2.6, 2.7, or 3.2+) to use it and it is not platform specific. There's also a [Windows executable](https://yt-dl.org/latest/youtube-dl.exe) for Windows user. And the most cool thing about youtube-dl is that it's opensource and released to the public domain.

This tutorial illustrates how to install and use it in Ubuntu. But to use this free software you need Python installed in your system.

## Step 1: Install youtube-dl
```bash
$ sudo apt-get install youtube-dl
```
or, install via [PIP](https://girisagar46.github.io/install-python-pip-package-management-system-in-ubuntu)

```bash
$ sudo pip install youtube-dl
```

## Step 2 : Use it for free

Fire up your terminal. And type

`$ youtube-dl [URL for video]`

eg. `$ youtube-dl https://www.youtube.com/watch?v=KWZGAExj-es`

### Choosing the quality:
youtube-dl gives option to download videos of different quality. 
To download videos of high quality, type the commands provided below:

`$ youtube-dl -F https://www.youtube.com/watch?v=KWZGAExj-es`

This command gives the information of the video. 

```bash
linuxsagar@ubuntu:~ $ youtube-dl -F https://www.youtube.com/watch?v=KWZGAExj-es
[youtube] KWZGAExj-es: Downloading webpage
[youtube] KWZGAExj-es: Downloading video info webpage
[youtube] KWZGAExj-es: Extracting video information
[info] Available formats for KWZGAExj-es:
format code  extension  resolution note
249          webm       audio only DASH audio   53k , opus @ 50k, 1.81MiB
250          webm       audio only DASH audio   73k , opus @ 70k, 2.35MiB
140          m4a        audio only DASH audio  128k , m4a_dash container, mp4a.40.2@128k, 4.65MiB
171          webm       audio only DASH audio  137k , vorbis@128k, 4.44MiB
251          webm       audio only DASH audio  174k , opus @160k, 5.84MiB
278          webm       256x144    144p   92k , webm container, vp9, 12fps, video only, 2.60MiB
160          mp4        256x144    144p  111k , avc1.4d400c, 24fps, video only, 3.86MiB
242          webm       426x240    240p  223k , vp9, 24fps, video only, 6.27MiB
133          mp4        426x240    240p  243k , avc1.4d4015, 24fps, video only, 8.57MiB
243          webm       640x360    360p  420k , vp9, 24fps, video only, 11.11MiB
134          mp4        640x360    360p  517k , avc1.4d401e, 24fps, video only, 11.36MiB
244          webm       854x480    480p  715k , vp9, 24fps, video only, 17.63MiB
135          mp4        854x480    480p  970k , avc1.4d401e, 24fps, video only, 21.71MiB
247          webm       1280x720   720p 1499k , vp9, 24fps, video only, 32.43MiB
136          mp4        1280x720   720p 1666k , avc1.4d401f, 24fps, video only, 39.95MiB
248          webm       1920x1080  1080p 2744k , vp9, 24fps, video only, 55.46MiB
137          mp4        1920x1080  1080p 2752k , avc1.640028, 24fps, video only, 71.87MiB
17           3gp        176x144    small , mp4v.20.3, mp4a.40.2@ 24k
36           3gp        320x180    small , mp4v.20.3, mp4a.40.2
43           webm       640x360    medium , vp8.0, vorbis@128k
18           mp4        640x360    medium , avc1.42001E, mp4a.40.2@ 96k
22           mp4        1280x720   hd720 , avc1.64001F, mp4a.40.2@192k (best)

```

Notice the format column in the output above? Yes, that's what you need. Also, remember capital F in the above command (-F) gives the format information.

Now, lets download a 720p mp4 file with format code *136*.

` $ youtube-dl -f 136 https://www.youtube.com/watch?v=KWZGAExj-es `

## You only want the audio of a file? No problem, youtube-dl got your back

`youtube-dl --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=5dKGK81z4js`

That's it. Similarly, you will be able to download videos/ audio from any site using youtube-dl tool from command line interface.


This opensource project has been hosted in GitHub. You can checkout the source code from here: [https://github.com/rg3/youtube-dl](https://github.com/rg3/youtube-dl)


[youtube-dl]: <https://rg3.github.io/youtube-dl/>