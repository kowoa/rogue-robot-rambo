from pathlib import Path
# EX: parent_path = /home/khoa/PycharmProjects/667
current_path = Path(__file__).resolve().parents[0]
parent_path = Path(__file__).resolve().parents[1]

# NOTE: make sure to convert each Path() to string

# High score
high_score_path = str(current_path / "high_score.txt")

# Images
icon_path = str(parent_path / "resources/icons/robot.png")

