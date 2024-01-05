import pygame
import sys

# 初始化Pygame
pygame.init()

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 設定視窗尺寸
WIDTH, HEIGHT = 800, 600

# 創建視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("移動方塊小遊戲")

# 初始化方塊
player_size = 50
player_x = (WIDTH - player_size) // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

clock = pygame.time.Clock()

# 遊戲主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # 清除畫面
    screen.fill(BLACK)

    # 繪製方塊
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲更新速率
    clock.tick(60)

