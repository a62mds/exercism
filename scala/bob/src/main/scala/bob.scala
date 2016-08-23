class Bob {

  def hey(greeting: String): String = {
    if (isYelled(greeting)) "Whoa, chill out!"
    else if (isQuestion(greeting)) "Sure."
    else if (isWhiteSpace(greeting)) "Fine. Be that way!"
    else "Whatever."
  }

  def isYelled(greeting: String): Boolean = {
    val hasLetter: Boolean = greeting.exists(_.isLetter) 
    val isAllCaps: Boolean = greeting.toUpperCase == greeting
    hasLetter && isAllCaps
  }

  def isQuestion(greeting: String): Boolean = greeting.endsWith("?")

  def isWhiteSpace(greeting: String): Boolean = greeting.trim.isEmpty

}
