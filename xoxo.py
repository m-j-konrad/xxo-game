#!/bin/python3
# -*- coding:utf-8 -*-
# PYTHON 3 ONLY

from tkinter import *
import tkinter.messagebox
from pathlib import Path


# determine the path of the script - useful if the script is running from another directory
script_path = Path(__file__).resolve().parent

# configuration variables
cfg_fullscreen = False
cfg_screen_resolution = "720x480"
cfg_mouse_cursor_visible = True
cfg_assets_folder = Path(script_path/"assets/") # with "path()" it's compatible with Linux,Mac,Windows
cfg_picture_x = "x.png"
cfg_picture_o = "o.png"
cfg_picture_button_bg = "empty.png"


class XOXO:
	print("create an empty game field...")
	game_field = [" "," "," "," "," "," "," "," "," "]
	actual_player = "X"
	print("Active Player is »X«.")
	
	buttons = [0 for x in range(10)]
	
	label_actual_player = None
	pic_x = None
	pic_o = None
	pic_empty = None
	
	####################################################################
	def __init__(self):
		root = Tk()
		root.title("XOXO")
		root.geometry(cfg_screen_resolution)
		
		if cfg_fullscreen: root.attributes("-fullscreen", True)
		if not cfg_mouse_cursor_visible: root.config(cursor="none")
		
		self.pic_x = PhotoImage(file = cfg_assets_folder/cfg_picture_x)
		self.pic_o = PhotoImage(file = cfg_assets_folder/cfg_picture_o)
		self.pic_empty = PhotoImage(file = cfg_assets_folder/cfg_picture_button_bg)
		
		print("Main window was created.")
		
		buttonRestart = Button(root,
		                       text="restart game",
		                       fg="black",
		                       bg="yellow",
		                       command=self.restart_game)
		                       
		buttonQuit = Button(root,
		                    text="quit game",
		                    fg="black",
		                    bg="red",
		                    command=self.quit_game)
		
		for i in range(10):
			self.buttons[i] = Button(root,
			                         image = self.pic_empty,
			                         command=lambda c=i: self.button_action(c))
		
		self.label_actual_player = Label(root, text="»X« is playing.")
		
		print("Buttons and Label were created.")
		
		self.buttons[0].place(x=20,  y=20,  width=120, height=120)
		self.buttons[1].place(x=180, y=20,  width=120, height=120)
		self.buttons[2].place(x=340, y=20,  width=120, height=120)
		self.buttons[3].place(x=20,  y=180, width=120, height=120)
		self.buttons[4].place(x=180, y=180, width=120, height=120)
		self.buttons[5].place(x=340, y=180, width=120, height=120)
		self.buttons[6].place(x=20,  y=340, width=120, height=120)
		self.buttons[7].place(x=180, y=340, width=120, height=120)
		self.buttons[8].place(x=340, y=340, width=120, height=120)
		buttonRestart.place(x=540, y=260, width=160, height=100)
		buttonQuit.place(x=540, y=380, width=160, height=80)
		self.label_actual_player.place(x=540, y=50)
		print("Buttons were placed.")
		
		print("mainloop() will start now...")
		root.mainloop()
	
	
	####################################################################
	def button_action(self, i):
		print("Button ",i," was clicked.")
		if self.game_field[i] == " ":
			if self.actual_player == "X":
				print("Picture of button",i,"will be set to »X«...")
				self.buttons[i].configure(image=self.pic_x)
			else:
				print("Picture of button",i,"will be set to »Y«...")
				self.buttons[i].configure(image=self.pic_o)
			
			self.game_field[i] = self.actual_player
			
			if self.checkForWin() == True:
				tkinter.messagebox.showinfo(message="»"+self.actual_player+"« won the game!")
				self.restart_game()
			
			self.change_player()
	
	
	####################################################################
	def change_player(self):
		print("Changing active player...")
		if self.actual_player=="X":
			self.actual_player="O"
		else:
			self.actual_player="X"
		
		self.label_actual_player.config(text="Now »"+self.actual_player+"« is playing.")
		print("Active player is now »",self.actual_player,"«.")
	
	
	####################################################################
	def restart_game(self):
		print("RESET GAME...")
		for i in range(9):
			print("Button[",i,"] will be reset...")
			self.buttons[i].configure(image=self.pic_empty)
		print("Empty game field...")
		self.game_field = [" "," "," "," "," "," "," "," "," ",]
		self.change_player()
	
	
	####################################################################
	def quit_game(self):
		print("Aks for quit the game...")
		if True: #tkinter.messagebox.askyesno("Quit Game", "Do you really want to leave?"):
			print("Quit game now...")
			quit(0)
		else:
			print("Das Programm wurde nicht beendet.")
	
	
	####################################################################
	def checkForWin(self):
		win = False
		c = self.actual_player
		print("Checking if »",c,"« won...")
		if (
		   ((self.game_field[0]==c) and (self.game_field[1]==c) and (self.game_field[2]==c)) or
		   ((self.game_field[3]==c) and (self.game_field[4]==c) and (self.game_field[5]==c)) or
		   ((self.game_field[6]==c) and (self.game_field[7]==c) and (self.game_field[8]==c)) or
		   ((self.game_field[0]==c) and (self.game_field[3]==c) and (self.game_field[6]==c)) or
		   ((self.game_field[1]==c) and (self.game_field[4]==c) and (self.game_field[7]==c)) or
		   ((self.game_field[2]==c) and (self.game_field[5]==c) and (self.game_field[8]==c)) or
		   ((self.game_field[0]==c) and (self.game_field[4]==c) and (self.game_field[8]==c)) or
		   ((self.game_field[2]==c) and (self.game_field[4]==c) and (self.game_field[6]==c))
		   ): win = True
		else: win = False
		
		print(c)
		print(self.game_field)
		
		return win


XOXO()

print("Quit game now (main windows was closed)...")
quit(0)
