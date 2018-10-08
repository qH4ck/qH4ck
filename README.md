# qH4ck
*Useful tools for CTF challanges*

**DISCLAIMER:** these tools are not developed by us. We only collected them in this repository to keep them handy for future CTFs.


### Mixed tools
- [CTF frameworks, libraries, resources, softwares and tutorials](https://github.com/apsdehal/awesome-ctf)
- [Online tools for every challenge](https://gchq.github.io/CyberChef/)


### Guides
- [CTF Field Guide](https://trailofbits.github.io/ctf/)


### Coding
- [hexadoku solver](tools/hexadoku-solver.py) 


### Crypto
- [Frequency analysis](http://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html)
- [Substitution cipher solver](https://quipqiup.com/)
- [Reverse hashes](https://crackstation.net/)
- [Mixed tools](http://rumkin.com/tools/cipher/)
- [Vigsolve.c](http://www.caesum.com/handbook/vigsolve.c)
- [Cripto and encoding tools](http://snarkles.net/scripts/sneak/sneak.php)


### Encoding
- [Base64 decode](https://www.base64decode.net/)
- [Binary 2 UTF-8](https://onlinebinarytools.com/convert-binary-to-utf8)
- [Base64 to binary](https://cryptii.com/pipes/base64-to-binary)


### Password, hash and key cracking
- [John the Ripper](https://www.openwall.com/john/) with a good [word list](http://www.caesum.com/handbook/johnfiles.zip)
- [Hash killer](https://hashkiller.co.uk)
- [featherduster](https://github.com/nccgroup/featherduster): the feathermodules folder contains usefuls python scripts


### Steganograpy

#### Images
- [steganabara](http://www.caesum.com/handbook/steganabara-1.1.1.tar.gz)
- [Stegsolve.jar](http://www.caesum.com/handbook/Stegsolve.jar)
   
#### Audio
- [mp3stego](http://www.petitcolas.net/fabien/software/MP3Stego_1_1_18.zip) (Windows only)

#### Docker container
- Original image: [dominicbreuker/stego-toolkit](https://hub.docker.com/r/dominicbreuker/stego-toolkit/)  
- Modified [Dockerfile](tools/Dockerfile) with SSH
- Copy a folder: `scp -P 2222 -r folder user@host:/data`

## Contribute
Feel free to open issues or to make pull requests.

Do you know some useful tools? Let us know!
