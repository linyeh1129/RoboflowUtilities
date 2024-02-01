from ultralytics import YOLO

# Load a model
model = YOLO(model='last.pt')  # build from YAML and transfer weights

# Train the model
results = model.predict(source='z.jpg', show=True)

print