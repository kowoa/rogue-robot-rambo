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
# Walk sprite is 32x32, 8 frames
player_walk_path = str(parent_path / "resources/sprites/player/walk_sheet.png")
# Jump sprite is 28x28, 6 frames
player_jump_path = str(parent_path / "resources/sprites/player/jump_sheet.png")
# Jump fx sprite is 28x28, 6 frames
player_jump_fx_path = str(parent_path / "resources/sprites/player/jump_fx_sheet.png")
# Death sprite is 52x28, 11 frames
player_death_path = str(parent_path / "resources/sprites/player/death_sheet.png")
# Fall sprite is 32x28, 2 frames
player_fall_path = str(parent_path / "resources/sprites/player/fall_sheet.png")
# Hurt sprite is 32x28, 9 frames
player_hurt_path = str(parent_path / "resources/sprites/player/hurt_sheet.png")
# Land dust sprite is 44x32, 4 frames
player_land_dust_path = str(parent_path / "resources/sprites/player/land_dust_sheet.png")
# Land fx sprite is 44x32, 4 frames
player_land_fx_path = str(parent_path / "resources/sprites/player/land_fx_sheet.png")
# Land no dust sprite is 44x32, 4 frames
player_land_no_dust_path = str(parent_path / "resources/sprites/player/land_no_dust_sheet.png")