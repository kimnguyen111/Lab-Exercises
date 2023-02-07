class KoreanDict:
  def __init__(self, koreanWord, englishWord):
    self.koreanWord = koreanWord
    self.englishWord = englishWord
    
  def englishToKorean(self, englishWord):
    print("The Korean word:", self.koreanWord)

  def koreanToEnglish(self, koreanWord):
    print("The English word:", self.englishWord)
    
card1 = KoreanDict("사랑해요","I love you")
card1.englishToKorean("I love you")
card1.koreanToEnglish("사랑해요")