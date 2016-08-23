class Anagram(val mWord: String) {

  type Predicate[T] = T => Boolean

  lazy val lcWord: String = mWord.toLowerCase

  lazy val isPermutation: Predicate[String] =
    candWord => charCount(candWord.toLowerCase) == charCount(lcWord)
  lazy val isIdentical: Predicate[String] =
    candWord => candWord.toLowerCase == lcWord
  lazy val isAnagram: Predicate[String] =
    candWord => isPermutation(candWord) && !isIdentical(candWord)

  def matches(wordList: Seq[String]): Seq[String] = wordList.filter(isAnagram(_))

  def charCount(aWord: String): Map[Char,Int] = {
    aWord.foldLeft(Map[Char,Int]() withDefaultValue 0)((a,c) => a+(c->(a(c)+1)))
  }

}
