# YTDL Machine
Scripts to automate the downloading of all of the Youtube videos linked to from a page, using Youtube-DL.

# Use
Pass the dlpage script a command line argument, which is the url of the page to get video links from.
It should open up Firefox and open the page, this is so it can be sure it has scrolled all the way to the bottom of the page.
It will then generate a file called "links".
Run dlv3 in the same directory as the links file, and it should download all of the Youtube videos on the page.
It currently will download multiple videos at the same time.
The default is a maximum of 20 videos being downloaded at the same time.
if a natural number (positive integer) is passed as an argument to dlv3, it will use that as the maximum number.
You can also make your own links file manually.
Just name it "links" and put one link on each line.

# Notes and Bugs
I only currently have support for Youtube videos, and I know that youtube-dl can download videos from other sites too.
There are not currently any addons for the webdriver's Firefox that the script adds, but I may add this in the future.
Sometimes the videos fail to merge the audio and the video.
This should technically be fixable with a video editor like [kdenlive](https://kdenlive.org/en/).
I intend to help fix these issues in the future.
This script is known to work on Linux Mint, and will almost certainly work properly on other distributions of GNU/Linux.

# Dependencies
## dlpage:
[Firefox](https://www.mozilla.org/en-US/firefox/new/) needs to be installed in PATH.
Additionally, the following Python libraries are necessary to be installed: [selenium](https://pypi.org/project/selenium/), [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/).
The geckodriver binary provided must be in the same directory as the dlpage script when it is run.
It may be outdated, so you can get another one from [here](https://github.com/mozilla/geckodriver/releases) if you want.
## dlv3:
[Youtube-DL](https://yt-dl.org/) needs to be installed in PATH.
