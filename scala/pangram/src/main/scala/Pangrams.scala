object Pangrams {

  lazy val theAlphabet: String = "abcdefghijklmnopqrstuvwxyz"

  def isPangram(phrase: String): Boolean = {
    val phraseLetters: String = phrase.toLowerCase.filter(_.isLetter)
    theAlphabet.forall(phraseLetters.contains(_)) 
  }

}
