from ultralytics import YOLO

# Load a model
model = YOLO(model='yolo/files/yolov8n.pt')  

# Train the model
results = model.train(data='data.yaml', epochs=100, imgsz=704, device='mps')

print