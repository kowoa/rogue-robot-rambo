from enum import Enum

class ScoreType(Enum):
    # Death type enums for player
    FALL_DEATH = 1
    DEATH_BY_ENEMY = 2
    GENERIC_EVENT = 3
    NONE_TYPE = 4

class Score:
    def __init__(self, points=0, point_type=ScoreType.NONE_TYPE):
        self.points = points
        self.point_type = point_type


    def __str__(self):
        return "Points: {}, Score Type: {}".format(self.points, self.point_type)

    def __lt__(self, other):
        if self.getPoints() < other.getPoints():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.getPoints() > other.getPoints():
            return True
        else:
            return False

    def __add__(self, other):
        return Score(self.getPoints() + other.getPoints(), ScoreType.GENERIC_EVENT)

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
        self.high_score = 0
        self.total_points = 0

    def __str__(self):
        s = ""
        for scores in self.scores:
            s += str(scores) + "\n"
        return s

    def addScore(self, score):
        self.scores.append(score)
        self.total_points += score.getPoints()

    def getHighestScore(self):
        highest = 0
        for i in range(0, len(self.scores)-1):
            if self.scores[i].getPoints() < self.scores[i+1].getPoints():
                highest = self.scores[i+1].getPoints()
            else:
                highest = self.scores[i].getPoints()
        return highest

    # Reads the current score object list to determine total point values
    # Assigns the total number to self.total_points and then returns this value
    def getTotalPoints(self):
        self.total_points = sum([i.getPoints() for i in self.scores])
        return self.total_points

    def getScoreByIndex(self, index):
        if 0 <= index < len(self.scores):
            return self.scores[index]



if __name__ == '__main__':
    score = Score(10, ScoreType.FALL_DEATH)
    score2 = Score(20, ScoreType.FALL_DEATH)
    score3 = Score(5, ScoreType.FALL_DEATH)

    board = ScoreBoard([score, score2, score3])

    print(board)

    print(board.getHighestScore())

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

