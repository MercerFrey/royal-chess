import pygame

from data.classes.Piece import Piece

class Knight(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'data/imgs/' + color[0] + '_knight.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

		self.notation = 'N'


	def get_possible_moves(self, board):
		output = []
		moves = [
			(1, -2),
			(2, -1),
			(2, 1),
			(1, 2),
			(-1, 2),
			(-2, 1),
			(-2, -1),
			(-1, -2)
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (
				new_pos[0] < 8 and
				new_pos[0] >= 0 and 
				new_pos[1] < 8 and 
				new_pos[1] >= 0
			):
				output.append([
					board.get_square_from_pos(
						new_pos
					)
				])
		output.append(self.king_moves(board))
		return output
	
	def king_moves(self, board):
		output = []
		moves = [
			(0,-1), # north
			(1, -1), # ne
			(1, 0), # east
			(1, 1), # se
			(0, 1), # south
			(-1, 1), # sw
			(-1, 0), # west
			(-1, -1), # nw
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (
				new_pos[0] < 8 and
				new_pos[0] >= 0 and 
				new_pos[1] < 8 and 
				new_pos[1] >= 0
			):
				square = board.get_square_from_pos(new_pos)
				if square.occupying_piece == None:
					output.append(square)
		return output
	