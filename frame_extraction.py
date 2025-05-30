import os
import cv2

dataset_path = r"C:\Users\visw\OneDrive\Desktop\project\DAiSEE\DataSet"  
output_path = r"C:\Users\visw\OneDrive\Desktop\project\extract_frames"

os.makedirs(output_path, exist_ok=True)

def extract_limited_frames(video_path, output_folder, num_frames=3):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return 0

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
    frame_interval = max(total_frames // num_frames, 1)  

    extracted_count = 0
    frame_count = 0
    success, frame = cap.read()

    while success and extracted_count < num_frames:
        if frame_count % frame_interval == 0:  
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            extracted_count += 1
        
        success, frame = cap.read()
        frame_count += 1

    cap.release()
    return extracted_count  

total_extracted = 0 

for split in ["Train", "Test", "Validation"]:
    split_path = os.path.join(dataset_path, split)
    
    if not os.path.exists(split_path):
        print(f"Error: The path '{split_path}' does not exist. Skipping {split}.")
        continue

    for person in os.listdir(split_path):
        person_path = os.path.join(split_path, person)
        
        if os.path.isdir(person_path):
            for video_folder in os.listdir(person_path):
                video_path = os.path.join(person_path, video_folder)
                
                if os.path.isdir(video_path):
                    for file in os.listdir(video_path):
                        if file.endswith((".mp4", ".avi")):
                            video_file_path = os.path.join(video_path, file)
                            
                            relative_path = os.path.relpath(video_path, dataset_path)
                            output_folder = os.path.join(output_path, relative_path)
                            os.makedirs(output_folder, exist_ok=True)

                            print(f"Extracting limited frames from {video_file_path} to {output_folder}")
                            frames_extracted = extract_limited_frames(video_file_path, output_folder, num_frames=3)
                            print(f"Extracted {frames_extracted} frames from {file}\n")
                            total_extracted += frames_extracted

print(f"✅ Total frames extracted: {total_extracted}")