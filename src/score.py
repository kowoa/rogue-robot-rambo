from enum import Enum

class ScoreType(Enum):
    # Death type enums for player
    FALL_DEATH = 1
    DEATH_BY_ENEMY = 2
    GENERIC_EVENT = 3
    NONE_TYPE = 4

class Score:
    def __init__(self, player=Player(), points=0, point_type=ScoreType.NONE_TYPE):
        self.player = player
        self.points = points
        self.point_type = point_type

    def applyPoints(self, point_type=ScoreType.NONE_TYPE):
        if point_type == ScoreType.FALL_DEATH:
            self.points += 10
        elif point_type == ScoreType.DEATH_BY_ENEMY:
            self.points += 10
        elif point_type == ScoreType.GENERIC_EVENT:
            self.points += 5
        elif point_type == ScoreType.NONE_TYPE:
            self.points += 0
        else:
            print("Error: Invalid point type applied!!!")

    def getPlayer(self):
        return self.player

    def getPoints(self):
        return self.points

    def getPointType(self):
        return self.point_type

    def returnAll(self):
        return (self.player, self.points, self.death_type)


class ScoreBoard():
    def __init__(self, scores=[]):
        self.scores = scores
        self.total_points = 0

    def addScore(self, score):
        self.scores.append(score)
        self.total_points += score.getPoints()

    # Reads the current score object list to determine total point values
    # Assigns the total number to self.total_points and then returns this value
    def getTotalPoints(self):
        self.total_points = sum([i.getPoints() for i in self.scores])
        return self.total_points

    def getScoreByIndex(self, index):
        if 0 <= index < len(self.scores):
            return self.scores[index]
        
    
if __name__ == '__main__':
    score = Score(Player(), 10, ScoreType.FALL_DEATH)
    board = ScoreBoard([score])

    # Print the point value for this Score object
    print(score.getPoints())

    # Add a new score to the board, specifying only points for the Score object
    board.addScore(Score(points = 1337))
    
    # Assign points to the score object located at index 0 corresponding with event DEATH_BY_ENEMY 
    board.getScoreByIndex(0).applyPoints(ScoreType.DEATH_BY_ENEMY)

    # Print the points for the score object located at index 0
    print(board.getScoreByIndex(0).getPoints())

    # Print total number of points in board
    print(board.getTotalPoints())
