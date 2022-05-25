class Settings:
  	#A class to store all the settings for the game

  	def __init__(self):
  		#Initalise the game settings
  		#Screen settings
  		self.screen_width=1200
  		self.screen_height=800
  		self.bg_color=(220,220,220)

  		#Ship settings
  		self.ship_speed = 3
  		#Bullet settings
  		self.bullet_speed= 1.5
  		self.bullet_width = 20
  		self.bullet_height = 15
  		self.bullet_color = (60,60,60)
  		self.bullets_allowed = 3
  		self.ship_limit = 3
  		#Alien settings
  		self.alien_speed= 1.0
  		self.fleet_drop_speed=10
  		#Fleet_direction of 1 represents right; -1 represents left
  		self.fleet_direction = 1

  		#How quikcly game sppeds up
  		self.speedup_scale= 1.1

  		#How quickly the alien point values increase
  		self.score_scale= 1.5

  		self.initalize_dynamic_settings()

  	def initalize_dynamic_settings(self):
  		#Initalise settings that change through the game
  		self.ship_Speed= 1.5
  		self.bullet_speed= 1.5
  		self.bullet_speed= 3.0
  		self.alien_speed= 1.0

  		#Fleet_direction of 1 represents right; -1 represents left
  		self.fleet_direction= 1

  		#Scoring
  		self.alien_points= 50


  	def increase_speed(self):
  		#Increase speed settings
  		self.ship_speed*= self.speedup_scale
  		self.bullet_speed*= self.speedup_scale
  		self.alien_speed*= self.speedup_scale

  		self.alien_points= int(self.alien_points * self.score_scale)

