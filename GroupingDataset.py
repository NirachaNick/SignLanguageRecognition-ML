import os
import shutil
import json

def group_videos_by_gloss(json_file, videos_folder, output_folder):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Dictionary to store the video count for each gloss
    video_count_by_gloss = {}

    for entry in data:
        gloss_name = entry['gloss']
        instances = entry['instances']

        # Create a folder for the gloss in the output directory
        gloss_folder = os.path.join(output_folder, gloss_name)
        os.makedirs(gloss_folder, exist_ok=True)

        # Initialize the video count for the current gloss to zero
        video_count_by_gloss[gloss_name] = 0

        # Process each instance for the current gloss
        for instance in instances:
            video_id = instance['video_id']
            video_file_name = f"{video_id}.mp4"
            video_path = os.path.join(videos_folder, video_file_name)

            # Check if the video file exists in the videos folder
            if os.path.exists(video_path):
                # Copy the video to the gloss folder in the output directory
                destination_path = os.path.join(gloss_folder, video_file_name)
                shutil.copy(video_path, destination_path)

                # Increment the video count for the current gloss
                video_count_by_gloss[gloss_name] += 1
            else:
                print(f"Video with video_id '{video_id}' does not exist. Skipping...")

    # Print the video count for each gloss and save it in a text file in the new folder
    count_text_file = os.path.join(output_folder, "video_count_by_gloss.txt")
    with open(count_text_file, "w") as count_file:
        for gloss, count in video_count_by_gloss.items():
            count_file.write(f"Number of videos in folder '{gloss}': {count}\n")

if __name__ == "__main__":
    json_file = "D:\Msc\ProjectResearch\WLASL-2000 Resized\wlasl-complete\WLASL_v0.3.json"
    videos_folder = "D:\Msc\ProjectResearch\WLASL-2000 Resized\wlasl-complete\\videos"
    output_folder = "D:\Msc\ProjectResearch\WLASL-2000 Resized\wlasl-complete\\train_video"
   
    group_videos_by_gloss(json_file, videos_folder, output_folder)
