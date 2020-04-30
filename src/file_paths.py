from pathlib import Path
# EX: parent_path = /home/khoa/PycharmProjects/667
current_path = Path(__file__).resolve().parents[0]
parent_path = Path(__file__).resolve().parents[1]

# NOTE: make sure to convert each Path() to string

# High score
high_score_path = str(current_path / "high_score.txt")

# Icon
icon_path = str(parent_path / "resources/icons/gun.png")

# Start Menu Image Header
header_path = str(parent_path / "resources/extra/startmenu.gif")

# Our Pics
adrienne_path = str(parent_path / "resources/extra/adriennepic.jpeg")

# Player sprite sheet paths
p = parent_path / "resources/sprites/player"
# Idle sprite is 32x28, 8 frames
player_idle_path = str(p / "idle_sheet.png")
# Walk sprite is 32x32, 8 frames
player_walk_path = str(p / "walk_sheet.png")
# Jump sprite is 28x28, 6 frames
player_jump_path = str(p / "jump_sheet.png")
# Jump fx sprite is 28x28, 6 frames
player_jump_fx_path = str(p / "jump_fx_sheet.png")
# Death sprite is 52x28, 11 frames
player_death_path = str(p / "death_sheet.png")
# Fall sprite is 32x28, 2 frames
player_fall_path = str(p / "fall_sheet.png")
# Hurt sprite is 32x28, 9 frames
player_hurt_path = str(p / "hurt_sheet.png")
# Land dust sprite is 44x32, 4 frames
player_land_dust_path = str(p / "land_dust_sheet.png")
# Land fx sprite is 44x32, 4 frames
player_land_fx_path = str(p / "land_fx_sheet.png")
# Land no dust sprite is 44x32, 4 frames
player_land_no_dust_path = str(p / "land_no_dust_sheet.png")

# Backgrounds
# Glacial Mountains (384x216)
p = parent_path / "resources/backgrounds/glacial_mountains/Layers"
# sky < glacial_mountains < clouds_bg = clouds_lonely < clouds_mg_3 < clouds_mg_2 < clouds_mg_1
glacial_sky_path = str(p / "sky.png")
glacial_mountains_path = str(p / "glacial_mountains.png")
glacial_clouds_bg_path = str(p / "clouds_bg.png")
glacial_clouds_lonely_path = str(p / "cloud_lonely.png")
glacial_clouds_mg_3_path = str(p / "clouds_mg_3.png")
glacial_clouds_mg_2_path = str(p / "clouds_mg_2.png")
glacial_clouds_mg_1_path = str(p / "clouds_mg_1.png")

# Grassy Mountains (384x216)
p = parent_path / "resources/backgrounds/grassy_mountains/layers_fullcolor"
# sky < far_mountains < grassy_mountains < clouds_mid < hill < clouds_front
grassy_sky_path = str(p / "sky_fc.png")
grassy_far_mountains_path = str(p / "far_mountains_fc.png")
grassy_mountains_path = str(p / "grassy_mountains_fc.png")
grassy_clouds_mid_path = str(p / "clouds_mid_fc.png")
grassy_hill_path = str(p / "hill.png")
grassy_clouds_front_path = str(p / "clouds_front_fc.png")

# Sounds
# Blazer Rail
blazer_rail_path = str(parent_path / "resources/music/Blazer Rail.wav")
# Jump
jump_sound_path = str(parent_path / "resources/sound_fx/Jump.wav")
