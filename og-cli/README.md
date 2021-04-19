# OG CLI

Simple commandline utility that shows the Open Graph tags given a url.

e.g.

```sh
python main.py audit https://blog.sethcorker.com/importance-of-the-readme/
```

outputs the following:

```sh
Open Graph Properties

* og:url         = https://blog.sethcorker.com/importance-of-the-readme/
* og:type        = article
* og:title       = The importance of the README | What I look for in a library
* og:description = There’s a library for everything and usually lot’s of alternatives but, how do you pick which one is right for your project?
* og:image       = https://og-image-bb.sethcorker.vercel.app/The%20importance%20of%20the%20README.png?theme=light&kicker=What%20makes%20good%20documentation%3F&subtitle=What%20I%20look%20for%20in%20a%20library&fontSize=150px&mainImage=https%3A%2F%2Fblog.sethcorker.com%2Fprofile-picture.jpeg&mainImageWidth=350&mainImageHeight=350&footerImage=https%3A%2F%2Fblog.sethcorker.com%2Fheader-image.png&footerImageWidth=auto&footerImageHeight=50
* og:image       = Illustration of the GitHub logo and NPM logo on either side of a person holding a file
* og:image       = 2048
* og:image       = 1170
* og:site_name   = Benevolent Bytes
```