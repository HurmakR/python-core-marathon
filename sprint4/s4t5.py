class Gallows:
    
    def __init__(self, game_over=False):
        self.words=[]
        self.game_over=game_over
        
        
    def play(self, word):
        if self.words:
            if word[0] == self.words[-1][-1] and word not in self.words:
                self.words.append(word)
                return self.words
            else:
                self.game_over = True
                
                return 'game over'    
                
        else:
            self.words.append(word)
            return self.words
    
    def restart(self):
        self.words=[]
        self.game_over = False
        return 'game restarted'