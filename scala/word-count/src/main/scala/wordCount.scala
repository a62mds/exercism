class Phrase(val phrase: String) {
  val wordList: Array[String] =
    phrase.toLowerCase().split("""[^\w']+""")
  def wordCount: Map[String,Int] = {
    def wordCountAcc(words: Array[String], acc: Map[String,Int]): Map[String,Int] = {
      if (words.isEmpty)
        acc
      else if (acc.contains(words.head))
        wordCountAcc(words.tail, acc + (words.head -> (acc(words.head) + 1)))
      else
        wordCountAcc(words.tail, acc + (words.head -> 1))
    }
    wordCountAcc(wordList, Map())
  }
}

