import scala.collection.mutable
import scala.util.Random.shuffle

object Robot {

  type Letter = Char
  type Digit = Char

  private val Letters: List[Letter] = ('A' to 'Z').toList
  private val Numbers: List[Digit] = ('0' to '9').toList

  private var nameDB = List[String]()

  private val namePat: String = "LLDDD"

  private val numNames: Int =
    namePat.foldLeft(1)((a,c) => c match {
      case 'L' => a * Letters.length
      case 'D' => a * Numbers.length
    })

  private def genName(numAttempts: Int): String = {
    require(numAttempts < numNames, "Name possibilities exhausted")
    val aName: String =
      namePat.foldLeft("")((a,c) => c match {
        case 'L' => a + shuffle(Letters).head.toString
        case 'D' => a + shuffle(Numbers).head.toString
      })
    if (nameDB.contains(aName)) genName(numAttempts + 1) else aName
  }

  def apply = {
    val newRobot = new Robot
    nameDB :+ newRobot.name
  }

}

class Robot {
  var name: String = Robot.genName(0)
  def reset(): Unit = { name = Robot.genName(0) }
}