from pathlib import Path
# EX: parent_path = /home/khoa/PycharmProjects/667
current_path = Path(__file__).resolve().parents[0]
parent_path = Path(__file__).resolve().parents[1]

# NOTE: make sure to convert each Path() to string

# High score
high_score_path = str(current_path / "high_score.txt")

# Icon
icon_path = str(parent_path / "resources/icons/robot.png")

# Player sprite sheet paths
# Idle sprite is 32x28, 8 sprites
player_idle_path = str(parent_path / "resources/sprites/player/idle_sheet.png")
# Walk sprite is 32x32, 8 sprites
player_walk_path = str(parent_path / "resources/sprites/player/walk_sheet.png")
# Jump sprite is 28x28, 6 sprites
player_jump_path = str(parent_path / "resources/sprites/player/jump_sheet.png")