# NVM, this dont work

import moviepy.config as moviepyconf
import moviepy.editor as e

# moviepyconf.IMAGEMAGICK_BINARY = 'insert binary here'
moviepyconf.IMAGEMAGICK_BINARY = 'C:\\programi\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe'

# Load the original video
original = e.VideoFileClip('video.mp4')

# Don't make it too long
def __f__(inp) -> e.VideoClip:
  return inp
original = __f__(original.subclip(0, 2))

def preview_multiple_clips(clips_arr, rows, cols, height):
  video_grid = [[] for _ in range(rows)]

  for idx, clip in enumerate(clips_arr):
    clip_row = idx // cols
    clip_col = idx % cols
    if clip_row < rows and clip_col < cols:
      clip = clip.copy().resize(height=height//rows)
      video_grid[clip_row - 1].append(clip)

  video_grid.reverse()
  combined_video = e.clips_array(video_grid)

  max_w = 160
  max_h = 120
  if combined_video.w > max_w:
    combined_video = combined_video.resize(width=max_w)
  if combined_video.h > max_h:
    combined_video = combined_video.resize(height=max_h)

  # combined_video.preview()
  combined_video.write_videofile('output.mp4')


# # Increase the R value by factor 10 for every pixel of every frame in edited_video
# red_vid = original.copy().fl_image(lambda frame: frame * [10, 1, 1])

# # Increase the G value by factor 10 for every pixel of every frame in edited_video
# green_vid = original.copy().fl_image(lambda frame: frame * [1, 10, 1])

# # Increase the B value by factor 10 for every pixel of every frame in edited_video
# blue_vid = original.copy().fl_image(lambda frame: frame * [1, 1, 10])

# # Add a title to video
# titled_vid = e.CompositeVideoClip([
#       original,
#       e.TextClip("Hello world!", fontsize=70, color='white')
#         .set_position('center')
#         .set_duration(3)
#     ]
#   )

# # Concatenate two videos and speed them up x2
# conc_vid = e.concatenate_videoclips([
#   red_vid.copy(),
#   blue_vid.copy(),
# ]).fx(e.vfx.speedx, 2)

# # Clip composition using clips_array
# cliparr_marg = original.margin(10)
# cliparr_hor_flip = cliparr_marg.fx(e.vfx.mirror_x)
# cliparr_hor_flip = cliparr_hor_flip.set_start(1)  # Delay start of second clip by 1 second
# cliparr_vert_flip = cliparr_marg.fx(e.vfx.mirror_y)
# cliparr_resized = cliparr_marg.resize(0.6)
# cliparr_test = e.clips_array([[cliparr_marg, cliparr_hor_flip], [cliparr_vert_flip, cliparr_resized]])
# # Resize to original dimensions
# cliparr_test = cliparr_test.resize(width=original.w, height=original.h)

# # Clip composition using CompositeVideoClips
# cvclip_marg = original.margin(10)
# cvclip_hor_flip = cvclip_marg.fx(e.vfx.mirror_x
#   ).fl_image(
#     # Increase red by factor of 10
#     lambda frame: frame * [10, 1, 1]
#   ).resize(
#     # Downsize by 20%
#     0.8
#   )
# cvclip_resized = cvclip_marg.resize(0.6)
# cvclip_test = e.CompositeVideoClip([
#   cvclip_marg,  # cvclip_test takes cvclip_marg's height and width (first clip is usually bg)
#   cvclip_resized.set_position(('center', 'bottom')),  # Set position to bot center
#   cvclip_hor_flip.crossfadein(0.5).set_start(2.1),  # Fade in and delay start
#   cvclip_resized.set_start(2.1).set_position(
#     (150, cvclip_marg.h - cvclip_resized.h // 2)
#   ),  # Set (x,y) position in pixels (intentionally clipped height by 50%)
# ])


# # For performance reasons, not all clips are set inside clips_array
# # To play original clips, call .preview on it and comment out other clips
# clips_array = [
#   original,
#   red_vid,
#   green_vid,
#   blue_vid,
#   titled_vid,
#   conc_vid,
# ]

# False and preview_multiple_clips(
#   clips_array,
#   rows=2,
#   cols=3,
#   height = 480,
# )
