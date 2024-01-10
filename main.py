# NVM, this dont work

import sys
import math
import moviepy.config as moviepyconf
import moviepy.editor as e

# moviepyconf.IMAGEMAGICK_BINARY = 'insert binary here'
moviepyconf.IMAGEMAGICK_BINARY = 'C:\\programi\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe'

# Load the original video (.close will be called later)
# In this case, with..as is not needed as its block is the
#   entire program; here it is used for demonstration purposes
# Using with..as releases the file when not needed
#   so that other programs may use it
with e.VideoFileClip('video.mp4') as original:

  # Linting helper
  # Using moviepy editing functions such as subclip and fl_image
  #   blocks linting; i.e., most functions return type Any and not VideoClip.
  def to_vclip(inp) -> e.VideoClip:
    return inp
  
  # Add title to a clip
  def add_text(clip, title) -> e.CompositeVideoClip:
    return e.CompositeVideoClip([
      clip,
      e.TextClip(title, fontsize=50, color='white').set_position('center').set_duration(clip.duration)
    ])

  # Take a subclip in interval 0-5s
  original = to_vclip(original.subclip(0, 5))


  # Increase the R value by factor 10 for every pixel of every frame in edited_video
  red_vid = original.fl_image(lambda frame: frame * [10, 1, 1])

  # Increase the B value by factor 10 for every pixel of every frame in edited_video
  blue_vid = original.fl_image(lambda frame: frame * [1, 1, 10])

  # Apply custom effect
  def change_color_channels(clip):
    # Change R channel with B, G with R and B with G
    return clip.fl_image(lambda frame: frame[..., [2, 0, 1]])

  custom_fx_vid = original.fx(change_color_channels)


  # Apply complex time effects with time filter
  #   Add 1 to sin to avoid negative values
  #   Set duration to avoid infinite loops
  # Resulting video takes first 2 seconds of video and oscillates it in a loop (1x per second)
  time_fx_vid = original                   \
    .fl_time(lambda t: 1 + math.sin(2 * math.pi * t))  \
    .set_duration(original.duration)


  # Add a title to video
  titled_vid = e.CompositeVideoClip([
        original,
        e.TextClip("Hello world!", fontsize=70, color='white')
          .set_position('center')
          .set_duration(3)
      ]
    )

  # Concatenate two videos and speed them up x2
  conc_vid = e.concatenate_videoclips([
    red_vid.copy(),
    blue_vid.copy(),
  ]).fx(e.vfx.speedx, 2)

  # Scroll effect
  def scroll_filter(get_frame, t):
    frame = get_frame(t)
    # as time progresses, scroll down and up
    frame_region = frame[int(t * 25):int(5 * 25) + 150, :]
    return frame_region
  
  scrolling_vid = original.fl(scroll_filter)


  # Clip composition using clips_array
  cliparr_marg = original.margin(10)
  cliparr_hor_flip = cliparr_marg.fx(e.vfx.mirror_x)
  cliparr_hor_flip = cliparr_hor_flip.set_start(1)  # Delay start of second clip by 1 second
  cliparr_vert_flip = cliparr_marg.fx(e.vfx.mirror_y)
  cliparr_resized = cliparr_marg.resize(0.6)
  cliparr_test = e.clips_array([[cliparr_marg, cliparr_hor_flip], [cliparr_vert_flip, cliparr_resized]])
  # Resize to original dimensions
  cliparr_test = cliparr_test   \
    .resize(width=original.w, height=original.h)

  # Clip composition using CompositeVideoClips
  cvclip_marg = original.margin(10)
  cvclip_hor_flip = cvclip_marg.fx(e.vfx.mirror_x
    ).fl_image(
      # Increase red by factor of 10
      lambda frame: frame * [10, 1, 1]
    ).resize(
      # Downsize by 20%
      0.8
    )
  cvclip_resized = cvclip_marg.resize(0.6)
  cvclip_test = e.CompositeVideoClip([
    cvclip_marg,  # cvclip_test takes cvclip_marg's height and width (first clip is usually bg)
    cvclip_resized.set_position(('center', 'bottom')),  # Set position to bot center
    cvclip_hor_flip.crossfadein(0.5).set_start(2.1),  # Fade in and delay start
    cvclip_resized.set_start(2.1).set_position(
      (150, cvclip_marg.h - cvclip_resized.h // 2)
    ),  # Set (x,y) position in pixels (intentionally clipped height by 50%)
  ])
  cvclip_time_factor = cvclip_test.duration / original.duration
  cvclip_test = cvclip_test                     \
    .fl_time(lambda t: t * cvclip_time_factor)  \
    .set_duration(original.duration)            \
    .resize(width=original.w, height=original.h)

  # For performance reasons, not all clips are set inside clips_array
  # To play original clips, call .preview on it and comment out other clips
  clips_array = e.clips_array([
    [
      add_text(original, 'original'),
      add_text(red_vid, 'Increase red x10'),
      add_text(custom_fx_vid, 'RGB => BRG'),
      add_text(time_fx_vid, 'Looping'),
    ],
    [
      titled_vid,
      add_text(conc_vid, 'Concatenate'),
      add_text(scrolling_vid, 'Scroll'),
      add_text(cvclip_test, 'Video composition'),
    ]
  ])

  # To save output, send write_audiofile argument
  # e.g. start the script with "python3 main.py --write_audiofile=true"
  write_af_flag = len([
    arg for arg in sys.argv
    if arg.lower() == '--write_audiofile=true'
  ]) > 0

  if write_af_flag:
    clips_array.write_videofile('output.mp4')
  else:
    scrolling_vid.preview()
