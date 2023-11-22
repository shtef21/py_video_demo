
## Installation
Method with pip: if you have pip installed, just type this in a terminal (it will install ez_setup if you don’t already have it)


```pip install moviepy```

If you have neither setuptools nor ez_setup installed the command above will fail.

### Dependencies

MoviePy depends on the Python modules **Numpy**, **imageio**, **Decorator**, and **tqdm**, which will be automatically installed during MoviePy’s installation.

MoviePy depends on the software **FFMPEG** for video reading and writing.
You don’t need to worry about that, as FFMPEG should be automatically downloaded/installed by ImageIO during your first use of MoviePy.
If you want to use a specific version of FFMPEG, you can set the **FFMPEG_BINARY** environment variable.

### Other optional but useful dependencies

**ImageMagick** is not strictly required, only if you want to write texts. It can also be used as a backend for GIFs but you can do GIFs with MoviePy without ImageMagick.

Once you have installed it, ImageMagick will be automatically detected by MoviePy, **except on Windows** !.
Windows user, before installing MoviePy by hand, go into the **moviepy/config_defaults.py** file and provide the path to the ImageMagick binary called magick. It should look like this

```IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"```
You can also set the IMAGEMAGICK_BINARY environment variable See moviepy/config_defaults.py for details.

**PyGame** is needed for video and sound previews (useless if you intend to work with MoviePy on a server but really essential for advanced video editing by hand).

For advanced image processing you will need one or several of these packages.
For instance, using the method **clip.resize** requires that at least one of **Scipy, PIL, Pillow or OpenCV** are installed.

Download links:
- The Python Imaging Library (PIL) or, better, its branch Pillow: https://pillow.readthedocs.org/en/latest/
- Scipy (for tracking, segmenting, etc.), and can be used for resizing video clips if PIL and OpenCV aren’t installed on your computer: https://www.scipy.org/
- Scikit Image may be needed for some advanced image manipulation: http://scikit-image.org/download.html
- OpenCV 2.4.6 or more recent (provides the package cv2) or more recent may be needed for some advanced image manipulation: https://sourceforge.net/projects/opencvlibrary/files/

If you are on linux, these packages will likely be in your repos.
