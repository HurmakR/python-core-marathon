import math

class Testpaper:
    
    def __init__(self, subject, markscheme, pass_mark):
        self.subject=subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark

class Student:
    
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken=tests_taken
        
        
        
    def take_test(self, papers, marks):
        if self.tests_taken == 'No tests taken': self.tests_taken={}
        score=self.count_score(papers.markscheme, marks)
        if score > int(papers.pass_mark[:-1]):
            self.tests_taken[papers.subject]=f"Passed! ({score}%)"
        else:
            self.tests_taken[papers.subject]=f"Failed! ({score}%)"
    
    def count_score(self,paper, mark):
        return int(math.ceil(len(set(mark)&set(paper))/len(paper)*100))
