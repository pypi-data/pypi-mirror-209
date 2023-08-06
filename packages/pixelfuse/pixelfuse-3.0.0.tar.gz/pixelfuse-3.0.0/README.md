# 📄🔄🎞️ PixelFuse

Convert any file to video and video to file.

**WARNING: videos created from files are very fragile. But if you create videos with the `--lessf` flag, the videos are not so fragile anymore**

## 💿 Installation

* Set up using `pip`:
```bash
pip install pixelfuse
```
* Install from `Git`:
```bash
pip install git+https://github.com/TheTS-labs/PixelFuse.git
```

## 🎬 Usage

### Convert file to video(`fileToVideo`)

To convert a file into a video just write the following command:
```bash
python -m pixelfuse fileToVideo "test/example.text.txt"
```

Where ["test/example.text.txt"](./test/example.text.txt) the file you want to convert to video

As output you get the file `output.avi` - video 640x480, 1.0 FPS, codec HFYU [like this](https://drive.google.com/file/d/1OTZ9rF-6SI73BiLEwY4gJeJ2RVddLsfn/edit)

As for the parameters:
* `path: Path` - mandatory, the path to the file you want to convert
* `fps: float` - frame rate, default is `1.0`
* `width: int` - Video length, default is `480px`
* `height: int` - Video height, `640px` by default
* `fourcc: str` - Codec, a string of 4 characters, **WARNING: Use lossless codecs ONLY(except for the `--lessf` flag)**, default is "`HFYU`".
* `output: Path` - Path to output file, default is "`output.avi`", **note you need to use file extension compatible with codec, for example if you use `HFYU` codec you can NOT specify `output` as `output.mp4`**
* `verbose: int` - Output level, from 0 to 3, default is 2
* `lessf: bool` - Changes the way the video is recorded so that the video becomes less fragile, with this flag you can use lossy compression, default is `False`

### 🆕 Convert files to video(`filesToVideo`)

To convert a file into a video just write the following command:
```bash
python -m pixelfuse filesToVideo "test/example.text.txt" "test/example.image.jpg"
```

Where ["test/example.text.txt"](./test/example.text.txt) and ["test/example.image.jpg"](./test/example.image.jpg) the files you want to convert to video

This command will create a tar.gz archive which will later convert to a video, and delete the archive

This command will also create a hash map in which it will write the hash of **each** file. Then `convertToFile` unpacks all files and checks them according to this map

As output you get the file `output.avi` - video 640x480, 1.0 FPS, codec HFYU [like this](https://drive.google.com/file/d/1OTZ9rF-6SI73BiLEwY4gJeJ2RVddLsfn/edit)

As for the parameters:
* `paths: list[Path]` - mandatory, the paths to the files you want to convert
* `fps: float` - frame rate, default is `1.0`
* `width: int` - Video length, default is `480px`
* `height: int` - Video height, `640px` by default
* `fourcc: str` - Codec, a string of 4 characters, **WARNING: Use lossless codecs ONLY(except for the `--lessf` flag)**, default is "`HFYU`".
* `output: Path` - Path to output file, default is "`output.avi`", **note you need to use file extension compatible with codec, for example if you use `HFYU` codec you can NOT specify `output` as `output.mp4`**
* `verbose: int` - Output level, from 0 to 3, default is 2
* `lessf: bool` - Changes the way the video is recorded so that the video becomes less fragile, with this flag you can use lossy compression, default is `False`

### Convert video to file(`videoToFile`)

To get your file(s) back now you need to use this command:
```bash
python -m pixelfuse videoToFile "test/example.video.avi"
```

Where ["test/example.video.avi"](./test/example.video.avi) is the video you want to convert into file(s)

As output, you will get the file with the name it was converted into a video. For example, if you converted the file "example.image.jpg", when you convert the video back to a file you get a file named example.image.jpg

Or a folder with files, if you converted several files. By default, the folder name is the name of the video file without path or extension, but you can specify something else with the `extractDir` parameter

Regarding the parameters:
* `path: Path` - Mandatory, the path to the video you want to convert back to a file
* `verbose: int` - Output level, from 0 to 2, default is 2
* `extractDir: str` - Path to extract archive files
* `lessf: bool` - If the video was encoded with this flag, you need to use it. Otherwise the decoding will end with an error

## ⚠️ Warning

Because of the way this converter works, the video output is **very, very** fragile, **about the `--lessf` flag below**.

In order for you to convert the file back, every pixel **MUST remain unchanged**, here is what you should avoid:
* Use ONLY lossless codecs, as all other codecs corrupt the pixels. For example, FFMPEG `FFV1`, Huffman `HFYU`, Lagarith `LAGS` etc.
* Do not convert videos to other formats, as this is likely to corrupt the pixels.
* Remember that if you upload a video to YouTube, it will re-encode the video (and, guess what, damage the pixels), so if you want to download videos from YouTube, you need to use [Google Takeout](https://takeout.google.com/)
* Don't trim the video, it will cut off some of the information and therefore the converted file.
* Do not apply filters to the video, for example. Anything that can change pixels will damage the file and you won't be able to decode it.
* Never convert zip archives, for some unknown reason the decoder (or encoder) cannot process these archives correctly. If you want to convert multiple files, it is better to use `filesToVideo` command.

### About `--lessf` flag
If you use this flag, the file will be encoded differently (using black and white squiggles), so you can compress videos with lossy codecs and post them on YouTube and download them without Google Takeout. It is also better not to apply filters, but for that matter **maybe** the file can still be decoded, but it is better not to do it. Otherwise, the restrictions for the --lessf flag are the same as for the normal encoding method