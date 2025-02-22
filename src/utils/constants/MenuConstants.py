import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DISTANCE_BEETWEEN_BUTTONS = 100

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initial puck speed
INITIAL_PUCK_SPEED = 15

# Epsilon for collision (error margin)
EPSILON = 3

# Puck margins
TABLE_SIDE_WALLS = 55
TABLE_TOP_WALLS = 92
MARGINS = (TABLE_SIDE_WALLS, SCREEN_WIDTH - TABLE_SIDE_WALLS,	
		   TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)

# After goal for player two, puck starts from player one
POSITION_PUCK_PLAYER_ONE = (SCREEN_WIDTH / 4 - 40, SCREEN_HEIGHT / 2)

# After goal for player one, puck starts from player two
POSITION_PUCK_PLAYER_TWO = (3 * SCREEN_WIDTH / 4 + 40, SCREEN_HEIGHT / 2)

# Gates dimensions for the map
GOAL_HEIGHT = 200
GOAL_TOP = (SCREEN_HEIGHT - GOAL_HEIGHT) // 2
GOAL_BOTTOM = GOAL_TOP + GOAL_HEIGHT

# Positions for the gates
GATE_LEFT_POSITION = (TABLE_SIDE_WALLS - 10, GOAL_TOP + GOAL_HEIGHT // 2)
GATE_RIGHT_POSITION = (SCREEN_WIDTH - TABLE_SIDE_WALLS + 10, GOAL_TOP + GOAL_HEIGHT // 2)

# Initial paddle speed
INITIAL_PADDLE_SPEED = 7

# Starting point for the paddles
DISTANCE_FROM_CENTER = 500

# Paddle margins
TABLE_SIDE_WALLS = 105
TABLE_TOP_WALLS = 140
PADDLE_CENTER_MARGIN = 57
MARGINS_ONE = (TABLE_SIDE_WALLS, SCREEN_WIDTH / 2 - PADDLE_CENTER_MARGIN,
               TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)
MARGINS_TWO = (SCREEN_WIDTH / 2 + PADDLE_CENTER_MARGIN, SCREEN_WIDTH - TABLE_SIDE_WALLS,
               TABLE_TOP_WALLS, SCREEN_HEIGHT - TABLE_TOP_WALLS)



__all__ = ['SCREEN_WIDTH', 'SCREEN_HEIGHT', 'GOAL_HEIGHT', 'GOAL_TOP', 'GOAL_BOTTOM',
           'DISTANCE_BEETWEEN_BUTTONS', 'INITIAL_PUCK_SPEED', 'TABLE_SIDE_WALLS', 'TABLE_TOP_WALLS',
           'MARGINS', 'SCREEN', 'INITIAL_PADDLE_SPEED', 'DISTANCE_FROM_CENTER', 'PADDLE_CENTER_MARGIN',
           'MARGINS_ONE', 'MARGINS_TWO', 'EPSILON', 'POSITION_PUCK_PLAYER_ONE', 'POSITION_PUCK_PLAYER_TWO',
           'GATE_LEFT_POSITION', 'GATE_RIGHT_POSITION']
