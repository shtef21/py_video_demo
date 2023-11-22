import moviepy.editor as editor

# Load the original video
video = editor.VideoFileClip('video.mp4')

# Copy the original video to create edited_video
edited_video = video.copy()

# Change the R value to 10 for every pixel of every frame in edited_video
edited_video = edited_video.fl_image(lambda frame: frame * [10, 1, 1])

# Double the width of the videos
combined_video = editor.clips_array([[video, edited_video]])

# Set the duration of the combined video to the maximum duration of the input videos
combined_video = combined_video.set_duration(max(video.duration, edited_video.duration))

# Preview the combined video
combined_video.preview()
