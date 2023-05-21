import pygame
import random

# 初始化游戏
pygame.init()
fonts = pygame.font.get_fonts()
print(fonts)

# 游戏窗口大小
window_width = 800
window_height = 600

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 设置游戏窗口
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("snake game")

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义蛇和食物的大小
snake_block_size = 20
snake_speed = 10

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def show_score(score):
    score_text = score_font.render("score:" + str(score), True, white)
    window.blit(score_text, [10, 10])


def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, red, [x[0], x[1], snake_block_size, snake_block_size])


def game_loop():
    game_over = False
    game_close = False

    # 初始位置
    x1 = window_width / 2
    y1 = window_height / 2

    # 初始移动方向
    x1_change = 0
    y1_change = 0

    # 蛇的身体列表
    snake_list = []
    snake_length = 1

    # 随机生成食物的位置
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            game_over_text = font_style.render("game over!press q to exit,press c to restart", True, red)
            window.blit(game_over_text, [window_width / 2 - 200, window_height / 2])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -=snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change -=snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # 判断蛇是否超出边界
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        # 绘制食物
        pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])

        # 更新蛇的身体
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # 检查蛇是否碰到自己的身体
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 绘制蛇
        snake(snake_block_size, snake_list)

        # 显示得分
        show_score(snake_length - 1)

        # 更新游戏窗口
        pygame.display.update()

        # 检查蛇是否吃到食物
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            snake_length += 1

        # 控制游戏速度
        clock.tick(snake_speed)

    pygame.quit()


# 开始游戏循环
game_loop()
