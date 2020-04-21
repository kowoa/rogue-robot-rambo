import sys
import pygame
from pygame.locals import *
import pymunk # import to use pymunk
import pymunk.pygame_util
import random


def add_ball(space):
    mass = 1
    radius = 14
    # All bodies must have moment of inertia set
    # Pymunk comes with moment_for_circle() method
    # so avoid manually selecting value for inertia for simplicity (unless required)
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)  # Body of ball
    x = random.randint(120, 380)
    body.position = (x, 550)  # Set random position for body
    # In order for ball to collide with things, it must have
    # at least one shape (circle in this case)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)  # Add body and shape to simulation
    return shape


def draw_ball(screen, ball):
    # screen is pygame.display.set_mode((x, y))
    # ball is pymunk.Circle() created in add_ball()
    # pos is conversion from pymunk coordinates to pygame coordinates
    pos = int(ball.body.position.x), 600-int(ball.body.position.y)
    # param: (surface, color, center, radius)
    pygame.draw.circle(screen, (0, 0, 255), pos, int(ball.radius), 2)

def add_static_L(space):
    # Static body is never added to space like dynamic ball bodies
    # Static bodies don't need mass or moment because forces don't affect them
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)  # segments
    l2 = pymunk.Segment(body, (-150, 0), (-150, 50), 5)
    # Add the segments to the space, not the body
    space.add(l1, l2)
    return l1, l2

def add_L(space):
    # rotation_center_body acts as static point in the joint so the line can rotate around it
    # We never add any shapes to it
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_limit_body.position = (200, 300)

    # The L-shape will now be moving and can no longer be a static body
    # Moment of inertia is set to 10000 because it just works
    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)
    l2 = pymunk.Segment(body, (-150, 0), (-150, 50), 5)

    # Pin joint allows two objects to pivot about a single point
    # In this case, one of the objects will be stuck to the world
    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0))
    joint_limit = 25
    # Slide joints behave like pin joints but have a min and max distance
    # The two bodies can slide between the min and max
    # In this case, one of the bodies is static, meaning only the body attached with the shapes will move
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100, 0), (0, 0), 0, joint_limit)

    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1, l2

def to_pygame(pos):
    # Converts coordinates from pymunk to pygame
    # Flip the y-coordinate (-p.y) and offset it with screen height (+SCREEN_HEIGHT)
    return int(pos.x), int(-pos.y + 600)
    # We could have used this method in draw_ball()


def draw_lines(screen, lines):
    for line in lines:
        body = line.body
        # Get position with line rotation using this calculation
        # line.a is first endpoint of line, line.b the second
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, (128, 128, 128), False, [p1, p2])

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()  # space with gravity
    space.gravity = (0.0, -900.0)  # (x-gravity, y-gravity)

    # Create 5 balls and add them to space
    balls = []
    for i in range(0, 5):
        ball = add_ball(space)
        balls.append(ball)

    # Create L-shape
    l_shape = add_L(space)

    # See below for info
    # >> draw_options = pymunk.pygame_util.DrawOptions(screen)

    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        screen.fill((255, 255, 255))
        space.step(1/50.0)  # Steps simulation forward
        # NOTE: avoid adjusting timestep based on FPS
        # simulation will work much better
        # Fixed timestep: game goes slow motion low FPS
        # FPS-dependent timestep: game changes speed based on FPS

        # Creates new ball every 25 ticks
        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        # Draw all 5 balls at beginning of simulation
        for ball in balls:
            draw_ball(screen, ball)

        draw_lines(screen, l_shape)

        # Remove balls for performance
        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y < 0:
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            # To remove an object from the space, remove its shape AND body
            space.remove(ball, ball.body)
            balls.remove(ball)

        # See below for info
        # >> space.debug_draw(draw_options)

        # There is another way to draw shapes:
        # Declare this before loop:
        # >> draw_options = pymunk.pygame_util.DrawOptions(screen)
        # Then put this inside loop:
        # >> space.debug_draw(draw_options)
        # However, pymunk.pygame_util is inefficient and should only be used for testing


        pygame.display.flip()
        clock.tick(50)


if __name__ == "__main__":
    sys.exit(main())