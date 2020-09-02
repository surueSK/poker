import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((600, 500))    # 大きさ600*500の画面を生成
    pygame.display.set_caption("Poker")              # タイトルバーに表示する文字

    #while (1):
        #screen.fill((0,100,0))        # 画面を黒色(#000000)に塗りつぶし
        #pygame.display.update()     # 画面を更新
        ## イベント処理
        #for event in pygame.event.get():
            #if event.type == QUIT:  # 閉じるボタンが押されたら終了
                #pygame.quit()       # Pygameの終了(画面閉じられる)

                #sys.exit()

    #背景画像の取得
    bg = pygame.image.load("background.jpg")
    rect_bg = bg.get_rect()

    #コミュニティーカード1の画像の取得
    comCard1 = pygame.image.load("card.png").convert_alpha()
    rect_comCard1 = comCard1.get_rect()
    rect_comCard1.center = (,) #画像の初期位置

    #コミュニティーカード2の画像の取得
    comCard2 = pygame.image.load("card.png").convert_alpha()
    rect_comCard2 = rect_comCard2.get_rect()
    rect_comCard2.center = (,) #画像の初期位置

    #コミュニティーカード3の画像の取得
    comCard3 = pygame.image.load("card.png").convert_alpha()
    rect_comCard3 = comCard3.get_rect()
    rect_comCard3.center = (,) #画像の初期位置

    #コミュニティーカード4の画像の取得
    comCard4 = pygame.image.load("card.png").convert_alpha()
    rect_comCard4 = comCard1.get_rect()
    rect_comCard4.center = (,) #画像の初期位置

    #コミュニティーカード5の画像の取得
    comCard5 = pygame.image.load("card.png").convert_alpha()
    rect_comCard5 = comCard1.get_rect()
    rect_comCard5.center = (,) #画像の初期位置

    while(1):
        pygame.display.update() #画面更新
        screen.fill(0,100,0) #画面の背景色
        screen.blit(bg, rect_bg) #背景画像の描画
        screen.blit(comCard1, rect_comCard1)
        screen.blit(comCard2, rect_comCard2)
        screen.blit(comCard3, rect_comCard3)
        screen.blit(comCard4, rect_comCard4)
        screen.blit(comCard5, rect_comCard5) #コミュニティーカード画像の描画

        #終了用のイベント処理
        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
