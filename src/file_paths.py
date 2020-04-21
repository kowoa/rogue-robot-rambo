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
# Idle sprite is 32x28, 8 frames
player_idle_path = str(parent_path / "resources/sprites/player/idle_sheet.png")
# Walk sprite is 32x32, 8 framees
player_walk_path = str(parent_path / "resources/sprites/player/walk_sheet.png")
# Jump sprite is 28x28, 6 frames
player_jump_path = str(parent_path / "resources/sprites/player/jump_sheet.png")
# Jump fx sprite is 28x28, 6 frames
'''player_jump_fx_path =
# Death sprite is 52x28, 11 frames
player_death_path =
# Fall sprite is 32x28, 2 frames
player_fall_path =
# Hurt sprite is 32x28, 9 frames
player_hurt_path =
# Land dust sprite is 44x32, 4 frames
player_land_dust_path =
# Land fx sprite is 44x32, 4 frames
player_land_fx_path =
# Land no dust sprite is 44x32, 4 frames
player_land_no_dust_path ='''