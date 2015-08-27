#!/usr/bin/python
#coding:utf8
'''
Created on 2015年8月24日

@author: Kenny.Li
'''
import wx
import random
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,title="Game",size=(500,400),style=wx.MINIMIZE_BOX|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.CAPTION)
        
        scissors_image = wx.Image('scissors.gif', wx.BITMAP_TYPE_GIF)
        self.temp_scissors = scissors_image.ConvertToBitmap()
        rock_image = wx.Image('rock.gif', wx.BITMAP_TYPE_GIF)
        self.temp_rock = rock_image.ConvertToBitmap()
        paper_image = wx.Image('paper.gif', wx.BITMAP_TYPE_GIF)
        self.temp_paper = paper_image.ConvertToBitmap()
#         self.temp_paper.
        
        win_image = wx.Image("win.jpg",wx.BITMAP_TYPE_JPEG)
        self.temp_win = win_image.ConvertToBitmap()
        lose_image = wx.Image("lose.jpg",wx.BITMAP_TYPE_JPEG)
        self.temp_lose = lose_image.ConvertToBitmap()
        dogfall_image = wx.Image("dogfall.jpg",wx.BITMAP_TYPE_JPEG)
        self.temp_dogfall = dogfall_image.ConvertToBitmap()
#         self.temp_dogfall.
        
        self.panel_main = wx.Panel(frame,size=frame.GetSize())
        self.panel_main.SetBackgroundColour("white")
#         self.panel_main.SetForegroundColour("white")
#         self.panel_main.SetBackgroundColour("white")
        
        self.panel_com_scissors = wx.Panel(frame,size=(self.temp_scissors.GetWidth(), self.temp_scissors.GetHeight()),pos=(self.temp_scissors.GetWidth()+180,30))
        self.panel_com_rock = wx.Panel(frame,size=(self.temp_scissors.GetWidth(), self.temp_scissors.GetHeight()),pos=(self.temp_scissors.GetWidth()+180,30))
        self.panel_com_paper = wx.Panel(frame,size=(self.temp_scissors.GetWidth(), self.temp_scissors.GetHeight()),pos=(self.temp_scissors.GetWidth()+180,30))
        
        self.panel_player_scissors = wx.Panel(frame,size = (self.temp_scissors.GetWidth(), self.temp_scissors.GetHeight()) ,pos=(60,30))
        self.panel_player_rock = wx.Panel(frame,size = (self.temp_rock.GetWidth(), self.temp_rock.GetHeight()) ,pos=(60,30))
        self.panel_player_paper = wx.Panel(frame,size = (self.temp_paper.GetWidth(), self.temp_paper.GetHeight()) ,pos=(60,30))
        
        bmp_scissors_1 = wx.Image("scissors_1.gif", wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        bmp_rock_1 = wx.Image("rock_1.gif", wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        bmp_paper_1 = wx.Image("paper_1.gif", wx.BITMAP_TYPE_GIF).ConvertToBitmap()
        
        scissors_button = wx.BitmapButton(self.panel_main,-1, bmp_scissors_1,size=(50,50),pos=(30,300),style=wx.BU_AUTODRAW)
        rock_button = wx.BitmapButton(self.panel_main,-1, bmp_rock_1,size=(50,50),pos=(100,300))
        paper_button = wx.BitmapButton(self.panel_main,-1, bmp_paper_1,size=(50,50),pos=(170,300))
        
        scissors_button.Bind(wx.EVT_BUTTON, self.scissors_button_press)
        rock_button.Bind(wx.EVT_BUTTON, self.rock_button_press)
        paper_button.Bind(wx.EVT_BUTTON, self.paper_button_press)
        
        self.panel_player_result = wx.Panel(frame,size =(self.temp_win.GetWidth(),self.temp_win.GetHeight()),pos =(85,170))
        self.panel_com_result = wx.Panel(frame,size =(self.temp_win.GetWidth(),self.temp_win.GetHeight()),pos =(335,170))
        
        self.win_play = 0
        self.lose_play = 0
        self.dogfall_play = 0
        self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
        self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
        frame.Show()
        
        return 1
    def Start(self,flag):
        choice = random.randint(0,2)
        if choice == 0:
            self.panel_com_rock.Show(False)
            self.panel_com_paper.Show(False)
            self.panel_com_scissors.Show(True)
            self.bmp = wx.StaticBitmap(parent=self.panel_com_scissors, bitmap=self.temp_scissors)
            if flag == 0:
                self.dogfall_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_dogfall)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_dogfall)
                
            elif flag ==1:
                self.win_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_win)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_lose)
            elif flag == 2:
                self.lose_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_lose)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_win)
        elif choice == 1:
            self.panel_com_rock.Show(True)
            self.panel_com_paper.Show(False)
            self.panel_com_scissors.Show(False)
            self.bmp = wx.StaticBitmap(parent=self.panel_com_rock, bitmap=self.temp_rock)
            if flag == 0:
                self.lose_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_lose)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_win)
            elif flag ==1:
                self.dogfall_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_dogfall)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_dogfall)
            elif flag == 2:
                self.win_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_win)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_lose)
                
        elif choice == 2:
            self.panel_com_rock.Show(False)
            self.panel_com_scissors.Show(False)
            self.panel_com_paper.Show(True)
            self.bmp = wx.StaticBitmap(parent=self.panel_com_paper, bitmap=self.temp_paper)
            if flag == 0:
                self.win_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_win)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_lose)
            elif flag ==1:
                self.lose_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_lose)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_win)
            elif flag == 2:
                self.dogfall_play += 1
                self.result_play = wx.StaticText(self.panel_main,size = (150,20),pos=(87,260),label=u"胜:%d 负:%d 平:%d"%(self.win_play,self.lose_play,self.dogfall_play))
                self.result_com = wx.StaticText(self.panel_main,size = (150,20),pos=(337,260),label=u"胜:%d 负:%d 平:%d"%(self.lose_play,self.win_play,self.dogfall_play))
                self.bmp = wx.StaticBitmap(parent=self.panel_player_result,bitmap=self.temp_dogfall)
                self.bmp = wx.StaticBitmap(parent=self.panel_com_result,bitmap=self.temp_dogfall)
        
            
            
    def scissors_button_press(self,evt):
        self.panel_player_rock.Show(False)
        self.panel_player_paper.Show(False)
        self.bmp = wx.StaticBitmap(parent=self.panel_player_scissors, bitmap=self.temp_scissors)
        self.panel_player_scissors.Show(True) 
        self.Start(0)
        
    def rock_button_press(self,evt):
        self.panel_player_paper.Show(False)
        self.panel_player_scissors.Show(False)
        self.bmp = wx.StaticBitmap(parent=self.panel_player_rock, bitmap=self.temp_rock) 
        self.panel_player_rock.Show(True) 
        self.Start(1)
        
    def paper_button_press(self,evt):
        self.panel_player_rock.Show(False)
        self.panel_player_scissors.Show(False)
        self.bmp = wx.StaticBitmap(parent=self.panel_player_paper, bitmap=self.temp_paper) 
        self.panel_player_paper.Show(True) 
        self.Start(2)
        
        
        
        
app = MyApp()
app.MainLoop()
