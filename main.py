from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # build a new model from scratch

# Use the model
results = model.train(data="configuration/config.yaml", epochs=3)  # train the model
